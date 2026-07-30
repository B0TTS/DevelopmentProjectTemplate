#!/bin/bash
# ============================================================
# Ground-truth sweep for the MinecraftNavGuide update.
# Read-only. No changes. Run on the InterServer VPS.
# (ssh deploy@interdeploymcvps.tailf94009.ts.net)
# ============================================================

echo "############ A. FINAL docker-compose.yml (raw, current state) ############"
sudo cat /home/minecraft/docker-compose.yml

echo ""
echo "############ A2. RENDERED compose (confirms entrypoint override took) ############"
sudo docker compose -f /home/minecraft/docker-compose.yml config 2>&1 | grep -A 15 -iE 'viaproxy:|entrypoint|mem_limit|ports:'

echo ""
echo "############ B. CONTAINERS — status / ports / health ############"
sudo docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -iE 'viaproxy|minecraft|NAMES'
echo "--- viaproxy inspect: entrypoint + memory + image ---"
sudo docker inspect viaproxy --format 'Image: {{.Config.Image}}\nEntrypoint: {{.Config.Entrypoint}}\nMemory(bytes): {{.HostConfig.Memory}}\nRestartPolicy: {{.HostConfig.RestartPolicy.Name}}' 2>&1
echo "--- minecraft inspect: memory + restart ---"
sudo docker inspect minecraft --format 'Memory(bytes): {{.HostConfig.Memory}}\nRestartPolicy: {{.HostConfig.RestartPolicy.Name}}' 2>&1

echo ""
echo "############ C. WHO HOLDS THE PORTS (host) ############"
echo "--- TCP 25565 ---"
sudo ss -ltnp | grep 25565 || echo "  !! nothing on 25565/tcp"
echo "--- UDP 19132 ---"
sudo ss -lunp | grep 19132 || echo "  !! nothing on 19132/udp"

echo ""
echo "############ D. VIAPROXY LOGS (confirm clean boot — no FATAL) ############"
sudo docker logs viaproxy --tail 40 2>&1

echo ""
echo "############ E. GEYSER-VIAPROXY config.yml (remote + bedrock + floodgate) ############"
GC=/home/viaproxy/plugins/Geyser/config.yml
if sudo test -f "$GC"; then
  echo "--- $GC exists ---"
  echo "--- key scalar settings ---"
  sudo grep -nE '^\s*(address|port|auth-type|floodgate-key-file|clone-remote-port|remote-address|remote-port):' "$GC" | grep -v '^\s*#'
  echo ""
  echo "--- full 'remote:' block ---"
  sudo awk '/^remote:/{f=1} f{print} /^[^ [:space:]]/ && !/^remote:/ && f{c++} c>1{exit}' "$GC" | head -25
  echo "--- full 'bedrock:' block ---"
  sudo awk '/^bedrock:/{f=1} f{print} /^[^ [:space:]]/ && !/^bedrock:/ && f{c++} c>1{exit}' "$GC" | head -25
else
  echo "  !! $GC missing"
fi

echo ""
echo "############ F. FLOODGATE KEYS — do server + Geyser match? ############"
echo "--- server-side key ---"
SK=/home/minecraft/data/config/floodgate/key.pem
if sudo test -f "$SK"; then
  echo "  path: $SK"
  sudo sha256sum "$SK"
  sudo stat -c '  owner: %U:%G  mode: %a' "$SK"
  sudo head -1 "$SK"
else
  echo "  !! server key missing at $SK"
fi
echo ""
echo "--- Geyser/ViaProxy-side keys (search /home/viaproxy) ---"
sudo find /home/viaproxy -name 'key.pem' -o -name 'public-key.pem' 2>/dev/null | while read -r f; do
  echo "  found: $f"
  sudo sha256sum "$f"
  sudo stat -c '  owner: %U:%G  mode: %a' "$f"
done
echo "  (if nothing found, Geyser-ViaProxy has no floodgate key — yet it works, so note how)"

echo ""
echo "############ G. FLOODGATE server config (prefix, key-file-name) ############"
FC=/home/minecraft/data/config/floodgate/config.yml
if sudo test -f "$FC"; then
  sudo grep -nE 'key-file-name|username-prefix|send-floodgate-data|config-version' "$FC" | grep -v '^\s*#'
else
  echo "  (no $FC — floodgate config elsewhere?)"
  sudo find /home/minecraft/data/config/floodgate -maxdepth 1 -type f 2>/dev/null
fi

echo ""
echo "############ H. server.properties (ground truth) ############"
SP=/home/minecraft/data/server.properties
if sudo test -f "$SP"; then
  sudo grep -iE '^(online-mode|white-list|enforce-whitelist|server-port|level-seed|max-players|view-distance|simulation-distance|motd|level-name|difficulty)' "$SP"
else
  echo "  !! $SP missing"
fi

echo ""
echo "############ I. UFW (full state — note PUBLIC game-port rules) ############"
sudo ufw status verbose

echo ""
echo "############ J. TAILSCALE — this box IP + serve/funnel + resolve 100.122.184.37 ############"
sudo tailscale status 2>&1 | head -3
echo "--- all tailnet nodes (look for 100.122.184.37 and 100.100.223.6) ---"
sudo tailscale status 2>&1 | grep -E '100\.122\.184\.37|100\.100\.223\.6' || echo "  (neither found in status)"
echo "--- tailscale serve ---"
sudo tailscale serve status 2>&1 || echo "  (serve: n/a)"
echo "--- tailscale funnel ---"
sudo tailscale funnel status 2>&1 || echo "  (funnel: n/a)"

echo ""
echo "############ K. OWNERSHIP of data dirs ############"
echo "--- /home/minecraft + data ---"
sudo ls -la /home/minecraft/ | head -15
echo "--- /home/minecraft/data (top) ---"
sudo ls -la /home/minecraft/data/ | head -15
echo "--- /home/viaproxy ---"
sudo ls -la /home/viaproxy/ | head -15
echo "--- /home/viaproxy/plugins ---"
sudo ls -la /home/viaproxy/plugins/

echo ""
echo "############ L. BACKUPS / CRON (current reality vs guide) ############"
echo "--- scripts in /home/minecraft ---"
sudo ls -la /home/minecraft/*.sh 2>/dev/null || echo "  (no .sh in /home/minecraft)"
echo "--- root crontab ---"
sudo crontab -l 2>/dev/null | grep -i minecraft || echo "  (nothing in root crontab for minecraft)"
echo "--- /etc/cron.d ---"
sudo ls -la /etc/cron.d/ 2>/dev/null | grep -i minecraft || echo "  (no minecraft file in /etc/cron.d)"
echo "--- backup dir ---"
sudo ls -la /home/minecraft/backups/ 2>/dev/null | tail -5 || echo "  (no backups dir)"

echo ""
echo "############ M. PUBLIC IP confirmation ############"
curl -s --max-time 5 https://ifconfig.me 2>/dev/null && echo " (curl ifconfig.me)" || echo "  (curl unavailable)"

echo ""
echo "############ DONE — paste everything back ############"
