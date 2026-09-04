# LangSearch → OpenCode Integration (Windows)

**Date:** 2026-09-03
**Scope:** How to wire the LangSearch web search API (langsearch.com) into OpenCode (opencode.ai) on Windows/PowerShell.
**Security note:** No real API keys appear in this doc. Use the placeholder `<LANGSEARCH_API_KEY>`.

---

## 1. Verdict & recommended path

**LangSearch has NO official MCP server or hosted MCP endpoint.** Its docs cover only two REST APIs (Web Search, Semantic Rerank) plus a LangChain integration — the docs index (`llms.txt`) contains no MCP page, and `github.com/langsearch/mcp-server` returns 404. All LangSearch MCP servers are community-maintained.

**Recommended path (viable):** run the community npm package **`langsearch-mcp-server`** (v1.0.1, MIT, by fusman60) as a **local stdio MCP server** via `npx`, with the API key injected through OpenCode's `environment` block. It is the only LangSearch MCP server that is (a) installable via `npx` (no Python/uv, no build step), (b) Node ≥18 stdio — matching OpenCode's local-MCP model on Windows, and (c) actively published on npm (2026-05-11).

**Caveat (honest):** this package is community code — 0 GitHub stars, 5 commits, single author, published 2026-05-11. It is a thin, readable wrapper (~150 lines) over the official REST API, so the supply-chain surface is small, but treat it as untrusted third-party code. The v1.0.0 npm metadata claimed homepage `github.com/langsearch/mcp-server` (the official org) — that repo does not exist (404); v1.0.1 correctly points at `fusman60/langsearch-mcp-server`. Do not mistake it for an official LangSearch product.

**Do NOT use the PyPI package `langsearch-mcp` (0.1.1)** — despite the name it is unrelated to langsearch.com (generic semantic-search MCP by "jiyzhang", placeholder repo `github.com/yourusername/langsearch-mcp`).

---

## 2. Ready-to-merge opencode.json snippet

Merge into the project config **`.opencode/opencode.json`** (project config wins over global `~/.config/opencode/opencode.json` on deep-merge; config loads only at startup — restart OpenCode after editing).

**Option A — recommended: key pulled from the Windows user environment (no secret in the config file):**

```json
{
  "mcp": {
    "langsearch": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "langsearch-mcp-server"],
      "environment": {
        "LANGSEARCH_API_KEY": "{env:LANGSEARCH_API_KEY}"
      },
      "enabled": true
    }
  }
}
```

**Option B — key inline (simpler, but the secret lives in the repo config — not recommended for a git repo):**

```json
{
  "mcp": {
    "langsearch": {
      "type": "local",
      "command": ["cmd", "/c", "npx", "-y", "langsearch-mcp-server"],
      "environment": {
        "LANGSEARCH_API_KEY": "<LANGSEARCH_API_KEY>"
      },
      "enabled": true
    }
  }
}
```

Notes:
- `command` MUST be an array of strings (OpenCode schema). The `["cmd","/c","npx","-y",...]` shape is required on Windows so `npx.cmd` resolves.
- The package's own README uses Claude Code's `"env"` key — OpenCode uses **`"environment"`**. Do not copy the README verbatim.
- The server is **stdio-only** (verified in source: `StdioServerTransport`, no `--sse`/HTTP flag). Do NOT configure it as `"type": "remote"`.

---

## 3. Env vars / auth — what and where (Windows)

| Variable | Required | Set where | Notes |
|---|---|---|---|
| `LANGSEARCH_API_KEY` | Yes | Windows user env var (recommended) OR inline in `environment` | Server exits at startup if missing (verified in source). Get key at https://langsearch.com/api-keys (dashboard: https://langsearch.com/dashboard → API Key Management). |
| `LANGSEARCH_RERANK_MODEL` | No | Same places | Optional; default `langsearch-reranker-v1` (verified in source). |

Set the user env var once in PowerShell (persists for future sessions; new processes pick it up):

```powershell
setx LANGSEARCH_API_KEY "<LANGSEARCH_API_KEY>"
```

Then restart OpenCode from a NEW terminal (setx does not update already-running processes). With Option A, OpenCode interpolates `{env:LANGSEARCH_API_KEY}` at config load.

**How the key is used on the wire** (verified in server source + official API docs): the server sends `Authorization: Bearer <key>` + `Content-Type: application/json` to `POST https://api.langsearch.com/v1/web-search` and `POST https://api.langsearch.com/v1/rerank`. There is no hosted MCP endpoint and no query-param auth — Bearer header only.

---

## 4. Tools exposed (and usefulness for a coding agent)

Verified from the npm package source (`src/index.js`):

1. **`langsearch_web_search`** — query (1–500 chars), count (1–10, default 10), freshness (`oneDay|oneWeek|oneMonth|oneYear|noLimit`), summary (bool), response_format (`markdown|json`). Returns title/URL/snippet/summary/datePublished. **Useful for a coding agent** — freshness filtering is genuinely valuable for "latest docs/API changes" lookups; markdown output is agent-friendly; 25k-char truncation guard.
2. **`langsearch_semantic_rerank`** — query, documents (1–100 strings), top_n, response_format. Niche for a coding agent (RAG-style document triage); harmless to leave enabled.

Both are read-only/idempotent (annotations in source).

---

## 5. Free tier / rate limits (one line)

Free tier: **1 QPS / 60 QPM / 1000 QPD** (rate limits scale with cumulative account recharge: $0 → 1/60/1000; $10–50 → 5/200/2000; $100 → 10/500/10000; $500 → 30/2000/100000) — a busy agent session can exhaust 1000 queries/day, so keep `count` low and `summary` off by default.

---

## 6. Windows-specific gotchas

1. **`cmd /c npx -y` is mandatory** — bare `"npx"` as a string or without `cmd /c` fails on Windows (npx.cmd resolution).
2. **Node ≥ 18 required** (package `engines`). Verify with `node --version`.
3. **First launch downloads the package** via `npx -y` — needs network; subsequent launches use the npx cache. Slow first start is normal.
4. **Missing key = silent-ish failure**: server prints `ERROR: LANGSEARCH_API_KEY environment variable is required` to stderr and exits — check OpenCode's MCP logs if the server shows as failed.
5. **No hot reload** — edit config, fully restart OpenCode.
6. **`setx` caveat** — set the env var, then start OpenCode from a new terminal; the running shell won't see it.
7. **Free-tier QPD** — 1000 searches/day; a long agent session doing many searches can hit 429s (server surfaces these as readable errors).
8. **Trust caveat** — community package, 0 stars; pin the version (`npx -y langsearch-mcp-server@1.0.1`) if you want reproducibility.

---

## 7. Ranked alternatives

1. **`langsearch-mcp-server` (npm, fusman60) — PRIMARY.** npx-installable, stdio, Node ≥18, no build step. Best fit for OpenCode on Windows. (community, MIT)
2. **`OJamals/langsearch-mcp-python` (Python/uv)** — same two tools; needs `uv` + git clone; stdio by default, can be switched to `streamable-http` locally (`mcp.run(transport="streamable-http")` → `http://localhost:8000/mcp`) if you ever want a remote-style endpoint. Heavier Windows setup (uv, Python ≥3.10). (community, MIT)
3. **`OJamals/langsearch-mcp-ts`** — TypeScript from source, requires clone + `npm run build`; not published to npm. Not worth it vs #1.
4. **Skip MCP entirely** — LangSearch is a plain REST API (`POST /v1/web-search`, Bearer auth). If you don't need MCP tool discovery, a tiny OpenCode plugin or direct `fetch` in agent code is simpler and removes the third-party MCP dependency.
5. **If the goal is just "web search inside OpenCode" (not LangSearch specifically):** `mrkrsl/web-search-mcp` (1.1k stars, keyless Bing/Brave/DDG) is a more battle-tested stdio MCP server — but it is not LangSearch.

---

## 8. Sources (all read in full, 2026-09-03)

| Claim | Source | Confidence |
|---|---|---|
| No official MCP page/endpoint; docs = 2 REST APIs + LangChain only | https://docs.langsearch.com/llms.txt (full index) | verified-against-primary-docs |
| REST auth = `Authorization: Bearer {API KEY}`; endpoints `/v1/web-search`, `/v1/rerank`; params | https://docs.langsearch.com/api/web-search-api.md ; https://docs.langsearch.com/getting-started/quickstart.md | verified-against-primary-docs |
| Free tier 1 QPS/60 QPM/1000 QPD; tier table | https://docs.langsearch.com/limits/api-limits.md | verified-against-primary-docs |
| npm `langsearch-mcp-server` exists, v1.0.1, 2026-05-11, MIT, Node ≥18, ESM, bin `src/index.js` | https://registry.npmjs.org/langsearch-mcp-server (registry JSON) | verified-against-primary-docs |
| Server reads `LANGSEARCH_API_KEY` (required), optional `LANGSEARCH_RERANK_MODEL`; stdio-only transport; tools `langsearch_web_search` / `langsearch_semantic_rerank`; Bearer header; 25k truncation | https://raw.githubusercontent.com/fusman60/langsearch-mcp-server/main/src/index.js | verified-against-primary-docs |
| Repo is community (fusman60, 0 stars, 5 commits, created 2026-05-11) | https://github.com/fusman60/langsearch-mcp-server | verified-against-primary-docs |
| Official org repo `github.com/langsearch/mcp-server` does NOT exist | https://github.com/langsearch/mcp-server (HTTP 404) | verified-against-primary-docs |
| PyPI `langsearch-mcp` 0.1.1 is unrelated to langsearch.com (placeholder repo) | https://pypi.org/project/langsearch-mcp | verified-against-primary-docs |
| Python/uv alternative details | https://glama.ai/mcp/servers/OJamals/langsearch-mcp-python | verified-against-primary-docs (listing) |
| Keyless alternative `mrkrsl/web-search-mcp` | https://github.com/mrkrsl/web-search-mcp | verified-against-primary-docs |
| OpenCode config facts (mcp schema, `environment`, `{env:VAR}`, project/global merge, no hot reload) | Provided as pre-verified facts in task brief (from official OpenCode schema) | verified-against-primary-docs (per task brief) |

**Anomalies / dead ends searched:**
- `github.com/langsearch/mcp-server` → 404 (v1.0.0 npm metadata referenced it; misleading).
- Searched for hosted endpoints (`mcp.langsearch.com`, "official MCP announcement") — none exist.
- PyPI `langsearch-mcp` is a name-collision trap — unrelated package.
- The docs Quickstart mentions "LLM tools, or AI Agent Plugins" but the page itself only documents cURL/Python REST calls — no MCP content.