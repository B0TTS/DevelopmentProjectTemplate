---
name: LocalLobeHubNavGuide
topics: [lobehub, lobe-chat, docker, wsl, openrouter, llm, windows]
description: "Lobe Chat self-hosted locally on Windows via Docker Desktop + WSL2 Ubuntu — PostgreSQL, Redis, RustFS, SearXNG, OpenRouter API — manual start/stop with desktop shortcuts"
---

# Local Lobe Chat Navigation Guide V1.0

> Docker conventions for the VPS are in [VpsNavGuide](VpsNavGuide.md). This guide covers the local Windows/WSL instance only.
>
> **Superseded:** The live Lobe Chat instance has been migrated to the VPS. See [VpsLobeHubNavGuide](VpsLobeHubNavGuide.md) for the current production setup. This local instance may be retained for reference or decommissioned.

## Overview

| Property | Value |
|---|---|
| **App directory** | `~/lobehub/` (Ubuntu WSL) |
| **Windows path** | `\\wsl$\Ubuntu\home\jonah\lobehub\` |
| **Access URL** | `http://localhost:3210` |
| **API provider** | OpenRouter (key stored in browser settings) |
| **RustFS admin** | `http://localhost:9001` — user `admin`, password `6771e9b2` |
| **Auto-start** | Disabled — `restart: "no"` on all services |

## Stack

| Container | Image | Port |
|---|---|---|
| `lobehub` | `lobehub/lobehub` | `3210` |
| `lobe-postgres` | `paradedb/paradedb:latest-pg17` | `5432` |
| `lobe-redis` | `redis:7-alpine` | `6379` |
| `lobe-rustfs` | `rustfs/rustfs:latest` | `9000`, `9001` |
| `lobe-searxng` | `searxng/searxng` | (internal only) |

All containers on the `lobehub_lobe-network` bridge network.

## Start / Stop

### Desktop shortcuts (Windows)

- **Lobe Chat Start** — double-click. Starts all containers + opens browser to `http://localhost:3210`
- **Lobe Chat Stop** — double-click. Runs `docker compose down`

### Terminal (Ubuntu WSL)

```bash
lobe-up      # start + print URL
lobe-down    # stop all containers
lobe-logs    # tail lobehub logs
```

Aliases are defined in `~/.bashrc`.

### Manual

```bash
cd ~/lobehub && docker compose up -d     # start
cd ~/lobehub && docker compose down      # stop
```

## PostgreSQL

| Setting | Value |
|---|---|
| **Image** | `paradedb/paradedb:latest-pg17` (pgvector + pg_search) |
| **Database** | `lobechat` |
| **User** | `postgres` |
| **Password** | `uWNZugjBqixf8dxC` |
| **Data volume** | `./data/` (bind mount) |

### Connect

```bash
docker compose exec postgresql psql -U postgres -d lobechat
```

## RustFS (S3 file storage)

| Setting | Value |
|---|---|
| **Access key** | `admin` |
| **Secret key** | `6771e9b2` |
| **Bucket** | `lobe` |
| **Endpoint (from browser)** | `http://localhost:9000` |
| **Admin console** | `http://localhost:9001` |
| **Data volume** | `rustfs-data` (named) |

> The `rustfs-init` service was removed from `docker-compose.yml` — its `bucket.config.json` had a JSON key `"ID"` that should be `"Id"`, causing policy creation to fail. The bucket itself was created successfully in an earlier run and persists in the volume. If the volume is ever wiped, the bucket must be recreated via `mc mb`.

## SearXNG (local web search)

Running internally — no host port. Enable in Lobe Chat settings to search the web from conversations without any external API key.

## Environment (.env)

Key variables in `~/lobehub/.env`:

| Variable | Value |
|---|---|
| `LOBE_PORT` | `3210` |
| `APP_URL` | `http://localhost:3210` |
| `INTERNAL_APP_URL` | `http://localhost:3210` |
| `LOBE_DB_NAME` | `lobechat` |
| `POSTGRES_PASSWORD` | `uWNZugjBqixf8dxC` |
| `S3_ENDPOINT` | `http://localhost:9000` |
| `RUSTFS_ACCESS_KEY` | `admin` |
| `RUSTFS_SECRET_KEY` | `6771e9b2` |
| `RUSTFS_LOBE_BUCKET` | `lobe` |
| `KEY_VAULTS_SECRET` | *(set, do not change)* |
| `AUTH_SECRET` | *(set)* |

> `DATABASE_URL` is constructed in `docker-compose.yml`, not in `.env`: `postgresql://postgres:${POSTGRES_PASSWORD}@postgresql:5432/${LOBE_DB_NAME}`

## Files

```
~/lobehub/
├── docker-compose.yml    ← stack definition (rustfs-init removed, restart: "no")
├── .env                  ← secrets and config
├── bucket.config.json    ← unused (RustFS policy fix)
├── searxng-settings.yml  ← SearXNG config
├── data/                 ← PostgreSQL data (bind mount)
```

Named volumes: `redis_data`, `rustfs-data`.

## API keys

OpenRouter key is stored in the browser via Lobe Chat's **Settings → Language Model → OpenRouter** — not in `.env`. To add another provider, use the same settings UI.

## Gotchas

> **Don't edit `docker-compose.yml` with `sed` alone.** The indentation is sensitive and `sed` can mangle YAML. Edit via Windows-side tools (`\\wsl$\Ubuntu\home\jonah\lobehub\`) or use `docker compose config` to validate after every change.

> **The `lobe` service must include `DATABASE_URL` in its `environment:` block.** An earlier sed accidentally deleted the entire environment section. If the lobehub container crashes with "DATABASE_URL is not set," this is why.

> **The stack does not auto-start on boot.** All services use `restart: "no"`. You must explicitly start it via the desktop shortcut or `lobe-up`.

> **SearXNG connectivity check may timeout in the Lobe Chat settings UI** — this is cosmetic. SearXNG works in actual chat usage.

> **The OpenRouter connectivity check button can return 404** even when the key and connection are valid. Skip the check and test with a real chat message instead.

## Update

```bash
cd ~/lobehub && docker compose pull && docker compose up -d
```

## Backup

PostgreSQL data is at `~/lobehub/data/`. Back it up with:

```bash
docker compose exec postgresql pg_dump -U postgres lobechat > ~/lobechat-backup.sql
```

RustFS files:

```bash
docker compose exec rustfs tar czf /tmp/backup.tar.gz /data
docker cp lobe-rustfs:/tmp/backup.tar.gz ~/rustfs-backup.tar.gz
```
