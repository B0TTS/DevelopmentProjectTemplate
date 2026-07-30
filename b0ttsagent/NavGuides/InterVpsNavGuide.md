---
name: InterVpsNavGuide
topics: [vps, interserver, ssh, tailscale, ufw, security, hardening, ubuntu, minecraft]
description: "Reference for the InterServer VPS (vps3484597) security baseline, access, and configuration"
---

# InterServer VPS Navigation Guide

> Second VPS on the `tailf94009` tailnet. Dedicated to Minecraft hosting. See `VpsNavGuide.md` for shared conventions (Docker, system-user-per-app pattern, Tailscale Serve, compose workflow) — they apply here too.

## Overview

| Property          | Value                                   |
| ----------------- | --------------------------------------- |
| Provider          | InterServer                             |
| Provider hostname | vps3484597                              |
| Public IP         | 67.211.215.84                           |
| Tailscale hostname| interdeploymcvps.tailf94009.ts.net      |
| Tailscale IP      | 100.100.223.6                           |
| OS                | Ubuntu 26.04 LTS (Resolute Raccoon)     |
| Specs             | 12 GB RAM, 3 vCPU                       |
| Admin user        | deploy (UID 1000, GID 1000)             |
| Tailnet           | tailf94009                              |
| Purpose           | Minecraft server hosting                |

## Access

```bash
ssh deploy@interdeploymcvps.tailf94009.ts.net
# or by Tailscale IP:
ssh deploy@100.100.223.6
```

> The public IP (67.211.215.84) is **not** reachable for SSH — UFW drops everything on the public interface. Tailscale is the only way in.
>
> SSH keys are managed via Bitwarden SSH agent on the workstation. No passwords are accepted by SSH.

Recovery path if locked out: InterServer control panel → VNC/noVNC console → log in as root.

## SSH Hardening

Drop-in config at `/etc/ssh/sshd_config.d/99-hardening.conf`:

```
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
ChallengeResponseAuthentication no
PubkeyAuthentication yes
AuthenticationMethods publickey
AllowUsers deploy
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
LoginGraceTime 30
X11Forwarding no
```

```bash
# Verify hardening is in effect
sudo sshd -T | grep -iE 'permitrootlogin|passwordauthentication'
# Reload after edits
sudo systemctl reload sshd
```

> Use a drop-in file, not the main `sshd_config` — package updates won't overwrite it.

## UFW Firewall

```
Default: deny (incoming), allow (outgoing)
Rules:
  - Anywhere on tailscale0  ALLOW IN   (ACLs do the actual port gating)
```

```bash
sudo ufw status verbose
sudo ufw allow in on tailscale0      # already set
# To expose a public game port later (only if players connect over public IP):
sudo ufw allow 25565/tcp
```

> Public SSH (`allow 22/tcp`) was intentionally removed after confirming tailnet-only access. If you ever need it back temporarily: `sudo ufw allow 22/tcp`.
>
> Tailscale-only players need no extra rules — `allow in on tailscale0` already covers game ports.

## Tailscale

```bash
sudo tailscale status
sudo tailscale set --ssh=false   # standard OpenSSH over tailnet, NOT Tailscale SSH
```

- Joined tailnet `tailf94009`, hostname `interdeploymcvps`
- ACLs managed via **tags** (added in the Tailscale admin console)
- **Key expiry disabled** on this machine (prevents 180-day lockout)
- `--ssh=false`: uses standard OpenSSH on port 22 over the tailnet, matching the `VpsNavGuide` pattern

> Do **not** run `tailscale up --ssh` on this box — it intercepts port 22 and requires an SSH ACL rule, which breaks the standard-OpenSSH-over-tailnet model. If accidentally enabled, fix with `sudo tailscale set --ssh=false`.

## Automatic Updates

```bash
sudo systemctl is-enabled unattended-upgrades   # -> enabled
```

Security patches apply automatically. Application/feature updates are left for manual review.

## What was deliberately NOT installed

- **fail2ban** — skipped. SSH is tailnet-only with key-only auth; there is no public brute-force surface to ban. No bots can reach port 22.
- **Custom SSH port** — kept on 22. No public exposure means no noise to reduce; preserves muscle memory.

## Snapshots

- InterServer snapshot taken after hardening — clean restore point before the Minecraft stack was built. Re-snapshot after major stack changes.

## Gotchas from Setup

> The `.ssh` directory and `authorized_keys` ended up owned by `root:root` instead of `deploy:deploy`, which silently broke key auth after the SSH hardening reload. Fix: `sudo chown -R deploy:deploy /home/deploy/.ssh`. SSH is strict about ownership — always verify with `ls -la` after creating the directory.

> The `--ssh` flag on `tailscale up` caused `tailnet policy does not permit you to SSH to this node` because no SSH ACL existed. This box uses standard OpenSSH over the tailnet (not Tailscale SSH), so the flag must be off: `sudo tailscale set --ssh=false`.
