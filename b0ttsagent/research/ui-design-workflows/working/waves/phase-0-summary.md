# Phase 0 Summary — ui-design-workflows research run

- Written: 2026-08-17 · Phase 0 (candidate discovery) gate review
- Gate verdict: **PASS**

## Gate evidence

| Gate item | Result | Evidence |
|---|---|---|
| candidates.md ≥20 unique, schema-complete rows | PASS | 44 unique rows; all have name + ≥1 scale-lead URL + ≥1 first-party doc URL; schema conformant |
| Dedup correct, same-name disambiguated | PASS | Steve Schoger merged across lanes A/B (1 row, noted); 45 raw → 44 unique; no same-name/different-person collisions |
| Lane balance ≥4 per lane; weak rows flagged `?` | PASS | A: 17, B: 13, C: 14; `?` flags present in all lanes |
| report-01.md per-researcher status + anomalies | PASS | Status table (3 researchers PASS), 5 anomalies, QA checklist all checked |

## Ranked priority list for Phase 1 verification (by likely verification strength)

1. **Ken Wong** — 2 ADA wins (Wikipedia list), 26M copies (Architizer), GDC talks.
2. **Asher Vollmer** — Threes! ADA 2014, 45k-word devmail archive, #1 in 60 countries.
3. **Lucas Pope** — IGF Grand Prize + BAFTA, dukope.com devlogs.
4. **Philipp Stollenmayer** — Song of Bloom ADA 2020, own design docs, Apple feature.
5. **Curtis Herbert** — Slopes ADA 2022, $1M ARR (RevenueCat), Slopes Diaries.
6. **Simon Flesser** — 2 ADAs (Device 6, Sayonara), Making-of blog posts.
7. **Ryan McLeod** — Blackbox ADA 2017 (individually credited), Medium process posts.
8. **Adam Wathan** — Tailwind GitHub/npm stats verifiable, design blog posts.
9. **Mark Otto** — Bootstrap stats, design deep-dives + talk.
10. **shadcn** — shadcn/ui stars, documented design principles.
11. **Mike Bostock** — D3 stats, canonical visualization essays.
12. **Lea Verou** — Prism downloads, design/standards background, blog.
13. **Steve Schoger** — heroicons stars, Refactoring UI, YouTube breakdowns.
14. **Brad Frost** — Atomic Design, 15-year process blog.
15. **Ethan Marcotte** — RWD book free online, journal.
16. **Erika Hall** — Mule Design books + blog.
17. **Karri Saarinen** — Linear co-founder, "Now" essays.
18. **Tobias Ahlin Bjerrome** — Spotify/GitHub design blog.
19. **Zach Gage** — Knotwords ADA 2023 finalist (Apple newsroom), stfj.net talks.
20. **Terry Cavanagh** — Super Hexagon, Dicey Dungeons devlog.

## Bottom / REJECT-risk (verify only if pool runs short)

- **Zeno Rocha, Nicolas Gallagher, Andrey Sitnik, Matt Perry, Paul Henschel** — engineer-only credits, not visual designers.
- **Sindre Sorhus** — thin written process content (`?` flagged).
- **Greg Wohlwend** — team-credited artist (Vlambeer); own site thin on process.
- **Daniel Benmergui** — no ADA win; personal site down.
- **Michael Flarup** — scale self-disclosed only; no ADA win.
- **Marc Edwards** — Mac-utility niche, revenue not public.
- **Dann Petty, Mike Kus** — award claims self-listed; thin first-party process content.
- **Charli Marie Prangley** — role self-disclosed; revenue not public.
- **Julie Zhuo** — org-level leadership credit (VP), product scale is team-level.
- **Chris Do, Ran Segall, Erik Kennedy, Meng To, Tobias van Schneider, Pablo Stanley** — education/agency revenue self-disclosed or third-party interview only.

## Caveats Phase 1 researchers MUST honor

1. **Window 2021-08-17 → 2026-08-17**: verification evidence must fall inside the window; pre-window awards are credit context only.
2. **Award claims → primary lists** (Wikipedia ADA winners, Apple newsroom, IGF/BAFTA pages); never trust self-disclosures.
3. **Self-disclosed scale figures are insufficient** — require third-party or public corroboration (revenue, MAU, downloads).
4. **Lane B engineer rows (5–6)** — orchestrator must decide whether strict visual-design credit is required before burning verification budget.
5. **Dead/thin first-party docs** (danielbenmergui.com down, gregwohlwend.com thin, Mike Kus portfolio-only) — locate alternates early or drop.
6. **SearXNG flakiness** — follow skill routing (SearXNG once → websearch → web_search last resort); log fallbacks.
