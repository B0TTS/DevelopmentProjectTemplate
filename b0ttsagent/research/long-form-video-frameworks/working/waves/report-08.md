# Wave 08 Report — Phase 2 Deep-dive

**Date:** 2026-08-29
**Wave goal:** deep-dive for the roster; every shortlisted creator gets `case-studies/<slug>.md` passing the depth gate (every workflow step ≥1 first-party source link; every claim linked; verified-vs-claimed + caveats + contradictions explicit). Exit: DEPTH-PASS or THIN-with-explicit-gap.

## Roster & status

| # | Slug | Creator | Worker | Status | Verdict | Output |
|---|------|---------|--------|--------|---------|--------|
| 4 | veritasium | Derek Muller | b0tts-general-agent | done | DEPTH-PASS | `case-studies/veritasium.md` |
| 5 | drew-gooden | Drew Gooden | b0tts-general-agent | done | DEPTH-PASS | `case-studies/drew-gooden.md` |
| 6 | kurtis-conner | Kurtis Conner | b0tts-general-agent | done | DEPTH-PASS | `case-studies/kurtis-conner.md` |
| 7 | johnny-harris | Johnny Harris | b0tts-general-agent | done | DEPTH-PASS | `case-studies/johnny-harris.md` |

All 4 workers spawned in a single parallel fanout. No worker failed; no retries required; no FAIL-UNKNOWN.

## Verdicts (one-line each)

- **veritasium** — First-party corpus read end-to-end (Fireside Lisbon 2026-02-27, The Future of Veritasium 2025-12-24 via `python -m yt_dlp`). Covers no-intro hook, problem→solution no-thesis structure, promise-based title/thumbnail (ABC test, asteroids anecdote), hand-drawn storyboards + legal/expert check, cadence 40-50h, business evolution ($840→$12k→solo→hiring trap→Electrify cash-for-equity), power-law + experimentation engine. Thin areas (cuts-per-minute, retention-graph doctrine, script SOP) explicitly stopped, not padded.
- **drew-gooden** — Solo workflow replicable from first-party corpus (Padilla 2024-03-08, own essays, WIRED 2022-05-16). Anti-padding ethic and monthly built-in recharge documented. Gaps (hook beyond "hey guy", CTR/AVD, cut cadence, thumbnail iteration) explicitly flagged thin.
- **kurtis-conner** — Two monetized first-party interviews (Colin and Samir 2023-11-07, Anthony Padilla 2023-04-01) plus four recent first-party videos. Covers scripting-over-improv, topic-hate solo hunt, cold-hook, editing-as-writing blocks, thumbnail cottage industry, touring-dominated business. Retention/cut-rhythm/cadence/burnout flagged thin with monetized-as-marketing caveats.
- **johnny-harris** — 86-min Perell interview transcript (81k chars) + team hiring docs + map/animation/composer videos. End-to-end pipeline (4-month claimed, story day→info doc→visual coding→shame→picture lock), packaging/promise, two voices, sacred 9-2 blocks, bottleneck-accept replication. Verified-vs-claimed/contradictions/thin flags explicit.

## Lead QA checklist

- [x] every expected `case-studies/<slug>.md` exists — 4/4 on disk
- [x] every workflow step carries a source link — spot-grep per section: all workflow sections have links; only "Sources" reference lists are link-free (expected). Link counts: veritasium 220, drew-gooden 114, kurtis-conner 163, johnny-harris 175
- [x] THIN verdicts carry explicit gap statements — N/A (all DEPTH-PASS); thin areas flagged explicitly, no padding
- [x] doc count in report matches files on disk — 4 docs, 4 roster entries
- [x] FAIL-UNKNOWN workers retried once — none failed

## Anomalies

- None. All workers completed cleanly on first attempt.

## Next actions

- Wave 08 complete. All 4 roster entries for Phase 2 deep-dive are DEPTH-PASS.
- Proceed to next wave / synthesis phase per orchestrator sequencing.