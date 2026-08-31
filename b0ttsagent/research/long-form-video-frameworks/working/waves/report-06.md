# Wave 06 Report — Phase 1 Verification (wave 5 of N)

**Date:** 2026-08-29
**Wave goal:** verify 4 candidates (Dan Koe, Linus Tech Tips, Airrack, Mina Le) under the strict wave-02 protocol.
**Workers:** 4 × `b0tts-general-agent` (shell access for yt-dlp), spawned in parallel in one message.

## Per-worker status

| Candidate | Slug | Verdict | JSON path | One-line reason |
|---|---|---|---|---|
| Dan Koe | dan-koe | **REJECT** | `working/evidence/dan-koe-2026-08-29.json` | Consistency FAIL — 7/12 eligible (58.3%) >100k, median 111k, dominance 0.38; gate not lowered. |
| Linus Tech Tips | linus-tech-tips | **PASS** | `working/evidence/linus-tech-tips-2026-08-29.json` | 12/12 (100%) >100k, median 1,004,889, dominance 0.55; first-party forum doc 2021-06-03 in window. |
| Airrack | airrack | **PASS** | `working/evidence/airrack-2026-08-29.json` | 12/12 (100%) >100k, median 9.89M, dominance 0.894; first-party 2025 Comeback interview. |
| Mina Le | mina-le | **PASS** | `working/evidence/mina-le-2026-08-29.json` | 12/12 (100%) >100k, median 530k, dominance 0.527; WaPo Creator Q+A 2026-05-06 as workflow doc. |

## Lead QA checklist

- [x] all 4 `working/evidence/*.json` exist (airrack, dan-koe, linus-tech-tips, mina-le)
- [x] every PASS JSON contains hit_rate, median_views, dominance inputs + arithmetic
- [x] counts came from `python -m yt_dlp` pulls, not aggregator estimates — all per_video counts are exact integers; dead_ends confirm per-video watch-page pulls with flat-vs-per-video drift <0.3%; no estimate-grade counts found
- [x] every REJECT JSON contains rejection_reason and dead_ends_searched (dan-koe: reason + 8 dead-ends)
- [x] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN — N/A (no worker failed)

No re-runs required. All 4 workers completed on first attempt.

## Dominance scores (PASSes)

- Airrack: **0.894** (hit_rate 1.0, magnitude 0.989, activity 0.5)
- Linus Tech Tips: **0.55** (hit_rate 1.0, magnitude 0.100, activity 1.0)
- Mina Le: **0.527** (hit_rate 1.0, magnitude 0.053, activity 1.0)

## Anomalies

- **Airrack doc provenance nuance:** primary doc `wtMudMODlWU` is hosted on Jon Youshaei's channel (not Airrack's), but Eric Decker is the interview guest explaining his own workflow — worker classified FIRST-PARTY via creator voice. Flagged for orchestrator awareness; not a gate failure.
- **Linus Tech Tips:** 8 members-only videos in the recent window have no view counts via yt-dlp and were excluded from the eligible pool/denominator. 12/12 of the eligible long-forms still clear 100k. Note for shortlist: median is just above 1M (1,004,889).
- **Dan Koe:** documentation PASS (Nov 2025 YouTube Workflow letter) but consistency gate blocks PASS — borderline, correctly not lowered. No Wikipedia page (dead end confirmed).
- **Mina Le:** no on-channel "how I make my videos" video exists (100-title scan confirmed); workflow doc is a SECOND-HAND-framed interview (WaPo Q+A) classified FIRST-PARTY by creator voice. Flagged.

## Next actions

- **Run-wide PASS count:** 14 banked before this wave + 3 new PASS = **17 PASS total**, exceeding the preferred target of 15. Cap the shortlist at 15 — orchestrator must decide which PASSes to drop/rank (Airrack 0.894 is the strongest new anchor; Linus 0.55 and Mina Le 0.527 are mid-tier).
- Dan Koe is REJECTED — remove from shortlist consideration.
- No further verification waves strictly required for the 15-cap unless orchestrator wants to replace a weaker PASS; otherwise proceed to shortlist ranking / next phase.