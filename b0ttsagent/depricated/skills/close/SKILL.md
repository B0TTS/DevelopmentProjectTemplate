---
name: close
description: Close out a coding session by reviewing chat memory and proposing memory-file updates, new skills, skill improvements, helpful tips, and a session log. Use when the user says '/close', 'close this session', 'wrap up', 'end session', or wants to close out the current conversation.
---

# /close

## Quick start

When the user invokes `/close`:

1. Present a multi-select menu of the 5 closing steps.
2. Run selected steps in fixed order: Memory → Skills → Improvements → Tips → Log.
3. For proposal branches (1–4), use the ranked proposal loop.
4. Write the session log last if selected.

## Menu

Present this multi-select menu:

```
What do you want to close with? (multi-select)
[ ] 1. Update memory files    — propose AGENTS.md edits from this session
[ ] 2. Propose new skills     — spot reusable work worth a skill
[ ] 3. Improve skills used    — QoL fixes for skills touched this session
[ ] 4. Helpful Tips           — suggest time-saving systems and QoL ideas
[ ] 5. Write session log      — log to b0ttsagent/sessionlogs/
[ ] 6. All
```

If nothing selected, exit with "Nothing selected, closing."

## Branch 1: Update memory files

- Read the session for memory-worthy items: corrections, additions, deprecations, decisions.
- Threshold: durable + actionable + not already captured elsewhere.
- Ranking: corrections > high-impact additions > elegance/insight > deprecations > decisions.
- Target files:
  - Default: `./AGENTS.md`, `~/.pi/agent/AGENTS.md`
  - Auto-discover: `CONTEXT.md`, `CLAUDE.md`, `.planning/*.md`, `References/NavGuides/*.md`, `docs/adr/*.md`, root `README.md`
- Use the proposal loop.
- On approval, apply the edit directly to the target file.

## Branch 2: Propose new skills

- Identify reusable workflows or QoL improvements from the session.
- Ranking: reusability + QoL (highest), clear trigger, scope focus, creative/novel.
- Check existing skill front matter to avoid exact duplicates. Similar skills are allowed with a quick context note.
- Use the proposal loop.
- On approval, write a complete `SKILL.md` to `~/.pi/agent/skills/<name>/SKILL.md`.
- If the name collides with an existing skill, block and propose an alternative.

## Branch 3: Improve skills used

- Scope: skills actually invoked during this session. Exclude `/close` itself.
- Ranking: observed painpoint ≈ QoL improvement > outdated info > clarification.
- Use the proposal loop.
- On approval, apply the edit directly to the target skill file.

## Branch 4: Helpful Tips

- Identify session-derived ideas for time-saving systems, automation, organization, tooling, or workflow improvements.
- Ranking: quick win (high time/money savings, low effort) > repeated manual work > error reduction / cognitive load > organization / discoverability > nice-to-have. Within each tier, prefer ideas with long-term viability.
- Let the model decide what qualifies; avoid hard-coded heuristics.
- Tips may overlap conceptually with branches 1–3. Deduplicate against items already proposed in this run so the user doesn't see the same suggestion twice.
- Use the proposal loop.
- Present each tip with: category tag, title, observation from the session, recommendation, and estimated impact.
- On approval, acknowledge the tip and continue. Do not generate implementation code; the user can ask for that separately after closing.

## Proposal loop (branches 1–4)

1. Present the top 3 items with full detail (target, rationale, proposed change).
2. User multi-selects which to approve. Apply approved edits immediately (for branches 1–3); for Helpful Tips, acknowledge and continue.
3. Present the next 3 items as one-line summaries.
4. User can expand some, skip the batch, or exit the loop.
5. Loop ends on explicit exit.
6. When the pool is empty, acknowledge it and ask an open prompt: "No more items in this pool. Anything I missed, or shall we move on?"
7. Declined/unselected items are gone forever.

## Branch 5: Write session log

- Run last.
- Generate 3 filename ideas in lowercase kebab-case; recommend one.
- **Pause for user confirmation** — user may choose a different name, adjust the recommended name, or skip entirely.
- Once confirmed, write to `b0ttsagent/sessionlogs/<MM-DD-YYYY>/<HHMM>_<name>.md`
- Use this template:

```markdown
# <selected_name>

**Date:** MM-DD-YYYY  
**Time:** HH:MM  

## What happened
- ...

## Skills used
- ...

## Closing outcomes
- ...

## Open / next
- ...
```

## Edge cases

- **Empty branch**: ask the user whether to skip or write a minimal log.
- **New skill name collision**: block and propose an alternative name.
- **Missing target file**: ask the user whether to recreate the file with the proposed content.
- **Mid-run abort**: no special handling; immediate apply preserves already-approved work.
