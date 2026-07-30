#!/bin/bash
# ============================================================
# Bedrock-connect diagnostics — run on the InterServer VPS
# (ssh deploy@interdeploymcvps.tailf94009.ts.net)
# Read-only. No changes made. Paste ALL output back.
# ============================================================

echo "############ A. CONTAINERS ############"
sudo docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -iE 'minecraft|viaproxy|NAMES'

echo ""
echo "############ B. HOST UDP 19132 LISTENER ############"
echo "--- ss (who actually holds 19132/udp) ---"
sudo ss -lunp | grep 19132 || echo "  !! NOTHING listening on 19132/udp on the host"
echo "--- netstat fallback ---"
sudo netstat -lunp 2>/dev/null | grep 19132 || echo "  (netstat: nothing / not installed)"

echo ""
echo "############ C. CURRENT docker-compose.yml ############"
cat /home/minecraft/docker-compose.yml

echo ""
echo "############ D. MINECRAFT CONTAINER LOGS (tail) ############"
sudo docker logs minecraft --tail 25 2>&1 || echo "  (minecraft container not found / not running)"

echo ""
echo "############ E. VIAPROXY CONTAINER LOGS (tail) ############"
sudo docker logs viaproxy --tail 40 2>&1 || echo "  (viaproxy container not found / not running)"

echo ""
echo "############ F. VIAPROXY DATA DIR (/home/viaproxy) ############"
echo "--- tree of /home/viaproxy (2 levels) ---"
sudo find /home/viaproxy -maxdepth 2 -type f 2>/dev/null | sort || echo "  (dir missing)"
echo ""
echo "--- plugins folder (is Geyser jar here?) ---"
sudo ls -lh /home/viaproxy/plugins/ 2>/dev/null || echo "  !! /home/viaproxy/plugins/ does NOT exist -> Geyser plugin NOT installed in ViaProxy"
echo ""
echo "--- viaproxy.yml (bind + target server) ---"
sudo cat /home/viaproxy/viaproxy.yml 2>/dev/null || sudo cat /home/viaproxy/config/viaproxy.yml 2>/dev/null || echo "  (no viaproxy.yml found)"

echo ""
echo "############ G. MINECRAFT MODS (is Geyser-Fabric / Floodgate still there?) ############"
sudo ls -lh /home/minecraft/data/mods/ 2>/dev/null | grep -iE 'geyser|floodgate|NAME' || echo "  (no geyser/floodgate mods in minecraft container)"

echo ""
echo "############ H. GEYSER CONFIG (if still on minecraft container) ############"
sudo cat /home/minecraft/data/config/Geyser-Fabric/config.yml 2>/dev/null | grep -iE 'auth-type|port:|address:|clone-remote' | grep -v '^[[:space:]]*#' || echo "  (no Geyser-Fabric config found)"

echo ""
echo "############ I. UFW (confirm tailscale0 open) ############"
sudo ufw status verbose | head -20

echo ""
echo "############ J. FREE MEMORY ############"
free -m

echo ""
echo "############ DONE — paste everything back ############"
