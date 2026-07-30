#!/bin/bash
set -e
# ============================================================
# Fix ViaProxy crash-loop (bedrock connect) — run on InterServer VPS
# Root cause: ViaProxy ENTRYPOINT hardcodes `java -jar` with no -Xmx;
# container-aware default heap (25% of 1g) lands just under the 256MB
# minimum -> FATAL -> Geyser plugin never loads -> nothing on UDP 19132.
# Fix: override entrypoint to force -Xmx512m, recreate, verify.
# ============================================================

CD=/home/minecraft
F=$CD/docker-compose.yml

echo "===== 0. Backup compose file ====="
sudo cp -a "$F" "$F.bak.$(date +%Y%m%d-%H%M%S)"
ls -la "$F".bak.* | tail -1

echo ""
echo "===== 1. Insert entrypoint override (idempotent) ====="
if sudo grep -q '^    entrypoint: \["java", "-Xmx512m"' "$F"; then
  echo "  entrypoint override already present — skipping"
else
  sudo sed -i '\|^    container_name: viaproxy$|i\    entrypoint: ["java", "-Xmx512m", "-jar", "/app/ViaProxy.jar", "config", "viaproxy.yml"]' "$F"
  echo "  inserted entrypoint line before 'container_name: viaproxy'"
fi

echo ""
echo "===== 2. Show resulting viaproxy block ====="
sudo grep -A 12 "^  viaproxy:" "$F"

echo ""
echo "===== 3. Validate compose ====="
sudo docker compose -f "$F" config --quiet && echo "  compose OK" || { echo "  !! compose INVALID — check $F"; exit 1; }

echo ""
echo "===== 4. Recreate viaproxy with new entrypoint ====="
cd "$CD" && sudo docker compose up -d --force-recreate viaproxy

echo ""
echo "===== 5. Wait 12s, then logs ====="
sleep 12
sudo docker logs viaproxy --tail 50 2>&1

echo ""
echo "===== 6. Is UDP 19132 now held? ====="
sudo ss -lunp | grep 19132 || echo "  !! still nothing on 19132/udp"

echo ""
echo "===== 7. Container status ====="
sudo docker ps --format "table {{.Names}}\t{{.Status}}" | grep -iE 'viaproxy|minecraft|NAMES'

echo ""
echo "===== 8. Geyser config (generated on first successful start) ====="
GC=/home/viaproxy/plugins/Geyser/config.yml
if sudo test -f "$GC"; then
  echo "--- $GC exists ---"
  sudo grep -nE '^\s*(address|port|auth-type|clone-remote-port):' "$GC" | grep -v '^\s*#'
else
  echo "  (no Geyser config yet — ViaProxy may still be starting; check logs above)"
fi

echo ""
echo "===== 9. Geyser/Floodgate lines in viaproxy logs (look for bedrock bind) ====="
sudo docker logs viaproxy 2>&1 | grep -iE 'geyser|floodgate|bedrock|raknet|19132|Started|listening' | tail -20 || echo "  (none yet)"

echo ""
echo "===== DONE ====="
echo "If section 6 shows a listener on 19132/udp, have the Xbox try connecting now."
echo "If it connects but gets rejected (not whitelisted / online-mode), we set up"
echo "Floodgate key sharing next."
