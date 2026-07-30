-- b0ttsagent/temp/gradient_lut_preview.lua
-- ILLUSTRATION ONLY (not the final system).
-- Prints a few entries of the phase LUT so you can SEE what the table looks like.
-- Paste into a Roblox Studio command bar / script to view output.
--
-- Core idea: the new gradient at time t = the original gradient at time (t + p) mod 1.
-- We precompute one ColorSequence per phase p, for p = 0, 1/N, 2/N, ..., (N-1)/N.
-- At runtime, animation = pick LUT[index] and assign. Zero allocation.

local function makeBaseGradient()
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

-- Evaluate a ColorSequence at time t in [0,1] (linear interp between keypoints).
local function sampleAt(cs, t)
	local kps = cs.Keypoints
	if t <= kps[1].Time then return kps[1].Color end
	if t >= kps[#kps].Time then return kps[#kps].Color end
	for i = 1, #kps - 1 do
		local a, b = kps[i], kps[i + 1]
		if t >= a.Time and t <= b.Time then
			local f = (t - a.Time) / (b.Time - a.Time)
			return Color3.new(
				a.Color.R + (b.Color.R - a.Color.R) * f,
				a.Color.G + (b.Color.G - a.Color.G) * f,
				a.Color.B + (b.Color.B - a.Color.B) * f
			)
		end
	end
	return kps[#kps].Color
end

-- Build ONE LUT entry for phase p in [0,1).
local function buildEntryAtPhase(baseCS, p)
	-- Endpoints close the loop seamlessly: color@0 == color@1 == sampleAt(p).
	local ep = sampleAt(baseCS, p)
	local pts = { ColorSequenceKeypoint.new(0, ep) }
	-- Interior keypoints: shift original times by p (mod 1).
	-- Skip the original keypoint at t=1; it collapses into the endpoint color.
	for _, kp in ipairs(baseCS.Keypoints) do
		if kp.Time < 1 then
			table.insert(pts, ColorSequenceKeypoint.new((kp.Time + p) % 1, kp.Color))
		end
	end
	table.insert(pts, ColorSequenceKeypoint.new(1, ep))
	table.sort(pts, function(a, b) return a.Time < b.Time end)
	return ColorSequence.new(pts)
end

-- Preview: print N entries across one full cycle (small N for readability).
local N = 6
local base = makeBaseGradient().Color
print(string.format("=== LUT preview  N=%d  (one full cycle) ===", N))
for i = 0, N - 1 do
	local p = i / N
	local cs = buildEntryAtPhase(base, p)
	print(string.format("LUT[%d]  phase=%.4f   keypoints=%d", i, p, #cs.Keypoints))
	for _, kp in ipairs(cs.Keypoints) do
		print(string.format("    t=%.4f   r=%.3f g=%.3f b=%.3f",
			kp.Time, kp.Color.R, kp.Color.G, kp.Color.B))
	end
end
print("=== end preview ===")
