---
name: tutorial-v2
description: Generates a step-by-step walkthrough for any concept, tool, or setup task — then guides the user through executing each step one at a time with pacing, validation, and diagnosis. Use when the user wants to learn something, set something up, or be walked through a process.
disable-model-invocation: true
---

# Tutorial

When the user asks to learn or set up something, follow this workflow.

## Phase 1: Plan

1. Clarify the goal with the user if it's vague. Ask what they already know, what their environment is, and what success looks like.
2. Research the topic thoroughly. Use web search for current documentation, APIs, and best practices. Inspect the user's project context (files, configs, dependencies) for environment-specific details.
3. Create a numbered, step-by-step plan. Each step should be a single, concrete action the user can take. Include the expected command or action, what the user should see, and how to verify success.
4. Present the full plan to the user.
5. Offer a grill-me session. Ask something like: "Do you have any questions or concerns about this plan? Would you like to grill it for a deeper shared understanding before we start?"
6. If the user says yes: interview them relentlessly, one question at a time. Resolve every branch of the decision tree — environment, constraints, preferences, dependencies, edge cases. If a question can be answered by web research or inspecting their project context, do that instead of asking. Refine the plan based on their answers.
7. If the user says no or is satisfied: confirm and move to Phase 2.

## Phase 2: Execute

Work through one step at a time. **Never present multiple steps at once.**

For each step:

1. Present the step clearly — what to do, what command to run, what to expect. Commands at/over 100 chars go to a file — present the short runner, never the full text (see the command rule in Rules).
2. Wait for the user to complete it and share their output.
3. Read the output carefully. Confirm it looks correct. If it does, briefly acknowledge it and move to the next step.
4. If something looks wrong — unexpected errors, wrong output, anything off — stop and diagnose before continuing. Help the user understand what went wrong and how to fix it. Do not skip past errors.
5. Repeat until all steps are complete.

## Phase 3: Wrap Up

1. Summarize what was accomplished.
2. Suggest logical next steps or related topics to explore.
3. Offer to help troubleshoot anything that came up.

## Rules

- **Never** front-load multiple steps — one step, then wait.
  - If the user wants to skip a step, ask them to confirm, then move on.
  - If the user wants to go back to a previous step, help them undo or revisit.
  - Adapt the plan if the user's environment or needs change mid-tutorial.
- **Never display a command at/over 100 characters for copy-paste** — the user's Windows terminal mangles pasted commands. The limit counts the full command text (multi line commands must not be displayed). Write over-limit or multi line commands to a file for the user to copy and paste:
  - When the tutorial starts (Phase 1), create `b0ttsagent/tutorial/<slug>/` (slug = lowercase-hyphenated topic) with `commands/`, `scripts/`, and `misc/` subfolders.
  - `commands/` = commands the user must run (one file even if multi-line or over the limit). `scripts/` = standalone agent-authored scripts with multiple commands, loops, or functions (e.g. deployed to the VPS). `misc/` = anything not runnable (configs, notes, saved output). Name files `stepN.file_type` / `stepN.sh`;.
  - PowerShell is the default local device shell unless the tutorial explicitly states otherwise.
