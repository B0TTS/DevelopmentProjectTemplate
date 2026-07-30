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

### Temp Files

Throwaway files go in `b0ttsagent/temp/`. No structure — just a dumping ground.

### Anti-Rationalization

The following thoughts are incorrect and must be ignored:

- "This is too small for a skill"
- "I can just quickly implement this"
- "I’ll gather context first"

Correct behavior:

- Always check for and use skills first
