---
name: explain-it
description: Beginner-friendly walkthrough of a file, code snippet, or error message — calibrated to the user's level via quick grilling. Use when user says "explain this", "walk me through", "what does this do", "teach me this", "break this down", or pastes an error and asks "what happened".
disable-model-invocation: true
---

# Explain It

Walk the user through a file, code snippet, or error message section by section, calibrated to their actual understanding.

## Phase 1: Gather

Determine what's being explained:

- **File in project** → read it in full
- **Code in chat** → work from the conversation directly
- **Error message** → work from the pasted text

If the file references other files (imports, configs, schemas), read those too — but only if they're short and directly relevant.

## Phase 2: Calibrate

### Quick check (always)

Ask 2-3 rapid-fire questions to gauge the user's level with the technologies in the file. One question at a time.

**Style:** casual, low-pressure. Frame it as "help me calibrate" not "let me test you."

Example calibration questions:
- "Have you worked with [technology] before, or is this new?"
- "Quick gut check — what do you think [concept] does? Even a wrong guess helps me calibrate."
- "On a scale of 'never seen it' to 'use it daily', where are you with [thing]?"

If a question can be answered from the codebase or conversation history (e.g., they've been working with SQL all session), figure it out yourself instead of asking.

### Grill session (optional)

After the quick check, offer a deeper calibration:

> "Want to do a quick grill session? I'll ask a few more targeted questions to dial in exactly where you're at — takes about a minute and means I won't over-explain stuff you already know."

If yes: interview one question at a time. Probe specific concepts that appear in the file. For each concept, determine if the user genuinely understands it, sort of gets it, or has no clue. Move on once you have a clear picture. Don't pad with unnecessary questions.

If no: proceed with what you know from the quick check.

### Build the level map

Based on all answers, tag each concept/technology in the file:
- ✅ **Knows it** → correct terminology, skip basics, focus on project-specific usage
- 🟡 **Sort of knows it** → brief refresh, then connect to the new context
- ❌ **No idea** → plain English, analogies, tables, build from scratch

If the user says "just explain it" or "skip the questions" → default to beginner and go.

## Phase 3: Explain

Walk through section by section.

### For each section:

1. **Name it** — what this section does, in one plain sentence
2. **Show the code** — reference the actual lines
3. **Break it down** using:
   - **Tables** for structured comparisons (column meanings, permissions, options)
   - **Analogies** for abstract concepts (badges, whiteboards, snapshots)
   - **Plain English translations** of technical syntax
4. **Why it matters** — one line on why this section exists

### For error messages:

1. **TL;DR** — what went wrong in plain English
2. **The fix** — what to do about it
3. **Why it happened** — the underlying cause
4. **Prevention** — what to watch for next time

### After all sections:

End with a **connection diagram** — ASCII art showing how all the pieces relate. This is the "how it all comes together" moment.

## Rules

- **One section at a time** for large files (>50 lines). Smaller files can be explained in one pass.
- **Match the user's level** — don't explain what `SELECT` means if they said they know SQL.
- **Use their project's context** — reference their actual names, data, and use cases.
- **Pause for questions** — after every 2-3 sections, check in: "Questions on that, or keep going?"
- **No setup overhead** — conversational only. Don't create tracking files or lesson plans unless asked.
