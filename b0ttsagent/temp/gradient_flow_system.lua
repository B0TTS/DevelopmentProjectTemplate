--[[
================================================================================
  b0ttsagent/temp/gradient_flow_system.lua
  Infinite flowing UIGradient animation — built for high object counts.
================================================================================

  STRATEGY & WHY (read me)
  --------------------------------------------------------------------------------
  Goal: animate a UIGradient so its colors flow infinitely, scaled to thousands
  of simultaneous gradients at up to 240Hz+, with near-zero per-frame cost.

  The naive approach — rebuilding a ColorSequence every frame per gradient —
  allocates 7+ objects per gradient per frame. At 1000 gradients x 60fps that's
  ~60k ColorSequences/sec and ~420k keypoint allocations/sec. The GC destroys
  your frame budget. So every decision below exists to kill allocations and
  per-object connections in the hot path.

  DECISIONS (each resolved to keep the hot path allocation-free & single-threaded):

  1. COLOR-FLOW VIA KEYFRAME SHIFT
     The gradient starts AND ends on red (1,0,0) → it is a closed loop. We
     "flow" by shifting every keypoint's TIME by a phase p (mod 1) and wrapping.
     As p advances 0→1 the rainbow slides seamlessly and repeats forever.
     Chosen because it is the only truly seamless + infinite option for this
     gradient (Offset-pan clamps at edges; Rotation spins, doesn't flow).

  2. PRECOMPUTED PHASE LUT (the core performance win)
     Build ONCE, at init, an array LUT[1..N] of ready ColorSequence objects,
     one per phase p = 0, 1/N, 2/N, ..., (N-1)/N. At runtime the hot path is:
         Gradient.Color = LUT[idx]
     — a single table index + one property set. ZERO construction, ZERO
     allocation in the hot path. All gradients share the one table. Memory is
     paid once (~N * 8 keypoints * tiny userdata ≈ a few hundred KB).

  3. N IS DECOUPLED FROM REFRESH RATE (built into the logic)
     N = "max distinct phases per cycle", NOT a Hz lock. Motion advances by
     real delta-time (phase += dt * speed), and the index wraps with modulo:
         idx = floor(phase * N) % N
     So the SAME table serves 60/144/240Hz with no rebuild. A 240Hz monitor
     just samples the table more often (smoother), never more expensively.
     Default N=240; bump it for technically-lossless 240Hz on fast cycles.

  4. CONFIGURABLE CYCLE SPEED (live, seamless)
     speed = 1 / CycleSeconds. We read CycleSeconds fresh every frame, so
     changing it mid-flight just changes the rate — no jump, no restart.
     Default 5s per cycle.

  5. PER-GRADIENT PHASE OFFSET (coherent waves, one global knob)
     Each gradient stores an offset; effective phase = (globalPhase + offset)%1.
     Global phase advances once per frame for ALL gradients (one knob for speed),
     while offsets create a traveling wave across the set. Default offset spreads
     a uniform wave (repeating every DEFAULT_WAVE gradients); override per
     instance for random/organic or lockstep (offset = 0).

  6. SINGLE SHARED RenderStepped LOOP (the scalability lever)
     The module owns ONE RunService.RenderStepped connection, always — whether
     you have 1 or 10,000 gradients. It iterates flat arrays and does one
     property set per active gradient. No per-gradient connections, no held
     closures, no per-object callback dispatch. Auto-pauses (disconnects) when
     the set empties; reconnects lazily on next Register.

  7. PARALLEL PRIMITIVE ARRAY STORAGE
     gradients[], offsets[], paused[], frozenPhase[], handles[] are separate
     flat arrays indexed identically. The hot loop reads primitives (no
     per-entry table deref for animation data). Handles exist only for the
     external API and are touched on Register/Unregister/Pause/Resume (rare).

  8. LAZY SWAP-POP CLEANUP (no per-object connections)
     Each frame the loop cheaply checks Gradient.Parent == nil for entries it
     touches anyway. A destroyed/unparented gradient is removed via O(1)
     swap-pop (last element moves into the dead slot, array shrinks). The
     displaced handle's index is updated. Leaks are impossible: anything
     Destroy()'d is gone next frame with no caller action. Explicit
     handle:Unregister() also available for deterministic removal.

  9. INDIVIDUAL PAUSE/RESUME (free, even a perf win)
     Pause captures the current effective phase into frozenPhase and flags the
     entry paused. The loop then SKIPS it (no property set) — paused gradients
     cost only the Parent nil-check. Resume recomputes that gradient's offset
     so (globalPhase + offset) % 1 == frozenPhase → it picks up EXACTLY where
     it froze, no visible jump, even though the global clock kept running.
     Pausing half your gradients halves the per-frame work.

  HOT-PATH COST PER ACTIVE GRADIENT PER FRAME:
     1 nil-check (Parent) + 1 add + 1 modulo + 1 multiply + 1 floor + 1 modulo
     + 1 array index + 1 property set. No allocation. No connection dispatch.
     At 1000 gradients this loop is a fraction of a millisecond at 240Hz.

  CAVEAT: register gradients AFTER parenting them (or call handle:Unregister()
  when done). The auto-cleanup uses Parent == nil as the "destroyed" signal, so
  an intentionally-unparented gradient would be reaped next frame.
================================================================================
]]

local RunService = game:GetService("RunService")

--== CONFIG (tune freely) ======================================================
local N                  = 240    -- LUT granularity: distinct phases per cycle.
                                  --   Decoupled from Hz. Bump to 480/960 for
                                  --   technically-lossless 240Hz on fast cycles.
local DEFAULT_CYCLE_SEC  = 5      -- seconds for one full rainbow to flow past.
local DEFAULT_WAVE       = 8      -- default offset wave period (gradients per
                                  --   full wave). Override per-instance.
local EPS                = 1e-6   -- keypoint-time dedup tolerance (build only).

--== BASE GRADIENT (your colors, red-looped => seamless) =======================
local BASE_KEYS = {
	{ 0.0000000000000000, Color3.new(1, 0, 0) },
	{ 0.1510416716337204, Color3.new(0.615686297416687, 0, 1) },
	{ 0.3072916567325592, Color3.new(0.06666667014360428, 0, 1) },
	{ 0.4965277910232544, Color3.new(0, 1, 1) },
	{ 0.6649305820465088, Color3.new(0.01568627543747425, 1, 0) },
	{ 0.8385416865348816, Color3.new(1, 1, 0) },
	{ 1.0000000000000000, Color3.new(1, 0, 0) },
}

--== MODULE STATE (single shared controller) ===================================
local LUT          = {}      -- [1..N] = ColorSequence, built once
local gradients    = {}      -- parallel primitive arrays
local offsets      = {}
local paused       = {}
local frozenPhase  = {}
local handles      = {}
local count        = 0
local globalPhase  = 0       -- [0,1), advances once per frame for ALL gradients
local cycleSeconds = DEFAULT_CYCLE_SEC
local connection   = nil     -- the ONE RenderStepped connection

--== LUT BUILD (runs once at init) =============================================
-- Linear-interp sample of the base keypoint set at time t in [0,1].
local function sampleAt(kps, t)
	if t <= kps[1][1] then return kps[1][2] end
	if t >= kps[#kps][1] then return kps[#kps][2] end
	for i = 1, #kps - 1 do
		local a, b = kps[i], kps[i + 1]
		if t >= a[1] and t <= b[1] then
			local f = (t - a[1]) / (b[1] - a[1])
			local ca, cb = a[2], b[2]
			return Color3.new(
				ca.R + (cb.R - ca.R) * f,
				ca.G + (cb.G - ca.G) * f,
				ca.B + (cb.B - ca.B) * f
			)
		end
	end
	return kps[#kps][2]
end

-- Build ONE ColorSequence for phase p in [0,1).
-- Convention: color at position x = base color at ((x - p) mod 1).
--   => as p increases, colors flow RIGHT. Seamless because base(0)==base(1)==red.
-- Interior keypoints sit at x = (t_k + p) mod 1; endpoints carry the seam color
-- base((1 - p) mod 1) so x=0 and x=1 match. Near-equal times are de-duped.
local function buildEntryAtPhase(kps, p)
	local seam = sampleAt(kps, (1 - p) % 1)
	local raw = {}
	for _, kp in ipairs(kps) do
		local x = (kp[1] + p) % 1
		if x > EPS and x < 1 - EPS then
			table.insert(raw, { time = x, color = kp[2] })
		end
	end
	table.sort(raw, function(a, b) return a.time < b.time end)

	local pts = { ColorSequenceKeypoint.new(0, seam) }
	for _, r in ipairs(raw) do
		local last = pts[#pts]
		if (r.time - last.Time) >= EPS then
			table.insert(pts, ColorSequenceKeypoint.new(r.time, r.color))
		end
	end
	table.insert(pts, ColorSequenceKeypoint.new(1, seam))
	return ColorSequence.new(pts)
end

local function buildLUT()
	table.clear(LUT)
	for i = 0, N - 1 do
		LUT[i + 1] = buildEntryAtPhase(BASE_KEYS, i / N)
	end
end

--== CONNECTION MANAGEMENT =====================================================
local function ensureConnected()
	if not connection then
		connection = RunService.RenderStepped:Connect(function(dt)
			-- advance the single global clock (one knob controls all speeds)
			globalPhase = (globalPhase + dt * (1 / cycleSeconds)) % 1

			local i = 1
			while i <= count do
				local g = gradients[i]
				-- LAZY CLEANUP: destroyed/unparented => O(1) swap-pop, no leak
				if g.Parent == nil then
					local hRemoved = handles[i]
					if hRemoved then hRemoved.IsValid = false end
					if i == count then
						gradients[i] = nil; offsets[i] = nil; paused[i] = nil
						frozenPhase[i] = nil; handles[i] = nil
					else
						local last = count
						gradients[i] = gradients[last]; offsets[i] = offsets[last]
						paused[i] = paused[last]; frozenPhase[i] = frozenPhase[last]
						handles[i] = handles[last]
						if handles[i] then handles[i].index = i end
						gradients[last] = nil; offsets[last] = nil; paused[last] = nil
						frozenPhase[last] = nil; handles[last] = nil
					end
					count -= 1
					if count == 0 then
						if connection then connection:Disconnect(); connection = nil end
						return
					end
					-- do NOT increment i: recheck the swapped-in element
				else
					if not paused[i] then
						local phase = (globalPhase + offsets[i]) % 1
						local idx = math.floor(phase * N) % N
						g.Color = LUT[idx + 1]
					end
					-- paused entries: skip the property set (frozen, zero work)
					i += 1
				end
			end
		end)
	end
end

--== HANDLE (per-gradient API) =================================================
local HandleMt = {}
HandleMt.__index = function(t, k)
	if k == "Paused" then return paused[t.index] or false end
	if k == "Offset" then return offsets[t.index] or 0 end
	if k == "IsValid" then return rawget(t, "IsValid") end
	return HandleMt[k]
end
HandleMt.__newindex = function(t, k, v)
	if k == "Paused" then
		if v then t:Pause() else t:Resume() end
	elseif k == "Offset" then
		t:SetOffset(v)
	end
end

function HandleMt:Pause()
	if not self.IsValid then return end
	local i = self.index
	if not paused[i] then
		-- freeze at the exact color currently shown (seamless)
		frozenPhase[i] = (globalPhase + offsets[i]) % 1
		paused[i] = true
	end
end

function HandleMt:Resume()
	if not self.IsValid then return end
	local i = self.index
	if paused[i] then
		-- recompute offset so we resume at the frozen phase (no jump)
		offsets[i] = (frozenPhase[i] - globalPhase) % 1
		paused[i] = false
	end
end

function HandleMt:Toggle()
	if not self.IsValid then return end
	if paused[self.index] then self:Resume() else self:Pause() end
end

function HandleMt:SetOffset(newOffset)
	if not self.IsValid then return end
	newOffset = (tonumber(newOffset) or 0) % 1
	local i = self.index
	offsets[i] = newOffset
	if paused[i] then
		-- reposition the frozen visual immediately to the new offset
		frozenPhase[i] = (globalPhase + newOffset) % 1
		local idx = math.floor(frozenPhase[i] * N) % N
		gradients[i].Color = LUT[idx + 1]
	end
end

function HandleMt:Unregister()
	if not self.IsValid then return end
	local i = self.index
	self.IsValid = false
	if i == count then
		gradients[i] = nil; offsets[i] = nil; paused[i] = nil
		frozenPhase[i] = nil; handles[i] = nil
	else
		local last = count
		gradients[i] = gradients[last]; offsets[i] = offsets[last]
		paused[i] = paused[last]; frozenPhase[i] = frozenPhase[last]
		handles[i] = handles[last]
		if handles[i] then handles[i].index = i end
		gradients[last] = nil; offsets[last] = nil; paused[last] = nil
		frozenPhase[last] = nil; handles[last] = nil
	end
	count -= 1
	if count == 0 and connection then
		connection:Disconnect(); connection = nil
	end
end

--== CONTROLLER API ============================================================
local function register(gradient, offsetOverride)
	assert(gradient and gradient.IsA and gradient:IsA("UIGradient"),
		"GradientFlow.Register: expected a UIGradient")
	count += 1
	local idx = count
	local off = (offsetOverride ~= nil)
		and ((tonumber(offsetOverride) or 0) % 1)
		or  (((idx - 1) % DEFAULT_WAVE) / DEFAULT_WAVE)  -- uniform wave default
	gradients[idx] = gradient
	offsets[idx] = off
	paused[idx] = false
	frozenPhase[idx] = 0
	local handle = setmetatable({ index = idx, Gradient = gradient, IsValid = true }, HandleMt)
	handles[idx] = handle
	ensureConnected()
	return handle
end

local Controller = setmetatable({
	Register = register,

	UnregisterAll = function()
		for i = 1, count do
			local h = handles[i]
			if h then h.IsValid = false end
			gradients[i] = nil; offsets[i] = nil; paused[i] = nil
			frozenPhase[i] = nil; handles[i] = nil
		end
		count = 0
		if connection then connection:Disconnect(); connection = nil end
	end,

	PauseAll = function()
		for i = 1, count do
			if not paused[i] then
				frozenPhase[i] = (globalPhase + offsets[i]) % 1
				paused[i] = true
			end
		end
	end,

	ResumeAll = function()
		for i = 1, count do
			if paused[i] then
				offsets[i] = (frozenPhase[i] - globalPhase) % 1
				paused[i] = false
			end
		end
	end,
}, {
	__index = function(_, k)
		if k == "CycleSeconds" then return cycleSeconds end
		if k == "Count"        then return count end
		if k == "N"            then return N end
		if k == "IsRunning"    then return connection ~= nil end
		return nil
	end,
	__newindex = function(_, k, v)
		if k == "CycleSeconds" then
			cycleSeconds = math.max(1e-3, tonumber(v) or cycleSeconds)
		end
	end,
})

-- build the LUT once at module load
buildLUT()

return Controller

--[[
================================================================================
  USAGE
================================================================================
  -- 1) Your gradient factory (unchanged from your snippet):
  local function makeGradient()
      local g = Instance.new("UIGradient")
      g.Color = ColorSequence.new({
          ColorSequenceKeypoint.new(0, Color3.new(1, 0, 0)),
          ColorSequenceKeypoint.new(0.1510416716337204, Color3.new(0.615686297416687, 0, 1)),
          ColorSequenceKeypoint.new(0.3072916567325592, Color3.new(0.06666667014360428, 0, 1)),
          ColorSequenceKeypoint.new(0.4965277910232544, Color3.new(0, 1, 1)),
          ColorSequenceKeypoint.new(0.6649305820465088, Color3.new(0.01568627543747425, 1, 0)),
          ColorSequenceKeypoint.new(0.8385416865348816, Color3.new(1, 1, 0)),
          ColorSequenceKeypoint.new(1, Color3.new(1, 0, 0)),
      })
      return g
  end

  local GradientFlow = require(script.GradientFlow)  -- this module

  -- 2) Create + PARENT + register (parent before registering!):
  local grad = makeGradient()
  grad.Parent = someFrameOrLabel   -- IMPORTANT: parent first
  local handle = GradientFlow.Register(grad)
  --     optional: GradientFlow.Register(grad, 0.37)  -- custom phase offset
  --               GradientFlow.Register(grad, 0)     -- lockstep with others

  -- 3) Tuning (live, seamless):
  GradientFlow.CycleSeconds = 3      -- speed up / slow down anytime
  -- GradientFlow.CycleSeconds = 8   -- calm ambient

  -- 4) Individual pause / resume / toggle:
  handle:Pause()
  task.wait(2)
  handle:Resume()        -- picks up exactly where it froze, no jump
  handle.Paused = true   -- also works via the property
  handle:Toggle()

  -- 5) Batch controls:
  GradientFlow:PauseAll()
  GradientFlow:ResumeAll()
  GradientFlow:UnregisterAll()

  -- 6) Explicit removal (optional; auto-cleanup also handles Destroy'd gradients):
  handle:Unregister()

  -- 7) Scaling: register thousands the same way. One connection total.
  --    Pausing some of them makes the loop even cheaper.
================================================================================
]]
