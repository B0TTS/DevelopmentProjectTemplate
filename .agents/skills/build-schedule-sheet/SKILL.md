---
name: build-schedule-sheet
description: Build a Weekly Schedule Sheet from a canonical Schedule Spec Markdown document (a fenced `schedule-spec` JSON block with format_version + content_version, calendar, budgets, and tasks). Computes daily tables, POW/POF/Sleep breakdowns, a task-to-day matrix, ranked weekly hours, and execution notes from the spec — free-day accounting excluded by default. Use when the user wants to generate, create, or build a weekly schedule sheet from a Schedule Spec, says "build the schedule sheet", "generate the weekly sheet", "make the schedule from the spec", or wants to turn a Schedule Spec into a time-accounted weekly breakdown. NOT for editing Schedule Specs, general schedule planning, or silently converting legacy prose "Schedule Architecture" documents (legacy migration is separate and explicit).
compatibility: requires node
---

# Build Schedule Sheet

Turn a **Schedule Spec** (Markdown with an authoritative `schedule-spec` JSON block) into a **Weekly Schedule Sheet** — a single Markdown file with provenance, legend, master summary, 7 daily tables, POW/POF/Sleep breakdowns, a task-to-day matrix, ranked weekly hours, and execution notes.

The deterministic work (parse, validate, compute flex/totals/ranking, render) is owned by scripts. The agent owns source selection, preflight presentation, approval, collision recheck, and the single gated final write. **Never overwrite an existing output silently.**

## Terms (do not blur)

- **Schedule Spec** — the input. File pattern `Schedule Spec V*.md`. Contains an authoritative fenced `schedule-spec` JSON block. Prose around it is context only.
- **Weekly Schedule Sheet** — the output. Filename `weekly-schedule-sheet-v<content_version>.md` (lowercase, preserves the source `content_version`). Written beside the source by default; an explicit destination overrides.

## References (read one level deep)

- `references/schedule-spec-contract.md` — full input schema, task shapes, subtask rules, flex rules, free-day accounting. **Read this before authoring or debugging a spec.**
- `references/schedule-sheet-contract.md` — exact output sections, table layouts, duration notation. **Read this before changing rendering or arguing about output shape.**
- `references/schedule-spec-example.md` — a complete V4.1 worked spec; copy/edit from this. Also the canonical validation fixture.
- `assets/schedule-spec-template.md` — a minimal blank Schedule Spec skeleton for starting fresh.

## Scripts (run, do not read unless debugging)

Resolve all script paths against this skill's directory. Run with `node` from the project root.

- `scripts/parse-spec.js` — Stage 1. Extracts the `schedule-spec` fenced JSON block and emits a normalized model.
- `scripts/validate-spec.js` — Stage 2. Validates (blockers vs warnings) and computes flex, totals, and ranking. Exits non-zero on blockers; always writes a structured result.
- `scripts/build-sheet.js` — Stage 3. Renders the 10-section sheet to a **draft under `b0ttsagent/temp/`** and prints a **preflight JSON** to stdout. **Never writes the final output** — the agent does, after approval.

## Workflow

Copy this checklist into your reply and tick each step. **Stop on blockers. Stop and wait at every `→ ASK` gate.**

1. **Resolve the source.** `→ VERIFY` one explicit path was given, else find a `Schedule Spec V*.md`. Priority: explicit path → `Schedule Spec V*.md` under `b0ttsagent/Notes/` → directory scan → highest unambiguous version. On missing / tied / ambiguous: `→ STOP and ask the user` which source to use. Do not guess. (Legacy `Schedule Architecture V*.md` is **not** auto-discovered; an explicit path may be used only during migration.)
2. **Decide free-day accounting.** Default = **excluded**. Include free-day accounting **only if the user explicitly requests it** ("include Sunday"), and never merely because the spec declares a free-day budget. `→ VERIFY` this is settled before the next step.
3. **Parse.** Run:
   ```bash
   node .agents/skills/build-schedule-sheet/scripts/parse-spec.js "<source>" --out b0ttsagent/temp/bsst-model.json
   ```
   On parse error: `→ STOP`, report the error, do not continue.
4. **Validate + compute.** Run:
   ```bash
   node .agents/skills/build-schedule-sheet/scripts/validate-spec.js b0ttsagent/temp/bsst-model.json --free-day-accounting excluded --out b0ttsagent/temp/bsst-validated.json
   ```
   (use `included` only when the user explicitly requested it in step 2.) On non-zero exit: `→ STOP`. Read `blockers[]` from the written file, surface every blocker to the user, and do not proceed to build.
5. **Build draft + preflight.** Run:
   ```bash
   node .agents/skills/build-schedule-sheet/scripts/build-sheet.js b0ttsagent/temp/bsst-validated.json
   ```
   Read the preflight JSON from stdout. If `ok:false` (shouldn't happen post-validate, but defense-in-depth): `→ STOP`, surface blockers.
6. **Show the preflight.** Present concisely: source spec, spec/format version, free-day accounting mode, **proposed output path**, generated sections, **warnings** (call out conditional/NR presence explicitly), weekly totals, and the draft path for preview.
7. **Recheck collision.** `→ VERIFY` the proposed `output_path` does not already exist. If it does: `→ STOP and ASK` — offer (a) a different destination, (b) explicit replacement, or (c) cancel. **Never overwrite silently.** Do not proceed until the user explicitly chooses.
8. **Get approval.** `→ ASK` the user for explicit approval to write the final sheet. If warnings are present, approval must acknowledge them. Do not write until you have an explicit yes.
9. **Write the final sheet.** Read the draft file and write its contents to `output_path` using your file-write tool. This is the only destructive step and it is gated.
10. **Confirm.** Report the final written path, the source spec, the free-day accounting mode used, and any residual warnings.

## Rules the agent must enforce (scripts cannot)

- **Source selection** — the priority order and the stop-on-ambiguous gate.
- **Free-day accounting** — the opt-in gate (step 2). The default is excluded; never infer inclusion.
- **Collision recheck** — step 7. The scripts only propose a path; they never write it.
- **Approval** — step 8. No final write without an explicit yes.
- **Single final write** — step 9. The agent performs it, not a script.

## Output sections (fixed order — see `references/schedule-sheet-contract.md`)

1. Provenance metadata · 2. Legend and accounting rules · 3. Master weekly summary · 4. Daily schedule tables (all 7 days) · 5. POW breakdown · 6. POF breakdown · 7. Sleep breakdown · 8. Task-to-day matrix · 9. Ranked weekly task hours · 10. Task details / execution notes. **Insight Highlights and Clarifying Q&A are not generated.**

Durations render as `Xh Ym` (e.g. `1h 30m`, `30m`, `8h`); no decimal-hour notation. Free day is shown (its own daily table + reference columns in breakdowns + matrix) but excluded from weekly totals, averages, percentages, and rankings by default.

## Blockers (generation halts — scripts exit non-zero)

Duplicate task id · missing/invalid free day · invalid calendar · invalid budgets · unsupported budget category · unknown `format_version` · `content_version`/filename version conflict · missing `content_version` · unknown task category · unknown/uncalendar day code · invalid duration · ambiguous task shape (mixed flags) · invalid conditional/NR shape · over budget (per day/category) · unallocated time (no flex owner for a remainder) · ambiguous flex ownership (two flex tasks, one category, one day) · subtask day outside parent · uniform-subtask duration sum ≠ parent. `schedule-spec-contract.md` is authoritative for the full list.

## Warnings (non-blocking — shown in preflight, approval required)

Conditional tasks present (visible, not counted by default) · NR tasks present (0 scheduled minutes, excluded) · flex task with 0 remainder · per-day subtask variance (duration-conflict check skipped, subtask durations advisory).

##_NR / Conditional / Flex defaults_

- **NR** — visible as a recommendation; **0 scheduled minutes**; excluded from totals, ranking, flex, and percentages. Shown in the daily-table NR note and the matrix.
- **Conditional** — visible in daily tables as `0–Xh`, marked `*(conditional)*`, **not counted by default**; counts only when the user explicitly requests it or the spec marks it required.
- **Flex** — `flex: true` + `duration_minutes: "FLEX"`; the single owner of a category's remainder on a day. Never inferred from a task name; the flag is required.

## One job

This skill builds a Weekly Schedule Sheet from a Schedule Spec. It does not edit Schedule Specs, plan schedules, or migrate legacy prose docs. Those are separate tasks.