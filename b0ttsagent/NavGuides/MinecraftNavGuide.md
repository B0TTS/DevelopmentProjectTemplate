---
name: MinecraftNavGuide
topics: [minecraft, mods, server, gaming]
description: "Reference for Minecraft server configuration and mod management"
---

# Minecraft Server Guide

> **Status: Stopped** (2026-06-19). Container is down with `restart: "no"` in docker-compose.yml. World data preserved at `/home/minecraft/data/`. Daily backup cron at `/etc/cron.d/minecraft-backup` still runs but fails silently (container not found). To restore, change `restart: "no"` back to `restart: unless-stopped` and run `cd /home/minecraft && sudo docker compose up -d`.

---

## Reference

### Server Config

|Property|Value|
|---|---|
|Minecraft Version|1.21.11|
|Server Type|Fabric|
|World Seed|7414878756768619920|
|Game Mode|Hardcore Survival|
|View Distance|10|
|Simulation Distance|8|
|Spawn Protection|0|
|Container Memory Limit|4GB|
|JVM Heap|3072m|
|JVM Flags|Aikar's flags (`USE_AIKAR_FLAGS: true`)|
|UID:GID|987:982|
|RCON|Port 25575, password `mc-rcon-changeme`|
|Restart Policy|`unless-stopped`|

### File Locations

| File             | Path                                 |     |
| ---------------- | ------------------------------------ | --- |
| Compose file     | `/home/minecraft/docker-compose.yml` |     |
| World data       | `/home/minecraft/data`               |     |
| Backup script    | `/home/minecraft/backup.sh`          |     |
| Backup directory | `/home/minecraft/backups/`           |     |
| Backup log       | `/home/minecraft/backups/backup.log` |     |
| Pregen script    | `/home/minecraft/pregen.sh`          |     |
| Pregen log       | `/home/minecraft/pregen.log`         |     |

### Mods

Pulled automatically from Modrinth via `MODRINTH_PROJECTS` in the compose file.

> `fabric-api` must be explicitly listed — the server will crash on startup without it.

|Mod|Notes|
|---|---|
|Lithium||
|Chunky|World pre-generation|
|Krypton||
|FerriteCore||
|Fabric API|Required, not auto-included|
|Spark|Performance profiler|
|Noisium||

### Connection

|Property|Value|
|---|---|
|Server Address|`100.122.184.37:25565`|
|Client|Java Edition 1.21.1|
|Requirement|Tailscale (VPN)|

> Public IP is locked down via UFW. Tailscale is required to connect.

### Backups

|Property|Value|
|---|---|
|Schedule|Daily at 4:00 AM UTC-10 (14:00 UTC)|
|Retention|30 days|
|Format|`minecraft-YYYY-MM-DD_HH-MM-SS.tar.gz`|
|Via|Root crontab (independent of Docker)|

### Chunky Pre-gen Status

|Dimension|Radius|Status|
|---|---|---|
|Overworld (`minecraft:overworld`)|5000 blocks|Not started|
|Nether (`minecraft:the_nether`)|10000 blocks|Not started|

> `pregen.sh` auto-chains overworld → nether. Polls logs every 60s, starts nether once overworld completion is detected.

---

## Operations

### Server — Start / Stop / Restart

```bash
# Start
cd /home/minecraft && sudo docker compose up -d

# Stop
cd /home/minecraft && sudo docker compose down

# Restart
cd /home/minecraft && sudo docker compose restart
```

### Server — Check Logs

```bash
sudo docker logs minecraft --tail 20
```

### Mods — Add or Remove

Edit `MODRINTH_PROJECTS` in the compose file, then:

```bash
cd /home/minecraft && sudo docker compose up -d --force-recreate
```

### World — Sending Commands
```bash
# Use rcon cli inside of the docker container.
sudo docker exec minecraft rcon-cli "command_here"
```

### World — Regenerate

```bash
# Stop server
cd /home/minecraft && sudo docker compose down

# Delete world folders only
sudo rm -rf /home/minecraft/data/world
sudo rm -rf /home/minecraft/data/world_nether
sudo rm -rf /home/minecraft/data/world_the_end

# Start server
sudo docker compose up -d
```

### World — Regenerate with a new seed

Set `SEED` in the compose file's `environment:` block before deleting the world
folders. The itzg/minecraft-server image reads `SEED` on startup and generates
the world from it.

> **Do not use `LEVEL_SEED`.** The `itzg/minecraft-server` image only recognizes
> the environment variable `SEED` (which maps to `server.properties`'s
> `level-seed`). `LEVEL_SEED` is silently ignored and the server generates a
> random world.
>
> **`docker compose up -d --force-recreate` does not regenerate the world.** It
> only rebuilds the container from the image; the `/home/minecraft/data` volume
> (and existing `world*` folders) is left untouched. Always delete the world
> folders when changing the seed.

```bash
# 1. Check current SEED line
grep -i seed /home/minecraft/docker-compose.yml

# 2a. If a SEED line exists -> replace it
sudo sed -i 's/^.*SEED:.*/      SEED: 7414878756768619920/' /home/minecraft/docker-compose.yml

# 2b. If no SEED line -> add one under environment: (6-space indent)
#     sudo nano /home/minecraft/docker-compose.yml
#         SEED: 7414878756768619920

# 3. Verify
grep -i seed /home/minecraft/docker-compose.yml

# 4. Stop, wipe worlds, start
cd /home/minecraft && sudo docker compose down \
  && sudo rm -rf data/world data/world_nether data/world_the_end \
  && sudo docker compose up -d \
  && sudo docker logs minecraft --tail 30 -f
```

> Watch logs for `Done (...s)! For help, type "help"` to confirm the new world
> is up. Gamerules and Chunky pregen state live in `level.dat` and are wiped
> with the world — re-apply them after regen.

### Chunky — Start Pre-gen (Overworld)

```bash
sudo docker exec minecraft rcon-cli "chunky world minecraft:overworld"
sudo docker exec minecraft rcon-cli "chunky radius 5000"
sudo docker exec minecraft rcon-cli "chunky start"
```

### Chunky — Pause / Resume

```bash
# Pause
sudo docker exec minecraft rcon-cli "chunky pause"

# Resume
sudo docker exec minecraft rcon-cli "chunky continue"
```

### Chunky — Auto-chain (Overworld → Nether)

```bash
# Start pregen script in background
sudo bash -c 'nohup bash /home/minecraft/pregen.sh &> /home/minecraft/pregen.log &'

# Monitor
tail -f /home/minecraft/pregen.log
```

> Start the overworld gen first, then start the script — or start the script first and kick off gen whenever ready. The script waits until overworld completion is detected before starting the nether.

### Backups — Manual Backup

```bash
sudo bash /home/minecraft/backup.sh
```

### Backups — Restore

```bash
# Stop server
cd /home/minecraft && sudo docker compose down

# Extract (replace filename)
sudo tar -xzf /home/minecraft/backups/minecraft-YYYY-MM-DD_HH-MM-SS.tar.gz -C /home/minecraft/data

# Start server
sudo docker compose up -d
```
