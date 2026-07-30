---
name: NtfyNavGuide
topics: [ntfy, notifications, push, pubsub, webhook, alerting]
description: "Self-hosted ntfy notification server on the VPS — setup, config, auth, and common operations"
---

# Ntfy Navigation Guide

## Overview

| Detail | Value |
|---|---|
| Container | `ntfy` (`binwiederhier/ntfy`) |
| Compose path | `/home/ntfy/docker-compose.yml` |
| System user | `ntfy` (988:983) |
| Config | `/home/ntfy/config/server.yml` |
| Host port | `127.0.0.1:8083` → container `:80` |
| External URL | `https://vmi3326176.tailf94009.ts.net:3000` (Tailscale Serve) |
| Auth | enabled — `deny-all` by default |
| Auth DB | `/home/ntfy/data/user.db` (mounted as `/var/lib/ntfy/user.db`) |
| Cache | `/home/ntfy/cache/cache.db` |
| Attachments | `/home/ntfy/cache/attachments/` |

## Config (`server.yml`)

```
base-url: "https://vmi3326176.tailf94009.ts.net:3000"
listen-http: ":80"
cache-file: "/var/cache/ntfy/cache.db"
attachment-cache-dir: "/var/cache/ntfy/attachments"
auth-file: "/var/lib/ntfy/user.db"
auth-default-access: "deny-all"
behind-proxy: true
```

- `behind-proxy: true` is required because Tailscale Serve sits in front. Without it, rate-limiting and IP-based features break.
- `auth-default-access: deny-all` means unauthenticated clients get nothing — every topic requires explicit ACL entries or an admin user.

## Compose file

Key details from `/home/ntfy/docker-compose.yml`:

- Runs as `user: "988:983"` (the `ntfy` system user — no sudo, no login shell)
- Three mounted volumes: `config/`, `cache/`, and `data/` all under `/home/ntfy/`
- Healthcheck on `:80/v1/health` every 60s
- `restart: unless-stopped`

## Auth & Access Control

Auth is enabled. The user DB lives at `/home/ntfy/data/user.db`.

### Managing users

```bash
# Add an admin (full read-write to all topics)
sudo docker exec -it ntfy ntfy user add --role=admin <username>

# Add a regular user (ACL-controlled)
sudo docker exec -it ntfy ntfy user add <username>

# Change password
sudo docker exec -it ntfy ntfy user change-pass <username>

# List all users
sudo docker exec -it ntfy ntfy user list
```

### Managing topic access

```bash
# Grant user read-write to a topic
sudo docker exec -it ntfy ntfy access <username> <topic> read-write

# Grant anonymous read-only to a topic
sudo docker exec -it ntfy ntfy access everyone <topic> read-only

# View all ACL entries
sudo docker exec -it ntfy ntfy access
```

### Permissions reference

| Permission | Alias | Can publish | Can subscribe |
|---|---|---|---|
| `read-write` | `rw` | ✓ | ✓ |
| `read-only` | `read`, `ro` | ✗ | ✓ |
| `write-only` | `write`, `wo` | ✓ | ✗ |
| `deny` | `none` | ✗ | ✗ |

> **Admin users bypass all ACL entries.** An admin can read/write to every topic without any ACL rules.

## Web App

The web UI is served by the ntfy container itself. Navigate to:

```
https://vmi3326176.tailf94009.ts.net:3000
```

> **Always use the self-hosted URL above — never `https://ntfy.sh`.** Chrome blocks cross-origin requests from `ntfy.sh` to a private Tailscale address (Private Network Access / CORS policy). Using the self-hosted URL keeps the web app and API on the same origin, avoiding the block entirely.

The web app stores settings and subscribed topics in the browser's localStorage. If the Subscribe button stops working or the UI behaves oddly, clear site data for the ntfy URL and reload.

## Publishing & Subscribing

```bash
# Publish from CLI (authenticated)
curl -u <username>:<password> -d "Hello world" https://vmi3326176.tailf94009.ts.net:3000/<topic>

# Subscribe from CLI (stream)
curl -u <username>:<password> -s https://vmi3326176.tailf94009.ts.net:3000/<topic>/json
```

## Docker Operations

```bash
# Restart after config changes
cd /home/ntfy && sudo docker compose up -d --force-recreate

# Logs
sudo docker logs ntfy --tail 30
sudo docker logs ntfy -f

# Health check
curl http://localhost:8083/v1/health
```

## Gotchas

> **ntfy.sh web app vs self-hosted:** The public web app at `ntfy.sh/app` cannot subscribe to a self-hosted server on a Tailscale/private IP. This produces a CORS "local address space" error. Always use the web UI at your own server's URL.

> **`behind-proxy` must stay `true`.** Tailscale Serve is a reverse proxy. If this is set to `false`, rate limiting will apply to Tailscale's internal IP instead of the real client, breaking multi-device subscriptions.

> **`auth-default-access: deny-all` means everything is locked down.** If you create a new topic and can't subscribe or publish, you need an ACL entry for it — or use an admin account.

> **Browser notifications only work in Chrome, Edge, and Opera.** Firefox and Safari on desktop have limited or no support for the Web Push / notification actions that ntfy uses. See [ntfy web docs](https://docs.ntfy.sh/subscribe/web/) for the full compatibility table.
