---
name: closev2
description: Close out a coding session with deep context extraction, memory-file updates, skill proposals, skill improvements, tips, and a session log. Use when user says '/close', 'close this session', 'wrap up', 'end session', or wants to close out the current conversation. Forces exhaustive reflection via per-branch scratchpads before any proposals are made.
---

# /closev2

## Quick start

1. Present menu → user selects branches
2. Propose 3 session names → user picks one
3. Write all selected branch scratchpads upfront, verify them, then run each proposal loop in branch order (Memory → Skills → Improvements → Tips)
4. Run Branch 5 (session log) last
5. If nothing selected, exit with "Nothing selected, closing."

## Step 1 — Menu

Present this menu, exactly as shown:

    What do you want to close with? (multi-select)
    [ ] 1. Update memory files    — propose AGENTS.md edits from this session
    [ ] 2. Propose new skills     — spot reusable work worth a skill
    [ ] 3. Improve skills used    — QoL fixes for skills touched this session
    [ ] 4. Helpful Tips           — suggest time-saving systems and QoL ideas
    [ ] 5. Write session log      — log to b0ttsagent/sessionlogs/
    [ ] 6. All

    I'll do a deep scan of our conversation before proposing anything.

## Step 2 — Session name

Propose 3 filename ideas in lowercase kebab-case. Recommend one. Wait for user confirmation — they may choose a different name, adjust the recommended one, or skip (use a timestamp-only name). This name is used for all scratchpad files and the session log.

## Step 3 — Branch processing

Run selected branches in fixed order: Memory → Skills → Improvements → Tips.

### 3a — Write all scratchpads

Write all selected branch scratchpads upfront, in branch order. For each: use the scratchpad format and self-taxonomy instructions in [REFERENCE.md](REFERENCE.md). Write to `b0ttsagent/scratchpads/<MM-DD-YYYY>/<HHMM>_<session-name>_scratchpad-<branch>.md`.

Each file MUST include a `## Gleaning Pass` section at the bottom. See REFERENCE.md for the per-category forcing question.

**Triple-check:** if every self-defined category in the Gleaning Pass has no new items, run the triple-check protocol in REFERENCE.md.

### 3b — Verify all scratchpads

1. Read each scratchpad file you just wrote.
2. Confirm: each file exists and has a `## Gleaning Pass` section.
3. For any that fail: re-write that scratchpad. If it fails a second time: offer the user (i) retry with a different path, (ii) inline extraction into a visible message, or (iii) skip this branch. Do not skip silently.

### 3c — Proposal loops

For each selected branch, in order: read the branch's scratchpad, rank items using the fixed priority rules (see REFERENCE.md), then run the proposal loop:

1. Present a batch preview line, then 3 items with full detail: headline (target + action), Impact, How, Why, and optional Risk. Format is defined in REFERENCE.md.
2. Mention where the full extraction lives: *"Full extraction at `<scratchpad-path>`."* (once, after the first batch).
3. User multi-selects which to approve.
4. For Branches 1–3: apply approved edits immediately. For Branch 4 (Tips): acknowledge and continue.
5. Present next 3 items with the same full-detail format. Every batch gets full detail — no one-line summaries.
6. User can approve (multi-select), skip the batch, or exit.
7. Loop ends on explicit exit.
8. If pool is empty: *"No more items. Anything I missed, or shall we move on?"*
9. Declined/unselected items are gone forever.

### 3d — Tips dedup

Branch 4 (Tips) only: before presenting, check whether an item was already proposed in any earlier branch (accepted or declined). If yes, skip it.

## Step 4 — Session log

Run last, even if Branches 1–4 were not selected.

Use the session name from Step 2. Write to `b0ttsagent/sessionlogs/<MM-DD-YYYY>/<HHMM>_<session-name>.md` with:
- `# <session-name>` header, Date, Time
- `## What happened`, `## Skills used`, `## Closing outcomes`, `## Open / next`

## Edge cases

- **Empty branch**: ask to skip or write minimal log.
- **Skill name collision**: block, propose alternative.
- **Missing target file**: ask to recreate with proposed content.
- **Mid-run abort**: no special handling; approved work is preserved.
- **File write failure**: follow Step 3b soft escape — retry once, offer alternatives, never skip silently.
