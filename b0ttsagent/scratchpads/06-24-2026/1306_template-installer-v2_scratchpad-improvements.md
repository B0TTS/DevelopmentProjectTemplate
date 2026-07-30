# Scratchpad — Branch 3: Improve skills
**Session:** template-installer-v2
**Date:** 06-24-2026 13:06

## Categories identified
- missing-coverage
- friction-points
- outdated-references
- poor-triggering

## Extraction

### missing-coverage
- update-template-installer: The "Diff methods" table says `additive: true` items get "exists check only" — but we synced AGENTS.md (an additive item) anyway because the project version had changed. The skill should clarify when additive items SHOULD be synced (project has newer content than bundle).
- update-template-installer: No mention that the installer itself (`cli.mjs`) might import dependencies like `reactive-checkbox.mjs`. When adding new bin files, the skill should flag that `package.json` `"files"` needs updating.
- update-template-installer: Step 1 says "Read cli.mjs to extract CATEGORIES" — but if the installer gains new modules (like reactive-checkbox.mjs), the skill should also verify they exist in the bundle.

### friction-points
- update-template-installer: The "additive" flag semantics are confusing. AGENTS.md is additive (skip if dest exists) but the bundle still needs the latest version for new installs. The distinction between "install behavior" and "bundle sync behavior" is blurry.
- create-nav-guide: Was read for format rules during the nav guide update, but the skill's instructions are primarily about creating new guides from scratch, not updating existing ones. No friction observed since we just used it for format reference.

### outdated-references
- update-template-installer: The skill's post-sync section says to remind about bump + publish but doesn't mention the nav guide update. We already fixed this in the session, so this is no longer outdated.
- update-template-installer: The quick start still says "parse mappings from cli.mjs" — doesn't mention the new step 0 (read nav guide) or step 7 (check nav guide freshness). The quick start line should be updated.

### poor-triggering
- update-template-installer: The skill description says "update the template-dev-installer npm package's bundled files" — but the actual session involved modifying the installer logic (cli.mjs, reactive-checkbox.mjs), not just syncing bundled files. The skill's scope is file sync, not code changes. This is by design — code changes don't use this skill.

## Gleaning Pass

### missing-coverage
- Re-checked messages 17-19 (the update-template-installer skill edits): the additive flag vs sync behavior tension was noted during the diff step when AGENTS.md showed a diff but was marked additive. Added to extraction above.

### friction-points
- Re-checked the AGENTS.md sync decision (messages 18-19): the user had to explicitly approve syncing an additive file — the skill could handle this more gracefully by flagging additive files that have newer project versions. Added to extraction.

### outdated-references
- Re-checked the skill edits (messages 17-18): the quick start line wasn't updated to reflect the new workflow. Confirmed as a real gap.

### poor-triggering
- Re-checked the skill invocation (messages 18-19): the skill was correctly triggered for file sync, and code changes (reactive checkbox, skill filter) were done outside the skill. The trigger is fine — the scope is intentionally narrow.
