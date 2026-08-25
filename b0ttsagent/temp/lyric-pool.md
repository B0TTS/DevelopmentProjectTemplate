# Lyric Workflow Candidate Pool — Phase 0 (Discovery & Screening)

Scratch artifact for Phase 0 only. Verified output goes to `b0ttsagent/research/viral-lyric-workflows/` in later phases.

## 0.1 Clarifying answers (recorded 2026-08-13)

- **Genre coverage:** Primary = Pop + Hip-Hop/Rap (EDM dropped from primary). Secondary pool = all other genres, incl. EDM.
- **Target creator count:** 10 (bottom of mission's 10–15 range).
- **Time budget per candidate (Phase 1 deep dives):** Moderate, ~20–30 min each.

## 0.2 Capability probe verdict

- **Sub-agents own verification: YES.**
- Evidence: pilot `general` sub-agent ran yt-dlp 2026.07.04 + curl.exe 8.21.0 on Windows PowerShell 5.1. `ytsearch1` + `--flat-playlist -J` both produced clean JSON (view_count, upload_date, channel, channel_url, channel_follower_count extracted). stderr empty; no JS-runtime warning. Note: flat-playlist entries returned empty `timestamp` on this build — Phase 1 cadence dates must come from the dated listing command (`-J --playlist-items 1-30`).

## Candidate pool (28)

### Tier 1 — Artists (22)

| # | Name | Genre | Eligibility hypothesis (one line) |
|---|---|---|---|
| 01 | Charlie Puth | Pop | Releases Changes/Sideways/Washed Up era (2025–26); consistently 1M+ views; runs his own songwriting course documenting process |
| 02 | Mike Shinoda | Hip-Hop / alt-rock | Solo releases 2023–25 each 100k+; posts "behind the song" breakdowns on own channel |
| 03 | Jon Bellion | Pop | "Making of Guillotine" 3.1M views; WASH era (2025) + decades of studio-process docs |
| 04 | AJR | Pop | Every single since 2020 clears 1M+; films living-room writing process (The Maybe Man era 2023–24 + newer) |
| 05 | Logic | Hip-Hop | Ultra 85 (2024) + 2025–26 singles; two feature-length studio-process documentaries |
| 06 | Russ | Hip-Hop / R&B | Huge self-produced output (Crazy 6.6M, Workin On Me 12M, 2025); documents song creation step-by-step |
| 07 | Hanumankind | Hip-Hop (desi/global) | Big Dawgs 100M+ views; Run It Up / Lost / Bills (2024–25); did making-of Footnotes |
| 08 | mgk | Pop-punk / Rap | cliché 24.2M views (2025), Lonely Road, Lost Americana album; explains writing process in Footnotes |
| 09 | San Holo | EDM / indie-electronic | Album documentaries (album1, bb u ok?); what is life? EP (2024) + 2024–25 singles, 100k+ plays |
| 10 | Olivia Dean | Pop / neo-soul (UK) | 2026 Grammy winner; Man I Need top-5 Hot 100 (2025) + The Art of Loving (2026); "How I wrote" interview series |
| 11 | Tessa Violet | Indie pop | Crush = 112M views; 2026 album one-song-a-month (3+ releases/24mo); first-line-first process documented |
| 12 | Jack Harlow | Hip-Hop | 4 albums since 2020, latest 2026; Song Exploder ep. 311 documents approach change |
| 13 | Gracie Abrams | Pop | Secret of Us (2024) + That's So True 100M+; Song Exploder ep. 283 airs her raw writing voice memos |
| 14 | Raye | Pop | Escapism #1 UK + platinum multi-country; 2025 singles 7.5M+ views; songwriter-for-hire history documented |
| 15 | Billie Eilish | Pop | Multi-billion-stream discography; Song Exploder ep. 197 with original writing voice memos |
| 16 | Lizzo | Pop / hip-hop | Love In Real Life (2025) + platinum back catalog; plays demos-to-final on Song Exploder ep. 291 + Truth Hurts breakdown |
| 17 | Denzel Curry | Hip-Hop | ZUU→Melt My Eyez→King of the Mischievous South (2024); Song Exploder ep. 164 lyrics-driven breakdown |
| 18 | J. Cole | Hip-Hop | The Off-Season + Might Delete Later era; Applying Pressure documentary: writing drills, studio routine |
| 19 | Porter Robinson | EDM | Nurture (2021) + Smile (2024) eras, singles 5–50M+; documented building lyric craft from scratch |
| 20 | Laufey | Jazz-pop | Most-streamed jazz artist; Bewitched + A Matter of Time (2025) singles 1M+; Song Exploder ep. 259 full transcript |
| 21 | Maggie Rogers | Indie folk-pop | Alaska 40M+ streams; Don't Forget Me (2024) era; Song Exploder ep. 115 lyric/melody origin story |
| 22 | HALIENE | EDM vocalist | Rush Over Me 18M+ Spotify; Heavenly (2022) + ongoing collabs; long-form interviews detail 55-min lyric sessions |

### Tier 2 — Songwriters/ghostwriters via credits (6)

| # | Name | Genre | Eligibility hypothesis (one line) |
|---|---|---|---|
| 23 | Ryan S. Jhun | K-pop | Credited writer/producer: IVE ELEVEN/After LIKE, IU Celebrity, SHINee Lucifer, NCT U Maniac (all 100k+); 7-element recipe documented in interviews |
| 24 | Toby Gad | Pop / R&B | Writer on John Legend All of Me (1.8B), Beyoncé If I Were a Boy; chorus-first + Google Docs method documented; hosts Songs You Know podcast |
| 25 | Ross Golan | Pop | Co-writer Ariana Grande Dangerous Woman, Selena Gomez Same Old Love; hosts And The Writer Is… (~150 songwriter deep dives) |
| 26 | Nicolle Galyon | Country | Co-writer Dan + Shay Tequila (ACM Song of the Year), Miranda Lambert Automatic; own American Songwriter column + session breakdowns |
| 27 | Brent Baxter | Country | Alan Jackson Monday Morning Church (US top-5), Gord Bamford #1; step-by-step blog method + C.L.I.M.B. podcast |
| 28 | ADORA | K-pop | 30+ KOMCA credits incl. BTS Spring Day / Magic Shop / Euphoria; documents process in own ADORA-BLE series |

## Candidate details (URLs)

- **01 Charlie Puth** — YT: https://www.youtube.com/channel/UCwppdrjsBPAZg5_cUwQjfMQ · SC: https://soundcloud.com/charlieputh · Docs: studio.com/charlie-puth-music (course); youtu.be/XeO5RoVFkIY (hit chorus in real time)
- **02 Mike Shinoda** — YT: https://www.youtube.com/@mikeshinoda · Docs: youtu.be/z3z5Uz355lM (behind the song); tim.blog/2014/08/04/mike-shinoda/ (podcast)
- **03 Jon Bellion** — YT: https://www.youtube.com/@jonbellion · Docs: youtu.be/PZReO_-XeJU (Making of WASH, 209K); youtu.be/TGO-CAImUeY (Making of Guillotine)
- **04 AJR** — YT: https://www.youtube.com/@AJR · Docs: youtu.be/TA13bQExrh8 (Making of Bang!); en.wikipedia.org/wiki/AJR (The Dumb Song creation)
- **05 Logic** — YT: https://www.youtube.com/@logic · Docs: youtu.be/1yIBOuW-pyI (Vinyl Days documentary)
- **06 Russ** — YT: https://www.youtube.com/@russ · Docs: tiktok.com/@russ/video/7146988027435339014 (step-by-step creation); youtu.be/TuaoB4ph5xU (songwriting process)
- **07 Hanumankind** — YT: https://www.youtube.com/@hanumankind · Docs: udiscovermusic.com/news/hanumankind-vevo-footnotes-big-dawgs/ (Footnotes making-of)
- **08 mgk** — YT: https://www.youtube.com/@mgk · Docs: youtu.be/hLcbc5L8vI8 (Making of cliché Footnotes)
- **09 San Holo** — YT: https://www.youtube.com/@sanholobeats · SC: https://soundcloud.com/sanholobeats · Docs: youtu.be/hI8V0vR08H0 (bb u ok? documentary); youtu.be/ulGhV9lwrPc (album1 documentary)
- **10 Olivia Dean** — YT: https://www.youtube.com/channel/UCT3cEUoL1X0_BxN6q7LVH1w · Docs: youtube.com/shorts/5qZ02LjsRx4 (How I wrote Man I Need)
- **11 Tessa Violet** — YT: https://www.youtube.com/channel/UCOw4v1j3QnzH7X4krQAS7fg · Docs: coupdemainmagazine.com/tessa-violet/15439 (first-line-first process)
- **12 Jack Harlow** — YT: https://www.youtube.com/channel/UC6vZl7Qj7JglLDmN_7Or-ZQ · Docs: songexploder.net/jack-harlow (ep. 311)
- **13 Gracie Abrams** — YT: https://www.youtube.com/gracieabrams · Docs: songexploder.net/gracie-abrams (ep. 283, voice memos)
- **14 Raye** — YT: https://www.youtube.com/channel/UCw5z_dopYnvEL6Rc8KNKsnw · Docs: songexploder.net/raye (ep. 264, Escapism demo-to-final)
- **15 Billie Eilish** — YT: https://www.youtube.com/@billieeilish · Docs: songexploder.net/billie-eilish (ep. 197)
- **16 Lizzo** — YT: https://www.youtube.com/@LizzoMusic · Docs: songexploder.net/lizzo (ep. 291, demos); billboard.com/music/rb-hip-hop/lizzo-truth-hurts-breakdown-video-8530765/
- **17 Denzel Curry** — YT: https://www.youtube.com/channel/UCiKxNv_MHAShqT2lATxG_Wg · Docs: songexploder.net/denzel-curry (ep. 164)
- **18 J. Cole** — YT: https://www.youtube.com/@JColeNC · Docs: youtu.be/135bv6GhD2M (Applying Pressure documentary)
- **19 Porter Robinson** — YT: https://www.youtube.com/channel/UCKKKYE55BVswHgKihx5YXew · Docs: papermag.com/porter-robinson-nurture (lyric craft interview)
- **20 Laufey** — YT: https://www.youtube.com/@laufey · Docs: songexploder.net Laufey ep. 259 transcript (From The Start breakdown)
- **21 Maggie Rogers** — YT: https://www.youtube.com/@maggierogers · Docs: songexploder.net/maggie-rogers (ep. 115 + transcript)
- **22 HALIENE** — YT: https://www.youtube.com/@HALIENEmusic · SC: https://soundcloud.com/halienemusic · Docs: edmidentity.com/2017/07/22/depth-interview-haliene/ (Saving Light written in 55 min)
- **23 Ryan S. Jhun** — Docs: nocutnews.co.kr/news/5267922 (7-element recipe); billboard.com/music/music-news/k-pop-dr-ryan-jhun-stories-behind-hits-7423151/
- **24 Toby Gad** — YT: https://www.youtube.com/@songsyouknowpodcast · SC: https://soundcloud.com/tobygadmusic · Docs: musicconnection.com/songwriter-profile-toby-gad-self-led/
- **25 Ross Golan** — YT: https://www.youtube.com/@AndTheWriterIs · Docs: shows.acast.com/andthewriteris; billboard.com/music/pop/ross-golan-songwriter-podcast-interview-7751609/
- **26 Nicolle Galyon** — Docs: americansongwriter.com/songwriters-column-friendships-and-relationships-spark-intros-to-nicolle-galyons-songs/
- **27 Brent Baxter** — Docs: manvsrow.com/2014/08/31/the-story-behind-monday-morning-church/ (draft-to-hit timeline); manvsrow.com/2015/08/31/let-your-title-write-your-song/
- **28 ADORA** — YT: https://www.youtube.com/channel/UC8QgG_-2Uz_1PFOFBMYVyPg · Docs: youtu.be/UKiL645zsT8 (making-of series)

## Deferred (7 — considered, cut for Phase 0)

| Name | Reason deferred |
|---|---|
| Lorde | Slow release cadence — likely fails 3 releases/24mo (agent flagged); recheck only if shortfall |
| Dua Lipa | Thin process doc (one co-write episode, production-leaning); mega-star co-write model |
| Sabrina Carpenter | Thin process doc; co-write episode only |
| Lady Gaga | Co-write process doc, less lyric-craft focused; mega-star |
| Jason Blume | Credits 20+ years old (Britney Dear Diary era); documentation is books, not link-verifiable process content |
| Ed Bell | Tier 3 theatre/film writer — no viral song content |
| Cole Mize | Tier 3; own releases unverified below 100k |

## 0.5 Cheap pre-screening results (run 2026-08-13, hand-verified commands)

YouTube cheap flow: `yt-dlp --flat-playlist -J "<channel>/videos"` (views only). SoundCloud: `yt-dlp --flat-playlist -J "https://soundcloud.com/<h>"` (track list). Tier-2: `ytsearch1` on credited song's official upload. Raw JSON in `b0ttsagent/temp/lyricscreen/`.

| # | Name | Tier | Channel entries | Videos ≥100k | Max views | Notes |
|---|---|---|---|---|---|---|
| 01 | Charlie Puth | 1 | 154 | 154 | 3.5B | SC: 150 tracks ✓ |
| 02 | Mike Shinoda | 1 | 184 | 81 | 14M | |
| 03 | Jon Bellion | 1 | 91 | 63 | 242M | |
| 04 | AJR | 1 | 167 | 140 | 285M | |
| 05 | Logic | 1 | 325 | 193 | 466M | |
| 06 | Russ | 1 | 327 | 295 | 480M | |
| 07 | Hanumankind | 1 | 17 | 17 | 312M | all uploads ≥100k |
| 08 | mgk | 1 | 436 | 413 | 545M | doc thin |
| 09 | San Holo | 1 | 331 | 99 | 4.9M | SC: 943 tracks ✓ |
| 10 | Olivia Dean | 1 | 108 | 82 | 107M | |
| 11 | Tessa Violet | 1 | 151 | 97 | 113M | |
| 12 | Jack Harlow | 1 | 129 | 126 | 354M | |
| 13 | Gracie Abrams | 1 | 137 | 132 | 73M | |
| 14 | Raye | 1 | 123 | 105 | 277M | |
| 15 | Billie Eilish | 1 | 264 | 264 | 2.4B | |
| 16 | Lizzo | 1 | 156 | 110 | 333M | corrected channel (Lizzo Music, 3.07M subs) |
| 17 | Denzel Curry | 1 | 196 | 140 | 111M | |
| 18 | J. Cole | 1 | 30 | 30 | 359M | corrected channel (all 30 ≥100k) |
| 19 | Porter Robinson | 1 | 132 | 112 | 91M | |
| 20 | Laufey | 1 | 214 | 204 | 150M | |
| 21 | Maggie Rogers | 1 | 115 | 65 | 26M | fallback-resolved, official |
| 22 | HALIENE | 1 | 39 | 8 | 788k | own channel confirmed; SC: 147 tracks ✓; weakest cheap signal |
| 23 | Ryan S. Jhun | 2 | — | — | — | credit: IVE 'ELEVEN' MV 265M ✓ (STARSHIP, 2021-12-01) |
| 24 | Toby Gad | 2 | — | — | — | credit: John Legend 'All of Me' 2.71B ✓; SC: 9 tracks ✓ |
| 25 | Ross Golan | 2 | — | — | — | credit: Ariana Grande 'Dangerous Woman' 779M ✓ |
| 26 | Nicolle Galyon | 2 | — | — | — | credit: Dan + Shay 'Tequila' 164M ✓ |
| 27 | Brent Baxter | 2 | — | — | — | credit: Alan Jackson 'Monday Morning Church' 1.03M ✓ |
| 28 | ADORA | 2 | — | — | — | credit: BTS 'Spring Day' 574M ✓ (HYBE, 2017-02-12) |

Screening gotchas handled: Lizzo + J. Cole handles resolved to wrong channels — re-resolved via ytsearch1 (correct channel URLs in the rows above). Flat-playlist `timestamp` is empty on yt-dlp 2026.07.04 → 24-month cadence dates deferred to Phase 1 dated-listing command. Tier-2 credit checks confirm each has ≥1 credited song ≥100k on an official upload (full credit verification via Discogs/ASCAP is Phase 1).

## 0.6 Shortlist — 24 candidates (≥15 required; attrition buffer over 10)

Ranked by cheap signal (videos ≥100k on own channel) combined with process-doc depth. Tier 2 shortlisted on credit evidence + doc depth. All shortlist rows carry 0.5 evidence above.

| Shortlist rank | # | Name | Tier | Why shortlisted |
|---|---|---|---|---|
| 1 | 06 | Russ | 1 | 295 ≥100k videos, step-by-step creation docs, primary genre (hip-hop) |
| 2 | 05 | Logic | 1 | 193 ≥100k, feature-length process documentaries, primary genre |
| 3 | 18 | J. Cole | 1 | 30/30 ≥100k, Applying Pressure doc (writing drills), primary genre |
| 4 | 01 | Charlie Puth | 1 | 154 ≥100k, own course + real-time hit-writing videos, primary genre |
| 5 | 15 | Billie Eilish | 1 | 264 ≥100k, SE ep. 197 with writing voice memos, primary genre |
| 6 | 12 | Jack Harlow | 1 | 126 ≥100k, SE ep. 311 approach-change breakdown, primary genre |
| 7 | 04 | AJR | 1 | 140 ≥100k, filmed living-room writing process, primary genre |
| 8 | 17 | Denzel Curry | 1 | 140 ≥100k, SE ep. 164 lyric-driven breakdown, primary genre |
| 9 | 16 | Lizzo | 1 | 110 ≥100k, SE ep. 291 demos-to-final + Truth Hurts breakdown |
| 10 | 20 | Laufey | 1 | 204 ≥100k, SE ep. 259 full transcript, secondary genre (jazz-pop) |
| 11 | 13 | Gracie Abrams | 1 | 132 ≥100k, SE ep. 283 raw voice memos, primary genre |
| 12 | 14 | Raye | 1 | 105 ≥100k, SE ep. 264 demo-to-final + songwriter-for-hire history |
| 13 | 11 | Tessa Violet | 1 | 97 ≥100k, repeated first-line-first process interviews |
| 14 | 10 | Olivia Dean | 1 | 82 ≥100k, how-I-wrote interview series, primary genre |
| 15 | 19 | Porter Robinson | 1 | 112 ≥100k, documented lyric-craft building, secondary genre (EDM) |
| 16 | 02 | Mike Shinoda | 1 | 81 ≥100k, behind-the-song videos + Tim Ferriss deep dive |
| 17 | 03 | Jon Bellion | 1 | 63 ≥100k, making-of lyric-genesis videos, primary genre |
| 18 | 21 | Maggie Rogers | 1 | 65 ≥100k, SE ep. 115 full transcript |
| 19 | 24 | Toby Gad | 2 | All of Me 2.71B credit; chorus-first workflow docs + own podcast |
| 20 | 25 | Ross Golan | 2 | Dangerous Woman 779M credit; And The Writer Is… host (~150 deep dives) |
| 21 | 28 | ADORA | 2 | Spring Day 574M credit; own making-of series |
| 22 | 26 | Nicolle Galyon | 2 | Tequila 164M credit; own column + session breakdowns |
| 23 | 23 | Ryan S. Jhun | 2 | ELEVEN 265M credit; 7-element recipe interviews |
| 24 | 27 | Brent Baxter | 2 | Monday Morning Church 1.03M credit; draft-to-hit blog method |

**Backfill (in pool, not shortlisted):** mgk (413 ≥100k but thinnest doc — one Footnotes), Hanumankind (huge but thin doc), San Holo (docs production-leaning), HALIENE (8 ≥100k, weakest numbers). Promotable in Phase 1 wave 3 if attrition demands.

## Phase 0 exit gate status

- [x] Pool file with 28 candidates + one-line eligibility hypothesis each (20–30 required) — PASS
- [x] ≥15 shortlisted with cheap-screened evidence — PASS (24)
- [x] Probe verdict recorded (sub-agents own verification: YES) — PASS
- [x] 0.1 clarifying answers recorded at top — PASS
- **GATE: PASSED.** Phase 0 complete. Do not start Phase 1.
