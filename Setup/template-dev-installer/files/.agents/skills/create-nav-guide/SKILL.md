---
name: create-nav-guide
description: Generate a reference document (nav guide) from the current conversation. Use when user says "doc this", "write this up", "make a reference", "create a nav guide", "document what we just did", or similar.
---

# Create Nav Guide

## What this skill does

Reads the current conversation and produces a markdown nav guide in `b0ttsagent/NavGuides/`. The guide is written for two audiences: the user as a personal reference, and future AI assistants who need to understand the setup before suggesting changes or additions.

## Workflow

1. **Extract** key information from the conversation — only what's actually present, don't invent.
2. **Generate front matter** — produce `name`, `topics`, and `description` from the conversation content. Use the naming convention matching the filename (e.g. `MinecraftModsGuide`).
3. **Write overview table** — key properties as a markdown table. Adapt fields to the domain (ports, locations, credentials, versions, config values — whatever is relevant). Don't force Docker-specific fields onto non-Docker setups.
4. **Write key systems** — one section per major subsystem that has its own commands or configuration. For each: what it does, how to operate it, current state.
5. **Write gotchas** — brief blockquotes (`>`) for anything non-obvious that caused problems during setup.
6. **Avoid duplication** — scan related nav guides in `b0ttsagent/NavGuides/` for overlapping topics. Don't repeat information already covered there. Reference them if needed.
7. **Present** — show the generated guide to the user for confirmation before writing the file.

## What to leave out

- Step-by-step setup instructions — current state only
- Speculative future features
- Things that worked without incident

## Format rules

- Markdown only, with YAML front matter
- Tables for config values and key properties
- Bash code blocks for all commands
- Gotchas as `>` blockquotes inline with the relevant section
- No preamble, no closing remarks
- Section headers should match the actual systems — don't use generic headers like "Configuration" if a more specific name fits (e.g. "Backups", "Chunky", "RCON")

## Output

Write to `b0ttsagent/NavGuides/<name>.md` after user confirms.
