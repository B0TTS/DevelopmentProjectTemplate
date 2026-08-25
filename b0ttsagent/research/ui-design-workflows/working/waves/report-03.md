# Wave 03 Report — Phase 1: Verification (wave 2 of N)

- Wave: 03 · Phase: 1 (verification) · Date: 2026-08-17
- Verification window: 2021-08-17 → 2026-08-17
- Goal: verdict (PASS/REJECT) for 4 candidates — running pool: 4 PASS, target ≥12
- Status: **COMPLETE** — 4/4 candidates verified, **3 PASS / 1 REJECT** (running total: 7 PASS toward ≥12)

## Per-researcher status

| Candidate | Researcher | Status | Route | Verdict | Evidence file |
|-----------|-----------|--------|-------|---------|---------------|
| Karri Saarinen | b0tts-researcher (ses_feda914b4ffeF5K51O27dhX2LY) | retried (killed mid-wave, respawned) | revenue | REJECT | `working/evidence/karri-saarinen-2026-08-17.json` |
| Ryan McLeod | b0tts-researcher (ses_feda8f6c7ffeZ8cUdKeonwZVeA) | retried (killed mid-wave, respawned) | award | PASS | `working/evidence/ryan-mcleod-2026-08-17.json` |
| Mike Bostock | b0tts-researcher (pre-existing, wave start) | done (first attempt, no re-spawn) | usage-stat | PASS | `working/evidence/mike-bostock-2026-08-17.json` |
| Steve Schoger | b0tts-researcher (pre-existing, wave start) | done (first attempt, no re-spawn) | usage-stat | PASS | `working/evidence/steve-schoger-2026-08-17.json` |

**Mid-wave failure & resume:** Two researchers (Karri Saarinen, Ryan McLeod) stalled and were killed mid-wave; the wave lead also died once. On resume, the two pre-existing JSONs (Bostock, Schoger) passed QA against the spec checklist and were **not** re-spawned. The two missing researchers were respawned in parallel (one message, verbatim task prompts + efficiency line) and both completed. No data loss.

## Verdict details

| Candidate | Scale evidence (dated figure, tier) | Window | Doc-currency |
|-----------|-------------------------------------|--------|--------------|
| Karri Saarinen | REJECT `tier3-only` — no Tier 1/2 revenue/ARR figure findable. Tier 1 press (TechCrunch, Reuters, Forbes) reports funding ($82M Series C @ $1.25B, $35M Series B @ ~$400M), 15,000+ customers, 280% profit growth — but no revenue dollars; Linear's own blog (T2) discloses none. ~$100M ARR appears only in estimate trackers (LATKA, ARR Club, GrowthHunt, Systemaic, whoearns) — excluded as anchors. No MAU ≥1M, no usage-stat (SaaS, not a library), no individually-credited in-window top-tier award (Apple Design Awards 2025 list checked — Linear absent) | in-window (checks 1–2 pass) | Linear design blog current (Saarinen posts through Jun 2026); 2024 redesign post live but historical |
| Ryan McLeod | Apple Design Award 2024, Spatial Computing winner (announced 2024-06-06, Apple newsroom), T1 — individually credited (solo creator, Shapes and Stories LLC) | in-window | Medium @warpling profile 403-blocked (recency UNKNOWN); current first-party design-process doc is the live Apple Developer feature (2024-01-30) |
| Mike Bostock | npm 15,818,249 dl/wk (2026-08-09→15) + GitHub 113,478 stars, fetch 2026-08-17, T1 | in-window | bost.ocks.org/mike live; essays still cited as current (d3js.org joins docs, UW IDL tutorial, Observable Mar 2026 blog Q&A) |
| Steve Schoger | GitHub 23,748 stars (tailwindlabs/heroicons) + npm 2,704,587 dl/wk (@heroicons/react, 2026-08-09→15), fetch 2026-08-17, T1 | in-window | steveschoger.com live, still referenced as his current site in recent content (YesPress 2025-26, tokyn credits) |

All three PASSes individually credited (McLeod: Apple newsroom + Developer feature + press kit; Bostock: D3 creator/designer, NYT Graphics editor; Schoger: Tailwind blog, SmashingConf bio, refactoringui.com). The single REJECT is a clean `tier3-only` miss — attribution and window pass, but no Tier 1/2 scale figure is publicly findable.

## QA checklist results

- [x] All 4 JSONs exist, parse as JSON, all schema keys present (top-level + `scale_evidence` sub-keys) — verified via script; `rejection_reason` is proper `null` on all PASS files
- [x] Every PASS backed by dated figure + tier — all 3 PASS have figure/date/source_url/tier (T1 official APIs or Apple newsroom)
- [x] Every REJECT carries reason + dead ends — Karri Saarinen REJECT has full reason + 9 dead ends logged
- [x] Verdicts in report match JSONs on disk — 3 PASS / 1 REJECT confirmed against files
- [x] `report-03.md` written with per-researcher status + PASS/REJECT counts + anomalies

## Anomalies

1. **Mid-wave failure (2 researchers + lead)** — Karri Saarinen and Ryan McLeod researchers stalled and were killed; the wave lead died once mid-wave. Resolved on resume: pre-existing JSONs QA'd (no re-spawn), missing researchers respawned in parallel and completed. No data loss; all 4 files on disk.
2. **SearXNG flakiness (consistent with prior waves)** — `searxng_searxng_web_search` returned empty for attribution queries; researchers fell back to `websearch` (Exa) per skill routing. No data loss.
3. **Karri Saarinen — clean tier3-only REJECT** — strong individual attribution and in-window evidence, but no Tier 1/2 scale figure publicly findable; ~$100M ARR only in estimate trackers (excluded as anchors). Not a data gap; standard rejection.
4. **Ryan McLeod — doc-currency UNKNOWN for Medium** — @warpling profile 403-blocked; substituted live Apple Developer feature (2024-01-30) as current first-party design-process doc. Award route unaffected.
5. **Ryan McLeod — out-of-window evidence ignored correctly** — 2017 Apple Design Award (out-of-window) and 14M+ players (self-disclosed T3) not used; the in-window 2024 Apple Design Award carries the PASS.

## Next actions

1. **Wave 4 (verification)** — verify next candidate batch toward ≥12 PASS (currently 7). Prioritize strongest un-flagged rows from `working/candidates.md` (e.g., Julie Zhuo, Brad Frost, Ethan Marcotte, Frank Chimero, Erika Hall, Tobias Ahlin Bjerrome, Meng To, Ran Segall, Chris Do).
2. **Track PASS total** — 7/12 reached; remaining waves should target ≥5 more PASS with margin for REJECTs.
3. **Lane B triage decision (carried from wave 01)** — decide whether engineer-creator rows stay in the candidate pool.
