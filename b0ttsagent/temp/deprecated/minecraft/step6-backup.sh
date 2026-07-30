#!/usr/bin/env bash
# Step 6: Backup script, manual test, and daily cron
# Run each block one at a time.

# --- Part A: Write the backup script ---
sudo tee /home/minecraft-hc-solo/backup.sh << 'EOF'
#!/usr/bin/env bash
# Backup script for minecraft-hc-solo
# Hot backup (tar while server is running).
# Daily cron at 14:00 UTC (4 AM HST), 30-day retention.

set -euo pipefail

TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
DATA_DIR="/home/minecraft-hc-solo/data"
BACKUP_DIR="/home/minecraft-hc-solo/backups"
BACKUP_FILE="$BACKUP_DIR/minecraft-hc-${TIMESTAMP}.tar.gz"
LOG_FILE="$BACKUP_DIR/backup.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

log "Starting backup..."

if [ ! -d "$DATA_DIR" ]; then
    log "ERROR: data dir $DATA_DIR not found. Aborting."
    exit 1
fi

tar -czf "$BACKUP_FILE" -C /home/minecraft-hc-solo data 2>&1 | tee -a "$LOG_FILE"
log "Created: $BACKUP_FILE ($(du -h "$BACKUP_FILE" | cut -f1))"

# Prune backups older than 30 days
DELETED=$(find "$BACKUP_DIR" -name "minecraft-hc-*.tar.gz" -mtime +30 -delete -print)
if [ -n "$DELETED" ]; then
    log "Pruned: $DELETED"
else
    log "No old backups to prune."
fi

log "Backup complete."
EOF

# --- Part B: Make executable and test ---
sudo chmod +x /home/minecraft-hc-solo/backup.sh
sudo bash /home/minecraft-hc-solo/backup.sh

# --- Part C: After confirming the test works, add the daily cron ---
# sudo tee /etc/cron.d/minecraft-hc-solo-backup << 'CRON_EOF'
# 0 14 * * * root /bin/bash /home/minecraft-hc-solo/backup.sh
# CRON_EOF
