# minecraft-seed-docker-fix
**Date:** 06-24-2026  
**Time:** 02:34

## What happened

The user wanted to set their Minecraft server on the VPS to use seed `7414878756768619920`. They had run Docker Compose with `--force-recreate` multiple times, but the generated world never matched the seed.

Investigation showed:
- The server was listed as stopped in the nav guide with `restart: "no"`.
- The `docker-compose.yml` on the VPS used `LEVEL_SEED` instead of `SEED`.
- The `itzg/minecraft-server` image only recognizes the env var `SEED`; `LEVEL_SEED` is silently ignored, causing a random world.
- `--force-recreate` only rebuilds the container and leaves `/home/minecraft/data` intact, so old world data was never wiped.

I provided the fix: change `LEVEL_SEED` to `SEED`, stop the container, delete `data/world`, `data/world_nether`, and `data/world_the_end`, then start fresh. I also verified the correct env var name against the official `itzg/docker-minecraft-server` docs.

## Skills used

- `closev2` (end-of-session close)
- `write-a-skill` (via closev2 branch 2 approval)

## Closing outcomes

- Updated `.pi/b0ttsagent/NavGuides/MinecraftNavGuide.md`:
  - Added a warning that `LEVEL_SEED` is invalid and `SEED` must be used.
  - Added a warning that `--force-recreate` does not delete world data.
- Created new skill `.pi/agent/skills/regenerate-minecraft-world/SKILL.md`.
- Wrote scratchpads and session log for this close session.

## Open / next

- User still needs to run the fix on the VPS:
  ```bash
  cd /home/minecraft
  sudo sed -i 's/LEVEL_SEED/SEED/' docker-compose.yml
  sudo docker compose down
  sudo rm -rf data/world data/world_nether data/world_the_end
  sudo docker compose up -d
  sudo docker logs minecraft --tail 30 -f
  ```
- Optionally create `/home/minecraft/regenerate-world.sh` helper script (declined as a tip).
