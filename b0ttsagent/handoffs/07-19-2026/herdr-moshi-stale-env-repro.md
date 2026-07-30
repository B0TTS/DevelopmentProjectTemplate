# Herdr + Moshi PATH Issue — Corrected Root Cause (Repro-Backed)

**Date:** 07-19-2026
**Status:** Root cause corrected; permanent fix identified (not yet executed)
**Supersedes (for diagnosis):** `b0ttsagent/handoffs/07-19-2026/herdr-moshi-windows-junction-path.md`

---

## TL;DR

The prior handoff named the root cause as "cmd.exe fails to traverse the Herdr directory junction during PATH pattern resolution." **That is wrong.** Direct reproduction on this machine shows cmd.exe traverses the junction fine — `where herdr` resolves `herdr.exe` through *both* Herdr junctions in a thin, non-interactive, `LoadUserProfile=false` cmd session.

The **actual** root cause is a **stale Mosh session environment**: the mosh-server process captured its environment at bootstrap time, *before* Herdr was added to machine PATH. Moshi's roam-reconnect resumes that same shell with the same stale env (no Herdr on PATH), so `herdr` stays "not recognized" indefinitely. The prior session mis-attributed the persistence to the junction — by inference, never by an isolated test.

PATHEXT is also exonerated: cmd.exe supplies its own built-in default PATHEXT (including `.EXE`) even when the env var is absent or empty, so it cannot drop `.EXE` via env manipulation in a normal launch.

---

## What Was Accomplished This Session

Read the prior handoff and all six debug scripts in `b0ttsagent/temp/herdr-*.ps1`. Discovered that **none of the six ever check `PATHEXT`, never run `where herdr.exe` (only bare `herdr`), and never isolate the junction vs. the env.** Their "simulate SSH" scripts overwrite `$env:Path` but leave `$env:PATHEXT` intact from the interactive PowerShell — so the simulation could not reproduce a real non-interactive SSH env.

Ran deep web research (Moshi docs, Win32-OpenSSH GitHub issues, ServerFault, Microsoft Learn) confirming the mechanism: Moshi bootstraps via a non-interactive SSH command (`ssh user@host mosh-server new`), and the interactive session inherits that bootstrap env. Win32-OpenSSH returns only a "paltry subset" of env vars in non-interactive sessions — relevant for the APPDATA risk below, but **not** for the `herdr` "not recognized" symptom (PATHEXT self-heals).

Then ran **three controlled repros** on this machine, spawning `cmd.exe` with `LoadUserProfile=false` and a thin env (mimicking non-interactive SSH):

| # | Env | `where herdr` | `herdr --version` |
|---|---|---|---|
| 1 | Machine PATH (junction entries) + machine PATHEXT | ✅ found through both junctions | ✅ `herdr 0.7.4-preview…` |
| 2 | PATHEXT **absent** from env | ✅ found (cmd supplies default incl. `.EXE`) | ✅ works |
| 3 | PATHEXT = empty string `""` | ✅ found (cmd still defaults to `.EXE`) | ✅ works |
| 4 | Herdr **stripped from PATH** | ❌ "Could not find files" | ❌ not recognized |

- Tests 1–3 disprove the junction hypothesis and the PATHEXT hypothesis.
- Test 4 is the **only** repro of the exact symptom, and it's simply "Herdr not on PATH."

Also confirmed via PowerShell (git-bash `reg query | tr` pipelines give **false negatives** — the prior session may have been misled by this):

---

## Current System State (verified this session)

- ✅ Herdr is on **machine PATH** (both junction entries) **and** user PATH — the prior session's machine-PATH add *did persist*.
- ✅ Machine `PATHEXT` present and correct (`.EXE` included).
- ✅ Both junctions healthy — resolve to `…\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc`; `herdr.exe` present (17.7 MB).
- ✅ sshd Running / Automatic. `DefaultShell` unset → cmd.exe. No `SetEnv`/`PermitUserEnvironment` in `C:\ProgramData\ssh\sshd_config`.
- ✅ `SafeProcessSearchMode` / `SafeDllSearchMode` unset (defaults) — no exotic SearchPathW override.
- ⚠️ **Two** herdr processes running:
  - PID 30044 = installed `herdr` client (healthy).
  - **PID 30756 = `C:\Users\Jonah\Downloads\SetupFIles\herdr-windows-x86_64.exe server`** — stale server from the installer binary, separate from the installed herdr. Should be killed.
- ✅ Herdr server log healthy: `client_id=10` attached 21s then detached via **user keybind** (not a crash). The `client_id=9` 2s connect/disconnect is the Moshi session-picker probe (list-and-exit), not a crash. The `WARN … failed to read Windows console input mode for VT input` is benign.

---

## The Real Fix (do this, not the prior handoff's junction-avoidance)

1. **Fully tear down the existing Mosh session** — kill the mosh-server process on the Windows host, then start a **brand-new** Moshi connection from the phone. *Not* just a roam-reconnect. The new bootstrap reads the current machine PATH (which has Herdr) → `herdr` resolves. Optionally `Restart-Service sshd` first (elevated) for safety, though new sessions read registry machine env directly.
2. **Verify in the new session** (this is the one decisive test the prior session never ran):
   ```cmd
   echo PATH=%PATH%
   echo PATHEXT=%PATHEXT%
   echo APPDATA=%APPDATA%
   where herdr
   where herdr.exe
   herdr --version
   ```
   Predicted: `where herdr` + `herdr --version` succeed. **Check `APPDATA`** (see open decision).
3. **Leave the junction-based PATH entries alone.** They work. The prior handoff's "permanent fix" (redirect PATH to `current`) and the `C:\ProgramData\herdr-launch` real-copy both solve a non-problem. The launcher dir + copy may still exist from the prior session — harmless, can be left or cleaned up.
4. **Kill the stale second server:**
   ```powershell
   Stop-Process -Id 30756 -Force
   ```

---

## Open Decisions

1. **APPDATA in the fresh Moshi session (the real remaining risk).** With `LoadUserProfile=false`, Win32-OpenSSH can set `APPDATA`/`LOCALAPPDATA` to `C:\Windows\system32\config\systemprofile\AppData\...` instead of the user's profile. If so, a Moshi-launched `herdr session list` probe won't find `%APPDATA%\herdr\herdr.sock` → session auto-detection fails even though `herdr` is now findable. **This was not testable from the local repro (it set APPDATA correctly); needs the in-session `echo %APPDATA%` check above.** If broken, options:
   - `SetEnv APPDATA C:\Users\Jonah\AppData\Roaming` + `SetEnv LOCALAPPDATA …` + `SetEnv USERPROFILE …` in `C:\ProgramData\ssh\sshd_config` (requires `PermitUserEnvironment yes` or AcceptEnv support — verify Win32-OpenSSH version supports it).
   - Or a `DefaultShell` wrapper script that sets the env before exec'ing cmd.
   - Or Herdr's `HERDR_CONFIG_PATH` env override (documented in `herdr --help`) to point at the real config — keeps it herdr-specific without touching sshd env.
2. **Whether to add a NavGuide** for the Herdr + Moshi + Windows-OpenSSH integration. No such guide exists in `b0ttsagent/NavGuides/` (confirmed this session). Worth doing once the fix is confirmed working.

---

## Suggested Skills for Next Session

- **create-nav-guide** — once the fix is verified, capture the Herdr + Moshi + Windows-OpenSSH integration as a reference guide. The prior handoff suggested this; still not done.
- (No planning-doc skill needed — this is a focused fix, not a multi-phase build.)

---

## Key Files, Paths, and Commands

**Prior handoff + debug scripts (reference, don't re-derive):**
- `b0ttsagent/handoffs/07-19-2026/herdr-moshi-windows-junction-path.md` — the (now-corrected) prior diagnosis.
- `b0ttsagent/temp/herdr-*.ps1` — the six debug scripts. Useful for re-running the in-session probe; note their PATHEXT/simulation gaps.

**Herdr paths:**
| What | Path |
|---|---|
| Herdr bin (junction, WORKS) | `C:\Users\Jonah\AppData\Local\Programs\Herdr\bin` |
| Herdr `current` (junction) | `C:\Users\Jonah\.herdr\packages\standalone\current` |
| Actual release | `C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc` |
| Config & logs | `C:\Users\Jonah\AppData\Roaming\herdr\` |
| Socket | `C:\Users\Jonah\AppData\Roaming\herdr\herdr.sock` |
| Stale server binary (kill PID 30756) | `C:\Users\Jonah\Downloads\SetupFIles\herdr-windows-x86_64.exe` |
| sshd config | `C:\ProgramData\ssh\sshd_config` |

**Authoritative env check (use PowerShell, NOT git-bash `reg query | tr`):**
```powershell
[Environment]::GetEnvironmentVariable('Path','Machine')   # has Herdr junctions
[Environment]::GetEnvironmentVariable('PATHEXT','Machine') # .EXE present
[Environment]::GetEnvironmentVariable('Path','User')       # has Herdr junction
```

**Thin-env repro (the proof — re-run if junction claim resurfaces):**
```powershell
$mPath = [Environment]::GetEnvironmentVariable('Path','Machine')
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = 'cmd.exe'
$psi.Arguments = '/c where herdr & where herdr.exe & herdr --version'
$psi.UseShellExecute = $false
$psi.RedirectStandardOutput = $true; $psi.RedirectStandardError = $true
$psi.LoadUserProfile = $false
$psi.Environment.Clear()
$psi.Environment['Path'] = $mPath
$psi.Environment['PATHEXT'] = [Environment]::GetEnvironmentVariable('PATHEXT','Machine')
$psi.Environment['SystemRoot'] = $env:SystemRoot
$psi.Environment['ComSpec'] = $env:ComSpec
$p = [Diagnostics.Process]::Start($psi)
$p.StandardOutput.ReadToEnd(); $p.WaitForExit()
# Expect: herdr.exe found through both junctions, --version succeeds
```

**One-line stale-server cleanup:**
```powershell
Stop-Process -Id 30756 -Force
```
