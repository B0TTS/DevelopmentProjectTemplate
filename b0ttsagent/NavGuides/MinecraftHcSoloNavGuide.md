---
name: MinecraftHcSoloNavGuide
topics:
  - minecraft
  - hardcore
  - fabric
  - contabo
  - docker
  - tailscale
description: Hardcore solo Fabric 1.21.11 Minecraft server on the Contabo VPS, Tailscale-only, Java-client access via port 25566.
---

> **Status: Running on the Contabo VPS** (migrated from InterServer 2026-08-16). Container `minecraft-hc-solo` is live at `/home/minecraft-hc-solo/`. Daily backups at 14:00 UTC via root crontab. RCON mapped on host port 25575.

## Overview

| Property          | Value                                     |
|-------------------|-------------------------------------------|
| Container         | `minecraft-hc-solo`                       |
| System user       | `minecraft-hc-solo` (UID 981, GID 976)    |
| Home              | `/home/minecraft-hc-solo/`                |
| Compose file      | `/home/minecraft-hc-solo/docker-compose.yml` |
| Data directory    | `/home/minecraft-hc-solo/data`            |
| Image             | `itzg/minecraft-server`                   |
| Type              | `FABRIC`                                  |
| Version           | `1.21.11`                                 |
| Seed              | `5277846394751328433`                     |
| Hardcore          | `true`, difficulty `hard`, mode `survival` |
| Memory            | `2G` heap, `2.5g` container limit          |
| Java port         | `25566` (Tailscale-only, no public exposure) |
| RCON              | Host port 25575 (mapped). Password: `f140f768d563ec1b47327af82e6189fd` |
| OP                | `GEGEgaymers`                             |
| View distance     | 10                                        |
| Simulation dist   | 8                                         |
| Online mode       | `true`                                    |
| Spawn protection  | 0                                         |

## Mods

| Mod         | Modrinth slug      |
|-------------|--------------------|
| Fabric API  | `fabric-api`       |
| Lithium     | `lithium`          |
| Krypton     | `krypton`          |
| FerriteCore | `ferrite-core`     |
| Noisium     | `noisiumforked`    |
| Chunky      | `chunky`           |
| Spark       | `spark`            |

## Access

Tailscale-only — connects via `vmi3326176.tailf94009.ts.net:25566` or `100.122.184.37:25566`. The Tailscale ACL is tag-based (`tag:workstation` → `tag:vps`) and already includes `tcp:25566`, so no ACL changes were needed for the move. No UFW change needed (all of `tailscale0` is already open). Java 1.21.1 client required — no Bedrock/Geyser support.

> Use `sudo` for Docker commands (see `VpsNavGuide.md` conventions).

## Operations

### Start / Stop / Restart

```bash
cd /home/minecraft-hc-solo && sudo docker compose up -d      # Start
cd /home/minecraft-hc-solo && sudo docker compose down       # Stop
cd /home/minecraft-hc-solo && sudo docker compose restart    # Restart
```

### Logs

```bash
sudo docker logs minecraft-hc-solo --tail 50
sudo docker logs -f minecraft-hc-solo                       # Follow
```

### Send Commands

```bash
# RCON is mapped on 25575; rcon-cli inside the container is the easiest way in:
sudo docker exec minecraft-hc-solo rcon-cli "say hello"
```

### Verify Settings

```bash
sudo docker exec minecraft-hc-solo cat /data/server.properties | grep -E "^(hardcore|level-seed)"
```

## Backups

| Property     | Value                                        |
|--------------|----------------------------------------------|
| Script       | `/home/minecraft-hc-solo/backup.sh`          |
| Directory    | `/home/minecraft-hc-solo/backups/`           |
| Log          | `/home/minecraft-hc-solo/backups/backup.log` |
| Schedule     | Daily at 14:00 UTC (4 AM HST)                |
| Retention    | 30 days                                      |
| Format       | `minecraft-hc-YYYY-MM-DD_HH-MM-SS.tar.gz`    |
| Via          | Root crontab: `0 14 * * * /bin/bash /home/minecraft-hc-solo/backup.sh` |

```bash
sudo bash /home/minecraft-hc-solo/backup.sh                # Manual backup
sudo cat /home/minecraft-hc-solo/backups/backup.log        # View log
```

### Restore

```bash
cd /home/minecraft-hc-solo && sudo docker compose down
sudo tar -xzf /home/minecraft-hc-solo/backups/minecraft-hc-YYYY-MM-DD_HH-MM-SS.tar.gz -C /home/minecraft-hc-solo
sudo docker compose up -d
```

## Gotchas

> **Modrinth slugs:** `ferrite-core` (hyphenated, not `ferritecore`) and `noisiumforked` (not `noisium`). Using the wrong slug causes the container to crash-loop.

> **RCON is exposed now:** The compose maps `25575:25575`, and the ACL catch-all (`autogroup:member` → `*`) means any tailnet member can reach RCON. The password lives in the compose (`RCON_PASSWORD`) and is documented above — keep it strong. The log line `RCON running on 0.0.0.0:25575` is expected. `rcon-cli` inside the container reads `.rcon-cli.yaml` (regenerated from compose on startup), so no password arg is needed.

> **Migration history:** Moved from the InterServer VPS (2026-08-16). The old instance is stopped there but data + backups remain at `/home/minecraft-hc-solo/` on `interdeploymcvps` — see `InterVpsNavGuide.md`.

## Chunky Pre-gen (do-later)

| Dimension              | Radius  |
|------------------------|---------|
| Overworld              | 5000    |
| Nether                 | 10000   |

> See the Contabo `MinecraftNavGuide.md` "Chunky" section for exact commands and the `pregen.sh` auto-chain pattern. Chunky is already installed as a mod — just needs the pregen commands run.
