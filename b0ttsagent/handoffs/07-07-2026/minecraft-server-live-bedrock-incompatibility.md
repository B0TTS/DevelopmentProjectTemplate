# Handoff: Minecraft Server Live — Bedrock Incompatibility Discovered

## Summary

Executed the Fabric 1.21.11 Java/Bedrock cross-play server setup on the InterServer VPS (`67.211.215.84`). **Java Edition works perfectly.** Bedrock cross-play hit a hard version incompatibility: current Bedrock clients (26.32) cannot connect to Geyser-Fabric on a 1.21.11 server. Three resolution options were presented; the session ended mid-decision.

> Previous planning handoff: [`minecraft-crossplay-interserver-setup.md`](../07-07-2026/minecraft-crossplay-interserver-setup.md)

---

## What Was Accomplished

### Server is live and running ✅

| Property | Value |
|---|---|
| Status | **Running** (`docker compose up -d`) |
| Access | Public IP `67.211.215.84` |
| Domain | `myngacraft.b0tts.me` → `67.211.215.84` (Cloudflare A record, DNS-only) |
| Java port | `25565/tcp` |
| Bedrock port | `19132/udp` (Geyser listens — can't serve current clients, see below) |
| Connection | Java 1.21.11 client → `myngacraft.b0tts.me:25565` ✅ tested working |
| Whitelist | 2 Java players: `GEGEgaymers` (op), `Gimymycookie` |
| World seed | Random (unset in compose; can change) |
| RCON | Port 25575, password unchanged from compose (`mc-rcon-changeme`) |

### Software stack

| Component | Version | Notes |
|---|---|---|
| Minecraft | 1.21.11 Fabric (loader 0.19.3) | itzg/minecraft-server |
| Docker | 29.6.1 / Compose v5.3.1 | Installed during setup |
| Lithium | 0.21.4+mc1.21.11 | auto-downloaded via MODRINTH_PROJECTS |
| Krypton | 0.2.10 | auto-downloaded |
| FerriteCore | latest | slug is `ferrite-core` (hyphenated, NOT `ferritecore`) |
| **Noisium (fork)** | **2.8.3+mc1.21.11** | ⚠️ slug is `noisiumforked` (by Coredex), NOT `noisium`. The original `noisium` has no 1.21.11 Fabric build. Discovered at startup — the server crash-looped until the slug was fixed. |
| Chunky | latest | auto-downloaded |
| Spark | 1.10.170 | auto-downloaded |
| Fabric API | latest | auto-downloaded |
| Geyser-Fabric | 2.9.5-b1103 (pinned) | Manual JAR in `/home/minecraft/data/mods/` |
| Floodgate-Fabric | 2.2.6-b54 (pinned) | Manual JAR in `/home/minecraft/data/mods/` |

### Firewall (UFW)

```
[1] Anywhere on tailscale0     ALLOW IN
[2] 25565/tcp                  ALLOW IN   (Java, public)
[3] 19132/udp                  ALLOW IN   (Bedrock, public)
```

### File locations

| Path | Description |
|---|---|
| `/home/minecraft/docker-compose.yml` | Compose file (UID 999, GID 982, MEMORY 4G, mem_limit 5g) |
| `/home/minecraft/data/` | Server world, mods, configs |
| `/home/minecraft/data/mods/` | Manual JARs (Geyser, Floodgate) + auto-downloaded Modrinth mods |
| `/home/minecraft/data/config/Geyser-Fabric/config.yml` | `auth-type: floodgate`, `port: 19132`, `clone-remote-port: false` |
| `/home/minecraft/data/config/floodgate/config.yml` | `username-prefix: "."` |
| `/home/minecraft/data/config/floodgate/key.pem` | Floodgate auth key (auto-generated, 16 bytes) |

### Key compose environment variables

```yaml
TYPE: FABRIC
VERSION: "1.21.11"
MEMORY: "4G"
USE_AIKAR_FLAGS: "true"
UID: 999
GID: 982
MODRINTH_PROJECTS: |
  fabric-api
  lithium
  krypton
  ferrite-core
  noisiumforked
  chunky
  spark
ENABLE_RCON: "true"
RCON_PORT: 25575
RCON_PASSWORD: "mc-rcon-changeme"
ENABLE_WHITELIST: "true"
ONLINE_MODE: "true"
DIFFICULTY: hard
MOTD: "MyngaCraft"
# SEED commented out → random world
```

---

## 🔴 THE BLOCKER: Bedrock Version Incompatibility

### Root cause

**Geyser-Fabric only supports the latest Minecraft Java version** (documented Geyser limitation — see [Supported Versions](https://geysermc.org/wiki/geyser/supported-versions/)). The version chain is:

| Geyser | MC Java | Bedrock support |
|---|---|---|
| 2.9.5-b1103 (our build) | 1.21.11 | ~26.10 |
| 2.9.6-b1133 (newest for 1.21.11) | 1.21.11 | **26.20 only** |
| 2.10.x (latest) | **26.1 only** | **26.0–26.32** |

Current Bedrock clients auto-update to **26.32**. No Geyser-Fabric build for MC 1.21.11 supports 26.32. To support 26.32, Geyser must be 2.10.x, which requires a MC Java 26.1 server — but Geyser-Fabric can't run on a non-latest MC version.

The handoff's note *"latest Geyser 2.10.1 only supports Java 26.1+"* meant **Minecraft Java Edition 26.1** — it correctly pinned 2.9.5. What it missed: Bedrock clients would auto-update past the 2.9.5 support ceiling.

### Server log evidence

```
[14:43:23] [INFO]: There's a new Geyser update available to support Bedrock version 26.32.
```

Geyser itself reporting it can't handle 26.32 and needs an update — but the update (2.10.x) won't run on our server.

### Attempted Bedrock connection

- Xbox user: couldn't test (Xbox Bedrock has no "Add Server" button for custom servers — see [Console access](#console-access) below)
- The user saw the Geyser update message and interpreted it as "need to install latest Geyser"
- No Bedrock player has successfully connected yet

---

## The Three Options (Session Ended Here)

### Option A — ViaProxy bridge (Geyser's officially recommended path) ⭐

```
Bedrock 26.32
  → Geyser-ViaProxy 2.10.x (latest, in ViaProxy)
  → ViaProxy (translates Java 26.1 → 1.21.11)
  → Fabric 1.21.11 server (25565)
```

- Remove Geyser-Fabric + Floodgate-Fabric mods from the server
- Run a second container: ViaProxy with Geyser-ViaProxy + Floodgate plugins, exposing 19132/udp, proxying to 25565
- Floodgate auth confirmed to work in this setup
- Preserves MC 1.21.11 + all performance mods
- Cost: extra container, Geyser loses direct Fabric world access (slightly more memory; fine for ≤5 players)
- **This is the path Geyser's wiki explicitly documents for "Fabric not on latest MC + current Bedrock client"**

### Option B — Upgrade server to MC Java 26.1

- `VERSION: 1.21.11` → `26.1`
- All 7 performance mods need 26.1-compatible builds → **availability uncertain**
- World forward-migrates 1.21.11 → 26.1 (usually safe)
- Geyser-Fabric 2.10.x + Floodgate-Fabric (26.1) natively → simplest final architecture
- Risk: mod availability for 26.1

### Option C — Java-only, abandon Bedrock cross-play

- Keep as-is; Bedrock likely non-functional for current clients
- Not realistic unless Bedrock players can stay on ≤26.20

### User was mid-decision at session end

User typed: *"Lets do a"* (cut off — likely choosing Option A, but unconfirmed).

---

## What's Still Not Done

### ⬜ Step 13: Backup cron

The backup script and root crontab from the old server pattern (daily 4am HST, 30-day retention tar.gz to `/home/minecraft/backups/`, log to `backup.log`) have NOT been created. This should be done regardless of Bedrock path.

### ⬜ Cloudflare/DNS Nav Guide

The original handoff noted no nav guide exists for Cloudflare/DNS management for `b0tts.me`. One should be created using the `create-nav-guide` skill.

### ⬜ Bedrock players whitelist

Two Bedrock-only players identified but not whitelisted via `fwhitelist`:
- `gimymycookie1`
- `Mrgoat0112`

`Gimymycookie` has a Java account and was whitelisted via `whitelist add`. The other two appear to be Bedrock-only gamertags (Mojang lookup says "does not exist"). Floodgate's `fwhitelist` command is the correct path (no prefix needed — `fwhitelist add <bedrock_name>`), but wasn't tested because no Bedrock player connected.

### ⬜ Console access workaround

Xbox/PlayStation/Switch Bedrock has no "Add Server" button — only featured servers. The standard workarounds:

1. **BedrockConnect** — DNS redirect trick (user tried, said "didn't work" — likely the public DNS was down)
2. **BedrockTogether** (iOS/Android app) — broadcasts as LAN game; install on phone on same Wi-Fi as Xbox
3. **Phantom** (desktop tool) — same LAN broadcast concept; runs on PC on same Wi-Fi

These are client-side and independent of server setup.

---

## Key Gotchas Discovered

1. **`noisium` → `noisiumforked`** — Original Noisium Modrinth project has no Fabric 1.21.11 file. The fork by Coredex (slug `noisiumforked`, version 2.8.3+mc1.21.11) is the working replacement. The container crash-loops with a fatal Modrinth download error if `noisium` is used.

2. **`ferritecore` → `ferrite-core`** — The Modrinth slug is hyphenated. The itzg docs example shows `ferritecore` (one word), which 404s on the Modrinth API. Used correctly in the compose.

3. **`clone-remote-port: false`, not `true`** — The planning handoff said to set it `true`. Per Geyser docs, `true` overwrites the Bedrock port with the Java port (forces both to 25565). Since we want Bedrock on 19132, the correct setting is `false` (which is also the default). Verified correct in the running config.

4. **Geyser default `auth-type` was `online`, not `offline`** — Changed to `floodgate` via sed edit. Floodgate key auto-links on Fabric (no manual key copy needed, unlike Spigot).

5. **`tee` heredoc + RCON console paste** — The VPS terminal doesn't handle multi-line copy/paste well from the chat. All commands were written to `b0ttsagent/temp/` files first, then pasted.

6. **DNS propagation on VPS** — `dig +short myngacraft.b0tts.me` returned empty from the VPS's default resolver, but `dig @1.1.1.1 +short` correctly returned `67.211.215.84`. The record is correct on Cloudflare; the VPS local resolver was slow. External clients resolve fine.

---

## Suggested Skills for Next Session

- If **Option A** (ViaProxy): a new multi-container architecture plan. The `create-execution-plan` skill could formalize the ViaProxy bridge setup. The handoff decision to use independent servers (no Velocity proxy) on the original compose should be reviewed — ViaProxy adds a lightweight proxy layer for Geyser only, not full-blown Velocity.
- **Backup cron setup** — step 13 of original plan, independent of Bedrock path, still pending.
- **`create-nav-guide`** — create the Cloudflare/DNS nav guide the original handoff said was missing.

---

*Handoff created 07-07-2026. Next session: resolve Bedrock path (likely ViaProxy) + backup cron + DNS nav guide.*
