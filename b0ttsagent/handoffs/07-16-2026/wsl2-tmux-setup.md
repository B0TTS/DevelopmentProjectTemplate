# Handoff: WSL2 + Real tmux Setup (for Termius/phone use)

**Date:** 07-16-2026
**Session goal:** Get tmux working over SSH from Termius (phone), pivoting from psmux to real tmux in WSL2.

---

## What was accomplished this session

1. **Researched** tmux-on-Windows options. Two viable paths identified: **psmux** (scoop, Windows-native tmux-compatible) and **WSL2 + real tmux**.
2. **Installed psmux 3.3.6 via scoop** — works locally in Git Bash. Created `~/.tmux.conf` (Git Bash default-shell, mouse, vi mode, status bar). Started a session successfully.
3. **Hit a blocker over SSH (Termius):** scoop's `tmux` shim points through a `current` junction, which Windows **RedirectionGuard** (enabled for `sshd.exe` by a recent OpenSSH update) refuses to follow over SSH. Diagnosed and confirmed with research (ScoopInstaller issues #6594, #6612).
4. **Workarounds evaluated:**
   - Option A (direct version-path binary) — **tried, did not work over Termius.**
   - Option B (registry-disable RedirectionGuard for sshd) — rejected on security/fragility grounds.
   - Option C (bash function wrapping the version-path binary) — viable but user chose to pivot instead.
5. **Pivoted decision:** go with **WSL2 + real tmux** for SSH/Termius use. Deep research done on the full integration (SSH default shell, WSL2 keepalive, mosh, distro choice).
6. **All open decisions resolved** (see below).

## Current state

| Item | Status |
|---|---|
| OpenSSH server (Windows) | ✅ Installed, Running, Auto-start. Key auth configured (`administrators_authorized_keys`). |
| `DefaultShell` (registry) | ❌ Not set — SSH lands in Windows default shell (cmd/PowerShell). **Decision: leave as-is (manual drop-in).** |
| psmux | Installed at `~/scoop/apps/psmux/3.3.6/`. Works locally, NOT over SSH. May keep or remove — see notes. |
| `~/.tmux.conf` (psmux) | Exists at `C:\Users\intel\.tmux.conf`, configured for Git Bash. Separate from the WSL tmux config. |
| WSL2 distros | Only `docker-desktop` exists (Docker utility distro, NOT usable for tmux). |
| `.wslconfig` | ❌ Does not exist. **Must be created for tmux session persistence.** |
| WSL default version | 2 (good) |
| Real tmux | ❌ Not yet installed |

## Resolved decisions (for next session)

- **Distro:** **Ubuntu 24.04 LTS** (ships tmux 3.4 via apt; maximum tutorial/compat).
- **SSH landing:** **Manual drop-in** — keep landing in Windows shell, user types `wsl` then `tmux`. No `DefaultShell` registry change.
- **Admin access:** Available (needed for distro install + `.wslconfig` + firewall).
- **Session persistence scope:** Surviving **disconnects / WSL idle** is the must-have (`.wslconfig` keepalive). Surviving **full Windows reboots** is **out of scope** (documented below).
- **mosh:** **Out of scope** (documented below).

## Execution plan (next session — run via the `tutorial` skill)

1. **Admin PowerShell:** `wsl --install -d Ubuntu-24.04`
   - Triggers download + first-run. Set a Linux username + password when prompted.
   - No Windows reboot needed (WSL2 platform already enabled — docker-desktop proves it).
2. **Verify distro:** `wsl -l -v` shows `Ubuntu-24.04`. `wsl` drops into a bash prompt (`user@B0TTS:~$`), NOT the docker-desktop one.
3. **Install tmux inside Ubuntu:** `sudo apt update && sudo apt install -y tmux` → verify `tmux -V` shows `tmux 3.4`.
4. **Create `C:\Users\intel\.wslconfig`** with keepalive (THE critical step for phone use):
   ```
   [wsl2]
   vmIdleTimeout=-1

   [general]
   instanceIdleTimeout=-1
   ```
5. **Apply:** `wsl --shutdown`, then reopen WSL.
6. **Verify keepalive works:** In WSL run `tmux new -d -s test`; exit WSL; wait 10+ seconds; `wsl --list --running` should still show Ubuntu; reopen WSL and `tmux ls` should still list `test`. If the distro stops, see the WSL keepalive notes below.
7. **Create `~/.tmux.conf` inside Ubuntu's home** (`/home/<ubuntu-user>/.tmux.conf` — a DIFFERENT file from the psmux one at `C:\Users\intel\.tmux.conf`). Suggested starter: mouse on, vi copy mode, base-index 1, escape-time 10, history-limit 50000, status bar, `Prefix + r` reload.
8. **End-to-end test from Termius (phone):** SSH in → land in Windows shell → type `wsl` → `tmux new -s work` → detach (`Ctrl+b d`) → close Termius → reopen Termius → SSH in → `wsl` → `tmux attach -t work`. **Session must still be there.** This is the success criterion.
9. **Continue tmux tutorial** (keybindings, panes, windows, copy mode) — see tutorial skill.

## WSL2 keepalive — critical context (read before step 6)

This is the single most important part for phone use. Without it, WSL2 shuts down ~10 seconds after you close all terminals/SSH, **killing every tmux session**.

- `vmIdleTimeout=-1` + `instanceIdleTimeout=-1` in `.wslconfig` is the documented fix and usually sufficient on Windows 11.
- **If `.wslconfig` alone doesn't hold the instance alive** (some builds still reap it), the community-confirmed fallback is `wsl --exec dbus-launch true` (run once after boot, leaves the instance running). Can be automated via a Windows scheduled task or a systemd user service. Sources: microsoft/WSL #10138, #9245.
- A tmux session itself also keeps WSL alive (a detached tmux server is a running process), so once tmux is up and detached, WSL tends to stay up regardless. Belt-and-suspenders: set `.wslconfig` AND rely on the tmux server.
- Apply `.wslconfig` changes with `wsl --shutdown` (not just closing the window).

## Out-of-scope, documented for later

### mosh (mobile connection resilience)
**Why you'd add it:** Plain SSH is TCP — breaks every time the phone sleeps or switches Wi-Fi↔cellular, forcing a manual reconnect + `tmux attach`. mosh is UDP, auto-reconnects silently, and does local echo (instant typing on laggy cellular). Termius supports mosh natively (host settings toggle).
**How to add later:**
1. In Ubuntu: `sudo apt install mosh`
2. Windows firewall: open UDP port range 60000–61000 (admin PowerShell firewall rule).
3. In Termius: enable mosh for the host.
**Caveat:** mosh is interactive-shell only — no SCP/SFTP/port-forwarding; use plain SSH for file transfers.

### Reboot persistence (tmux-resurrect + tmux-continuum)
**Why you'd add it:** tmux sessions live in RAM, so a full Windows reboot or `wsl --shutdown` wipes them. These plugins save/restore pane layout + running-dir state to disk and auto-restore on tmux start.
**How to add later (inside Ubuntu):**
1. Install TPM: `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
2. Add to `~/.tmux.conf`:
   ```
   set -g @plugin 'tmux-plugins/tpm'
   set -g @plugin 'tmux-plugins/tmux-resurrect'
   set -g @plugin 'tmux-plugins/tmux-continuum'
   set -g @continuum-restore 'on'
   ```
3. `Prefix + I` to install plugins. `Prefix + Ctrl-s` save / `Prefix + Ctrl-r` restore manually; continuum auto-saves.
**Limitation:** resurrect restores layout + directories, NOT the actual running processes' in-memory state. Good enough for "my windows and panes come back."

## Key files & paths

| Path | Purpose |
|---|---|
| `C:\Users\intel\.wslconfig` | **TO CREATE** — WSL2 keepalive settings. |
| `C:\ProgramData\ssh\sshd_config` | Windows OpenSSH server config (already working; no change needed for this plan). |
| `HKLM:\SOFTWARE\OpenSSH\DefaultShell` | NOT being changed (manual drop-in decision). |
| `C:\Users\intel\.tmux.conf` | Existing **psmux** config (Git Bash). Leave as-is or clean up later. |
| `/home/<ubuntu-user>/.tmux.conf` | **TO CREATE** inside WSL Ubuntu — real tmux config. |
| `~/scoop/apps/psmux/3.3.6/tmux.exe` | psmux binary (works locally only). |
| `~/scoop/shims/tmux.shim` | The shim that fails over SSH (points through the blocked junction). |

## Note on the existing psmux install

psmux still works **locally** in Git Bash; only SSH/Termius is broken for it. Options for the next session:
- **Keep it** — no harm; local `tmux` (psmux) and WSL `tmux` (real) live in separate environments with separate homes/configs, no collision.
- **Remove it** — `scoop uninstall psmux` if you'd rather not maintain two tmux configs.
This is a minor housekeeping decision, not blocking.

## Suggested skills for next session

- **`tutorial`** — continue executing the tmux setup plan one step at a time (the primary skill for this work).
- **`create-execution-plan`** — optional, if you want a formal PLAN.md from this handoff before executing.
- **`grill-with-docs`** — optional, to stress-test the WSL keepalive / SSH approach against edge cases before committing.

## Success criteria for the next session

From a phone (Termius), the user can: SSH in → `wsl` → `tmux attach -t work` → see their previous session intact after closing and reopening Termius. If that round-trip holds, the setup is done.
