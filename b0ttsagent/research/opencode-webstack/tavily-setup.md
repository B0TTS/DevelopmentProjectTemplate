# Tavily Web Search API → OpenCode Integration (Windows)

**Date researched:** 2026-09-03
**Scope:** How to wire Tavily (tavily.com) into OpenCode (opencode.ai) on Windows/PowerShell, repo `C:\Users\Jonah\DevelopmentProjectTemplate`.
**Status:** Research complete — no config files were modified. Snippets below are ready to merge.
**Security note:** No real API key appears anywhere in this doc. All examples use the placeholder `<TAVILY_API_KEY>` (or `{env:TAVILY_API_KEY}` interpolation).

---

## 1. Recommended integration path (TL;DR)

**Primary: Remote MCP server (Streamable HTTP) with API-key auth via `Authorization` header, `oauth: false`, key injected with `{env:TAVILY_API_KEY}`.**

Why this path wins on Windows:

- **Zero local dependencies** — no Node.js, no npx, no `cmd /c` process-spawn quirks. OpenCode talks HTTP directly to `https://mcp.tavily.com/mcp/`.
- **Canonical OpenCode pattern** — OpenCode's own docs show exactly this shape (`oauth: false` + `Authorization: Bearer {env:...}`) as the way to use API-key remote MCP servers (opencode.ai/docs/mcp-servers/, "Disabling OAuth" section).
- **Key never lands in a file or URL** — `{env:TAVILY_API_KEY}` is interpolated at startup from the Windows environment; the config file and URL stay clean.
- **Full tool set** — remote server exposes search/extract/map/crawl (keyed access). Keyless mode (see §6) is search+extract only.

**Fallback: Local npm MCP** — `tavily-mcp` package via `["cmd","/c","npx","-y","tavily-mcp"]` with `TAVILY_API_KEY` in the `environment` block. Works, but requires Node.js v20+, and npx cold-start on Windows can exceed OpenCode's default 5 s tool-fetch timeout (see §5).

---

## 2. Exact ready-to-merge opencode.json snippets

### 2a. PRIMARY — remote MCP, Authorization header (recommended)

Merge into **project config** `C:\Users\Jonah\DevelopmentProjectTemplate\.opencode\opencode.json` (create the file; none exists today) or **global config** `~/.config/opencode/opencode.json`. Project config deep-merges over global; project wins.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "tavily": {
      "type": "remote",
      "url": "https://mcp.tavily.com/mcp/",
      "oauth": false,
      "headers": {
        "Authorization": "Bearer {env:TAVILY_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

### 2b. Same path, Tavily-documented query-param auth (equally valid alternative)

Tavily's own docs lead with the key in the URL query param. Works with any MCP client; use this if header auth ever misbehaves:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "tavily": {
      "type": "remote",
      "url": "https://mcp.tavily.com/mcp/?tavilyApiKey={env:TAVILY_API_KEY}",
      "oauth": false,
      "enabled": true
    }
  }
}
```

### 2c. Optional: default search parameters (both remote variants)

Remote MCP accepts a `DEFAULT_PARAMETERS` header (JSON object string). Example — advanced depth, 10 results:

```json
"headers": {
  "Authorization": "Bearer {env:TAVILY_API_KEY}",
  "DEFAULT_PARAMETERS": "{\"search_depth\": \"advanced\", \"max_results\": 10}"
}
```

### 2d. FALLBACK — local npm MCP (Windows command array)

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "tavily": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "tavily-mcp"],
      "environment": {
        "TAVILY_API_KEY": "{env:TAVILY_API_KEY}"
      },
      "timeout": 30000,
      "enabled": true
    }
  }
}
```

Notes on 2d:
- `command` MUST be an array of strings; on Windows the `cmd /c` wrapper is required because `npx` resolves to `npx.cmd` and OpenCode does not spawn through a shell.
- `"timeout": 30000` raises OpenCode's default 5 s tool-fetch timeout — first `npx -y` run downloads the package and can exceed 5 s. (Inferred; see §7.)
- Pin a version if reproducibility matters: `"tavily-mcp@0.2.22"` (npm latest as of 2026-09-03). Tavily's own docs still show `@0.1.2`/`@0.1.3` in examples — stale; do not copy those pins.
- Optional env vars for local mode: `DEFAULT_PARAMETERS` (JSON string, e.g. `"{\"search_depth\": \"advanced\", \"max_results\": 10}"`) and `TAVILY_HUMAN_ID` (per-user attribution; see §4).

---

## 3. Every env var / auth header needed, and where to set it on Windows

| Item | Where it goes | Set on Windows via |
|---|---|---|
| `TAVILY_API_KEY` (required) | Remote: `{env:TAVILY_API_KEY}` inside header/URL in config. Local: `environment` block (or inherited from process env). | `setx TAVILY_API_KEY "tvly-<your-key>"` (user-level, persists; takes effect in NEW shells only) — or System Properties → Environment Variables → User variables. Session-only alternative: `$env:TAVILY_API_KEY = "tvly-<your-key>"` in PowerShell. |
| `DEFAULT_PARAMETERS` (optional) | Remote: `DEFAULT_PARAMETERS` header in config. Local: `environment` block. | Same `setx` mechanism if you want it inherited; otherwise inline in config. |
| `TAVILY_HUMAN_ID` (optional) | Local MCP only (forwarded as `X-Human-Id` API header). Remote MCP forwards `X-Human-Id` only if the client supplies it — OpenCode remote config has no per-server custom-header mechanism beyond `headers`, so for remote you can add it as a header if desired. | `setx TAVILY_HUMAN_ID "<opaque-id>"` or inline in `environment`. |

**Critical:** OpenCode loads config at startup — there is no hot reload. Set the env var, then **fully restart opencode** (new shell) before the server appears.

**Verification commands** (after restart): `opencode mcp list` (shows servers + auth status) and `opencode mcp debug tavily` (tests connectivity). Then prompt: "use the tavily tools to search for X".

---

## 4. Tavily MCP tools and which matter for a coding agent

Per the current package README (GitHub `tavily-ai/tavily-mcp`, npm `tavily-mcp@0.2.22`), the server exposes **four tools**:

| Tool | Purpose | Useful for coding-agent web research? |
|---|---|---|
| `tavily-search` | Real-time web search, ranked/scored results, domain filters, `search_depth` basic/advanced/fast | **Yes — core.** Source discovery when URLs are unknown. |
| `tavily-extract` | Pull structured content from given URLs (handles JS rendering, returns clean markdown-ish content) | **Yes — core.** Reading a specific page found by search. |
| `tavily-map` | Structured map of a site's pages/links | Sometimes — site structure before deep-diving. |
| `tavily-crawl` | Systematic multi-page crawl of a site | Rarely — heavy; only for whole-site ingestion. |

Recommended defaults for agent use (from Tavily's agents guide): `search_depth="advanced"`, `max_results=5` (focused) or `10` (broad), `chunks_per_source=3`, `include_domains`/`exclude_domains` when source trust matters; prefer Search → Extract for grounded answers.

**Keyless mode** (no key at all): remote MCP with header `X-Tavily-Access-Mode: keyless` exposes **only `tavily-search` and `tavily-extract`**, rate-limited, free. Crawl/Map/Research require an API key.

---

## 5. Windows-specific gotchas

1. **Remote path: essentially none.** No local process is spawned; the only Windows dependency is that `TAVILY_API_KEY` exists in the environment of the shell that launches opencode (see §3).
2. **Local path — `cmd /c` wrapper:** `"command": ["cmd", "/c", "npx", "-y", "tavily-mcp"]` is required. A bare `["npx", "-y", "tavily-mcp"]` fails on Windows because `npx` is `npx.cmd` and OpenCode doesn't invoke a shell.
3. **Local path — Node.js v20+** required (Tavily prerequisite). Check with `node --version`.
4. **Local path — first-run timeout:** `npx -y` downloads the package on first launch; OpenCode's default tool-fetch timeout is 5000 ms. Raise `"timeout"` (e.g. 30000) or pre-warm with a manual `npx -y tavily-mcp` run in a terminal.
5. **Local path — version pinning:** Tavily docs show `tavily-mcp@0.1.2`/`0.1.3` (stale). npm latest is **0.2.22** (28 versions, MIT, ~17k weekly downloads). Use `tavily-mcp` (latest) or pin `tavily-mcp@0.2.22`.
6. **JSON escaping:** `DEFAULT_PARAMETERS` is a JSON string inside JSON config — quotes must be escaped (`\"`).
7. **No hot reload:** config + env changes require a full opencode restart.
8. **Tool naming:** MCP tools are registered with the server name as prefix (e.g. `tavily_*`), so name the server `tavily` for clean tool names.

---

## 6. Ranked alternatives if the primary path fails

1. **Remote MCP + query-param key** (§2b) — same endpoint, Tavily's documented primary method; use if header auth is rejected.
2. **Remote MCP + OAuth** — omit key entirely: `{"type": "remote", "url": "https://mcp.tavily.com/mcp/"}` (no `oauth: false`). OpenCode auto-detects the 401 and runs the OAuth flow; trigger manually with `opencode mcp auth tavily`. Tavily picks the API key named `mcp_auth_default` in your dashboard (fallback: `default` key, then first available). Requires a one-time browser flow; tokens stored in `~/.local/share/opencode/mcp-auth.json`.
3. **Local npm MCP** (§2d) — full tool set, no network dependency on Tavily's MCP host beyond the API itself; needs Node 20+ and the Windows quirks in §5.
4. **Keyless remote MCP** — zero config, zero key: `"headers": {"X-Tavily-Access-Mode": "keyless"}` on `https://mcp.tavily.com/mcp/`. Search + Extract only, rate-limited; fine for light use while deciding on a key.
5. **Direct REST API via a custom tool/plugin** — Tavily's REST API (`https://api.tavily.com/search`, `Authorization: Bearer tvly-...`) could be wrapped in a custom OpenCode tool, but that's build work; the MCP paths above are strictly simpler.

---

## 7. Source URLs and confidence labels

| # | Claim | Source | Confidence |
|---|---|---|---|
| 1 | Remote MCP endpoint `https://mcp.tavily.com/mcp/`; key via query param `?tavilyApiKey=<key>` | https://docs.tavily.com/documentation/mcp.md ; https://github.com/tavily-ai/tavily-mcp (README) ; https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs |
| 2 | Key also accepted via `Authorization: Bearer <key>` header | https://github.com/tavily-ai/tavily-mcp (README) ; https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs |
| 3 | Remote MCP supports OAuth; key selection via `mcp_auth_default` naming | https://docs.tavily.com/documentation/mcp.md | verified-against-primary-docs |
| 4 | OpenCode remote MCP config shape (`type: remote`, `url`, `headers`, `enabled`, `timeout`, `oauth: false`); `{env:VAR}` interpolation in headers; `oauth: false` + `Authorization: Bearer {env:...}` shown as canonical API-key pattern; `opencode mcp list/auth/debug` commands; default 5 s timeout; local MCP `command` array + `environment` block | https://opencode.ai/docs/mcp-servers/ (last updated 2026-09-03) | verified-against-primary-docs |
| 5 | npm package `tavily-mcp`, latest **0.2.22**, 28 versions, MIT, ~16,982 weekly downloads | https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs |
| 6 | Local server reads `TAVILY_API_KEY` env var; optional `DEFAULT_PARAMETERS` and `TAVILY_HUMAN_ID` env vars | https://github.com/tavily-ai/tavily-mcp (README) ; https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs |
| 7 | Tools exposed: search, extract, map, crawl (`tavily-search`, `tavily-extract`, `tavily-map`, `tavily-crawl`) | https://github.com/tavily-ai/tavily-mcp (README) ; https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs |
| 8 | Keyless mode: `X-Tavily-Access-Mode: keyless` header; search+extract only; rate-limited; keyed responses identical | https://docs.tavily.com/documentation/keyless.md | verified-against-primary-docs |
| 9 | Node.js v20+ required for local MCP | https://docs.tavily.com/documentation/mcp.md | verified-against-primary-docs |
| 10 | Windows `cmd /c` wrapper needed for npx-based local MCP | Task brief (verified OpenCode config facts) + standard Windows `npx.cmd` behavior | accepted-as-given / inferred |
| 11 | First-run npx download may exceed 5 s tool-fetch timeout → raise `timeout` | OpenCode docs (timeout option exists, default 5000) + npx cold-start behavior | inferred |
| 12 | Tavily docs' local examples pin `tavily-mcp@0.1.2`/`0.1.3` (stale vs npm 0.2.22) | https://docs.tavily.com/documentation/mcp.md vs https://www.npmjs.com/package/tavily-mcp | verified-against-primary-docs (conflict surfaced) |
| 13 | Human-ID env var name: docs page says `HUMAN_ID`, package READMEs say `TAVILY_HUMAN_ID` | https://docs.tavily.com/documentation/mcp.md vs https://github.com/tavily-ai/tavily-mcp | conflict — package README (current, 0.2.22) treated as authoritative |
| 14 | Repo has no `.opencode/` config yet; project config would be a new file | Local filesystem check (glob) | verified (local) |

**Dead ends / not re-verified:** `opencode-metasearch2` plugin API-key support (verified false per task brief — not re-checked); SearXNG instance (deprecated — not used, per task rules).

---

## 8. One-line summary

Add a `tavily` remote MCP entry to `.opencode/opencode.json` (or global config) pointing at `https://mcp.tavily.com/mcp/` with `"oauth": false` and `"Authorization": "Bearer {env:TAVILY_API_KEY}"`, set `TAVILY_API_KEY` as a Windows user env var (`setx`), restart opencode, verify with `opencode mcp list` — fallback is the local `tavily-mcp` npm package via `["cmd","/c","npx","-y","tavily-mcp"]`.