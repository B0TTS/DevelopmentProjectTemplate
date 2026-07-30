# Herdr + Moshi Windows Junction PATH Issue

**Date:** 07-19-2026  
**Status:** Root cause identified, permanent fix pending

---

## Summary

User connects to Windows PC via Moshi (SSH over Tailscale). They have Herdr running locally on the PC. When they try to run `herdr` from the Moshi SSH shell, cmd.exe reports:

```
'herdr' is not recognized as an internal or external command,
operable program or batch file.
```

Even though `herdr` works fine from the desktop, and `echo %PATH%` shows Herdr's bin directory present.

---

## Root Cause

`C:\Users\Jonah\AppData\Local\Programs\Herdr\bin` is a **Junction** (Directory + ReparsePoint) created by the Herdr Windows installer. It points to the versioned release at:

```
C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc
```

cmd.exe in SSH sessions (non-interactive, `LoadUserProfile=false`) fails to traverse this junction during PATH pattern resolution. `where herdr` finds nothing even though the directory is on PATH and the binary exists inside it.

Additionally, Herdr's bin directory was originally only on the **user** PATH — SSH sessions get a thinner environment that may not include user PATH. This was fixed mid-session by adding it to machine PATH, but the junction issue persisted.

---

## What Was Tried

| Step | Result |
|---|---|
| Added Herdr bin to machine PATH | Didn't fix it — junction still blocks find |
| Set OpenSSH `DefaultShell` to PowerShell | Not done yet — may help but doesn't fix junction |
| Verified binary works with absolute path | **Works** — `herdr --version` succeeds |
| Simulated non-interactive cmd with `LoadUserProfile=false` | Binary IS accessible, dir listing works — issue is specifically cmd's PATH search + junction |

---

## Workaround (works now)

In Moshi, use the absolute path to the real binary (not the junction):

```bat
"C:\Users\Jonah\.herdr\packages\standalone\current\herdr.exe"
```

Or the full release path:

```bat
"C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc\herdr.exe"
```

---

## Permanent Fix (recommended)

Add the **real** release directory (`current` junction target) to the machine PATH, alongside or replacing the Programs junction path.

**Admin PowerShell:**

```powershell
$realDir = "C:\Users\Jonah\.herdr\packages\standalone\current"
$machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
if ($machinePath -notlike "*$realDir*") {
  [Environment]::SetEnvironmentVariable("Path", "$machinePath;$realDir", "Machine")
}
Restart-Service sshd
```

Then fully disconnect and reconnect Moshi.

**Caveat:** The `current` directory is itself a junction that gets updated on `herdr update`. If updates change the junction target, the machine PATH entry should still work since it points to `current` (which gets re-pointed), not the versioned release. But this hasn't been tested across upgrades.

**Alternative:** Copy `herdr.exe` to a non-junction directory on machine PATH (e.g., `C:\ProgramData\herdr-launch\herdr.exe`). This was done mid-session but the machine PATH entry for that directory failed to set due to admin elevation. Retry from elevated shell.

---

## Key Paths

| What | Path |
|---|---|
| Herdr bin (junction, problematic) | `C:\Users\Jonah\AppData\Local\Programs\Herdr\bin` |
| Herdr `current` (junction) | `C:\Users\Jonah\.herdr\packages\standalone\current` |
| Actual release (real dir) | `C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc` |
| Config & logs | `C:\Users\Jonah\AppData\Roaming\herdr\` |
| Socket (server ↔ client) | `C:\Users\Jonah\AppData\Roaming\herdr\herdr.sock` |
| Session data | `C:\Users\Jonah\AppData\Roaming\herdr\session.json` |
| Server log | `C:\Users\Jonah\AppData\Roaming\herdr\herdr-server.log` |
| Client log | `C:\Users\Jonah\AppData\Roaming\herdr\herdr-client.log` |
| Debug scripts (temp) | `C:\Users\Jonah\DevelopmentTemplate\b0ttsagent\temp\herdr-*.ps1` |

---

## Open Questions / Risks

1. **Does Herdr survive upgrades?** The `current` junction is re-pointed by `herdr update`. If the machine PATH uses `current`, it should keep working. If it uses the versioned release path, it'll break on upgrade. Prefer `current` path.

2. **Moshi detection of Herdr sessions** — Even once `herdr` is findable, Moshi's auto-detection (which runs `herdr session list --json` over a thin SSH shell) may still fail if it hits the same junction problem. Test the session picker after the fix.

3. **Console input mode warning** — Logs show `WARN herdr::client: failed to read Windows console input mode for VT input` when Herdr runs through Moshi's PTY. This may cause rendering quirks but doesn't seem to block attach (client_id=9 connected successfully then disconnected — unclear if user initiated or crash).

4. **Second herdr process** — `C:\Users\Jonah\Downloads\SetupFIles\herdr-windows-x86_64.exe server` is running separately from the installed herdr.exe. Could be a stale process from manual launch or old install. Worth cleaning up.

---

## Suggested Skills for Next Session

- **create-nav-guide** — to capture this Herdr + Moshi + Windows integration knowledge if a reference guide doesn't already exist
- **create-context-doc** — if this turns into a larger Windows terminal workspace project

---

## Quick Reference Commands

```powershell
# Check junction type
Get-Item 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin' -Force | fl FullName, LinkType, Target

# Check what SSH session sees
ssh Jonah@127.0.0.1 'echo %PATH%; where herdr; herdr --version'

# Server/process status
herdr status
herdr session list

# Logs
Get-Content "$env:APPDATA\herdr\herdr-server.log" -Tail 50
Get-Content "$env:APPDATA\herdr\herdr-client.log" -Tail 50

# SSH auth log
Get-WinEvent -LogName 'OpenSSH/Operational' -MaxEvents 15 | ft TimeCreated, Message -Wrap
```
