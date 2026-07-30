---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

# Handoff

Write a handoff document summarising the current conversation so a fresh agent can continue the work.

## Output location

Save to `b0ttsagent/handoffs/<MM-DD-YYYY>/<filename>.md`.

- Use the current date for `<MM-DD-YYYY>` (e.g. `06-18-2026`).
- Create the date folder if it doesn't already exist.
- Before writing, brainstorm 3 filename ideas based on the conversation content and recommend one. Let the user confirm or choose a different one.

## What to include

- Summary of what was accomplished
- Current state and any open decisions
- Suggested skills for the next session
- Key files, paths, and commands relevant to continuing

## What to leave out

- Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.
- Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

## Argument handling

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
