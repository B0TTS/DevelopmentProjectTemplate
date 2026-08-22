# Handoff — daily-trends-report skill build (session 2 of the build)

## TL;DR

Building the `daily-trends-report` agent skill per `b0ttsagent/planning/daily-trends-report-skill/CONTEXT-v2.md`. This session locked all open decisions via user Q&A and wrote the deterministic script layer. **Next session: run the 7 fixture scenarios against the scripts, then write the 4 reference docs, then SKILL.md.**

## Accomplished this session

- Read CONTEXT-v2.md (the contract) and the active skills: `write-a-skill-v2`, `karpathy-guidelines` (both must be re-activated next session).
- Asked the blocking questions; all answered by the user (recorded below).
- Created the skill tree: `.agents/skills/daily-trends-report/{scripts,references}/` and the sandbox `b0ttsagent/temp/dtr-fixtures/reports/`.
- Wrote 3 script files (stdlib-only Python 3.14, none tested yet):

| File | Role |
|---|---|
| `.agents/skills/daily-trends-report/scripts/_lib.py` | Shared helpers: `REPORT_TZ` (fixed UTC−10), `RECENCY_DAYS=7`, `MAX_STILL_CIRCULATING=10`, `MAX_MAIN_ITEMS=5`, `TRACKING_PARAMS` denylist, `today_iso`, `parse_date`, `in_window`, `normalize_url`, `normalize_headline`, `item_keys`, `identity_key`, `find_streak`, `parse_report_md` (markdown table parser) |
| `.agents/skills/daily-trends-report/scripts/build-inventory.py` | Scans last 2 report files (`base/*/*/report.md`, excludes today's folder) → `inventory.json` with `streak_hits` (url-key) + `streak_headline_hits` maps, newest-wins |
| `.agents/skills/daily-trends-report/scripts/route-and-verify.py` | `route` subcommand: leaf candidates + inventory → `routed.json` (main / still_circulating / excluded / dropped, domain notes, exclusions, prior_identities). `verify` subcommand: report.md vs inventory+routed; gate violations = exit 1, format nudges = warnings only |

## Locked decisions (user answers this session — do not re-ask)

1. **Timezone**: fixed UTC−10 offset (HST, no DST). `zoneinfo` is broken on this machine (no `tzdata`), so no IANA names, no pip deps.
2. **Leaf caps**: 8 searches + 5 full page-reads per leaf, both waves. Lead QA stays summaries-only.
3. **No PLAN.md** — build directly from CONTEXT-v2.
4. **Verify** = `route-and-verify.py verify` second mode (still 2 scripts total).
5. **Dates**: `YYYY-MM-DD` everywhere. **Folder structure changed from CONTEXT-v2**: reports live at `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\<YYYY-MM>\<YYYY-MM-DD>\` (month folder containing day folders). `index.md` stays at `AI-Development Trends/index.md`; File column like `2026-08/2026-08-18/report.md`.
6. **Anchors**: orchestrator fetches HN front page + GitHub Trending via harness web tools → raw title+URL lists to `anchors.md`. No script, no formatting rules.
7. **Still circulating** sorted by **original published date**, newest first.
8. **Fixtures**: 7 scenarios (5 mandated + update-test-pass + same-day rerun).
9. **Do NOT update CONTEXT-v2.md** (user explicit) — it still says `<MM-DD-YYYY>/`; the skill implements the new month/day structure instead.
10. **Build order approved**: fixtures → scripts → references → SKILL.md → final checklist → local tests.

**Open note for next session**: CONTEXT-v2's "settled" description wording says "a Redundant section" (v1 name). v2 renamed the section to "Still circulating". Decision: use **"Still circulating"** in the description (flagged to user as deliberate).

## Next session steps (in order)

1. **Test the scripts against the 7 fixture scenarios** in sandbox `b0ttsagent/temp/dtr-fixtures/reports/` (create prior report files + candidate JSONs + hand-written report.md per fixture; use explicit `--today 2026-08-18` so fixtures are rerunnable any day):
   - **F1 first-ever run**: empty base → inventory 0 streak hits; 5 fresh dated candidates → main; template report.md → verify exit 0 (word-budget warning expected).
   - **F2 streak + re-proposal**: prior reports 08-16 and 08-17 both carry X in main; candidate re-proposes X (same URL, date ≤7d, no delta) → `still_circulating`; a report placing X in main → verify FAIL.
   - **F3** >7-day item → `excluded`.
   - **F4** undated finding → `dropped`.
   - **F5 verify collision**: 1 prior with X in main; today's report has X in main, no update → verify FAIL.
   - **F6 update pass**: prior X (old URL, 08-15); candidate with new URL + newer date + concrete delta → main with `update: true`; report framed as update → verify PASS.
   - **F7 same-day rerun**: inventory `--today` excludes today's folder from `reports_scanned`.
2. **`references/eval-fixtures.md`** — document those 7 scenarios with the observed commands/outputs (must exist before SKILL.md body per CONTEXT-v2).
3. **`references/report-contract.md`** — skeleton, item schema, glance/chat/index rules, one good + one rejected example per section.
4. **`references/routing-rules.md`** — identity normalization (URL denylist + headline fallback), gates, update test (a)/(b), domain preference.
5. **`references/wave-spec.md`** — wave-1.md template, 3 leaf task prompts, leaf JSON schema (`headline, why, url, published_date, domain, source_type, delta_or_null`), QA checklist, gap-fill variant.
6. **`SKILL.md`** — settled description, `disable-model-invocation: true`, refuse list, numbered runbook + copy-in checklist, reference map, script usage ("run, don't read").
7. **write-a-skill-v2 final checklist** audit + line-count check (<500 lines).

## Contract facts to carry into the docs

- **Skeleton**: title + run date → `*Today at a glance*` (exactly 3 bullets, one per section) → 3 main tables (`Domain · Headline · Why it matters · Date · Link`) → `Still circulating` table (`Headline · Date · Link`) or omitted → nothing else (no outro, no methodology).
- **Headings**: `## AI trends`, `## SWE trends`, `## Productivity`, `## Still circulating` (stable, no emoji).
- **Items**: 3–5/section, 1–2 valid thin day, never pad, ordered by "worth a click"; why ≤2 sentences/~40 words; word budget 400–700 excl. Still circulating; one story one section; max 2 items per domain per section is a writer *preference* (note the cluster, keep better items).
- **index.md**: columns `Date · File · Item count · One-line glance`, newest row first, same-day upsert.
- **Chat pointer**: path + the 3 glance bullets + "N items demoted" if Still circulating non-empty. Nothing else.
- **Quality bar**: markdown-doc-designs auto-mode checklist only; DESIGN.md does not apply.
- **Harness**: opencode only — never mention pi. Orchestration: wave-lead fans out 3 leaves → route script → one gap-fill wave max (target exactly 3, exclusion list + empty domain hints) → writer = `b0tts-smart-agent`, wording only → verify, one rewrite then ship → index upsert → chat pointer.
- **Refuse list** (body): no weekly recap, no single-topic deep dive, no schedule-spec edit, no personalization, no tracker publish, no "also refresh yesterday".

## Commands

```bash
python .agents/skills/daily-trends-report/scripts/build-inventory.py \
  --base "b0ttsagent/reports/daily-reports/AI-Development Trends" [--today YYYY-MM-DD]
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route   --folder <day-folder> [--today YYYY-MM-DD]
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify  --folder <day-folder> [--today YYYY-MM-DD]
```

## Key references

- Contract (authoritative, supersedes everything): `b0ttsagent/planning/daily-trends-report-skill/CONTEXT-v2.md`
- Skills for next session: `.agents/skills/write-a-skill-v2/SKILL.md`, `.agents/skills/karpathy-guidelines/SKILL.md`, `.agents/skills/markdown-doc-designs/SKILL.md` (silent advisor for the reference docs)
- Fleet (no new agent definitions): `.opencode/agents/b0tts-lead-researcher.md`, `.opencode/agents/b0tts-researcher.md`, `.opencode/agent/b0tts-smart-agent.md`
- Environment: Python 3.14.6 on PATH; machine TZ HST; `b0ttsagent/reports/daily-reports/AI-Development Trends/` exists and is empty (first-ever run applies).

## Skills to activate in the next session

`write-a-skill-v2`, `karpathy-guidelines`, `markdown-doc-designs` (when writing the reference docs), `log-session` at close.
