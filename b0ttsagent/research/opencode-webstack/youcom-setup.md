# You.com + OpenCode on Windows (PowerShell) — Setup Research

**Date:** 2026-09-03
**Scope:** How to install and configure You.com for OpenCode (opencode.ai) on Windows/PowerShell, for a user who **has a You.com API key** and does **not** want OAuth.
**Security note:** No real key values appear anywhere in this doc. Use `<YDC_API_KEY>` as the placeholder.

---

## TL;DR (recommended path)

**Do NOT rely on the `@youdotcom-oss/opencode` plugin for API-key auth — it is OAuth-only and hardcodes its MCP entries so that it overwrites any `mcp.you` you define yourself.** For an API-key user the clean path is:

1. Configure the MCP servers **manually** in `.opencode/opencode.json` (no plugin), with `"oauth": false` + `Authorization: Bearer {env:YDC_API_KEY}` on the authenticated servers.
2. Install the You.com **skills** separately via `npx skills add youdotcom-oss/agent-skills` (lands in `.agents/skills/`, which OpenCode reads) — or copy the 5 skill folders into `.opencode/skills/`.
3. Set the `YDC_API_KEY` env var on Windows (`setx` for persistent, `$env:` for the current session).
4. Restart OpenCode (config loads at startup; no hot reload).

---

## 1. What the npm package `@youdotcom-oss/opencode` actually does

**Verified against primary sources** (npm page + plugin source on GitHub).

- Package: `@youdotcom-oss/opencode` **v0.5.0**, MIT, published ~Aug 2026, 0 runtime dependencies. Repository: `youdotcom-oss/agent-skills`, directory `packages/opencode`. Peer deps: `@opencode-ai/plugin` / `@opencode-ai/sdk` `>= 1.18.0`. Entry point is `./plugin.ts` (TypeScript, shipped raw).
  - Source: https://www.npmjs.com/package/@youdotcom-oss/opencode
  - Source: https://github.com/youdotcom-oss/agent-skills/blob/main/packages/opencode/package.json
- It is an OpenCode **plugin** whose `config` hook mutates the live merged config at startup. Full source (52 lines) at:
  - https://github.com/youdotcom-oss/agent-skills/blob/main/packages/opencode/plugin.ts
- Exactly what it registers (from the source):
  - **Skills path** → `join(currentDir, 'skills')` — the bundled skills `you-web`, `you-free`, `you-research`, `you-finance`, `you-discover`.
  - **MCP server `you`** → `https://api.you.com/mcp`, `enabled: true`, **`oauth: {}`** (OAuth).
  - **MCP server `you-free`** → `https://api.you.com/mcp?profile=free`, `enabled: true`, no auth.
  - **MCP server `you-finance`** → `https://api.you.com/mcp?tools=you-finance`, `enabled: true`, **`oauth: {}`**.
  - **MCP server `you-docs`** → `https://you.com/docs/_mcp/server`, `enabled: true`, no auth.
- **It does NOT read `YDC_API_KEY`, does NOT set any headers, and ignores plugin options** (the factory is `async () => ({...})` — no options parameter). There is **no API-key mechanism in the plugin**. The npm README confirms: "`you`, `you-finance`, and authenticated You.com tools use OAuth through OpenCode's remote MCP support."
  - Source: https://www.npmjs.com/package/@youdotcom-oss/opencode (Auth section)
- **Critical clobbering behavior:** OpenCode's plugin loader calls the `config` hook with the **already-fully-merged config** (`const cfg = yield* config.get()` then `hook.config?.(cfg)`), and the plugin **unconditionally assigns** `input.mcp.you = {...}`. So with the plugin installed, any `mcp.you` entry you write in your own `opencode.json` is **overwritten at startup** — you cannot override the plugin's `you` server via config.
  - Source: https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/plugin/index.ts (plugin state init: `config.get()` → `hook.config?.(cfg)`)
  - Corroborated by community issue confirming `config`-hook mutation of the live config is the de-facto plugin pattern: https://github.com/anomalyco/opencode/issues/24065

**Confidence: verified-against-primary-docs** (read the plugin source and the opencode plugin loader source directly).

---

## 2. `opencode plugin <spec>` CLI vs manual `"plugin"` array

**Both are valid and equivalent.** Verified against OpenCode CLI docs.

- CLI command exists: `opencode plugin <module>` (alias `opencode plug <module>`), flags `--global`/`-g` (install in global config) and `--force`/`-f` (replace existing plugin version). It "Install[s] a plugin and update[s] your config" — i.e., it writes the entry into your config file (project config by default, global with `-g`).
  - Source: https://opencode.ai/docs/cli/ (Commands → plugin)
- Manual equivalent — the exact config the CLI writes:
  ```json
  { "plugin": ["@youdotcom-oss/opencode"] }
  ```
  - Source: https://opencode.ai/docs/plugins/ ("From npm" section) and the package README.
- npm plugins are **installed automatically at startup using Bun** and cached in `~/.cache/opencode/node_modules/`. Config is read at startup; **no hot reload** — restart OpenCode after adding.
  - Source: https://opencode.ai/docs/plugins/ ("How plugins are installed")
- Plugin load order: global config → project config → global plugin dir → project plugin dir. Duplicate npm packages loaded once.
  - Source: https://opencode.ai/docs/plugins/ ("Load order")

**Confidence: verified-against-primary-docs.**

---

## 3. Auth: how the API key is supplied (the exact mechanism)

### 3a. What the You.com MCP server accepts

The full server `https://api.you.com/mcp` accepts **either** OAuth **or** a static API key via header `Authorization: Bearer <YDC_API_KEY>`. The agent-skills README documents the header form:

```bash
export YDC_API_KEY="your-api-key"
# header: { "Authorization": "Bearer ${YDC_API_KEY}" }
```

- Source: https://github.com/youdotcom-oss/agent-skills (README → "Configure You.com MCP servers")
- Source: https://github.com/youdotcom-oss/agent-skills/blob/main/skills/you-web/SKILL.md (frontmatter `auth: YDC_API_KEY OAuth x402`; "For bearer auth, configure the host MCP client with an authorization header equivalent to `{ "Authorization": "Bearer ${YDC_API_KEY}" }`")
- API keys are issued at https://you.com/platform/api-keys

### 3b. How OpenCode sends the header (and disables OAuth)

OpenCode remote MCP config supports `headers` plus an explicit `"oauth": false` to **disable automatic OAuth** for API-key servers. This is the documented pattern:

```json
{
  "mcp": {
    "my-api-key-server": {
      "type": "remote",
      "url": "https://mcp.example.com/mcp",
      "oauth": false,
      "headers": { "Authorization": "Bearer {env:MY_API_KEY}" }
    }
  }
}
```

- Source: https://opencode.ai/docs/mcp-servers/ (Remote → options; OAuth → "Disabling OAuth")
- `{env:VARNAME}` interpolation is supported in string config values; **if the env var is unset it is replaced with an empty string** (silent failure → 401).
  - Source: https://opencode.ai/docs/config/ (Variables → Env vars)

### 3c. Where the env var must be set on Windows

- **Persistent (user-level):** `setx YDC_API_KEY "<key>"` — takes effect only in **newly started** processes (restart the terminal and OpenCode).
- **Current PowerShell session only:** `$env:YDC_API_KEY = "<key>"`.
- OpenCode reads the process environment at startup; the `{env:YDC_API_KEY}` substitution happens when the config is loaded.

### 3d. The catch: the plugin blocks this

Because the plugin unconditionally overwrites `mcp.you` (and `mcp['you-finance']`) with its OAuth config **after** your config files are merged, you **cannot** attach the API-key header to the plugin's `you` server. Two workable arrangements:

- **A (recommended): don't install the plugin.** Define the MCP servers yourself (section 4) and install the skills separately (section 5). Full control, no OAuth servers at all.
- **B: install the plugin AND add your own server under a different name** (e.g. `you-api`) with the API-key headers, then disable the plugin's OAuth servers' tools so they never prompt:
  ```json
  {
    "plugin": ["@youdotcom-oss/opencode"],
    "mcp": {
      "you-api": {
        "type": "remote",
        "url": "https://api.you.com/mcp",
        "enabled": true,
        "oauth": false,
        "headers": { "Authorization": "Bearer {env:YDC_API_KEY}" }
      }
    },
    "tools": { "you_*": false, "you-finance_*": false }
  }
  ```
  (MCP tools are registered with the server name as prefix, so `you_*` disables the plugin's OAuth `you` server tools; `you-free_*` and `you-docs_*` are keyless and can stay enabled. Source for the glob mechanism: https://opencode.ai/docs/mcp-servers/ → Manage → Glob patterns.)

**Confidence: verified-against-primary-docs** for the header mechanism, `oauth: false`, and `{env:}` interpolation; **inferred** (from reading the plugin source) that the plugin clobbers user `mcp.you` — the clobber itself is directly visible in the plugin source and the loader source, so treat it as verified-by-source.

---

## 4. Exact ready-to-merge config snippet (recommended, no plugin)

File: `.opencode/opencode.json` (project config; project-root `opencode.json` also works — both are loaded and deep-merged, project wins over global).

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "you": {
      "type": "remote",
      "url": "https://api.you.com/mcp",
      "enabled": true,
      "oauth": false,
      "headers": { "Authorization": "Bearer {env:YDC_API_KEY}" }
    },
    "you-free": {
      "type": "remote",
      "url": "https://api.you.com/mcp?profile=free",
      "enabled": true
    },
    "you-finance": {
      "type": "remote",
      "url": "https://api.you.com/mcp?tools=you-finance",
      "enabled": true,
      "oauth": false,
      "headers": { "Authorization": "Bearer {env:YDC_API_KEY}" }
    },
    "you-docs": {
      "type": "remote",
      "url": "https://you.com/docs/_mcp/server",
      "enabled": true
    }
  }
}
```

Notes:
- `you` = full authenticated server (search/answer/research/contents/news). `you-free` = keyless basic `you-search` only. `you-finance` = finance-only profile. `you-docs` = keyless docs search (`searchDocs` tool).
- Endpoints verified in the agent-skills README: https://github.com/youdotcom-oss/agent-skills (README → "Configure You.com MCP servers" / "Useful tool profiles").
- If you want the plugin's auto-updating skills instead, use arrangement B in §3d (plugin + `you-api` + tool-disable).
- Config precedence (global → project, deep-merged, later wins): https://opencode.ai/docs/config/ (Locations → Precedence order).

**Confidence: verified-against-primary-docs** (schema shapes from https://opencode.ai/docs/mcp-servers/; URLs from agent-skills README).

---

## 5. Skills and tools that become available

### Skills (registered by the plugin, or installable standalone)

| Skill | What it does (one line) |
|---|---|
| `you-web` | Current web search, URL content extraction, cited synthesis; routes to the `you-search` / `you-contents` / `you-research` MCP tools. |
| `you-free` | Keyless basic web search using only `you-search` (for when no API key / OAuth is available). |
| `you-research` | Routes research tasks between cost-conscious agent-led search, You.com Research API scripts, and managed `you-research` MCP fallback. |
| `you-finance` | Routes finance questions to a script, a Finance Research API call, or the finance MCP fallback. |
| `you-discover` | Finds the best way to integrate You.com APIs, MCP servers, SDKs, docs, and tools into an agentic project. |

- Source (descriptions): https://github.com/youdotcom-oss/agent-skills (README → Skills table)
- Source (skill list in repo): https://github.com/youdotcom-oss/agent-skills/tree/main/skills

### MCP tools (from the `you` server at `https://api.you.com/mcp`)

| Tool | What it does (one line) |
|---|---|
| `you-search` | Current web search with snippets, source discovery, freshness/domain-targeted queries. |
| `you-contents` | Reads supplied URLs / promising search results before relying on exact details. |
| `you-research` | One-shot cited synthesis (managed research) when the host exposes it. |
| `searchDocs` | You.com docs search (from the keyless `you-docs` server). |
| finance tools | Finance research tools (from the `?tools=you-finance` profile). |

- Source: https://github.com/youdotcom-oss/agent-skills/blob/main/skills/you-web/SKILL.md (Tools table + frontmatter)
- Source: https://github.com/youdotcom-oss/agent-skills/blob/main/skills/you-research/SKILL.md (frontmatter `mcp_servers`)

### Installing the skills WITHOUT the plugin

- `npx skills add youdotcom-oss/agent-skills` — the universal Agent Skills installer. It installs to `.agents/skills/` (project) or `~/.agents/skills/` (global), and **OpenCode reads `.agents/skills/<name>/SKILL.md`** directly. OpenCode is a supported agent target.
  - Source: https://github.com/youdotcom-oss/agent-skills (README → Start Here)
  - Source (install locations): https://github.com/vercel-labs/skills (README agent table: OpenCode → project `.agents/skills/`, global `~/.config/opencode/skills/`)
  - Source (OpenCode skill discovery): https://opencode.ai/docs/skills/ (Place files: `.agents/skills/<name>/SKILL.md`)
- Deterministic alternative: copy the 5 skill folders from `skills/` in the repo into `.opencode/skills/` (each folder contains `SKILL.md`).

**Confidence: verified-against-primary-docs.**

---

## 6. Windows-specific gotchas

1. **OpenCode officially recommends WSL on Windows** but runs natively on Windows/PowerShell. Remote MCP servers are plain HTTPS — no local process spawn, so no Windows-specific MCP issues. (Local-type MCP servers would need `npx`/`bun` on PATH; not needed here.)
   - Source: https://opencode.ai/docs/windows-wsl/
2. **Global config path on Windows:** `C:\Users\Jonah\.config\opencode\opencode.json` (`~` = `C:\Users\Jonah`). Project config: `.opencode/opencode.json` or project-root `opencode.json`.
   - Source: https://opencode.ai/docs/config/ (Locations)
3. **Env var persistence:** `setx YDC_API_KEY "<key>"` only affects **new** processes — restart the terminal and OpenCode. `$env:YDC_API_KEY = "<key>"` is session-only. If the var is unset, `{env:YDC_API_KEY}` becomes an empty string and the server returns 401 (silent failure — verify with `opencode mcp list` / a test call).
   - Source: https://opencode.ai/docs/config/ (Variables → Env vars)
4. **No hot reload:** config (including plugins and MCP servers) loads at startup. Restart OpenCode after any change.
   - Source: https://opencode.ai/docs/plugins/ and https://opencode.ai/docs/config/
5. **Plugin install uses Bun at startup** (bundled with OpenCode); the first startup after adding a plugin downloads/installs the npm package into `~/.cache/opencode/node_modules/`. On Windows this is handled internally, but expect a one-time delay.
   - Source: https://opencode.ai/docs/plugins/ ("How plugins are installed")
6. **OAuth avoidance:** with `"oauth": false` + headers, no browser authorization flow is triggered. (Without it, OpenCode would open a browser for OAuth on first tool use — the thing the user wants to avoid.)
   - Source: https://opencode.ai/docs/mcp-servers/ (OAuth → Disabling OAuth)
7. **MCP context cost:** each enabled MCP server adds its tool list to context. If you don't need finance/docs, set `"enabled": false` on those servers.
   - Source: https://opencode.ai/docs/mcp-servers/ (Caveats)

---

## 7. Ranked alternatives

1. **Manual config, no plugin (recommended)** — full control; API-key auth on `you`/`you-finance`; no OAuth servers; skills installed via `npx skills add` or copied. Downside: skills don't auto-update with the plugin.
2. **Plugin + custom-named API-key server (`you-api`) + disable plugin OAuth tools** — keeps auto-updating bundled skills and keyless servers, but is redundant (two `you`-equivalent servers) and relies on the `tools` glob to suppress OAuth prompts.
3. **Plugin alone, accept OAuth** — simplest, but requires the browser OAuth flow the user explicitly doesn't want.
4. **`you-free` keyless only** — no key needed at all, but limited to basic `you-search` (no contents/research/finance).
5. **`opencode-metasearch2` plugin** — explicitly out of scope (no API-key provider support; per task instructions).

---

## 8. Source URLs (all claims)

| Claim | Source |
|---|---|
| Package exists, v0.5.0, MIT, repo, README (skills + MCP + OAuth auth) | https://www.npmjs.com/package/@youdotcom-oss/opencode |
| Plugin source: registers 4 MCP servers + skills path; OAuth hardcoded; no YDC_API_KEY | https://github.com/youdotcom-oss/agent-skills/blob/main/packages/opencode/plugin.ts |
| Package.json (entry `./plugin.ts`, peer deps) | https://github.com/youdotcom-oss/agent-skills/blob/main/packages/opencode/package.json |
| Repo README: install routes, MCP endpoints, API-key header, skill descriptions, packages | https://github.com/youdotcom-oss/agent-skills |
| Skills directory listing | https://github.com/youdotcom-oss/agent-skills/tree/main/skills |
| you-web skill: tool names, bearer header, auth modes | https://github.com/youdotcom-oss/agent-skills/blob/main/skills/you-web/SKILL.md |
| you-research skill: tool profiles, docs server | https://github.com/youdotcom-oss/agent-skills/blob/main/skills/you-research/SKILL.md |
| `opencode plugin <module>` CLI command + flags | https://opencode.ai/docs/cli/ |
| Plugin config (`"plugin": [...]`), Bun install, load order, no hot reload | https://opencode.ai/docs/plugins/ |
| Remote MCP schema, headers, `oauth: false`, tool globs, `opencode mcp` commands | https://opencode.ai/docs/mcp-servers/ |
| Config precedence, `{env:}` interpolation (empty when unset), global path | https://opencode.ai/docs/config/ |
| Skill discovery locations (`.agents/skills/`) | https://opencode.ai/docs/skills/ |
| Windows/WSL guidance | https://opencode.ai/docs/windows-wsl/ |
| Plugin `config` hook receives merged config (`config.get()` → `hook.config?.(cfg)`) | https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/plugin/index.ts |
| Config-hook mutation pattern is the de-facto plugin mechanism | https://github.com/anomalyco/opencode/issues/24065 |
| `npx skills add` install locations (`.agents/skills/`, OpenCode supported) | https://github.com/vercel-labs/skills |
| API key issuance | https://you.com/platform/api-keys |

---

## 9. Confidence labels

- **verified-against-primary-docs:** plugin behavior (source read), CLI command existence, MCP schema + `oauth:false` + `{env:}` interpolation, config precedence, skill discovery paths, `npx skills add` locations, MCP endpoints, tool/skill names, Windows config path.
- **inferred:** that the plugin's unconditional `mcp.you` assignment defeats a user override in practice (the assignment and the loader order are both directly visible in source, so this is effectively verified-by-source, but no runtime test was performed); that `setx`/`$env:` are the right Windows mechanisms (standard Windows behavior, not OpenCode-documented).
- **UNKNOWN / not tested:** actual runtime behavior of the `you` server with a real key (no key used in this research); whether `npx skills add` prompts for agent selection on this machine (CLI is interactive by default).