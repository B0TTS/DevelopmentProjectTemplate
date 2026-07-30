#!/usr/bin/env bash
# Step 2: Create system user and directories for minecraft-hc-solo
# Run these one at a time or all together on the VPS.

# Create system user (no home dir, no login shell)
sudo useradd --system --no-create-home --shell /usr/sbin/nologin minecraft-hc-solo

# Create directories
sudo mkdir -p /home/minecraft-hc-solo/{data,backups}

# Set ownership
sudo chown -R minecraft-hc-solo:minecraft-hc-solo /home/minecraft-hc-solo

# Verify and capture UID:GID
id minecraft-hc-solo
