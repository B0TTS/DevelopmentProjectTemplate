# Dual-PC Streaming Without Capture Card — SRT Plan

## Summary

The user wants to stream games from a **gaming PC** to a **laptop**, then restream to Twitch/TikTok while recording locally — all without a capture card. After researching NDI, Moonlight/Sunshine, and SRT, the recommended approach is **OBS-to-OBS via SRT** because both PCs are on Wi-Fi and SRT uses far less bandwidth than uncompressed NDI.

### Hardware mapping
- **Gaming PC**: Windows, i7-11700F, 32 GB DDR4, RTX 3060  
  Role: capture game, encode once with NVENC, send SRT feed to laptop.
- **Laptop**: Windows 11, Intel Core Ultra 9, 32 GB RAM, RTX 4050  
  Role: receive SRT feed, add webcam/mic/overlays, record locally, multistream to Twitch/TikTok.

### Approach chosen
- **Primary**: OBS Studio → OBS Studio over **SRT** (Secure Reliable Transport).
- **Why not NDI**: NDI is nearly uncompressed and performs poorly over Wi-Fi.
- **Why not Moonlight**: better for interactive game streaming; adds an extra window-capture step for OBS use.

## Current state

A step-by-step plan has been drafted but **not yet executed**. The next session should confirm four open decisions, then walk through the plan one step at a time.

### Open decisions
1. **TikTok delivery method**: Does the user have a TikTok stream key/RTMP URL, or will they use TikTok LIVE Studio / Streamlabs for TikTok?
2. **Overlay location**: Should overlays/alerts be added on the laptop, or should the gaming PC send a fully composed scene?
3. **Network**: Can either PC be wired to Ethernet, or are both staying on Wi-Fi?
4. **Scope**: Keep the first test to Twitch + TikTok only, or include YouTube/Discord multistream setup now?

### Recommended bitrates / settings
- Intermediate SRT feed from gaming PC: **1080p60, 10–15 Mbps, NVENC H.264**.
- Latency parameter: `latency=20000` (20 ms) for local network.
- Gaming PC output URL: `srt://<LAPTOP_IP>:10000?mode=caller&latency=20000`
- Laptop media source URL: `srt://0.0.0.0:10000?mode=listener&latency=20000`
- Laptop recording: use NVENC or Intel Quick Sync (Core Ultra 9 has Arc/Quick Sync).

## Plan to execute

1. Update OBS Studio to v30+ on both PCs.
2. Install **obs-multi-rtmp** plugin on the laptop.
3. On gaming PC OBS: create a clean Game Capture scene (game + desktop audio only).
4. On gaming PC OBS: set Stream service to Custom, server to `srt://<LAPTOP_IP>:10000?mode=caller&latency=20000`, encoder NVENC H.264, 10–15 Mbps.
5. On laptop: add an SRT Media Source with `srt://0.0.0.0:10000?mode=listener&latency=20000`.
6. On laptop: add webcam and microphone sources to the scene.
7. On laptop: configure recording (path, encoder, format).
8. On laptop: configure obs-multi-rtmp targets for Twitch and TikTok.
9. Offline test: start gaming PC output, verify feed appears on laptop.
10. First live test: stream to Twitch only, check stats, then add TikTok.
11. Optimize: adjust bitrates, audio sync, Wi-Fi placement, or switch to wired if issues appear.

## Useful skills for next session

- `tutorial` — continue the step-by-step execution of this plan.
- `docs-mcp` — look up exact OBS SRT or obs-multi-rtmp docs/settings if needed.
- `create-nav-guide` — turn the final working setup into a reusable reference doc.

## Notes

- Both PCs on Wi-Fi is workable with SRT but not ideal. If stutters occur, wire at least one PC and use 5 GHz/6 GHz Wi-Fi with both devices close to the router.
- The user is experienced with OBS and has used Streamlabs for Twitch/YouTube/TikTok multistreaming; they may prefer to stay in OBS or fall back to Streamlabs if plugin setup is troublesome.
- Replace `<LAPTOP_IP>` with the laptop’s actual local IP address (e.g., `192.168.1.123`).
