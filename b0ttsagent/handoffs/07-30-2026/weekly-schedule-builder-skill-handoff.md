# Handoff: Weekly Schedule Builder Skill

## Status

The design/grill session is complete and the user approved the closing summary. Implementation has **not** started.

The complete decision transcript and approved design summary are stored in:

`C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\handoffs\07-30-2026\grill-session-weekly-schedule-guide-skill.json`

Treat that JSON artifact as the authoritative record of the decisions. This handoff intentionally does not duplicate the full decision transcript.

## Accomplished

- Chosen skill name: `weekly-schedule-builder`.
- Defined the output as a concrete **Weekly Schedule**, not primarily a guide.
- Established that the skill creates new schedules by full regeneration.
- Established version mirroring: `Schedule Architecture V4.1.md` → `weekly-scheduleV4.1.md`.
- Decided the skill must be self-contained and must not depend on `weekly-scheduleV5.md` or another external template at runtime.
- Chosen package shape: `SKILL.md` plus a scalable `REFERENCE.md`.
- Defined semantic parsing, an intermediate normalized schedule model, dynamic rendering, and validation-first generation.
- Locked the permanent Sunday/free-day and Monday–Saturday aggregation rules.
- Decided durations are calculated as integer minutes and displayed as hours/minutes everywhere.
- Defined preflight, temporary-draft, collision, ambiguity, warning, and approval behavior.

## Implementation target

Create:

```text
.agents/skills/weekly-schedule-builder/
├── SKILL.md
└── REFERENCE.md
```

`SKILL.md` should be concise and operational: trigger description, source discovery, preflight, parse/normalize/render/validate workflow, pause conditions, approval gate, and output writing.

`REFERENCE.md` should be self-contained and designed for long-term scalability. Use layers such as:

1. Stable terminology and output contract
2. Architecture parsing model and recognized semantic aliases
3. Normalized intermediate schedule model
4. Day/category/duration inheritance rules
5. Conditional, NR, and flex semantics
6. Rendering contract for the Weekly Schedule sections and tables
7. Compatibility gates for unsupported structural changes
8. Validation checklist and invariant rules

Do not hardcode the current 21-step architecture. Generate task rows, labels, IDs, categories, days, durations, and notes from the selected architecture while preserving the established semantic presentation.

## Important source files

- `b0ttsagent/Notes/Schedule Architecture V4.1.md` — current architecture example/source of truth.
- `b0ttsagent/Notes/weekly-scheduleV5.md` — presentation example only; do not make the new skill depend on it at runtime.
- `b0ttsagent/temp/` — location for temporary generated drafts.
- `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\handoffs\07-30-2026\grill-session-weekly-schedule-guide-skill.json` — full approved design artifact.

## Suggested skills for the implementation session

- `write-a-skill-v2` — create and validate the new Agent Skill structure.
- `karpathy-guidelines` — keep the implementation minimal, explicit, and validation-driven.
- `pi-subagents` — optional independent review of the drafted `SKILL.md` and `REFERENCE.md`; keep one writer for the implementation.

## Continuation notes

- Source selection: explicit path/directory takes precedence; a filename alone resolves under `b0ttsagent/Notes/`; missing or ambiguous sources pause for the user.
- Output defaults beside the source. An existing target filename is reported and paused; never overwrite silently.
- A preflight identifies source, version, output, sections, validation findings, and structural changes before any final write.
- All findings pause generation, including warnings. The user may explicitly say `continue` for a clearly non-blocking warning; correctness-impacting issues must be resolved.
- The final schedule is written only after the user approves the draft/preflight.
- The approved design calls for no external template dependency and no need to add a bundled parser/generator script initially; the skill should remain adaptable through its reference contract.

## Relevant inspection command

```bash
node C:/Users/intel/DevelopmentProjectTemplate/.agents/skills/grill-me-v2/scripts/append.js state C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/handoffs/07-30-2026/grill-session-weekly-schedule-guide-skill.json
```
