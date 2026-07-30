# Gradient Flow System — Readability Handoff

## What was accomplished this session

Used the **grill-me** skill to design and build a high-performance, infinitely-flowing `UIGradient` animation system for Roblox, tuned to scale to thousands of simultaneous gradients at up to 240Hz+ with near-zero per-frame cost.

The user's input was a `UIGradient` factory whose `ColorSequence` starts AND ends on red (`1,0,0`) — i.e. a closed/seamless loop. The design was produced by walking the decision tree one question at a time. **The user ran the final system in-game and confirmed it "works amazingly perfect and correct."**

The full strategy write-up and locked decisions live in the file header — do NOT duplicate them here. See **Key files**.

## Current state

- ✅ Working, tested original exists and is proven correct in-game.
- ⚠️ The user created a duplicate to refactor for readability, but **the duplicate is currently EMPTY (0 bytes)**. The next session must populate it from the working original before refactoring.
- The next session's goal: **make the system easier to read**, working in the duplicate so the known-good original is preserved.

## Open decisions / next-session focus

- **Readability refactor** — no specific approach locked yet. The next session should establish the readability strategy (e.g. clearer naming, sectioning, comments, splitting concerns) **without changing behavior**, since the original is verified working.
- **CRITICAL:** First action next session — copy the working content of `gradient_flow_system.lua` into `MakeUnderstandable.luau` (currently empty). Never modify the original.

## Suggested skills for the next session

- **`karpathy-guidelines`** — strongly recommended. A readability refactor must change *form*, not *behavior*; this skill enforces surgical changes and verifiable success criteria (i.e. the refactor preserves identical output).
- **`grill-me`** — if the user wants to stress-test a readability approach before applying it.
- **`create-context-doc`** / **`create-execution-plan`** — only if the readability refactor grows into a multi-phase effort.

## Key files & paths

| Path | Status | Purpose |
|---|---|---|
| `b0ttsagent/temp/gradient_flow_system.lua` | ✅ Working, tested, 16,493 bytes | **The known-good original. DO NOT MODIFY.** Header contains the full strategy + 9 locked design decisions. |
| `b0ttsagent/temp/MakeUnderstandable.luau` | ⚠️ EMPTY (0 bytes) | Intended duplicate / target for the readability refactor. Populate from the original first. |
| `b0ttsagent/temp/gradient_lut_preview.lua` | Illustration | Prints LUT entries into Studio so you can SEE the phase-shift table. Not part of the runtime system. |

## Locked design decisions (summary — full detail in the file header)

1. Color-flow via keyframe shift (seamless because the gradient is red-looped)
2. Precomputed phase LUT, `N=240` (the core performance win — zero hot-path allocation)
3. `N` decoupled from refresh rate (built into the dt + modulo logic) — same table serves 60/144/240Hz
4. 5s default cycle, **configurable live** (seamless, no restart/jump)
5. Per-gradient phase offset, global phase advancement, default uniform wave, configurable per-instance
6. Single shared `RenderStepped` loop (one connection always), parallel primitive-array storage, auto-pause when empty
7. Lazy swap-pop cleanup on `Parent == nil` (no per-object connections, leak-free), optional explicit `Unregister`
8. Individual pause/resume (added late) — freezes at exact color, resumes with no jump; paused gradients cost zero per frame

## Notes for the next agent

- The runtime API surface to preserve during the refactor: `Controller:Register(gradient, offset?)` → handle; `handle:Pause/Resume/Toggle/Unregister/SetOffset`; `handle.Paused`, `handle.Offset` (settable); `Controller:PauseAll/ResumeAll/UnregisterAll`; `Controller.CycleSeconds` (settable), `.Count`, `.N`, `.IsRunning`.
- One caveat already documented in the file: register gradients **after parenting them** — auto-cleanup uses `Parent == nil` as the "destroyed" signal.
