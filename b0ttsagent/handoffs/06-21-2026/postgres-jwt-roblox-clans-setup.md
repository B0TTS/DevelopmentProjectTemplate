# PostgREST JWT + Roblox Clans Setup

**Date:** June 21, 2026  
**Status:** Mostly complete — one remaining step  
**Time to resume:** ~30 minutes

---

## What was accomplished

Built an event-sourced clan leaderboard system on the VPS with secure Roblox integration:

### 1. Schema & Database (✅ Complete)
- **Event-sourced architecture**: Append-only `api.events` table for all scoring actions
- **Automatic aggregation**: Trigger updates `api.clan_season_scores` on every event insert
- **Materialized leaderboard**: Pre-computed ranks in `api.leaderboard` view
- **JWT authentication**: PostgREST now requires valid tokens — anonymous access disabled
- **Roles**: `authenticator` (login) and `roblox_game` (no-login, switched via JWT)
- **Row-level security**: Enabled on all tables with policies for `roblox_game` role

**Key tables:**
- `api.clans` — Clan identity (id, name, tag)
- `api.events` — Event log (event_id, clan_id, player_id, season_id, event_type, points, metadata)
- `api.clan_season_scores` — Aggregated scores per clan per season
- `api.leaderboard` — Materialized view with precomputed ranks

**Key functions:**
- `api.submit_event()` — Idempotent event submission (deduplicates by event_id)
- `api.refresh_leaderboard()` — Refreshes materialized view concurrently

### 2. JWT Authentication (✅ Complete)
- Generated JWT secret (48 chars) and authenticator password (32 chars)
- Stored in `/home/postgrest/.env` as `PGRST_JWT_SECRET` and `AUTHENTICATOR_PASSWORD`
- Generated long-lived JWT token for `roblox_game` role (no expiration)
- **Tested successfully**: Authenticated requests return data, anonymous requests get 401

### 3. Roblox Lua Modules (✅ Complete)
Created two module scripts in `.pi/temp/roblox/`:

- **`ApiConfig.lua`** — Loads JWT from Roblox Secrets Store, builds auth headers
- **`LeaderboardService.lua`** — Full API client with functions:
  - `GetLeaderboard(limit, offset, seasonId)` — Paginated leaderboard
  - `GetClanRank(clanId, seasonId)` — Single clan lookup
  - `SubmitEvent(eventId, clanId, playerId, seasonId, eventType, points, metadata)` — Score submission
  - `CreateClan(name, tag)` / `UpdateClan()` / `DeleteClan()` — CRUD operations
  - `GetAllClans()` — Raw clan list

**Documentation:** Full setup guide and usage examples in `.pi/temp/roblox/README.md`

### 4. API Testing (✅ Complete)
Verified on VPS with curl:
- `GET https://b0tts.dev/api/leaderboard` with JWT → Returns 5 test clans with correct rankings
- `GET https://b0tts.dev/api/leaderboard` without JWT → Returns 401 "Anonymous access is disabled"

---

## Current state

**Working:**
- ✅ Postgres schema with event sourcing
- ✅ JWT authentication
- ✅ PostgREST API endpoints
- ✅ Roblox Lua modules written and documented
- ✅ Backup system (daily at noon)
- ✅ Materialized view ready for refresh

**Not yet done:**
- ❌ **Leaderboard auto-refresh cron job** (see "Next step" below)
- ❌ Testing in actual Roblox Studio
- ❌ Adding the JWT secret to Roblox Secrets Store

---

## Next step: Leaderboard auto-refresh cron

**What:** Set up a cron job to refresh the materialized view every 60 seconds.

**Why:** The leaderboard view only updates when `api.refresh_leaderboard()` is called. Without automation, ranks stay stale until manually refreshed.

**How:**
1. Create `/home/postgrest/refresh-leaderboard.sh`:
   ```bash
   #!/bin/bash
   docker exec postgrest-api psql -U authenticator -d appdb -c "SELECT api.refresh_leaderboard();"
   ```

2. Make it executable:
   ```bash
   sudo chmod +x /home/postgrest/refresh-leaderboard.sh
   sudo chown postgrest:postgrest /home/postgrest/refresh-leaderboard.sh
   ```

3. Add cron job (edit with `sudo crontab -e`):
   ```bash
   * * * * * /home/postgrest/refresh-leaderboard.sh >> /home/postgrest/refresh.log 2>&1
   ```

4. Test manually:
   ```bash
   sudo /home/postgrest/refresh-leaderboard.sh
   ```

**Expected result:** Leaderboard updates every minute without manual intervention.

---

## After the cron job: Roblox Studio integration

Once the cron is working, the next session should:

1. **Add the JWT secret to Roblox Studio:**
   - Open your game in Roblox Studio
   - File → Game Settings → Security → Secrets
   - Create secret named `POSTGREST_JWT` with the token value from Bitwarden
   - Set access to "Server-side only"

2. **Import the Lua modules:**
   - Copy `ApiConfig.lua` and `LeaderboardService.lua` from `.pi/temp/roblox/` into ServerScriptService
   - Enable HTTP requests in Game Settings → Security

3. **Test with a simple script:**
   ```lua
   local LeaderboardService = require(game.ServerScriptService:WaitForChild("LeaderboardService"))
   wait(2)
   local data, err = LeaderboardService.GetLeaderboard(5, 0, 1)
   if data then
       print("✓ Leaderboard working!")
       for _, clan in ipairs(data) do
           print(string.format("#%d: %s - %d pts", clan.rank, clan.name, clan.total_score))
       end
   else
       warn("✗ Failed:", err)
   end
   ```

---

## Key files & commands

### VPS files
- `/home/postgrest/init.sql` — Database schema (the one you applied via Beekeeper)
- `/home/postgrest/.env` — Environment variables (JWT secret, DB credentials)
- `/home/postgrest/docker-compose.yml` — Stack definition
- `/home/postgrest/backups/` — Daily backups (7-day retention)

### Local files
- `.pi/temp/init.sql` — Clean copy of the schema migration
- `.pi/temp/roblox/` — Roblox Lua modules and README
- `.pi/References/NavGuides/PostgrestApiGuide.md` — Full PostgREST stack documentation

### Useful commands
```bash
# Check PostgREST logs
sudo docker logs postgrest-api --tail 20

# Test leaderboard API
curl https://b0tts.dev/api/leaderboard -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Test event submission
curl -X POST https://b0tts.dev/api/rpc/submit_event \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"p_event_id":"test-uuid","p_clan_id":"00000000-0000-0000-0000-000000000001","p_player_id":12345,"p_season_id":1,"p_event_type":"test","p_points":10}'

# Manual leaderboard refresh
sudo docker exec postgrest-api psql -U authenticator -d appdb -c "SELECT api.refresh_leaderboard();"
```

---

## Security notes

- JWT secret, authenticator password, and Postgres password are stored in Bitwarden
- JWT token for Roblox is also in Bitwarden (search for "PostgREST JWT")
- The JWT token has no expiration — it's valid indefinitely (stored server-side in Roblox Secrets Store, so this is acceptable)
- Anonymous access is disabled — all API requests require valid JWT

---

## Architecture decisions made

1. **Event sourcing over direct updates** — All scoring goes through `api.events`, which is append-only. This prevents race conditions and provides an audit trail.

2. **Materialized view for leaderboard** — Ranks are pre-computed every 60 seconds (once cron is set up). Reads are instant, writes are cheap.

3. **Idempotent events** — Each event has a unique `event_id` (UUID). Duplicate submissions are safely ignored.

4. **JWT over API keys** — PostgREST-native authentication. Tokens are stateless and can include claims (currently just `role: "roblox_game"`).

5. **Roblox Secrets Store** — JWT token stored server-side only, never exposed to clients.

---

## Reference documentation

- **PostgREST API Guide:** `.pi/References/NavGuides/PostgrestApiGuide.md`
- **VPS Nav Guide:** `.pi/References/NavGuides/VpsNavGuide.md`
- **Lua module docs:** `.pi/temp/roblox/README.md`

---

## Suggested skills for next session

- **Handoff** — If you want to pause again, use this skill to capture progress
- **Tutorial** — Continue step-by-step if you hit issues with Roblox integration
- **No specific skill needed** — The cron job is straightforward bash + cron

---

**You're 90% done.** The cron job is the last infrastructure piece, then it's just importing the Lua modules into Roblox Studio and testing. Good luck!
