# Scratchpad — Branch 1: Memory files
**Session:** template-installer-v2
**Date:** 06-24-2026 13:06

## Categories identified
- architectural-decisions
- tooling-choices
- path-conventions
- new-facts
- project-state-changes
- gotchas

## Extraction

### architectural-decisions
- Custom reactive "All" checkbox built on @inquirer/core (createPrompt) rather than using the built-in 'a' keyboard shortcut. Reason: user wanted a visible "All" choice in the list, not a keyboard-only toggle. The custom prompt clones checkbox v2.5.0 behavior and adds `isAll` choice property with reconcileAll logic.
- Two-prompt install flow: category selection → skill sub-selection. The skill prompt only appears when Skills is in toInstall. SkillsFilter (null = all, array = selected) flows through copyItem → copyAdditiveSkills.
- "All" reactivity: space on All toggles all others; deselecting any individual unchecks All; manually checking everything auto-checks All. The 'a' and 'i' keyboard shortcuts also update All accordingly.

### tooling-choices
- Pinned reactive-checkbox.mjs to @inquirer/core v9.2.1 and @inquirer/checkbox v2.5.0 API. Uses yoctocolors-cjs (not styleText), ansi-escapes (not @inquirer/ansi), v2 theme structure (disabledChoice, helpMode, no keysHelpTip callback). The GitHub main branch has a newer API — upgrading @inquirer/prompts past v5.x would break the custom prompt.
- Chose to fork the full checkbox behavior (~230 lines) rather than wrap or post-process. Gives complete control over space/a/i/number key handlers to coordinate "All" state.
- `skillsFilter: null` means "install all skills" — `null` is the absence of a filter. An empty array would install nothing, which is handled separately.

### path-conventions
- `reactive-checkbox.mjs` lives in `Setup/template-dev-installer/bin/` alongside `cli.mjs`.
- `package.json` `"files"` uses `"bin/"` directory pattern (not `"bin/cli.mjs"`) to include all bin files.
- Nav guide lives at `b0ttsagent/NavGuides/NpmTemplateNavGuide.md`.
- update-template-installer skill lives at `.agents/skills/update-template-installer/SKILL.md`.

### new-facts
- npm will silently omit files not listed in `"files"` — caused the v1.2.0 publish failure where reactive-checkbox.mjs was in bin/ but not packed.
- @inquirer/prompts v5.x bundles checkbox v2.5.0 and core v9.2.1 (different API from GitHub main branch).
- There are 17 bundled skills (18 including update-template-installer which exists in project `.agents/skills/` but is NOT yet synced to the bundle's `files/.agents/skills/`).
- @inquirer/confirm prompt from @inquirer/prompts behaves poorly with piped stdin in automated testing.

### project-state-changes
- Package version path: 1.1.1 → 1.2.0 (failed publish) → 1.2.1 (fixed "files") → 1.3.0 (skill filter feature) → 1.3.1 (AGENTS.md sync).
- New file: `bin/reactive-checkbox.mjs` (custom prompt, ~230 lines).
- Modified: `bin/cli.mjs` — imports reactive checkbox, adds Separator, isAll flag, skill selection sub-prompt.
- Modified: `package.json` — version, "files": ["bin/", "files/"].
- Modified: `b0ttsagent/NavGuides/NpmTemplateNavGuide.md` — updated to v1.3.0 with prompt flow, bin gotchas, skill filtering.
- Modified: `.agents/skills/update-template-installer/SKILL.md` — added step 0 (read nav guide), steps 7-9 (nav guide freshness → propose → approve), Bin files section, updated post-sync.
- Synced: `Setup/template-dev-installer/files/AGENTS.md` (added "Temp Files" section from project root).

### gotchas
- `"bin/cli.mjs"` in package.json `"files"` silently omits other bin files. Must use `"bin/"` when multiple files exist.
- `reactive-checkbox.mjs` is pinned to specific @inquirer versions (core v9.x, checkbox v2.5.0). Upgrading @inquirer/prompts past v5.x requires updating the custom prompt to match the newer API.
- AGENTS.md is marked `additive: true` in CATEGORIES, meaning the installer skips it if destination exists — but the bundle version should still be kept current with the project version for new installs.

## Gleaning Pass

### architectural-decisions
- Re-checked messages 1-22 (the full reactive checkbox design and implementation): no missed architectural decisions. The extraction covers custom prompt architecture, two-prompt flow, and the reconcileAll state management pattern.

### tooling-choices
- Re-checked messages 9-15 (the research phase where I compared @inquirer versions and APIs): no missed tooling choices. The extraction covers the version pinning decision and fork-vs-wrap choice.

### path-conventions
- Re-checked the full conversation for file path patterns: no missed conventions. The bin/, NavGuides/, and skills/ paths are all captured.

### new-facts
- Re-checked the v1.2.0 publish failure (messages 20-22) and the @inquirer version discovery (messages 12-15): no missed facts. The silent file omission and version pinning details are captured.

### project-state-changes
- Re-checked the publish sequence (v1.2.0 → v1.2.1 → v1.3.0 → v1.3.1) and all file modifications: no missed changes. The extraction covers all 4 publishes, the new file, and all 4 modified files.

### gotchas
- Re-checked the v1.2.0 failure (message 20) and the @inquirer research (messages 12-15): no missed gotchas. The "files" pattern and version pinning gotchas are captured.
