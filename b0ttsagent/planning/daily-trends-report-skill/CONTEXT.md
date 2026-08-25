# CONTEXT.md — daily-trends-report skill

## What I Want

A skill — `daily-trends-report` — that, when invoked manually each day, produces a quick-scan digest of the current day's AI trends, software-engineer trends, and productivity content: 3–5 items per section, each a headline + why-it-matters + source link + published date.

The defining promise: every main-section item is **new** information. No item lingers in the main sections beyond a two-day streak; nothing older than 7 days appears anywhere unless it carries a genuine update; repetitive-but-still-relevant items are demoted to a clearly-marked Redundant section instead of being re-served as fresh.

Research is done by orchestrated waves of sub-agents riding on the existing agent fleet, and the finished report lands where the 15-minute "Read the daily AI reports" ritual slot can consume it.

## Scope

In scope:

- The skill itself (instructions, workflow, deterministic helper logic, reference material) per the agent-skills standard
- The daily research orchestration flow (multi-wave sub-agent research)
- The two-gate dedup system (streak gate + 7-day recency gate) and the item routing rules
- The report contract (structure, item schema, Redundant section, index, chat highlights)

Out of scope: everything in Non-Goals.

## Report Contract

The daily deliverable the user reads:

- One dated markdown file per day: `b0ttsagent/reports/daily-reports/AI-Development Trends/<MM-DD-YYYY>.md`
- Three main sections — AI trends, SWE trends, productivity — 3–5 items each, sized for a ~15-minute quick scan
- Item format: headline · 1–2 sentence why-it-matters · source link · published date
- Redundant section at the bottom: streak-hit items still ≤7 days old and still surfacing — ~10 max, sorted newest-published first, compact one-liner format
- `index.md` in the reports folder gains one row per run (date + link)
- A short highlights summary is posted in chat after generation

## Coverage Domains

Enrich-only: no new sections, but each section's research scope is broadened to a fixed domain list. Items should spread across domains — max 2 items per domain per section.

| Section | Domains |
|---|---|
| AI trends | frontier model releases · AI research papers · AI company news · open-source AI · AI policy/regulation · AI infra/hardware |
| SWE trends | security & CVEs · OSS licensing & governance · cloud & pricing · languages & frameworks · web platform & standards · dev tools & editors |
| Productivity | new SWE productivity tools · AI-assisted dev workflows · emerging practices & workflows |

## Settled Decisions

Decisions from this session's Q&A (routing rules are the behavioral heart of the skill):

1. **Structure**: keep the 3 existing sections; enrich via broader domain coverage (see Coverage Domains) — no new sections.
2. **Research orchestration**: orchestrator agent (spawned by the user) → one parallel wave of 3 leaf researchers (one per section) → gap-fill researcher on demand when a section comes up short of 3 items → report written by the smart general agent spawned with a synthesis spec (deliberately not the orchestrator, and not a new agent definition).
3. **Anchors**: Hacker News front page + GitHub Trending are fetched each run and fed to researchers as starting points.
4. **Dedup gates**, checked every run:

   | Gate | Rule |
   |---|---|
   | Streak | An item present in BOTH of the last 2 reports is demoted |
   | 7-day recency | Only items published within 7 days may appear anywhere in the report; undated items are dropped |

5. **Routing**:

   | Condition | Destination |
   |---|---|
   | Fresh, not streak-hit | Main section |
   | Streak-hit + published ≤7d | Redundant section |
   | Streak-hit + published >7d | Excluded entirely |
   | New development, any age | Main section, framed as an update citing the delta |

6. **Redundant section**: persists while the item keeps surfacing and stays ≤7 days old; ~10 max; newest published first. Once demoted, an item can only return to a main section via the new-development path.
7. **Source of truth**: repeat detection is computed from the report files themselves — the last 2 reports. No separate state database.

## What Success Looks Like

1. Given a first-ever run (no prior reports), when generation completes, then a dated report file exists with 3 main sections of 3–5 items each, and every item carries headline, why-it-matters, source link, and published date.
2. Given a topic that appeared in BOTH of the last 2 reports with no new development, when the next run completes, then that topic appears in no main section.
3. Given a streak-hit topic published ≤7 days ago that still surfaces, when the run completes, then it appears in the Redundant section, which holds ≤10 items sorted newest-published first.
4. Given a streak-hit or >7-day-old topic with a genuine new development, when the run completes, then it appears in a main section framed as an update with the delta cited.
5. Given an item published >7 days ago with no new development, when the run completes, then it appears nowhere in the report.
6. Given a finding without a verifiable published date, when the run completes, then it is absent from the report.
7. Given any run, when verification runs, then no main-section source link matches any link present in either of the last 2 reports (deterministic check).
8. Given any run, when it completes, then index.md has a new row for the day and a highlights summary was posted in chat.

## What I Already Know

- Prior design session: `b0ttsagent/handoffs/08-17-2026/1722_daily-trends-report-skill/grill-session-daily-trends-report-skill.json` (skill name/location, output folder, manual invocation, quick-scan depth, index.md, chat highlights, Schedule-Spec boundary)
- Existing agent fleet: `.opencode/agents/b0tts-lead-researcher.md` (wave-lead orchestration + QA), `.opencode/agents/b0tts-researcher.md` (leaf research, evidence discipline, disk-first output), `.opencode/agent/b0tts-smart-general-agent.md` (writer role)
- `AGENTS.md` — project conventions, temp-file location, skill-invocation rules
- Skill-authoring conventions: `.agents/skills/write-a-skill-v2/SKILL.md`
- Report readability rules: `.agents/skills/markdown-doc-designs/SKILL.md` + `DESIGN.md`

## Constraints & Principles

- Skill must follow the agent-skills standard — progressive disclosure, forward-slash paths, one job per skill (per write-a-skill-v2)
- Orchestration described harness-agnostically; the user runs it under opencode
- No new agent definitions — the writer role uses the existing smart general agent
- Reports follow markdown-doc-designs + DESIGN.md
- Schedule Spec V6 is not modified (grill decision D11)
- No personalization section (grill decision Q1/D6)
- Strict evidence discipline: undated items are dropped; no invented dates or links (b0tts-researcher contract)

## Assumptions

- Runtime harness is opencode (sub-agents via its task tool)
- Manual daily invocation; no scheduling
- The ~15-minute reading budget still holds; if reading habits change, item budgets adjust

## Open Questions

1. Exact trigger wording for the skill description (must reliably fire on "generate today's report" and similar phrasing)
2. Whether index.md creation is part of the skill's first-run flow or a one-time manual setup
3. Whether harness-agnostic phrasing should still mention pi given opencode is now the primary runtime
4. Gap-fill target: when a section comes up short of 3 items, should the fill target exactly 3 or up to 5?

## Non-Goals

- Scheduling/cron automation
- Personalized "what this means for you" section
- New report sections or rotating spotlight domains
- A separate state database for dedup (report files are the source of truth)
- Modifying Schedule Spec V6 or any existing agent definitions
- Publishing to an issue tracker (no tracker configured)
