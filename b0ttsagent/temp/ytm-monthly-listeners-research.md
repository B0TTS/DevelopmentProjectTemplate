# YouTube Music "Monthly Listeners" — Research Findings (2026-08-13)

**Question:** Can a research agent obtain a "monthly listeners"-style audience metric for a musician on YouTube / YouTube Music, in practice, today?

**Verdict: YES — YouTube Music exposes a public, fan-facing metric called "Monthly Audience"** (launched Jan 2025), which is the exact analog of Spotify Monthly Listeners. It is displayed on YouTube Music artist pages and is programmatically fetchable (verified live this session). It is NOT exposed via the YouTube Data API v3, but IS exposed via the unofficial ytmusicapi library and via the raw artist-page HTML.

---

## 1. The metric: YouTube Music "Monthly Audience"

- **Official definition** (Google Help): "a new fan-facing public metric on YouTube Music: Monthly Audience. It will update daily to show an artist's total number of unique listeners and viewers across all formats in the last 28 days." It "estimates the number of unique users globally who have viewed or listened to an artist's content in the past month across all YouTube formats" — YouTube, YouTube Music, and YouTube Kids. Counts: videos incl. Shorts uploaded by the artist/label, collaborations on other channels, fan-uploaded content using the artist's music, and non-music content from the artist's channel. [CITED: https://support.google.com/youtubemusic/answer/15621827?hl=en]
- **Where it appears publicly:** YouTube Music artist pages (web & mobile) beside the subscriber count, and in YT Music search results; only artists meeting eligibility get the public number. [CITED: Google Help above; https://precise.digital/youtube-music-monthly-audience-metric/]
- **Eligibility thresholds:** channel must be an Official Artist Channel (OAC), have >7,500 subscribers, and Monthly Audience > 50,000. Below that, only subscriber count is displayed. [CITED: Google Help above]
- **Launch/rollout:** announced/testing Jan 2025. [CITED: https://9to5google.com/2025/01/07/youtube-music-monthly-audience-metric/ (snippet); https://musically.com/2025/01/09/youtube-music-adds-monthly-audience-public-metric-for-artists/ (snippet)]
- **Live verification (this session):** Fetched the raw HTML of the Oasis YT Music artist page (https://music.youtube.com/channel/UCmMUZbaYdNH0bEd1PAlAqsA) today and found embedded in `ytInitialData`:
  `"monthlyListenerCount":{"runs":[{"text":"52.5M monthly audience"}],"accessibility":{"accessibilityData":{"label":"52.5 million monthly audience"}}}`
  and microformat description `"Artist • 52.5M monthly audience"`. The field is present in the server-rendered HTML — no login or API key required to see it. [VERIFIED: live fetch]

## 2. YouTube Data API v3 (official)

- `channels.list` with `part=statistics` returns `subscriberCount`, `videoCount`, `viewCount`, `hiddenSubscriberCount`. [CITED: https://developers.google.com/youtube/v3/docs/channels — statistics object; field note for statistics.subscriberCount on https://developers.google.com/youtube/v3/docs/channels/list]
- **Quota cost: 1 unit per call** (official quota calculator table: `channels | list | 1`); default allocation 10,000 units/day; `search.list`/`videos.insert` have their own 100/day buckets. [CITED: https://developers.google.com/youtube/v3/determine_quota_cost]
- The Data API v3 has **no monthly-audience/monthly-listeners field anywhere** — Monthly Audience only exists on YT Music surfaces (innertube), not the Data API. [ASSUMED — consistent with official docs reviewed; no such field found in the API reference]
- Closest Data API equivalent to "monthly listeners" is subscriberCount + total viewCount (all-time), neither of which is a 28-day unique-user figure.

## 3. Practical fetch methods (ranked)

1. **ytmusicapi (recommended — no API key, returns the exact metric):**
   `from ytmusicapi import YTMusic; YTMusic().get_artist(channelId)["monthlyListeners"]` → e.g. `"29.1M"`.
   - Added in **v1.11.5 (released 2025-12-22)**: "feat(artists): add new monthly audience feature to get_artist (#769)" — [CITED: https://github.com/sigma67/ytmusicapi/releases/tag/1.11.5; PR https://github.com/sigma67/ytmusicapi/pull/849]
   - Documented in official docs (get_artist example shows `"monthlyListeners": "29.1M"`) — [CITED: https://ytmusicapi.readthedocs.io/en/stable/reference/browsing.html]
   - Implementation extracts innertube field `header.monthlyListenerCount` and strips the " monthly audience" suffix; returns None when absent (artist below eligibility). [CITED: PR #849 diff]
2. **Raw HTML scrape (no library):** GET `https://music.youtube.com/channel/<channelId>` and parse `ytInitialData` → `header.monthlyListenerCount.runs[0].text` (e.g. "52.5M monthly audience"). Verified present in the live page today. [VERIFIED: live fetch]
3. **YouTube Data API v3:** does NOT give Monthly Audience; use only for the proxy stats (subscribers, total views): `GET https://www.googleapis.com/youtube/v3/channels?part=statistics&id=<channelId>` — 1 quota unit per artist. [CITED: https://developers.google.com/youtube/v3/docs/channels/list]
4. **yt-dlp: NOT suitable.** No channel-level stat extraction (subscriber count) exists — open feature request since 2020 — [CITED: https://github.com/yt-dlp/yt-dlp/issues/2350]; channel metadata extraction is flaky for content-less channels [CITED: https://github.com/yt-dlp/yt-dlp/issues/13155]. Monthly Audience is not exposed by yt-dlp in any form.

## 4. Third-party aggregators (public/free)

- **kworb.net:** NO monthly listeners/audience for YouTube. YouTube section = video-level views, trending, and per-artist **cumulative all-time official-channel views** ("Total views (in millions) across all official channels", e.g. Bad Bunny 41,694.5M) — [CITED: https://kworb.net/youtube/archive.html; https://kworb.net/youtube/stats.html]. Free, plain HTML tables (scrapable). kworb's monthly-listeners product is Spotify-only (https://www.kworb.net/spotify/listeners.html).
- **Social Blade:** free tier shows subscriber count, total views, daily view/sub deltas (last 14 days), ranks; "last 30 days" summaries and earnings gated behind login; **no monthly audience** — [CITED: https://socialblade.com/youtube/channel/UCmMUZbaYdNH0bEd1PAlAqsA (read live)].
- **Viewstats:** YouTube channel analytics (subs/views/estimates, free tier + Pro). Page is client-rendered; content not readable this session; no evidence it carries Monthly Audience. [ASSUMED / LOW confidence — https://viewstats.com/channel/UCmMUZbaYdNH0bEd1PAlAqsA returned only a logo]
- **Songstats / Viberate / Chartmetric:** paid artist-analytics platforms; Viberate markets a monthly-audience-style product pulling Spotify + YouTube data; none expose free public YTM monthly audience. [CITED: https://musically.com/2020/11/04/tools-viberate-the-all-in-one-platform-for-growing-your-music-career/ (snippet); https://www.musicanalyticstools.com/music-analytics/youtube-music-listening-stats-viberate-or-chartmetric/ (snippet: Chartmetric from ~$160/mo, Viberate cheaper)]

## 5. Recommendation for the mission prompt

**Use YouTube Music Monthly Audience as the soft signal — it exists, it is public, and it is the exact structural analog of Spotify Monthly Listeners** (unique users over the last 28 days, updated daily).

- **Fetch method to put in the mission:** ytmusicapi >= 1.11.5 — `YTMusic().get_artist(channel_id)["monthlyListeners"]` (returns e.g. "29.1M"; None if artist below eligibility). Fallback: parse the artist-page HTML for `monthlyListenerCount`. Proxy fallback (Data API): `channels.list?part=statistics` → subscriberCount + viewCount.
- **Caveats to encode in the prompt:**
  - Only available for eligible artists (OAC, >7,500 subs, >50k monthly audience) — irrelevant for the 1–20M Spotify-listener band, which far exceeds the floor.
  - It counts *audience across all YouTube surfaces* (views incl. Shorts + streams), so it runs **higher** than Spotify monthly listeners for the same artist (example: Oasis ≈ 52.5M YTM monthly audience vs ~30M Spotify monthly listeners) — the mission's thresholds need recalibration, not 1:1 mapping.
  - Value is rounded to 1 decimal ("52.5M") — a soft signal, not a precise count.
  - ytmusicapi is unofficial (emulates browser requests to music.youtube.com/youtubei/v1/browse); may break on YouTube changes; no API key needed for public data.

## Sources read this session (primary)
- https://support.google.com/youtubemusic/answer/15621827?hl=en (official Google Help — definition, calculation, eligibility) [read]
- https://music.youtube.com/channel/UCmMUZbaYdNH0bEd1PAlAqsA (live Oasis artist page HTML — monthlyListenerCount "52.5M monthly audience") [read]
- https://developers.google.com/youtube/v3/determine_quota_cost (quota table: channels.list = 1 unit) [read]
- https://developers.google.com/youtube/v3/docs/channels/list (quota note "1 unit"; statistics.subscriberCount note) [read]
- https://developers.google.com/youtube/v3/docs/channels (statistics object reference) [partially read]
- https://ytmusicapi.readthedocs.io/en/stable/reference/browsing.html (get_artist docs, monthlyListeners example) [read]
- https://github.com/sigma67/ytmusicapi/releases/tag/1.11.5 and https://github.com/sigma67/ytmusicapi/pull/849 (feature ship + parsing code) [read via search-result full text]
- https://kworb.net/youtube/archive.html, https://kworb.net/youtube/stats.html, https://kworb.net/youtube/ (kworb YouTube coverage = video views, no monthly audience) [read]
- https://socialblade.com/youtube/channel/UCmMUZbaYdNH0bEd1PAlAqsA (free-tier metrics) [read]
- https://github.com/yt-dlp/yt-dlp/issues/2350, /issues/13155 (yt-dlp lacks channel stat extraction) [read via search snippets]
- https://9to5google.com/2025/01/07/youtube-music-monthly-audience-metric/ (Jan 2025 rollout) [snippet only]
- https://musically.com/2025/01/09/youtube-music-adds-monthly-audience-public-metric-for-artists/ (Jan 2025 rollout) [snippet only]
- https://precise.digital/youtube-music-monthly-audience-metric/, https://soundplate.com/youtube-musics-new-monthly-audience-metric-how-it-works-what-it-means-for-artists/ (secondary coverage) [read]
