# Wave 07 Report — Phase 2 Deep-dive

**Date:** 2026-08-29
**Wave goal:** deep-dive for the roster; every shortlisted creator gets `case-studies/<slug>.md` passing the depth gate (every workflow step ≥1 first-party source link; every claim linked; verified-vs-claimed + caveats + contradictions explicit). Exit: DEPTH-PASS or THIN-with-explicit-gap.

**Workers:** 3 × `b0tts-general-agent`, spawned in parallel (single fanout message). All completed on first attempt; no retries required.

## Per-worker status

| # | Creator | Slug | Status | Verdict | Output |
|---|---------|------|--------|---------|--------|
| 1 | MrBeast | mrbeast | done | DEPTH-PASS | `case-studies/mrbeast.md` (50,138 B) |
| 2 | Mark Rober | mark-rober | done | DEPTH-PASS | `case-studies/mark-rober.md` (31,812 B) |
| 3 | Airrack / Eric Decker | airrack | done | DEPTH-PASS | `case-studies/airrack.md` (67,212 B) |

No FAIL-UNKNOWN, no retries.

## Verdicts & evidence

- **mrbeast** — DEPTH-PASS. First-party depth from 36-page production guide (2024-09-15, INDEPENDENT) + Lex Fridman #351 transcript (2023-01-11). Documents CTR/AVD/AVP, title<50c + thumbnail promise, minute-mark retention architecture (1min/1-3/3-6/back-half with re-engagements), wow factor, formats/stair-stepping, critical components/bottlenecks, replication. Thin only on precise edit cadence and wellness protocol — explicitly flagged, not padded.
- **mark-rober** — DEPTH-PASS. Full first-party corpus read: TED WorkLife 2026-06-02, Colin and Samir 2022-12-07 (72k-char), Video Production Daily 2021-04-03. Covers 15yr/1-per-month cadence, visceral response, treadmill/jogging burnout model, title/thumbnail 1-3 sentence filter, 9-10 parallel year-long builds, general-points→film→story-found-in-edit→intro-last, 200h→10m, Super Mario effect. Verified-vs-claimed (75M→81.6M, 10M-before-quitting, team 100→140) and contradictions explicit. Thin tactics (no retention graph, no CTR/A-B) stated.
- **airrack** — DEPTH-PASS. Two first-party MONETIZED Jon Youshaei interviews (2025-10-14 Comeback 1:44:47; 2025-12-23 Prank Breakdown) transcribed end-to-end via `youtube-transcript` skill. Covers mischief filter, 3-thumb+how pitch, identify&innovate/shoe-swap, buckets/branching 87→99%, A-plot=title, exponential intro, <$10k multipliers, one-day real-cop prank playbook, Claude paper-edit + editors-as-storytellers, humble-era replication. Thin areas (numerical CTR/AVD, cut rhythm) stated and stopped.

## Lead QA checklist

- [x] every expected `case-studies/<slug>.md` exists — 3/3 on disk
- [x] every workflow step carries a source link — spot-grep link density: mrbeast 126 http-links, mark-rober 108, airrack 262. Two sections flagged by automated counter (mark-rober §7, mrbeast §2) were verified as false positives: the zero-link span is only a prose lead-in between a `##` heading and its first `###` subheading; all workflow steps in those sections are densely linked.
- [x] THIN verdicts carry explicit gap statements — N/A (all DEPTH-PASS; thin areas explicitly flagged in each doc)
- [x] doc count in report matches files on disk — 3 report / 3 disk
- [x] FAIL-UNKNOWN workers retried once before recording — none failed

## Anomalies

- None blocking. Minor: automated section-link counter produced two false positives (prose lead-ins before subheadings); manually verified as non-issues.
- All three docs note thin areas (edit cadence / wellness for mrbeast; retention graph & CTR A-B for mark-rober; numerical CTR/AVD & cut rhythm for airrack) — flagged as explicit gaps, not padded.

## Next actions

- Wave 7 complete. All three roster entries exit Phase 2 with DEPTH-PASS.
- Proceed to next wave per orchestrator sequencing (Phase 3 synthesis / cross-creator comparison).
- Optional follow-up: fill the flagged thin areas (edit cadence, retention graphs, CTR A-B) if a later wave targets them.