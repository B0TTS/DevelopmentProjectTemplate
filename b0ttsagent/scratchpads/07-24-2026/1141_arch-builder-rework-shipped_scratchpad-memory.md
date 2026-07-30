# Scratchpad — Branch 1: Memory files
**Session:** arch-builder-rework-shipped
**Date:** 07-24-2026 11:41

## Categories identified
- user-environment-facts
- user-workflow-preferences
- corrections-applied
- shipped-state-changes

## Extraction

### user-environment-facts
- User reads design docs in VS Code split view (source + preview); the preview pane is ~600–900px wide. Mermaid SVGs scale to container width (`max-width: 100%`), so wide diagrams shrink to unreadable text while tall diagrams scroll for free — width is the scarce resource, height is free. Context: stated in the prior session's handoff (reading-context section) and re-read this session from `b0ttsagent/handoffs/07-24-2026/mermaid-grill-decisions-arch-builder.md`; it drove the locked Q1 decision and the chains-TD/DAGs-LR geometry rule. Reason: this is a durable cross-project fact about the user's environment that should inform ANY future diagram, doc, or visual-layout work — not just this rework. The geometry rule is now canonized in the mermaid-diagrams skill, but the underlying environment fact (and *why*) belongs in user memory.
- Supporting corollary established this session: pastel fills + dark text (~8:1 contrast) remain legible when SVGs scale down in narrow panes; saturated fills + white text (~2.3:1, fails WCAG) smear. Context: computed during the Q6.1 palette grill from the two real palettes (GLM doc vs handoff redesign). Reason: the palette canon lives in the skills now, but the contrast heuristic generalizes to any future color choice for rendered-down visuals.

### user-workflow-preferences
- In interview/grill-style sessions, the user wants recommendations auto-accepted for decisions the model judges mechanical/technical ("hard ones"), and only visual-design / UI-UX questions escalated for their input. Exact words: "lets speed this up lets take your recc for ones you think are hard. Just leave like visual design UI/UX questions for me." Context: said mid-grill after Q6.1, when the remaining queue was mostly mechanical sub-decisions. Reason: durable interaction preference — re-deriving it each session wastes the user's time and ignores an explicit instruction; it changes how grill-me (and similar interview loops) should pace questions for this user.
- Related pacing signal: user explicitly asked to "speed this up" — one-at-a-time questioning has a patience ceiling when recommendations are strong. Context: same message. Reason: same root cause as above; folded into one proposal.

### corrections-applied
- `mermaid-diagrams/EXAMPLES.md` templates #1 and #2 shipped YAML `---` config blocks that break GitHub/VS Code renderers — a live bug contradicting the REFERENCE.md compat fix from the prior session (the prior fix updated REFERENCE.md but missed EXAMPLES.md). Fixed this session: template #1 config stripped (classDef carries styling), template #2 converted to `%%{init: {'theme': 'forest'}}%%`, header note added to prevent regression. Context: flagged in the handoff as a live bug; fixed during implementation. Reason: the fix is complete and lives in the file — no ongoing memory needed beyond noting the sibling-file-propagation failure pattern (a fix applied to one file didn't reach its sibling); that pattern is a process lesson, not a fact to store.

### shipped-state-changes
- The systems-architecture-builder rework (planned in the prior session's handoff, "Implementation Plan" items 1–5) is now fully shipped: template rewritten as a full worked skeleton, builder SKILL.md gained classification + routing + compressed diagram rules, mermaid-diagrams SKILL.md gained 4 generic checklist lines, EXAMPLES.md bug fixed. Context: this session's implementation work. Reason: project-state change worth recording in the session log; the canon itself lives in the skill files (single source of truth), so no separate memory edit should duplicate it — recording rationale here to justify a light memory footprint.

## Gleaning Pass

### user-environment-facts
- Re-checked the full conversation, especially the handoff quote in message 1 (reading-context paragraph) and the Q6.1 palette message: no additional environment facts missed. The extraction covers the split-view width constraint, the SVG scaling behavior, and the contrast corollary. No other hardware/editor/OS facts appear (Windows is known from paths but already obvious to any session).

### user-workflow-preferences
- Re-checked messages 2–5 (Q6 confirm, Q6.1 answer, the "speed this up" message, ghost-style approval): the delegation preference and pacing signal are the only workflow preferences expressed. The user's terse approval style ("your recc works", "yeah that works sounds good") confirms but does not add a new preference. No others qualify.

### corrections-applied
- Re-checked the implementation phase and both handoffs for other things-wrong-and-fixed: the stale trigger #3 reference in mermaid-diagrams SKILL.md (`graph TD` scaffold) was also corrected this session, and a latent stray `Start --> Wave1` node in EXAMPLES.md template #1 was removed. Both are same-file fixes requiring no memory entry — the EXAMPLES.md YAML item is kept as the representative correction because it reveals the sibling-file-propagation pattern. No memory-edit proposals arise from any of these.

### shipped-state-changes
- Re-checked the final verification greps and summary message: the shipped file set is complete and accurate as extracted (4 files). No additional state changes (no new files outside the two skills, no deletions, no renames). Session log will carry this; no AGENTS.md edit proposed because duplicating skill-internal canon into memory invites drift.

## Triple-check note
Not activated — gleaning found qualifying context in every category, and no category was empty.
