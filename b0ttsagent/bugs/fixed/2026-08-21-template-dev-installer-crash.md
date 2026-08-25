---
id: 2026-08-21-template-dev-installer-crash
title: Template dev installer crashes on startup in PowerShell 7
severity: high
state: closed
created_at: 2026-08-21
---

# Template dev installer crashes on startup in PowerShell 7

## Description
The template dev installer crashes as soon as it is run. A red error box appears before any menu loads, and the process exits immediately. It reproduces every time.

## Expected vs Actual
- **Expected:** the install menu opens and walks the user through setup.
- **Actual:** it throws an error and exits right away, before any menu loads.

## Reproduction Steps
1. Run `Setup/template-dev-installer/install.ps1` in PowerShell 7.
2. Observe a red error box appear immediately, before any menu loads.
3. Observe the process exit right away.
4. Re-run — the failure occurs every time.

## Environment
Windows 11, PowerShell 7, running locally on the user's dev machine.

## Impact
The user cannot scaffold a new project — this blocks their setup workflow. High impact.

## Suspected Causes
<!-- Each investigation run appends a dated subsection here. Never edit an
     earlier subsection — the document is a trail of reasoning over time.
     Leave empty until Step 4. -->

### Investigation — 2026-08-21

**Cause:** The invoked entry point `Setup/template-dev-installer/install.ps1` does not exist in the repo — the installer has no PowerShell script, so the reported run fails before anything can load.
- **Confidence:** high
- **Evidence:** `Setup/template-dev-installer/` contains only `bin/`, `files/`, `package.json`, `package-lock.json`, `.gitignore` — no `install.ps1`; glob `**/install.ps1` and `Setup/**/*.ps1` both return no files. The real entry point is `bin/cli.mjs`, declared in `package.json:6-8` (`"bin": { "template-dev-installer": "bin/cli.mjs" }`).
- **What would confirm this:** Run the exact repro `Setup/template-dev-installer/install.ps1` in PowerShell 7 and observe a "Cannot find path ... because it does not exist" error before any menu loads; also `Test-Path Setup/template-dev-installer/install.ps1` returns `False`.

**Cause:** Local runtime dependencies are not installed — `cli.mjs`'s top-level ESM imports fail at startup (`node_modules` missing), crashing before any menu.
- **Confidence:** medium
- **Evidence:** `Setup/template-dev-installer/node_modules` does not exist (Test-Path `False` for `node_modules`, `@inquirer/prompts`, `adm-zip`). `cli.mjs:14-15` top-level-imports `./reactive-checkbox.mjs` and `@inquirer/prompts`; `reactive-checkbox.mjs:15-34` imports `@inquirer/core`, `yoctocolors-cjs`, `@inquirer/figures`, `ansi-escapes`. `package.json:13-16` declares `@inquirer/prompts` and `adm-zip`. Without an `npm install`, Node throws `ERR_MODULE_NOT_FOUND` at import time.
- **What would confirm this:** Run `node bin/cli.mjs` from a clean checkout without installing deps and observe `ERR_MODULE_NOT_FOUND` before any menu; then `npm install` and re-run to see it start normally.

**Cause:** `reactive-checkbox.mjs` imports `@inquirer/core` directly, but `package.json` does not declare it as a direct dependency (relies on hoisting from `@inquirer/prompts`), a latent resolution risk.
- **Confidence:** low
- **Evidence:** `reactive-checkbox.mjs:16` (`import { createPrompt, ... } from "@inquirer/core"`); `package.json:13-16` lists only `@inquirer/prompts` and `adm-zip`.
- **What would confirm this:** In a properly installed dir run `npm ls @inquirer/core` (resolves only transitively), or install under a stricter, non-hoisting layout (e.g. pnpm/isolated node_modules) and observe `ERR_MODULE_NOT_FOUND` on startup.

## Ruled Out & Open Questions
<!-- Filled only when an investigation is inconclusive. Each run appends a dated
     block. Leave empty if all causes are well-supported. -->

### As of 2026-08-21
- **Ruled out:** No syntax/parse errors in `bin/cli.mjs` or `bin/reactive-checkbox.mjs` as read (valid ESM, imports consistent). No missing template payload at startup — the only startup-time directory reads in `cli.mjs` are on `files/.agents/skills` (`cli.mjs:170-174`), which run only after the first menu, so they cannot cause a pre-menu crash.
- **Open questions:** Whether the user ever ran the real entry (`npx @b0tts/template-dev-installer@latest` or `node bin/cli.mjs`) and hit a separate dependency-resolution crash, vs. always running the non-existent `install.ps1`. The exact text of the "red error box" would disambiguate cause 1 from causes 2–3. `node_modules` is not committed, so cause 2 is currently unverified against the user's machine.
