---
name: NpmTemplateInstaller
topics:
  - npm
  - template
  - installer
  - dev-setup
  - scaffold
  - opencode
  - pi
  - skills
description: >
  Public npm package (@b0tts/template-dev-installer) that interactively installs template files (Skills, OpenCode, Pi) into any project directory via npx. Features a reactive "All" checkbox and per-skill selection. Bundles sanitized configs and agent skills from the DevelopmentTemplate.
---

## Overview

| Property | Value |
|----------|-------|
| Package | `@b0tts/template-dev-installer` |
| Registry | https://www.npmjs.com/package/@b0tts/template-dev-installer |
| Current version | 1.4.0 |
| Install command | `npx @b0tts/template-dev-installer@latest` |
| Local source | `C:\Users\Jonah\DevelopmentTemplate\Setup\template-dev-installer` |
| Published scope | `@b0tts` (user-scoped, public) |
| Node requirement | 18+ (ESM, `fetch`, `cpSync`) |

## Publishing

Bump the version in `package.json` then:

```bash
cd C:\Users\Jonah\DevelopmentTemplate\Setup\template-dev-installer
npm publish --access public
```

> Requires a granular access token with **Bypass required two-factor authentication** enabled. Set with `npm config set //registry.npmjs.org/:_authToken <token>`. Regular login + OTP also works if 2FA is in "auth-and-writes" mode.

## Package structure

```
Setup/template-dev-installer/
├── package.json
├── bin/
│   ├── cli.mjs                    ← ESM entry point
│   └── reactive-checkbox.mjs      ← custom @inquirer/core prompt with reactive "All"
└── files/                         ← bundled template payload
    ├── AGENTS.md
    ├── README.md
    ├── .agents/skills/            ← all 18 skill folders
    ├── b0ttsagent/                ← empty scaffold (additive)
    │   ├── temp/
    │   ├── sessionlogs/
    │   ├── handoffs/
    │   └── NavGuides/
    ├── opencode/
    │   ├── opencode.json
    │   ├── settings.json
    │   └── plugins/Notifications.js
    └── pi/
        ├── settings.json
        ├── mcp.json
        └── extensions/context-tiers.ts
```

## Prompt flow

The installer runs two sequential prompts:

### Step 1 — Category selection

Reactive checkbox with four choices: **All**, Skills, OpenCode, Pi. The "All" choice acts as a master toggle:

- Selecting "All" → all other choices become checked
- Deselecting any individual choice while "All" is checked → "All" becomes unchecked, other selections preserved
- Manually checking every individual choice → "All" auto-checks

Built on a custom `@inquirer/core` prompt (`reactive-checkbox.mjs`) that wraps the standard checkbox behavior. Also supports the built-in `a` (toggle all) and `i` (invert) keyboard shortcuts.

### Step 2 — Skill selection (only if Skills chosen)

If Skills was selected (directly or via All), a second reactive checkbox lists all bundled skills alphabetically with the same "All" toggle behavior. The user can install a subset of skills.

If no skills are selected, Skills is removed from the install list entirely. If nothing else remains, the installer aborts.

## Categories installed

| Choice | Files copied |
|--------|-------------|
| Skills | `AGENTS.md`, `README.md`, `.agents/skills/<selected>/`, `b0ttsagent/` scaffold |
| OpenCode | `.opencode/plugins/`, `.opencode/opencode.json`, `.opencode/settings.json` |
| Pi | `.pi/agent/settings.json`, `.pi/agent/extensions/`, `.pi/agent/mcp.json` |
| All | Everything above |

> **Skill filtering:** Only skills selected in Step 2 are copied. `AGENTS.md`, `README.md`, and `b0ttsagent/` scaffold install regardless of the skill filter (they are separate items in the Skills category).

## Secrets handling

All sensitive values in template files are replaced with placeholders before publishing:

| File | Sanitized |
|------|-----------|
| `Notifications.js` | ntfy URL → `{YOUR_TAILSCALE_URL}`, auth → `{YOUR_USER}:{YOUR_PASSWORD}` |
| `opencode.json` | Context7 key → `{env:CONTEXT7_API_KEY}`, user paths → relative, private MCP server removed |
| `pi/mcp.json` | Context7 key → `ctx7sk-YOUR_KEY_HERE`, docs MCP server removed |

> Users must fill in their own values after installation.

## Gotchas

> **Bin script must live in `bin/` folder.** npm strips the `bin` entry if the script is in the package root. The file goes in `bin/cli.mjs` and package.json references `"bin/cli.mjs"`.

> **Use `.mjs` extension for ESM bin scripts.** With `"type": "module"` in package.json, `.js` bin scripts trigger validation warnings on publish. `.mjs` avoids this.

> **`"files"` must use `"bin/"` not `"bin/cli.mjs"`.** When the bin directory contains multiple files (e.g. `cli.mjs` + `reactive-checkbox.mjs`), the `package.json` `"files"` field needs the directory pattern `"bin/"` to include both. A single-file pattern silently omits the other.

> **`reactive-checkbox.mjs` is pinned to `@inquirer/core` v9.x / `@inquirer/checkbox` v2.5.0.** It uses `yoctocolors-cjs`, `ansi-escapes`, and the v2 theme structure. Upgrading `@inquirer/prompts` past v5.x would require updating the custom prompt to match the newer theme API (`styleText`, `@inquirer/ansi`, `keysHelpTip` callback).

> **Every template file change requires a publish.** The files are bundled in the npm tarball — updating a skill or config means bumping the version and running `npm publish --access public` again.
