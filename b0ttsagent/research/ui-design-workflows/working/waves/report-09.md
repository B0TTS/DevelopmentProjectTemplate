# Wave 09 Report — Phase 2 Depth Docs (wave 3 of 3)

- Research date: 2026-08-17
- Goal: `creators/<Name>.md` for the final 4 verified designers (ranking #9-12), each passing the depth gate
- Roster: 4 researchers, one designer each, parallel fanout
- Status: **COMPLETE** — 4/4 DEPTH-PASS, 0 DEPTH-REJECT
- **Process note: the wave lead died mid-wave after 3/4 researchers completed (Stoiber, Palmer, Prangley). Ryan McLeod (researcher 1) was completed via direct orchestrator respawn, DEPTH-PASS.** This report was written by the Phase 2 lead (END QA), completing the wave-09 record.

## Per-researcher status

| # | Designer | Output file | Status | Verdict |
|---|----------|-------------|--------|---------|
| 1 | Ryan McLeod | `creators/Ryan-McLeod.md` | lead died mid-run → completed via direct orchestrator respawn | DEPTH-PASS |
| 2 | Max Stoiber | `creators/Max-Stoiber.md` | done | DEPTH-PASS |
| 3 | Jared Palmer | `creators/Jared-Palmer.md` | done | DEPTH-PASS |
| 4 | Charli Marie Prangley | `creators/Charli-Marie-Prangley.md` | done | DEPTH-PASS |

**DEPTH-PASS: 4 | DEPTH-REJECT: 0**

## Verdicts (one-line reasons)

- **Ryan McLeod — PASS.** Named, ordered challenge-design loop (constraint → "castle with a moat" interface → playtest → red-herring removal → ship gate → analytics loop) with explicit gates ("observable change" test, "perfection is the enemy of good" shipping gate), anchored on the Apple Developer feature and the Going Indie transcript (his words). Port variant (Blackbox for Vision) documented separately with its own ordered steps.
- **Max Stoiber — PASS.** Named taste workflow ("get parts on the table → dissect the greats → iterate") with the explicit "make it work, make it right, make it fast" ordering gate, proven by the first-party styled-components API case study (five prior-knowledge pieces → three breakthroughs).
- **Jared Palmer — PASS.** Two ordered workflows: the generative-UI loop (describe → generate → select iteration → edit → copy-paste) and his designer-era prototyping loop (Photoshop → Framer → handoff before build), with the named "no slop" quality gate. Phase-1 thin-source flag resolved via Madrona + Latent Space first-party interviews.
- **Charli Marie Prangley — PASS.** Named, ordered marketing-site workflow (content outline before design → grey-box wireframes + Crazy 8's → "sleep on it" gate → ship → measure loop), source-linked to CharliMarieTV, Inside Marketing Design, and Kit-rebrand interviews. Depth rests on first-party process content, per the Phase-1 flag.

## QA checklist results (Phase 2 lead, END QA)

- [x] All 4 docs exist with all 4 sections present (verified via section-header scan of all 12 `creators/*.md`)
- [x] Every workflow step has a source link — steps are grouped under subsection-level source links; only intro/transition paragraphs lack links (same acceptance standard as report-08)
- [x] "What Makes It Distinct" is non-generic signature elements (verified for all 4)
- [x] No DEPTH-REJECTs, so no missing reasons (N/A)
- [x] Eligibility Evidence has route + tier + window + currency line + product-type tag + craft/growth tag (verified via targeted scan, all 4 present)
- [x] `report-09.md` written with per-researcher status + counts + anomalies

## Anomalies

1. **Wave lead death (process).** Lead died mid-wave after 3/4 researchers completed. Ryan McLeod completed via direct orchestrator respawn using the wave-09 spec's first-party leads; DEPTH-PASS with no researcher context lost. No other researchers affected.
2. **Ryan McLeod — bare-label sources.** 9 in-workflow citations use the bare label "Source: Going Indie transcript" without a URL (the full URL appears once, in Sources). Links resolvable; style inconsistent — carried to Phase 3 as the bare-URL source-style flag.
3. **Encoding display artifacts.** All creator docs on disk are UTF-8 clean (verified byte-level; zero U+FFFD). Em-dashes/arrows display as mojibake through non-UTF-8 readers (e.g., PowerShell 5.1 default ANSI decode). Carried to Phase 3 — synthesis must read files as UTF-8; files do not need fixing.
4. **Max Stoiber — single-anchor depth.** Shortest PASS doc (10.5 KB); the core workflow rests largely on one "taste" note. Distinct section verified non-generic, but Phase 3 should treat claims citing only that note as single-anchor.

## Next actions

- Wave 09 complete; Phase 2 complete at 11 DEPTH-PASS / 1 DEPTH-REJECT (shadcn).
- No re-runs; no replenishment needed (11 >= floor 10).
- Proceed to Phase 3 synthesis per orchestrator sequencing.
