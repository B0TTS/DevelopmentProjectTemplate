---
name: PgwebNavGuide
topics: [pgweb, postgresql, docker, tailscale, database-admin, gui]
description: "Lightweight web-based PostgreSQL explorer hosted on the VPS, connecting to postgrest-db via the postgrest_internal Docker network"
---

# pgweb Navigation Guide V1.0

> VPS conventions (Docker, system users, Tailscale) are in [VpsNavGuide](VpsNavGuide.md). The PostgreSQL instance is documented in [PostgrestApiGuide](PostgrestApiGuide.md).

> ⚠️ **DECOMMISSIONED — planned for removal.** pgweb was set up once and never used. The container currently has **no port mapping** (it is not bound to 3001). Port `3001` is now claimed by **CouchDB / Obsidian LiveSync** via Tailscale Serve HTTPS (see `ObsidianLiveSyncNavGuide.md`). Do **not** re-add the `0.0.0.0:3001` mapping from this guide — it will collide with CouchDB's Tailscale Serve entry. Planned replacement: **Supabase** (not yet set up). To tear down: `cd /home/pgweb && sudo docker compose down`, then remove `/home/pgweb` and the `pgweb` system user. The guide below is kept as a reference for the teardown.

## Overview

| Property | Value |
|---|---|
| **App directory** | `/home/pgweb/` |
| **System user** | `pgweb` (uid 985, gid 980) |
| **Container** | `pgweb` (`sosedoff/pgweb:latest`) |
| **pgweb version** | v0.17.0 |
| **Internal port** | 8081 |
| **Host port** | *(none — unmapped; was `0.0.0.0:3001`, now taken by CouchDB)* |
| **Access URL** | *(none — not currently exposed)* |
| **Network** | `postgrest_internal` (external, shared with postgrest stack) |
| **Auth** | None — relies on Tailscale network access control |

## Connection

pgweb auto-connects on startup via `PGWEB_DATABASE_URL`. No login screen.

| Setting | Value |
|---|---|
| **Target container** | `postgrest-db` |
| **Database** | `appdb` |
| **User** | `postgrest` |
| **Password** | Stored in `/home/pgweb/.env` as `POSTGRES_PASSWORD` |
| **Connection string** | `postgres://postgrest:${POSTGRES_PASSWORD}@postgrest-db:5432/appdb?sslmode=disable` |

## Files

```
/home/pgweb/
├── docker-compose.yml    ← container definition
└── .env                  ← POSTGRES_PASSWORD (mode 600)
```

## Operation

### Status check

```bash
sudo docker logs pgweb --tail 10
```

### Restart / pick up compose changes

```bash
cd /home/pgweb && sudo docker compose up -d --force-recreate
```

### Stop

```bash
cd /home/pgweb && sudo docker compose down
```

### Update image

```bash
cd /home/pgweb && sudo docker compose pull && sudo docker compose up -d
```

## Gotchas

> **Hostname is `postgrest-db` (with the 't')**, not `postgres-db`. A missing 't' caused `dial tcp: lookup postgres-db on 127.0.0.11:53: server misbehaving`.

> **Port 3001 is no longer available to pgweb.** It is now claimed by CouchDB / Obsidian LiveSync (Tailscale Serve HTTPS `:3001` → `localhost:5984`). The original rationale ("3001 is in the ACL") still holds, but the port is taken. If pgweb is ever re-exposed before full removal, it must use a different ACL-allow-listed port.

> **pgweb has no built-in authentication.** Security depends on Tailscale restricting access to authorized devices. Do not expose this port publicly.

> **If `POSTGRES_PASSWORD` changes on the postgrest stack**, update `/home/pgweb/.env` and run `sudo docker restart pgweb`.

> **pgweb is read-write by default.** It can modify data — treat it as a full admin tool.
