# Wave 07 Report — Phase 2 Depth Docs (wave 1 of 3)

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, parallel fanout (R1–R4 = fresh), one designer each, ranking order (strongest verification first)
- Status: **COMPLETE** — 4/4 researchers done, 0 failed, 0 retries needed
- Verdicts: **3 DEPTH-PASS / 1 DEPTH-REJECT** (running depth-doc pool: 3 PASS, 1 REJECT)

## Per-researcher status

| # | Designer | Status | Verdict | Output file |
|---|----------|--------|---------|-------------|
| R1 | Adam Wathan | done | DEPTH-PASS | `creators/Adam-Wathan.md` |
| R2 | Mark Otto | done | DEPTH-PASS | `creators/Mark-Otto.md` |
| R3 | Mike Bostock | done | DEPTH-PASS | `creators/Mike-Bostock.md` |
| R4 | shadcn | done | DEPTH-REJECT | `creators/shadcn.md` |

## Verdicts & rationale

- **R1 — Adam Wathan: DEPTH-PASS.** Anchor is his first-party "Designing Tailwind UI Ecommerce" post (read end-to-end) — a named 5-step workflow (research & catalog → design full pages → build & browser-review [quality gate] → extract components → inventory & repeat [iteration loop]) — reinforced by the Refactoring UI book's named "Starting from Scratch / Work in cycles" process, his KiteTail decision-loop gist, and the Laracon US 2024 talk transcript (currency confirmed: blog active May 2026, talk 2024). Every step source-linked.
- **R2 — Mark Otto: DEPTH-PASS.** Named, ordered 4-stage process ("ideation, debate and feature review, implementation, and lastly abstraction and documentation," A List Apart 2012) with explicit gates (debate-before-moving-on, feature-admission, dogfooding "binge-close" test, test-pass merge, prototype≠production-ready) and iteration loops (v1→v12 Issues, design↔code ping-pong), all first-party and source-linked; currency confirmed via "Shipping Blended Diffs" (Jan 2024) reusing the same workflow.
- **R3 — Mike Bostock: DEPTH-PASS.** "Design is a Search Problem" (OpenVis 2014, transcript read end-to-end) gives an 8-step search process (frame-as-search → divergent exploration → hypothesis-testing prototypes → context-deprived evaluation → git/branch/preview infrastructure → simulated-annealing convergence → pruning + Makefiles → real-data testing) with explicit quality gates (prototype-hypothesis test, "does it communicate" feedback gate, annealing commit point, plus a documented self-correction loop when his own Prim's color-flood visualization misled). All first-party; every step source-linked; supported by his essays.
- **R4 — shadcn: DEPTH-REJECT** (`principles-only, no ordered process`). First-party output (ui.shadcn.com/docs principles, theming/registry docs, product-announcement X threads, shadcn.com) is design principles + system specification + shipped artifacts — no named, ordered design/build workflow with an explicit quality gate or iteration loop documented by him. No talks or in-depth first-party interviews surfaced; closest items (Theo's video, RedMonk, Vercel Academy lesson) are secondhand/Vercel-authored and excluded as anchors per the depth gate. Eligibility facts copied from evidence JSON (usage-stat, T1, in-window, docs current).

## QA checklist results

- [x] All 4 docs exist with all 4 sections present (verified via section headers)
- [x] Every workflow step has a source link (bare-URL links; Adam-Wathan steps 2–5 use "Source: same." referencing step-1 link — acceptable)
- [x] "What Makes It Distinct" is specific, non-generic in all 3 PASS docs (shadcn marks N/A with system properties)
- [x] Every DEPTH-REJECT carries a reason (shadcn: principles-only, no ordered process)
- [x] Eligibility Evidence has route + tier + window + currency line + product-type tag + craft/growth tag in all 4 docs
- [x] report-07.md has per-researcher status + DEPTH-PASS/REJECT counts + anomalies

## Anomalies

1. **R1 Adam Wathan:** no verbatim "build the ugly version first" quote found in first-party content (verified equivalents documented: book's "Work in cycles / build the simple version first" + ecommerce post's "repeat the whole thing" loop). YouTube transcript services all blocked — Laracon transcript obtained from laracontv.com instead. Refactoring UI chapter text verified via third-party PDF copy; citations point to the official book page.
2. **R2 Mark Otto:** SearXNG returned empty for all queries (fell back to Exa per skill routing). "Managing features in Bootstrap" live URL 404s on the rebuilt site — content verified via Wayback capture. Old `/talks` page and pre-2023 post URLs 404 on the Astro-rebuilt site; posts live under `/blog/<slug>`.
3. **R3 Mike Bostock:** Medium blocked direct fetch of "What Makes Software Good?" (403) — omitted, not needed. "Design is a Search Problem" cited via YouTube + videodb.org transcript (his own words).
4. **R4 shadcn:** SearXNG empty for process queries (fell back to Exa). Searched talks (Vercel Ship / Next.js Conf / React Summit), podcast interviews, X threads on design process — none yielded first-party ordered-process content.
5. **Encoding artifacts:** em-dashes render as replacement chars (`�?`) in several docs (inherited from evidence JSON). Cosmetic only — does not affect structure, links, or verdicts. Optional cleanup.
6. **Link format:** docs use bare URLs rather than markdown `[text](url)` links — satisfies "every step carries a source link"; noted for consistency with prior waves.

## Next actions

- **Wave 07 complete as wave 1 of 3 for Phase 2 depth docs.** 3 depth docs landed (Adam-Wathan, Mark-Otto, Mike-Bostock); shadcn DEPTH-REJECT is a valid outcome per spec — no re-run needed, no depth doc for shadcn.
- **Remaining waves (2–3 of 3):** continue depth docs for the rest of the verified pool per the phase plan.
- Optional: fix em-dash encoding in the 4 docs during a later cleanup pass.
