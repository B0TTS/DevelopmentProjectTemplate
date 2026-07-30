# Handoff: ViaProxy Bridge Plan Ready — Bedrock Cross-Play Resolution

## Summary

Chose **Option A (ViaProxy bridge)** to resolve the Bedrock version incompatibility blocking the live MyngaCraft server. Researched and pinned exact current versions, and — importantly — **corrected the prior handoff's Option A architecture** using the official GeyserMC wiki. A complete, evidence-backed 10-step execution plan is ready. **Nothing has been executed on the VPS yet.** The session ended at "plan confirmed, ready to start Step 1."

> Previous handoffs (same folder):
> - [`minecraft-server-live-bedrock-incompatibility.md`](./minecraft-server-live-bedrock-incompatibility.md) — discovered the 26.32 Bedrock blocker, presented the 3 options
> - [`minecraft-crossplay-interserver-setup.md`](./minecraft-crossplay-interserver-setup.md) — original planning handoff

The server is **still running** exactly as documented in the prior handoff (Java 1.21.11 Fabric live, Bedrock broken, Geyser-Fabric 2.9.5 still installed on the backend).

---

## The Decision

**Option A — ViaProxy bridge** (Geyser's officially recommended path for "Fabric not on latest MC + current Bedrock client"). Confirmed by user this session. Options B (upgrade to MC Java 26.1) and C (Java-only) rejected.

## 🔴 Key Correction to the Prior Handoff's Option A

The prior handoff said: *"Remove Geyser-Fabric **+ Floodgate-Fabric** mods from the server"* and *"run Floodgate plugins in ViaProxy."*

**This is wrong for an `online-mode=true` Fabric backend.** The official GeyserMC wiki page "Floodgate setup with Geyser for ViaProxy" states:

> "To be able to use Floodgate authentication, you need to be able to install Floodgate **on the Java server you are connecting to**."
> 1. Install the platform-specific Floodgate jar (e.g. **floodgate-fabric**) **on the backend**.
> 2. Copy the `key.pem` from the backend's Floodgate config folder to ViaProxy's `/plugins/Geyser/` directory.
> 3. Restart ViaProxy.

**There is no separate "Floodgate-ViaProxy" jar.** ViaProxy is a protocol translator (connects to the backend as a normal Java client), NOT a Velocity/BungeeCord-style proxy with player forwarding. Because the Fabric backend is `online-mode=true`, Bedrock players (no Java account) can only bypass Mojang auth if **Floodgate-Fabric stays on the backend** to verify the signed identity. ViaProxy's Geyser just needs the backend's `key.pem`.

Evidence source (raw wiki include, JS-rendered page doesn't extract):
`https://raw.githubusercontent.com/GeyserMC/GeyserWiki/master/_includes/setup/instructions/floodgate/viaproxy.md`

Corroborating: GeyserWiki issues doc — *"you have enabled `send-floodgate-data`... but either Floodgate isn't installed on the target server, or your floodgate key isn't the same between the installs."*

### Corrected architecture

```
Bedrock 26.32 client
  → Geyser-ViaProxy 2.10.1   (listens 19132/udp, signs identity with key.pem)
  → ViaProxy 3.4.12          (translates Java 26.1 → 1.21.11, in-process)
  → Fabric 1.21.11 server    (25565, online-mode=true)
       └─ Floodgate-Fabric KEPT here, same key.pem → accepts Bedrock player
```

- **Remove ONLY Geyser-Fabric** from the backend (it can't handle 26.32 anyway).
- **KEEP Floodgate-Fabric** on the backend; reuse its existing `key.pem`.
- In ViaProxy: only **Geyser-ViaProxy.jar** + the backend's **key.pem** copied to `/plugins/Geyser/`.

---

## Researched & Pinned Versions (verified today, 2026-07-07)

| Component | Version | Source / note |
|---|---|---|
| Geyser-ViaProxy | **2.10.1 build 1181** (built 2026-07-07) | `download.geysermc.org` API — supports Bedrock **26.0–26.32**, presents Java 26.1 |
| ViaProxy | **3.4.12** (latest release, 2026-06-29) | GitHub releases; Docker image `ghcr.io/viaversion/viaproxy:latest` bundles Temurin 25 JRE |
| Floodgate-Fabric | already installed on backend (2.2.6-b54) | keep as-is, reuse `key.pem` |

### Direct download URL (headless VPS-friendly, verified 200 OK + sha256)

```
https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/viaproxy
→ Geyser-ViaProxy.jar, 18,369,756 bytes
  sha256: 48d16b48b6074a8ea085ff6e87280d60d75bcfca75e77b4e35874126e4d2e727
  filename* (CD): Geyser-ViaProxy.jar
```

API metadata endpoint (for re-verifying version at execution time):
`https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest`

### Verified ViaProxy config keys (from `ViaProxyConfig.java` source)

The Docker image `ENTRYPOINT` is `java -jar /app/ViaProxy.jar config viaproxy.yml` — and the in-code usage message confirms `config <file>` **starts** ViaProxy with that config (does NOT just generate-and-exit). Relevant keys for this setup:
- `bind-address` (default `0.0.0.0:25568`) — ViaProxy's own listen port (Java-side, internal)
- `target-address` (default `127.0.0.1:25565`) — the backend; set to the mc compose **service name**
- `target-version` (default auto-detect) — set to `1.21.11`; fallback to auto-detect if the literal is rejected
- `auth-method` — `none` (offline at the ViaProxy→backend hop); Floodgate handles Bedrock identity separately via key.pem

### Verified Geyser-ViaProxy behavior (from ViaProxy setup wiki)

- Geyser-ViaProxy listens on `19132/udp` by default (config at `/plugins/Geyser/config.yml`).
- **`auth-type` in the Geyser config is ignored and managed by ViaProxy automatically** — do not manually set it.
- `clone-remote-port: false` (default) — keep; we want Bedrock on 19132, not the ViaProxy bind port.

---

## The 10-Step Execution Plan (NOT yet started)

Conventions: agent never touches the VPS. Every command is written to `b0ttsagent/temp/` files for the user to paste. One step at a time, verify each before moving on.

1. **Pre-flight inspection (read-only)** — confirm `mc` container running & healthy; `free -m` headroom for ~1 GB container; the mc compose **service name** (for `target-address`); current `ports:` block (which `19132/udp` line moves); `Geyser-Fabric.jar` + `Floodgate-Fabric.jar` present in `/home/minecraft/data/mods/`; `/home/minecraft/data/config/floodgate/key.pem` exists.
2. **Stage ViaProxy data dir + download** — `mkdir -p /home/viaproxy/plugins/Geyser`; `wget` Geyser-ViaProxy.jar into `/home/viaproxy/plugins/`; verify sha256 `48d16b48…d2e727`; `cp /home/minecraft/data/config/floodgate/key.pem /home/viaproxy/plugins/Geyser/key.pem` (chmod 600).
3. **Edit `docker-compose.yml`** — add `viaproxy` service (image `ghcr.io/viaversion/viaproxy:latest`, volume `/home/viaproxy:/app/run`, publish `19132:19132/udp`, `restart: unless-stopped`, `depends_on: [mc]`); **in the same edit** remove the `19132:19132/udp` line from the `mc` service (it moves to viaproxy). `docker compose up -d`.
4. **Generate `viaproxy.yml`** — `docker compose up -d viaproxy` auto-generates `/home/viaproxy/viaproxy.yml` with defaults and starts; check logs to confirm generation, then `docker compose stop viaproxy` to edit.
5. **Configure `viaproxy.yml` + start** — set `bind-address: 0.0.0.0:25568`, `target-address: <mc-service>:25565`, `target-version: 1.21.11`, `auth-method: none`; `docker compose up -d viaproxy`; verify logs (listening, reaches backend). Fallback: auto-detect if `1.21.11` literal is rejected.
6. **Remove Geyser-Fabric from backend** — stop `mc`; delete **only** `Geyser-Fabric-*.jar` (keep `Floodgate-Fabric-*.jar`); restart `mc`; confirm clean startup, Floodgate-Fabric still loaded, key.pem intact, Java players connect on 25565.
7. **Verify Geyser-ViaProxy** — inspect `/home/viaproxy/plugins/Geyser/config.yml` (bedrock port 19132, address 0.0.0.0; `auth-type` auto-managed, leave it); restart viaproxy; confirm logs show `Started Geyser on 0.0.0.0:19132` and **no** "new Geyser update available to support Bedrock 26.32" warning.
8. **Firewall + first Bedrock connection test** — confirm UFW allows `19132/udp` (already open per prior handoff); from a **Windows/mobile** Bedrock client add server `myngacraft.b0tts.me:19132` and connect; diagnose from ViaProxy + mc logs on failure.
9. **Whitelist Bedrock players** — once a Bedrock player has connected once, `fwhitelist add gimymycookie1` and `fwhitelist add Mrgoat0112` from the ViaProxy/Geyser console.
10. **Harden + record** — pin the ViaProxy image (record resolved version + digest from logs), set `mem_limit: 1g`, confirm `restart: unless-stopped`; record final versions in a nav guide / handoff update.

> The user confirmed the plan ("Looks good"). Next session starts at **Step 1**.

---

## Current State

- **VPS**: untouched since prior handoff. `mc` container running; `67.211.215.84`; `myngacraft.b0tts.me` resolves correctly.
- **Java Edition**: working (`myngacraft.b0tts.me:25565`, MC 1.21.11 Fabric, online-mode=true, whitelist on).
- **Bedrock**: still broken (Geyser-Fabric 2.9.5 on backend can't serve 26.32 clients). No ViaProxy container exists yet.
- **Files**: `/home/minecraft/docker-compose.yml` (single `mc` service), `/home/minecraft/data/mods/` (incl. `Geyser-Fabric-2.9.5-b1103.jar` + `Floodgate-Fabric-2.2.6-b54.jar`), `/home/minecraft/data/config/floodgate/key.pem`.
- **Firewall**: UFW open on `25565/tcp` and `19132/udp` (19132 currently published by the `mc` service, will move to viaproxy).

## Open Decisions

- None blocking. All version pins and the architecture are settled. The only in-flight items are the pending independent tasks below (none block Step 1).

## Still Pending (independent of Bedrock path — carried from prior handoff)

1. ⬜ **Backup cron** — daily 4am HST, 30-day retention tar.gz to `/home/minecraft/backups/`, log to `backup.log`. Step 13 of the original plan. Do regardless of Bedrock path.
2. ⬜ **Cloudflare/DNS nav guide** for `b0tts.me` — original handoff noted none exists; use `create-nav-guide` skill.
3. ⬜ **Console-access workaround** for Xbox/Switch Bedrock — BedrockConnect / BedrockTogether / Phantom (client-side). Xbox Bedrock has no "Add Server" button; Step 8's connection test should use Windows/mobile first.

## Suggested Skills for Next Session

- **`tutorial`** — continue executing the 10-step plan one step at a time (this is what was active). Start at Step 1.
- **`create-nav-guide`** — after the server is fully working, capture the Cloudflare/DNS management reference for `b0tts.me`.
- **`create-execution-plan`** — *optional*; if the user wants a formal multi-container PLAN.md before touching the VPS, this skill could formalize the ViaProxy bridge. The inline 10-step plan above is likely sufficient.

## Key References

- **Geyser-ViaProxy setup wiki**: https://geysermc.org/wiki/geyser/setup/self/viaproxy/
- **Floodgate-ViaProxy setup (raw include)**: `https://raw.githubusercontent.com/GeyserMC/GeyserWiki/master/_includes/setup/instructions/floodgate/viaproxy.md`
- **Geyser supported versions**: https://geysermc.org/wiki/geyser/supported-versions/ (Bedrock 26.0–26.32, Java 26.1–26.1.2)
- **ViaProxy repo/releases**: https://github.com/ViaVersion/ViaProxy (latest v3.4.12; Docker `ghcr.io/viaversion/viaproxy:latest`)
- **ViaProxyConfig.java** (config keys): `src/main/java/net/raphimc/viaproxy/protocoltranslator/viaproxy/ViaProxyConfig.java`
- **Geyser download API**: `https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest`

---

*Handoff created 2026-07-07. Next session: execute the ViaProxy bridge plan starting at Step 1.*
