# Wave 05 Report — Phase 1 Verification (wave 4 of N)

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, parallel fanout (R1 = re-check, R2–R4 = fresh)
- Status: **COMPLETE** — 4/4 researchers done, 0 failed, 0 retried
- Verdicts: **1 PASS / 3 REJECT** (running pool: 11 PASS → 11 PASS after this wave; target ≥12 NOT met)

## Per-researcher status

| # | Candidate | Status | Verdict | Output file |
|---|-----------|--------|---------|-------------|
| R1 | Tobias Ahlin Bjerrome (re-check) | done | REJECT | `working/evidence/tobias-ahlin-bjerrome-2026-08-17.json` (edited in place) |
| R2 | Jared Palmer | done | PASS | `working/evidence/jared-palmer-2026-08-17.json` |
| R3 | Mike Kus | done | REJECT | `working/evidence/mike-kus-2026-08-17.json` |
| R4 | Matt Perry | done | REJECT | `working/evidence/matt-perry-2026-08-17.json` |

## Verdicts & rationale

- **R1 — Tobias Ahlin Bjerrome: REJECT** (`scale-not-met: cumulative users only, no public MAU`). No public GitHub Copilot MAU exists. Microsoft FY2026 Q1 (Oct 29 2025) discloses "over 26 million users" (cumulative, official transcript, T1); TechCrunch (2025-07-30) frames 20M as "all-time users." The only MAU Microsoft discloses (150M) is the combined first-party Copilot family, not GitHub Copilot. Individual design credit CONFIRMED (X bio "Designing Copilot and Mona Sans @GitHub"; Future Product Days 2026 / Nordic.js 2025 "Principal Design Engineer working on GitHub Copilot") — but scale check fails first. Prior PASS flipped to REJECT per spec.
- **R2 — Jared Palmer: PASS**. Attribution: Formik README "Authors" lists Palmer first; designer credentials via The Palmer Group ("strategy, design, and engineering firm"), Dribbble presence, 🎨 credit in all-contributors. Scale (usage-stat, T1 official APIs): npm formik 3,844,046 downloads/wk (2026-08-09→15); GitHub 34,325 stars (fetched 2026-08-17). Both exceed the ≥1M/wk and ≥20k stars bars. Doc-currency: 2018 blog post still live and listed as top resource on formik.org/docs/resources.
- **R3 — Mike Kus: REJECT** (`scale-not-met`). Official Awwwards profile (T1) shows SOTM: 0 — contradicts the self-listed "1x Site of the Month" on mikekus.com/about. All 5 SOTDs are 2010–2014 (out of window; SOTD excluded anyway). In-window awards are only Honor Mentions (Kus-Studio 2025, Just Phil 2026), which don't qualify. No FWA profile (404), no CSSDA WOTY. Doc-currency: current (mikekus.com actively maintained).
- **R4 — Matt Perry: REJECT** (`attribution`). Check 1 fails: all public credit is engineering — "creator of Motion" / "software engineer at Framer" / "Senior Software Engineer - Framer" (motion.dev/about, GitHub, LinkedIn, X, oss.institute, devtools.fm, syntax.fm). No third-party source credits him as a designer on a shipped design tool; designer background is self-disclosed (Tier 3) only. Per spec, purely-engineering credit → REJECT on attribution despite scale (npm framer-motion 37,531,096/wk; GitHub 33,268 stars, both T1).

## QA checklist results

- [x] All 4 JSONs exist, parse as JSON, all schema keys present (verified via parse)
- [x] Every PASS backed by dated figure + tier (R2: fetch date 2026-08-17, T1)
- [x] Every REJECT carries reason + dead ends (R1: 10, R3: 11, R4: 5)
- [x] R1's update: verdict flipped to REJECT with reason `scale-not-met: cumulative users only, no public MAU` (one of the two allowed outcomes)
- [x] Verdicts in report match JSONs on disk
- [x] report-05.md has per-researcher status + PASS/REJECT counts + anomalies

## Anomalies

1. **Encoding artifacts** in R1 and R3 JSONs: em-dashes rendered as replacement chars (`�?`) in `scale_evidence.figure` / `doc_currency` strings. Cosmetic only — does not affect schema, parsing, or verdicts. Optional cleanup.
2. **R1 window_5yr = "in-window"** despite REJECT — consistent (evidence is in-window; scale not met). Not an error.
3. **R3 window_5yr = "out-of-window"** — consistent with no in-window qualifying award. Not an error.
4. Evidence directory is untracked in git (no baseline to diff R1's in-place edit against); R1's edit verified via file state + researcher summary (dead_ends preserved, 6 appended → 10 total).

## Next actions

- **Pool shortfall**: running pool is 11 PASS (1 flagged→REJECT this wave, +1 new PASS = net 0). Target ≥12 not met → schedule Wave 06 with fresh candidates (recommend 2–3 new dev-tools/agency-lane candidates to close the gap).
- Flag R1 (Tobias Ahlin Bjerrome) as REJECTED in the pool; remove from PASS count.
- Optional: fix em-dash encoding in R1/R3 JSONs during a later cleanup pass.
