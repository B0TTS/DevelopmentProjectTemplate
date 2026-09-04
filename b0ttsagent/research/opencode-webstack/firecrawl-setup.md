# Firecrawl + OpenCode on Windows — Integration Research

**Date:** 2026-09-03
**Scope:** How to wire Firecrawl (firecrawl.dev) into OpenCode (opencode.ai) on Windows (PowerShell host), repo `C:\Users\Jonah\DevelopmentProjectTemplate`.
**Status:** Research complete. No project files modified except this document.

---

## 1. Recommended integration path + why

**PRIMARY: Remote MCP server with a paid/full API key.**

```text
URL:  https://mcp.firecrawl.dev/v2/mcp
Auth: Authorization: Bearer <FIRECRAWL_API_KEY>   (header, NOT query param, NOT in URL)
```

Why this wins over the local npm server on Windows:

1. **Zero local process management.** No Node.js 22+ requirement, no `npx` spawn issues, no version pinning. Firecrawl's own docs list "spawn npx ENOENT" as a Windows failure mode for the local server — the remote path avoids that class of problem entirely.
2. **Full tool surface with an API key.** Hosted API-key mode exposes the full tool set (same as a local server connected to the cloud API). Keyless mode exposes only 3 tools.
3. **Firecrawl officially documents OpenCode for this exact endpoint.** Their docs show `{"mcp": {"firecrawl": {"type": "remote", "url": "https://mcp.firecrawl.dev/v2/mcp", "enabled": true}}}` for OpenCode — the remote shape is a first-class supported client config, not a hack.
4. **Key stays out of config files.** OpenCode's `{env:VARNAME}` interpolation in headers means the key lives only in a Windows environment variable.
5. **No meaningful downside for a cloud-API user.** The local server's only extra capability (direct local-file `firecrawl_parse` reading `filePath`) requires a **self-hosted** Firecrawl API (`FIRECRAWL_API_URL`); against the cloud API, hosted and local expose the same API-backed tools. Hosted parse of local files uses a two-call signed-upload handoff instead — minor.

**FALLBACK: Local stdio MCP server** (`npx -y firecrawl-mcp` with `FIRECRAWL_API_KEY` env) — use only if the remote endpoint is blocked (corporate firewall/proxy) or you need a self-hosted Firecrawl API.

---

## 2. Exact ready-to-merge opencode.json snippets

### 2a. PRIMARY — remote MCP with API key (recommended)

```json
{
  "mcp": {
    "firecrawl": {
      "type": "remote",
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "headers": {
        "Authorization": "Bearer {env:FIRECRAWL_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

### 2b. Keyless variant (no key, 3 tools, rate-limited — emergency fallback)

```json
{
  "mcp": {
    "firecrawl": {
      "type": "remote",
      "url": "https://mcp.firecrawl.dev/v2/mcp",
      "enabled": true
    }
  }
}
```

### 2c. FALLBACK — local npm MCP server (stdio)

```json
{
  "mcp": {
    "firecrawl": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "firecrawl-mcp"],
      "environment": {
        "FIRECRAWL_API_KEY": "{env:FIRECRAWL_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

**Where the file goes:** project-scoped `.opencode/opencode.json` (recommended for this repo — project wins over global on deep-merge) or global `~/.config/opencode/opencode.json`. Config is read at startup; **no hot reload** — restart OpenCode after editing.

---

## 3. Env vars / auth headers needed, and where to set them on Windows

| Item | Value | Where |
|---|---|---|
| `FIRECRAWL_API_KEY` (env var) | `fc-...` (create at https://www.firecrawl.dev/app/api-keys) | Windows **User** environment variable, set BEFORE launching OpenCode |
| `Authorization` header (remote MCP) | `Bearer {env:FIRECRAWL_API_KEY}` | In opencode.json `headers` — never hardcode the key |
| `FIRECRAWL_API_URL` (local fallback only) | Optional; only for self-hosted Firecrawl | Same env-var mechanism |

**Setting the env var in PowerShell (persistent, user-level):**

```powershell
[Environment]::SetEnvironmentVariable("FIRECRAWL_API_KEY", "fc-...", "User")
# or: setx FIRECRAWL_API_KEY "fc-..."
```

**Session-only (current shell only, inherited by OpenCode launched from it):**

```powershell
$env:FIRECRAWL_API_KEY = "fc-..."
```

Gotchas: `setx`/`SetEnvironmentVariable` only affect **new** processes — the current PowerShell session won't see the value; launch OpenCode from a fresh terminal. OpenCode interpolates `{env:...}` at config load (startup), so set the var before starting OpenCode and restart OpenCode after changing it.

---

## 4. Windows-specific gotchas

1. **`{env:VARNAME}` interpolation happens at startup.** Set `FIRECRAWL_API_KEY` before launching OpenCode; restart OpenCode after any change. No hot reload.
2. **Local npx MCP servers need the `cmd /c` wrapper.** Use `["cmd","/c","npx","-y","firecrawl-mcp"]` (command MUST be an array of strings). Firecrawl's own docs document the Windows failure "spawn npx ENOENT" and recommend using the `npx.cmd` path or a `cmd /c` wrapper; their npm README shows `cmd /c "set FIRECRAWL_API_KEY=... && npx -y firecrawl-mcp"` for Windows.
3. **Local server requires Node.js 22+** (Firecrawl docs, local page). Check with `node --version` before choosing the fallback path.
4. **Never put the API key in the MCP URL or in opencode.json.** Firecrawl explicitly warns: "Configure the key through an environment variable or your client's secret storage, never in the MCP URL." Query-param auth (`?FIRECRAWL_API_KEY=...`) is NOT a supported mechanism — the documented mechanism is the Bearer header (remote) or `FIRECRAWL_API_KEY` env (local stdio).
5. **Keyless mode is a trap for production use:** only `firecrawl_search`, `firecrawl_scrape`, `firecrawl_parse`, rate-limited. Crawl/map/agent/interact/monitor/research/developer tools require a key.
6. **OAuth endpoint (`/v2/mcp-oauth`) requires a client-side browser sign-in flow.** OpenCode's remote MCP config is a static URL+headers — whether OpenCode implements the interactive OAuth flow is unverified (see §7). The API-key path avoids this entirely.
7. **SECURITY NOTE (repo hygiene):** the local skill file `.agents/skills/fire-crawl/SKILL.md` ends with a "Session-specific auth" section containing a **real, live API key**. It was not copied or recorded here. Recommend rotating that key and removing it from the file — any agent reading the skill now has a working credential.
8. **Verify after startup:** check OpenCode's MCP tool list after launch. Keyless shows 3 tools; keyed shows the full surface. A `401` means the header didn't resolve — check the env var name and restart.

---

## 5. MCP tools exposed

**Keyless (no key):** `firecrawl_search`, `firecrawl_scrape`, `firecrawl_parse` only.

**With API key (full surface, subject to plan/team policy):**

- `firecrawl_scrape` (incl. JSON-schema structured extraction), `firecrawl_map`, `firecrawl_search`, `firecrawl_parse`
- `firecrawl_crawl`, `firecrawl_check_crawl_status`
- `firecrawl_agent`, `firecrawl_agent_status` (async research)
- `firecrawl_interact`, `firecrawl_interact_stop` (live-page clicks/forms)
- `firecrawl_research_search_papers`, `firecrawl_research_inspect_paper`, `firecrawl_research_related_papers`, `firecrawl_research_read_paper`, `firecrawl_research_search_github`
- `firecrawl_developer_search` (GitHub issues/PRs/READMEs/docs index)
- `firecrawl_monitor_create`, `firecrawl_monitor_list`, `firecrawl_monitor_get`, `firecrawl_monitor_update`, `firecrawl_monitor_run`, `firecrawl_monitor_delete`, `firecrawl_monitor_checks`, `firecrawl_monitor_check`
- `firecrawl_search_feedback`, `firecrawl_feedback` (opt-out via `FIRECRAWL_NO_SEARCH_FEEDBACK=1` / `FIRECRAWL_NO_ENDPOINT_FEEDBACK=1`)

Former `firecrawl_extract` is deprecated/removed — use scrape-with-JSON or agent.

---

## 6. The CLI path (`npx -y firecrawl-cli@latest init --all`) — substitute or complementary?

**Complementary, not a substitute.** The CLI (`firecrawl-cli`, v1.23.3) installs a terminal binary plus agent skills that teach the agent to shell out to `firecrawl search/scrape/interact/...` commands during a session. Inside OpenCode that means the agent drives web work through the bash tool, guided by installed skills — workable, and OpenCode is an officially supported harness (`--agent opencode` routes skills to it; `firecrawl setup mcp` can also write MCP config into editors). But MCP is the more native integration: structured tool calls with live input schemas, no shell parsing, no output-file round-trips. They coexist fine — MCP for in-session tool calls, CLI/skills for workflow deliverables and for the `firecrawl doctor`/`developer` diagnostics. If you want both, run the CLI init for skills AND add the remote MCP block above.

---

## 7. Ranked alternatives

1. **Remote MCP + API key** (PRIMARY — §2a). Full tools, zero local deps, officially documented for OpenCode.
2. **Local npm MCP** (`firecrawl-mcp`, FALLBACK — §2c). Same cloud tools; needs Node 22+, `cmd /c` wrapper; only advantage is self-hosted API support.
3. **Keyless remote MCP** (§2b). Zero setup, 3 tools, rate-limited — emergency only.
4. **OAuth remote MCP** (`https://mcp.firecrawl.dev/v2/mcp-oauth`). Browser sign-in, no key management — but requires OpenCode to implement the MCP OAuth browser flow, which is **unverified**; API key is simpler and documented.
5. **CLI + skills** (`npx -y firecrawl-cli@latest init --all`). Complementary layer, not a replacement for MCP (§6).
6. **Search-only endpoint** (`https://mcp.firecrawl.dev/v2/mcp-search`). Read-only: `firecrawl_search` + 5 research tools, own OAuth identity. Niche; not needed.

---

## 8. Source URLs

- Firecrawl MCP Get Started (API-key auth, Bearer header): https://docs.firecrawl.dev/mcp-server
- Firecrawl MCP For Agents / keyless + OpenCode snippet: https://docs.firecrawl.dev/mcp-server/keyless
- Firecrawl MCP tools (tool list, availability by mode): https://docs.firecrawl.dev/mcp-server/tools
- Firecrawl MCP local server (stdio, `FIRECRAWL_API_KEY`, Node 22+, Windows npx ENOENT): https://docs.firecrawl.dev/mcp-server/local
- Firecrawl MCP OAuth (humans): https://docs.firecrawl.dev/mcp-server/oauth
- npm `firecrawl-mcp` (v3.24.0, README: hosted/keyless/local, Windows `cmd /c` example, env vars, full tool docs): https://www.npmjs.com/package/firecrawl-mcp
- npm `firecrawl-cli` (v1.23.3, init/setup, `--agent opencode`, `firecrawl setup mcp`): https://www.npmjs.com/package/firecrawl-cli
- GitHub `firecrawl/firecrawl-mcp-server` (hosted/keyless/OAuth/API-key, search-only endpoint): https://github.com/firecrawl/firecrawl-mcp-server
- Local skill (CLI/REST/keyless paths; contains a live key — see §4.7): `C:\Users\Jonah\DevelopmentProjectTemplate\.agents\skills\fire-crawl\SKILL.md`
- OpenCode config facts (MCP shapes, `{env:}` interpolation, no hot reload, merge order): pre-verified per task brief (official OpenCode schema) — not re-fetched.

---

## 9. Confidence labels

| Claim | Label |
|---|---|
| Remote endpoint `https://mcp.firecrawl.dev/v2/mcp` + `Authorization: Bearer <key>` is the API-key auth mechanism (not query param, not x-api-key) | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server + /mcp-server/keyless + npm README + GitHub repo) |
| Keyless mode = same URL, no auth, only `firecrawl_search`/`firecrawl_scrape`/`firecrawl_parse`, rate-limited | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server/tools, /mcp-server/keyless) |
| Full tool list with API key (scrape/map/search/parse/crawl/agent/interact/research/developer/monitor/feedback) | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server/tools; npm README) |
| Local package `firecrawl-mcp`, stdio, `FIRECRAWL_API_KEY` env required for cloud API, Node 22+ | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server/local; npm) |
| Windows `spawn npx ENOENT` gotcha + `cmd /c` / `npx.cmd` remedy | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server/local troubleshooting; npm README Windows note) |
| OpenCode remote MCP config shape (`type: remote`, `headers`, `{env:}` interpolation, `cmd /c` array for local, startup-only load, project-wins merge) | **verified** (pre-verified facts from official OpenCode schema per task brief; Firecrawl docs independently show the OpenCode remote snippet) |
| OpenCode implements the interactive MCP OAuth browser flow for `/v2/mcp-oauth` | **UNKNOWN / inferred-uncertain** — Firecrawl docs show the config line but nothing confirms OpenCode's OAuth client support; API-key path avoids the question |
| CLI path is complementary rather than a substitute | **inferred** from npm README + local skill (CLI = shell commands + skills; MCP = native tools) |
| Local server has no advantage over hosted for cloud-API users (direct file parse needs self-hosted API) | **verified-against-primary-docs** (docs.firecrawl.dev/mcp-server/local note; npm README parse section) |

---

## 10. Dead ends / notes

- Did not re-verify OpenCode schema facts (task brief marked them verified).
- Did not test the connection live (no key used in this research; the key in the local skill file was deliberately not used or recorded).
- SearXNG tools were not used (deprecated per task rules); discovery used `websearch`, verification used `webfetch` on primary pages.