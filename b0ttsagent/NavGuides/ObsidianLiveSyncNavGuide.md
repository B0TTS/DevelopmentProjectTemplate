---
name: ObsidianLiveSyncNavGuide
topics: [obsidian, livesync, couchdb, sync, vault, tailscale-serve, e2e-encryption]
description: "Reference for the Obsidian Self-hosted LiveSync deployment — CouchDB on the VPS with E2E-encrypted sync across devices"
---

# Obsidian LiveSync Navigation Guide V1.0

## Overview

| Property | Value |
|---|---|
| Backend | CouchDB 3.5.2 (Docker, VPS) |
| Container | `couchdb`, uid `5984:5984`, `restart: unless-stopped` |
| Host bind | `127.0.0.1:5984` (localhost only) |
| Public exposure | None — Tailscale Serve HTTPS only |
| Sync endpoint | `https://vmi3326176.tailf94009.ts.net:3001` |
| Tailscale Serve port | `3001` |
| Database | `obsidian-vault` |
| Encryption | E2E ON (256-bit AES-GCM) + path obfuscation |
| Sync mode | LiveSync (real-time bidirectional) |
| Devices configured | Laptop (first/push), Phone (pull) |
| Devices pending | PC (backlogged) |
| Docs on CouchDB | 110 (encrypted) |

> VPS access, Docker conventions, Tailscale Serve basics, and tailnet ACLs are documented in `VpsNavGuide.md`. This guide covers only the Obsidian LiveSync specifics.

## CouchDB

CouchDB runs on the VPS as a Docker container under the `couchdb` system user. Data and config live at `/home/couchdb/`.

| Path | Owner | Purpose |
|---|---|---|
| `/home/couchdb/.env` | `couchdb:couchdb` (600) | Admin creds (`COUCHDB_USER`, `COUCHDB_PASSWORD`) |
| `/home/couchdb/docker-compose.yml` | `couchdb:couchdb` | Compose file (image `couchdb:3.5.2`, `127.0.0.1:5984:5984`, volumes for data + etc/local.d) |
| `/home/couchdb/couchdb-data` | `5984:5984` | CouchDB data volume |
| `/home/couchdb/couchdb-etc` | `5984:5984` | `etc/local.d` volume |

| System user | uid:gid |
|---|---|
| `couchdb` | 982:977 (no login shell, owns compose/env only) |

> The data dirs are owned by `5984:5984` (the container's internal uid), NOT the host `couchdb` user. The host `couchdb` user only owns the compose/env files. If the data dirs aren't chowned to `5984:5984`, the container can't write and fails to start.

### Operating CouchDB

```bash
# Start
cd /home/couchdb && sudo docker compose up -d

# Stop
cd /home/couchdb && sudo docker compose down

# Restart / pick up compose changes
cd /home/couchdb && sudo docker compose up -d --force-recreate

# Logs
sudo docker logs couchdb --tail 30
sudo docker logs couchdb -f

# Update image
cd /home/couchdb && sudo docker compose pull && sudo docker compose up -d
```

### Checking the database

```bash
# DB metadata (doc_count, sizes) — does NOT show note contents (E2E encrypted)
source <(sudo cat /home/couchdb/.env) && curl -s -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" http://localhost:5984/obsidian-vault | python3 -m json.tool | head -15

# List all databases
source <(sudo cat /home/couchdb/.env) && curl -s -u "${COUCHDB_USER}:${COUCHDB_PASSWORD}" http://localhost:5984/_all_dbs

# Welcome / version check (returns 401 if require_valid_user is on — that's expected)
curl http://localhost:5984
```

### CouchDB configuration (set by couchdb-init.sh)

| Config key | Value |
|---|---|
| `_cluster_setup` | single-node enabled |
| `chttpd/require_valid_user` | `true` |
| `chttpd_auth/require_valid_user` | `true` |
| `httpd/WWW-Authenticate` | `Basic realm="couchdb"` |
| `httpd/enable_cors` | `true` |
| `chttpd/enable_cors` | `true` |
| `chttpd/max_http_request_size` | `4294967296` (4GB) |
| `couchdb/max_document_size` | `50000000` (50MB) |
| `cors/credentials` | `true` |
| `cors/origins` | `app://obsidian.md,capacitor://localhost,http://localhost` |

> `cors/origins` must include `app://obsidian.md` (desktop), `capacitor://localhost` (mobile), and `http://localhost` (dev). Obsidian's web requests get blocked without CORS configured for these exact origins. CouchDB handles CORS itself — do NOT process CORS on any reverse proxy in front of it.

> `couchdb-init.sh` does NOT create the database — the LiveSync plugin creates `obsidian-vault` during the Minimal Setup wizard on the first device.

## Tailscale Serve

CouchDB is exposed to the tailnet only via Tailscale Serve HTTPS on port `3001`, proxying `localhost:5984`.

```bash
# Current serve mappings
tailscale serve status

# Add (already done)
sudo tailscale serve --https=3001 --bg http://localhost:5984

# Remove
tailscale serve --https=3001 off
```

> Port `3001` was chosen because `:443`, `:3000`, and `:8443` were already taken by other Tailscale Serve entries. `:3001` is in the tailnet ACL allow-list (see `VpsNavGuide.md`).

> A `401 Unauthorized` response from `https://...ts.net:3001` (with `Server: CouchDB/3.5.2` header) is SUCCESS — it proves the full path works AND that `require_valid_user` is enforced. Do not mistake it for a failure.

## LiveSync Plugin

The Self-hosted LiveSync community plugin (by **vrtmrz**) runs inside each Obsidian vault and talks to CouchDB. Configured via the **Minimal Setup** wizard on the first device; subsequent devices import a **setup URI**.

### LiveSync settings (configured values)

| Setting | Value | Why |
|---|---|---|
| Remote type | CouchDB | — |
| URI | `https://vmi3326176.tailf94009.ts.net:3001` | Tailscale Serve endpoint |
| Database name | `obsidian-vault` | — |
| Username | `admin` | From `/home/couchdb/.env` |
| End-to-End Encryption | ON (256-bit AES-GCM) | Vault is sensitive |
| Path Obfuscation | ON | Encrypts filenames on server |
| Sync preset | LiveSync | Real-time bidirectional |
| Handle files as Case-Sensitive | `false` | Windows devices (case-insensitive FS) |
| Per file saved customization sync | ON | — |
| Enhance chunk size | `60` (6MB) | v3 Rabin-Karp + CouchDB default max chunk |
| Send all chunks before replication | ON | Full vault on server before ongoing sync |

### Renamed buttons (plugin versions)

| Old name | New name |
|---|---|
| Open setup URI | Use the copied setup URI |
| Copy setup URI | Copy current settings as a new setup URI |
| Setup Wizard | Minimal Setup |
| Check database configuration | Check and Fix database configuration |

> On the FIRST device, use the **"Start"** button (opens Minimal Setup wizard) to enter connection fields manually. The **"Use the copied setup URI"** / "Import Setup URI" button is for SUBSEQUENT devices only — it errors with "setup URI appears to not be valid" if you don't have one yet.

> After Obsidian restarts, LiveSync may show a "Tweaks Mismatched" / data comparison dialog. On the FIRST device (source of truth), choose **"Compare and take over"** — NOT "overwrite with remote data".

### The "Check and Fix database configuration" step

The Minimal Setup wizard runs 3 checks. Fix each:
1. **Handle files as Case-Sensitive** → fix to `false` (Windows compat)
2. **Per file saved customization sync** → fix to ON
3. **Enhance chunk size** → fix to `60` (6MB, v3 Rabin-Karp + CouchDB default)

## Devices

| Device | Role | Vault path | Status |
|---|---|---|---|
| Laptop (Windows) | First device (push) | `C:\Development\GameProjects\Whack Grass\Game Design Docs` | ✅ Configured, 110 docs pushed |
| Phone | Subsequent (pull) | (local container) | ✅ Self-configured via setup URI, two-way verified |
| PC (Windows) | Subsequent (pull) | (TBD) | ⏳ Backlogged — same flow as phone |

> Vault path changed during setup: was `...\Planning Docs`, now `...\Game Design Docs`. Subfolder renamed from `Whack Grass` to `Main`.

> The vault is NOT in git and is sensitive. Do not read vault contents; only check existence / `.obsidian` presence.

## Setup URI (adding subsequent devices)

The setup URI is an encrypted `obsidian://setuplivesync?settings=...` string that encodes the full LiveSync config for sharing between devices. Encrypted with its OWN passphrase (distinct from the E2E passphrase).

### Generate (on a configured device)

```
Command palette (Ctrl+P) → "Copy settings as a new setup URI" → enter setup URI passphrase → URI copied to clipboard
```

Save the URI + its passphrase OUTSIDE Obsidian (e.g., password manager secure note). Reuse the same URI for every subsequent device.

### Import (on a new device)

1. Create an empty vault + install Self-hosted LiveSync (by vrtmrz).
2. Command palette → **"Use the copied setup URI"** → paste URI → enter setup URI passphrase.
3. Answer **"Set it up as secondary or subsequent device"**.
4. Fast Setup runs → initial pull → sync begins.

## Credentials

All credentials are stored in the user's password manager. On the VPS, the CouchDB admin creds live ONLY in `/home/couchdb/.env` (never in git, never in any doc/handoff/nav-guide).

| Credential | Stored where | Used for |
|---|---|---|
| CouchDB admin user (`admin`) | `.env` + password manager | CouchDB auth |
| CouchDB admin password | `.env` + password manager | CouchDB auth |
| E2E passphrase | password manager | Decrypting vault on each device |
| Setup URI passphrase | password manager | Encrypting/decrypting the setup URI |

> The E2E passphrase and the setup URI passphrase are DIFFERENT things. The E2E passphrase encrypts vault contents (required on every device to read notes; lost = lost notes irretrievably). The setup URI passphrase only encrypts the setup URI blob for device-to-device sharing.

> Never commit credentials to git. Redact them from any handoff, nav guide, or doc.

## Key references

- LiveSync README: https://github.com/vrtmrz/obsidian-livesync/blob/main/README.md
- CouchDB on own server: https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/setup_own_server.md
- Plugin quick setup: https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/quick_setup.md
- Troubleshooting: https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md
- couchdb-init.sh: https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh
