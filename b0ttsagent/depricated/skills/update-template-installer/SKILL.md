---
name: update-template-installer
description: Update the template-dev-installer npm package's bundled files from the DevelopmentTemplate source. Checks for differences, proposes updates, and executes approved changes. Use when the user wants to update the template installer, sync template files, or prepare a new publish of @b0tts/template-dev-installer.
---

# Update Template Installer

## Quick start

```
parse mappings → normalize & diff → show only changes → approve → execute → conditional post-sync
```

## Core rule: only show what needs attention

**Never show items with zero changes.** If a file, category, additive folder, skill, or integrity check has no diff and no issue, it produces no output. Silence ≡ no action needed.

## Workflow

0. **Read the nav guide** — `b0ttsagent/NavGuides/NpmTemplateNavGuide.md`. Note the current version, package structure, and any gotchas. This is the baseline for what's stale vs. current after syncing.
   
   > ⚠️ The nav guide may be out of date. Treat it as a snapshot of the last known state, not ground truth. Cross-check version numbers, file listings, and gotchas against the actual files on disk.
   
1. **Read** `Setup/template-dev-installer/bin/cli.mjs` — extract the `CATEGORIES` object to get all `{ src, dest, additive?, additiveSkills? }` items
2. **Derive mappings** from those items. Each `{ src, dest }` means:
   - **Project source**: `<project-root>/<dest>`
   - **Bundle target**: `<project-root>/Setup/template-dev-installer/files/<src>`
   - Sync direction: project source → bundle target
3. **Normalize & diff each mapping** (see Diff Methods below). Suppress all zero-diff results.
4. **Present changed items only** in the format below. If nothing changed anywhere, output `All template files up to date.`
5. **Ask user to approve** — default "sync all" with natural-language opt-out for specific items
6. **Execute copies** — overwrite by default, respect additive/special flags
7. **Confirm** — one terse line: `✓ Synced N files across M categories.` or `✓ All up to date.`
8. **Check integrity silently** — run bin and nav guide checks. Only surface problems. Don't edit any files, just propose any problems and how you'll fix it.
9. **Conditional post-sync footer** — see Post-Sync section

## Output format

When changes exist, present them as a tree with counts. Diff hunks follow after the tree. Nothing else appears.

```
## Changes to sync

### <Category> (N changes)
  <path> (modified)
  <path> (new)
  <path> (removed — are you sure?)

### Bin source (N changes)
  <path> (uncommitted changes)
  <path> (not covered by package.json "files")

### Nav guide
  Version is 1.2.0 but package.json is 1.3.0. Stale.

────────────────────────────────────
Sync all? (y/n)
```

Follow the tree with diff hunks for each modified file (tidied unified diff — no timestamps, no `Only in` noise):

```
--- a/<path>
+++ b/<path>
@@ ... @@
 ...
```

When nothing has changed anywhere:

```
All template files up to date.
```

## Parsing the mappings

The `CATEGORIES` object in `cli.mjs` is the single source of truth. Each category has an `items` array. For example:

```js
skills: {
  items: [
    { src: "AGENTS.md",  dest: "AGENTS.md",  additive: true },
    { src: ".agents",    dest: ".agents",    additiveSkills: true },
    { src: "b0ttsagent/temp", dest: "b0ttsagent/temp", additive: true },
  ],
},
```

Derive: project `AGENTS.md` → bundle `files/AGENTS.md`, project `.agents/` → bundle `files/.agents/`, etc.

## Diff methods — normalized, no zero-diffs

**Always normalize before diffing.** Normalization replaces known secret patterns with the canonical token `__PLACEHOLDER__` in both source and bundle. Diff the normalized versions. If the diff is empty after normalization, the file is unchanged — produce no output.

### Placeholder patterns to normalize

| Pattern | Example |
|---|---|
| ntfy URL with tailscale host | `https://<host>/<topic>` → `__PLACEHOLDER__` |
| ntfy auth header value | `Basic <base64>` → `__PLACEHOLDER__` |
| Context7 API key (`ctx7sk-`) | `ctx7sk-abcdef12345` → `__PLACEHOLDER__` |
| Context7 env reference | `{env:CONTEXT7_API_KEY}` → `__PLACEHOLDER__` |
| User-specific paths | `C:\\Users\\...` → `__PLACEHOLDER__` |
| Private MCP server entries | Entire server object if name is not public → `__PLACEHOLDER__` |

> **Sanity check:** if any diff hunk contains `ctx7sk-`, `{YOUR_`, `{env:CONTEXT7`, user paths, or private MCP server names, you normalized incorrectly. Re-normalize and diff again.

### Diff methods per item flag

| Item flag | Comparison method |
|---|---|
| *(none)* | `diff -r <project>/<dest> <bundle>/<src>` after normalization. Report per-file: modified, new (in project, missing from bundle), removed (in bundle, missing from project) |
| `additive: true` | Exist check: verify bundle folder exists. Show only if bundle folder is **missing** or has **unexpected content** (leaked files). Otherwise silent |
| `additive: true` for AGENTS.md / README.md | Diff after normalization. If changed: show as a warning — `AGENTS.md — bundle has changes, but project exists (additive, won't overwrite)`. If unchanged: silent |
| `additiveSkills: true` | List skill dirs in project `.agents/skills/`. For each, diff every file inside the skill directory against `files/.agents/skills/<skill>/`. Report per-file. **New skill** (in project, not in bundle): flag as new. **Missing skill** (in bundle, not in project): warn — `<skill> was in the bundle but is no longer in the project. Did you mean to remove it?` |

## Bin files — separate section

After diffing templates, list files in `bin/`. Check each against `git status` for uncommitted changes. Cross-check each file against `package.json` `"files"` — if not covered, flag it. Present in a separate **Bin source** section, distinct from template changes.

## Post-sync — conditional footer

Only show lines that apply:

- **Template changes occurred:** `Bump version in Setup/template-dev-installer/package.json, then run npm publish --access public.`
- **Only bin files changed (templates clean):** `Bin source changed. Bump and publish even though templates are current.`
- **Nav guide was updated:** `Nav guide updated to v<new>.`
- **Nothing changed anywhere:** Print nothing beyond the confirmation line.

Never print a footer line when its condition is false.
