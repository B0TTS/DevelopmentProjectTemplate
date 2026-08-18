# Wave 08 Report — Phase 2 Depth Docs (wave 2 of 3)

- Research date: 2026-08-17
- Goal: `creators/<Name>.md` for 4 verified designers (ranking #5-8), each passing the depth gate
- Roster: 4 researchers, one designer each, parallel fanout
- Status: **COMPLETE** — 4/4 DEPTH-PASS, 0 DEPTH-REJECT

## Per-researcher status

| # | Designer | Output file | Status | Verdict |
|---|----------|-------------|--------|---------|
| 1 | Lea Verou | `creators/Lea-Verou.md` | done (retried once) | DEPTH-PASS |
| 2 | Steve Schoger | `creators/Steve-Schoger.md` | done (retried once) | DEPTH-PASS |
| 3 | Philipp Stollenmayer | `creators/Philipp-Stollenmayer.md` | done | DEPTH-PASS |
| 4 | Curtis Herbert | `creators/Curtis-Herbert.md` | done | DEPTH-PASS |

**DEPTH-PASS: 4 | DEPTH-REJECT: 0**

## Verdicts (one-line reasons)

- **Lea Verou — PASS.** Named, ordered Hovercar Framework (North Star → Constraints → Compromises + Skateboard→Hovercar shipping spectrum) with two explicit gates (consensus on North Star; user-testing North Star on low-fi prototypes) and iteration loops, corroborated end-to-end by her Context Chips case study and API-design posts.
- **Steve Schoger — PASS.** Ordered workflow anchored in the systematic Refactoring UI book TOC (co-authored with Adam Wathan, both credited) plus named-step video series/talks, with explicit gates/loops ("Supercharge the defaults" finishing gate; "work in cycles" iteration loop) — not listicle-grade tip threads.
- **Philipp Stollenmayer — PASS.** His own design docs (kamibox.de/songofbloom-files, pbj-files), Apple "Behind the Design" + PBJ feature, and Game Developer deep dives yield a named, ordered workflow with an explicit quality gate (the "housewife test") and multiple named iteration loops ("jazz improvisation"; "back to the drawing board"; discard-and-restart). All sources English.
- **Curtis Herbert — PASS.** 32 of 48 Slopes Diaries posts read end-to-end plus Apple "Behind the Design: Slopes" (his own words); named, ordered 10-step workflow with explicit gates (MVP lens, gut-check, "better not more", future-self, 80% polish, A/B/kill-switch/SQL data gates) and concrete v1→v2 iterations. Every step source-linked.

## QA checklist results

- [x] All 4 docs exist with all 4 sections present (verified via section-header scan)
- [x] Every workflow step has a source link (verified per-step block; only intro paragraphs lack links)
- [x] "What Makes It Distinct" is non-generic signature elements (verified for all 4)
- [x] No DEPTH-REJECTs, so no missing reasons (N/A)
- [x] Eligibility Evidence has route + tier + window + currency line + product-type tag + craft/growth tag (verified for all 4)
- [x] `report-08.md` written with per-researcher status + counts + anomalies

## Anomalies

1. **Lea Verou (researcher 1):** Initial run returned an empty result and no output file → retried once by resuming the session; completed on retry. Full "API Design is UI Design" talk transcript was not retrievable (youtubetotranscript 403, tactiq/notegpt/youtube-transcript JS-rendered, timedtext API empty) — noted honestly in the doc; the talk's core content is corroborated by her own blog posts that explicitly reference it.
2. **Steve Schoger (researcher 2):** Initial run returned an empty result and no output file → retried once by resuming the session; completed on retry. No further anomalies reported.
3. **Philipp Stollenmayer:** No GDC talk transcript found (only a Hamburg Games Conference 2020 bio listing); a Medium interview fetch returned 403 — quotes cited from search-indexed content and flagged in the doc.
4. **Curtis Herbert:** SearXNG returned empty for the Apple "Behind the Design" query (fell back to Exa per skill routing, then read the page directly). Post #28 "Constraints" has a slug collision (tag index links to /slopes-diaries/; content verified as #28 by reading). Diaries are heavily business/growth-oriented; workflow reconstructed from recurring named practices across the series, each step source-linked to the specific post.

## Next actions

- Wave 8 complete; all 4 depth docs pass the gate and are ready for downstream synthesis.
- No re-runs required. No DEPTH-REJECTs to remediate.
- Proceed to wave 9 (final depth-doc wave, ranking #9-12) per orchestrator sequencing.
