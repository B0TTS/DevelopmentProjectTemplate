# Phase 1 → Phase 1.5 Working File

## Phase 1 raw pool (22 candidates returned across 3 agents)

### Agent A — Course/blog authors (7)
1. Jenny Hoyos (0.95) — overlaps B
2. Gary Vaynerchuk (0.645) — overlaps B, C
3. Alex Hormozi (0.51) — overlaps B, C
4. That Icelandic Guy (0.43)
5. Edward Sturm (0.39)
6. Keenya Kelly (0.34)
7. Ole Lehmann (0.29)

### Agent B — Podcast regulars (10)
1. MrBeast (1.0) — long-form-first caveat (flagged by agent)
2. Zach King (1.0) — overlaps C
3. Keith Lee (0.975)
4. Dhar Mann (0.975)
5. Airrack (0.95) — long-form-first caveat
6. Steven He (0.925)
7. Jenny Hoyos (0.9) — DUPE with A
8. Nick DiGiovanni (0.875)
9. Caleb Simpson (0.85)
10. Sam Sulek (0.74) — borderline long-form hybrid

### Agent C — Own-channel strategy creators (5)
1. Zach King (1.00) — DUPE with B
2. Peter McKinnon (0.75)
3. Mino Lee (0.58)
4. Ryan Magin (0.375)
5. Hannah Witton (0.35)

## Dedup (merge across agents)
- **Zach King** (surfaced by B + C) — single entry
- **Jenny Hoyos** (surfaced by A + B) — single entry; reconcile dominance scores via yt-dlp
- **Gary Vaynerchuk** (surfaced by A); B cut him for being a host but A keeps him
- **Alex Hormozi** (surfaced by A); B cut him as "clip-repurposer"

## Hard cuts (rule-based, pre-yt-dlp)
- ❌ **That Icelandic Guy** — Activity = 0. Publicly quit TikTok ~2023-24. Fails "hits within 2021–2026 active dominance".
- ❌ **Ole Lehmann** — Career tenure UNVERIFIED (<3 yrs per agent's own admission). hit_rate est. 0.15, well below 0.6 floor.
- ❌ **Edward Sturm** — Estimated hit_rate 0.2 (below 0.6 floor); PARTIAL verification; per-video consistency self-reported only.
- ❌ **Ryan Magin** — Estimated hit_rate 0.4 (below floor); documentation borderline stale (2021–22, "UNCLEAR" per agent).
- ❌ **Hannah Witton** — Estimated hit_rate 0.35; fails consistency (only outliers >100k).
- ❌ **Keenya Kelly** — Estimated hit_rate 0.3 (below floor); fails consistency.
(Minor: That Icelandic Guy also dropped earlier under activity test.)

## Surviving pool for yt-dlp verification (14)
1. Zach King
2. Jenny Hoyos
3. MrBeast
4. Keith Lee
5. Dhar Mann
6. Airrack
7. Steven He
8. Nick DiGiovanni
9. Caleb Simpson
10. Gary Vaynerchuk
11. Sam Sulek
12. Peter McKinnon
13. Alex Hormozi
14. Mino Lee

## Authoritative yt-dlp pulls (Phase 1.5) — IN PROGRESS

### Test batch (first 4 candidates)
| Candidate | Platform | Result | Hit-rate (after 7-day excl.) | Median | Activity | Dominance (recalc) | Notes |
|---|---|---|---|---|---|---|---|
| Zach King | YT Shorts @ZachKing | ✓ 22 rows returned | 20/20=1.0 | ~3.2M | 1.0 | **1.0** | Confirms agent B/C estimate. Healthy v/f ratio. |
| Jenny Hoyos | YT Shorts @JennyHoyos | ✓ 22 rows returned | 20/20=1.0 | ~190k | 1.0 | **0.757** | Agent A's 0.95 was based on 2023-24 peak. Current ~190k/video is far below "10M avg" claim. Channel-size underperformance flag needed re: 12.3M subs (per Agent A asknaveen ref). |
| Mino Lee | TikTok @minolee | ✗ bot-flag | — | — | — | — | TikTok returned 1 scrubbed row (date 2015-11-30, view_count=12). Will retry with chrome cookies, fallback to his YouTube presence. |
| Gary Vee | TikTok @garyvee | ✓ 22 rows mostly <7d | pending wider pull | — | — | — | Need --playlist-end 60+ to fetch ≥7-day-eligible vids. Current week's vids 5k–459k median ~15k — well below 100k on a 15M-follower channel: underperformance concern. |

### Pending batch (next 4 candidates)
- Keith Lee — TikTok @keith_lee125 (primary platform)
- Dhar Mann — YT Shorts @dharmann
- Airrack — YT Shorts @airrack
- Gary Vee — TikTok retry with --playlist-end 60

### Pending batch 2 (post)
- Steven He — YT Shorts @StevenHe
- Nick DiGiovanni — YT Shorts @nickdigiovanni
- Caleb Simpson — TikTok @calebwsimpson
- Sam Sulek — YT Shorts @sam_sulek

### Pending batch 3 (post)
- Peter McKinnon — YT Shorts @PeterMcKinnon
- Alex Hormozi — YT Shorts @AlexHormozi
- Mino Lee — YT (after channel URL lookup via metadata of known video)
- MrBeast — YT Shorts @MrBeast (long-form-first caveat noted)