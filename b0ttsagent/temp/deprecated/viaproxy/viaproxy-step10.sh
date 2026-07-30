#!/bin/bash
# Step 10: Harden - add memory limit to viaproxy service

# Insert mem_limit after the last line of the viaproxy block ("      - minecraft")
sudo sed -i '/^      - minecraft$/a\    mem_limit: 1g' /home/minecraft/docker-compose.yml

# Verify the change
echo "--- Updated compose file (check viaproxy section) ---"
grep -A 12 "viaproxy:" /home/minecraft/docker-compose.yml

echo ""
echo "--- Recreate viaproxy with memory limit ---"
sudo docker compose -f /home/minecraft/docker-compose.yml up -d viaproxy

echo ""
echo "--- Confirm limit applied ---"
sudo docker inspect viaproxy --format 'Memory Limit: {{.HostConfig.Memory}} bytes ({{div .HostConfig.Memory 1048576}}M)'
