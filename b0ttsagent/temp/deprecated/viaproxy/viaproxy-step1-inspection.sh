#!/bin/bash
# ============================================================
# Step 1 — Pre-flight Inspection (read-only, no changes made)
# ============================================================
# Run on the VPS. Copy-paste each block one at a time.

echo "===== 1. mc container status ====="
sudo docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep mc

echo ""
echo "===== 2. free memory (headroom for ~1GB ViaProxy container) ====="
free -m

echo ""
echo "===== 3. mc compose service name & ports block ====="
echo "--- Service name (the key under 'services:' in docker-compose.yml) ---"
cd /home/minecraft
cat docker-compose.yml | head -30
echo ""
echo "--- Full ports block of mc service ---"
sudo docker compose config | grep -A 20 "name: mc" || sudo docker compose config | grep -A 20 "container_name: mc"

echo ""
echo "===== 4. mods directory (Geyser-Fabric + Floodgate-Fabric) ====="
ls -lh /home/minecraft/data/mods/ | grep -i -E "geyser|floodgate"

echo ""
echo "===== 5. Floodgate key.pem ====="
ls -lh /home/minecraft/data/config/floodgate/key.pem
echo ""
echo "--- key.pem first 2 lines (should say BEGIN RSA PRIVATE KEY) ---"
head -2 /home/minecraft/data/config/floodgate/key.pem

echo ""
echo "===== DONE: Step 1 inspection ====="
echo "Share the output above and we'll move to Step 2."
