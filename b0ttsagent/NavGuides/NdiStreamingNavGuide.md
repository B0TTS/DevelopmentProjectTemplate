---
name: NdiStreamingGuide
topics: [NDI, OBS, Twitch, dual-PC, streaming, Screen Capture HX, DistroAV]
description: Dual-PC NDI streaming setup — gaming PC (RTX 3060) sends screen over Wi-Fi via NDI Screen Capture HX to laptop (RTX 4050) which streams to Twitch via OBS with DistroAV plugin.
---

## Overview

| Property | Value |
| --- | --- |
| Gaming PC | i7-11700F, RTX 3060, 32GB DDR4 |
| Streaming laptop | Ultra 9 Intel, RTX 4050, 32GB DDR5 |
| Network | Wi-Fi (gigabit, 4 bars, unstable) |
| Internet speeds | ~150 Mbps down, ~10 Mbps up |
| NDI mode | Screen Capture HX (GPU-accelerated, HEVC) |
| NDI resolution / framerate | 1080p60 |
| NDI bandwidth preset | Low |
| OBS encoder (laptop) | NVENC H.264 |
| Fallback plan | Powerline adapters if Wi-Fi can't sustain |

## NDI Tools (both PCs)

Installed on both machines from `ndi.video/tools`. Provides NDI Runtime, Screen Capture HX, Access Manager, Studio Monitor.

> Reboot both PCs after installing NDI Tools. NDI Runtime won't register until after restart.

## Gaming PC — NDI Screen Capture HX

Sends desktop over local network to laptop. Sits in the system tray. Right-click tray icon for settings.

| Setting | Value |
| --- | --- |
| Codec | HEVC |
| Resolution | 1080p (native) |
| Framerate | 60 |
| Bandwidth | Low |
| Stream name | GamingPC |

> NDI Screen Capture HX uses GPU (NVENC) to compress. Regular Screen Capture uses CPU. Both PCs have NVIDIA GPUs — HX is the right choice.

## Laptop — OBS Studio + DistroAV

### DistroAV plugin

Installed from `github.com/DistroAV/DistroAV/releases`. Required for the NDI Source option to appear in OBS.

> OBS does not include NDI Source by default. DistroAV must be installed on any OBS instance that receives NDI, even if you're not sending from OBS.

### NDI Source settings

| Setting | Value |
| --- | --- |
| Source Name | GamingPC (auto-detected) |
| Bandwidth | Low |
| Sync | Network |
| Audio | Disabled (audio comes via dedicated NDI streams — see Multi-Track Audio Routing below) |
| Framesync | Off |
| Hardware acceleration | On |
| YUV Range | Limited |
| Color Space | Rec. 709 |
| Fix alpha blending | Off |

### Twitch encoder

| Setting | Value |
| --- | --- |
| Encoder | NVIDIA NVENC H.264 |
| Rate control | CBR |
| Bitrate | 6000 Kbps |

## Multi-Track Audio Routing (4 sources)

Separates mic, game, music, and VC into independent NDI audio streams so the laptop can record them as distinct tracks and mix them independently for Twitch.

### Architecture

Screen Capture HX sends video only (audio source set to None). OBS on the gaming PC sends 4 audio-only NDI streams via DistroAV Dedicated Output filters. Laptop OBS receives them as separate NDI sources.

> DistroAV cannot output NDI HX (HEVC) video — it requires an NDI license not available to the plugin. Full-bandwidth NDI video (~150 Mbps) would choke the Wi-Fi. Audio-only NDI streams are tiny (a few hundred Kbps each), so full NDI is fine for audio while Screen Capture HX handles video.

### Gaming PC — OBS audio sources + NDI Dedicated Output

OBS on the gaming PC does NOT record or stream. It only captures audio and sends it over NDI. DistroAV Main Output is OFF (Screen Capture HX handles video).

| Source | NDI Dedicated Output name | Notes |
| --- | --- | --- |
| Mic | Mic | Audio Input Capture (physical mic) |
| Game | Game | Separated via existing OBS source |
| Music | Music | Separated via existing OBS source |
| VC | VC | Separated via existing OBS source |

> NDI Dedicated Output filter: right-click source → Filters → + → NDI Dedicated Output → name it.

### Laptop — NDI audio sources + multi-track recording

4 NDI sources added, one per dedicated output. Video source (GamingPC) has audio disabled.

| Setting | Value |
| --- | --- |
| Source Name | GamingPC - Mic / Game / Music / VC |
| Sync | Source Timing |
| Latency | Low |
| Hardware acceleration | Off (audio-only, no video to decode) |

Recording configured for 6 tracks (Advanced output mode). Each audio source assigned to its own track via Edit → Advanced Audio Properties:

| Track | Source |
| --- | --- |
| 1 | Stream mix (all sources) |
| 2 | Mic |
| 3 | Game |
| 4 | Music |
| 5 | VC |
| 6 | (reserved) |

> The DistroAV NDI Dedicated Output filter does not work on scene/group sources — only on individual audio sources (OBS limitation).

> Enable Low Latency Audio Buffering Mode (Settings → Audio) on laptop OBS to prevent NDI audio buffer drift causing A/V sync issues over time.

> If A/V drift appears, add a sync offset (~-50ms) to the NDI audio sources on the laptop to compensate for NDI network latency.

## Gotchas

> NDI is LAN-only traffic — internet upload/download speeds don't affect the NDI link between the two PCs. Only local Wi-Fi throughput matters.

> If the feed stutters while gaming: first try dropping to 720p60 or 1080p30 in NDI Screen Capture HX settings on the gaming PC, or enable Framesync in the OBS NDI Source. If still unstable, fall back to powerline adapters.

> OBS Stats window (`View → Stats`) shows dropped frames per source. Use it to diagnose whether stutter is from the NDI link (NDI source drops) vs internet (network drops) vs rendering (render lag).
