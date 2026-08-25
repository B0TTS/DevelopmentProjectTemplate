# Bug-Report Skill — Evaluations

Per `write-a-skill-v2`: run these in a **fresh runner session** (not the
authoring session). Watch what the runner actually does — which files it reads,
which rules it skips, whether it over- or under-explains. Feed observations back
into `SKILL.md`. Skills load at session start, so test triggering fresh each
time.

## The three seams

### Seam 1 — Skill invocation (end-to-end report)

Fresh session. Give a realistic bug report with **most details missing**.

Verify:
- Skill fires on natural-language bug phrasing ("there's a bug…", "X is crashing…").
- Intake asks **only** for gaps (extraction-first), ≤ ~4 questions, batched.
- Dedupe check runs before questioning.
- Read-back summary shown and confirmed before any file is written.
- Document appears at `b0ttsagent/bugs/open/YYYY-MM-DD-slug.md` with front
  matter (`id`, `title`, `severity`, `state: open`, `created_at`) and all prose
  sections.
- Exactly one valid line appended to `b0ttsagent/bugs/bugs.jsonl` with
  `state: open` and `causes: []`.
- Investigation runs read-only (no edit/write); suspected causes appended with
  confidence, `file:line` evidence, and a confirm-test; a **second** registry
  line appended with `causes[]` populated and `updated_at` refreshed.

### Seam 2 — Registry contract (invariant)

After any run, every line in `b0ttsagent/bugs/bugs.jsonl`:
- parses as JSON;
- conforms to the schema (`id`, `state`, `title`, `description`, `causes`,
  `filepath`, `severity`, `created_at`, `updated_at`, `related`);
- `state` ∈ {`open`, `in progress`, `closed`};
- `severity` ∈ {`low`, `medium`, `high`, `critical`, `unknown`};
- `filepath` resolves to an existing file (check both `open/` and `fixed/`);
- latest-wins holds per `id` — `node scripts/query-bugs.js --id <id>` output
  matches the last line for that id.

Quick check: `node scripts/query-bugs.js --json` then parse every line.

### Seam 3 — Mark-fixed path

Fresh session. Say "I fixed bug X, mark it fixed."

Verify:
- Skill routes to mark-fixed (does **not** file a new bug).
- Agent confirms which bug (search + user confirm).
- Document moves `open/` → `fixed/`.
- Front matter `state` → `closed`.
- A new registry line appended with `state: closed` and `filepath` now under
  `fixed/`; `id` unchanged.

## Three scenarios that fail WITHOUT the skill

1. **Bug report with most details missing** — without the skill, the agent
   either writes an incomplete doc or interrogates the user with >4 unbatched
   questions. With the skill: extraction-first, ≤4 batched, "unknown" allowed.
2. **A feature request phrased like a bug** ("it'd be cool if…") — without the
   skill, the agent might file it as a bug. With the skill: refused at the
   negative boundary.
3. **"I fixed the login crash, mark it fixed"** — without the skill, the agent
   might file a NEW bug or edit the registry in place. With the skill: routes
   to mark-fixed, moves the doc, appends a closed line (no in-place edits).

## Self-test checklist (author-side, before sharing)

- [ ] Description: specific, third person, includes what + `Use when…` + a `NOT for…` boundary.
- [ ] `name` ≤ 64 chars, valid charset, matches parent dir, no reserved words.
- [ ] `SKILL.md` body under 500 lines.
- [ ] References one level deep; forward-slash paths; descriptive filenames.
- [ ] One job per skill (report + mark-fixed are one job: bug lifecycle).
- [ ] Degrees of freedom chosen deliberately (intake = high/prose; registry = low/exact).
- [ ] No time-sensitive info; consistent terminology.
- [ ] Concrete input–output pairs included (registry example, template).
- [ ] Scripts solve (don't defer), no magic constants, deps declared (Node only).
- [ ] At least 3 evaluations; to be tested in a fresh session on each target model.
