# Handoff: `build-schedule-sheet` Skill

## Purpose

The next session should create a self-contained Agent Skill named `build-schedule-sheet`. The skill will create **Weekly Schedule Sheets** from canonical **Schedule Spec** Markdown documents.

The design/grilling session is complete. The authoritative transcript and approved summary are stored in:

`C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\handoffs\07-31-2026\grill-session-weekly-schedule-guide-skill-2.json`

Do not treat this handoff as authorization to skip review or silently expand scope. The next session should implement the agreed skill, validate it, and report residual risks.

## Accomplished decisions

### Terminology and scope

- Input documents are **Schedule Specs**.
- Generated documents are **Weekly Schedule Sheets**.
- Skill name and directory: `build-schedule-sheet`.
- Primary scope is creating new sheets from an input spec.
- Updating an existing sheet is not a separately designed workflow; an agent can use the creation workflow to generate a new sheet from a newer spec.
- The skill does not edit Schedule Specs, act as a general planning skill, or silently convert legacy prose documents.

### Naming and source selection

- Automatic discovery recognizes only `Schedule Spec V*.md`.
- `Schedule Architecture` is deprecated as an automatic filename pattern.
- An explicit legacy path may be used during migration, but normal operation requires a canonical Schedule Spec.
- Output is saved beside the selected source by default, unless an explicit destination is supplied.
- Output filenames are lowercase and preserve the source content version:

```text
Schedule Spec V4.1.md
→ weekly-schedule-sheet-v4.1.md
```

- Version conflicts, missing version metadata, ambiguous version parsing, and unsafe normalization are blockers.
- Existing output collisions are blockers. The skill must never overwrite silently; the user must choose another destination, explicitly approve replacement, or cancel.

### Canonical Schedule Spec format

The Schedule Spec remains Markdown for human context, but contains an authoritative strict JSON block:

````md
# Schedule Spec V4.1

## Human-readable context

Supporting notes may appear here.

```schedule-spec
{
  "format_version": 1,
  "content_version": "4.1",
  "calendar": {
    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    "free_day": "sun"
  },
  "tasks": []
}
```
````

Rules:

- The JSON block is authoritative.
- Surrounding prose is supporting context only and must not override structured values.
- `format_version` identifies the schema version and supports future schema migrations.
- `content_version` identifies the schedule/spec version and drives output naming.
- Every task requires a unique stable machine `id`, separate from its human-readable `name` and numeric display `order`.
- Explicit day assignments are authoritative; frequency is derived from them.
- Ordinary tasks may use a `days` array.
- Tasks with different durations by day or multiple occurrences on one day should use explicit assignment records.
- Durations are stored as integer minutes.
- The skill package should include its own canonical Schedule Spec template.
- An unknown or unsupported `format_version` is a blocker unless an explicit known migration exists.

### Intermediate model and deterministic processing

The implementation should use three conceptual stages:

1. Parse the Schedule Spec JSON block.
2. Normalize it into an intermediate schedule model.
3. Validate, calculate, and render the Weekly Schedule Sheet.

Deterministic scripts should own parsing, normalization, validation, calculations, and rendering wherever practical. The model should handle user interaction, source selection, genuine ambiguity resolution, preflight presentation, approval, and explanation of findings—not manual arithmetic across a long document.

Validation must block generation for issues such as:

- Missing required fields
- Duplicate task IDs
- Unknown categories or days
- Invalid durations
- Contradictory day assignments
- Parent/subtask duration conflicts
- Negative or ambiguous flex time
- Unsupported schedule models
- Missing or conflicting source versions
- Invalid category assignments
- Missing or invalid calendar/free-day data
- Unknown schema versions

Non-blocking warnings must still be shown in the preflight and require explicit approval before the final sheet is written.

### Free-day accounting

This is an important rule:

- Infer the designated free day from each Schedule Spec.
- Show that day in the generated sheet.
- Exclude free-day accounting from weekly totals, averages, percentages, rankings, flex calculations, and other aggregates by default.
- Include free-day accounting only when the user explicitly requests it.
- Do not infer that the user wants free-day accounting merely because the Schedule Spec describes a free-day budget.
- The provenance/legend must state the active accounting mode clearly.
- Missing, invalid, or structurally incompatible free-day data is a blocker.

### Output contract

The skill must define the output contract inside its own package. It must not depend on `weekly-scheduleV5.md` or another external example at runtime.

The generated Weekly Schedule Sheet should include:

1. Provenance metadata
2. Legend and accounting rules
3. Master weekly time summary
4. Ordered daily schedule tables for the seven-day calendar
5. POW breakdown
6. POF breakdown
7. Sleep breakdown
8. Task-to-day matrix
9. Ranked weekly task hours
10. A task-details/execution-notes section for actionable subtasks and notes

Do not generate:

- Insight Highlights
- Clarifying Q&A

Daily tables use this layout:

| # | Task | POF | POW | Sleep |
|---|---|---:|---:|---:|

Rules:

- `#` is the source task order/step identity.
- Each task is assigned to one applicable category.
- Rows are generated dynamically from the Schedule Spec.
- Preserve source order in per-day tables and the task matrix.
- Mark `Flex`, `Conditional`, and `NR` clearly.
- Keep longer subtasks and instructions in the associated details section rather than bloating daily tables.
- Subtasks are execution details within a parent by default and are not counted in addition to the parent. An independently scheduled subtask requires its own stable ID.
- Flex behavior must be explicit in the spec. Do not infer flex merely from task names. Calculate only the remainder after required fixed assignments; exclude conditional and NR time by default. Missing or ambiguous flex ownership is a blocker.
- Conditional tasks remain visible but do not enter fixed accounting by default. They may count only when explicitly requested or explicitly marked required.
- NR tasks remain visible as recommendations with zero scheduled minutes and are excluded from totals, rankings, flex calculations, and percentages.

Durations are calculated internally as integer minutes and rendered everywhere in human-readable form:

```text
90 minutes → 1h 30m
30 minutes → 30m
8 hours → 8h
```

Do not use decimal-hour notation in the generated sheet.

Suggested provenance block:

```md
> **Source Spec:** `Schedule Spec V4.1.md`
> **Spec Version:** `4.1`
> **Format Version:** `1`
> **Built By:** `build-schedule-sheet`
> **Free-Day Accounting:** Excluded by default
```

### Approval workflow

The skill should:

1. Resolve the input source.
2. Parse and normalize the Schedule Spec.
3. Validate the model and calculate the output.
4. Create a temporary draft under `b0ttsagent/temp/`.
5. Show a concise preflight containing source, version, output path, generated sections, validation status, warnings, and blockers.
6. Stop on blockers.
7. Require explicit user approval before writing the final output.
8. Recheck output collision before writing.
9. Write the final Weekly Schedule Sheet only after approval.
10. Never overwrite an existing output silently.

## Recommended package structure

Create the skill under:

`.agents/skills/build-schedule-sheet/`

Recommended contents:

```text
build-schedule-sheet/
├── SKILL.md
├── references/
│   ├── schedule-spec-contract.md
│   └── schedule-sheet-contract.md
├── scripts/
│   ├── parse-spec.js
│   ├── validate-spec.js
│   ├── build-sheet.js
│   └── validate-sheet.js
└── assets/
    └── schedule-spec-template.md
```

Use judgment about whether all scripts are needed in the first implementation. Do not add speculative complexity; the scripts should solve deterministic, repeated work. Keep `SKILL.md` under 500 lines and use progressive disclosure.

## Reference files examined

- Current source example: `b0ttsagent/Notes/Schedule Architecture V4.1.md`
- Current output example: `b0ttsagent/Notes/weekly-scheduleV5.md`
- These documents informed the output shape, but the new skill must define its own contract and must not require either file at runtime.

## Required authoring protocol

Before implementation, follow the repository’s skill rules:

- Use the `write-a-skill-v2` skill.
- Apply the `karpathy-guidelines` skill.
- Use surgical changes and avoid modifying unrelated files.
- Define success criteria before coding.
- Validate the skill package and scripts after writing.
- Prefer a minimal first implementation that fully satisfies the agreed contract over speculative generalization.

## Open implementation choices

The major product/design decisions are resolved. Implementation details may be chosen by the next agent using the authoring protocols, including:

- Exact JSON schema field structure for subtasks, assignments, flags, notes, and flex declarations.
- Exact validation script interfaces.
- Exact renderer implementation.
- Whether to use one combined deterministic script or several focused scripts.
- Exact wording and numbering of output headings, as long as the semantic output contract remains intact.

Do not reopen resolved terminology, scope, naming, free-day accounting defaults, output sections, or approval behavior unless new evidence exposes a contradiction.

## Suggested next-session opening

Read this handoff and the approved grill session log, then inspect the current skill-authoring files. Build the self-contained `build-schedule-sheet` package, validate it against at least three realistic scenarios, and report changed files, commands/tests run, and any residual risks. Do not build a schedule sheet itself unless needed as a test fixture; the immediate deliverable is the skill.
