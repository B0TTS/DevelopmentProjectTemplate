---
name: PrismNavGuide
topics: [prism, restream, multistream, rtmp, streaming, obs]
description: "Reference for Prism multistream relay container — compose setup, key management, and OBS configuration"
---

# Prism Navigation Guide V1.1

## Overview

| Property       | Value                            |
| -------------- | -------------------------------- |
| App            | Prism (multistream relay)        |
| Source         | `github.com/MorrowShore/Prism`   |
| Container name | `prism`                          |
| System user    | `prism` (uid 993, gid 985)       |
| Compose file   | `/home/prism/docker-compose.yml` |
| Port           | `1935` (RTMP)                    |
| Image          | `prism` (local build)            |

---

## Compose file

```yaml
services:
  prism:
    image: prism
    container_name: prism
    ports:
      - "1935:1935"
    environment:
      - YOUTUBE_KEY=<yt-stream-key>
      - TWITCH_URL=rtmp://live.twitch.tv/app/
      - TWITCH_KEY=<twitch-stream-key>
      - KICK_KEY=<kick-stream-key>
    restart: unless-stopped
```

Other supported env vars: `FACEBOOK_KEY`, `KICK_KEY`, `TROVO_KEY`, `CLOUDFLARE_KEY`, `INSTAGRAM_KEY`, `RTMP1_URL` + `RTMP1_KEY` (and RTMP2, RTMP3 for custom destinations).

---

## OBS Settings

|Field|Value|
|---|---|
|Service|Custom|
|Server|`rtmp://100.122.184.37/<generated-path>`|
|Stream Key|anything (ignored)|

---

## Switching Profiles (gaming ↔ dev)

```bash
# 1. Edit keys
sudo nano /home/prism/docker-compose.yml

# 2. Restart
cd /home/prism && sudo docker compose up -d --force-recreate

# 3. Get new OBS destination
sudo docker logs prism
```

Look for: `Your Stream Destination: rtmp://94.72.120.120/XXXXXXXXXX` Use the Tailscale IP in OBS instead: `rtmp://100.122.184.37/XXXXXXXXXX`

---

## Rebuilding the image

```bash
sudo docker build -t prism github.com/MorrowShore/Prism
cd /home/prism && sudo docker compose up -d --force-recreate
```

---

## Gotchas

> The RTMP destination URL regenerates randomly on every container restart — always check logs and update OBS after any restart.

> Prism must run as root inside the container — omit `user: "UID:GID"` from the compose file or nginx will fail with permission errors on startup.

> `TWITCH_URL` and `TWITCH_KEY` are separate env vars — pasting the key into the URL field causes nginx to concatenate them into an invalid hostname and crash-loop.

> OBS uses the Tailscale IP (`100.122.184.37`), not the public IP — UFW only allows traffic on `tailscale0`.

> Do NOT set `KICK_URL` in the compose file — Prism hardcodes it to `rtmp://127.0.0.1:19353/kick/` in the Dockerfile. Only `KICK_KEY` is required.
