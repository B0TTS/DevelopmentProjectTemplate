---
name: MinecraftHcSoloNavGuide
topics:
  - minecraft
  - hardcore
  - fabric
  - interserver
  - docker
  - tailscale
description: Hardcore solo Fabric 1.21.11 Minecraft server on the InterServer VPS, Tailscale-only, Java-client access via port 25566.
---

> **Status: Running** (2026-07-14). Container `minecraft-hc-solo` is live on the InterServer VPS at `/home/minecraft-hc-solo/`. Daily backups at 14:00 UTC. No RCON exposed.

## Overview

| Property          | Value                                     |
|-------------------|-------------------------------------------|
| Container         | `minecraft-hc-solo`                       |
| System user       | `minecraft-hc-solo` (UID 995, GID 981)    |
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
| RCON              | Not exposed (internal only, no port map)  |
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

Tailscale-only — connects via `interdeploymcvps.tailf94009.ts.net:25566` or `100.100.223.6:25566`. The Tailscale ACL allows `tcp:25566` from workstation to VPS. No UFW change needed (all of `tailscale0` is already open). Java 1.21.1 client required — no Bedrock/Geyser support.

> The `deploy` user needs `sudo` for all Docker commands. Plain `docker ps` works (user is in the `docker` group), but `docker compose` and `docker logs` require `sudo`.

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
# RCON is not exposed. Use docker exec to run rcon-cli inside the container:
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
| Via          | `/etc/cron.d/minecraft-hc-solo-backup` (root crontab) |

```bash
sudo bash /home/minecraft-hc-solo/backup.sh                # Manual backup
sudo cat /home/minecraft-hc-solo/backups/backup.log        # View log
```

### Restore

```bash
cd /home/minecraft-hc-solo && sudo docker compose down
sudo tar -xzf /home/minecraft-hc-solo/backups/minecraft-hc-YYYY-MM-DD_HH-MM-SS.tar.gz -C /home/minecraft-hc-solo/data
sudo docker compose up -d
```

## Gotchas

> **Modrinth slugs:** `ferrite-core` (hyphenated, not `ferritecore`) and `noisiumforked` (not `noisium`). Using the wrong slug causes the container to crash-loop.

> **RCON noise:** The server prints `RCON running on 0.0.0.0:25575` in logs even though no port is mapped. This is harmless — RCON is trapped inside the container and unreachable from outside.

## Chunky Pre-gen (do-later)

| Dimension              | Radius  |
|------------------------|---------|
| Overworld              | 5000    |
| Nether                 | 10000   |

> See the Contabo `MinecraftNavGuide.md` "Chunky" section for exact commands and the `pregen.sh` auto-chain pattern. Chunky is already installed as a mod — just needs the pregen commands run.
