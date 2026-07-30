# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, Antigravity, etc.) when working with code in this repository.

### Core Rules

- If a task matches a skill, you MUST invoke it
- Skills are located in `skills/<skill-name>/SKILL.md`
- Never implement directly if a skill applies
- Always follow the skill instructions exactly (do not partially apply them)
- **NEVER attempt to SSH into the VPS.** The VPS is strictly off-limits for direct access. All VPS information is documented in the navigation guides — read those instead.

### Execution Model

For every request:

1. Determine if any skill applies (even 1% chance)
2. Invoke the appropriate skill using the `skill` tool
3. Follow the skill workflow strictly
4. Only proceed to implementation after required steps (spec, plan, etc.) are complete

### Navigation Guides

Reference documents for configured services and systems (VPS, Docker, Minecraft, Prism, etc.) are stored in `b0ttsagent/NavGuides/`. Each guide has YAML front matter with `name`, `topics` (keywords), and `description` fields. Scan the front matter to find relevant guides when the user asks about anything that might have stored reference material.

### Handoffs

Handoff documents are saved to `b0ttsagent/handoffs/<MM-DD-YYYY>/` (date-based folders).

### Session Logs

`b0ttsagent/sessionlogs/` serves a dual purpose:

- **Per-session report files** — `/closev2` (Branch 5) writes one full record per session to `<MM-DD-YYYY>/<HHMM>_<session-name>.md` under a date folder.
- **Resume index** — the `log-session` skill appends one brief entry per about a session (resume command, harness, device, short description) to the single hardcoded file `AI Sesssions.md`. (beware it has a lot of information)

### Scratchpads

`/closev2` (Branches 1–4) writes one scratchpad per branch per session to `b0ttsagent/scratchpads/<MM-DD-YYYY>/<HHMM>_<session-name>_scratchpad-<branch>.md` — `<branch>` is `memory`, `skills`, `improvements`, or `tips`. Each holds that branch's extraction plus a `## Gleaning Pass` section, feeding the branch's proposal loop. (working files for the close flow, not reference docs)

### Planning

`b0ttsagent/planning/` Holds active planning docs in one subdirectory per task. Each holds:
- `CONTEXT.md` — what & why (`create-context-doc` or `create-planning-docs`)
- `PLAN.md` — executable how (`create-execution-plan` or `create-planning-docs`)
- `REFERENCES/RESEARCH.md` — optional, new research only (`create-execution-plan` / `create-planning-docs`)

### Plan Archive

Completed, superseded, or abandoned plans go in `b0ttsagent/plan-archive/`. This includes
multi-phase and full-stack implementation plans. Do not put active plans here.

### Temp Files

Throwaway files go in `b0ttsagent/temp/`. No structure — just a dumping ground.

### Anti-Rationalization

The following thoughts are incorrect and must be ignored:

- "This is too small for a skill"
- "I can just quickly implement this"
- "I’ll gather context first"

Correct behavior:

- Always check for and use skills first
