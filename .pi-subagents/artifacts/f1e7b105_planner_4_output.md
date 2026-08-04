Now I have a thorough understanding of the project conventions. Let me compile the plan.

---

# Implementation Plan

## Goal
Add a `code-review` skill to `.agents/skills/code-review/SKILL.md` that teaches agents how to perform structured, severity-graded code reviews with concrete file-level findings.

## Tasks

### 1. **Plan the skill with `create-planning-docs`**
   - **What**: Harvest requirements (review scope, severity taxonomy, output format, negative boundaries) and write CONTEXT.md + PLAN.md into `b0ttsagent/planning/code-review-skill/`. This gate-checks the spec before any skill file exists — the skill should specify *what* it reviews (PRs? architectural? security?), *how* it reports (inline? separate report file?), severity levels (blocker / major / minor / nit), and what it explicitly refuses to do (e.g., "NOT for writing fix commits — review only").
   - **Files**: `b0ttsagent/planning/code-review-skill/CONTEXT.md`, `b0ttsagent/planning/code-review-skill/PLAN.md`
   - **Acceptance**: Both docs approved; CONTEXT nails scope and boundaries; PLAN has phased checkboxes with exit gates.

### 2. **Author the skill using `write-a-skill-v2` conventions**
   - **What**: Following the approved PLAN, create `.agents/skills/code-review/SKILL.md` with YAML frontmatter (`name: code-review`, third-person description with trigger phrases like "review this code", "code review this PR", "audit for bugs" + a `NOT for` boundary excluding implementation tasks), a numbered workflow (gather context → inspect changed files → classify findings by severity → report), a copy-in checklist the agent ticks off, and a findings template that enforces concrete file paths and severity labels. Keep SKILL.md under 500 lines; push reference material (severity taxonomy, example reports) to `references/`.
   - **Files**: `.agents/skills/code-review/SKILL.md`, optionally `.agents/skills/code-review/references/severity-guide.md`
   - **Acceptance**: Frontmatter valid per `write-a-skill-v2` checklist; description fires on natural code-review triggers; agent can produce a findings report with file paths, line references, and severity labels.

### 3. **Validate and integration-test**
   - **What**: Run the `write-a-skill-v2` final checklist (name ≤64 chars, valid charset, matches parent dir, third-person description, body <500 lines, one-level-deep references, one job only, no time-sensitive info, concrete examples present). Then test in a fresh session: issue a natural code-review trigger against a known-buggy file and verify the agent loads the skill, follows the workflow, and produces findings with concrete file paths + severities. Feed any misfires back into the skill.
   - **Files**: None new (verification-only step)
   - **Acceptance**: Checklist all-green; fresh-session test produces at least one finding with a file path and a severity label (e.g., `blocker: src/auth.ts:42 — missing null check`).

## Files to Modify
- None — this is a net-new skill.

## New Files
- `b0ttsagent/planning/code-review-skill/CONTEXT.md` — what the skill does, scope, success criteria, boundaries
- `b0ttsagent/planning/code-review-skill/PLAN.md` — phased authoring plan with checkboxes and exit gates
- `.agents/skills/code-review/SKILL.md` — the skill: frontmatter + workflow + checklist + findings template
- `.agents/skills/code-review/references/severity-guide.md` *(optional, only if >500 lines in SKILL.md)* — severity taxonomy and example reports

## Dependencies
- Task 2 depends on Task 1 (skill authoring follows the approved PLAN).
- Task 3 depends on Task 2 (validation tests the written skill).

## Risks
- **Ambiguity — review scope**: The user hasn't specified what kind of code review (PR review vs. architectural audit vs. security review). The planning step (Task 1) must resolve this before authoring. If left broad, the skill will trigger too often and misfire.
- **Ambiguity — output target**: Whether findings go into a standalone file, inline in chat, or both affects the workflow design. Must be resolved during planning.
- **Trigger collision**: A too-broad description (e.g., "review code") may cause the skill to fire on unrelated tasks. The `NOT for…` boundary in the description is critical.
- **Token budget**: A thorough review workflow (collecting context, inspecting every changed file, classifying findings) could produce long agent turns. The workflow should batch where possible and push verbose reference material into `references/`.
- **Fresh-session test reliability**: Testing trigger behavior requires a genuinely fresh session — stale context from this session could mask description problems.

---