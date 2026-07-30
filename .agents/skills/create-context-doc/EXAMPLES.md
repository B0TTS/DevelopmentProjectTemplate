# Context Doc — Examples

Concrete examples of what a good **section outline** (pre-write gate) looks like for CONTEXT.md. Use these as calibration, not as literal templates — the sections must match the actual task.

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

## What a bad outline looks like (do not do this)

```
CONTEXT.md will contain the context with sections.
```

Why it's bad: no section list, no per-section notes, nothing for the user to approve or adjust. The user cannot catch a missing section or a misnamed heading from this.

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
Bad:   "Decision required (see notes)"
Why:   the second hides the actual question — the user can't tell what needs deciding from a skim
```

## Self-review checklist (run internally before presenting the CONTEXT outline)

Before showing the CONTEXT outline to the user, verify:

- [ ] Scope is stated (in and out)
- [ ] Success criteria are present (measurable if possible)
- [ ] WHAT/HOW separation holds — no tech stack or implementation in CONTEXT
- [ ] Cited artifact paths exist on disk
- [ ] Any ambiguity that would make the outline wrong is either resolved via clarifying round or marked as an Open Questions section

If any fail, either ask a clarifying question (Step 2) or adjust the outline before presenting.

## Review checkpoint phrasing (post-write)

After writing CONTEXT.md, the phrasing:

> CONTEXT.md is written to `b0ttsagent/planning/FirstFix/CONTEXT.md` (4.8 KB).
> Please review the written content and let me know if it's approved or needs changes.

Do NOT proceed to writing on assumption — wait for explicit approval.
