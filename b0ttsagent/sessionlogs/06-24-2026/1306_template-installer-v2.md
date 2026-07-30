# template-installer-v2
**Date:** 06-24-2026
**Time:** 13:06

## What happened
- Built a custom reactive "All" checkbox prompt (`reactive-checkbox.mjs`) on `@inquirer/core` for the template installer — selecting "All" checks everything, deselecting any individual unchecks "All", manually checking all auto-checks "All"
- Added a two-prompt install flow: category selection → per-skill sub-selection with filtering
- Published 4 versions: v1.2.0 (failed — missing bin file), v1.2.1 (fixed), v1.3.0 (skill filter), v1.3.1 (AGENTS.md sync)
- Updated `NpmTemplateNavGuide.md` to v1.3.0 with reactive checkbox docs, skill filtering, and two new gotchas
- Heavily improved the `update-template-installer` skill: added step 0 (read nav guide), steps 7-9 (freshness check → propose → approve nav updates), bin files section, post-sync nav guide note, and bin file coverage verification action
- Synced AGENTS.md to the installer bundle (added "Temp Files" section)
- Applied one closev2 improvement: made bin file dependency coverage check actionable in update-template-installer skill

## Skills used
- **update-template-installer** — invoked for file sync; heavily edited during session
- **create-nav-guide** — read for format rules during nav guide update
- **closev2** — session close

## Closing outcomes
- **Memory:** Nav guide updated to v1.3.0; AGENTS.md synced to bundle
- **Skills:** No new skills proposed
- **Improvements:** 1 applied — bin file coverage check now actionable in update-template-installer/SKILL.md
- **Tips:** None applied (all skipped)

## Open / next
- Bundle is missing `update-template-installer` skill (project has it, bundle doesn't). Needs sync + publish
- `opencode/opencode.json` bundle is significantly outdated vs project (~35 missing agents). Needs sync with full sanitization
- `opencode/plugins/Notifications.js` differs — project has stripped-down version. Needs direction on which version is canonical
- `pi/mcp.json` has docs MCP server block in project (sanitized out in bundle). Needs sanitization sync
- The `--yes`, `--list-skills`, and `--dry-run` flags are low-effort QoL additions for the installer
