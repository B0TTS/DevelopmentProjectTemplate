# Handoff: explain-it-v2 Voice Integration (Local Kokoro TTS)

**Date:** 06-30-2026
**Status:** Plan finalized, NOT yet executed. No code written, no deps installed, no PATH change made.
**Goal:** Make the `explain-it-v2` skill speak its Socratic walkthrough aloud via a local Kokoro-82M TTS model, looping each response until the user advances or mutes.

---

## What was accomplished this session

1. **Researched existing audio-explanation tools** (web + exa search). Evaluated Code Explainer, Agent TTS, Heard, BridgeSpeak, MCP Walkthrough, PR Explainer, Code2Cast, Code Tales, Code2Documentary.
   - Dismissed Agent TTS (0 stars) and Heard (macOS-only, user is on Windows).
   - Concluded: no existing tool fits the "keep explain-it-v2's interactive Socratic flow + add local audio" requirement. Build a thin integration instead.
2. **Chose the TTS engine:** local Kokoro-82M (Apache weights, 82M params, runs on CPU, top-ranked open-source TTS). User explicitly wants local, not cloud.
3. **Verified the environment** (read-only inspection):
   - Python 3.14.4 at `C:\Python314` — PyTorch supports 3.14 stably since torch 2.10. Not a blocker.
   - espeak-ng IS installed at `C:\Program Files\eSpeak NG\espeak-ng.exe` — but NOT on PATH (first blocker).
   - `kokoro`, `soundfile`, `torch` all uninstalled.
4. **Designed the architecture** through three rounds of Q&A with the user. Final design below.

## Finalized architecture (locked decisions)

A **single persistent Python daemon** (`tts_server.py`) that holds the model in memory and controls looping playback, plus a thin PowerShell wrapper the agent calls.

### One process: `tts_server.py`
- Loads `KPipeline(lang_code='a')` ONCE at startup (~330MB RAM resident).
- HTTP server on `127.0.0.1:8765` using stdlib `http.server` (no web framework).
- Audio playback via **`winsound`** (Python stdlib) — supports async infinite looping natively:
  - `winsound.PlaySound(path, SND_FILENAME | SND_LOOP | SND_ASYNC)` — loops gap-free forever
  - `winsound.PlaySound(None, SND_PURGE)` — instant stop
- Global hotkey listener via **`pynput`** (one extra dep): `Ctrl+Alt+M` → calls `/stop` internally. Configurable in-script. Chosen to avoid browser-mute conflict (Ctrl+Shift+M).

### API
| Endpoint | Behavior |
|---|---|
| `POST /loop` `{text}` | Generate WAV → winsound loop async → returns when audio starts (~2-5s on CPU) |
| `POST /stop` | Instant silence |
| `POST /replace` `{text}` | Atomic swap: stop + generate + loop new |
| `GET /status` | Idle / playing |

### `speak.ps1` (agent-facing helper)
- `speak.ps1 -Text "..."` → POST `/loop`
- `speak.ps1 -Stop` → POST `/stop`
- `speak.ps1 -Replace "..."` → POST `/replace`
- **Lazy auto-start:** health-checks the server; if down, launches it detached and waits for readiness. User never starts anything manually.

### explain-it-v2 SKILL.md workflow changes
Two instructions to insert into the existing 133-line skill:

1. **At the very start of every new turn** (before reading the user's message or doing any work):
   > Run `speak.ps1 -Stop` — the user sending a new message means they're ready to move on; silence any currently-looping audio.
2. **After producing the full response** (explanation + any Socratic question, as ONE block):
   > Run `speak.ps1 -Text "<your full response text>"` so it loops. Then end your turn.
3. **Note to add:** user can press `Ctrl+Alt+M` anytime for instant manual mute, independent of the agent.

### Resulting UX (locked)
- Agent responds → audio loops endlessly while user listens / repeat-listens
- `Ctrl+Alt+M` anytime → instant silence (no agent round-trip)
- User sends a new message → agent's first action is `/stop` → silence → new response → new audio loops
- Socratic Q&A preserved: the user's answer is a new message, which stops the loop and triggers the next response
- **Loop granularity:** whole response loops as one block (NOT per-section)
- **Stop trigger:** stop on ANY new message (not just explicit "stop")

---

## Current state / what's NOT done

- [ ] espeak-ng not on PATH (Step 1)
- [ ] Python deps not installed (Step 2)
- [ ] No smoke test run (Step 3)
- [ ] `tts_server.py` not written (Step 4)
- [ ] `speak.ps1` not written (Step 4)
- [ ] SKILL.md not edited (Step 5)
- [ ] No end-to-end loop test (Step 6)

## Open decisions

- **Default Kokoro voice:** undecided. Use `af_heart` (flagship female, used in Kokoro demos) for the smoke test, then list other voices (af_breeze, am_michael, etc.) for the user to pick. The voice is a one-line config in `tts_server.py`.
- **Generation latency on CPU:** unverified. Kokoro-82M is small; expect ~2-5s per response block on CPU. If too slow, the fallback is the persistent server already handles this (model stays loaded). No GPU available on this Windows box.
- **Hotkey conflicts:** `Ctrl+Alt+M` assumed safe; verify no conflict with user's running apps on first test.

---

## Key files, paths, commands

### Existing (read-only references)
- **Target skill:** `C:\Users\Jonah\DevelopmentTemplate\.agents\skills\explain-it-v2\SKILL.md` (133 lines, fully read this session — Socratic 4-phase walkthrough: Gather → Calibrate → Active Explanation → Reinforcement)
- **espeak-ng binary:** `C:\Program Files\eSpeak NG\espeak-ng.exe` (installed, not on PATH)
- **Python:** 3.14.4 at `C:\Python314` (pip 26.0.1)
- **Kokoro docs:** https://github.com/edv-k/kokoro — `pip install kokoro>=0.9.4`, `KPipeline(lang_code='a')`, 24000 Hz output, `voice='af_heart'`

### To be created (Step 4)
- `C:\Users\Jonah\DevelopmentTemplate\.agents\skills\explain-it-v2\scripts\tts_server.py` — the daemon
- `C:\Users\Jonah\DevelopmentTemplate\.agents\skills\explain-it-v2\scripts\speak.ps1` — the agent-facing wrapper

### Execution commands (in order)
```powershell
# Step 1: PATH fix (then open a NEW terminal)
setx PATH "$env:PATH;C:\Program Files\eSpeak NG"

# Step 2: install deps
pip install "kokoro>=0.9.4" soundfile torch pynput

# Step 3: smoke test (minimal KPipeline -> wav at 24000 Hz)

# Step 6: end-to-end test — start server, POST /loop, hear it loop, press Ctrl+Alt+M, confirm silence
```

### Verification commands
- `espeak-ng --version` (after new terminal) — confirms PATH fix
- `python -c "import kokoro, torch, soundfile, pynput; print('ok')"` — confirms deps
- `Invoke-RestMethod -Uri http://127.0.0.1:8765/status` — confirms server up

---

## Suggested skills for the next session

- **write-a-skill** — the SKILL.md edit follows its structure/template guidance; the `scripts/` subfolder pattern is its convention.
- **customize-opencode** — only if the integration needs opencode config hooks (e.g. auto-starting the server with opencode). Likely NOT needed since `speak.ps1` lazy-starts the server itself.
- **docs-mcp** — if Kokoro/misaki/pynput API questions arise during implementation (e.g. misaki G2P espeak-ng path resolution, pynput GlobalHotKeys syntax).
- **karpathy-guidelines** — the `tts_server.py` is a non-trivial new component; these guidelines (surgical changes, surface assumptions, verifiable success criteria) apply.

---

## Pitfalls to watch

1. **espeak-ng on PATH is mandatory** — Kokoro's G2P engine (misaki) shells out to `espeak-ng` by name. The full-path-in-wrapper approach is fragile because misaki's internal subprocess still looks on PATH. The `setx` PATH fix is the reliable route.
2. **First `KPipeline(...)` run downloads ~330MB of model weights** — one-time, needs internet. Don't be surprised by the delay on first smoke test.
3. **`winsound` is Windows-only** — this integration is Windows-specific by design (user is on win32). If porting later, swap for `simpleaudio`/`pygame.mixer` or Edge TTS's player.
4. **Per-invocation latency was the rejected option** — reloading the model each call (~1-3s + 330MB each time) is why we went with the persistent server. Don't regress to per-invocation.
5. **`setx` truncates PATH at 1024 chars** — if the user's PATH is already near that limit, use the Environment Variables UI or registry edit instead. Check PATH length first.

---

## Conversation context (one-paragraph summary)

User wanted an audio version of the `/explain-it-v2` Socratic walkthrough skill so they could listen instead of read. After researching existing tools (none fit: Heard is macOS-only, Agent TTS has 0 stars, Code Explainer replaces rather than augments explain-it-v2), we decided to keep explain-it-v2 intact and layer local Kokoro-82M TTS on top. The user wants each full agent response to loop endlessly until they mute (via `Ctrl+Alt+M` hotkey) or send a new message (which auto-stops the loop before the next response). Final architecture: one persistent Python daemon holding KPipeline in memory, stdlib `winsound` for gap-free async looping, stdlib `http.server` for the control API, `pynput` for the global mute hotkey, and a `speak.ps1` wrapper with lazy auto-start that the agent calls. Plan is fully designed and locked; execution has not begun.
