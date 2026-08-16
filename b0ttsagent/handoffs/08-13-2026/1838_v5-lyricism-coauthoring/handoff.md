# Handoff — Musician Lyricism Research V5 (doc co-authoring)

## Next session focus

Continue the **doc-coauthoring workflow** on the V5 mission prompt. Stage 1 (context gathering) is mostly done; next session picks up at the remaining clarifying questions, then Stage 2 (section-by-section refinement) and Stage 3 (reader testing with a fresh sub-agent).

The user explicitly wants the co-authoring to happen in a fresh session — do not edit the doc in this session.

## Mission context

The prompt (originally V3) directs research agents to find 10–15 creators who consistently make 100k–1m+ stream songs, verify their numbers, and document their lyric-writing workflows. V5 is a replatformed copy: **counts come from YouTube/YouTube Music and SoundCloud** (Spotify deprioritized), **Discogs** for credits + release dates, **Kworb** as optional tertiary cross-check.

## What was accomplished this session

1. Explored how agents practically obtain music stream data (first answer covered Spotify partner-API/embed tricks, kworb, YouTube API, SoundCloud v2 — now mostly irrelevant to V5).
2. User decided the replatform; asked pre-start questions, got decisions (below).
3. Spawned **two parallel sub-agents**:
   - Hands-on tool tester (general agent) → `b0ttsagent/temp/music-data-test-findings.md`
   - YTM monthly-listeners researcher (b0tts-researcher) → `b0ttsagent/temp/ytm-monthly-listeners-research.md`
4. **Personally spot-checked** every load-bearing claim (all passed; gotchas noted below).
5. Ran Stage 1 meta-questions of the doc-coauthoring workflow; user answered all five.

## Locked decisions (user answers)

1. **Target file:** edit `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Musician Lyricism Research V5.md` in place (copy of V3; V3 stays untouched).
2. **Consistency Test stays the same bar, replatformed:** ≥3 releases in last 24 months, each ≥100k. A release passes on **either** an official artist-channel YouTube upload OR a SoundCloud track. Fan re-uploads/compilations do NOT count.
3. **Soft signal:** keep the literal "roughly 1–20m" number, but sourced from **YouTube Music "Monthly Audience"** (not Spotify). User chose NOT to recalibrate despite YTM running higher.
4. **Below-threshold artists** (no Monthly Audience displayed — requires OAC + >7,500 subs + >50k audience): disqualify by default, UNLESS their documented workflow is demonstrably realistic and viable — then framework quality outweighs the missing metric.
5. **Discogs** = credits verification (tier 2) + release-date/cadence cross-check. Token gets embedded in the prompt. **The token was pasted by the user in this session's chat — it is redacted here; re-ask the user for it when embedding into V5.**
6. **Exact commands/endpoints embedded in the prompt** as a new VERIFICATION PROCEDURES section.
7. **Primary reader:** the executing agents. The orchestrator will be told to ask the user questions before beginning.
8. Tier 2 credit-source wording should swap "Spotify credits" → Discogs / ASCAP / BMI / Genius / YouTube credits. Platforms section → YouTube (incl. YouTube Music) + SoundCloud. Kworb stays optional tertiary.

## Verified data-acquisition playbook (the substance for Stage 2)

All four paths personally re-verified this session:

- **yt-dlp → YouTube (anchor platform, no keys):**
  - Single track: `yt-dlp -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:<song query>"` → exact `view_count`, `upload_date`, `channel`, `channel_follower_count`. Verified: 2hollis "jeans" = 6,206,838 views, followers 285,000.
  - Channel flat list (cheap, views only): `yt-dlp --flat-playlist -J "<channel_url>/videos"` → title + view_count, NO upload_date.
  - Dates for 24-month cadence check: non-flat `yt-dlp -J --playlist-items 1-3 "<channel_url>/videos"` → upload_date + view_count (~8s/3 videos).
  - `music.youtube.com/channel/<id>` URLs work identically.
  - Resolve artist name → channel via `ytsearch1:<artist>` (video result carries `channel_url`).
  - Gotcha: `2>&1 | Out-File` corrupts JSON (stderr mixed in); use `1>`/`2>` redirects. yt-dlp warns "No supported JavaScript runtime" (deno not installed) — metadata still extracts.
- **SoundCloud (no keys):**
  - Track page HTML hydration has exact `playback_count` + `created_at`: GET `https://soundcloud.com/<user>/<slug>` with a **browser User-Agent** (default curl UA returns a 389-byte stub — gotcha verified). Regex `"playback_count":(\d+)`. Verified: odesza/bloom = 9,842,540.
  - Artist pages are JS shells — hydration lacks track lists. Use `yt-dlp --flat-playlist -J "<soundcloud artist url>"` for permalinks, then hydrate each track page.
  - `scsearch3:<query>` via yt-dlp works for discovery but `play_count` is ALWAYS empty; add `--ignore-no-formats-error`.
- **Discogs API (token embedded in prompt):**
  - Use `curl.exe` + `token=` query param + User-Agent header. **Never Invoke-WebRequest** — it crashes in PowerShell NonInteractive mode (verified).
  - Artist search → `type=artist` → id; releases → filter `type=release`, sort by year; credits at `tracklist[].extraartists[].role == "Written-By"` (release-level `extraartists` also exists). 60 req/min.
  - Caveat: indie releases often have zero credit data (community-sourced).
  - Verified: 2hollis artist id 13974889.
- **YTM Monthly Audience (soft signal):**
  - Official metric (Google Help: support.google.com/youtubemusic/answer/15621827): unique listeners/viewers across ALL YouTube surfaces (incl. Shorts, fan uploads, collabs) last 28 days, daily. Eligibility: OAC + >7,500 subs + >50k audience.
  - Fetch: `ytmusicapi ≥ 1.11.5` `get_artist(channel_id)["monthlyListeners"]`, or parse `monthlyListenerCount` from `music.youtube.com/channel/<id>` HTML. YouTube Data API has NO audience field (only subs/views/videos).
  - Caveat: runs higher than Spotify monthly listeners (Oasis ≈52.5M YTM vs ~30M Spotify).
- **Kworb (tertiary, Spotify-centric):** `kworb.net/spotify/artist/{id}_songs.html` = cumulative + daily per song, no dates. Long-tail artists often absent.

## Open items for co-authoring (Stage 2 planning)

- Section-by-section edit plan for V5 (work through SOURCE ELIGIBILITY, Consistency Test, PLATFORMS, ORCHESTRATION, OUTPUT in some order — user picks).
- Draft the new VERIFICATION PROCEDURES section from the playbook above.
- Wording for the below-threshold exception (rule 4).
- Whether to note the Monthly Audience inflation caveat in the prompt or leave the band clean at 1–20m.
- Reader testing (Stage 3): fresh sub-agent gets doc + predicted reader questions.

## Key files

- **Target:** `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Musician Lyricism Research V5.md`
- Original: same folder, `Musician Lyricism Research V3.md` (read-only reference)
- Test findings: `b0ttsagent/temp/music-data-test-findings.md`
- YTM research: `b0ttsagent/temp/ytm-monthly-listeners-research.md`
- Temp dumping ground for any new test artifacts: `b0ttsagent/temp/`

## Skills for next session

- **doc-coauthoring** — primary; pick up Stage 1, run Stage 2 section-by-section, then Stage 3 reader testing with a fresh sub-agent.
- **opencode-web-research** — for any re-verification of claims during drafting.
- **markdown-doc-designs** — optional quality pass on the final prompt doc.
