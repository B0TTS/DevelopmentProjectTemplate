# CONTEXT.md v2 — daily-trends-report skill

Supersedes `CONTEXT.md` in this folder. What and why only — not the execution plan.

## What I Want

A skill — `daily-trends-report` — invoked on purpose each day, that writes a quick-scan digest of AI trends, SWE trends, and SWE productivity: a target of 3–5 items per section, each a headline + why-it-matters + source link + published date.

The defining promise: a story occupies a main section on **at most one run**. The next consecutive report appearance is demoted, not re-served as fresh. Nothing older than 7 days appears anywhere unless it carries a dated, concrete update. Residue that is still ≤7 days old and was proposed again goes to **Still circulating**, not back into a main section.

Research runs on the existing agent fleet (wave-lead → leaf researchers → writer). The finished file is what the 15-minute "Read the daily AI reports" ritual actually reads.

## Scope

In scope:

- The skill (instructions, workflow, two deterministic scripts, one-level references) per the agent-skills standard
- Daily research orchestration on the existing fleet
- Item identity, two-gate routing, and the Still circulating residue list
- The report contract (skeleton, word budget, glance block, index, chat pointer)
- Per-day folder of the report plus that run's related files

Out of scope: everything in Non-Goals.

## Key Terms

| Term | Meaning |
|---|---|
| Identity | How two findings are recognized as the same story. Primary key = normalized URL (strip tracking query, trailing slash, `www.`, mobile hosts). Fallback = normalized headline (lowercase, strip punctuation) only when URLs differ but name the same story. Every gate uses this key, not raw strings. |
| Streak-hit | The identity appeared in a main section of either of the last 2 report files (not calendar days) and has no passing update. |
| Update test | Re-entry to a main section is allowed only if (a) the URL is new **or** the page has a newer published/updated date, **and** (b) the why-it-matters cites a concrete delta that was not in the previous item (version, number, decision, CVE id, ship date). "Still being discussed" is not a delta. The *update itself* must be ≤7 days old even if the original story is older. (a) is mechanical; (b) is a writer/QA check. Fail (b) → Still circulating or drop. |
| Still circulating | Residue list, not a second digest. Heading name for what v1 called Redundant. |
| Inventory | Throwaway parse of the last 2 report files, rebuilt every run, never hand-edited. Not a state database. |
| Day folder | `b0ttsagent/reports/daily-reports/AI-Development Trends/<MM-DD-YYYY>/` — today's report and that run's related files. |

## Report Contract

The daily deliverable the user reads. Quality bar is the markdown-doc-designs auto-mode checklist only. `DESIGN.md` does not apply.

**Layout.** One day folder per run. The digest is `report.md` inside it. `index.md` lives in the parent folder.

```
b0ttsagent/reports/daily-reports/AI-Development Trends/
  index.md
  <MM-DD-YYYY>/
    report.md
    anchors.md
    inventory.json
    ai.json
    swe.json
    productivity.json
    routed.json
    wave-1.md
```

**`report.md` skeleton** — nothing else:

1. Title + run date
2. *Today at a glance* — exactly 3 bullets, one per section
3. Three main sections as tables: Domain · Headline · Why it matters · Date · Link
4. Still circulating as a table, or omit if empty
5. No outro, no methodology, no "sources consulted"

**Headings** (stable, no witty titles, no emoji): `## AI trends`, `## SWE trends`, `## Productivity`, `## Still circulating`.

**Main sections.** Target 3–5 items. 1–2 is a valid thin day. Never pad. Writer orders by "worth a click," not recency. Dates stay in the Date column.

**Item fields.** Headline · why-it-matters (≤2 sentences / ~40 words) · source link · published date.

**Word budget.** Whole `report.md` ~400–700 words excluding Still circulating.

**Still circulating.** Only identities that (i) are streak-hit, (ii) are ≤7 days, (iii) were actually proposed again this run. Cap 10, newest published first. One line: headline · date · link. No why-it-matters. Omit the section when empty.

**Cross-section.** One story, one section. If it fits AI and SWE, pick one.

**`index.md`.** The skill creates it if missing. Table, newest row at the top. Columns: Date · File · Item count · One-line glance. Same-day rerun updates the existing row; it does not append a duplicate.

**Chat.** Path + the 3 glance bullets + "N items demoted" if Still circulating is non-empty. No second report, no extra analysis.

## Coverage Domains

Three sections, no new ones. The lists below are **search hints**, not a coverage quota. Leaves are not asked to hit every domain.

Max 2 items per domain per section is a router *preference*. If enforcing it would drop a better item or empty a thin section, keep the better item and note the cluster.

| Section | Domain hints |
|---|---|
| AI trends | frontier model releases · AI research papers · AI company news · open-source AI · AI policy/regulation · AI infra/hardware |
| SWE trends | security & CVEs · OSS licensing & governance · cloud & pricing · languages & frameworks · web platform & standards · dev tools & editors |
| Productivity | new SWE productivity tools · AI-assisted dev workflows · emerging practices & workflows |

**Productivity constraint.** An item must be a shipped or newly documented tool, workflow, or practice with a dated primary source. No "10 tips" roundups, no evergreen blog posts, no "remember to use a todo list."

## Item Identity & Routing

This is the behavioral heart of the skill. Identity is defined in Key Terms. Without that key, the gates are not implementable.

**History window.** Last 2 *report files* (`report.md`), not last 2 calendar days. Today's day folder is never treated as history. Missed calendar days do not invent a streak. 0 priors → no streak-hits. 1 prior → that file's main-section identities are streak-hits (a story gets at most one day in main). Corrupt/unreadable prior → treat as missing, log it, do not abort.

**Same-day rerun.** Overwrite today's `report.md`. Inventory ignores today's folder. Index upserts the existing row.

**Anchors.** Hacker News front page + GitHub Trending are fetched once per run into `anchors.md`. They are discovery seeds only. An HN thread or trending row is never a report item. Researchers may use them only to find a dated primary source.

**Published date.** Page published/updated time, else HN submission time if the cited item *is* that post, else drop. No guessed dates. "Today" and the 7-day window use one named timezone — see Open Questions.

**Gates**, applied every run by script:

| Gate | Rule |
|---|---|
| Streak | An identity that occupied a main section in either of the last 2 reports is demoted unless it passes the update test |
| 7-day recency | Only items published within 7 days may appear anywhere; undated items are dropped. An update's own date must also be ≤7 days |

**Routing:**

| Condition | Destination |
|---|---|
| Fresh identity, not streak-hit, dated ≤7d | Main section |
| Streak-hit + published ≤7d + re-proposed + update test failed | Still circulating |
| Streak-hit + published >7d | Excluded |
| Update test passed (delta dated ≤7d) | Main section, framed as an update citing the delta |
| No verifiable published date | Dropped |
| Published >7d, no passing update | Excluded |

Once demoted, an identity returns to a main section only via the update test.

**Deterministic layer.** Two scripts, executed not read, stdlib-only if possible, deps declared in SKILL.md:

1. `scripts/build-inventory.py` — last 2 `report.md` files → `inventory.json` (identity, URL, section, date, one-line summary)
2. `scripts/route-and-verify.py` — leaf candidates + inventory → `routed.json` plus pass/fail: main / still-circulating / excluded, counts, domain preference, undated drops, identity collisions with last 2 reports

The writer does not apply gates. The writer does not add sources, dates, or rescue rejects.

## Research Orchestration

Use the fleet that already exists. No new agent definitions.

**Sequence:**

1. Orchestrator (user-spawned, this skill loaded) builds inventory, fetches anchors to disk, writes one wave spec
2. `b0tts-lead-researcher` fans out 3 `b0tts-researcher` leaves (AI / SWE / Productivity) and QA's disk outputs against the spec
3. Orchestrator runs the route/verify script
4. If a section has 0–2 survivors: one gap-fill wave only, target exactly 3, with the exclusion list and the empty domain hints. Then stop. If it still cannot, ship short
5. Writer (`b0tts-smart-general-agent`) receives frozen `routed.json` + the report template. Wording only. No research, no routing
6. Verify script must pass. One rewrite then ship with a "verify failed" note rather than looping
7. Upsert `index.md`; post the chat pointer

**What leaves receive.** `inventory.json` + `anchors.md`. Do not re-propose those identities unless a dated delta exists. Leaf schema: headline, why, url, published_date, domain, source_type, delta_or_null.

**Who may write what.** Leaves and the wave-lead write only their assigned paths inside the day folder. Only the writer writes `report.md`.

**Run bounds.** Each leaf has a hard search/read cap (see Open Questions). One gap-fill wave max. No third wave. Keep the day folder; no cleanup step.

**Copy-in checklist** the orchestrator pastes and ticks:

- [ ] Inventory built
- [ ] Anchors fetched
- [ ] Wave spec written
- [ ] Lead spawned
- [ ] QA passed
- [ ] Route script run
- [ ] Writer spawned
- [ ] Verify script pass
- [ ] Index updated
- [ ] Chat pointer posted

## Skill Shape

One job: generate the daily report. Name stays `daily-trends-report`. Home: `.agents/skills/daily-trends-report/`.

**Frontmatter.** `disable-model-invocation: true` — hidden from auto-load; fires only as `/skill:daily-trends-report`. The description is still the router text for harnesses that honor it and for the slash-command help.

**Description (settled wording):**

> Generates a dated daily quick-scan digest of AI trends, software-engineering trends, and SWE productivity items, with source links, published dates, and a Redundant section for streak-hit stories. Use when the user says "generate today's report", "daily trends report", "today's AI report", "daily AI digest", "SWE trends report", or wants today's AI/dev/productivity scan written to the daily-reports folder. NOT for weekly recaps, researching a single topic, personalized coaching, schedule changes, or publishing to a tracker.

**Refuse list** (body, not just description): no weekly recap, no single-topic deep dive, no schedule-spec edit, no personalization, no tracker publish, no "also refresh yesterday."

**Progressive disclosure.** SKILL.md is the numbered runbook + checklist + which reference to read when. Body stays under 500 lines. References are one level deep:

| File | Holds |
|---|---|
| `references/report-contract.md` | Skeleton, item schema, glance / chat / index rules, one good and one rejected example per section |
| `references/routing-rules.md` | Identity, gates, update test, domain preference |
| `references/wave-spec.md` | Leaf schema, day-folder paths, QA checklist, prompts |
| `references/eval-fixtures.md` | Runnable scenarios |

**Degrees of freedom.**

| Freedom | Locked or open |
|---|---|
| Low | Identity, gates, dates, paths, verify script, section membership |
| Medium | Which 3–5 survivors to keep, domain-spread preference, gap-fill queries |
| High | Headline phrasing and why-it-matters |

**Authoring order.** Write the eval fixtures *before* the SKILL.md body. Minimum fixtures:

1. First-ever run (empty folder) → day folder + `report.md`, 3 sections, required fields
2. Same identity in last 2 reports, no dated delta → not in any main section; Still circulating only if re-proposed and ≤7 days
3. >7-day item, no delta → absent everywhere
4. Undated finding → absent
5. Main-section identity collision with either of the last 2 reports → verify script fails

**Harness.** Runtime is opencode. Orchestration is described as "spawn the wave-lead with this spec; leaves use the harness web-research skill." Do not mention pi. No dual-harness code path.

## What Success Looks Like

1. Given a first-ever run (no prior reports), when generation completes, then a day folder exists with a `report.md` that has 3 main sections and every item carries headline, why-it-matters, source link, and published date. Item count may be 1–5 per section; padding to 3 is a failure.
2. Given an identity that appeared in a main section of either of the last 2 reports with no passing update, when the next run completes, then that identity appears in no main section.
3. Given a streak-hit identity published ≤7 days ago that was proposed again and failed the update test, when the run completes, then it appears in Still circulating (≤10, newest published first) or the section is omitted if none qualify.
4. Given a streak-hit or >7-day-old identity that passes the update test, when the run completes, then it appears in a main section framed as an update with the delta cited, and the update's own date is ≤7 days.
5. Given an item published >7 days ago with no passing update, when the run completes, then it appears nowhere in the report.
6. Given a finding without a verifiable published date, when the run completes, then it is absent from the report.
7. Given any run, when verification runs, then no main-section identity matches a main-section identity from either of the last 2 reports unless the update test passed (deterministic script check).
8. Given any run, when it completes, then `index.md` has today's row (created if missing; upserted on rerun) and chat received the path + 3 glance bullets.
9. Given a completed `report.md`, a reader can name the day's 3 headlines from the glance block in under a minute, and finish the file in 15 minutes without scrolling through methodology.
10. Given a same-day rerun, when it completes, then today's `report.md` was overwritten, inventory ignored today's folder, and `index.md` still has one row for the day.

## What I Already Know

- v1 brief: `b0ttsagent/planning/daily-trends-report-skill/CONTEXT.md`
- Grill session: `b0ttsagent/handoffs/08-17-2026/1722_daily-trends-report-skill/grill-session-daily-trends-report-skill.json` (name, output folder, manual invocation, quick-scan depth, index, chat highlights, Schedule-Spec boundary)
- Fleet: `.opencode/agents/b0tts-lead-researcher.md`, `.opencode/agents/b0tts-researcher.md`, `.opencode/agent/b0tts-smart-general-agent.md`
- `AGENTS.md` — project conventions and skill-invocation rules
- Skill-authoring bar: `.agents/skills/write-a-skill-v2/SKILL.md`
- Report readability: `.agents/skills/markdown-doc-designs/SKILL.md` (not `DESIGN.md`)

## Constraints & Principles

- Agent-skills standard: progressive disclosure, forward-slash paths, one job, scripts only for deterministic work (cite write-a-skill-v2; do not restate it)
- `disable-model-invocation: true` stays on
- No new agent definitions; writer is the existing smart general agent
- Report files are the source of truth; inventory is a derived parse, not a database
- Schedule Spec V6 is not modified (grill D11)
- No personalization section (grill Q1/D6)
- Evidence discipline: undated items dropped; no invented dates or links (b0tts-researcher contract)
- Thin day > padded day. Ship short rather than fill

## Assumptions

- Runtime harness is opencode
- Manual invocation via `/skill:daily-trends-report`; no scheduling
- The digest filename inside the day folder is `report.md`
- Day folders stay `MM-DD-YYYY` under the existing `AI-Development Trends` path (space in the folder name is accepted)
- The 15-minute reading budget still holds; if reading habits change, item budgets adjust
- Script language is Python, stdlib-only if possible

## Open Questions

1. Which named timezone is "today" and the 7-day window? (Required before the recency script can be correct.)
2. Exact per-leaf search cap and page-read cap for a bounded run?

## Non-Goals

- Scheduling / cron automation
- Personalized "what this means for you" section
- New report sections or rotating spotlight domains
- Treating domain lists as a coverage quota
- A separate state database for dedup
- Applying `DESIGN.md` to the reports
- Mentioning pi or maintaining a dual-harness path
- Cleanup of the day folder
- Modifying Schedule Spec V6 or any existing agent definition
- Publishing to an issue tracker
- Auto-invoking the skill from a loose "report" request (`disable-model-invocation` stays true)
