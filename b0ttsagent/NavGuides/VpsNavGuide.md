---
name: VpsNavGuide
topics: [vps, docker, ssh, tailscale, caddy, deploy, server, infrastructure]
description: "Reference for deploying and managing services on the VPS"
---

# VPS Navigation Guide V1.1

## Access

```bash
ssh deploy@vmi3326176.tailf94009.ts.net
```

**Tailscale hostname:** `vmi3326176.tailf94009.ts.net` **Tailscale IP:** `100.122.184.37` **Public IP:** `94.72.120.120`

> Always use the Tailscale IP/hostname for service access. UFW only allows traffic on `tailscale0` — the public IP is locked down.

---

## Stack

| Component      | Version |
| -------------- | ------- |
| Docker         | 29.1.3  |
| Docker Compose | v5.1.4  |
| Tailscale      | 1.98.3  |
|                |         |

---

## Conventions

- Each app gets its own **system user** — no sudo, no login shell
- App data and compose files live at `/home/<appname>/`
- All containers use `restart: unless-stopped`
- `deploy` user manages Docker; apps run as their own unprivileged users via `user: "UID:GID"` in compose

### Add a new app

```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin <appname>
sudo mkdir -p /home/<appname>
sudo chown -R <appname>:<appname> /home/<appname>
id <appname>  # note UID:GID for compose file
```

### Expose an app over HTTPS (Tailscale Serve)

```bash
sudo tailscale serve --https=443 --bg http://localhost:<port>
tailscale serve status
```

> Only one app can sit on port 443. For multiple HTTPS apps, put Caddy in front.

### Current Tailscale Serve mappings

| Endpoint | Proxies | App |
|---|---|---|
| `https://vmi3326176.tailf94009.ts.net` (`:443`) | `localhost:8080` | vaultwarden |
| `https://vmi3326176.tailf94009.ts.net:3000` | `localhost:8083` | ntfy |
| `https://vmi3326176.tailf94009.ts.net:3001` | `localhost:5984` | couchdb (Obsidian LiveSync) |
| `https://vmi3326176.tailf94009.ts.net:8443` | `localhost:8001` | *(unidentified — no container on 8001 in `docker ps`; possibly stale)* |

> Verify with `tailscale serve status`. The `:8443 → localhost:8001` entry has no matching container — candidate for removal or identification.

---

## Deployed apps

| App | Path | System user (uid:gid) | Host port(s) | Exposed via | Nav guide |
|---|---|---|---|---|---|
| couchdb | `/home/couchdb` | `couchdb` (982:977) | `127.0.0.1:5984` | Tailscale Serve `:3001` | `ObsidianLiveSyncNavGuide.md` |
| vaultwarden | *(unconfirmed)* | *(unconfirmed)* | `127.0.0.1:8080`, `127.0.0.1:3012` | Tailscale Serve `:443` | *(none)* |
| ntfy | *(unconfirmed)* | *(unconfirmed)* | `127.0.0.1:8083` | Tailscale Serve `:3000` | *(none)* |
| postgrest | `/home/postgrest` | `postgrest` (986:981) | *(none — internal)* | Cloudflare Tunnel `b0tts.dev/api` | `PostgrestApiGuide.md` |
| lobehub | `/home/lobehub` | `lobehub` (984:979) | *(none — internal)* | Cloudflare Tunnel `chat.b0tts.me` | `VpsLobeHubNavGuide.md` |
| minecraft | `/home/minecraft` | `minecraft` (987:982) | `0.0.0.0:25565` (RCON internal) | direct (tailnet) | `MinecraftNavGuide.md` |
| minecraft-hc-solo | `/home/minecraft-hc-solo` | `minecraft-hc-solo` (981:976) | `0.0.0.0:25566`, RCON `0.0.0.0:25575` | direct (tailnet) | `MinecraftHcSoloNavGuide.md` |
| prism | `/home/prism` | `prism` (993:985) | `0.0.0.0:1935` (RTMP) | direct (tailnet) | `PrismNavGuide.md` |
| searxng (standalone) | *(unconfirmed)* | *(unconfirmed)* | `0.0.0.0:8082->8080` | direct (`0.0.0.0`; not in ACL) | *(none — distinct from `lobe-searxng`)* |
| docs-mcp | *(unconfirmed)* | *(unconfirmed)* | `0.0.0.0:6280`, `0.0.0.0:6281` | direct (`0.0.0.0`; not in ACL) | *(none)* |
| pgweb | `/home/pgweb` | `pgweb` (985:980) | *(none — unmapped)* | *(decommissioned-planned; Supabase to replace)* | `PgwebNavGuide.md` |

> Ports confirmed from `sudo docker ps --format "table {{.Names}}\t{{.Ports}}"` and `tailscale serve status` (2026-07-17, refreshed 2026-08-16). Cells marked *(unconfirmed)* have no nav guide; fill in when those apps get documented. `minecraft` (personal hardcore world, port 25565) and `minecraft-hc-solo` (stream hardcore world, port 25566 — migrated from the InterServer VPS 2026-08-16) run as two separate servers; see `MinecraftNavGuide.md` and `MinecraftHcSoloNavGuide.md`. `searxng` and `docs-mcp` bind `0.0.0.0`; their ports (`8082`, `6280`, `6281`) are now in the ACL allow-list (policy as of 2026-08-16).

---

## Docker Quick Reference

```bash
# Conflict Check / always before assigning ports in a compose file, check for conflicts
sudo docker ps --format "table {{.Names}}\t{{.Ports}}"  

# Start
cd /home/<appname> && sudo docker compose up -d

# Stop
cd /home/<appname> && sudo docker compose down

# Restart / pick up compose changes
cd /home/<appname> && sudo docker compose up -d --force-recreate

# Logs
sudo docker logs <container>
sudo docker logs <container> --tail 30
sudo docker logs <container> -f

# Update image
cd /home/<appname> && sudo docker compose pull && sudo docker compose up -d

# List running containers
sudo docker ps
```

---

## Tailscale ACL

Grants as of 2026-08-16 (tag-based — applies to all `tag:vps` machines):

| Source | Destination | Ports |
|---|---|---|
| `tag:workstation` | `tag:vps` | `tcp: 22, 443, 1935, 3000, 3001, 6280, 6281, 6432, 8001, 8080, 8082, 8443, 25565, 25566` |
| `tag:vps` | `tag:workstation` | `tcp: 11434, 6432` |
| `autogroup:shared` | `tag:vps` | `tcp: 25565` |
| `autogroup:member` | `*` | `*` (catch-all — members reach everything) |

> The catch-all grant means the port lists matter mainly for shared (non-member) users; RCON (`25575`) is reachable by members via the catch-all.

If you add a new service and can't reach it, check the ACL at [login.tailscale.com/admin/acls](https://login.tailscale.com/admin/acls).

---

## Troubleshooting

|Symptom|Check|
|---|---|
|Can't reach a service|Use Tailscale IP, not public IP|
|Container keeps restarting|`sudo docker logs <container> --tail 20`|
|Service down after reboot|`sudo docker ps` — `systemctl is-enabled docker` should be `enabled`|