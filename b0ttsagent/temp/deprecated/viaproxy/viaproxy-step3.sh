#!/bin/bash
# Step 3: Add viaproxy service to docker-compose.yml
# The 19132/udp line was already removed from minecraft service.

cat << 'EOF' | sudo tee -a /home/minecraft/docker-compose.yml > /dev/null

  viaproxy:
    image: ghcr.io/viaversion/viaproxy:latest
    container_name: viaproxy
    restart: unless-stopped
    ports:
      - "19132:19132/udp"
    volumes:
      - /home/viaproxy:/app/run
    depends_on:
      - minecraft
EOF

echo "--- Verify the file ---"
cat /home/minecraft/docker-compose.yml
