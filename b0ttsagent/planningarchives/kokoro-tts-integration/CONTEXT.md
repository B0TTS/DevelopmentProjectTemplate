# CONTEXT — explain-it-v2-voice (Local Kokoro TTS)

## What I Want

I want an audio version of the `explain-it-v2` Socratic walkthrough skill so I can listen to each full response spoken aloud instead of reading it. Each complete response should loop endlessly until I either mute it (via a global hotkey) or send a new message (which auto-stops the loop before the next response is generated and spoken). The original `explain-it-v2` skill must stay intact and untouched — this is a new, separate skill cloned from it, with voice layered on top. The Socratic Q&A flow must be preserved: my answer is a new message, which stops the loop and triggers the next spoken response.

## Scope

**In scope:**
- A new skill, `explain-it-v2-voice`, cloned from `.agents/skills/explain-it-v2/` (the existing 133-line SKILL.md with its 4-phase flow: Gather → Calibrate → Active Explanation → Reinforcement).
- Two workflow insertions into the cloned SKILL.md: (1) stop any currently-looping audio at the start of every new turn, (2) speak the full response after it's produced so it loops.
- A persistent local TTS daemon that holds the model in memory and controls looping playback.
- An agent-facing PowerShell wrapper the agent calls to start/stop/replace speech.
- A global mute hotkey the user can press anytime for instant silence without an agent round-trip.
- A safe, persistent PATH fix so the TTS engine's phoneme backend can find its system dependency.

**Out of scope:**
- Any change to the original `explain-it-v2` skill (read-only reference only).
- Any change to the Socratic pedagogy (audio is layered on; the 4-phase flow, retrieval practice, generation effect, and calibration are preserved verbatim from the source).
- Cloud TTS (must be local).
- Non-Windows support (the looping mechanism is Windows-stdlib).
- Any other skill touched.
- Auto-starting the daemon via opencode config (the wrapper lazy-starts it instead).

## What Success Looks Like

1. **Given** the `explain-it-v2-voice` skill is invoked for the first time in a session, **when** the agent produces its first full response, **then** a local TTS daemon lazy-starts (no manual step) and the response begins looping aloud within ~5 seconds on CPU.
2. **Given** audio is currently looping, **when** the user presses `Ctrl+Alt+M`, **then** audio stops in under 500ms with no agent round-trip (the hotkey hits the daemon directly).
3. **Given** audio is currently looping, **when** the user sends a new message, **then** the agent's first action is to stop the loop (silence) before producing the next response — which then loops anew.
4. **Given** the 4-phase Socratic flow (Gather → Calibrate → Active Explanation → Reinforcement) in the source skill, **when** the clone is compared to it, **then** every phase, principle, and interaction pattern is preserved verbatim — only the two audio insertions are added.
5. **Given** the user's current PATH is 2028 characters, **when** the PATH fix is applied, **then** the PATH is not truncated or corrupted (no entries lost) — verified by comparing entry count before and after.
6. **Given** the daemon is already running and holding the model in memory, **when** a subsequent response is spoken, **then** the model is NOT reloaded (no second ~330MB resident allocation, no repeated multi-second init) — the running daemon is reused.
7. **Given** the original `explain-it-v2` skill, **when** the clone is created, **then** the original skill's files are byte-for-byte unchanged.

## What I Already Know

- **`b0ttsagent/handoffs/06-30-2026/explain-it-v2-voice-integration.md`** — the prior session's handoff. Contains the locked architecture (persistent daemon + thin wrapper), locked UX (loop whole response, stop on any new message, `Ctrl+Alt+M` mute), the API design, and open decisions. This is the primary design input.
  - **Gaps in that analysis, corrected by this session's research:**
    - The Kokoro repo URL cited (`edv-k/kokoro`) is wrong; the real repo is `hexgrad/kokoro` (7.7k stars; `NVIDIA/kokoro` is a mirror).
    - The handoff's Step 1 (`setx PATH ...`) is unsafe: `setx` silently truncates PATH at 1024 chars (Microsoft docs confirm; multiple user reports of destroyed PATHs). The user's PATH is 2028 chars — `setx` would have destroyed it. Resolved: use PowerShell `[Environment]::SetEnvironmentVariable` instead (user-confirmed).
    - The handoff conflated first-run download size (~200MB) with resident RAM (~330MB) — two different numbers.
    - The handoff's voice list included `af_breeze`, which is not in the canonical voice list.
    - The handoff did not know about the `misaki/espeak.py` `set_data_path()` landmine (removed in phonemizer ≥3.4 — issue #206).
- **`.agents/skills/explain-it-v2/SKILL.md`** (133 lines) — the source skill to clone. 4-phase Socratic walkthrough. Fully read in the prior session and re-verified this session (front matter + first 15 lines confirmed).
- **Environment (verified this session):** `C:\Program Files\eSpeak NG\espeak-ng.exe` is present; `b0ttsagent/planning/` exists; Python 3.14.4 at `C:\Python314`; PyTorch 2.10 supports Python 3.14 (compat matrix `<=3.14`; Windows CPU-only wheel exists).

## Constraints & Principles

- **Windows-only:** the looping playback mechanism is Windows-stdlib (`winsound`); not portable. (User is on win32.)
- **Local-only TTS:** no cloud calls; the model runs on this machine. GPU is available (RTX 3060, 32GB DDR4, i7-11700F) — Kokoro needs <2GB VRAM, so CUDA inference is viable and preferred over CPU for latency.
- **Must not corrupt the user's PATH:** the user's PATH is 2028 chars — far over `setx`'s 1024 truncation limit. The PATH fix must use a truncation-safe mechanism.
- **Preserve the pedagogy intact:** the clone's Socratic flow, principles, and interaction patterns must match the source verbatim. Audio is additive only — no rewriting of how the skill teaches.
- **Whole-response loop granularity:** the full response (explanation + any Socratic question) loops as one audio block, not per-section.
- **Stop on ANY new message:** any user message stops the loop, not just explicit "stop" commands.
- **One persistent daemon:** the model loads once and stays in memory; no per-invocation reload (per-invocation was the rejected option — ~1-3s init + 330MB each call).
- **Original skill is read-only:** `explain-it-v2` must not be modified.

Project-wide rules (e.g., skill structure conventions, "use the skill workflow") are cited from `AGENTS.md` rather than restated here.

## Key Terms

- **G2P (Grapheme-to-Phoneme):** the process of converting written text to phoneme sequences. Kokoro uses `misaki` as its G2P engine.
- **misaki:** the G2P library Kokoro uses under the hood. Falls back to `espeak-ng` for out-of-dictionary words.
- **phonemizer:** the lower-level library `misaki` shells into for espeak fallback. Has its own espeak-path resolution via env vars.
- **`KPipeline`:** Kokoro's main inference pipeline class. `KPipeline(lang_code='a')` loads the American-English model + weights.
- **`SND_LOOP` / `SND_ASYNC`:** `winsound` flags. `SND_LOOP|SND_ASYNC` plays a WAV file repeatedly, non-blocking, forever. `SND_LOOP` is incompatible with `SND_MEMORY` (must play from a file path, not a memory buffer).
- **OOD fallback:** out-of-dictionary fallback — words the G2P dict doesn't know get passed to espeak-ng for phoneme lookup.
- **Looping daemon:** a long-running process that holds the model in memory, generates WAV on demand, and controls infinite-loop playback.
- **Lazy auto-start:** the agent-facing wrapper health-checks the daemon; if down, launches it detached and waits for readiness. The user never starts anything manually.

## Assumptions

- **Default voice:** `af_heart` (flagship female, used in Kokoro demos) for the first smoke test. Other voices offered after the user hears it. The voice is a one-line config in the daemon. *(Decided-by-default; override if wrong.)*
- **`Ctrl+Alt+M` is conflict-free** on the user's machine. Chosen to avoid the browser-mute conflict (`Ctrl+Shift+M`). Verified at first end-to-end test. *(Decided-by-default; verify at test.)*
- **GPU (CUDA) is the primary inference device.** RTX 3060 + PyTorch 2.10 (CUDA 12.6/12.8/13.0 on Windows supported) — `KPipeline` should use `device='cuda'`. CPU is the fallback only if CUDA setup fails. Generation latency on GPU should be well under the ~2-5s CPU estimate. *(Decided-by-default; verify at smoke test.)*
- **`kokoro-onnx` is the escape hatch**, not a planned phase. Noted in REFERENCES only. Switch to it only if the pip+espeak path proves unworkable on this Windows box. *(Decided-by-default.)*
- **Install latest deps, pin only if it breaks.** `pip install kokoro soundfile torch pynput` (latest). If the `misaki/espeak.py` `set_data_path()` AttributeError fires (phonemizer ≥3.4 removed it — issue #206), pin `misaki[en]`/`phonemizer` to a known-good pair at that point. *(Decided-by-default.)*
- **The PATH fix targets the User scope** (not Machine), appending `C:\Program Files\eSpeak NG` via `[Environment]::SetEnvironmentVariable('Path', ..., 'User')`. A new terminal is required to pick it up. *(Decided-by-default.)*

## Open Questions

- **Final default voice:** the user picks after hearing `af_heart` and comparing against other candidates (`af_bella`, `af_nicole`, `af_sarah`, `af_sky`, `am_adam`, `am_michael`, `bf_emma`, `bf_isabella`, `bm_george`, `bm_lewis`). Resolved at/after the smoke test.
- **Actual GPU latency on this box:** unverified until the smoke test. Expect well under the ~2-5s CPU estimate once `device='cuda'` is confirmed working. CPU fallback latency (~2-5s) is the ceiling if CUDA fails.
- **`Ctrl+Alt+M` hotkey conflict:** assumed safe; must verify no conflict with the user's running apps at the first end-to-end test.
- **Exact first-run download size:** sources cite ~200MB; confirm at smoke test (one-time, needs internet).
- **Whether the `set_data_path` bug fires on a fresh latest install:** unknown until `KPipeline` is first constructed. If it fires, the fix is a version pin (issue #206 documents the one-line patch, but pinning is cleaner).

## Non-Goals

- Cloud TTS (Edge TTS, Google, ElevenLabs, etc.).
- Non-Windows porting (no macOS/Linux audio path).
- Per-section audio looping (the whole response is one loop block).
- Altering `explain-it-v2`'s pedagogy in any way.
- Auto-starting the daemon via opencode config hooks (`speak.ps1` lazy-starts instead).
- Voice cloning or custom voices.
- Multi-language support (English only for v1; `lang_code='a'`).
- Real-time streaming audio (generation is batch-then-loop, not stream-as-you-go).
