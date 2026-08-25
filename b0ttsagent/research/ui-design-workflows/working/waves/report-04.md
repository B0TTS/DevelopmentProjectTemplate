# Wave 04 Report — Phase 1: Verification (wave 3 of N)

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, one candidate each, parallel fanout
- Result: **4 PASS / 0 REJECT** (running pool: 7 prior PASS + 4 = 11 PASS; target ≥12)

## Per-researcher status

| # | Candidate | Status | Verdict | Route | Evidence file |
|---|-----------|--------|---------|-------|---------------|
| 1 | Lea Verou | done | PASS | usage-stat | `working/evidence/lea-verou-2026-08-17.json` |
| 2 | Max Stoiber | done | PASS | usage-stat | `working/evidence/max-stoiber-2026-08-17.json` |
| 3 | Tobias Ahlin Bjerrome | retried | PASS | MAU | `working/evidence/tobias-ahlin-bjerrome-2026-08-17.json` |
| 4 | Charli Marie Prangley | retried | PASS | revenue | `working/evidence/charli-marie-prangley-2026-08-17.json` |

## Verdicts & evidence summary

- **Lea Verou — PASS (usage-stat).** npm prismjs 24,027,701 downloads/week (2026-08-09→15, fetched 2026-08-17), Tier 1 official API; GitHub 13,035 stars (below 20k bar, but npm clears the OR alone). Individually credited as Prism's creator (prismjs.com footer, GitHub profile, README link to her "Introducing Prism" post); designer credentials established (graphic design background, CSS Secrets author, web-standards design work). Doc-currency: lea.verou.me active through Aug 2026, still referenced as current by Prism README.
- **Max Stoiber — PASS (usage-stat).** npm styled-components 9,437,267 downloads/week + GitHub 41,120 stars (both Tier 1 official APIs, fetched 2026-08-17). Individually credited as styled-components creator (own site, Software Engineering Daily, Wikipedia-draft bio). Doc-currency: css-in-js essay (2019) still live and listed on current homepage.
- **Tobias Ahlin Bjerrome — PASS (MAU).** Individually credited as Principal Design Engineer on GitHub Copilot (own site, X bio, 2025/2026 speaker pages). Scale: GitHub Copilot 50M users (Microsoft FY2026 Q4 earnings, ~Jul 2026, Tier 1) + 20M all-time users (TechCrunch 2025-07-30, Tier 1). Doc-currency: blog live and canonical, referenced as current in 2026 speaker pages; last post ~Sep 2023.
- **Charli Marie Prangley — PASS (revenue).** Individually credited as Kit's Creative Director (bylined Kit rebrand post, press quotes). Scale: Kit "$41MM ARR" (Kit newsroom, Jun 2024, Tier 2) corroborated by Sacra ($41M Apr 2024 / $43M 2024) + Business Wire (Oct 2024, "$43MM company"). In-window (2024).

## Anomalies

1. **Researchers 3 & 4 first attempt returned empty** — no summary, no output file written. Retried once each (fresh spawn, same verbatim prompt); both succeeded on retry. Recorded as `retried`.
2. **Tobias Ahlin — metric is cumulative "users", not strict MAU.** Microsoft/GitHub do not disclose Copilot MAU; researcher used 50M all-time users (Tier 1) + 20M all-time (TechCrunch). Exceeds 1M threshold by orders of magnitude, but flag for orchestrator: MAU wording vs cumulative-users evidence.
3. **Charli Marie — no independent Tier 1 journalism found** for Kit's revenue. Evidence rests on Kit's own newsroom (Tier 2) with Sacra (estimate tracker — corroborate-only per standard) + Business Wire (company-authored release). Judged to satisfy Tier-2-with-corroboration, but this is the weakest PASS in the wave; recommend orchestrator review before counting toward the ≥12 pool.
4. **Max Stoiber — "Moxy Studio" design-work claim UNVERIFIED** (3 search angles, no connection found). His verifiable design work (Animade Frankensim) is 2015–16, out-of-window/team, not used for scale. LinkedIn profile gated behind sign-in. PASS stands on usage-stat route alone.
5. **Lea Verou — GitHub stars below 20k bar** (13,035); npm figure carries the route. Not a blocker (OR condition).

## QA checklist (lead)

- [x] All 4 JSONs exist, parse as JSON, all schema keys present (verified programmatically)
- [x] Every PASS backed by dated figure + tier (all 4 have figure/date/source_url/tier)
- [x] Every REJECT carries reason + dead ends (N/A — no REJECTs; all PASS carry dead_ends_searched)
- [x] Verdicts in report match JSONs on disk (4/4 PASS)
- [x] report-04.md has per-researcher status + PASS/REJECT counts + anomalies

## Next actions

- Pool now at 11 PASS (7 prior + 4). One more PASS needed to reach target ≥12 → run Wave 05.
- Orchestrator to adjudicate anomalies 2 & 3 (Copilot cumulative-users metric; Kit Tier-2-with-estimate-tracker corroboration) before final pool count.
- No re-runs outstanding; all 4 evidence files final.
