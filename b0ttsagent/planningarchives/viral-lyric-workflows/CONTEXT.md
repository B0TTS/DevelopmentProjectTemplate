## MISSION:
Find and document in depth the lyric-writing workflows/formulas of 10-15 verified creators who consistently make songs that hit 100k-1m+ plays/views, and synthesize the parallels between frameworks that work.

### SOURCE ELIGIBILITY (in priority order):
1. VERIFIED ARTISTS (top priority) — musicians who meet ALL of:
   - Active within the last 5 years of the current date
   - Pass the Consistency Test (below) — this is the hard gate
   - Roughly 1-20m Monthly Audience on YouTube Music (soft signal only; do not disqualify on this alone)
   - If an artist has no displayed Monthly Audience (below YouTube Music eligibility), they disqualify by default — UNLESS their publicly documented writing workflow is demonstrably realistic and viable; then framework quality outweighs the missing metric.
   - Publicly documented their writing process step by step (videos, blogs, podcasts, interviews, courses)
2. VERIFIED SONGWRITERS/GHOSTWRITERS — writers who aren't famous themselves but have verified credits on songs with ≥100k plays/views on YouTube or SoundCloud (Discogs, ASCAP/BMI, Genius, YouTube credits, interviews). They qualify via credits, not their own listener numbers.
3. ANALYSTS/COACHES (secondary, fill gaps only) — deeply credentialed creators who reverse-engineer viral songs with concrete case studies. Only include if their frameworks are documented in depth with real examples.

Weigh tier 1 (VERIFIED ARTISTS) and tier 2 (VERIFIED SONGWRITERS/GHOSTWRITERS) heavily; tier 3 fills gaps only. Anyone with no viral content within the last 5 years is EXCLUDED.

#### The Consistency Test (hard eligibility gate):
- "Consistently" = at least 3 releases within the last 24 months of the current date.
- "100k-1m+ plays/views" = each qualifying release has ≥100k plays/views on at least one target platform, per public counts at research time. The "1m+" describes the top of the typical range — there is NO upper cap; a song over 1m does not disqualify.
- A release passes if EITHER an official upload on the artist's own YouTube channel OR its SoundCloud track has ≥100k at research time. Fan re-uploads, compilations, and auto-generated Topic-channel uploads do NOT count.
- Verify against public counts on the target platforms below, using VERIFICATION PROCEDURES. Cite the counts and where you saw them.

### SCOPE:
Lyrics + song craft — words, hooks, song structure, rhyme/flow, and melody-adjacent lyric decisions. Not full production.

### PLATFORMS:
YouTube (incl. YouTube Music) and SoundCloud. Spotify (via kworb) only as an optional tertiary cross-check. Not TikTok-centric.

### VERIFICATION PROCEDURES:
Exact, hand-verified commands for every number this mission needs. All run on Windows PowerShell 5.1 (yt-dlp 2026.07.04 on PATH, curl.exe 8.21.0). When saving JSON output, use `1> file.json 2> file_err.txt` — NEVER `2>&1 | Out-File` (stderr leaks into the JSON and corrupts it).

#### YouTube (anchor platform — views + cadence, no keys):
1. Single song → exact views, upload date, channel, subs:
   `yt-dlp -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:<song query>"`
   → read `view_count`, `upload_date`, `channel`, `channel_follower_count`.
2. Resolve artist name → channel from step 1's `channel_url` (or `ytsearch1:<artist> channel`, or a known @handle).
3. Cheap channel listing (views only, no dates):
   `yt-dlp --flat-playlist -J "<channel_url>/videos"` → per video: `title`, `view_count`, epoch `timestamp` (usable as a rough date).
4. Dates for the 24-month cadence check (newest first; ~8s per 3 videos):
   `yt-dlp -J --playlist-items 1-30 "<channel_url>/videos"` → `upload_date` + `view_count` per video.
   `music.youtube.com/channel/<id>` URLs work identically to `www.youtube.com`.
- Gotchas: yt-dlp may warn "No supported JavaScript runtime" (deno not installed) — metadata still extracts. Auto-generated Topic-channel, lyric, and fan uploads are SEPARATE videos; only the artist's own channel uploads count for the Consistency Test.

#### SoundCloud (plays):
1. List all tracks: `yt-dlp --flat-playlist -J "https://soundcloud.com/<artist>"` → each entry's `url` is the track permalink.
2. Per track, GET the page with a BROWSER User-Agent (the default UA returns a stub page) and parse the hydration JSON:
   `Invoke-WebRequest -Uri "<track-url>" -UseBasicParsing -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}` → regex `window\.__sc_hydration\s*=\s*(.*?);</script>` → `ConvertFrom-Json` → find the entry where `hydratable -eq "sound"` (find it BY TYPE, not by index — index 0 is now session noise) → read `data.playback_count`, `data.created_at`.
- Gotchas: `scsearch3:<query>` via yt-dlp works for discovery but its `play_count` is ALWAYS empty — page hydration is the only play-count source. Add `--ignore-no-formats-error` as insurance.

#### YouTube Music Monthly Audience (soft signal):
1. Simplest — parse the artist page HTML: GET `https://music.youtube.com/channel/<channel_id>` and search `ytInitialData` for `monthlyListenerCount` (e.g. `"52.5M monthly audience"`).
2. Alternative — ytmusicapi ≥ 1.11.5 (Python): `YTMusic().get_artist(channel_id)["monthlyListeners"]` → `"52.5M"`; returns None when the artist is below eligibility.
3. Proxy fallback — YouTube Data API: `channels.list?part=statistics&id=<channel_id>` → `subscriberCount` + `viewCount` (there is NO audience field; 1 quota unit per call).
- Eligibility: the number displays only for Official Artist Channels with >7,500 subs and >50k Monthly Audience. No displayed number = below threshold → apply the SOURCE ELIGIBILITY exception.
- Caveat: audience counts all YouTube surfaces (incl. Shorts, fan uploads, collabs), so it runs higher than Spotify monthly listeners for the same artist, and values are rounded to 1 decimal. Soft signal only.

#### Discogs (credits + release dates):
Token embedded below. Always send it as the `token=` query param (NOT an Authorization header — that 401s and crashes Invoke-WebRequest in NonInteractive mode), with a User-Agent header, using `curl.exe` (PowerShell `curl` is an IWR alias).
1. Artist search → id:
   `curl.exe -H "User-Agent: MusicResearch/1.0" "https://api.discogs.com/database/search?q=<artist>&type=artist&token=SaexfzTKevFUIavsQItSTBzxZDQvJItGkGJACDoN"` → `results[0].id`.
2. Releases: `GET https://api.discogs.com/artists/<id>/releases?sort=year&sort_order=desc&token=SaexfzTKevFUIavsQItSTBzxZDQvJItGkGJACDoN` → filter `type == "release"`; re-sort client-side by `year` (Discogs ordering is imperfect).
3. Writing credits: per release, check `tracklist[N].extraartists[]` for `role` matching "Written" (release-level `extraartists[]` also exists).
- Rate limit: 60 req/min (check `X-Discogs-Ratelimit-Remaining` header). Caveat: credits are community-sourced and often absent on indie releases — treat as "if present", never block on them.

#### Kworb (Spotify data — optional tertiary cross-check only):
Resolve the Spotify artist id externally (kworb's own artist index is incomplete), then fetch `https://kworb.net/spotify/artist/<id>_songs.html` → per-song cumulative + daily streams. No dates — cannot derive cadence from kworb alone.

#### Cross-check note:
No single "true" number exists — report per-platform counts and cite where each was seen. Ratios across platforms are directionally consistent; a massive mismatch usually means you're looking at the wrong video/track.

### EVIDENCE BAR:
This bar applies to workflow documentation depth, NOT to eligibility — numbers and credits must always be third-party verified first. Given verification passes, deep, self-consistent documentation of the workflow is enough. Never fabricate repeatability claims — if a framework lacks proof of repeat success, say so explicitly.

### ORCHESTRATION:
- The orchestrator must ask the user clarifying questions before beginning.
- Use the opencode-web-research skill for all web research and source discovery.
- **Phase 0 — Discovery first.** Before any deep dives, build a candidate pool of 20-30 names, each with a one-line eligibility hypothesis. Screen every candidate against SOURCE ELIGIBILITY + the Consistency Test. Pre-screen candidate numbers with the cheap flows (flat-playlist views, SoundCloud track list) before dispatching deep dives. Only then dispatch deep-dive agents for the screened candidates.
- Dispatch research sub-agents in parallel — roughly one per screened creator — pulling from ALL formats: YouTube/podcast transcripts (yt-dlp available), blogs, newsletters, course material, interviews, AMAs.
- Every sub-agent brief must instruct the sub-agent to load/activate the `opencode-web-research` skill.
- Each sub-agent must verify the creator's numbers/credits BEFORE documenting the workflow (use VERIFICATION PROCEDURES).
- **Source constraints:** publicly accessible sources only. Paid courses and paywalled material may be cited as existing, but never fabricate their contents. If a video has no captions, note it as a gap and move on. Quote or timestamp transcript claims.
- **Failure path:** if fewer than 10 creators pass verification, deliver what passed and state the shortfall explicitly in INDEX.md — never pad with unverified names. Log every candidate who failed verification, with the reason, in REJECTED.md.
- After collection, the main agent runs a synthesis pass that extracts cross-framework parallels.

### OUTPUT (under b0ttsagent/research/viral-lyric-workflows/):
- INDEX.md — all verified creators, ranked by (1) verification strength, then (2) depth of process documentation. For each: verification status, platform, 1-2 line summary. If fewer than 10 qualified, state that here.
- creators/<name>.md — ONE doc per creator, ~400-800 words, using this exact skeleton (parallel structure is what makes the synthesis possible):
  1. **Eligibility Evidence** — the numbers/credits that passed the Consistency Test, with links
  2. **Step-by-Step Workflow** — their exact process as they documented it
  3. **Real Song Examples** — songs they've broken down or that demonstrate the method
  4. **Tools & Templates** — anything named and reusable
  5. **Proven vs Claimed** — where the method has repeat success vs where it's only asserted
  6. **Sources** — links throughout and listed
- SYNTHESIS.md — parallels ranked by how many creators share each element, delivered as: (a) a creators × elements matrix table, (b) a ranked list with per-element creator counts, weighted by verification strength, and (c) notable divergences.
- SOURCES.md — every link used, per creator, with access dates.
- REJECTED.md — every candidate who failed verification, and why.

EVERY claim must be traceable to a cited source link. No guesses about what a creator does — only document what they've actually published.
