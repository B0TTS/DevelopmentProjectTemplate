# Handoff: Hardcore Solo Fabric Server on InterServer VPS — Plan Ready

## Summary

Planned a **second** Minecraft server on the InterServer VPS that mirrors the Contabo hardcore-vanilla server (`MinecraftNavGuide.md`) but with a different seed. The plan is fully locked and verified against the itzg/minecraft-server docs; nothing has been executed on the VPS yet. Next session starts at **Step 1** of a 7-step plan.

This server is **Java-only, performance-modded Fabric 1.21.11, hardcore survival, Tailscale-only, single player (the user)**. It is intentionally distinct from the existing **MyngaCraft** cross-play server already running on the same VPS out of `/home/minecraft/` (see prior handoffs in `b0ttsagent/handoffs/07-07-2026/`).

The next session picks up at **execution**: pre-flight inspection → create system user → write compose → first boot → Tailscale ACL + connection test → backup cron → wrap up.

---

## Decision Tree (resolved this session)

| Question | Resolution | Rationale |
|---|---|---|
| Access model | **Tailscale-only** (no public port) | Solo player (the user); UFW already allows `tailscale0`; no new public exposure needed |
| Java port | `25566/tcp` (host) → `25565` (container) | `25565` taken by MyngaCraft; `25566` is free |
| App / system-user name | `minecraft-hc-solo` (dir `/home/minecraft-hc-solo/`, container `minecraft-hc-solo`) | `minecraft` already taken by MyngaCraft; distinct name avoids collision |
| Whitelist | **None** (no `ENABLE_WHITELIST`, no `WHITELIST`) | Tailscale ACLs already gate access; user is the only player |
| Op | `OPS: GEGEgaymers` | Lets the user run commands, pregen, etc. |
| Backups | Daily backup cron — **in scope**; mirrors Contabo pattern | Important even for solo (hardcore = single life) |
| Chunky pregen | **Out of scope** for this setup | User may do it later; plan leaves exact "do-later" commands |
| Hardcore mode | `HARDCORE: "true"` + `DIFFICULTY: hard` + `MODE: survival` | Confirmed by user; matches nav guide |

---

## Locked Configuration

| Property | Value |
|---|---|
| Container name | `minecraft-hc-solo` |
| System user | `minecraft-hc-solo` (UID/GID captured at Step 2 via `id`) |
| Compose file | `/home/minecraft-hc-solo/docker-compose.yml` |
| World data | `/home/minecraft-hc-solo/data` |
| Backups dir | `/home/minecraft-hc-solo/backups/` |
| Backup script | `/home/minecraft-hc-solo/backup.sh` |
| Image | `itzg/minecraft-server` |
| `TYPE` | `FABRIC` |
| `VERSION` | `"1.21.11"` |
| `SEED` | `"5277846394751328433"` |
| `HARDCORE` | `"true"` |
| `DIFFICULTY` | `hard` |
| `MODE` | `survival` |
| `ONLINE_MODE` | `"true"` |
| `VIEW_DISTANCE` | `10` |
| `SIMULATION_DISTANCE` | `8` |
| `SPAWN_PROTECTION` | `0` |
| `MEMORY` | `4G` |
| `USE_AIKAR_FLAGS` | `"true"` |
| `mem_limit` | `5g` |
| `UID` / `GID` | from `id minecraft-hc-solo` (Step 2) |
| RCON (host→container) | `25576` → `25575`, password **<RCON_PASSWORD>** (choose a strong one; do NOT reuse `mc-rcon-changeme`) |
| Java port (host→container) | `25566` → `25565` |
| `OPS` | `GEGEgaymers` |
| `MODRINTH_PROJECTS` | `fabric-api`, `lithium`, `krypton`, `ferrite-core`, `noisiumforked`, `chunky`, `spark` |
| `restart` | `unless-stopped` |

### Mods (corrected slugs — carried from prior handoffs)

| Mod | Modrinth slug |
|---|---|
| Fabric API | `fabric-api` |
| Lithium | `lithium` |
| Krypton | `krypton` |
| FerriteCore | **`ferrite-core`** (hyphenated; `ferritecore` 404s) |
| Noisium (fork) | **`noisiumforked`** (original `noisium` has no 1.21.11 Fabric build → crash-loop) |
| Chunky | `chunky` |
| Spark | `spark` |

> **No Geyser/Floodgate** — this server is Java-only, true to the Contabo nav guide.

---

## The 7-Step Execution Plan (NOT yet started)

Conventions: agent never touches the VPS. Every command is written to `b0ttsagent/temp/` files for the user to paste. One step at a time, verify each before moving on. (The `tutorial` skill was active; its one-step-at-a-time rule continues.)

1. **Pre-flight inspection (read-only)** — confirm `mc` (MyngaCraft) container running & healthy and won't be touched; `free -m` headroom (12 GB total, MyngaCraft uses ~5 G; need ~5 G more); `sudo docker ps` confirms no port conflict on `25566`/`25576`; `sudo ufw status verbose` confirms `tailscale0` open + public locked down. Nothing changed.
2. **Create system user `minecraft-hc-solo`** — `useradd --system --no-create-home --shell /usr/sbin/nologin minecraft-hc-solo`; `mkdir -p /home/minecraft-hc-solo/{data,backups}`; `chown -R minecraft-hc-solo:minecraft-hc-solo /home/minecraft-hc-solo`; `id minecraft-hc-solo` → capture UID:GID for compose `UID`/`GID`.
3. **Write `docker-compose.yml`** — single service as in the Locked Configuration table; ports `25566:25565` + `25576:25575`; volumes `./data:/data`; the corrected `MODRINTH_PROJECTS` block; `EULA: "TRUE"`. (Write to `b0ttsagent/temp/` first for paste.)
4. **First boot & verify** — `cd /home/minecraft-hc-solo && sudo docker compose up -d`; tail logs for `Done (...s)! For help, type "help"`; verify `hardcore=true` and `level-seed=5277846394751328433` in rendered `server.properties` (`docker exec` cat, or `DUMP_SERVER_PROPERTIES: "true"`); confirm all 7 mods loaded via Modrinth. Diagnose any crash-loop (both known slug pitfalls already corrected, but watch logs).
5. **Tailscale ACL + connection test** — add `tcp:25566` to the workstation→InterServer-VPS allow list at `login.tailscale.com/admin/acls` (InterServer node = `interdeploymcvps` / `100.100.223.6`). From the workstation Java 1.21.1 client connect to `100.100.223.6:25566` (= `interdeploymcvps.tailf94009.ts.net:25566`). Confirm login, hardcore indicator, and OP status. No UFW change needed (tailnet already open).
6. **Backup script + daily cron** — write `/home/minecraft-hc-solo/backup.sh` mirroring the Contabo pattern (`MinecraftNavGuide.md` "Backups" section): tar.gz of `data/` → `/home/minecraft-hc-solo/backups/minecraft-hc-YYYY-MM-DD_HH-MM-SS.tar.gz`, 30-day prune, append to `backup.log`. Root crontab entry at `0 14 * * *` (14:00 UTC = 4 AM HST). Manual test run: `sudo bash /home/minecraft-hc-solo/backup.sh`. (Inspect the Contabo `/home/minecraft/backup.sh` first to mirror its exact safe-stop vs hot-tar approach.)
7. **Wrap up** — create/update a nav guide entry for `minecraft-hc-solo` (use `create-nav-guide` skill); add the out-of-scope Chunky "do-later" block (overworld r5000, nether r10000, `pregen.sh` auto-chain — see `MinecraftNavGuide.md` "Chunky" section for exact commands). No further changes.

---

## Current State

- **VPS**: InterServer `interdeploymcvps.tailf94009.ts.net` / `100.100.223.6` / public `67.211.215.84` (public SSH closed; tailnet only). Ubuntu 26.04 LTS, 12 GB RAM, 3 vCPU. Docker 29.6.1 / Compose v5.3.1 installed. UFW: `tailscale0` open, `25565/tcp` + `19132/udp` open (those belong to MyngaCraft).
- **Existing MyngaCraft server**: running at `/home/minecraft/` (user `minecraft`, UID 999/GID 982), Fabric 1.21.11, public `25565/tcp` + `19132/udp`, Cloudflare `myngacraft.b0tts.me`. **Untouched by this plan.** Its pending Bedrock ViaProxy work (see `07-07-2026/viaproxy-bridge-plan-ready.md`) is independent and remains pending.
- **New server**: nothing on disk yet. Plan locked, awaiting Step 1.

## Open Decisions

- None blocking. All configuration and the access model are settled. The only choice deferred to execution is the RCON password (pick a strong one; do not reuse MyngaCraft's `mc-rcon-changeme`).

## Still Pending (independent of this plan)

1. ⬜ **MyngaCraft ViaProxy bridge** — `07-07-2026/viaproxy-bridge-plan-ready.md`, 10-step plan, nothing executed. Unrelated to the solo server.
2. ⬜ **MyngaCraft backup cron** — step 13 of the original MyngaCraft plan, still pending. Independent; do regardless.
3. ⬜ **Cloudflare/DNS nav guide** for `b0tts.me` — noted missing in the 07-07 handoffs. Independent.

## Suggested Skills for Next Session

- **`tutorial`** (active) — continue executing the 7-step plan one step at a time. Start at **Step 1**.
- **`create-nav-guide`** — at Step 7, capture the solo server reference (and optionally the still-missing Cloudflare/DNS guide).
- **`regenerate-minecraft-world`** — reference only for seed handling; **not** needed since `SEED` is set directly in compose and world folders don't exist yet (fresh gen).

## Key References

- `b0ttsagent/NavGuides/InterVpsNavGuide.md` — VPS access, SSH hardening, UFW, conventions
- `b0ttsagent/NavGuides/VpsNavGuide.md` — Docker conventions, system-user-per-app pattern, Tailscale ACL note
- `b0ttsagent/NavGuides/MinecraftNavGuide.md` — Contabo template config, backup pattern (to mirror), Chunky pregen commands (for the do-later block)
- `b0ttsagent/handoffs/07-07-2026/minecraft-crossplay-interserver-setup.md` — MyngaCraft planning (existing server)
- `b0ttsagent/handoffs/07-07-2026/minecraft-server-live-bedrock-incompatibility.md` — discovered the `noisiumforked` + `ferrite-core` slug gotchas (carried into this plan)
- `b0ttsagent/handoffs/07-07-2026/viaproxy-bridge-plan-ready.md` — MyngaCraft Bedrock fix (pending, unrelated)
- itzg server-properties docs: https://docker-minecraft-server.readthedocs.io/en/latest/configuration/server-properties/ — confirmed `HARDCORE`→`hardcore`, `SEED`→`level-seed`, `DIFFICULTY`, `MODE`, `SPAWN_PROTECTION`, `VIEW_DISTANCE`, `SIMULATION_DISTANCE`, `ONLINE_MODE`, `ENABLE_RCON`, `RCON_PORT`, `RCON_PASSWORD`, `OPS`, `MEMORY`, `USE_AIKAR_FLAGS`, `TYPE`, `VERSION`

---

*Handoff created 2026-07-14. Next session: execute the 7-step plan starting at Step 1.*