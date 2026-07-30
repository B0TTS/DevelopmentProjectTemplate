#!/bin/bash
# ===================================================
# MyngaCraft Backup Script
# Runs daily via cron. Stops mc, tars data, restarts.
# Retention: 30 days. Logs to /home/minecraft/backup.log
# ===================================================

set -e

BACKUP_DIR="/home/minecraft/backups"
DATA_DIR="/home/minecraft/data"
LOG_FILE="/home/minecraft/backup.log"
COMPOSE_FILE="/home/minecraft/docker-compose.yml"
RETENTION_DAYS=30
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="$BACKUP_DIR/mc-backup-$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "[$(date)] Starting backup..." >> "$LOG_FILE"

# Gracefully stop the mc container
echo "[$(date)] Stopping minecraft container..." >> "$LOG_FILE"
docker compose -f "$COMPOSE_FILE" stop minecraft >> "$LOG_FILE" 2>&1

# Tar the data directory
echo "[$(date)] Creating backup: $BACKUP_FILE" >> "$LOG_FILE"
tar -czf "$BACKUP_FILE" -C "$(dirname "$DATA_DIR")" "$(basename "$DATA_DIR")" >> "$LOG_FILE" 2>&1
BACKUP_SIZE=$(du -h "$BACKUP_FILE" | cut -f1)

# Restart the mc container
echo "[$(date)] Starting minecraft container..." >> "$LOG_FILE"
docker compose -f "$COMPOSE_FILE" up -d minecraft >> "$LOG_FILE" 2>&1

# Clean up old backups
echo "[$(date)] Cleaning backups older than $RETENTION_DAYS days..." >> "$LOG_FILE"
find "$BACKUP_DIR" -name "mc-backup-*.tar.gz" -mtime +$RETENTION_DAYS -delete -print >> "$LOG_FILE" 2>&1
KEEP_COUNT=$(find "$BACKUP_DIR" -name "mc-backup-*.tar.gz" | wc -l)

echo "[$(date)] Backup complete. Size: $BACKUP_SIZE. Keeping $KEEP_COUNT backups." >> "$LOG_FILE"
