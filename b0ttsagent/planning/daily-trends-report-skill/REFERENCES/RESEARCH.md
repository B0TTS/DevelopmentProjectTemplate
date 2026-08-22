# RESEARCH.md — daily-trends-report skill planning research

New research from the S0 planning session only. Complements CONTEXT-v2.md (what/why) and PLAN.md (how). Cited from PLAN.md §Existing assets.

## 1. Existing artifacts inventory (2026-08-18)

Skill dir: `.agents/skills/daily-trends-report/` (32K total, created in an aborted earlier session, untracked in git).

| Artifact | Status | Contents |
|---|---|---|
| `scripts/_lib.py` | exists (~180 lines) | Locked constants (UTC−10 fixed offset, 7-day window, caps 10/5), URL/headline normalization, identity keys, streak lookup, markdown table parser, date helpers |
| `scripts/build-inventory.py` | exists (~110 lines) | Last 2 `report.md` via `*/*/report.md` glob (month layout), excludes today's day folder, builds streak maps, warnings-never-abort |
| `scripts/route-and-verify.py` | exists (~280 lines) | `route` + `verify` subcommands; gates, update test, Still-circulating cap/sort, domain-preference notes, exclusion list, verify errors (gates) vs warnings (format nudges) |
| `SKILL.md` | **missing** | — |
| `references/*.md` | **missing** (all 4) | routing-rules, report-contract, wave-spec, eval-fixtures |

Never executed or tested. Policy: review → surgical fixes → fixture tests (PLAN S1–S2); rewrite only if broken.

## 2. Gap map: CONTEXT-v2 contract → script implementation

| Contract element | Script locus | Verdict |
|---|---|---|
| Identity: normalized URL primary, normalized headline fallback | `_lib.item_keys` / `identity_key` / `find_streak` | ✓ implemented |
| Streak gate over last 2 report *files* (not days); 0/1-prior edge cases | build-inventory streak maps; `route_candidate` | ✓ |
| 7-day window; undated dropped; future dates dropped | `route_candidate` + `in_window` | ✓ |
| Update test (a) mechanical, (b) delta | `route_candidate`: (a) new URL or newer date AND non-empty delta — delta presence is the (b) **proxy**; concreteness enforced by lead QA + writer | ✓ with documented proxy |
| Update's own date ≤7 days even if story older | `in_window` on candidate's published date | ✓ |
| Still circulating: ≤10, newest published first, one-liner | sort + cap in `cmd_route` | ✓ |
| Domain preference max 2/domain (advisory, never drops) | `domain_preference_notes` | ✓ |
| Exclusion list for gap-fill wave | `routed.exclusions` + `prior_identities` | ✓ |
| Verify: writer can't add sources/dates/rescue rejects | `verify` subcommand membership + gate checks | ✓ |
| Thin day (1–2 items) is valid | verify has max caps only, no minimum | ✓ |
| Glance exactly 3 bullets; word budget 400–700 | verify **warnings** (soft, not failures) | ✓ |
| index.md upsert (newest row top, no duplicate on rerun) | not scripted | by design — manual SKILL.md instruction; deterministic layer is exactly 2 scripts |
| Anchors fetch (HN front + GitHub Trending) | not scripted | by design — orchestrator fetches via harness web tools, writes `anchors.md` |
| Chat pointer (path + 3 bullets + demote count) | not scripted | by design — orchestrator manual step |

## 3. Decisions from this session's Q&A (2026-08-18)

- **Timezone:** fixed UTC−10 offset (HST, no DST). `ZoneInfoNotFoundError` confirmed on this machine; Hawaii has no DST so the offset is exact. (A2)
- **Caps:** 8 searches + 5 full page-reads per leaf, both waves; lead QA summaries-only per existing contract. (A3)
- **Dates:** canonical `YYYY-MM-DD` everywhere — report Date column, leaf JSONs, inventory, folder names.
- **Folder layout (A1):** month folders `YYYY-MM`, day folders `YYYY-MM-DD` under `AI-Development Trends/`; single `index.md` at the root of the month folders. Existing scripts already implement this.
- **Still-circulating sort:** original published date, newest first.
- **Anchors:** raw title + URL lists into `anchors.md`; no script, no formatting rules.
- **Verify mode:** subcommand of `route-and-verify.py` (2 entry points preserved).
- **Fixtures:** 7 scenarios covering all 10 success criteria; the 5 mandated minimums marked.
- **CONTEXT-v2 frozen:** amendments live in PLAN.md §0 (user Q1 answer: b).
- **Sessions chunked <50k context** per build piece (user constraint).
- **Outline gate waived:** user instructed "don't present the plan, auto write it out" — accepted exception to the create-execution-plan workflow; post-write review likewise batched.

## 4. Environment facts

- Python 3.14.6 on PATH; stdlib `zoneinfo` fails without `tzdata` (no IANA db on Windows).
- Machine timezone: Hawaiian Standard Time; today = 2026-08-18.
- `b0ttsagent/reports/daily-reports/AI-Development Trends/` exists and is **empty** → first-ever run applies; no legacy report files to migrate.
- Git repo present; skill dir untracked → script fixes are trivially reversible.
- AGENTS.md: no build/test/lint pipeline; throwaway files go in `b0ttsagent/temp/`.
