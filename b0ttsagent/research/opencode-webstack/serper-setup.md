# Serper.dev → OpenCode (Windows) Integration Research

**Date:** 2026-09-03
**Scope:** How to wire the Serper.dev Google SERP API into OpenCode (opencode.ai) on Windows (PowerShell host), repo `C:\Users\Jonah\DevelopmentProjectTemplate`.
**Method:** Web research only (websearch + webfetch). No code changes. No real API keys recorded — placeholders only.

---

## 1. Verdict / Recommended Path

**Verdict: VIABLE — use the community npm MCP server `serper-search-mcp` (v3.0.3) as a local stdio MCP server.**

- Serper has **NO official MCP server** (no remote endpoint, no official npm/PyPI package). The serper.dev homepage footer lists only Haystack, Jan AI, CrewAI, and LangChain integrations — no MCP. (verified-against-primary-docs)
- The best-maintained community option as of 2026-09-03 is **`serper-search-mcp`** (npm, by smjahid012 / SMLabs AI): v3.0.3 published ~3 months ago (≈ Jun 2026), 7 versions with a documented v1→v2→v3 evolution, MCP SDK ^1.0.0, Node ≥ 18, zero-build JS entry designed for `npx`, stdio transport by default, Apache-2.0. (verified-against-primary-docs — npm registry page + GitHub repo)
- Honest caveats: tiny adoption (1 GitHub star, 0 forks, ~60 weekly npm downloads), solo maintainer. It is the *most recently maintained* option, not the most *adopted* one. The most-adopted option (`serper-search-scrape-mcp-server`, 165 stars / ~1.5k weekly downloads) has been stale for ~1 year and carries a vulnerable `@modelcontextprotocol/sdk@0.6.0` dependency — not recommended.
- If you need **scholar / patents / lens / autocomplete / maps / reviews** coverage (13 tools), the PyPI `serper-mcp-server` (garylab) is the fallback — but it is stale (last release Nov 10, 2025) and needs Python 3.11+ and `uvx` on Windows.
- If you want **zero third-party code**: the Serper REST API is a plain POST + `X-API-KEY` header — usable from OpenCode via bash/curl whenever needed (see §6). This is the "skip MCP" fallback.

---

## 2. Ready-to-Merge opencode.json Snippet

### Primary (recommended): `serper-search-mcp` via npx

Add to **project config** `.opencode/opencode.json` (project wins over global `~/.config/opencode/opencode.json`; deep-merged):

```json
{
  "mcp": {
    "serper": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "serper-search-mcp"],
      "environment": {
        "SERPER_API_KEY": "{env:SERPER_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

Notes:
- `command` MUST be an array of strings (OpenCode schema). The `["cmd","/c",...]` wrapper is required on Windows because `npx` is a `.cmd` shim that needs cmd.exe to resolve.
- `{env:SERPER_API_KEY}` interpolates from the process environment at startup — the key never lives in the config file. (If you prefer, you can put the literal key in `environment`, but then the key is in a file that could be committed — not recommended.)
- Optional: add `"GEMINI_API_KEY": "{env:GEMINI_API_KEY}"` to unlock the `deep_research` tool (uses Gemini/OpenRouter free tier). The other 7 tools need only `SERPER_API_KEY`.
- Config loads at startup — restart OpenCode after editing.

### Fallback A: `serper-mcp-server` (PyPI, garylab) via uvx — 13 tools incl. scholar/patents

Requires Python ≥ 3.11 and `uv` installed (`winget install astral-sh.uv` or `pip install uv`):

```json
{
  "mcp": {
    "serper": {
      "type": "local",
      "command": ["cmd", "/c", "uvx", "serper-mcp-server"],
      "environment": {
        "SERPER_API_KEY": "{env:SERPER_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

### Fallback B: REST API via curl (no MCP at all)

```powershell
# PowerShell one-liner (key from env var, never typed inline)
$body = @{ q = "query here"; gl = "us"; hl = "en" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri "https://google.serper.dev/search" `
  -Headers @{ "X-API-KEY" = $env:SERPER_API_KEY; "Content-Type" = "application/json" } `
  -Body $body
```

---

## 3. Env Vars / Auth Headers and Where to Set Them (Windows)

| Variable | Required | Used by | Set where |
|---|---|---|---|
| `SERPER_API_KEY` | Yes | All options (MCP servers read it from env; REST API sends it as `X-API-KEY` header) | Windows user env var: `setx SERPER_API_KEY <key>` in PowerShell, or System Properties → Environment Variables. **Must be set before OpenCode starts** (config loads at startup; MCP child processes inherit OpenCode's env). |
| `GEMINI_API_KEY` | No | `deep_research` tool of `serper-search-mcp` only | Same mechanism (`setx GEMINI_API_KEY <key>`). |
| `OPENROUTER_API_KEY` | No | `deep_research` alternative provider | Same mechanism. |

- The MCP servers themselves authenticate to Serper with the **`X-API-KEY` header** (POST + JSON body) — you never configure that header yourself; the server does it. (verified via secondary sources — see §7)
- `setx` only affects **new** processes — restart the terminal and OpenCode after setting.
- Never write the real key into `opencode.json`, this file, or any committed file.

---

## 4. Windows-Specific Gotchas

1. **`cmd /c` wrapper is mandatory** for npx/uvx in the `command` array — bare `"npx"` fails to spawn on Windows (it's `npx.cmd`).
2. **First `npx -y serper-search-mcp` run downloads the package** (~seconds, needs network). Subsequent runs hit the npx cache. If the machine is offline at OpenCode startup, the MCP server fails to start — check `opencode` logs.
3. **Node.js ≥ 18 required** for `serper-search-mcp` v3 (native `fetch`). Verify with `node --version`.
4. **No hot reload** — config is read at startup. Restart OpenCode after any change.
5. **Env interpolation timing**: `{env:SERPER_API_KEY}` is resolved when OpenCode starts. If you set the var with `setx` and don't restart the terminal, the value won't be visible.
6. **Project vs global config**: project `.opencode/opencode.json` deep-merges over global `~/.config/opencode/opencode.json` — put the Serper block in whichever scope you want it active for (project file recommended for this repo).
7. **PyPI fallback on Windows**: `uvx` must be on PATH; `uv` installs `uvx.exe`. First run also downloads the package.
8. **Do not commit the key**: `.opencode/opencode.json` with a literal key would be committed to git — use `{env:...}` interpolation.
9. **SearXNG note**: the repo's SearXNG instance is deprecated (returns junk) — Serper via MCP is a clean replacement for Google SERP data; OpenCode's built-in `websearch` (Exa) remains available as a keyless alternative.

---

## 5. Ranked Alternatives (honest maintenance status)

| Rank | Option | Tools | Maintenance status (as of 2026-09-03) | Verdict |
|---|---|---|---|---|
| 1 | **`serper-search-mcp`** (npm, smjahid012/SMLabs) — `npx -y serper-search-mcp` | `search_web`, `search_images`, `search_videos`, `search_news`, `search_shopping`, `search_places`, `deep_research` (needs LLM key), `search_rag_context` | v3.0.3 published ~3 months ago; 7 versions; MCP SDK ^1.0.0; Node ≥18; Apache-2.0. Tiny adoption: 1 star, ~60 weekly downloads, solo maintainer. | **RECOMMENDED** — most recently maintained, npx-native, stdio default. |
| 2 | **`serper-mcp-server`** (PyPI, garylab) — `uvx serper-mcp-server` | 13 tools: `google_search`, `_images`, `_videos`, `_places`, `_maps`, `_reviews`, `_news`, `_shopping`, `_lens`, `_scholar`, `_patents`, `_autocomplete`, `webpage_scrape` | v0.0.10 released Nov 10, 2025 (~10 months stale); 38 stars, 15 forks; Python ≥3.11; MIT. | Fallback if scholar/patents/lens coverage needed; stale. |
| 3 | **`serper-search-scrape-mcp-server`** (npm, marcopesani) | `google_search`, `scrape` | v0.1.2 published ~1 year ago; 165 stars, ~1,519 weekly downloads (most adopted); npm.io health score F 30/100 "maintenance-mode / poorly maintained"; vulnerable dep `@modelcontextprotocol/sdk@0.6.0`. | Not recommended — stale + vulnerable dep + only 2 tools. |
| 4 | **`postfix/serper-mcp`** (Go, fork of agenthands/serpapi-mcp) | single `serper` tool (type param), stdio + HTTP | Created 2026-04-20, 189 commits, 0 stars; upstream `agenthands/serper-mcp` **404s** — release binary links in INSTALL.md are dead; needs Go 1.25+ to build. | Skip — dead release links, no binaries, 0 adoption. |
| 5 | **`NightTrek/Serper-search-mcp`** | search + deep research | 48 stars; npm weekly downloads ~0; last updated 2026-02-19. | Skip — no npm distribution traction. |
| 6 | **`Traia-IO/serper-api-mcp-server`** | placeholder `example_tool` only | 3 commits, README admits tools not implemented. | Skip — non-functional. |
| 7 | **Serper REST API via curl** (no MCP) | all Serper types | N/A — first-party API. | Always available fallback; no third-party code. |

---

## 6. Serper REST API Facts (for the curl fallback)

- Base URL: `https://google.serper.dev` — per-type endpoints: `/search`, `/images`, `/news`, `/places`, `/maps`, `/shopping`, `/scholar`, `/patents`, `/autocomplete`, `/lens`, `/reviews`, `/videos` (homepage lists Search, Images, News, Maps, Places, Videos, Shopping, Scholar, Patents, Autocomplete).
- Auth: **`X-API-KEY: <key>` header**, POST with JSON body `{"q": "...", "gl": "us", "hl": "en"}`.
- Free tier: 2,500 queries/month, no credit card (per serper.dev homepage).
- Primary docs site `documentation.serper.dev` was **unreachable** during this research (transport errors on repeated fetches; `serper.dev/docs` returns 404) — auth mechanism confirmed via secondary sources instead (see §7).

---

## 7. Source URLs and Confidence Labels

| Claim | Confidence | Source(s) |
|---|---|---|
| Serper has no official MCP server; homepage lists only Haystack/Jan/CrewAI/LangChain integrations | verified-against-primary-docs | https://serper.dev (fetched 2026-09-03, footer integration list) |
| `serper-search-mcp` v3.0.3, published ~3 months ago, 8 tools, SERPER_API_KEY env, npx install, stdio default, Node ≥18, Apache-2.0 | verified-against-primary-docs | https://www.npmjs.com/package/serper-search-mcp ; https://github.com/smjahid012/serper-search-mcp-server |
| `serper-mcp-server` (PyPI) v0.0.10 released Nov 10, 2025; 13 tools; uvx install; SERPER_API_KEY env; Python ≥3.11 | verified-against-primary-docs | https://pypi.org/project/serper-mcp-server/ ; https://github.com/garylab/serper-mcp-server |
| `serper-search-scrape-mcp-server` v0.1.2 ~1 year stale; 1,519 weekly downloads; health F; vulnerable @modelcontextprotocol/sdk@0.6.0 | verified-against-primary-docs | https://www.npmjs.com/package/serper-search-scrape-mcp-server ; https://npm.io/package/serper-search-scrape-mcp-server ; https://github.com/marcopesani/mcp-server-serper |
| `postfix/serper-mcp` upstream `agenthands/serper-mcp` 404s; release links dead; Go 1.25+ | verified-against-primary-docs | https://github.com/postfix/serper-mcp/blob/main/INSTALL.md ; https://github.com/agenthands/serper-mcp (404) |
| Serper REST auth = `X-API-KEY` header, POST to google.serper.dev endpoints | verified-via-secondary-sources (primary docs unreachable) | https://tryagi.github.io/Serper/guides/authentication/ ; https://github.com/agenthands/serper-cli/blob/main/CLAUDE.md (cites Context7 verification of serper.dev) |
| Serper free tier 2,500 queries/month | verified-against-primary-docs | https://serper.dev |
| OpenCode config facts (paths, mcp schema, `{env:}` interpolation, no hot reload) | verified (given in task brief; not re-verified) | OpenCode official schema per task brief |
| `opencode-metasearch2` v0.1.2 has no API-key provider support | verified (given in task brief; not re-verified) | Task brief |

**Dead ends searched:** `documentation.serper.dev` (transport error ×2), `serper.dev/docs` (404), `github.com/agenthands/serper-mcp` (404), `serper.dev/api-keys` (login wall). SearXNG tools not used (deprecated per task rules).

---

## 8. One-Line Summary

Wire `serper-search-mcp` (npm) as a local stdio MCP server via `["cmd","/c","npx","-y","serper-search-mcp"]` with `SERPER_API_KEY` set as a Windows user env var and referenced as `{env:SERPER_API_KEY}` — no official Serper MCP exists, and this is the only actively maintained community option; curl + `X-API-KEY` remains the zero-dependency fallback.