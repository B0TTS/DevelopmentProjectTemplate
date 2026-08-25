# INDEX — ui-design-workflows research run

- **Research date:** 2026-08-17
- **Verification window:** 2021-08-17 → 2026-08-17
- Pipeline: 44 candidates (Phase 0) → 12 verified PASS (Phase 1) → 11 depth docs (Phase 2) → synthesis (Phase 3, `SYNTHESIS.md`)
- Full per-designer depth: `creators/<Name>.md` · wave records: `working/waves/`

## Ranked creators (11 verified, DEPTH-PASS)

Ranked on: (1) verification strength — evidence route (MAU/revenue > usage-stat > award), scale margin above the bar, attribution solidity; (2) documentation depth / structural completeness; (3) workflow specificity / transferability. Ratings are 1–5 stars for doc depth and workflow specificity.

| Rank | Creator | Product(s) | Route | Verif. tier | Doc depth | Workflow specificity | Why this rank |
|---|---|---|---|---|---|---|---|
| 1 | Adam Wathan | Tailwind CSS, Tailwind UI | usage-stat: npm 85.4M/wk (~85× bar) + 97.3k GH stars | T1 | ★★★★★ | ★★★★★ | Largest scale margin in the set, unambiguous individual credit, and the richest process corpus (book + flagship post + build log + talk) with named loops and gates. |
| 2 | Mark Otto | Bootstrap | usage-stat: npm 4.1M/wk + 174.6k GH stars | T1 | ★★★★★ | ★★★★☆ | Canonical creator credit and a named 4-stage process stated verbatim and re-run across 13 years (2011→2024); slightly framework-general. |
| 3 | Mike Bostock | D3.js, Observable | usage-stat: npm 15.8M/wk + 113.5k GH stars | T1 | ★★★★★ | ★★★★☆ | Official docs still cite his essays as current; a fully named search process with unique gates; viz-specific but the search/annealing frame transfers. |
| 4 | Lea Verou | Prism.js, Color.js, Mavo | usage-stat: npm 24.0M/wk (stars below bar; OR satisfied via npm) | T1 | ★★★★★ | ★★★★★ | Designer-credential judgment call (standards roles), but the Hovercar Framework is the most explicitly transferable named method in the set, with a full end-to-end case study. |
| 5 | Steve Schoger | Heroicons, Tailwind UI, Refactoring UI | usage-stat: npm 2.7M/wk + 23.7k GH stars (stars just above bar) | T1 | ★★★★☆ | ★★★★★ | Joint authorship (book with Wathan) but solid visual-designer credit; the book-TOC-as-workflow is maximally concrete, though book text itself is paywalled. |
| 6 | Philipp Stollenmayer | Kamibox games (Song of Bloom, ZIP ZAP, PBJ) | award: Apple Design Award 2025 Innovation, individually credited | T1 | ★★★★☆ | ★★★☆☆ | Individually credited top-tier award and rich first-party design docs; game-specific (housewife test, physical-first pipeline) but the named gates transfer. |
| 7 | Curtis Herbert | Slopes | award: Apple Design Award 2022 Interaction; individual credit via Apple feature | T1 | ★★★★★ | ★★★★☆ | The deepest documentation in the set (48-post diaries, 32 read end-to-end); workflow is app-and-season-specific but every gate is named and transferable. |
| 8 | Ryan McLeod | Blackbox, Blackbox for Vision | award: Apple Design Award 2024 Spatial Computing | T1 | ★★★★☆ | ★★★★☆ | Individually credited one-man studio; named loop + gates are crisp; Medium recency UNKNOWN (bot-blocked, read via archives) docks doc depth. |
| 9 | Max Stoiber | styled-components | usage-stat: npm 9.4M/wk + 41.1k GH stars | T1 | ★★★☆☆ | ★★★★☆ | Co-creator credit (with Glen Maddern) and designer-credential judgment call; the taste workflow + work/right/fast gate are strong but single-anchor (shortest depth doc). |
| 10 | Jared Palmer | Formik, Turborepo, v0 | usage-stat: npm 3.8M/wk + 34.3k GH stars | T1 | ★★★☆☆ | ★★★☆☆ | Weakest designer credentials of the set and no single process doc (bylined post + interviews); the generative-UI loop is named but product-specific. |
| 11 | Charli Marie Prangley | Kit (ex-ConvertKit) marketing sites | revenue: $41M ARR (Kit newsroom + estimate-tracker only) | T2 | ★★★★★ | ★★★★★ | Weakest verification (T2, no independent T1 figure) holds her to last despite the most complete, transferable end-to-end workflow in the set — rank is verification-driven, not content-driven. |

## Rejected candidates

- **Karri Saarinen** — tier3-only: no T1/T2 revenue figure for Linear; ~$100M ARR exists only in estimate trackers.
- **Mike Kus** — no qualifying in-window award; self-listed "1× Site of the Month" contradicted by official Awwwards profile (SOTM: 0).
- **Matt Perry** — attribution: purely engineering credit (creator of Motion, engineer at Framer); no public designer credit.
- **Tobias Ahlin Bjerrome** — scale-not-met: no public GitHub Copilot MAU exists (cumulative users only).
- **Zach Gage** — no qualifying award: Knotwords was an Apple Design Award 2023 finalist only.
- **Michael Flarup** — tier3-only: 5M-users claim self-disclosed (2015), out-of-window, no corroboration; Oko ADA 2024 credited to team, not individually.
- **shadcn** — depth-reject (Phase 2): first-party content is design principles + system spec only; no named, ordered workflow with explicit gates/loops. Doc currency was fine.
- **Sindre Sorhus** — FAIL-UNKNOWN: researcher failed twice, no evidence file produced; not needed (pool already met) — recommended targeted re-run if revisited.

## Notes

- Full rejection evidence (routes searched, dead ends) in `working/evidence/<name>-2026-08-17.json` for each rejected candidate.
- Phase-1 ranked order is preserved here; Phase-2 depth rejects (shadcn) removed from the ranked table.
- Usage-stat figures are official API pulls (npm downloads 2026-08-09→15, GitHub stars fetched 2026-08-17); award routes are Apple newsroom/developer winner pages; revenue route is Kit's own newsroom (flagged weak).
