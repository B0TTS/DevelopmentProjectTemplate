---
name: YtmdesktopAdBlocker
topics:
  - ytmdesktop
  - ad blocker
  - youtube music
  - electron
  - integration
description: >
  Custom ad-blocker integration in the local ytmdesktop source tree. Blocks
  ads via network filtering, CSS hiding, and JS auto-skip (speed boost +
  mute + seek). Default-enabled. Built as a standalone Windows installer.
---

## Overview

| Property | Value |
|----------|-------|
| **Project** | [ytmdesktop/ytmdesktop](https://github.com/ytmdesktop/ytmdesktop) v2.0.11 |
| **Local path** | `C:\Users\Jonah\ytmdesktop` |
| **Tech stack** | Electron 40, Vite, Vue 3, TypeScript, yarn 4.5 |
| **Integration class** | `src/main/integrations/ad-blocker/AdBlocker` |
| **Store key** | `integrations.adBlockerEnabled` (boolean, default `true`) |
| **Settings UI** | Integrations tab → "Ad blocker" checkbox |
| **Installer output** | `out\make\squirrel.windows\x64\youtube-music-desktop-app-2.0.11 Setup.exe` |

## Run / dev

```bash
cd C:\Users\Jonah\ytmdesktop
yarn start
```

## Build installer

```bash
cd C:\Users\Jonah\ytmdesktop
$env:YTMD_DISABLE_UPDATES="true"; yarn make
```

Setting `YTMD_DISABLE_UPDATES` prevents the packaged app from auto-updating from the official GitHub releases (which would overwrite the ad blocker). The codebase already checks for this env var — no code changes needed.

Installer lands at `out\make\squirrel.windows\x64\`. Uninstall any existing ytmdesktop app first, then run the new installer. Config files in `%APPDATA%` persist and are compatible.

## Architecture

Built as an `IIntegration` following the same pattern as `VolumeRatio` and `CustomCSS`.

### Files created

```
src/main/integrations/ad-blocker/
├── index.ts                          # AdBlocker class (IIntegration)
└── script/
    ├── enable.script.js              # JS injected into YTM page
    ├── enable.script.d.ts            # raw import type decl
    ├── disable.script.js             # cleanup JS
    └── disable.script.d.ts           # raw import type decl
```

### Files modified

| File | Change |
|------|--------|
| `src/shared/store/schema.ts` | Added `adBlockerEnabled: boolean` to `integrations` |
| `src/main/index.ts` | Import, instantiate, `setPartition`/`provide` in `createYTMView`, store change handler, startup enable, script registration, `ytmView:loaded` re-enable |
| `src/renderer/windows/settings/Settings.vue` | Checkbox in Integrations tab, v-model + store read/write |

### Integration points in main/index.ts

| Location | What it does |
|----------|-------------|
| `createYTMView()` | `adBlocker.setPartition(...)` — registers network listener BEFORE `loadURL` |
| `createYTMView()` | `adBlocker.provide(store, ytmView)` — hands the BrowserView reference |
| `store.onDidAnyChange` | Toggle handler — calls `enable()`/`disable()` on change |
| `ytmView:loaded` handler | Re-enables JS/CSS after YTM page loads (handles view recreation) |
| Script registration | `ytmViewIntegrationScripts["adBlocker"]` populated from `getYTMScripts()` |
| Startup enable | Enables on app launch if toggled on |

## Three-layer blocking

### 1. Network (session.webRequest)

Registered on `session.fromPartition("persist:ytmview")` before `loadURL()`. The callback checks `this.isEnabled` so the Settings toggle controls blocking. Listener is idempotent via a `networkBlockingSetup` flag — registered once per app session, persists across BrowserView recreations.

**Blocked domains** (in `BLOCKED_URL_PATTERNS`):

```
*.doubleclick.net, ad.doubleclick.net, *.googleadservices.com,
*.googlesyndication.com, ade.googlesyndication.com,
googleads.g.doubleclick.net, adservice.google.com,
*.googletagmanager.com, *.googletagservices.com,
pagead2.googlesyndication.com, *.google-analytics.com
```

> `googlevideo.com` and `manifest.googlevideo.com` are **never blocked** — they serve legitimate music streams.

> YouTube API endpoints (`youtube.com/api/stats`, `ptracking`, `pagead`, `log_event`, `jnn-pa.googleapis.com`) were originally included but removed — they risk breaking recommendations and playback history.

### 2. CSS (insertCSS)

Injected via `webContents.insertCSS()`. Hides:
- Premium/trial promo banners
- Ad-badge carousel shelves
- "Are you still there" inactivity dialogs
- Video ad overlays (`.ytp-ad-*`)
- Premium upsell nav items and links

Re-injected automatically on YTM view recreation (`provide()` checks `ytmViewChanged`).

### 3. JavaScript (webFrame.executeJavaScript)

Injected via `ytmView:executeScript` IPC, runs in the page's main world. Scripts are **function expressions** (not IIFEs) because the preload calls them as functions.

**Strategy (on ad start):**

| Order | Action | Timing |
|-------|--------|--------|
| 1 | **Mute** player (`playerApi.mute()`) | Immediately |
| 2 | **Speed boost** video to 16x | Immediately |
| 3 | **Skip button** — try `.ytp-ad-skip-button-*` selectors + text-match buttons | Continuously |
| 4 | **Seek past** — if still ad after 2s and `getDuration() < 45s`, call `playerApi.seekTo(dur - 0.5)` | Delayed 2s |

**On ad end:** restore previous mute state and playback rate.

`playerApi.nextVideo()` is deliberately **not used** — it skips whatever is playing (ad or song) and caused false positives.

## Bugs encountered and fixed

> **Import/instantiation silently dropped.** The first batch `edit` to `main/index.ts` reported success but didn't actually insert the `import AdBlocker` and `new AdBlocker()` lines. Added manually in subsequent edits.

> **Ad blocker never enabled on existing configs.** `store.get("integrations").adBlockerEnabled` returned `undefined` (falsy) for pre-existing config files. Conf `defaults` only apply to new configs. Fixed with `?? true` fallback in all runtime checks and Settings UI initialization.

> **Network blocking registered too late.** `setupNetworkBlocking()` was called from `enable()` which runs AFTER `loadURL()`. Moved to `setPartition()` (called in `createYTMView` before `loadURL`) with eager registration and `isEnabled` check in the callback.

> **Script crashed: `(intermediate value) is not a function`.** Scripts were self-executing IIFEs `(function(){...})()`, but the preload does `(await webFrame.executeJavaScript(script))()` — calling the returned value as a function. The IIFE returned `undefined`, causing the crash. Fixed by removing the trailing `()` from both scripts — they're now function expressions the preload invokes.

> **`nextVideo()` skipped songs.** `playerApi.nextVideo()` skips whatever track is playing. If `adPlaying` detection lags slightly, it nukes the actual song. Replaced with safe approach: speed boost + timed seek with `getDuration() < 45s` guard.

> **Garbled audio during speed boost.** Ads played at 16x created unpleasant noise. Added `playerApi.mute()` on ad start, `unMute()` on ad end, respecting the user's previous mute state.

> **Interactive/click-to-play ads pause themselves.** Some ads deliberately pause the video (requiring user interaction). Speed boost and seek are ineffective on a paused video. Added `tryUnpauseVideo()` which calls `video.play()` on ad start and on every tick while an ad is playing — immediately overrides the self-pause so the rest of the skip pipeline (speed boost → skip button → seek) works normally.
