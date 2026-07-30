#!/usr/bin/env bash
# Remake the minecraft-hc-solo world (same seed, fresh world).
# Run on the InterServer VPS over Tailscale as the `deploy` user.
#
# Source: b0ttsagent/NavGuides/MinecraftHcSoloNavGuide.md

cd /home/minecraft-hc-solo \
  && sudo docker compose down \
  && sudo rm -rf data/world data/world_nether data/world_the_end \
  && sudo docker compose up -d \
  && sudo docker logs minecraft-hc-solo --tail 30 -f