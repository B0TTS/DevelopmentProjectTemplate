# Handoff: Obsidian LiveSync Setup for "Whack Grass" Planning Docs

**Date:** 07-17-2026
**Status:** Planning complete (Phase 1 of the `tutorial` skill). Ready to execute. Nothing deployed yet.

---

## Summary

The user wants live, bidirectional sync of an Obsidian vault across **three devices** (laptop, PC, phone) using the **Self-hosted LiveSync** plugin backed by a **CouchDB** instance deployed on their VPS. The vault is sensitive and must **never** be committed to git.

This session was the research + planning phase of the `tutorial` skill workflow. We: read the VPS nav guide, researched the LiveSync plugin and CouchDB deployment, inspected the user's environment, resolved all architecture decisions with the user, produced a finalized step-by-step plan (v2), and were about to begin execution (Step 1) when the user chose to hand off to a new session.

**No commands were run on the VPS. No files were created or modified.** Everything is still in the planning state.

## Goal

Set up Obsidian Self-hosted LiveSync so the user can read/edit their "Whack Grass" game-design planning docs on their laptop, PC, and phone, with a self-hosted CouchDB sync server on the VPS, E2E encrypted, over the Tailscale tailnet (no public exposure).

## Vault

- **Path (laptop):** `C:\Development\GameProjects\Whack Grass\Planning Docs`
- **NOT in git** — sensitive. The handoff/agent must **not** read the contents of this directory (user instruction). Only verify existence / `.obsidian` presence as needed.
- Folder exists on the laptop but is **not yet an Obsidian vault** (no `.obsidian` folder).
- The vault does **not** exist on the PC or phone yet (those will pull from CouchDB).

## Devices (device lineup)

| Device | Role | Obsidian installed? | On tailnet? | Has vault? |
|---|---|---|---|---|
| Laptop (Windows, the box at `C:\Development\...`) | **First device — pushes existing docs to CouchDB** | **No** (must install) | Yes (assumed) | Yes (existing docs) |
| PC (separate desktop) | **Subsequent — pulls** | **Yes** (already installed) | Yes | No |
| Phone | **Subsequent — pulls** | Yes | Yes | No |

> The laptop was the machine the agent inspected this session. The PC and phone use the identical "subsequent device" flow (empty vault → import setup URI → pull).

## Architecture (locked-in decisions)

- **Sync backend:** CouchDB on the VPS via Docker Compose, at `/home/couchdb/`, container bound to `127.0.0.1:5984` (localhost only — never public).
- **CouchDB image:** `couchdb:3.5.2` (current stable; the official LiveSync example ships ancient `3.1.2` — do not use that).
- **Phone/PC access path:** **Tailscale Serve HTTPS on port `3001`** → proxies `localhost:5984`. Endpoint: `https://vmi3326176.tailf94009.ts.net:3001`.
  - Chosen because `:443`, `:3000`, `:8443` are all already occupied by existing Tailscale Serve entries (see "VPS current state" below). Port `3001` is already in the tailnet ACL allow-list, so no ACL edit expected.
  - Tailscale Serve issues publicly-trusted Let's Encrypt certs for `*.ts.net`, which Obsidian mobile accepts. LiveSync's troubleshooting doc confirms mobile **rejects** non-secure/self-signed endpoints — this is why Tailscale Serve (not a self-signed cert) is required.
- **E2E encryption:** **ON** — 256-bit AES-GCM + filename/path obfuscation. Required by user (docs are sensitive). Passphrase will be needed on every device.
- **Sync mode:** LiveSync (real-time bidirectional).
- **Sync scope:** Notes only initially (no settings/plugin/theme sync). Can add later.
- **Credentials:** Agent generates a strong CouchDB admin user/password + E2E passphrase at execution time. Stored in `/home/couchdb/.env` on the VPS (never in git). User keeps a copy in their password manager. **No credentials exist yet.**

## VPS current state (relevant)

From `b0ttsagent/NavGuides/VpsNavGuide.md`:
- SSH: `ssh deploy@vmi3326176.tailf94009.ts.net` (Tailscale IP `100.122.184.37`; public IP locked down, UFW only allows `tailscale0`).
- Convention: each app gets a system user (no sudo, no login shell), data + compose at `/home/<appname>/`, containers `restart: unless-stopped`.
- Add-an-app recipe:
  ```bash
  sudo useradd --system --no-create-home --shell /usr/sbin/nologin <appname>
  sudo mkdir -p /home/<appname>
  sudo chown -R <appname>:<appname> /home/<appname>
  id <appname>  # note UID:GID
  ```
- Tailscale Serve HTTPS: `sudo tailscale serve --https=<port> --bg http://localhost:<port>`. Only one app per port 443; use a dedicated port otherwise.

From `tailscale serve status` (user-pasted, this session):
```
https://vmi3326176.tailf94009.ts.net:3000 (tailnet only)  -> localhost:8083
https://vmi3326176.tailf94009.ts.net       (tailnet only) -> localhost:8080   [port 443]
https://vmi3326176.tailf94009.ts.net:8443 (tailnet only)  -> localhost:8001
```
→ `:443`, `:3000`, `:8443` are **taken**. `:3001` is free (to be confirmed at execution).

**Tailnet ACL** (from VpsNavGuide): traffic allowed from workstation→VPS on `tcp: 22, 443, 1935, 3000, 3001, 6432, 8001, 8080, 8443, 25565`. `3001` is included.
- **Open item:** the ACL line says "from workstation to VPS" — need to confirm the **phone** and **PC** are in the same allowed source group. Folded into Phase 2 / Phase 3 step 1 ("test connectivity to `:3001`") — fix ACL at login.tailscale.com/admin/acls if blocked.

## Laptop environment (inspected this session)

- Obsidian: **not installed**.
- `deno`: not installed → **not needed**; we use Obsidian's in-app "Minimal setup" wizard on the first device, then export a setup URI from inside Obsidian to the other devices.
- `docker`: 29.5.3 (optional, for local dry-run only — not required).
- `node`: v24.18.0.
- Vault dir exists, no `.obsidian` yet.

## The finalized plan (v2) — execution starting point

**Architecture:** CouchDB 3.5.2 on VPS (Docker, localhost-only) → Tailscale Serve HTTPS `:3001` → Obsidian + Self-hosted LiveSync on laptop (first, pushes), then PC and phone (subsequent, pull). E2E encrypted. Vault out of git.

### Phase 1 — VPS: Deploy CouchDB (user runs over SSH; agent never SSHes)
1. Create `couchdb` system user + dirs (`/home/couchdb/couchdb-data`, `/home/couchdb/couchdb-etc`). Note: the CouchDB *container* runs as uid `5984` internally, so `chown` the two data dirs to `5984:5984` before starting in Step 3. Host `couchdb` user just owns the compose files.
2. Write `/home/couchdb/.env` (strong creds) + `docker-compose.yml` (CouchDB `3.5.2`, `user: 5984:5984`, bound `127.0.0.1:5984`, `restart: unless-stopped`, volumes for data + etc/local.d). Reference: LiveSync `setup_own_server.md` Docker Compose example.
3. `chown` data dirs to `5984:5984`, `docker compose up -d`, verify running (`docker ps`, `curl http://localhost:5984`).
4. Run `curl -s https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh | bash` (or with explicit `hostname=`/`username=`/`password=` env if it errors). Configures CORS for Obsidian mobile origins (`app://obsidian.md,capacitor://localhost,http://localhost`) + creates the DB.
5. `sudo tailscale serve --https=3001 --bg http://localhost:5984`; `tailscale serve status`. Verify from laptop: `curl https://vmi3326176.tailf94009.ts.net:3001` should return CouchDB JSON.

### Phase 2 — Laptop: first device (has existing docs)
6. Install Obsidian on laptop; verify it can reach `https://vmi3326176.tailf94009.ts.net:3001`.
7. Open `Planning Docs` as a vault + install the Self-hosted LiveSync community plugin.
8. Run the Minimal Setup wizard: CouchDB URI (`https://vmi3326176.tailf94009.ts.net:3001`), DB name, username/password; **E2E encryption + path obfuscation ON**; choose "LiveSync" preset; Apply.
9. Let initial sync push the docs to CouchDB; verify (status bar indicators settle; check DB doc count).

### Phase 3 — PC: subsequent device (pulls)
10. Open Obsidian on PC (already installed); verify it reaches `https://...ts.net:3001`.
11. Create an empty vault + install LiveSync.
12. From the laptop, run "Copy settings as a new setup URI" (encrypt with a setup-URI passphrase — distinct from the E2E passphrase). Import the setup URI on the PC → initial pull.
13. Verify docs appear on the PC.

### Phase 4 — Phone: subsequent device (pulls)
14. Create empty vault on phone + install LiveSync.
15. Import the same setup URI (reuse the laptop one) → initial pull.
16. Verify docs appear on the phone.

### Phase 5 — Verify + wrap up
17. Edit-round-trip test across all three devices (both directions).
18. Store CouchDB creds + E2E passphrase + setup-URI passphrase in password manager; final cleanup.

## Open decisions / things to confirm at execution time

1. **Port 3001 actually free on the VPS** — confirm during Step 5 (the `tailscale serve status` we saw didn't list 3001, so it should be).
2. **Phone & PC in the tailnet ACL source group** — confirm during Phase 2/3 first connectivity step; edit ACL at login.tailscale.com/admin/acls if blocked.
3. **CouchDB credentials + E2E passphrase** — generate at execution; store in `/home/couchdb/.env` (VPS) + user's password manager. Redact from any docs/handoffs.
4. **Setup-URI passphrase** — distinct from E2E passphrase; generated inside Obsidian when exporting the setup URI; user notes it outside Obsidian.

## Suggested skills for the next session

- **`tutorial`** — we are mid-way through this skill's workflow. Phase 1 (Plan) is done; resume at Phase 2 (Execute), Step 1 of the plan above. **Critical: the tutorial skill requires executing ONE step at a time — present a step, wait for the user to run it and paste output, verify, then proceed. Never front-load multiple steps.**
- **`create-nav-guide`** — after the setup is complete and verified, capture the CouchDB/LiveSync deployment as a new nav guide (e.g. `ObsidianLiveSyncNavGuide.md`) in `b0ttsagent/NavGuides/`, following the same front-matter + structure pattern as the existing guides.
- **`close` / `closev2`** — at the very end of the work, to log the session.

## Key references (external)

- LiveSync README: https://github.com/vrtmrz/obsidian-livesync/blob/main/README.md
- CouchDB on own server: https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/setup_own_server.md
- Plugin quick setup: https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/quick_setup.md
- Troubleshooting (mobile SSL constraint): https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/troubleshooting.md
- couchdb-init.sh: https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh

## Key files (local, this repo)

- `b0ttsagent/NavGuides/VpsNavGuide.md` — VPS access, conventions, Tailscale Serve, ACL.
- `b0ttsagent/NavGuides/InterVpsNavGuide.md` — second VPS (Minecraft only; not used here).
- `b0ttsagent/NavGuides/PostgrestApiGuide.md` — documents the existing public-facing Caddy + Cloudflare Tunnel setup at `b0tts.dev/api` (separate from the tailnet path we're using).
- `.agents/skills/tutorial/SKILL.md` — the workflow we're following.

## Constraints / rules for the next agent

- **NEVER SSH into the VPS.** All VPS commands are run by the user over SSH; the agent diagnoses from pasted output.
- **Do not read the contents** of `C:\Development\GameProjects\Whack Grass\Planning Docs` — it's sensitive. Only check existence / `.obsidian` presence as needed for setup.
- The vault is **not in git** and must never be committed.
- **Redact all credentials** (CouchDB user/pass, E2E passphrase, setup-URI passphrase) from any handoff, nav guide, or doc. Store them only in `/home/couchdb/.env` on the VPS and the user's password manager.
- Follow the `tutorial` skill strictly: one step at a time, verify each, never front-load.
