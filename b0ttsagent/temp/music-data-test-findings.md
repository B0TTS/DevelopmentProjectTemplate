# Music Stream/Play/View Data — Hands-On Test Findings

**Date:** 2026-08-13 · **Machine:** Windows 11, PowerShell 5.1 · **yt-dlp:** 2026.07.04 on PATH · **curl.exe:** 8.21.0

**Test artist:** **2hollis** — modern rap/electronic producer (hyperpop-adjacent), YouTube channel 285k subs,
SoundCloud 165k followers, Spotify ~5.3M monthly listeners. Spotify artist id `72NhFAGG5Pt91VbheJeEPG`.
Real mid-tier subject with both YT and SC presences (NOT a megastar). Numbers below are all live-verified.

**Raw outputs** saved in `b0ttsagent\temp\f*.json/html` next to this file.

---

## FLOW 1 — yt-dlp single track search — ✅ WORKS

```powershell
yt-dlp -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:2hollis jeans"
```

Result (verified): `title="2hollis - jeans (official video)"`, `upload_date=20231027`,
`view_count=6206802`, `channel="2hollis"`, `channel_follower_count=285000`, `duration=181`.

All requested fields present and sensible. `channel_follower_count` is live sub count — good tier signal.

## FLOW 2 — yt-dlp channel FLAT list — ✅ WORKS (upload_date absent, as expected)

```powershell
yt-dlp --flat-playlist -J "https://www.youtube.com/@2hollis/videos"
```

Flat entry keys: `title, thumbnails, duration, view_count, timestamp, live_status, availability,
channel_url, uploader_url, creators, ie_key, id, _type, url`.
Confirmed: `view_count` PRESENT (e.g. 640000), `upload_date` **EMPTY**.
Bonus: flat entries DO carry `timestamp` (epoch seconds) — usable as a rough upload date
without the slow per-video fetch.

## FLOW 3 — yt-dlp NON-FLAT channel fetch (dates) — ✅ WORKS, ~8s for 3 videos

```powershell
yt-dlp -J --playlist-items 1-3 "https://www.youtube.com/channel/UCFyU8c3PqVmyvDtks-_1biQ/videos"
```

Timed: **8.09 s** for 3 videos. Per-video `upload_date` + `view_count` both present:
Hurt `640421 / 20260722`, Shrine live `226183 / 20260322`, flash `1466871 / 20250730`.
This is the flow for the 3-releases-in-24-months cadence check. Note: 3 items ≈ 8s → ~40 videos ≈ 100s+;
recommend `--playlist-items 1-N` on the RECENT N (newest first) so cadence checks only need N≈30.

**PowerShell gotcha:** do NOT use `2>&1 | Out-File` — stderr warning lines become error records and corrupt
the JSON. Use `1> file.json 2> file_err.txt`.

**JS runtime warning:** yt-dlp 2026.07.04 emits
`WARNING: No supported JavaScript runtime could be found` on YouTube extraction
(deno enabled by default but not installed). Metadata extraction still worked for all YT flows here,
but install deno / pass `--js-runtimes` for guaranteed format extraction.

## FLOW 4 — artist name → channel URL via yt-dlp — ✅ WORKS (indirectly)

```powershell
yt-dlp -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:2hollis channel"
```

`ytsearch1:<artist> channel` returns a VIDEO result, not a channel object — but the result JSON carries
`channel_url: https://www.youtube.com/channel/UCFyU8c3PqVmyvDtks-_1biQ` and `channel_follower_count`.
So: search any song/video of the artist → read `channel_url` → feed flows 2/3. Direct `https://www.youtube.com/@<handle>`
also works when the handle is known. **Resolution path confirmed.**

## FLOW 5 — YouTube MUSIC URLs — ✅ WORKS (previously untested)

```powershell
yt-dlp --flat-playlist -J "https://music.youtube.com/channel/UCFyU8c3PqVmyvDtks-_1biQ"
```

Extracted 19 entries with title + view_count. Same channel id works on both domains —
swap `www.youtube.com` → `music.youtube.com` freely.

## FLOW 6 — SoundCloud search via yt-dlp — ✅ WORKS, play_count EMPTY (confirmed)

```powershell
yt-dlp -j --ignore-no-formats-error --skip-download --no-warnings --playlist-items 1 "scsearch3:2hollis"
```

Result: `title=jeans`, `upload_date=20231027`, `like_count=155775`, `repost_count=1619`,
`play_count=` **EMPTY** (yt-dlp limitation — confirmed).
Note: with `-j --skip-download` it also succeeded WITHOUT `--ignore-no-formats-error` (exit 0);
the flag is still recommended insurance (the hls_mp3/DRM error hits when formats are actually resolved,
e.g. on download or on some tracks).

## FLOW 7 — SoundCloud track page hydration — ✅ WORKS (real play counts)

```powershell
$html = (Invoke-WebRequest -Uri "https://soundcloud.com/2hollis/jeans" -UseBasicParsing -Headers @{"User-Agent"="Mozilla/5.0 ... Chrome/126 ..."}).Content
$m = [regex]::Match($html, 'window\.__sc_hydration\s*=\s*(.*?);</script>', 'Singleline')
$j = $m.Groups[1].Value | ConvertFrom-Json
$s = ($j | Where-Object { $_.hydratable -eq 'sound' }).data
```

**2026 layout change:** hydration array index 0 is now `hydratable: anonymousId`; entries 0–6 are session
noise (`features, geoip, privacySettings, statsigClientInitializeResponse, trackingBrowserTabId, apiClient`).
The track object is `hydratable == "sound"` (index 8 on track pages) — find it BY TYPE, not by index.
Exact fields: `data.playback_count`, `data.created_at` (ISO 8601 UTC), plus `likes_count`,
`reposts_count`, `comment_count`, `duration`, `user_id`, `permalink_url`.

Verified numbers: **jeans** → `playback_count=8354909`, `created_at=2023-10-27T18:56:36Z`, likes 155775.

## FLOW 8 — SoundCloud artist page → per-track counts — ⚠️ PARTIAL (fix found)

Artist page HTML (`soundcloud.com/2hollis`) is a client-rendered JS shell:
its `__sc_hydration` contains only `user` (id=256335704, track_count=97, followers_count=165364) —
**NO track permalinks or per-track counts embedded.** HTML link scraping returns nothing.

**Working replacement:** yt-dlp's user extractor lists every track with its permalink URL:

```powershell
yt-dlp --flat-playlist -J "https://soundcloud.com/2hollis"
```

→ `_type: playlist`, 104 entries, each `url: https://soundcloud.com/2hollis/<slug>`.
Then loop flow 7 per track URL. End-to-end verified (4 tracks):

| track | plays | created | likes |
|---|---|---|---|
| hurt | 88,984 | 2026-07-16 | 4,843 |
| fly | 657,266 | 2025-08-04 | 20,603 |
| crush | 4,882,036 | 2024-04-17 | 100,949 |
| cliche | 1,215,759 | 2023-08-04 | 29,153 |

Note: SC API v2 (`api-v2.soundcloud.com/users/256335704/tracks`) without a client_id → **HTTP 401** (gated).
No rate limiting observed on page fetches (~8 requests, 0.7s spacing).

## FLOW 9 — Discogs API (token as `token=` query param) — ✅ WORKS

Token: sent as `?token=...` query param + custom User-Agent header. **Required**: PowerShell `Invoke-WebRequest`
with `-UseBasicParsing`; sending the token as `Authorization` header → 401 → IWR throws NonInteractive-mode
error trying to prompt for credentials.

```powershell
Invoke-WebRequest -Uri "https://api.discogs.com/database/search?q=2hollis&type=artist&token=<TOKEN>" -Headers @{"User-Agent"="MusicDataTest/1.0"} -UseBasicParsing
```

(a) Artist search → **2hollis artist id = 13974889** (first hit).
(b) `GET /artists/13974889/releases?sort=year&sort_order=desc` → releases; filter `type == "release"` (8 found,
e.g. Boy 2024 id 30968632, White Tiger 2022 id 37673622, Animæl 2025 id 35971384). Note: `sort=year` ordering
was imperfect (some out-of-year-order rows) — re-sort client-side by `year` to be safe. Console mangles some
UTF-8 titles (Animæl) — display artifact only, JSON is fine.
(c) **Credit JSON paths (VERIFIED on a credit-rich release, Kendrick DAMN id 10559651):**
   - Release-level: **`release.extraartists[]`** → `{name, role}` (e.g. A&R roles).
   - Per-track: **`tracklist[N].extraartists[]`** → `{name, role}` — "Written-By" lives here:
     `tracklist[0].extraartists` contained `{name: "Kendrick Duckworth", role: "Written-By"}` etc.
     Filter: `tracklist[N].extraartists | where role -match "Written"`.
   - ⚠️ Caveat: 2hollis's own Discogs releases (30968632, 34799171) have NO extraartists anywhere —
     Discogs credits are community-sourced and often absent for newer/indie releases. Treat Discogs
     credits as "if present", not guaranteed.
Rate limit: header `X-Discogs-Ratelimit-Remaining` = 59 after first call (60/min, no burst pain at this pace).

## FLOW 10 — Kworb artist songs page — ✅ WORKS (column format captured)

Finding the artist id: 2hollis was **NOT in kworb's artists.html** and not in songs.html —
must resolve Spotify artist id elsewhere (search engine / Spotify web), then hit the direct URL:

```
https://kworb.net/spotify/artist/72NhFAGG5Pt91VbheJeEPG_songs.html
```

Page = TWO tables:
1. **Artist summary:** `Streams` (cumulative TOTAL = 682,614,131), split `As lead` / `Solo` / `As feature (*)`,
   plus `Daily` and `Tracks` rows.
2. **Songs table** (3 columns): `Song Title` (links to open.spotify.com/track/<id>) | `Streams` (cumulative
   lifetime) | `Daily`.

So: per-song CUMULATIVE total exists (column 2), and an artist-wide cumulative total exists in the summary.
NO date column — cannot derive per-song cadence from kworb alone.
Sample rows: poster boy 206,485,133 (daily 278,744) · jeans 55,291,708 (56,816) · crush 36,428,136 (118,031) ·
cliche 19,563,266 (27,081).

## FLOW 11 — Cross-check (one song, 3 sources) — ✅ consistent-with-platform-mix

**jeans** (released 2023-08/2023-10):
| source | number |
|---|---|
| YouTube official video views (flow 1) | 6,206,802 |
| SoundCloud plays (flow 7) | 8,354,909 |
| Spotify cumulative (kworb) | 55,291,708 |

Also: **cliche** → YT official audio 640,133 / SC 1,215,759 / Spotify 19,563,266.
**crush** → YT official video 3,542,620 / SC 4,882,036 / Spotify 36,428,136.

Expected divergence: YouTube counts VIDEO views (topic/lyric/audio uploads are separate videos and must be
summed), SoundCloud is one upload per track, Spotify is the largest platform for this artist (~7x SC).
No single "true" number exists — report per-platform. Ratios are directionally consistent.

---

## GOTCHAS SUMMARY

1. PowerShell: `curl` = alias for Invoke-WebRequest; use `curl.exe` or IWR.
2. Discogs: token MUST be `token=` query param, NOT Authorization header (401 → IWR NonInteractive crash).
3. IWR: always `-UseBasicParsing`; send a real browser UA to SoundCloud/kworb.
4. yt-dlp: don't merge stderr into JSON files (`2>&1 | Out-File` corrupts). Use `1>` / `2>`.
5. SoundCloud hydration: find `hydratable == "sound"` by TYPE (index 0 is now anonymousId noise).
6. yt-dlp scsearch `play_count` is always empty — hydration is the only play-count source.
7. YouTube JS runtime warning (no deno) — metadata still extracted; install deno for full safety.
8. Kworb artists.html is incomplete — resolve Spotify artist id externally.

## RATE LIMITS OBSERVED

- Discogs: 60 req/min (X-Discogs-Ratelimit-Remaining header). No throttling hit in this test.
- SoundCloud page fetches: none observed at ~8 reqs / 0.7s spacing. API v2 needs client_id (401 without).
- YouTube: none observed (yt-dlp handles consent/cookies transparently; ~10 calls).
- Kworb: none observed (2 fetches, plain static HTML).

## RECOMMENDED PER-PLATFORM PROCEDURE (for the mission prompt)

**YouTube (views + cadence):**
1. `yt-dlp -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:<song>"` → view_count, upload_date, channel_url, channel_follower_count.
2. Resolve channel via `channel_url` from step 1 (or `ytsearch1:<artist> channel`, or known @handle).
3. Flat list (cheap): `yt-dlp --flat-playlist -J "<channel>/videos"` → titles + views + epoch `timestamp`.
4. Dates (3-releases-in-24mo check): `yt-dlp -J --playlist-items 1-30 "<channel>/videos"` (~80s for 30; newest first).
   music.youtube.com URLs work identically.

**SoundCloud (plays):**
1. Track list: `yt-dlp --flat-playlist -J "https://soundcloud.com/<artist>"` → permalink URLs.
2. Per track: GET track page (browser UA) → regex `window.__sc_hydration` → `hydratable=="sound"` → `data.playback_count` + `data.created_at`.
   (scsearch works for discovery but its play_count is always empty.)

**Discogs (credits/release dates):** search artist → releases (filter type=release, client-side sort by year) →
per release: `extraartists[]` (release-level roles) + `tracklist[N].extraartists[]` (`role == "Written-By"` for
writing credits). Credits absent on many indie releases — don't block on them. Token as query param + UA header, 60 req/min.

**Kworb (Spotify tertiary):** resolve Spotify artist id (search, then `open.spotify.com/artist/<id>`), fetch
`kworb.net/spotify/artist/<id>_songs.html` → per-song cumulative + daily; artist summary has cumulative total.
No dates.
