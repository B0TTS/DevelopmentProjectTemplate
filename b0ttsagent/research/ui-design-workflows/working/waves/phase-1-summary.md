# Phase 1 Summary — ui-design-workflows verification (END QA)

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Waves: 02–06 (5 verification waves), all PASS
- Target: 12 verified PASS — **MET** (pool = 12)

## Phase gate

| Check | Result |
|-------|--------|
| 12 PASS evidence records on disk, each with dated figure + tier | **PASS** — 12/12 on disk, all have dated figure + source URL + tier (11 T1, 1 T2) |
| All REJECT records have reasons + dead ends | **PASS** — 6/6 REJECT files carry rejection_reason + dead_ends_searched |
| Sorhus FAIL-UNKNOWN logged (no file — acceptable, pool already met) | **PASS** — logged in report-06.md anomaly #1; no JSON on disk; pool ≥12 without him |

**Phase 1 gate verdict: PASS. Counts: 12 PASS / 6 REJECT / 1 FAIL-UNKNOWN (Sorhus).**

## Phase 2 depth-doc order (ranked by verification strength: route quality, scale margin, attribution solidity)

1. **Adam Wathan** — T1 usage-stat, npm 85.4M/wk (~85× threshold), unambiguous individual designer credit.
2. **Mark Otto** — T1 usage-stat, npm 4.1M/wk + GitHub 174.6k stars, canonical Bootstrap creator credit.
3. **Mike Bostock** — T1 usage-stat, npm 15.8M/wk + 113.5k stars, essays cited as current by official D3 docs.
4. **shadcn** — T1 usage-stat, 121.5k stars + npm 6.9M/wk; solid but pseudonymous attribution.
5. **Lea Verou** — T1 usage-stat, npm 24M/wk (stars below bar; OR satisfied via npm); designer credentials a judgment call.
6. **Steve Schoger** — T1 usage-stat, npm 2.7M/wk + 23.7k stars (stars just above bar); attribution as visual designer very solid.
7. **Philipp Stollenmayer** — T1 award, ADA 2025 Innovation, individually credited by Apple on the award page.
8. **Curtis Herbert** — T1 award, ADA 2022 Interaction; individual credit confirmed via Apple Developer feature; active 48-post doc series.
9. **Ryan McLeod** — T1 award, ADA 2024 Spatial Computing; Medium doc recency UNKNOWN (bot-block).
10. **Max Stoiber** — T1 usage-stat, npm 9.4M/wk; co-creator credit nuance + designer-credential judgment call.
11. **Jared Palmer** — T1 usage-stat, npm 3.8M/wk; designer credentials weakest of the group; single 2018 blog post as doc lead.
12. **Charli Marie Prangley** — T2 revenue (Kit's own newsroom) + estimate-tracker corroboration only; no independent T1 press figure.

## Flags carried into Phase 2

- **Prangley** — weak T2 + estimate-tracker corroboration; no T1 press figure found. Depth-doc should lean on first-party process content, not the revenue route.
- **Palmer** — doc lead is a single 2018 blog post; designer credentials rest on self-disclosed studio + all-contributors 🎨 credit. Verify more first-party process content exists before depth-doc.
- **Verou / Stoiber** — designer-credentials judgment calls: Verou's credit is graphic-design background + standards roles (W3C TAG/CSS WG) rather than product-designer title; Stoiber is co-creator of styled-components (with Glen Maddern) and Moxy Studio claim is unverified. Depth docs should frame credits precisely.
- **Stollenmayer** — verify first-party docs (kamibox.de songofbloom-files) exist in English before depth-doc; site may be German-primary.
- **Doc-currency warnings** — Mark Otto (blog stale since Jun 2024), Ryan McLeod (Medium recency UNKNOWN, 403), Adam Wathan (2021 flagship post historical; product rebranded Tailwind Plus 2025). All three acceptable, but depth docs should cite the current lineage.

## Rejected candidates (for INDEX.md)

- **Karri Saarinen** — tier3-only: no T1/2 revenue figure for Linear; only estimate trackers (~$100M ARR).
- **Mike Kus** — scale-not-met: no in-window qualifying award; self-listed SOTM contradicted by official Awwwards profile (SOTM: 0).
- **Matt Perry** — attribution: purely engineering credit (creator of Motion, engineer at Framer); no public designer credit.
- **Tobias Ahlin Bjerrome** — scale-not-met: no public GitHub Copilot MAU exists (cumulative users only).
- **Zach Gage** — no qualifying in-window award: Knotwords was ADA 2023 finalist only.
- **Michael Flarup** — tier3-only: 5M-users claim self-disclosed (2015), out-of-window, no corroboration.
- **Sindre Sorhus** — FAIL-UNKNOWN: researcher failed twice, no evidence file; recommend targeted re-run (high-confidence usage-stat route).
