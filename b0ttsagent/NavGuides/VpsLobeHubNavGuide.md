---
name: VpsLobeHubNavGuide
topics: [lobehub, lobe-chat, docker, cloudflare-tunnel, github-oauth, postgresql, paradedb, vps]
description: "Lobe Chat self-hosted on VPS via Docker — ParadeDB PostgreSQL, Redis, RustFS, SearXNG, Cloudflare Tunnel, GitHub OAuth — served at chat.b0tts.me"
---

# Lobe Chat VPS Navigation Guide V1.1

> VPS conventions (Docker, system users, Tailscale) are in [VpsNavGuide](VpsNavGuide.md). The local Windows/WSL instance is in [LocalLobeHubNavGuide](LocalLobeHubNavGuide.md) (superseded).

## Overview

| Property | Value |
|---|---|
| **App directory** | `/home/lobehub/` |
| **System user** | `lobehub` (uid 984, gid 979) |
| **Access URL** | `https://chat.b0tts.me` |
| **Auth** | GitHub OAuth via Better Auth (Lobe Chat 2.0+) |
| **Tunnel** | `lobe-gate` (dedicated Cloudflare tunnel) + Cloudflare Access gate |
| **Restart policy** | `unless-stopped` on all services |
| **RAM freed for this** | Minecraft (1.97 GiB), Open WebUI (950 MiB), standalone SearXNG (136 MiB) — all stopped, all `restart: "no"` |

## Stack

| Container | Image | Memory Limit |
|---|---|---|
| `lobe-paradedb` | `paradedb/paradedb:0.24.0-pg17` | 512m |
| `lobe-redis` | `redis:7-alpine` | 128m |
| `lobe-rustfs` | `rustfs/rustfs:latest` | 256m |
| `lobe-searxng` | `searxng/searxng:latest` | 256m |
| `lobehub` | `lobehub/lobehub:latest` | 1024m |
| `lobe-tunnel` | `cloudflare/cloudflared:latest` | 64m |

All containers on the `lobehub_internal` bridge network. **No host ports** exposed — all traffic enters through Cloudflare Tunnel.

## Start / Stop

```bash
# Start all
cd /home/lobehub && sudo docker compose --env-file .env up -d

# Stop all
cd /home/lobehub && sudo docker compose down

# Restart lobehub only (pick up config/env changes)
cd /home/lobehub && sudo docker compose --env-file .env up -d lobehub

# Logs
sudo docker logs lobehub --tail 30
```

## PostgreSQL (paradedb)

| Setting | Value |
|---|---|
| **Image** | `paradedb/paradedb:0.24.0-pg17` (pgvector + pg_search) |
| **Database** | `lobechat` |
| **User** | `postgres` |
| **Password** | `POSTGRES_PASSWORD` in `.env` |
| **Data volume** | `./pgdata/` (bind mount, owned by uid 70) |

### Connect

```bash
sudo docker compose --env-file .env exec paradedb psql -U postgres -d lobechat
```

## RustFS (S3 file storage)

| Setting | Value |
|---|---|
| **Access key** | `admin` |
| **Secret key** | `RUSTFS_SECRET_KEY` in `.env` |
| **Bucket** | `lobe` |
| **Endpoint (internal)** | `http://rustfs:9000` |
| **Data volume** | `rustfs_data` (named) |

> The `rustfs-init` container was removed from docker-compose.yml. The `lobe` bucket was created manually. If the volume is wiped, recreate it:
> ```bash
> source /home/lobehub/.env && sudo docker run --rm --network lobehub_lobehub_internal \
>   -e "MC_HOST_local=http://admin:${RUSTFS_SECRET_KEY}@rustfs:9000" \
>   --entrypoint /bin/sh minio/mc:latest -c "mc mb --ignore-existing local/lobe"
> ```

> RustFS health endpoint (`/minio/health/live`) returns 403 without auth, which broke `curl -f` health checks. The healthcheck is now `CMD-SHELL exit 0` (pass-through). RustFS works fine — the health status is cosmetic.

## SearXNG (local web search)

| Setting | Value |
|---|---|
| **Config file** | `/home/lobehub/searxng-settings.yml` |
| **Access** | Internal only (no host port) |

## Cloudflare Tunnel

| Setting | Value |
|---|---|
| **Tunnel name** | `lobe-gate` |
| **Image** | `cloudflare/cloudflared:latest` |
| **Token** | `CLOUDFLARED_TUNNEL_TOKEN` in `.env` |
| **Ingress** | `chat.b0tts.me` → `http://lobehub:3210` |

> Dedicated tunnel — separate from `sigma_gate` which serves `b0tts.dev`. DNS: `chat` CNAME → tunnel endpoint (proxied).
>
> **Cloudflare Access is enabled on top of the tunnel** to gate signups. Without it, any GitHub user could create an account (see Auth section). Access has an **Allow** policy for `justgoodyt@gmail.com` and a **Bypass** policy for URL path `/api/auth/*` so the GitHub OAuth callback flow is not intercepted.

## Authentication (Better Auth)

| Property | Value |
|---|---|
| **SSO Provider** | GitHub OAuth |
| **Env vars** | `AUTH_GITHUB_ID`, `AUTH_GITHUB_SECRET` |
| **Callback URL** | `https://chat.b0tts.me/api/auth/callback/github` |
| **User gate** | Cloudflare Access (Allow policy for `justgoodyt@gmail.com`, Bypass policy for `/api/auth/*`) |

> **Signups are restricted via Cloudflare Access**, not via Lobe Chat env vars. The `AUTH_ALLOWED_EMAILS` env var is set in `.env` but is **ineffective** — confirmed bug in the current Better Auth implementation where registration is hardcoded as enabled and ignores the allowlist (see lobehub/lobehub#11979). Don't rely on it. Cloudflare Access is the real gate.
>
> The previous Cloudflare Access attempt broke because it intercepted `/api/auth/*` and returned an HTML login page instead of letting GitHub's OAuth redirect through (NextAuth/Better Auth couldn't parse the HTML, failed with `AdapterError`). The fix is a **Bypass policy scoped to URL path `/api/auth/*`** so the OAuth callback reaches Lobe Chat untouched. The trailing `*` is critical — `/api/auth/` alone does NOT match `/api/auth/callback/github`.
>
> To delete an unwanted user that slipped in before the gate: delete their `sessions` rows (FK `user_id` is **text**), then delete the `users` row (PK `id` is **text** — quote it):
> ```bash
> sudo docker compose --env-file .env exec paradedb psql -U postgres -d lobechat \
>   -c "DELETE FROM sessions WHERE user_id = '<id>';" \
>   -c "DELETE FROM users WHERE id = '<id>';" \
>   -c "SELECT id, email, created_at FROM users;"
> ```

## Environment (.env)

| Variable | Purpose |
|---|---|
| `APP_URL` | `https://chat.b0tts.me` |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `KEY_VAULTS_SECRET` | Encryption key for stored credentials |
| `AUTH_SECRET` | Better Auth session encryption |
| `AUTH_GITHUB_ID` | GitHub OAuth client ID |
| `AUTH_GITHUB_SECRET` | GitHub OAuth client secret |
| `AUTH_ALLOWED_EMAILS` | `justgoodyt@gmail.com` — **set but ineffective** (Better Auth bug; gate is enforced by Cloudflare Access instead) |
| `CLOUDFLARED_TUNNEL_TOKEN` | Tunnel token for `lobe-gate` |
| `RUSTFS_ACCESS_KEY` | `admin` |
| `RUSTFS_SECRET_KEY` | RustFS secret key |

> **KEY_VAULTS_SECRET and AUTH_SECRET must be exactly 44 characters** (`openssl rand -base64 32`). Any other length causes "Invalid key length" errors. Do not change these after data is in the database.

## Files

```
/home/lobehub/
├── docker-compose.yml      ← stack definition
├── .env                    ← secrets and config
├── searxng-settings.yml    ← SearXNG config
├── backup.sh               ← daily pg_dump script
├── pgdata/                 ← PostgreSQL data (bind mount)
└── backups/                ← daily dump files
```

Named volumes: `redis_data`, `rustfs_data`.

## Backups

| Setting | Value |
|---|---|
| **Method** | `pg_dump` (gzip compressed) |
| **Schedule** | Daily at 12:00 (noon) |
| **Retention** | 14 days |
| **Cron file** | `/etc/cron.d/lobehub-backup` |
| **Script** | `/home/lobehub/backup.sh` |

```bash
sudo bash /home/lobehub/backup.sh          # manual run
ls -lh /home/lobehub/backups/              # list backups
```

## Gotchas

> **`lobehub/lobe-chat-database` is deprecated — frozen at v1.143.3.** The `latest` tag on Docker Hub was last pushed January 25, 2026 and silently fails to update. V2 uses `lobehub/lobehub:latest`. The `-database` image was renamed in LobeChat 2.0. Migration requires: change the image name, remove deprecated env vars (`NEXT_PUBLIC_SERVICE_MODE`, `NEXT_AUTH_SSO_PROVIDERS`, `ACCESS_CODE`, `NEXTAUTH_URL`, `NEXT_AUTH_SECRET`, `AUTH_URL`), add `AUTH_SSO_PROVIDERS: github` and `INTERNAL_APP_URL`.

> **S3 variable names differ between images.** The database image requires `S3_ACCESS_KEY_ID` / `S3_SECRET_ACCESS_KEY` in addition to `S3_ACCESS_KEY` / `S3_SECRET_KEY`. Missing the ID/ACCESS variants causes "S3 environment variables are not set completely" errors.

> **Database image OOM'd at 512m.** Bumped to `mem_limit: 1024m` with `NODE_OPTIONS: --max-old-space-size=768`.

> **Cloudflare Access works if you add a Bypass policy for `/api/auth/*`.** Without the bypass (and the trailing `*` is critical — `/api/auth/` alone does NOT match `/api/auth/callback/github`), Access intercepts the OAuth callback and returns an HTML login page instead of letting GitHub's redirect through. NextAuth/Better Auth can't parse HTML as JSON and fails with `AdapterError`. **Current setup:** Allow policy for `justgoodyt@gmail.com` + Bypass policy for URL path `/api/auth/*`. This is the working configuration — do not remove the bypass.

> **MCP/Agent marketplace discovery is broken for self-hosted instances — by design.** The marketplace API (`market.lobehub.com`) requires a trust token (`x-lobe-trust-token` / `accessToken`) issued only to official LobeHub Cloud instances. There is **no env var** to configure it for self-hosted deployments; related issues (lobehub/lobehub#13686, #13435) are closed as `not_planned`. The discover/MCP list tab shows "Failed to fetch mcp list" / "Missing bearer token" and cannot be fixed from the self-hosted side. **Workaround:** add MCP servers manually by URL/command (Settings → MCP → Add custom), sourcing them from github.com/modelcontextprotocol/servers or mcp.so.

> **ACCESS_CODE is removed in v2.** The `ACCESS_CODE` env var no longer exists. Cloudflare Access is the gate (see Cloudflare Tunnel section). Remove `ACCESS_CODE` from `docker-compose.yml` and `.env` when migrating from v1.

> **v2 crashes on deprecated env vars.** LobeChat 2.x detects deprecated v1 variables at boot (`NEXT_AUTH_SECRET`, `AUTH_URL`, etc.) and refuses to start — looping `Restarting (1)`. The error message lists exactly which vars to remove. Check `sudo docker logs lobehub --tail 20` if the container won't stay up.

> **Missing `AUTH_SSO_PROVIDERS` = no GitHub login button.** Better Auth won't show any SSO provider unless `AUTH_SSO_PROVIDERS: github` is set in `docker-compose.yml` (compose-level, not `.env`). Without it, the signin page only shows email/password.

> **`INTERNAL_APP_URL` is required for Docker deployments.** Set it to the same value as `APP_URL` in `docker-compose.yml`. Missing it can break features like AI image generation.

> **Don't edit `docker-compose.yml` with sed for multi-line changes.** YAML indentation is sensitive. Sed multiline operations or substitutions that touch indentation can silently break the file. Use `nano` or a proper editor. Validate with `sudo docker compose --env-file .env config` after any edit.

> **ParadeDB version is pinned.** Image tagged `0.24.0-pg17`, not `latest`. Update the tag manually in docker-compose.yml when upgrading paradedb.

> **QStash warnings are cosmetic.** `[Upstash QStash] client token is not set` appears repeatedly in logs — this is for scheduled-task features that aren't configured. Harmless, ignore it.

## Update

```bash
# Pull + force-recreate (required — up -d alone won't pick up new images)
cd /home/lobehub && sudo docker compose --env-file .env pull && sudo docker compose --env-file .env up -d --force-recreate

# Lobehub-only update (faster, doesn't touch databases)
cd /home/lobehub && sudo docker compose --env-file .env pull lobehub && sudo docker compose --env-file .env up -d --force-recreate lobehub
```
