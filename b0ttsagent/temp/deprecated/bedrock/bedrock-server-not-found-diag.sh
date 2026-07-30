#!/bin/bash
# ============================================================
# Diagnose "server not found" — run RIGHT AFTER the Xbox fails to connect
# so the disconnect lines are fresh in the ViaProxy logs.
# Read-only.
# ============================================================

echo "############ A. VIAPROXY LOGS (last 80 lines — the real error is here) ############"
sudo docker logs viaproxy --tail 80 2>&1

echo ""
echo "############ B. FILTER LOGS for the disconnect / login failure ############"
sudo docker logs viaproxy 2>&1 | grep -iE 'disconnect|server not found|login|floodgate|key|auth|refused|timeout|connect|bedrock|geyser' | tail -40

echo ""
echo "############ C. GEYSER CONFIG (remote target + floodgate key path) ############"
GC=/home/viaproxy/plugins/Geyser/config.yml
if sudo test -f "$GC"; then
  echo "--- $GC ---"
  sudo grep -nE '^\s*(address|port|auth-type|floodgate-key-file|clone-remote-port|remote):' "$GC" | grep -v '^\s*#'
  echo ""
  echo "--- full 'remote:' + 'bedrock:' blocks ---"
  sudo sed -n '/^remote:/,/^[^ #]/p; /^bedrock:/,/^[^ #]/p' "$GC" | head -40
else
  echo "  !! $GC missing — Geyser may not have finished generating it. Check logs in A."
fi

echo ""
echo "############ D. FLOODGATE KEY — server side ############"
SK=/home/minecraft/data/config/floodgate/key.pem
if sudo test -f "$SK"; then
  echo "--- server key exists: $SK ---"
  sudo sha256sum "$SK"
  sudo head -1 "$SK"
else
  echo "  !! server Floodgate key missing at $SK"
fi

echo ""
echo "############ E. FLOODGATE KEY — Geyser/ViaProxy side ############"
echo "--- searching /home/viaproxy for any key.pem ---"
sudo find /home/viaproxy -name 'key.pem' -o -name 'public-key.pem' 2>/dev/null | while read -r f; do
  echo "  found: $f"
  sudo sha256sum "$f"
done
echo ""
echo "--- Geyser plugin dir listing (look for floodgate key / folder) ---"
sudo ls -la /home/viaproxy/plugins/Geyser/ 2>/dev/null || echo "  (no Geyser plugin dir)"
sudo ls -la /home/viaproxy/plugins/Geyser/floodgate/ 2>/dev/null || echo "  (no floodgate subfolder)"

echo ""
echo "############ F. IS THE MINECRAFT BACKEND REACHABLE FROM VIAPROXY? ############"
echo "--- viaproxy container can resolve + reach minecraft:25565? ---"
sudo docker exec viaproxy sh -c 'wget -qO- --timeout=5 http://minecraft:25565 2>&1 | head -c 200; echo; echo "exit=$?"' 2>&1 || echo "  (wget not available in container — that's fine, see logs in A/B)"

echo ""
echo "############ G. MINECRAFT SERVER — recent Floodgate/auth lines ############"
sudo docker logs minecraft --tail 60 2>&1 | grep -iE 'floodgate|bedrock|geyser|disconnect|whitelist|auth|login|\.Gimy|cookie' | tail -25 || echo "  (no matching lines)"

echo ""
echo "############ H. CONTAINER STATUS ############"
sudo docker ps --format "table {{.Names}}\t{{.Status}}" | grep -iE 'viaproxy|minecraft|NAMES'

echo ""
echo "############ DONE — paste ALL of it back, especially A and B ############"
