# Handoff: Spec-to-Sheet Skill Build

## Session artifact

Full grilling transcript with all design decisions:  
`b0ttsagent/handoffs/03-21-2026/grill-session-schedule-guide-generator-skill.json`

## What was accomplished

Designed a skill that generates weekly "schedule sheets" (computed table-driven documents) from "schedule specs" (hierarchical task breakdowns). All design decisions were resolved through a grill-me-v2 session. Nothing was built — the next session implements.

## Decisions locked in

| Decision | Outcome |
|---|---|
| **Input name** | Schedule Spec (`Schedule Architecture V*.md`) |
| **Output name** | Schedule Sheet (`weekly-scheduleV*.md`) |
| **Discovery** | Scan `b0ttsagent/Notes/` for highest-V spec; confirm with user; explicit path overrides |
| **Sheet versioning** | Mirrors spec version (V5.0 spec → V5.0 sheet) |
| **Regeneration** | Full rebuild only, no partial updates |
| **File location** | Flat in `b0ttsagent/Notes/` |
| **Deprecated** | Insight Highlights and Clarifying Q&A removed from sheet output |
| **Approval gate** | Show draft → user approves → write to disk |
| **Skill structure** | `SKILL.md` + `REFERENCE.md`; REFERENCE.md built for long-term scalability |
| **Edge cases** | No spec → ask for path; ambiguous data → stop & clarify; first sheet → note no overwrite; explicit path → skip scan |

## Current state

- Two existing files demonstrate the spec→sheet relationship:
  - Spec: `b0ttsagent/Notes/Schedule Architecture V4.1.md`
  - Sheet: `b0ttsagent/Notes/weekly-scheduleV5.md` (pre-skill, hand-built — versions don't match yet)
- No skill files exist yet. The skill directory needs to be created.

## Suggested skills for next session

- **write-a-skill** — to scaffold and write the actual SKILL.md + REFERENCE.md
- **karpathy-guidelines** — keep the implementation simple and surgical
- **mermaid-diagrams** — if the REFERENCE.md benefits from a parse-flow diagram

## Key files

| File | Role |
|---|---|
| `b0ttsagent/Notes/Schedule Architecture V4.1.md` | Current spec (example input) |
| `b0ttsagent/Notes/weekly-scheduleV5.md` | Current sheet (example output, will be superseded) |
| `b0ttsagent/handoffs/03-21-2026/grill-session-schedule-guide-generator-skill.json` | Full Q&A transcript |

## What to build

A skill named something like `generate-schedule-sheet` that:

1. **SKILL.md** (~80 lines): workflow — scan/confirm spec → parse → compute 13 tables → present draft → write on approval
2. **REFERENCE.md**: spec format documentation (sections, step fields, day notation conventions, sub-step inheritance), table computation rules, sheet template structure

The spec format includes: `## Tips and Information`, `## Stepped Schedule Layout` (numbered steps with category/frequency/duration/days/notes/sub-steps), and `## Schedule Requirements`. Day notations include "Freeday exception" (Mon–Sat), "Erryday" (7 days), comma-separated day names, and single days. Categories: POF, POW, Sleep, NR. The sheet has 13 tables: master summary, 7 per-day schedules, POW breakdown, POF breakdown, sleep breakdown, task-to-day matrix, and weekly ranked totals — plus a legend/key generated from spec definitions.

## Open decisions

None — all design decisions were resolved in the grilling session.
