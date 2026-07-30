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

--== HELPERS ===================================================================
-- Map a phase in [0,1) to a LUT index in [0, N-1].
local function phaseToIndex(phase)
	return math.floor(phase * N) % N
end

-- O(1) removal: move last element into the vacated slot, then shrink.
-- Invalidates the handle at position i.
local function swapRemoveAt(i)
	local h = handles[i]
	if h then h.IsValid = false end
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
end

--== LUT BUILD (runs once at init) =============================================
-- Linear-interp sample of the base keypoint set at time t in [0,1].
local function sampleAt(keypoints, t)
	if t <= keypoints[1][1] then return keypoints[1][2] end
	if t >= keypoints[#keypoints][1] then return keypoints[#keypoints][2] end
	for i = 1, #keypoints - 1 do
		local a, b = keypoints[i], keypoints[i + 1]
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
	return keypoints[#keypoints][2]
end

-- Build ONE ColorSequence for phase p in [0,1).
-- Convention: color at position x = base color at ((x - p) mod 1).
--   => as p increases, colors flow RIGHT. Seamless because base(0)==base(1)==red.
-- Interior keypoints sit at x = (t_k + p) mod 1; endpoints carry the seam color
-- base((1 - p) mod 1) so x=0 and x=1 match. Near-equal times are de-duped.
local function buildEntryAtPhase(keypoints, p)
	local seam = sampleAt(keypoints, (1 - p) % 1)
	local shiftedKeypoints = {}
	for _, kp in ipairs(keypoints) do
		local x = (kp[1] + p) % 1
		if x > EPS and x < 1 - EPS then
			table.insert(shiftedKeypoints, { time = x, color = kp[2] })
		end
	end
	table.sort(shiftedKeypoints, function(a, b) return a.time < b.time end)

	local sequenceKeypoints = { ColorSequenceKeypoint.new(0, seam) }
	for _, entry in ipairs(shiftedKeypoints) do
		local last = sequenceKeypoints[#sequenceKeypoints]
		if (entry.time - last.Time) >= EPS then
			table.insert(sequenceKeypoints, ColorSequenceKeypoint.new(entry.time, entry.color))
		end
	end
	table.insert(sequenceKeypoints, ColorSequenceKeypoint.new(1, seam))
	return ColorSequence.new(sequenceKeypoints)
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
				local gradient = gradients[i]
				if gradient.Parent == nil then
					-- LAZY CLEANUP: destroyed/unparented => O(1) swap-pop
					swapRemoveAt(i)
					if count == 0 then
						if connection then connection:Disconnect(); connection = nil end
						return
					end
					-- do NOT increment i: recheck the swapped-in element
				else
					if not paused[i] then
						local phase = (globalPhase + offsets[i]) % 1
						gradient.Color = LUT[phaseToIndex(phase) + 1]
					end
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
		gradients[i].Color = LUT[phaseToIndex(frozenPhase[i]) + 1]
	end
end

function HandleMt:Unregister()
	if not self.IsValid then return end
	self.IsValid = false
	swapRemoveAt(self.index)
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