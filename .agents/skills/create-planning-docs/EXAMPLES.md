# Planning Docs — Examples

Concrete examples of what a good **section outline** (pre-write gate) looks like for each of the three docs. Use these as calibration, not as literal templates — the sections must match the actual task.

## CONTEXT.md outline example

Presented to user before writing CONTEXT.md:

```
CONTEXT.md will contain:

- **What I Want** — one-paragraph statement of the end goal in the user's voice
- **Scope** — what's in scope (specific changes) and out of scope (explicit exclusions)
- **What Success Looks Like** — numbered, testable success criteria (prefer measurable; Given/When/Then when possible — see success-criteria section below)
- **What I Already Know** — citations to prior analysis by path (e.g., `b0ttsagent/handoffs/.../analysis.md` identified X); gaps in that analysis
- **Constraints & Principles** *(optional)* — task-specific constraints that gate the plan (e.g., "no new shared constants for this feature"). Persistent project rules ("build must stay green", "use the framework directly") belong in `AGENTS.md` or a constitution file — cite by path, don't re-state.
- **Key Terms** *(optional)* — project-specific jargon definitions (e.g., "fingerprint = the set of identifiers Google correlates across users")
- **Assumptions** *(optional)* — decided-by-default choices made when the conversation didn't specify (e.g., "Assumption: mobile support is out of scope for v1"). Treated as *decided* — override if wrong. Distinct from Open Questions below, which are unresolved and *must* be settled.
- **Open Questions** *(optional)* — unresolved items that must be settled before or during execution, distinct from Assumptions (decided), constraints (known), and non-goals (known exclusions)
- **Non-Goals** — things explicitly not being attempted
```

## PLAN.md outline example — technical-layer organization (for refactors)

Presented to user before writing PLAN.md:

```
PLAN.md will contain:

- **Technical Context** — compact quick-reference block at the top: Language/Version (TypeScript 5.x), Primary Dependencies (existing OAuth client, fetch), Storage (n/a), Testing (vitest, existing suite), Target Platform (Node 20+), Performance Goals (no regression vs baseline), Constraints (no new shared constants, build stays green), Scale/Scope (single repo, ~12 files touched). Use [NEEDS CLARIFICATION] for any field the conversation didn't pin down.
- **Strategy** — the layer-ordering rationale (credential → transport → payload) and the disguise principle
- **Phase 0 — Prep & baseline** — green build, test baseline, branch creation
- **Phase 1 — Credential layer** [P] — shed shared OAuth client (config fields, credentials module, rewire call sites, remove hardcoded project ID, setup docs)
- **Phase 2 — Transport layer** — strip ANTIGRAVITY from headers (Client-Metadata, User-Agent prefix, X-Goog-Api-Client pool)
- **Phase 3 — Payload layer** — strip Antigravity from request bodies (system instruction, body userAgent/requestType, deferred items)
  - **Risk / Rollback** *(optional, for irreversible ops)* — if Phase 3 breaks the live API, revert order: restore requestType first, then userAgent, then system instruction; each is independently revertible
- **Phase 4 — Auxiliary vectors** [P] — version fetch endpoint, OAuth scopes (independent of Phases 1-3, can run in parallel with Phase 2)
- **Phase 5 — Verification & hardening** — build, tests, typecheck, live smoke test, fingerprint audit
- **Phase 6 — Maintenance** — patch re-apply docs, upstream-drift note
- **What we are explicitly NOT doing** — deferred items restated
- **Complexity Tracking** — table of any constraint violations or over-engineering, with justification: `| Violation | Why Needed | Simpler Alternative Rejected Because |` (leave empty if none — its presence is the accountability mechanism)
- **Sequencing summary** — phase / layer / parallelizable / risk-reduced / effort table
```

*[P] = step can run in parallel with other [P] steps (different files, no dependencies). Mark every parallelizable step, not just obvious ones.*

*Progressive disclosure reminder: in the written PLAN, prefer symbol names + file paths (e.g., `getAntigravityHeaders()` in `constants.ts`) over line numbers. Line numbers rot on upstream drift. Push code excerpts and deep detail to REFERENCES.*

## PLAN.md outline example — user-story organization (for product features)

Use this pattern instead of the technical-layer pattern when the task is a product feature with independently shippable user stories, not a refactor. Each story is an MVP slice with its own Independent Test and checkpoint — enabling incremental delivery (P1 ships, then P2, then P3) rather than one big-bang release.

Presented to user before writing PLAN.md:

```
PLAN.md will contain:

- **Technical Context** — Language/Version (Python 3.11), Primary Dependencies (FastAPI, Postgres), Storage (Postgres), Testing (pytest), Target Platform (Linux server), Performance Goals (1000 req/s), Constraints (<200ms p95), Scale/Scope (10k users, ~8 endpoints). Use [NEEDS CLARIFICATION] for any field not pinned.
- **Strategy** — MVP-first: ship US1 (P1) as a standalone slice, validate, then add US2 and US3 incrementally. Each story is independently testable and deployable.
- **Phase 0 — Setup & shared infrastructure** — project init, DB schema framework, routing/middleware, env config. Blocks all stories. Checkpoint: foundation ready.
- **Phase 1 — User Story 1: Create task (P1) 🎯 MVP** — the most critical slice, shippable on its own
  - **Independent Test**: "User can create a task and see it in the list — nothing else needed"
  - **Acceptance (Given/When/Then)**: Given a logged-in user, When they submit the create-task form, Then the task appears in their task list within 1s
  - [P] Tests: contract test for create endpoint, integration test for create-then-list
  - [P] Models: Task model in src/models/task.py
  - Service: TaskService in src/services/task.py
  - Endpoint: POST /tasks in src/api/tasks.py
  - Checkpoint: US1 fully functional and testable independently — ship/demo ready
- **Phase 2 — User Story 2: Assign task (P2)** — builds on US1 but independently testable
  - **Independent Test**: "Given US1 works, user can assign a task to a teammate and it shows on their list"
  - **Acceptance**: Given a task exists, When the owner assigns it to a valid user, Then it appears on that user's list and the owner sees the assignee
  - [P] Tests: contract test for assign endpoint
  - Service: extend TaskService with assign()
  - Endpoint: PATCH /tasks/{id}/assign
  - Checkpoint: US1 AND US2 both work independently
- **Phase 3 — User Story 3: Comment on task (P3)**
  - **Independent Test**: "Given US1 works, user can comment on a task and see the comment"
  - **Acceptance**: Given a task exists, When a user adds a comment, Then the comment appears on the task detail with author and timestamp
  - [P] Tests: contract test for comments endpoint
  - [P] Models: Comment model
  - Service: CommentService
  - Endpoint: POST /tasks/{id}/comments
  - Checkpoint: all three stories independently functional
- **Phase 4 — Polish & cross-cutting** [P] — docs, refactors, perf, security hardening, quickstart validation
- **What we are explicitly NOT doing** — e.g., real-time presence, mobile app, SSO (deferred)
- **Complexity Tracking** — `| Violation | Why Needed | Simpler Alternative Rejected Because |` (empty unless a constraint was violated or over-engineering justified)
- **Sequencing summary** — phase / story / priority / parallelizable / effort table
```

Notes on this pattern:
- Stories are ordered by priority (P1 = MVP, P2 = next slice, P3 = next). The plan executes P1 → P2 → P3 sequentially by default, but tasks *within* each story marked [P] can run in parallel.
- The "Independent Test" per story is what makes incremental delivery safe — you can stop after any checkpoint and have something shippable.
- Pick the user-story pattern when the task delivers user-facing value in slices. Pick the technical-layer pattern (above) when the task is a refactor or architecture change with no user-facing slicing.

## REFERENCES/RESEARCH.md outline example

Presented to user before writing REFERENCES/RESEARCH.md:

```
REFERENCES/RESEARCH.md will contain:

- **§1 Full vector inventory** — 23-row table grouped by layer (A credential / B transport / C payload / D auxiliary) with location, frequency, why-it-matters
- **§2 OAuth setup** — step-by-step Google Cloud console walkthrough for personal credentials
- **§3 System instruction rationale** — why drop it, risk of dropping, alternative if needed
- **§4 UA templates** — Option A Electron-style vs Option B plain Chrome, recommendation
- **§5 VSCode version pool** — expanded 15-20 entry list, single-source-of-truth note
- **§6 Test impact** — which test files will break, fix strategy, grep command
- **§7 Patch re-apply map** — file / symbols / conflict-risk table
- **§8 Open questions** — 4 questions to resolve during live execution

Anti-bloat — do NOT include:
- Directory listings or file-structure maps (the agent can see the codebase)
- Code style rules (a linter's job, not a planning doc's)
- Anything inferable from reading the code
- Anything already stated in CONTEXT.md or PLAN.md
```

## What a bad outline looks like (do not do this)

```
PLAN.md will contain the plan with phases and steps.
```

Why it's bad: no section list, no per-section notes, nothing for the user to approve or adjust. The user cannot catch a missing phase or a misnamed section from this.

## Bad success criteria vs good (do not do the bad ones)

```
Bad:  "Notifications should be fast"
Bad:  "Accounts stop getting banned"
Why:  the agent can't evaluate these — no test, no threshold, no signal of done

Good: "Notification appears in sidebar within 2s of comment save"
Good: "No ban within 30 days of normal use across 3 accounts"
Why:  the agent can check these against an observable outcome

Best: "Given a logged-in user viewing a thread, When another user comments on that thread,
       Then a notification appears in the sidebar within 2s of the comment being saved"
Best: "Given 3 accounts used normally, When 30 days pass, Then zero bans occur"
Why:  Given/When/Then is the most agent-executable form — the agent can translate it
      directly into a test. Use this format when the scenario has a clear state/action/outcome.
```

Some tasks (ban avoidance, exploratory work) genuinely can't promise measurable outcomes on day one. Prefer measurable when possible; mark the rest as Open Questions in CONTEXT rather than faking a threshold. Tier preference: Best (Given/When/Then) > Good (measurable threshold) > Bad (vague — don't use).

## `[NEEDS CLARIFICATION]` marker pattern

When the conversation leaves something ambiguous, mark it explicitly in the doc rather than guessing:

```
Good:  FR-006: System MUST authenticate users via [NEEDS CLARIFICATION: auth method not specified — email/password, SSO, OAuth?]
Bad:   FR-006: System MUST authenticate users via email and password
Why:   the second is a plausible but possibly wrong assumption — the agent invented an answer

Good:  "Decision required: drop the system instruction entirely, or replace with a neutral one? [NEEDS CLARIFICATION: does the model expect an identity prompt?]"
Bad:   "Decision required (see REFERENCES)"
Why:   the second hides the actual question — the user can't tell what needs deciding from a skim
```

## Self-review checklist (run internally before presenting the CONTEXT outline)

Before showing the CONTEXT outline to the user, verify:

- [ ] Scope is stated (in and out)
- [ ] Success criteria are present (measurable if possible)
- [ ] WHAT/HOW separation holds — no tech stack or implementation in CONTEXT
- [ ] Cited artifact paths exist on disk
- [ ] REFERENCES skip is decidable (was there new research in the conversation, or not?)
- [ ] Any ambiguity that would make the outline wrong is either resolved via clarifying round or marked as an Open Questions section

If any fail, either ask a clarifying question (Step 2) or adjust the outline before presenting.

## Cross-doc consistency checklist (run after all docs are written, before closing)

This is the 3rd gate — run it after the final doc is written but before Step 4. It checks the docs are *mutually consistent*, not just that each is internally well-formed.

- [ ] Every Open Question in CONTEXT maps to a PLAN phase that resolves it (or is explicitly marked deferred with a reason)
- [ ] Every success criterion in CONTEXT is covered by a PLAN exit gate that verifies it
- [ ] Every REFERENCES section is cited from CONTEXT or PLAN — no orphan research the agent would never load
- [ ] No CONTEXT constraint is violated by a PLAN phase — or the violation is recorded in PLAN's Complexity Tracking table with justification
- [ ] WHAT/HOW separation still holds: no tech stack leaked into CONTEXT, no rationale dumped into PLAN beyond the Strategy section
- [ ] Every Assumption in CONTEXT is either consistent with PLAN or flagged as a contradiction to resolve

If any fail, surface them as a batched list and let the user decide: fix the docs, or accept and record the exception. Do not proceed to Step 4 with silent inconsistencies.

## Review checkpoint phrasing (post-write, batch-optional)

After writing each doc, the phrasing depends on mode:

**Per-doc mode** (default when not pre-authorized):
> CONTEXT.md is written to `b0ttsagent/planning/FirstFix/CONTEXT.md` (4.8 KB).
> Please review the written content and let me know if it's approved or needs changes before I move on to PLAN.md.

**Batch mode** (when user pre-authorized "write all, review at end"):
> CONTEXT.md written (4.8 KB). Moving to PLAN.md outline.
> [presents PLAN outline immediately]

**Closing review** (always, after the final doc + cross-doc consistency check):
> All docs written:
> - `b0ttsagent/planning/FirstFix/CONTEXT.md` (4.8 KB)
> - `b0ttsagent/planning/FirstFix/PLAN.md` (7.2 KB)
> - `b0ttsagent/planning/FirstFix/REFERENCES/RESEARCH.md` (5.1 KB)
>
> Cross-doc consistency check: [PASS / list any failures here for user resolution]
>
> Please review. Once approved, ready to start Phase 0 — give the go-ahead.
> Living-doc note: if a constraint is violated or an assumption turns wrong during execution, update CONTEXT.md before continuing.
> Convergence follow-up: after implementation, I can audit the codebase against these docs — checking each phase exit gate passes in code, each CONTEXT success criterion is met, no scope creep beyond PLAN, and REFERENCES rationale still holds. Output is a drift report plus remaining work appended as new tasks. Say the word to run it.

Do NOT proceed to the next doc's outline on assumption — wait for explicit approval (or the pre-authorization that enables batch mode).
