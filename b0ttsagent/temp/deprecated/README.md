# Deprecated Files

Archived temp files from previous work. Organized by category for easy reference.

> These files are kept for reference only. Nothing here is actively in use.

---

## 📁 backups

Backup and maintenance scripts for the server.

| File | Description |
|------|-------------|
| `backup-setup.sh` | Script for setting up automated backups |
| `mc-backup.sh` | Minecraft world backup script |
| `backup.sh` | Hardcore solo server backup script (daily tar.gz + 30-day prune) |

---

## 📁 bedrock

Diagnostic and fix scripts for Minecraft Bedrock Edition connectivity.

| File | Description |
|------|-------------|
| `bedrock-connect-diag.sh` | Diagnose Bedrock connection issues |
| `bedrock-server-not-found-diag.sh` | Troubleshoot "server not found" errors |
| `bedrock-viaproxy-fix.sh` | Fix Bedrock compatibility via ViaProxy |

---

## 📁 minecraft

Minecraft Java Edition server config and step-by-step setup artifacts.

| File | Description |
|------|-------------|
| `minecraft-docker-compose.yml` | Docker Compose config for the MC server |
| `minecraft-bedrock-whitelist.txt` | Bedrock cross-play whitelist config |
| `minecraft-step5-compose.txt` | Setup step 5 — compose configuration |
| `minecraft-step6-mods.txt` | Setup step 6 — mod installation |
| `minecraft-step7-fix.txt` | Setup step 7 — fixes/troubleshooting |
| `minecraft-step7-start.txt` | Setup step 7 — server startup |
| `minecraft-step8-geyser.txt` | Setup step 8 — Geyser (Bedrock bridge) config |
| `minecraft-step10-whitelist.txt` | Setup step 10 — whitelist config |
| `minecraft-step10b-whitelist.txt` | Setup step 10b — whitelist variant |
| `minecraft-step10c-fwhitelist.txt` | Setup step 10c — forced whitelist variant |
| `docker-compose.yml` | Hardcore solo server compose (Fabric 1.21.11, 2G, seed 5277846394751328433) |
| `step1-preflight.sh` | Hardcore solo step 1 — pre-flight inspection |
| `step2-create-user.sh` | Hardcore solo step 2 — create system user |
| `step6-backup.sh` | Hardcore solo step 6 — backup script + cron setup |

---

## 📁 schedules

Room/airing schedule notes and guides.

| File | Description |
|------|-------------|
| `room-airing-schedule.md` | Room airing schedule |
| `Schedule Guide-20260713013836.md` | Schedule guide draft (timestamped) |
| `Notes` | Freeform notes related to scheduling |

---

## 📁 utilities

Miscellaneous utility scripts.

| File | Description |
|------|-------------|
| `navguide-groundtruth.sh` | Script for validating/ground-truthing nav guides |

---

## 📁 viaproxy

ViaProxy setup and configuration scripts.

| File | Description |
|------|-------------|
| `viaproxy-step1-inspection.sh` | Step 1 — inspect ViaProxy setup |
| `viaproxy-step3.sh` | Step 3 — ViaProxy configuration |
| `viaproxy-step10.sh` | Step 10 — final ViaProxy verification |
