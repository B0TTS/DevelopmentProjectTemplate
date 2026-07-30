# closev2 — Reference

## Scratchpad file format

Every scratchpad file uses this structure:

```markdown
# Scratchpad — Branch <N>: <branch-name>
**Session:** <session-name>
**Date:** MM-DD-YYYY HH:MM

## Categories identified
- <category-1>
- <category-2>
- ...

## Extraction

### <category-1>
- <item>
- <item>
...

### <category-2>
- (none identified)
...

## Gleaning Pass

### <category-1>
- *Re-checked <range>: <result>* — either new items found or justification for none
...

### <category-2>
- *Re-checked <range>: no additional items qualify because <reason>*
...
```

Each item under a category uses a bullet with this structure:
```
- Brief, specific description of the item. Context: what happened in the session. Reason: why it matters.
```

Empty categories are **never deleted** — they stay as `(none identified)` with a gleaning entry explaining why.

---

## Self-taxonomy instructions

Before extracting, the model identifies 3–7 categories that fit the branch and the session. Categories should be:

- **Specific** — not "misc" or "things"
- **Session-aware** — named after what actually happened, not generic placeholders
- **Actionable** — each category should produce items the branch can use

### By branch

**Branch 1 — Memory files:** Look for changes the session made to the project's understanding. Good categories: architectural-decisions, tooling-choices, path-conventions, deprecations, new-facts, corrections, project-state-changes. The scan covers: what was decided, what was learned, what changed, what's now outdated.

**Target files (where edits apply):** Default — `./AGENTS.md`, `~/.pi/agent/AGENTS.md`. Auto-discover — `CONTEXT.md`, `CLAUDE.md`, `.planning/*.md`, `References/NavGuides/*.md`, `docs/adr/*.md`, root `README.md`.

**Branch 2 — New skills:** Look for workflows the model executed that follow a reusable shape. Good categories: repeated-patterns, multi-step-workflows, automation-worthy, config-templates. The scan covers: tasks done more than once, tasks with a clear trigger and output, things a future session would benefit from having templated.

**Branch 3 — Improve skills:** Look at skills actually invoked this session (excluding `/close` and `/closev2`). Good categories: missing-coverage, friction-points, outdated-references, poor-triggering, missing-edge-cases. The scan covers: times the model struggled with a skill, times the skill didn't cover a case, times the skill's instructions were wrong or incomplete.

**Branch 4 — Tips:** Look for meta-level improvements to workflow, tooling, or organization. Good categories: repeated-manual-work, automation-opportunity, organizational-gap, tooling-idea, cognitive-load-reduction. The scan covers: inefficiencies, things the user did manually, things that could be faster or clearer.

---

## Priority ranking rules

The model maps its self-defined categories onto these fixed tiers for each branch, then ranks items accordingly.

### Branch 1 — Memory files
1. **Corrections** — things that were wrong and got fixed
2. **High-impact additions** — new information that would cause friction if forgotten
3. **Deprecations** — things now outdated that should be removed
4. **Decisions** — choices made with reasoning
5. **Elegance/insight** — quality-of-life improvements, clarity

### Branch 2 — New skills
1. **Reusability + QoL** — most frequently reusable, highest time savings
2. **Clear trigger** — well-defined "when to invoke"
3. **Scope focus** — narrow enough to be reliable
4. **Creative/novel** — interesting but less tested

### Branch 3 — Improve skills
1. **Observed painpoint ≈ QoL improvement** — things that caused friction this session
2. **Outdated information** — references that are wrong
3. **Clarification** — ambiguous instructions that slowed the model down

### Branch 4 — Tips
1. **Quick win** — high time/money savings, low effort
2. **Repeated manual work** — things done by hand that could be automated
3. **Error reduction / cognitive load** — things that reduce mistakes or mental overhead
4. **Organization / discoverability** — things that make info easier to find
5. **Nice-to-have** — long-term ideas, lower urgency

Within each tier, prefer items with long-term viability.

---

## Gleaning pass — per-category forcing question

The `## Gleaning Pass` section must have one entry per category from `## Categories identified`. For each category, the model re-reads the conversation and answers:

> **Is there an item in the conversation that fits this category but is NOT in the extraction above?**
> - If yes: add it to the extraction section and note it in the gleaning entry.
> - If no: briefly state where in the conversation you looked (message range or topic) and why nothing qualified. Blanket "re-checked, nothing found" is insufficient.

Example gleaning entry:
```
### architectural-decisions
- Re-checked messages 1-45 (the full skill redesign discussion): no additional architectural decisions missed. The extraction covers per-branch scratchpad, self-taxonomy, file layout, and ranking approach.
```

Example with missed items:
```
### friction-points
- Re-checked the skill invocation at message 12: missed a friction point. The model had to ask clarifying questions about the skill's scope because the trigger description was too broad. Added to extraction above.
```

---

## Triple-check protocol

This ONLY activates when every self-defined category in the Gleaning Pass section has no new items found.

1. Re-read the ENTIRE conversation from the first message to the last.
2. Ignore your categories entirely.
3. List EVERY factual claim, action taken, file edited, tool used, and question asked in the session.
4. For each item in that list, ask: does this belong in the current branch? If yes, add it to the extraction and the gleaning pass. If no, state why not.
5. If after this pass the extraction is still empty: write a paragraph explaining why this specific conversation genuinely had nothing relevant to this branch, referencing specific conversation events.

---

## Proposal loop — full flow

The proposal loop runs after all scratchpads are written and verified. It is the SAME loop for all branches (1–4). Every batch of 3 items is presented with full detail — no condensed one-line summaries, no expand step.

### Per-batch format

Begin each batch with a **batch preview** line listing each item's target and tags:

> `AGENTS.md rule (high-impact / low-effort) · docs/adr/ index (medium-impact / medium-effort) · workflow idea (medium-impact / low-effort)`

Tags show impact and effort: `high-impact`, `medium-impact`, `low-impact`; `high-effort`, `medium-effort`, `low-effort`. If effort is irrelevant (e.g., a mindset shift), omit the effort tag.

Present 3 items at a time. Each item format:

```
**<N>. <target-or-domain>: <one-line-action-summary>** `<category-tag>`
Impact: <one-line statement of what changes if applied — consequences of doing vs not doing>
How: <mechanism — file path, exact content, target location, how it works>
Why: <what happened in the session that surfaced this, and why it matters now>
Risk: <edge case or watch-out, if any; omit if none>
```

Fields in order: Headline → Impact → How → Why → Risk (optional).

**File-based proposals:** target is the primary file path, secondary files go in How. **Non-file proposals (Tips):** target is a domain label (e.g., `Workflow`, `Tooling`, `Organization`, `Mindset`), and the third field is `How to act on this:` instead of `How:`.

After presenting the items, end with a line listing the user's available actions:

> *"Select numbers to approve (numbers, range, or 'all'), or say 'skip' / 'none' to skip this batch, or 'exit' / 'done' to end the loop."*

Apply approved edits immediately for Branches 1–3; for Branch 4 (Tips), just acknowledge.

Mention the scratchpad path after the first batch only: *"Full extraction at `<path>`."*

### Loop end

Loop ends when the user explicitly exits or the pool is exhausted. When the pool is exhausted, ask: *"No more items in this pool. Anything I missed, or shall we move on?"* If user suggests something, add it to the pool and resume the loop. Otherwise, move to the next branch.

Declined or skipped items are gone forever — do not re-propose them.

---

## File layout

```
b0ttsagent/
├── scratchpads/
│   └── <MM-DD-YYYY>/
│       ├── <HHMM>_<session-name>_scratchpad-memory.md
│       ├── <HHMM>_<session-name>_scratchpad-skills.md
│       ├── <HHMM>_<session-name>_scratchpad-improvements.md
│       └── <HHMM>_<session-name>_scratchpad-tips.md
└── sessionlogs/
    └── <MM-DD-YYYY>/
        └── <HHMM>_<session-name>.md
```

`<HHMM>` is the time the close session started, in 24-hour format. All scratchpad files and the session log share the same timestamp and session name.
