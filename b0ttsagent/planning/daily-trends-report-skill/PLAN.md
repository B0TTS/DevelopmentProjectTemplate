# PLAN.md — daily-trends-report skill (v2)

Executable how. The what/why lives in [CONTEXT-v2.md](CONTEXT-v2.md) — this plan cites it, never restates it. CONTEXT-v2 supersedes `CONTEXT.md` in this folder.

## §0 Amendments to CONTEXT-v2 (read first)

User decision: CONTEXT-v2 stays frozen; amendments live here. Where PLAN and CONTEXT-v2 conflict, these win.

| # | Amendment | Replaces |
|---|---|---|
| A1 | Day folders: `AI-Development Trends/<YYYY-MM>/<YYYY-MM-DD>/`; single `index.md` at `AI-Development Trends/index.md` (parent of month folders). Existing scripts already implement this layout. | CONTEXT-v2 Key Term "Day folder" (`<MM-DD-YYYY>` directly under `AI-Development Trends/`) |
| A2 | Open Q1 resolved: canonical timezone is a fixed UTC−10 offset (HST, no DST). Machine zoneinfo has no IANA db; the offset is exact, not approximate. | CONTEXT-v2 Open Questions #1 |
| A3 | Open Q2 resolved: per-leaf caps = 8 searches + 5 full page-reads (both waves); lead QA is summaries-only per its existing contract. | CONTEXT-v2 Open Questions #2 |
| A4 | Settled description wording: "a Redundant section" → "a Still circulating section". | CONTEXT-v2 "Description (settled wording)" |

## Technical Context

| Field | Value |
|---|---|
| Language/Version | Python 3.14, stdlib only, no pip deps |
| Primary Dependencies | None beyond stdlib; scripts run via `python` on PATH |
| Storage | Report files on disk at `b0ttsagent/reports/daily-reports/AI-Development Trends/`. `inventory.json` / `routed.json` are throwaway derived parses, rebuilt every run |
| Testing | Synthetic day folders under `b0ttsagent/temp/daily-trends-report-fixtures/`, run against the two scripts; scenarios derived from CONTEXT-v2 success criteria; final fresh-run trigger test in opencode (user step) |
| Target Platform | Runtime harness: opencode (lead-researcher, researcher, smart-general-agent). Build harness: current agent + bash |
| Performance Goals | Bounded run: ≤8 searches + ≤5 page-reads per leaf; one gap-fill wave max; SKILL.md body <500 lines; report ~400–700 words |
| Constraints | Agent-skills standard (write-a-skill-v2); SKILL.md never mentions pi; exactly 2 deterministic entry-point scripts; `disable-model-invocation: true`; no new agent definitions; no `DESIGN.md` on reports (markdown-doc-designs quality bar only) |
| Scale/Scope | 3 main sections × 1–5 items; Still circulating ≤10; 7-day window; ~15-minute read |

## Existing assets (starting point, user-approved)

`.agents/skills/daily-trends-report/` already contains `scripts/_lib.py`, `scripts/build-inventory.py`, `scripts/route-and-verify.py` (~600 lines total) implementing: identity normalization, streak + 7-day gates, update test ((b) proxied by non-empty delta), routing destinations, Still-circulating cap/sort, domain-preference notes, exclusion list, `route` + `verify` subcommands, month-folder layout, glance/word-budget nudges. They have **never been executed**. Policy (user Q3): review → surgical fixes → fixture tests; rewrite only if broken. Full inventory + gap map: [REFERENCES/RESEARCH.md](REFERENCES/RESEARCH.md).

## Sessions

Every session stays under ~50k context: read only the files named in its "Read" line, write only its named outputs. Build artifacts land in the skill dir; throwaway logs/fixtures in `b0ttsagent/temp/`.

### S0 — Planning docs (this session) ✅
- Deliverables: `PLAN.md` + `REFERENCES/RESEARCH.md`. Done.

### S1 — Script review & surgical fixes
- Read: CONTEXT-v2 §Key Terms, §Item Identity & Routing, §Report Contract, §What Success Looks Like + the 3 scripts.
- Audit every gate/routing rule/verify check in CONTEXT-v2 against script behavior. Log findings (rule → script locus → verdict) to `b0ttsagent/temp/daily-trends-report-skill/script-review.md`.
- Fix surgically only where behavior contradicts CONTEXT-v2. No speculative flexibility, no adjacent cleanup (karpathy). Each fix logged with justification.
- Known review points: (1) build-inventory glob `*/*/report.md` matches A1 layout; (2) update-test (b) non-empty-delta proxy is documented as a proxy; (3) verify has max-item caps but no minimum (thin day is valid); (4) future-dated candidates dropped; (5) today's day folder excluded from inventory; (6) corrupt prior → warning, never abort.
- **Exit gate:** script-review.md has zero open items; `python -m py_compile` clean on all 3 scripts.

### S2 — Fixture scenarios: build & run
- Read: CONTEXT-v2 §What Success Looks Like + script-review.md.
- Build synthetic day folders under `b0ttsagent/temp/daily-trends-report-fixtures/` (prior report.md files + leaf JSONs + today's folder per scenario).
- Run the 7 scenarios mapped from success criteria 1–7 + same-day rerun; record command + expected vs actual in `results.md` (same temp dir).
- If a script fails, fix the script surgically (S1 rules); if the fixture was wrong, fix the fixture.
- Criteria 8–10 are partially manual (index upsert, chat pointer, glance readability): note which parts are script-checkable and which become SKILL.md instruction checks.
- **Exit gate:** all 7 scenarios produce expected outcomes; results.md complete.

### S3 — references/routing-rules.md + references/report-contract.md [P]
- Read: CONTEXT-v2 §Key Terms, §Routing, §Report Contract + script-review.md.
- `routing-rules.md`: documents the rules the verified scripts enforce (identity, gates, update test, domain preference). Scripts are the executable truth; this doc must match them exactly.
- `report-contract.md`: skeleton, item schema, glance/chat/index rules, one good + one rejected example per section. Quality bar: markdown-doc-designs auto-mode.
- **Exit gate:** both files exist; TOC at top when >100 lines; terminology identical to scripts (`streak-hit`, `update test`, `Still circulating`); one-level-deep links only.

### S4 — references/wave-spec.md + references/eval-fixtures.md [P]
- Read: CONTEXT-v2 §Research Orchestration, §Skill Shape + S2 results.md.
- `wave-spec.md`: leaf schema (`headline, why, url, published_date, domain, source_type, delta_or_null`), day-folder paths, caps (A3), QA checklist, lead/leaf/writer prompts, gap-fill rules.
- `eval-fixtures.md`: the 7 scenarios as runnable steps (commands + expected output); the 5 mandated minimum fixtures marked. Written BEFORE SKILL.md per CONTEXT-v2 authoring order.
- **Exit gate:** every scenario reproducible from the doc alone (self-contained commands, no reliance on session memory).

### S5 — SKILL.md
- Read: CONTEXT-v2 §Skill Shape, §Report Contract, §What Success Looks Like + reference files as needed for citing.
- Frontmatter: `name: daily-trends-report`, `disable-model-invocation: true`, description = settled wording with A4 fix.
- Body <500 lines: numbered runbook + copy-in checklist + refuse list + degrees-of-freedom table + "read which reference when". Forward-slash paths; no pi mention; no time-sensitive facts.
- **Exit gate:** write-a-skill-v2 final checklist all green; body <500 lines; one job per skill.

### S6 — Validation & handoff
- Read: write-a-skill-v2 SKILL.md (final checklist) + all skill files.
- Fresh pass: re-run the S2 fixtures end-to-end in one go (runner-B style); run the write-a-skill-v2 final checklist; markdown-doc-designs pass on SKILL.md + references.
- Drift check vs CONTEXT-v2 success criteria: all 10 covered by a fixture or a SKILL.md instruction check.
- Handoff: user runs the fresh-session opencode test — `/skill:daily-trends-report` triggers, then a real first run into `b0ttsagent/reports/daily-reports/AI-Development Trends/`.
- **Exit gate:** fixtures green, checklist green, drift report empty or accepted by user.

## Sequencing summary

| Session | Deliverable | Depends on | Est. context |
|---|---|---|---|
| S0 ✅ | PLAN.md + REFERENCES/RESEARCH.md | CONTEXT-v2 + conversation | ~35k |
| S1 | script-review.md + surgical fixes | S0 | ~30k |
| S2 | fixture results + fixes | S1 | ~35k |
| S3 | routing-rules.md + report-contract.md | S2 (verified behavior) | ~30k |
| S4 | wave-spec.md + eval-fixtures.md | S2 | ~30k |
| S5 | SKILL.md | S3, S4 | ~30k |
| S6 | validation + handoff | S1–S5 | ~35k |

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| `_lib.py` is a third file where CONTEXT says "two scripts" | Two entry points share identity/parse logic | Duplicating the logic in both entry points invites drift; `_lib` is an import library, not a third entry point |
| `verify` as a subcommand of route-and-verify.py | CONTEXT mandates exactly 2 scripts AND a verify gate | A third script violates the 2-script constraint; omitting verify violates the gate |
| Fixed UTC−10 constant instead of IANA zone | zoneinfo has no tz database on this machine (verified) | `tzdata` pip dep breaks stdlib-only; HST has no DST so the offset is exact |
| ~70-line markdown table parser in `_lib` | Deterministic identity/date extraction from report.md | Naive regex breaks on wrapped cells; a markdown lib is a non-stdlib dep |
| Amendments in PLAN instead of CONTEXT edits | User decision (Q1: b) — CONTEXT-v2 frozen | Editing CONTEXT contradicts the user's explicit choice; mitigation: §0 is the first thing read and PLAN is the execution contract |
| Multi-session chunking | User constraint: <50k context per build piece | One mega-session rejected by user |

## Risk / Rollback

- The skill dir is untracked in git; script fixes are reversible by reverting the file. No irreversible operations in any session.
- Synthetic fixtures live in `b0ttsagent/temp/` — deletable at any time.
- First-real-run risk: leaves hit their caps on a heavy news day; the skill ships short rather than looping (CONTEXT bound). No rollback needed.
- Living-document rule: CONTEXT-v2 is frozen by user decision, so if execution contradicts it beyond §0, the amendment table is updated before continuing — stale CONTEXT is harmful.
