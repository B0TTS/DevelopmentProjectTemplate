---
name: regenerate-minecraft-world
description: Regenerate a Minecraft world with a specific seed on a Docker-based VPS running itzg/minecraft-server. Use when the user wants to change the Minecraft world seed, reset the world, or fix a world that does not match the expected seed.
---

# Regenerate Minecraft World

## Quick start

```bash
cd /home/minecraft
sudo sed -i 's/LEVEL_SEED/SEED/' docker-compose.yml
grep -i seed docker-compose.yml
sudo docker compose down
sudo rm -rf data/world data/world_nether data/world_the_end
sudo docker compose up -d
sudo docker logs minecraft --tail 30 -f
```

## Workflows

### Change seed on an existing server

- [ ] Read the VPS Minecraft nav guide at `.pi/b0ttsagent/NavGuides/MinecraftNavGuide.md`.
- [ ] Verify the compose file uses `SEED`, not `LEVEL_SEED`.
- [ ] Stop the container: `cd /home/minecraft && sudo docker compose down`.
- [ ] Delete the three dimension folders:
  - `sudo rm -rf /home/minecraft/data/world`
  - `sudo rm -rf /home/minecraft/data/world_nether`
  - `sudo rm -rf /home/minecraft/data/world_the_end`
- [ ] Start the container: `sudo docker compose up -d`.
- [ ] Watch logs until `Done (...s)!` appears.
- [ ] Have the user run `/seed` in-game to confirm.

### Troubleshoot "world doesn't match seed"

- [ ] Ask for `grep -i seed /home/minecraft/docker-compose.yml`.
- [ ] If it shows `LEVEL_SEED`, explain it must be `SEED` and provide the sed fix.
- [ ] Ask whether the world folders were deleted before startup.
- [ ] Remind the user that `--force-recreate` does NOT delete world data.

## Important warnings

- The `itzg/minecraft-server` image maps env var `SEED` to `server.properties`'s `level-seed`. `LEVEL_SEED` is silently ignored.
- `--force-recreate` only rebuilds the container; the `/home/minecraft/data` volume persists.
- Always back up before wiping world folders if there is anything worth keeping.
