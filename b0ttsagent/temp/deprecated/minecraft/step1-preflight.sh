#!/usr/bin/env bash
# Step 1: Pre-flight inspection (read-only)
# Paste these on the VPS one block at a time.

echo "=== 1. Docker containers ==="
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "=== 2. Memory headroom ==="
free -m

echo ""
echo "=== 3. UFW status ==="
sudo ufw status verbose
