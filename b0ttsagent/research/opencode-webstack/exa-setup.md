# Exa Web Search API → OpenCode Integration (Windows)

**Date researched:** 2026-09-03
**Scope:** How to wire Exa (exa.ai) into OpenCode (opencode.ai) on Windows/PowerShell, repo `C:\Users\Jonah\DevelopmentProjectTemplate`.
**Status:** Research complete — no config files were modified. Snippets below are ready to merge.
**Security note:** No real API key appears anywhere in this doc. All examples use the placeholder `<EXA_API_KEY>` (or `{env:EXA_API_KEY}` interpolation).

---

## 1. Recommended integration path (TL;DR)

**Primary: OpenCode's BUILT-IN `websearch` tool (already Exa-backed) + two Windows user environment variables. No opencode.json change required.**

Why this path wins on Windows:

- **Zero config, zero dependencies** — the tool is already compiled into opencode (verified in source at release tag `v1.18.27`). No MCP server, no npx, no Node.js requirement, no context-window cost from extra tool definitions.
- **It already works in current sessions** — the gate is an env var, and the tool is Exa-backed by default when only `OPENCODE_ENABLE_EXA` is set (provider selection logic verified in source).
- **A personal key IS supported and lifts rate limits** — contrary to what the docs page alone suggests ("No API key is required"), opencode's source reads `EXA_API_KEY` and appends it as `?exaApiKey=` to `https://mcp.exa.ai/mcp`. Exa's hosted MCP accepts that query param (backwards-compatible auth) and **bypasses the free-tier rate limits** (defaults: 2 QPS / 50 requests/day per IP) for keyed requests. So supplying a personal key changes behavior: it removes the free-tier cap. It is NOT required for the tool to function.
- **No OAuth flow risk** — the built-in tool posts directly to the MCP endpoint; no 401/OAuth dance.

**Fallback: Exa remote MCP server in `opencode.json`** (`x-api-key` header) — adds `web_fetch_exa` and (opt-in) `web_search_advanced_exa` / `agent_run` tools beyond the built-in search-only tool. Use this if you want advanced search filters or multi-step agent runs, or if the built-in tool is unavailable (very old opencode).

---

## 2. Exact ready-to-merge opencode.json snippets

### 2a. PRIMARY — nothing to merge (env vars only)

The built-in `websearch` tool needs **no config file entry**. Optional: explicitly allow the tool (it is allowed by default):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "permission": {
    "websearch": "allow"
  }
}
```

### 2b. FALLBACK A — remote MCP server, `x-api-key` header (Exa-documented, recommended fallback)

Merge into project config `.opencode/opencode.json` or global `~/.config/opencode/opencode.json` (project deep-merges over global; project wins). `{env:EXA_API_KEY}` is interpolated from the opencode process environment at startup.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "exa": {
      "type": "remote",
      "url": "https://mcp.exa.ai/mcp",
      "headers": {
        "x-api-key": "{env:EXA_API_KEY}"
      },
      "oauth": false,
      "enabled": true
    }
  }
}
```

`oauth: false` disables OpenCode's automatic OAuth detection (recommended for API-key servers; Exa's plain `/mcp` endpoint serves the free tier without auth, so OAuth would not trigger anyway).

### 2c. FALLBACK B — remote MCP server, `?exaApiKey=` query param (same mechanism opencode's built-in tool uses)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "exa": {
      "type": "remote",
      "url": "https://mcp.exa.ai/mcp?exaApiKey={env:EXA_API_KEY}",
      "oauth": false,
      "enabled": true
    }
  }
}
```

### 2d. FALLBACK C — local npm MCP server (Windows command array)

Package: **`exa-mcp-server`** (latest **3.4.1**, published 2026-08-22, requires Node.js ≥ 20). Reads `EXA_API_KEY` from its environment. Because local MCP servers are child processes of opencode, they inherit opencode's environment — if `EXA_API_KEY` is a Windows user env var, the `environment` block is optional (shown for explicitness):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "exa": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "exa-mcp-server"],
      "environment": {
        "EXA_API_KEY": "{env:EXA_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

### 2e. Optional: enable extra Exa MCP tools (fallback paths only)

Default tools: `web_search_exa`, `web_fetch_exa`. Opt-in via `?tools=` URL param: `web_search_advanced_exa` (full Search API filters), `agent_run` (multi-step research; requires a key). Example:

```json
"url": "https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa"
```

---

## 3. Every env var / auth header needed, and where to set it on Windows

### Env vars (built-in websearch path)

| Variable | Value | Effect | Source |
|---|---|---|---|
| `OPENCODE_ENABLE_EXA` | `1` (any truthy) | **Enables** the built-in `websearch` tool for non-OpenCode providers. Legacy aliases: `OPENCODE_EXPERIMENTAL_EXA`, `OPENCODE_EXPERIMENTAL`. | opencode docs + `runtime-flags.ts` |
| `EXA_API_KEY` | `<EXA_API_KEY>` | **Optional.** If set, opencode appends `?exaApiKey=<key>` to `https://mcp.exa.ai/mcp` → Exa bypasses free-tier rate limits (defaults 2 QPS / 50 req/day per IP). Without it, the tool still works on the free tier. | opencode `mcp-websearch.ts` (v1.18.27) + Exa `api/mcp.ts` |
| `OPENCODE_WEBSEARCH_PROVIDER` | `exa` | **Optional pin.** Only needed if `OPENCODE_ENABLE_PARALLEL` is ALSO set (Parallel wins when both flags are set; without the pin, provider is hash-picked per session). With only `OPENCODE_ENABLE_EXA=1`, provider is always `exa`. | opencode `websearch.ts` |

### Where to set them on Windows (so the opencode process sees them)

1. **User environment variables (recommended, works for every launch method):**
   - PowerShell: `setx OPENCODE_ENABLE_EXA 1` and `setx EXA_API_KEY <EXA_API_KEY>`
   - Or GUI: System Properties → Advanced → Environment Variables → User variables.
   - Takes effect only in **newly launched** processes — open a new terminal before starting opencode.
2. **PowerShell `$PROFILE` (PowerShell-launched sessions only):** add `$env:OPENCODE_ENABLE_EXA = "1"` and `$env:EXA_API_KEY = "<EXA_API_KEY>"`.
3. **NOT via a plugin `shell.env` hook** — that hook only injects env into shell executions (bash tool / user terminals), and the websearch gate is read from the opencode process env at startup. It cannot enable the tool.
4. **NOT via opencode.json** — the config schema has no top-level `env` field (verified against `https://opencode.ai/config.json`). Config `{env:VARNAME}` interpolation only *reads* process env for header/oauth/command values.

### Auth headers (fallback MCP paths)

| Path | Auth mechanism |
|---|---|
| Remote MCP (Fallback A) | `x-api-key: <EXA_API_KEY>` header (Exa's recommended method; priority #1) |
| Remote MCP (Fallback B) | `?exaApiKey=<EXA_API_KEY>` query param (priority #3, backwards-compatible) |
| Local npm (Fallback C) | `EXA_API_KEY` env var read by the server process |
| Built-in websearch | `?exaApiKey=` query param appended automatically when `EXA_API_KEY` is set |

Exa's auth priority (from `api/mcp.ts`): `x-api-key` header > `Authorization: Bearer` > `?exaApiKey=` query param > server env var. Free tier (no key) is rate-limited per IP; keyed requests bypass limits.

---

## 4. Windows-specific gotchas

1. **`setx` only affects new processes** — the current terminal keeps the old environment. Open a fresh terminal (or log off/on) before launching opencode. `setx` also truncates values >1024 chars (irrelevant for API keys).
2. **Config loads at startup, no hot reload** — restart opencode after any change to env vars or opencode.json.
3. **Local npm MCP cold start** — `npx -y exa-mcp-server` downloads the package on first run; on Windows this can exceed opencode's default 5 s tool-fetch timeout (`timeout` option exists on the MCP config; `experimental.mcp_timeout` also exists). Prefer the remote paths unless you need offline/local operation.
4. **Node.js ≥ 20 required** for `exa-mcp-server` 3.4.1 (engines field, npm registry).
5. **Command arrays must be `["cmd", "/c", "npx", "-y", "<pkg>"]`** on Windows — opencode spawns the array directly; bare `"npx"` strings fail.
6. **If both `OPENCODE_ENABLE_EXA` and `OPENCODE_ENABLE_PARALLEL` are set, Parallel wins** (checked first in provider selection). Pin with `OPENCODE_WEBSEARCH_PROVIDER=exa`.
7. **Free-tier 429s** — Exa's rate-limit error message tells you to add a key via `Authorization: Bearer` header or `?exaApiKey=` URL. Setting `EXA_API_KEY` (built-in path) or the header (MCP path) resolves it.
8. **Key in URL caveat** — `?exaApiKey=` puts the key in the URL (logs/proxies). Exa supports it explicitly and opencode's built-in tool uses it, but the `x-api-key` header (Fallback A) is the cleaner choice for the MCP path.
9. **WSL note** — opencode's Windows docs recommend WSL; if you run opencode inside WSL instead of native Windows, set these vars in the WSL shell profile (`~/.bashrc`/`~/.zshrc`), not Windows user env vars.

---

## 5. Ranked alternatives if the primary path fails

1. **Remote MCP + `x-api-key` header (Fallback A)** — Exa's documented method; adds `web_fetch_exa`; key stays out of URLs. Use if built-in websearch is unavailable or you want fetch/advanced tools.
2. **Remote MCP + `?exaApiKey=` param (Fallback B)** — identical mechanism to the built-in tool; useful if header auth ever misbehaves.
3. **Local npm `exa-mcp-server` (Fallback C)** — full control, works offline-ish; needs Node ≥ 20 and tolerates npx cold-start latency.
4. **`OPENCODE_ENABLE_PARALLEL` instead** — opencode's built-in websearch also supports Parallel (`https://search.parallel.ai/mcp`, `PARALLEL_API_KEY` → Bearer header). Not Exa; only relevant if Exa's service is down.
5. **Third-party opencode plugins** (e.g. `opencode-websearch-cited`, Brave/Serper plugins) — NOT recommended: the `opencode-metasearch2` plugin (v0.1.2) has no API-key provider support (verified separately), and other plugins add context/tool overhead for what the built-in tool already does.

---

## 6. Source URLs

- Exa Search API reference (auth via `Authorization: Bearer`, endpoint `POST https://api.exa.ai/search`): https://exa.ai/docs/reference/search-api-guide-for-coding-agents
- Exa MCP docs (hosted URL `https://mcp.exa.ai/mcp`, OpenCode tab, `x-api-key` header, free plan, `?tools=` param, 429 troubleshooting): https://exa.ai/docs/reference/exa-mcp
- Exa MCP npm package (latest 3.4.1, `EXA_API_KEY` env): https://www.npmjs.com/package/exa-mcp-server
- npm registry metadata (version 3.4.1, engines node ≥20, bin `dist/stdio.cjs`): https://registry.npmjs.org/exa-mcp-server/latest
- Exa MCP server source — hosted handler auth priority + rate limits (`api/mcp.ts`): https://github.com/exa-labs/exa-mcp-server/blob/main/api/mcp.ts
- Exa MCP server source — stdio env parsing (`src/stdio.ts`): https://github.com/exa-labs/exa-mcp-server/blob/main/src/stdio.ts
- OpenCode tools docs (websearch gate: OpenCode provider OR `OPENCODE_ENABLE_EXA`/`OPENCODE_ENABLE_PARALLEL`; "No API key is required"): https://opencode.ai/docs/tools
- OpenCode MCP servers docs (remote/local shapes, headers, `{env:...}` interpolation, `oauth: false`): https://opencode.ai/docs/mcp-servers
- OpenCode config JSON schema (no top-level `env`; `McpRemoteConfig`/`McpLocalConfig` shapes; `websearch` permission): https://opencode.ai/config.json
- OpenCode plugins docs (`shell.env` hook injects into shell execution only): https://opencode.ai/docs/plugins
- OpenCode source — built-in websearch tool (`packages/opencode/src/tool/websearch.ts`, provider selection + `OPENCODE_WEBSEARCH_PROVIDER`): https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/tool/websearch.ts
- OpenCode source — Exa MCP client (`packages/opencode/src/tool/mcp-websearch.ts`, `EXA_API_KEY` → `?exaApiKey=`): https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/tool/mcp-websearch.ts (identical at release tag `v1.18.27`: https://raw.githubusercontent.com/anomalyco/opencode/v1.18.27/packages/opencode/src/tool/mcp-websearch.ts)
- OpenCode source — runtime flags (`packages/opencode/src/effect/runtime-flags.ts`, `enableExa` = `OPENCODE_EXPERIMENTAL` | `OPENCODE_ENABLE_EXA` | `OPENCODE_EXPERIMENTAL_EXA`): https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/effect/runtime-flags.ts
- OpenCode repo (default branch `dev`; latest release v1.18.27, 2026-09-02): https://github.com/anomalyco/opencode
- OpenCode Windows docs (WSL recommendation; native Windows supported): https://opencode.ai/docs/windows-wsl

---

## 7. Confidence labels

| Claim | Label |
|---|---|
| Built-in `websearch` gated by `OPENCODE_ENABLE_EXA` / `OPENCODE_ENABLE_PARALLEL` (truthy), or OpenCode/OpenCode Go provider | **verified-against-primary-docs** (opencode.ai/docs/tools) + **verified-against-source** (runtime-flags.ts) |
| Built-in websearch reads `EXA_API_KEY` and appends `?exaApiKey=` to `https://mcp.exa.ai/mcp` | **verified-against-source** (mcp-websearch.ts at release tag v1.18.27 and dev) — note: NOT mentioned in opencode's docs page, which only says "no API key is required" |
| Exa hosted MCP accepts `x-api-key` header, `Authorization: Bearer`, and `?exaApiKey=` query param (priority in that order) | **verified-against-source** (exa-labs api/mcp.ts) + **verified-against-primary-docs** (exa.ai/docs/reference/exa-mcp) |
| Free tier rate limits default 2 QPS / 50 requests/day per IP; keyed requests bypass | **verified-against-source** (api/mcp.ts defaults `RATE_LIMIT_QPS=2`, `RATE_LIMIT_DAILY=50`; comment "Users who provide their own API key via ?exaApiKey= bypass rate limiting") — defaults may differ in production deployment (env-overridable) |
| `exa-mcp-server` npm latest = 3.4.1, reads `EXA_API_KEY` env var, Node ≥ 20 | **verified-against-primary-docs** (npm registry metadata + src/stdio.ts) |
| Remote MCP config shape, `headers`, `{env:VAR}` interpolation, `oauth: false` | **verified-against-primary-docs** (opencode.ai/docs/mcp-servers + config.json schema) |
| opencode.json has no top-level `env` field (cannot set process env from config) | **verified-against-primary-docs** (config.json schema — `Config` has no `env` property) |
| Plugin `shell.env` hook cannot enable the websearch tool | **inferred** (docs say the hook injects into "all shell execution (AI tools and user terminals)"; the websearch gate reads process env at startup — combination of verified docs + inference) |
| Local MCP servers inherit opencode's process env (so a user-level `EXA_API_KEY` reaches `npx exa-mcp-server` without the `environment` block) | **inferred** (standard child-process semantics; not explicitly documented) |
| `setx` / user env vars are the correct Windows mechanism; new processes only | **inferred** (standard Windows behavior, not opencode-specific) |
| With only `OPENCODE_ENABLE_EXA=1` set, provider is always Exa (Parallel only wins if its flag is also set) | **verified-against-source** (websearch.ts `selectWebSearchProvider` order) |

---

## 8. Dead ends / notes

- SearXNG tools were not used (deprecated instance per task rules); discovery used the built-in `websearch` tool, retrieval used `webfetch`.
- The opencode docs page for `websearch` does NOT document `EXA_API_KEY` — this is a source-level finding (mcp-websearch.ts). It is present in the latest release (v1.18.27), so it is live behavior, not unreleased dev code.
- Exa's OAuth flow exists for some clients (Claude connectors, plugin clients) but the plain `/mcp` endpoint serves the free tier without auth; opencode's built-in tool and the fallback configs above do not need OAuth.