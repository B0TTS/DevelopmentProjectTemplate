# Scratchpad — Branch 4: Tips
**Session:** template-installer-v2
**Date:** 06-24-2026 13:06

## Categories identified
- repeated-manual-work
- automation-opportunity
- organizational-gap
- tooling-idea
- cognitive-load-reduction

## Extraction

### repeated-manual-work
- The publish cycle (bump version in package.json → npm publish) was done 4 times this session. Could add an npm script like `"pub": "npm version patch && npm publish --access public"` or similar.
- Constructing printf test sequences with escape codes for checkbox testing was tedious and error-prone. A test harness or --dry-run flag would help.

### automation-opportunity
- The installer has no `--yes` or `-y` flag to skip interactive prompts. This would make automated testing and CI integration possible. Currently the confirm prompt blocks non-interactive usage entirely.
- A `--list-skills` flag that prints available skill names and exits would help users preview what's available before running the installer.

### organizational-gap
- The bundle's `files/.agents/skills/` is missing `update-template-installer` — it exists in the project's `.agents/skills/` but was never synced to the bundle. The diff step in this session flagged it as "MISSING in bundle."
- The nav guide was stale (v1.0.2 displayed, reality was v1.3.0) until we updated it during this session. This is now covered by the update-template-installer skill's steps 7-9.

### tooling-idea
- A `--dry-run` flag on the installer that shows what would be copied without actually copying. Would speed up testing and let users preview before committing.
- The installer could accept command-line args to pre-select categories and skills, e.g. `npx @b0tts/template-dev-installer --skills close,closev2 --opencode`. This would make the installer scriptable.

### cognitive-load-reduction
- The skill selection prompt shows 17 flat items. Could benefit from grouping (e.g., "Core", "Project Management", "Minecraft") or brief descriptions inline. Currently users need to know skill names from memory.
- The `--list-skills` idea above would also reduce the need to remember skill names — users could grep the output.

## Gleaning Pass

### repeated-manual-work
- Re-checked messages 20-24 (the publish sequence): the bump + publish cycle was indeed manual 4 times. A convenience script would save keystrokes. Added to extraction.

### automation-opportunity
- Re-checked the testing messages (8-11, 14-16, 22): every test required constructing printf sequences manually. A --yes flag and --dry-run flag would make testing far easier. Added to extraction.

### organizational-gap
- Re-checked the diff output in message 18: update-template-installer skill was flagged as MISSING in bundle. This is a real gap that should be synced. Added to extraction. The nav guide staleness was also a gap but is now addressed.

### tooling-idea
- Re-checked the full conversation: the --dry-run and CLI args ideas emerged from observing the testing friction and the multi-step prompt flow. Both would improve the installer's utility. Added to extraction.

### cognitive-load-reduction
- Re-checked the skill selection UI discussion (messages 12-13): 17 flat items without descriptions makes selection harder than it needs to be. Grouping or descriptions would help. Added to extraction.
