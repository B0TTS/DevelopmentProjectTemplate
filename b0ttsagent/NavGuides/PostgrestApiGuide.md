---
name: PostgrestApiGuide
topics: [postgrest, postgresql, api, cloudflare-tunnel, caddy, leaderboard, pgbouncer, pg_basebackup, cron, jwt, event-sourcing, bruno, beekeeper]
description: "PostgREST API layer served through Cloudflare Tunnel on the VPS — PostgreSQL 17, PgBouncer pooling, Caddy path routing, JWT authentication, event-sourced clan leaderboard, daily backups, exposed at b0tts.dev/api"
---

# PostgREST API Navigation Guide V2.0

> VPS conventions (Docker, system users, Tailscale) are covered in [VpsNavGuide](VpsNavGuide.md).

## Overview

| Property | Value |
|---|---|
| **Domain** | `b0tts.dev` |
| **API path** | `/api/*` → PostgREST |
| **Root path** | `/` → "coming soon" (placeholder) |
| **App directory** | `/home/postgrest/` |
| **System user** | `postgrest` (uid 986, gid 981) |
| **Public access** | Yes — via Cloudflare Tunnel |
| **Cloudflare Tunnel** | `sigma_gate` (remotely managed) |

## Stack

| Container | Image | Internal Port |
|---|---|---|
| `postgrest-db` | `postgres:17-alpine` | 5432 |
| `postgrest-api` | `postgrest/postgrest:v14.13` | 3000 |
| `postgrest-caddy` | `caddy:2-alpine` | 80 (no host port) |
| `postgrest-tunnel` | `cloudflare/cloudflared:2025.2.0` | — |
| `postgrest-pgbouncer` | `edoburu/pgbouncer:latest` | 6432 |

All containers share the `postgrest_internal` Docker bridge network. No host ports are exposed — traffic enters exclusively through Cloudflare Tunnel.

## PostgreSQL

### Connection (from VPS)

```bash
sudo docker exec -i postgrest-db psql -U postgrest -d appdb
```

| Setting | Value |
|---|---|
| **Database** | `appdb` |
| **Superuser** | `postgrest` |
| **Authenticator role** | `authenticator` (login, noinherit) |
| **Game role** | `roblox_game` (nologin, switched via JWT) |
| **Password** | Stored in `/home/postgrest/.env` as `POSTGRES_PASSWORD` |
| **Authenticator password** | Stored in `/home/postgrest/.env` as `AUTHENTICATOR_PASSWORD` |
| **Exposed schema** | `api` |
| **Anonymous access** | **Disabled** (no `web_anon` role) |

### Run SQL

```bash
sudo docker exec -i postgrest-db psql -U postgrest -d appdb < /home/postgrest/init.sql
```

> The `init.sql` file was not picked up during first deploy because the `CREATE SCHEMA` line was missing. It's been fixed. For new tables, either run SQL manually or add them to `init.sql` and re-run.

## PgBouncer

Connection pooling in front of PostgreSQL. PostgREST now connects via PgBouncer instead of directly to the database.

| Setting | Value |
|---|---|
| **Pool mode** | `transaction` |
| **default_pool_size** | `20` |
| **max_client_conn** | `100` |
| **Config file** | `/home/postgrest/pgbouncer.ini` |
| **Auth file** | `/home/postgrest/userlist.txt` |
| **Exposed port** | `100.122.184.37:6432:6432` (Tailscale only) |

### Status check

```bash
sudo docker logs postgrest-pgbouncer --tail 5
```

### Admin console

```bash
sudo docker exec -it postgrest-pgbouncer psql -U postgrest -p 6432 pgbouncer
```

Then run `SHOW POOLS;`, `SHOW STATS;`, etc.

> **Password change**: If you change `POSTGRES_PASSWORD`, update both `/home/postgrest/userlist.txt` and `/home/postgrest/pgbouncer.ini`, then `sudo docker restart postgrest-pgbouncer`.

### External access (Beekeeper/GUI)

PgBouncer is exposed on the Tailscale interface for database GUI access (Beekeeper). Only Tailnet devices can reach it — the binding is to the Tailscale IP specifically and UFW blocks the public IP.

| Field | Value |
|---|---|
| Host | `100.122.184.37` |
| Port | `6432` |
| User | `postgrest` |
| Password | `POSTGRES_PASSWORD` from `/home/postgrest/.env` |
| Database | `appdb` |

> **Stale db port mapping**: The compose file previously had `ports: - "0.0.0.0:6432:6432"` on the `db` (PostgreSQL) service, mapping host 6432 to container 6432 — but PostgreSQL listens on 5432, so it did nothing useful. Removed when PgBouncer was properly exposed. Don't re-add a 6432 mapping to `db`; for external DB access use the `pgbouncer` service mapping or map `5432:5432` on `db`.

## Backups

Daily `pg_basebackup` (physical, tar+gzip) scheduled via root cron. Script at `/home/postgrest/backup.sh`, storage at `/home/postgrest/backups/`.

| Setting | Value |
|---|---|
| **Method** | `pg_basebackup` (tar+gzip) |
| **Schedule** | Daily at 12:00 (noon) |
| **Retention** | 7 days |
| **Cron file** | `/etc/cron.d/postgrest-backup` |
| **Log file** | `/home/postgrest/backups/backup.log` |

### Run backup manually

```bash
sudo bash /home/postgrest/backup.sh
```

### Check backup log

```bash
cat /home/postgrest/backups/backup.log
```

### List backups

```bash
ls -la /home/postgrest/backups/
```

> **Backup runs as root**: The script needs Docker access. Cron runs it as root. Don't run it as `postgrest` directly.

## PostgREST

### Status check

```bash
sudo docker logs postgrest-api --tail 5
```

> PostgREST caches the schema on startup. If you `CREATE TABLE` without restarting, PostgREST returns 503 until you run `sudo docker restart postgrest-api`.

### Querying the API (internal)

```bash
sudo docker exec postgrest-caddy wget -qO- http://postgrest:3000/leaderboard
```

### Current schema (event-sourced clan leaderboard)

| Object | Type | Purpose |
|---|---|---|
| `api.clans` | Table | Clan identity (id, name, tag, created_at) |
| `api.events` | Table | Append-only event log (event_id, clan_id, player_id, season_id, event_type, points, metadata) |
| `api.clan_season_scores` | Table | Aggregated scores per clan per season (updated by trigger) |
| `api.leaderboard` | Materialized View | Pre-ranked clans by total_score DESC |

> The old `api.players` table and `api.leaderboard` view were dropped during the JWT migration. The system is now event-sourced: all scoring goes through `api.events`, which triggers updates to `api.clan_season_scores`, which feeds the materialized `api.leaderboard`.

## Caddy

Routes traffic within the Docker network:

```caddy
http://b0tts.dev {
    handle_path /api/* {
        reverse_proxy postgrest:3000
    }
    handle {
        respond "coming soon"
    }
}
```

> Must use `handle_path` (not `handle`) for `/api/*` — `handle_path` strips the `/api` prefix before forwarding to PostgREST. Without it, PostgREST sees `/api/leaderboard` and returns 400.

### Apply Caddyfile changes

```bash
sudo docker restart postgrest-caddy
```

## Cloudflare Tunnel

- **Tunnel name:** `sigma_gate`
- **Tunnel ID:** `ac92d453-5613-404e-a9ba-11daddc408ae`
- **Token:** Stored in `/home/postgrest/.env` as `CLOUDFLARED_TUNNEL_TOKEN`
- **Mode:** Remotely managed (configured via API, not local config file)

### DNS

`b0tts.dev` is a **CNAME** pointing to `ac92d453-5613-404e-a9ba-11daddc408ae.cfargotunnel.com` (proxied). The old ParkLogic parking A records (172.x) were removed. A wildcard `*.b0tts.dev` CNAME remains for free subdomain routing.

### Check tunnel status

```bash
sudo docker logs postgrest-tunnel --tail 5
```

### Tunnel config (ingress rules)

Set via Cloudflare API, not dashboard UI:

```bash
curl -X PUT "https://api.cloudflare.com/client/v4/accounts/0b99ebe4dc999b6b95daa992a3a84255/cfd_tunnel/ac92d453-5613-404e-a9ba-11daddc408ae/configurations" \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"config":{"ingress":[{"hostname":"b0tts.dev","service":"http://caddy:80"},{"service":"http_status:404"}]}}'
```

> The Cloudflare dashboard UI changed and the "Public hostname" button was missing. The API call above bypasses the dashboard. If the tunnel config ever needs updating, use the API rather than hunting through the dashboard.

## JWT Authentication

PostgREST requires valid JWT tokens for all API requests. Anonymous access is disabled.

| Setting | Value |
|---|---|
| **JWT secret** | 48-char string in `/home/postgrest/.env` as `PGRST_JWT_SECRET` |
| **Algorithm** | HS256 (HMAC-SHA256) |
| **Required claim** | `role: "roblox_game"` |
| **Token expiration** | None (long-lived, stored server-side in Roblox Secrets Store) |

### Test with curl

```bash
# Should return data (200)
curl https://b0tts.dev/api/leaderboard \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Should return 401 "Anonymous access is disabled"
curl https://b0tts.dev/api/leaderboard
```

### Generate JWT token (on VPS)

```bash
cd /home/postgrest && source .env && python3 - <<'PY'
import hmac,hashlib,base64,json;secret=None
with open('/home/postgrest/.env') as f:
    for line in f:
        if line.strip().startswith('PGRST_JWT_SECRET='):
            secret=line.split('=',1)[1].strip()
            break
header=base64.urlsafe_b64encode(json.dumps({'alg':'HS256','typ':'JWT'}).encode()).rstrip(b'=').decode()
payload=base64.urlsafe_b64encode(json.dumps({'role':'roblox_game'}).encode()).rstrip(b'=').decode()
signature=base64.urlsafe_b64encode(hmac.new(secret.encode(),(header+'.'+payload).encode(),hashlib.sha256).digest()).rstrip(b'=').decode()
print(f"{header}.{payload}.{signature}")
PY
```

> The JWT token is stored in Bitwarden under "PostgREST JWT" and must be added to Roblox Secrets Store as `POSTGREST_JWT` (server-side only).

## RPC Functions

| Function | Purpose | Endpoint |
|---|---|---|
| `api.submit_event()` | Idempotent event submission (deduplicates by event_id) | `POST /rpc/submit_event` |
| `api.refresh_leaderboard()` | Refresh materialized view concurrently | `POST /rpc/refresh_leaderboard` |

### Submit event example

```bash
curl -X POST https://b0tts.dev/api/rpc/submit_event \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "p_event_id": "123e4567-e89b-12d3-a456-426614174000",
    "p_clan_id": "00000000-0000-0000-0000-000000000001",
    "p_player_id": 12345,
    "p_season_id": 1,
    "p_event_type": "quest_complete",
    "p_points": 50,
    "p_metadata": {"quest_id": "daily_login"}
  }'
```

> The `submit_event` function is idempotent: duplicate `event_id` values are safely ignored. The trigger on `api.events` automatically updates `api.clan_season_scores`.

## Tools

| Tool | Purpose | Access |
|---|---|---|
| **Beekeeper** | PostgreSQL GUI client | Tailscale only (`100.122.184.37:6432`) |
| **Bruno** | REST API client (Postman alternative) | Any device with the JWT token |

### Beekeeper connection

Use PgBouncer credentials (see "External access" section above). Connect as `postgrest` superuser for full access, or `authenticator` for limited access.

### Bruno collections

API endpoints are at `https://b0tts.dev/api/`. All requests require `Authorization: Bearer <JWT_TOKEN>` header. See `.pi/temp/roblox/README.md` for endpoint examples.

## Environment (.env)

| Variable | Purpose |
|---|---|
| `POSTGRES_PASSWORD` | PostgreSQL superuser password |
| `PGPASSWORD` | Same password, for psql convenience |
| `AUTHENTICATOR_PASSWORD` | Password for `authenticator` role |
| `PGRST_DB_URI` | `postgres://authenticator:<pw>@pgbouncer:6432/appdb` |
| `PGRST_DB_SCHEMAS` | `api` |
| `PGRST_JWT_SECRET` | 48-char JWT signing secret (HS256) |
| `CLOUDFLARED_TUNNEL_TOKEN` | Tunnel connector token |

> The `.env` file is sensitive to line wrapping. If values get split across lines, everything breaks. Use `printf` or `base64 -d` to write it safely. Never paste multi-line `.env` values through a terminal.

## Files

```
/home/postgrest/
├── docker-compose.yml    ← stack definition
├── Caddyfile             ← path routing
├── init.sql              ← schema / seed data
├── .env                  ← secrets (passwords, tokens)
├── backup.sh             ← daily backup script
├── pgbouncer.ini         ← connection pooling config
├── userlist.txt          ← PgBouncer auth
├── pgdata/               ← PostgreSQL data volume
└── backups/              ← daily backup tarballs
```

Clean local copies are at `.pi/temp/init.sql`.

## Gotchas

> **UFW**: The VPS firewall only allows traffic on `tailscale0`. The Cloudflare tunnel works because `cloudflared` makes an outbound QUIC connection to Cloudflare's edge — no inbound port needed.

> **PostgreSQL user conflict**: Don't use `user: "UID:GID"` on the `db` container. PostgreSQL internally requires uid 70 (`postgres`). The override prevented `initdb` from chowning the data directory.

> **YAML indentation**: The terminal mangles pasted YAML. Write files locally and SCP them to the VPS, or use base64 encoding. All indentation must be exactly 2 spaces.

> **Caddy auto-redirect**: Writing just `b0tts.dev { ... }` in the Caddyfile causes Caddy to 308-redirect HTTP to HTTPS (which breaks because Cloudflare handles TLS). The block must start with `http://b0tts.dev {`.

> **Schema cache**: PostgREST caches the database schema at startup. New tables or views require `sudo docker restart postgrest-api`.

> **pg_basebackup needs superuser**: The backup script authenticates as the `postgrest` superuser. The container's internal `postgres` user also works if needed.

> **JWT token generation**: The Python script for generating JWT tokens reads `PGRST_JWT_SECRET` from `.env`. If the secret changes, regenerate the token and update Bitwarden + Roblox Secrets Store.

> **Materialized view refresh**: The `api.leaderboard` materialized view must be refreshed manually via `POST /rpc/refresh_leaderboard` or via cron job (pending setup). Without refresh, ranks stay stale.

> **Event sourcing**: All scoring must go through `api.events` via `submit_event()`. Direct `INSERT` into `api.clan_season_scores` will work but bypasses the audit trail.
