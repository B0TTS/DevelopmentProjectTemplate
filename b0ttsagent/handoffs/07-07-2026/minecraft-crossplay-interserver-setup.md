# Handoff: Minecraft Cross-Play Server on InterServer VPS

## Summary

Planned a Fabric 1.21.11 Java/Bedrock cross-play Minecraft server on the new InterServer VPS (`67.211.215.84`). First server of a planned 2–3 server Minecraft hosting setup. All software compatibility verified via web research — the stack is solid.

The next session picks up at **execution**: writing the Docker Compose file, setting up firewall rules, creating the Cloudflare DNS record, and deploying the server.

---

## Decisions Made

| Decision | Choice | Rationale |
|---|---|---|
| Server software | Fabric 1.21.11 | User preference, performance mods from old server |
| Cross-play | Geyser-Fabric 2.9.5-b1103 + Floodgate-Fabric 2.2.6-b54 | Pinned versions (latest Geyser 2.10.1 only supports Java 26.1+) |
| Multi-server architecture | Independent servers (no Velocity proxy) | Simpler setup, only 2–3 servers planned |
| RAM allocation | 4GB JVM heap | Enough for 5 players, leaves 8GB for future servers |
| Access | Fully public (no Tailscale requirement) | Player convenience |
| Whitelist | Enabled | Public IP means spam protection needed |
| Cloudflare DNS | `myngacraft.b0tts.me` A record, gray cloud (DNS-only) | Cloudflare free plan can't proxy Minecraft TCP/UDP |
| Ports | 25565/tcp (Java) + 19132/udp (Bedrock) | Standard Minecraft + Geyser Bedrock port |

---

## Verified Software Stack

| Component | Version | Source |
|---|---|---|
| Minecraft | 1.21.11 | itzg/minecraft-server (TYPE=FABRIC) |
| Lithium | 0.21.4 (mc1.21.11-fabric) | Modrinth |
| Krypton | 0.2.10 | Modrinth / SkinMC |
| FerriteCore | latest (1.21.3–1.21.11) | Modrinth |
| Noisium | Forked 2.8.4+mc1.21.11 | Modrinth |
| Fabric API | latest | Modrinth |
| Chunky | latest | Modrinth |
| Spark | latest | Modrinth |
| Geyser-Fabric | 2.9.5-b1103 | Modrinth (manual JAR download) |
| Floodgate-Fabric | 2.2.6-b54 | Modrinth (manual JAR download) |

**Note:** Performance mods use `MODRINTH_PROJECTS` auto-download (same pattern as old server). Geyser/Floodgate need manual JAR placement since they require specific pinned versions.

---

## VPS State

- **Provider:** InterServer (hostname `vps3484597`)
- **Public IP:** `67.211.215.84`
- **Tailscale:** `interdeploymcvps.tailf94009.ts.net` / `100.100.223.6`
- **OS:** Ubuntu 26.04 LTS
- **Specs:** 12GB RAM, 3 vCPU
- **Access:** SSH via Tailscale only, key-based auth via Bitwarden agent
- **UFW:** Default deny incoming, allow `tailscale0` only (no public ports open yet)
- **No Minecraft software installed yet**

---

## What Needs to Happen Next (Execution)

1. **Firewall** — `sudo ufw allow 25565/tcp` and `sudo ufw allow 19132/udp`
2. **Create system user** — `useradd --system` for `minecraft`, create `/home/minecraft/`
3. **Docker Compose file** — itzg/minecraft-server with TYPE=FABRIC, VERSION=1.21.11, 4GB MEMORY, Aikar's flags, MODRINTH_PROJECTS for perf mods, whitelist
4. **Manual mod placement** — download Geyser-Fabric 2.9.5-b1103 and Floodgate-Fabric 2.2.6-b54 JARs into `/home/minecraft/data/mods/`
5. **Geyser config** — configure Bedrock port 19132, set `clone-remote-port: true`
6. **Floodgate config** — auto-generates on first run, key file for auth
7. **Cloudflare DNS** — A record `myngacraft` → `67.211.215.84`, gray cloud toggle off
8. **Start & verify** — `docker compose up -d`, test Java + Bedrock connections
9. **Backup cron** — replicate backup pattern from old Minecraft server
10. **Whitelist** — add initial players via `whitelist.json` or RCON

---

## Key Reference Files

- `b0ttsagent/NavGuides/InterVpsNavGuide.md` — VPS access, SSH hardening, UFW, conventions
- `b0ttsagent/NavGuides/VpsNavGuide.md` — Docker conventions, system-user-per-app pattern
- `b0ttsagent/NavGuides/MinecraftNavGuide.md` — Old server config, backup pattern, Chunky workflow

## No Cloudflare/Domain Nav Guide Exists

One should be created during or after execution covering: `b0tts.me` on Cloudflare, DNS record patterns, gray vs orange cloud for game servers.

---

## Suggested Skills for Next Session

- **`create-execution-plan`** — formalize the PLAN.md from the decisions above before implementing
- **`regenerate-minecraft-world`** — relevant if starting fresh or seed selection comes up
- **`create-nav-guide`** — create a Cloudflare/DNS nav guide after setup is complete

---

*Handoff created 07-07-2026. Next session: execution.*
