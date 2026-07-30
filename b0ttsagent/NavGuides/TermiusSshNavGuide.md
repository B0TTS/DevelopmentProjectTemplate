---
name: TermiusSshNavGuide
topics: [ssh, openssh, termius, windows, phone, remote-access, ssh-keys, tailscale, local-network]
description: "SSH from a phone (Termius) into the Windows laptop over local WiFi — OpenSSH Server, firewall, Private network profile, and admin key auth. Laptop account is a passwordless Microsoft account, so password auth is impossible; key auth is the only path."
---

# Termius SSH to Laptop Navigation Guide V1.0

> Covers SSH **into the Windows laptop** (`b0tts`) from a phone on the same WiFi. For VPS/Docker SSH conventions see [VpsNavGuide](VpsNavGuide.md).

## Overview

| Property | Value |
|---|---|
| **Laptop hostname** | `b0tts` |
| **SSH username** | `intel` (local part of `b0tts\intel`) |
| **Laptop WiFi IP (LAN)** | `192.168.1.142` (DHCP — may change) |
| **Tailscale IP (stable alt)** | `100.118.41.42` |
| **WiFi SSID** | `SpectrumSetup-5179` |
| **SSH port** | `22` |
| **Auth method** | SSH key only (ed25519) — **password auth impossible** |
| **Client app** | Termius (phone) |
| **sshd service** | `Running`, `Automatic` |

## OpenSSH Server (sshd)

Windows OpenSSH Server optional feature, installed and running.

| Property | Value |
|---|---|
| **Service** | `sshd` (OpenSSH SSH Server) |
| **Status** | Running, auto-start on boot |
| **Config file** | `C:\ProgramData\ssh\sshd_config` (default) |
| **Logging** | Default (ETW) — DEBUG3 file logging was used to diagnose, then reverted |

```powershell
# Check status
Get-Service sshd
# Restart after config changes
Restart-Service sshd
```

## Windows Firewall

Built-in `OpenSSH-Server-In-TCP` rule allows inbound TCP/22. Scoped to the **Private** profile only.

```powershell
Get-NetFirewallRule -Name OpenSSH-Server-In-TCP | Select-Object Name, Profile, Enabled
Get-NetFirewallRule -Name OpenSSH-Server-In-TCP | Get-NetFirewallPortFilter
```

> **Gotcha:** the firewall rule is Private-only. When the WiFi network was classified as **Public**, the phone's packets were silently dropped → `connection timed out` (2 min). Reclassify to Private:
> ```powershell
> Get-NetConnectionProfile -InterfaceAlias Wi-Fi | Set-NetConnectionProfile -NetworkCategory Private
> ```

## Network Profile

| Interface | Network | Category |
|---|---|---|
| Wi-Fi | `SpectrumSetup-5179 2` | Private |
| Tailscale | `Tailscale` | Private |

```powershell
Get-NetConnectionProfile | Select-Object Name, NetworkCategory
```

## SSH Key Authentication

`intel` is an **administrator** account, so the public key lives in the shared admin file, not the per-user `~/.ssh/authorized_keys`.

| Property | Value |
|---|---|
| **Key file** | `C:\ProgramData\ssh\administrators_authorized_keys` |
| **Key type** | ed25519 (generated in Termius) |
| **Required ACL** | `Administrators:F` + `SYSTEM:F` only (inheritance removed) |
| **Per-user file** | `C:\Users\intel\.ssh\authorized_keys` — **ignored for admins** |

```powershell
# Verify the key + ACL
Get-Content C:\ProgramData\ssh\administrators_authorized_keys
icacls C:\ProgramData\ssh\administrators_authorized_keys
```

> **Gotcha:** sshd **silently ignores** `administrators_authorized_keys` if the ACL is too permissive (inherited Users/Authenticated-Users read). Must be Administrators + SYSTEM only:
> ```powershell
> icacls C:\ProgramData\ssh\administrators_authorized_keys /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'
> ```

## Termius Client (phone)

| Field | Value |
|---|---|
| Protocol | SSH |
| Host | `192.168.1.142` (or `100.118.41.42` via Tailscale) |
| Port | `22` |
| Username | `intel` |
| Password | *(empty — not used)* |
| SSH Key | ed25519 key generated in Termius Keychain, linked to the host |

> **Gotcha — passwordless Microsoft account:** `intel` is a personal Microsoft account (MSA) set to **passwordless** (passkey via Bitwarden + Windows Hello). The account has **no password**, so SSH password auth fails with error `1326` no matter what is typed. The Windows Hello "only allow Windows Hello" toggle (`DevicePasswordLessBuildVersion = 0`, already off) is **not** the fix — key auth is the only working path. See sshd log signature: `Windows authentication failed for user: intel domain: . error: 1326`.

> **Gotcha — Azure AD ≠ personal MSA:** the `azuread\user@email@host` username workaround is for **work/school Azure AD** accounts only. `intel` is a personal MSA (`AzureAdJoined: NO`), so plain `intel` is the correct username and no special prefix is needed.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `connection timed out` (2 min) | Network profile Public, firewall dropping port 22 | Set WiFi to Private |
| `Authentication failed (password)` ×3 | Passwordless MSA — no password exists | Use SSH key auth |
| `Windows authentication failed ... error: 1326` (sshd log) | Bad/no password | Key auth (or add a password at account.microsoft.com) |
| Key auth fails, falls through to password | `administrators_authorized_keys` ACL too open, or wrong file | Fix ACL to Admins+SYSTEM only; restart sshd |
| Works on LAN but IP keeps changing | DHCP reassigns `192.168.1.x` | Use Tailscale IP `100.118.41.42` (stable, also works off-WiFi) |

### Enabling/disabling DEBUG logging (temporary)

```powershell
# Enable file DEBUG3 logging (edit C:\ProgramData\ssh\sshd_config):
#   SyslogFacility LOCAL0
#   LogLevel DEBUG3
# Then: Restart-Service sshd
# Log appears at: C:\ProgramData\ssh\logs\sshd.log
# Revert by commenting those lines back out and restarting sshd.
```
