# Wave 06 Report — Phase 1 Verification (wave 5 of N)

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, parallel fanout (R1–R4 = fresh)
- Status: **COMPLETE** — 3/4 researchers done, 1 failed (FAIL-UNKNOWN), 4 retried once (initial fanout returned empty outputs wave-wide; retry recovered 3/4)
- Verdicts: **1 PASS / 2 REJECT / 1 FAIL-UNKNOWN** (running pool: 11 PASS → 12 PASS after this wave; target ≥12 **MET**)

## Per-researcher status

| # | Candidate | Status | Verdict | Output file |
|---|-----------|--------|---------|-------------|
| R1 | Sindre Sorhus | fail (FAIL-UNKNOWN) | — | `working/evidence/sindre-sorhus-2026-08-17.json` — **MISSING** |
| R2 | Zach Gage | done (retried) | REJECT | `working/evidence/zach-gage-2026-08-17.json` |
| R3 | Michael Flarup | done (retried) | REJECT | `working/evidence/michael-flarup-2026-08-17.json` |
| R4 | Philipp Stollenmayer | done (retried) | PASS | `working/evidence/philipp-stollenmayer-2026-08-17.json` |

## Verdicts & rationale

- **R2 — Zach Gage: REJECT** (`no qualifying in-window award`). Knotwords was an Apple Design Award 2023 **finalist** (Delight & Fun) — confirmed on Apple's official page (T1), credited to Gage & Schlesinger — but finalist ≠ winner and does not count. ADA winner lists 2021–2026 and Webby puzzle/games categories 2022–2026 contain no Gage product. Puzzmo's self-disclosed "Apple Design Award Winner" claim is Tier 3 and out-of-window; Playlin Awards runner-up is non-qualifying. No Tier 1/2 MAU/revenue for Puzzmo/Good Sudoku. Attribution PASS; scale fails.
- **R3 — Michael Flarup: REJECT** (`tier3-only`). Only scale figure is Thermo "more than 5 million users" — self-disclosed by Flarup in a 2015 Maker Hunt AMA (Tier 3, out-of-window). No independent Tier 1/2 press or App Store corroboration of ≥1M users in-window; AppStorio (~246k monthly downloads) is an estimate tracker (corroborate-only); Robocat's Thermo (id414215658) is delisted (404). Oko's 2024 ADA goes to the AYES team — Flarup only designed its icon, so no qualifying in-window award individually credited. Doc-currency: 2017 process article still live, republished via Smashing/Apply Pixels/Software Times (2021), no 2022+ citations.
- **R4 — Philipp Stollenmayer: PASS**. Song of Bloom's ADA 2020 was out-of-window, but **PBJ - The Musical won the Apple Design Award 2025 (Innovation, Games), credited individually to "Philipp Stollenmayer, Germany"** on Apple's official ADA 2025 page (T1), announced 2025-06-03 — in-window. All 4 checks pass. Doc-currency: kamibox.de/songofbloom-files live and current as of 2026-08-17; site actively maintained (PBJ released Mar 2025).

## QA checklist results

- [x] 3/4 JSONs exist, parse as JSON, all schema keys present (verified via parse; R1 file missing)
- [x] Every PASS backed by dated figure + tier (R4: ADA 2025-06-03, T1)
- [x] Every REJECT carries reason + dead ends (R2: 6, R3: 4)
- [x] Verdicts in report match JSONs on disk
- [x] report-06.md has per-researcher status + PASS/REJECT counts + anomalies

## Anomalies

1. **R1 Sindre Sorhus — FAIL-UNKNOWN.** Initial parallel fanout returned empty summaries and no output files for all 4 researchers (wave-wide tooling failure). Retried all 4 once via session resume; 3 recovered and wrote valid JSONs, R1 returned empty a second time with no file on disk. Per failure-handling rules, recorded FAIL-UNKNOWN and moved on — **no evidence JSON for Sindre Sorhus exists**; his candidate remains unverified.
2. **Encoding artifacts** in R2/R3 JSONs: em-dashes rendered as replacement chars (`�?`) in `scale_evidence.figure` / `doc_currency` strings. Cosmetic only — does not affect schema, parsing, or verdicts. Optional cleanup.
3. **R2 window_5yr = "in-window"** despite REJECT — consistent (finalist evidence is 2023, in-window; scale not met). Not an error.
4. **R3 window_5yr = "out-of-window"** — consistent with the 2015 claim date and no in-window corroboration. Not an error.

## Next actions

- **Pool target MET**: running pool is 12 PASS (net +1 this wave: +1 PASS Philipp Stollenmayer, +2 REJECT, +1 unverified). Target ≥12 satisfied.
- **R1 Sindre Sorhus**: re-run verification in a later wave (or accept as unverified) — his chalk usage-stat route (npm/GitHub live API) is high-confidence PASS if completed; recommend a targeted re-run to close the gap.
- Optional: fix em-dash encoding in R2/R3 JSONs during a later cleanup pass.
