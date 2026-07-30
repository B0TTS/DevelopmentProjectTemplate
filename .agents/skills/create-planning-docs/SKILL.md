---
name: create-planning-docs
description: Harvest the prior conversation into a 3-doc planning set (CONTEXT.md, PLAN.md, REFERENCES/RESEARCH.md) written one doc at a time with a mandatory per-doc outline gate and an optional post-write review. REFERENCES is skipped when no new research was done. Use when user wants to plan execution, create planning docs, says "let's plan this out", "write up the plan", "plan before coding", "make the planning docs", or before any multi-phase implementation.
---

# Planning Docs

Harvest the current conversation into a 3-doc planning set, one doc at a time. Each doc has a **mandatory outline gate** (approve sections before writing) and an **optional post-write review** (batch-able when you're confident). Optionally ask one batched clarifying round first if the conversation has gaps that would make the outline wrong.

## Doc set (always this order)

1. **CONTEXT.md** — what and why. Not how. Optional sections: "Constraints & Principles" (task-specific constraints that gate the plan — persistent project rules belong in `AGENTS.md`/constitution, cite by path), "Key Terms" (project-specific jargon), "Assumptions" (decided-by-default choices; treated as decided, override if wrong — distinct from Open Questions), "Open Questions" (must resolve before or during execution). Cite prior on-disk artifacts by path, don't re-summarize. Prefer measurable success criteria.
2. **PLAN.md** — executable how. Opens with a compact **Technical Context** block (Language/Version, Primary Dependencies, Storage, Testing, Target Platform, Performance Goals, Constraints, Scale/Scope — each with `[NEEDS CLARIFICATION]` fallback when unspecified): quick-reference that doesn't rot. Then phased body with checkboxes, exit gates per phase, `[P]` markers on parallelizable steps, and a sequencing summary table. Ends with a **Complexity Tracking** table (`| Violation | Why Needed | Simpler Alternative Rejected Because |`) — any constraint violation or over-engineering must be explicitly justified there. Progressive disclosure: prefer symbol names + file paths over line numbers (line numbers rot); push code excerpts to REFERENCES. Optional per-phase "Risk / Rollback" for irreversible ops. Two valid phase organizations: **technical-layer** (for refactors — credential → transport → payload) or **user-story** (for features — US1/P1 MVP → US2/P2 → US3/P3, each independently shippable with its own Independent Test and checkpoint); pick the one that fits the task.
3. **REFERENCES/RESEARCH.md** — new research from this session only: inventories, rationale, walkthroughs, conflict maps. Skippable when no new research. Exclude: directory listings, code style, anything inferable from codebase or already in CONTEXT/PLAN.

REFERENCES may be skipped when no new research was done; CONTEXT and PLAN are not skippable.

## Writing rules (all docs)

Apply these to every doc in the set:

- **Mark ambiguity, never invent an answer.** When the conversation leaves something unspecified, write `[NEEDS CLARIFICATION: specific question]` inline rather than guessing a plausible default. A flagged question is reviewable; a silent assumption is not.
- **Right altitude.** Each section should be specific enough to guide behavior, flexible enough to not be brittle. Not so detailed it rots on the first change; not so vague the agent can't tell what "done" looks like. The Goldilocks zone.
- **Cite persistent principles, don't re-state them.** Project-wide rules ("use the framework directly," "build must stay green") belong in `AGENTS.md` or a constitution file — cite by path. Only task-specific constraints go in CONTEXT. Same principle as citing prior on-disk artifacts: don't duplicate what already lives somewhere authoritative.

## Workflow

### Step 1 — Output directory

1. Ask which base path (default: `b0ttsagent/planning/`).
2. Generate **3 candidate directory names** based on the task; mark one "(Recommended)".
3. User confirms; create the directory + `REFERENCES/` subdirectory.

### Step 2 — Harvest & clarify

- **Harvest**: scan the current conversation for the task's what/why, scope, success criteria, cited artifact paths, and any research done. This is the primary input — don't re-interrogate from scratch.
- **Optional clarifying round**: if gaps would make the *outline itself* wrong (scope unclear, success criteria absent, WHAT/HOW confused, cited artifact missing, REFERENCES skip undecidable), ask one batched round of ≤5 questions. Otherwise go straight to outline. Detail-level gaps become Open Questions in CONTEXT, not clarifying questions.
- Run the self-review checklist (see [EXAMPLES.md](EXAMPLES.md)) internally before presenting the CONTEXT outline.

### Step 3 — Per-doc loop

Repeat for CONTEXT.md → PLAN.md → (REFERENCES/RESEARCH.md if not skipped):

**A. Present section outline (pre-write gate — mandatory)**
- Bullet list of headers/sections, one line each describing content.
- For PLAN.md: include proposed phase list with one-line summaries.
- For REFERENCES: include proposed reference section titles.
- Do NOT write yet. See [EXAMPLES.md](EXAMPLES.md).

**B. Wait for outline approval**
- User approves, adjusts, or rejects. If adjusted, re-present before writing.
- Only proceed to writing on explicit approval.

**C. Write the doc**
- Write to the agreed path.
- Apply the writing rules above (Doc set descriptions + Writing rules section).

**D. Report (post-write review — batch-optional)**
- Report the doc's path + size.
- If the user pre-authorized batch mode ("write all, review at end"), continue to the next doc's outline without stopping.
- Otherwise pause for review. If the user requests changes, edit and re-report.
- Always pause after the final doc for a closing review.

### Step 3.5 — Cross-doc consistency check (3rd gate)

After the final doc is written but **before** closing, run the cross-doc consistency checklist internally and report any failures to the user for resolution before suggesting next steps:

- Every Open Question in CONTEXT maps to a PLAN phase that resolves it (or is explicitly marked deferred with a reason).
- Every success criterion in CONTEXT is covered by a PLAN exit gate that verifies it.
- Every REFERENCES section is cited from CONTEXT or PLAN (no orphan research the agent would never load).
- No CONTEXT constraint is violated by a PLAN phase — or the violation is recorded in PLAN's Complexity Tracking table with justification.
- WHAT/HOW separation still holds: no tech stack leaked into CONTEXT, no rationale dumped into PLAN beyond the Strategy section.
- Every Assumption in CONTEXT is either consistent with PLAN or flagged as a contradiction to resolve.

If any fail, surface them as a batched list and let the user decide: fix the docs, or accept and record the exception. Do not proceed to Step 4 with silent inconsistencies. See [EXAMPLES.md](EXAMPLES.md) for the checklist form.

### Step 4 — Close

After the final doc is approved and the consistency check passes:
- List the written paths.
- **Living-document note**: if a constraint is violated or an assumption turns wrong during execution, update CONTEXT.md before continuing — stale CONTEXT is actively harmful.
- Suggest the next step (e.g., "Ready to start Phase 0 — give the go-ahead.").
- **Convergence follow-up offer** (structured, not a one-liner): offer to audit the codebase against these docs after implementation. The audit checks: each phase exit gate passes in code, each CONTEXT success criterion is met, no scope creep beyond PLAN, and REFERENCES rationale still holds. Output is a drift report plus remaining work appended as new tasks — say the word to run it.

## Anti-skip rules

- Never write a doc without an approved outline first.
- Never invent the output directory name — offer 3 candidates, let the user pick.
- Never proceed to the next doc on assumption — wait for explicit approval ("approved", "looks good", "continue", "go ahead").
- Never write more than one doc per *outline* approval; post-write review may be batched if pre-authorized.
- Never collapse the outline gate — it's mandatory. Only the post-write review is batch-optional.
- Never re-derive findings already captured in a cited on-disk artifact — cite by path instead.
