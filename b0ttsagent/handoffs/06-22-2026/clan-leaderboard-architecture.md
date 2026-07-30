# Clan Leaderboard Architecture — Handoff

**Date:** 06-22-2026  
**Context:** Building an event-sourced, competitive clan leaderboard system on the VPS, exposed via PostgREST + Cloudflare Tunnel at `b0tts.dev/api`.

---

## What Was Accomplished This Session

### Research & Design Decisions
- **Architecture chosen:** CQRS-lite, event-sourced leaderboard
  - Roblox sends immutable events (not score overwrites)
  - Postgres aggregates events into clan scores via triggers
  - Materialized view serves leaderboard reads (precomputed ranks)
  - Refresh interval: 30–60 seconds (acceptable staleness)
- **Concurrency model:** Append-only writes eliminate race conditions entirely
- **Scalability path:** Current design scales to 100k+ clans. Beyond that: cursor pagination → materialized rank columns → Redis sorted sets → read replicas
- **Auth model:** PostgREST JWT authentication with `roblox_game` role
- **Secret storage:** Roblox Secrets Store (not hardcoded in scripts)

### Schema (Written But NOT Yet Applied)
The new `init.sql` was written and saved to `.pi/temp/init.sql` but **has not been applied to the VPS yet**. The database still contains the old `api.players` table, old `api.leaderboard` view, and `web_anon` role with sample data (jonah, shadow, sigma_grind, test_bot).

**New tables (not yet in DB):**

| Table | Purpose |
|---|---|
| `api.clans` | Clan identity (id UUID, name, tag, created_at) |
| `api.events` | Append-only event log (event_id, clan_id, player_id, season_id, event_type, points, metadata) |
| `api.clan_season_scores` | Aggregated scores per clan per season (updated by trigger on event insert) |
| `api.leaderboard` | Materialized view with precomputed rank per clan per season |

**RPC functions:**

| Function | Purpose |
|---|---|
| `api.submit_event(event_id, clan_id, player_id, season_id, event_type, points, metadata)` | Idempotent event insertion (duplicate event_id returns `{"status":"duplicate"}`) |
| `api.refresh_leaderboard()` | Refreshes the materialized view (SECURITY DEFINER, callable by roblox_game) |

**Roles:**

| Role | Type | Purpose |
|---|---|---|
| `authenticator` | LOGIN, NOINHERIT | PostgREST connects as this role |
| `roblox_game` | NOLOGIN | Switched into via JWT `{"role":"roblox_game"}` claim |
| `web_anon` | Dropped | No longer exists |

**RLS:** Enabled on all tables. Currently `USING(true) WITH CHECK(true)` for `roblox_game` (permissive — no per-player restrictions yet).

**Indexes:**
- `idx_events_clan_season` on `events(clan_id, season_id)`
- `idx_events_created` on `events(created_at)`
- `idx_clan_scores_score` on `clan_season_scores(season_id, total_score DESC)`
- `idx_leaderboard_unique` on `leaderboard(clan_id, season_id)` — required for CONCURRENTLY refresh
- `idx_leaderboard_rank` on `leaderboard(season_id, rank)` — for fast paginated reads

---

## Current State

### What's deployed and working
- ✅ **Old** Postgres schema (`api.players`, `api.leaderboard` view, `web_anon` role, sample data)
- ✅ PostgREST v14.13 container running (with old config)
- ✅ Cloudflare Tunnel (`sigma_gate`) exposing `b0tts.dev`
- ✅ Caddy routing `/api/*` to PostgREST
- ✅ PgBouncer connection pooling
- ✅ Daily `pg_basebackup` backups at noon

### What's NOT yet done
- ❌ **Apply new init.sql to VPS** — `.pi/temp/init.sql` is written but not copied to VPS or executed. Old schema still live.
- ❌ **PostgREST JWT configuration** — still using old `.env` with `PGRST_DB_ANON_ROLE=web_anon`
- ❌ **JWT secret generation** — not yet created
- ❌ **DB URI update** — still points to `postgrest` superuser, needs to switch to `authenticator`
- ❌ **Authenticator password** — currently set to placeholder `CHANGE_ME_IN_ENV`, needs a real password
- ❌ **Roblox JWT token** — not yet generated
- ❌ **Roblox Lua modules** — not yet written
- ❌ **Leaderboard refresh cron** — not yet scheduled
- ❌ **PostgREST restart** — hasn't picked up new schema or role changes

### Key files on VPS

```
/home/postgrest/
├── docker-compose.yml    ← stack definition (needs JWT secret added)
├── Caddyfile             ← path routing (/api/* → postgrest:3000)
├── init.sql              ← OLD schema (needs to be replaced with .pi/temp/init.sql)
├── .env                  ← secrets (needs PGRST_JWT_SECRET, PGRST_DB_URI update)
├── pgbouncer.ini         ← connection pooling
├── userlist.txt          ← PgBouncer auth
├── backup.sh             ← daily backup script
├── pgdata/               ← PostgreSQL data
└── backups/              ← backup tarballs
```

---

## Planned Next Steps (Execution — Not This Session)

### Phase 2: Apply New Schema
1. Copy `.pi/temp/init.sql` to VPS: `scp .pi/temp/init.sql deploy@vmi3326176.tailf94009.ts.net:/tmp/init.sql`
2. SSH into VPS and replace: `sudo cp /tmp/init.sql /home/postgrest/init.sql && sudo chown postgrest:postgrest /home/postgrest/init.sql`
3. Apply: `sudo docker exec -i postgrest-db psql -U postgrest -d appdb < /home/postgrest/init.sql`
4. Verify: `sudo docker exec -i postgrest-db psql -U postgrest -d appdb -c "\dt api.*"` and `-c "\dm api.*"`

### Phase 3: JWT Configuration
1. Generate JWT secret: `openssl rand -base64 32`
2. Generate authenticator password: `openssl rand -base64 24`
3. `ALTER ROLE authenticator PASSWORD '<new-password>';`
4. Update `/home/postgrest/.env`:
   - Add `PGRST_JWT_SECRET=<secret>`
   - Change `PGRST_DB_URI` to `postgres://authenticator:<password>@pgbouncer:6432/appdb`
   - Remove `PGRST_DB_ANON_ROLE` (empty = no anonymous access)
5. Update `docker-compose.yml` to pass `PGRST_JWT_SECRET` to container
6. Restart PostgREST container
7. Verify anonymous requests get 401

### Phase 4: Generate & Test Roblox Token
8. Generate long-lived JWT with `{"role": "roblox_game"}` claim
9. Test with curl:
   - `GET https://b0tts.dev/api/leaderboard` with Bearer token → 200
   - Same without token → 401
   - `POST /rpc/submit_event` with test data
   - `POST /rpc/refresh_leaderboard` then re-query leaderboard

### Phase 5: Roblox Lua Modules
10. Write `ApiConfig.lua` — loads JWT from Roblox Secrets Store
11. Write `LeaderboardService.lua` — `SubmitEvent`, `GetLeaderboard`, `GetClanRank`, `CreateClan`, `DeleteClan`
12. Save to `.pi/temp/roblox/`

### Phase 6: Leaderboard Refresh Automation
13. Add cron job to call `refresh_leaderboard()` every 60 seconds

---

## Schema Quick Reference

### Creating a clan
```http
POST /api/clans
Content-Type: application/json
Authorization: Bearer <jwt>

{"name": "Sigma Grindset", "tag": "SIG"}
```

### Submitting a scoring event
```http
POST /api/rpc/submit_event
Content-Type: application/json
Authorization: Bearer <jwt>

{
  "p_event_id": "unique-uuid",
  "p_clan_id": "clan-uuid",
  "p_player_id": 12345678,
  "p_season_id": 1,
  "p_event_type": "quest_complete",
  "p_points": 50,
  "p_metadata": {"quest_id": "daily_1"}
}
```

### Reading the leaderboard (paginated)
```http
GET /api/leaderboard?season_id=eq.1&order=rank.asc&limit=25&offset=0
Authorization: Bearer <jwt>
```

### Refreshing the leaderboard
```http
POST /api/rpc/refresh_leaderboard
Authorization: Bearer <jwt>
```

---

## Related References

- VPS infrastructure: `.pi/References/NavGuides/VpsNavGuide.md`
- PostgREST stack details: `.pi/References/NavGuides/PostgrestApiGuide.md`
- Pgweb (DB admin GUI): `.pi/References/NavGuides/PgwebNavGuide.md`
- Local init.sql copy: `.pi/temp/init.sql`

---

## Notes for Next Session

- The user wants to explore and learn the API before committing to full execution
- The database still has the OLD schema (api.players, old api.leaderboard view, web_anon). The new event-sourced schema in `.pi/temp/init.sql` needs to be copied to the VPS and applied before anything else.
- PostgREST currently runs with old config — anonymous access still works via `web_anon`
- To inspect current DB state: `sudo docker exec -i postgrest-db psql -U postgrest -d appdb` on the VPS
