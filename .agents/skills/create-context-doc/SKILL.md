---
name: create-context-doc
description: Harvest the prior conversation into a single CONTEXT.md (what and why, not how) written through a mandatory outline gate and an optional post-write review. Use when user wants to capture context only, says "write up the context", "make a CONTEXT doc", "capture the what and why", or "define the problem before coding".
---

# Context Doc

Harvest the current conversation into a single CONTEXT.md. The doc has a **mandatory outline gate** (approve sections before writing) and an **optional post-write review**. Optionally ask one batched clarifying round first if the conversation has gaps that would make the outline wrong.

## The doc

**CONTEXT.md** — what and why. Not how. Optional sections: "Constraints & Principles" (task-specific constraints that gate the plan — persistent project rules belong in `AGENTS.md`/constitution, cite by path), "Key Terms" (project-specific jargon), "Assumptions" (decided-by-default choices; treated as decided, override if wrong — distinct from Open Questions), "Open Questions" (must resolve before or during execution). Cite prior on-disk artifacts by path, don't re-summarize. Prefer measurable success criteria.

## Writing rules

Apply these to the CONTEXT doc:

- **Mark ambiguity, never invent an answer.** When the conversation leaves something unspecified, write `[NEEDS CLARIFICATION: specific question]` inline rather than guessing a plausible default. A flagged question is reviewable; a silent assumption is not.
- **Right altitude.** Each section should be specific enough to guide behavior, flexible enough to not be brittle. Not so detailed it rots on the first change; not so vague the agent can't tell what "done" looks like. The Goldilocks zone.
- **Cite persistent principles, don't re-state them.** Project-wide rules ("use the framework directly," "build must stay green") belong in `AGENTS.md` or a constitution file — cite by path. Only task-specific constraints go in CONTEXT. Same principle as citing prior on-disk artifacts: don't duplicate what already lives somewhere authoritative.

## Workflow

### Step 1 — Output directory

1. Ask which base path (default: `b0ttsagent/planning/`).
2. Generate **3 candidate directory names** based on the task; mark one "(Recommended)".
3. User confirms; create the directory.

### Step 2 — Harvest & clarify

- **Harvest**: scan the current conversation for the task's what/why, scope, success criteria, and cited artifact paths. This is the primary input — don't re-interrogate from scratch.
- **Optional clarifying round**: if gaps would make the *outline itself* wrong (scope unclear, success criteria absent, WHAT/HOW confused, cited artifact missing), ask one batched round of ≤5 questions. Otherwise go straight to outline. Detail-level gaps become Open Questions in CONTEXT, not clarifying questions.
- Run the self-review checklist (see [EXAMPLES.md](EXAMPLES.md)) internally before presenting the CONTEXT outline.

### Step 3 — Outline → write → report

**A. Present section outline (pre-write gate — mandatory)**
- Bullet list of headers/sections, one line each describing content.
- Do NOT write yet. See [EXAMPLES.md](EXAMPLES.md).

**B. Wait for outline approval**
- User approves, adjusts, or rejects. If adjusted, re-present before writing.
- Only proceed to writing on explicit approval.

**C. Write the doc**
- Write to the agreed path.
- Apply the writing rules above.

**D. Report (post-write review)**
- Report the doc's path + size.
- Pause for review. If the user requests changes, edit and re-report.

### Step 4 — Close

After the doc is approved:
- List the written path.
- **Living-document note**: if a constraint is violated or an assumption turns wrong during execution, update CONTEXT.md before continuing — stale CONTEXT is actively harmful.
- Suggest the next step (e.g., "Ready when you are — give the go-ahead.").

## Anti-skip rules

- Never write the doc without an approved outline first.
- Never invent the output directory name — offer 3 candidates, let the user pick.
- Never proceed to writing on assumption — wait for explicit approval ("approved", "looks good", "continue", "go ahead").
- Never collapse the outline gate — it's mandatory.
- Never re-derive findings already captured in a cited on-disk artifact — cite by path instead.
