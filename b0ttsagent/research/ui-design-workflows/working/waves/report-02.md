# Wave 02 Report — Phase 1: Verification (wave 1 of N)

- Wave: 02 · Phase: 1 (verification) · Date: 2026-08-17
- Verification window: 2021-08-17 → 2026-08-17
- Goal: verdict (PASS/REJECT) for 4 candidates — first wave toward ≥12 PASS
- Status: **COMPLETE** — 4/4 candidates verified, **4 PASS / 0 REJECT** (running total: 4 PASS toward ≥12)

## Per-researcher status

| Candidate | Researcher | Status | Route | Verdict | Evidence file |
|-----------|-----------|--------|-------|---------|---------------|
| Adam Wathan | b0tts-researcher (ses_fee16ead8ffez6hqwBRaHe1V2c) | done | usage-stat | PASS | `working/evidence/adam-wathan-2026-08-17.json` |
| shadcn | b0tts-researcher (ses_fee16d79affeCS10WeqzcbrN6d) | done | usage-stat | PASS | `working/evidence/shadcn-2026-08-17.json` |
| Mark Otto | b0tts-researcher (ses_fee16c700ffeWjCzUBnHlF0OSP) | done | usage-stat | PASS | `working/evidence/mark-otto-2026-08-17.json` |
| Curtis Herbert | b0tts-researcher (ses_fee16b36bffewBnICeOG5JOVHX) | done | award | PASS | `working/evidence/curtis-herbert-2026-08-17.json` |

No retries required. All four researchers completed on first attempt.

## Verdict details

| Candidate | Scale evidence (dated figure, tier) | Window | Doc-currency |
|-----------|-------------------------------------|--------|--------------|
| Adam Wathan | npm 85,411,470 dl/wk (2026-08-09→15) + GitHub 97,250 stars (fetch 2026-08-17), T1 | in-window | Blog live (latest post May 2026); 2021 ecommerce post historical (product rebranded Tailwind Plus Mar 2025), design-process posts continue |
| shadcn | GitHub 121,508 stars + npm 6,864,700 dl/wk (2026-08-09→15), fetch 2026-08-17, T1 | in-window | ui.shadcn.com/docs live & current; Vercel guide 2026-07-07 confirms currency |
| Mark Otto | npm 4,144,770 dl/wk (2026-08-09→15) + GitHub 174,607 stars, fetch 2026-08-17, T1 | in-window | Site maintained; blog last post 2024-06-03 (~2 yrs stale) |
| Curtis Herbert | Apple Design Award 2022, Interaction winner (announced 2022-06-01, Apple newsroom), T1 | in-window | Slopes Diaries active 48-post series, latest #46 (2025-06-04) |

All four PASSes individually credited (Wathan: Wikipedia original-author + bylined posts; shadcn: Vercel guide + shadcn.com; Otto: markdotto.com/GitHub/LinkedIn/A List Apart; Herbert: Apple "Behind the Design" names him creator).

## QA checklist results

- [x] All 4 JSONs exist, parse as JSON, all schema keys present (top-level + `scale_evidence` sub-keys) — verified via script; `rejection_reason` is proper `null` on all PASS files
- [x] Every PASS backed by dated figure + tier — all 4 have figure/date/source_url/tier (T1 official APIs or Apple newsroom)
- [x] Every REJECT carries reason + dead ends — N/A (0 REJECTs); all files carry `dead_ends_searched` (2–3 each)
- [x] Verdicts in report match JSONs on disk — 4 PASS / 0 REJECT confirmed against files
- [x] `report-02.md` written with per-researcher status + PASS/REJECT counts + anomalies

## Anomalies

1. **SearXNG flakiness (all 4 researchers)** — `searxng_searxng_web_search` returned empty for attribution queries in every session; all fell back to `websearch` (Exa) per skill routing. No data loss; consistent with wave-01 observation.
2. **Mark Otto — file-write workaround** — researcher had no generic file-write tool in session; used `gsd_gsd_write_state` with the absolute path. File verified on disk, parses cleanly. Benign.
3. **Mark Otto — doc-currency partial staleness** — process blog's last post is 2024-06-03 (~2 yrs old); site itself maintained and still the referenced first-party source. Recorded honestly; does not affect verdict (usage-stat route).
4. **Adam Wathan — doc-currency nuance** — the discovery-row design post (Aug 2021) is historical since the product rebranded to Tailwind Plus (Mar 2025), but Wathan's design-process posts continue on the active blog. Recorded as still-current workflow content.
5. **Curtis Herbert — award credit nuance** — Apple newsroom credits the company (Breakpoint Studio); individual credit confirmed via Apple's own "Behind the Design: Slopes" feature (2022-08-15) naming Herbert "creator and mastermind". Award route accepted on that basis.

## Next actions

1. **Wave 3 (verification)** — verify next candidate batch toward ≥12 PASS (currently 4). Prioritize strongest un-flagged rows from `working/candidates.md` (e.g., Karri Saarinen, Julie Zhuo, Brad Frost, Ethan Marcotte, Frank Chimero, Erika Hall, Tobias Ahlin Bjerrome, Meng To, Ran Segall, Chris Do).
2. **Lane B triage decision (carried from wave 01)** — decide whether engineer-creator rows stay in the candidate pool.
3. **Track PASS total** — 4/12 reached; remaining waves should target ≥8 more PASS with margin for REJECTs.