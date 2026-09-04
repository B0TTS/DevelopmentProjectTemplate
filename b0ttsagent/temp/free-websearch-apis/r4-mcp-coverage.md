# R4 — MCP Server Coverage for Candidate Search APIs

Research date: 2026-09-03. Scope: for each candidate search API, determine whether an official (vendor-maintained) or community MCP server exists, and how it is configured (package, run command, env vars, transport).

Method note: SearXNG instance returned empty results for all queries, so all discovery was done via the built-in `websearch` tool (Exa-backed) with page reads via `searxng_web_url_read`. Every material claim below carries a URL that was fetched/read this session.

---

## (a) Summary table

| API | Official/Community/None | Package (npm) | GitHub | Key env var(s) | Run command |
|---|---|---|---|---|---|
| Exa | **Official** (exa-labs) | `exa-mcp-server` (v3.4.1) | github.com/exa-labs/exa-mcp-server | `EXA_API_KEY` | `npx -y exa-mcp-server` (stdio); hosted remote `https://mcp.exa.ai/mcp` |
| Tavily | **Official** (tavily-ai) | `tavily-mcp` (v0.2.22) | github.com/tavily-ai/tavily-mcp | `TAVILY_API_KEY` | `npx -y tavily-mcp@latest` (stdio); hosted remote `https://mcp.tavily.com/mcp/?tavilyApiKey=...` |
| Serper | **Community only** (no official found) | `serper-search-mcp` (best-documented); also `serper-search-scrape-mcp-server`, `serper-dev-mcp`, PyPI `serper-mcp-server` | smjahid012/serper-search-mcp-server; marcopesani/mcp-server-serper; GreXLin85/serper.dev-mcp; garylab/serper-mcp-server | `SERPER_API_KEY` | `npx -y serper-search-mcp` (stdio) |
| LangSearch | **Community only** (no official found) | `langsearch-mcp-server` | fusman60/langsearch-mcp-server; OJamals/langsearch-mcp-ts; OJamals/langsearch-mcp-python | `LANGSEARCH_API_KEY` | `npx -y langsearch-mcp-server` (stdio) |
| Brave Search API | **Official** (brave org) | `@brave/brave-search-mcp-server` | github.com/brave/brave-search-mcp-server | `BRAVE_API_KEY` (or `BRAVE_API_KEY_FILE`) | `npx -y @brave/brave-search-mcp-server` (stdio default; `--transport http` optional) |
| Google CSE / PSE | **Community only** (no official; API closing 2027-01-01) | `@thejusdutt/google-search-mcp`; also `@adenot/mcp-google-search` | thejusdutt/google-search-mcp; hunter-arton/google_search_mcp_server; ayush-rudani/google-search-mcp-server | `GOOGLE_API_KEY` + `GOOGLE_CX` (or `GOOGLE_SEARCH_ENGINE_ID` / `GOOGLE_CSE_ID` per server) | `npx -y @thejusdutt/google-search-mcp` (stdio) |
| Bing Search API (Azure) | **None — API retired 2025-08-11**; no official MCP; legacy community servers target a dead API | `bing-search-mcp` (community, dead target) | leehanchung/bing-search-mcp; microsoft/semanticworkbench (mcp-server-bing-search) | `BING_API_KEY` / `BING_SEARCH_API_KEY` (dead API) | `uvx bing-search-mcp` (dead) |
| SearXNG (self-hosted) | **Community** (de-facto standard; in GitHub MCP Registry) | `mcp-searxng` (v2.1.0 per npm page) | github.com/ihor-sokoliuk/mcp-searxng | `SEARXNG_URL` | `npx -y mcp-searxng` or global `mcp-searxng` (stdio) |
| OrioSearch (self-hosted Tavily-compatible) | **Community** (MCP server bundled in repo) | none (Python, in-repo) | github.com/vkfolio/orio-search (`mcp-server/`) | `ORIOSEARCH_BASE_URL` | `python mcp-server/index.py` (stdio) |
| WebSearchFree (self-hosted Tavily-compatible) | **Community** (MCP integration bundled in repo) | none (Python, in-repo) | github.com/drmikecrypto/WebSearchFree (`integrations/mcp/`) | `WSF_BASE_URL` | `python integrations/mcp/server.py` (stdio) |
| SearchForge (self-hosted) | **Community** (built-in MCP server; listed in official MCP Registry) | none on npm (run via npx github: or OCI image) | github.com/divyanshu-iitian/SearchForge | `SEARCHFORGE_SEARXNG_URL` | `node dist/mcp.js` or `npx --package github:divyanshu-iitian/SearchForge searchforge-mcp` (stdio) |
| SearchHarvester (searcharvester) | **Community** (adapter repo; main repo is REST-only) | none (run via npx github:) | github.com/MaYunFei/searcharvester-mcp (adapter); vakovalskii/searcharvester (REST API) | `SEARCHARVESTER_API_KEY`, `SEARCHARVESTER_INTERNAL_URL`, `SEARCHARVESTER_EXTERNAL_URL` | `npx -y github:MaYunFei/searcharvester-mcp` (stdio) |
| OpenSERP (self-hosted SERP) | **Official** (openserpapi org) | `@openserp/mcp` | github.com/openserpapi/mcp | `OPENSERP_API_KEY` (cloud) / `OPENSERP_BASE_URL` (self-hosted) | `npx -y @openserp/mcp` (stdio; `--http` optional) |

---

## (b) Detail per API

### 1. Exa (exa.ai) — OFFICIAL

- **Official MCP server maintained by the vendor** (Exa Labs org). GitHub: https://github.com/exa-labs/exa-mcp-server — README states "Connect AI agents to Exa for web search, content fetching, and multi-step research."
- **npm package**: `exa-mcp-server`, v3.4.1, author "Exa Labs", repo `git+https://github.com/exa-labs/exa-mcp-server.git`, 25,462 weekly downloads, last updated 2026-08-18. https://www.npmjs.com/package/exa-mcp-server
- **Run**: stdio via `npx -y exa-mcp-server` with `"env": {"EXA_API_KEY": "your_api_key"}` (README config blocks for Cursor/VS Code/Claude Code/Claude Desktop all use `EXA_API_KEY`). https://github.com/exa-labs/exa-mcp-server/blob/main/npm.readme.md
- **Hosted remote (preferred by vendor)**: `https://mcp.exa.ai/mcp` — works anonymously with rate limits; API key via `?exaApiKey=...` query param, `x-api-key` header, or `Authorization: Bearer`; OAuth supported. https://github.com/exa-labs/exa-mcp-server and https://exa.ai/docs/reference/exa-mcp (page read directly this session; confirms server URL, `EXA_API_KEY` env var, and `x-api-key` header config).
- **Env var confirmed in source**: `process.env.EXA_API_KEY` in `api/mcp.ts`. https://github.com/exa-labs/exa-mcp-server/blob/main/api/mcp.ts
- **Vendor docs page**: https://exa.ai/docs/reference/exa-mcp ("Web Search MCP — Complete setup guide for Exa MCP Server").

### 2. Tavily (tavily.com) — OFFICIAL

- **Official MCP server** in the `tavily-ai` GitHub org. GitHub: https://github.com/tavily-ai/tavily-mcp ("Production ready MCP server with real-time search, extract, map & crawl").
- **npm package**: `tavily-mcp`, v0.2.22, author "Tavily", repo `tavily-ai/tavily-mcp`, 20,899 weekly downloads, updated 2026-08-05. https://www.npmjs.com/package/tavily-mcp ; package.json confirms name `tavily-mcp`, bin `tavily-mcp`. https://github.com/tavily-ai/tavily-mcp/blob/main/package.json
- **Run**: `npx -y tavily-mcp@latest` with `"env": {"TAVILY_API_KEY": "your-api-key-here"}` (optional `DEFAULT_PARAMETERS` JSON env var). https://github.com/tavily-ai/tavily-mcp
- **Env var confirmed in source**: `const API_KEY = process.env.TAVILY_API_KEY;` in `src/index.ts` (also `TAVILY_HUMAN_ID`, `DEFAULT_PARAMETERS`). https://github.com/tavily-ai/tavily-mcp/blob/259bfd20/src/index.ts
- **Hosted remote**: `https://mcp.tavily.com/mcp/?tavilyApiKey=<your-api-key>` (or `Authorization: Bearer`; OAuth optional). https://docs.tavily.com/documentation/mcp
- **Vendor docs page**: https://docs.tavily.com/documentation/mcp
- **Package-name conflict (important)**: Tavily docs and GitHub's gh-aw docs reference `@tavily/mcp` as the package name, but `https://registry.npmjs.org/@tavily%2Fmcp` returns **404 — the package does not exist**. The canonical, verified npm package is `tavily-mcp`. Sources: https://docs.tavily.com/documentation/mcp (mentions `@tavily/mcp`), https://github.github.com/gh-aw/reference/web-search/ (uses `npx -y @tavily/mcp`), https://github.com/github/gh-aw/pull/24610 (fixes wrong `@tavily/mcp-server` → `@tavily/mcp`), and the 404 from registry read this session.

### 3. Serper (serper.dev) — COMMUNITY ONLY (no official found)

- **No official MCP server found.** serper.dev homepage (https://serper.dev/) and its docs do not mention MCP; no `serperdev` GitHub org MCP repo surfaced in searches.
- **Community options (all use `SERPER_API_KEY`):**
  - `serper-search-mcp` (npm) — 8 tools (web/images/videos/news/shopping/places/deep_research/rag_context); `npx -y serper-search-mcp` with `SERPER_API_KEY` (+ optional `GEMINI_API_KEY`); stdio default, HTTP via `SERPER_MCP_TRANSPORT`. https://www.npmjs.com/package/serper-search-mcp ; https://github.com/smjahid012/serper-search-mcp-server
  - `serper-search-scrape-mcp-server` (npm) — `npx -y serper-search-scrape-mcp-server`, `SERPER_API_KEY`. https://www.npmjs.com/package/mcp-server-serper ; https://github.com/marcopesani/mcp-server-serper
  - `serper-dev-mcp` (npm) — 12 tools, `SERPER_API_KEY`, `npx -y serper-dev-mcp`; explicitly "not affiliated with Google or Serper.dev". https://github.com/GreXLin85/serper.dev-mcp
  - `serper-mcp-server` (PyPI) — `uvx serper-mcp-server`, `SERPER_API_KEY`. https://github.com/garylab/serper-mcp-server
  - Remote gateway: pipeworx-io/mcp-serper (hosted URL `https://gateway.pipeworx.io/serper/mcp`). https://github.com/pipeworx-io/mcp-serper
  - Also: Traia-IO/serper-api-mcp-server. https://github.com/Traia-IO/serper-api-mcp-server

### 4. LangSearch (langsearch.com) — COMMUNITY ONLY (no official found)

- **No official MCP server found.** docs.langsearch.com (https://docs.langsearch.com/) has no MCP page; langsearch.com homepage shows only REST API + LangChain/OpenAI function-call integrations. https://langsearch.com/
- **Community options (all use `LANGSEARCH_API_KEY`):**
  - `langsearch-mcp-server` (npm) — `npx -y langsearch-mcp-server` with `"env": {"LANGSEARCH_API_KEY": "sk-your-key"}`; tools `langsearch_web_search`, `langsearch_semantic_rerank`; API base https://api.langsearch.com. https://github.com/fusman60/langsearch-mcp-server
  - OJamals/langsearch-mcp-ts — `LANGSEARCH_API_KEY` (+ optional `LANGSEARCH_BASE_URL`). https://glama.ai/mcp/servers/OJamals/langsearch-mcp-ts
  - OJamals/langsearch-mcp-python — `LANGSEARCH_API_KEY`, run via `uv --directory ... run main.py`. https://glama.ai/mcp/servers/OJamals/langsearch-mcp-python

### 5. Brave Search API (brave.com/search/api) — OFFICIAL

- **Official MCP server** in the `brave` GitHub org. GitHub: https://github.com/brave/brave-search-mcp-server (web, local, image, video, news, LLM-context search; stdio default + HTTP).
- **npm package**: `@brave/brave-search-mcp-server`, author "Brave Software, Inc.", published 2025-07-16. https://www.npmjs.com/package/@brave/brave-search-mcp-server
- **Run**: `npx -y @brave/brave-search-mcp-server` with `"env": {"BRAVE_API_KEY": "YOUR_API_KEY_HERE"}`; `--transport http` optional; also Docker `docker.io/mcp/brave-search`. https://github.com/brave/brave-search-mcp-server
- **Env vars**: `BRAVE_API_KEY` (required unless `BRAVE_API_KEY_FILE` set), `BRAVE_MCP_TRANSPORT`, `BRAVE_MCP_PORT`, `BRAVE_MCP_HOST`. https://github.com/brave/brave-search-mcp-server/tree/v2.0.74
- **Vendor docs guide**: https://brave.com/search/api/guides/use-with-claude-desktop-with-mcp/
- **Reference server (Anthropic)**: `@modelcontextprotocol/server-brave-search` in the modelcontextprotocol/servers repo — `npx -y @modelcontextprotocol/server-brave-search`, `BRAVE_API_KEY`. https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search ; https://github.com/modelcontextprotocol/servers/blob/main/src/brave-search/README.md. Note: MCPpedia lists it as "Has been replaced by the official server." https://mcppedia.org/s/brave-search

### 6. Google Custom Search JSON API / Programmable Search Engine — COMMUNITY ONLY (no official; API closing)

- **No official Google MCP server found** (Google does not publish one for CSE).
- **Community options:**
  - `@thejusdutt/google-search-mcp` (npm) — `npx -y @thejusdutt/google-search-mcp`, env `GOOGLE_API_KEY` + `GOOGLE_CX`. https://www.npmjs.com/package/@thejusdutt/google-search-mcp ; https://github.com/thejusdutt/google-search-mcp
  - `@adenot/mcp-google-search` (npm) — `npx -y @adenot/mcp-google-search`, env `GOOGLE_API_KEY` + `GOOGLE_SEARCH_ENGINE_ID`. https://registry.npmjs.org/@adenot/mcp-google-search
  - hunter-arton/google_search_mcp_server — env `GOOGLE_API_KEY` + `GOOGLE_CSE_ID`. https://github.com/hunter-arton/google_search_mcp_server
  - ayush-rudani/google-search-mcp-server — env `GOOGLE_API_KEY` + `GOOGLE_SEARCH_ENGINE_ID`. https://github.com/ayush-rudani/google-search-mcp-server
  - limklister/mcp-google-custom-search-server — env `GOOGLE_API_KEY` + `GOOGLE_SEARCH_ENGINE_ID`. https://github.com/limklister/mcp-google-custom-search-server
- **CRITICAL lifecycle warning**: Google's own docs state "The following pricing applies only to existing Custom Search JSON API customers until the service discontinuation on January 1, 2027. This API is not available for new customers." https://developers.google.com/custom-search/v1/overview — i.e., the API is closed to new signups and dies 2027-01-01. Any new harness wiring to Google CSE is not viable.

### 7. Bing Search API (Azure) — NONE (API retired 2025-08-11)

- **API retired**: "Bing Search APIs will be retired on August 11, 2025. Any existing instances of Bing Search APIs will be decommissioned completely." https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement
- **No official MCP server** for the retired API. Microsoft's replacement is **Grounding with Bing Search** inside Azure AI Agents / Foundry — an agent tool, not a raw SERP API (returns grounded answers, not SERP JSON). https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools
- **Legacy community servers that target the now-dead API:**
  - leehanchung/bing-search-mcp — `BING_API_KEY`, `uvx bing-search-mcp`. https://github.com/leehanchung/bing-search-mcp
  - microsoft/semanticworkbench `mcp-server-bing-search` — README (read directly this session) shows it "Calls the Bing Search API" with `BING_SEARCH_API_KEY`; i.e., targets the retired v7 API. https://raw.githubusercontent.com/microsoft/semanticworkbench/main/mcp-servers/mcp-server-bing-search/README.md
- **Community wrapper for the replacement**: drewelewis/ai-bing-grounding-mcp — FastAPI + MCP server wrapping Azure AI Agent Service with Bing grounding (via Azure API Management MCP endpoint). https://github.com/drewelewis/ai-bing-grounding-mcp

### 8. SearXNG (self-hosted) — `mcp-searxng` (community, de-facto standard)

- **npm package**: `mcp-searxng` — npm page metadata: v2.1.0, MIT, author Ihor Sokoliuk, repo `ihor-sokoliuk/mcp-searxng`, 14,640 weekly downloads, updated 2026-08-25. https://www.npmjs.com/package/mcp-searxng
- **GitHub**: https://github.com/ihor-sokoliuk/mcp-searxng — 1,145 stars, 151 forks, MIT, created 2024-12-23; "Featured in the GitHub MCP Registry" (https://github.com/mcp/ihor-sokoliuk/mcp-searxng).
- **Config**: env `SEARXNG_URL` (your SearXNG instance URL; supports semicolon-separated replica list). Run: `npx -y mcp-searxng` or global install `mcp-searxng`; stdio. Requires Node.js 22+ (20 deprecated). https://github.com/ihor-sokoliuk/mcp-searxng and https://github.com/mcp/ihor-sokoliuk/mcp-searxng
- **Version discrepancy to note**: npmjs.com page shows latest 2.1.0 (updated 2026-08-25); `package.json` on `main` shows 1.15.0; a cached registry view showed 1.12.0. Treat "2.1.0" as the current npm release per the npm page metadata. https://github.com/ihor-sokoliuk/mcp-searxng/blob/main/package.json
- **Fork**: `@kassol/mcp-searxng` adds custom outgoing headers (`SEARXNG_HEADERS`, `URL_READER_HEADERS`). https://github.com/kassol/mcp-searxng
- Note: direct read of the npm page was blocked (403 bot detection); npm metadata above comes from the search tool's fetch of the npm page.

### 9. Self-hosted Tavily-compatible adapters

- **OrioSearch** — MCP server bundled in the repo (`mcp-server/`): Python, stdio, env `ORIOSEARCH_BASE_URL` (default http://localhost:8000), tools `web_search` + `web_extract`. Repo: https://github.com/vkfolio/orio-search ; MCP README: https://github.com/vkfolio/orio-search/blob/039173f1/mcp-server/README.md ; source: https://github.com/vkfolio/orio-search/blob/039173f1/mcp-server/index.py
- **WebSearchFree** — MCP integration bundled (`integrations/mcp/server.py`): Python, stdio, env `WSF_BASE_URL` (point at `wsf serve --port 8080`), tools `web_search` + `web_extract`. Repo: https://github.com/drmikecrypto/WebSearchFree
- **SearchForge** — built-in MCP server (stdio, tools `web_search`/`read_url`/`search_status`), env `SEARCHFORGE_SEARXNG_URL`; run via `node dist/mcp.js` or `npx --package github:divyanshu-iitian/SearchForge searchforge-mcp`; also published in the official MCP Registry as `io.github.divyanshu-iitian/searchforge` with OCI image `ghcr.io/divyanshu-iitian/searchforge-mcp:0.2.0`. Repo: https://github.com/divyanshu-iitian/SearchForge ; README: https://github.com/divyanshu-iitian/SearchForge/blob/main/README.md
- **SearchHarvester (searcharvester)** — main repo (vakovalskii/searcharvester, 237 stars) is a **REST-only** Tavily-compatible API (`/search`, `/extract`, `/research`); no MCP server in the main repo. A **community MCP adapter** exists: MaYunFei/searcharvester-mcp — `npx -y github:MaYunFei/searcharvester-mcp`, env `SEARCHARVESTER_API_KEY` (required), `SEARCHARVESTER_INTERNAL_URL`, `SEARCHARVESTER_EXTERNAL_URL`; tools `searcharvester_search` + `searcharvester_extract`. https://github.com/MaYunFei/searcharvester-mcp ; main repo: https://github.com/vakovalskii/searcharvester
- **OpenSERP** — **official** MCP server from the openserpapi org: npm `@openserp/mcp`, repo https://github.com/openserpapi/mcp. Run `npx -y @openserp/mcp` (stdio; `--http --host --port` for HTTP). Env: `OPENSERP_API_KEY` (Cloud, from https://openserp.org/dashboard/keys) or `OPENSERP_BASE_URL` (self-hosted OSS at http://localhost:7000); also `OPENSERP_BACKEND`, `OPENSERP_TIMEOUT_MS`. README: https://github.com/openserpapi/mcp/blob/main/README.md ; docs: https://openserp.org/docs/ ; upstream OSS: https://github.com/karust/openserp

---

## (c) Unverified / Not Found

- **`@tavily/mcp` npm package — NOT FOUND (404)**. Referenced by Tavily docs and GitHub gh-aw docs, but `https://registry.npmjs.org/@tavily%2Fmcp` returned 404 when read this session. Use `tavily-mcp` instead.
- **Serper official MCP — NOT FOUND.** No vendor-maintained server; serper.dev docs have no MCP page.
- **LangSearch official MCP — NOT FOUND.** docs.langsearch.com has no MCP page.
- **Google official MCP for CSE — NOT FOUND.** Google publishes no MCP server for Custom Search; and the API is closed to new customers (discontinuation 2027-01-01).
- **Bing official MCP — NOT FOUND.** API retired 2025-08-11; only legacy community servers targeting the dead API, plus a community wrapper for the Azure "Grounding with Bing" replacement.
- **mcp-searxng npm page** — direct read blocked (HTTP 403 bot detection); version/download data taken from the search tool's page fetch. Version discrepancy (2.1.0 vs 1.15.0 vs 1.12.0) noted above.
- **microsoft/semanticworkbench mcp-server-bing-search** — existence confirmed and README read (targets old Bing Search API, `BING_SEARCH_API_KEY`); no npm package, run via `uv run mcp-server-bing-search`.
- **SearchHarvester main repo** — no MCP server found in the main repo (REST-only); only the third-party MaYunFei adapter provides MCP.
- **Star counts** for most repos were not re-verified on-page this session except mcp-searxng (1,145) and searcharvester (237); treat other star figures as unverified.

---

## (d) Source list (all fetched/read this session)

Vendor docs / official:
- https://exa.ai/docs/reference/exa-mcp (read directly)
- https://github.com/exa-labs/exa-mcp-server ; https://github.com/exa-labs/exa-mcp-server/blob/main/npm.readme.md ; https://github.com/exa-labs/exa-mcp-server/blob/main/api/mcp.ts ; https://www.npmjs.com/package/exa-mcp-server
- https://docs.tavily.com/documentation/mcp ; https://github.com/tavily-ai/tavily-mcp ; https://github.com/tavily-ai/tavily-mcp/blob/main/package.json ; https://github.com/tavily-ai/tavily-mcp/blob/259bfd20/src/index.ts ; https://www.npmjs.com/package/tavily-mcp ; https://registry.npmjs.org/@tavily%2Fmcp (404, read directly)
- https://github.com/brave/brave-search-mcp-server ; https://github.com/brave/brave-search-mcp-server/tree/v2.0.74 ; https://www.npmjs.com/package/@brave/brave-search-mcp-server ; https://brave.com/search/api/guides/use-with-claude-desktop-with-mcp/
- https://developers.google.com/custom-search/v1/overview
- https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement ; https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/bing-tools
- https://langsearch.com/ ; https://docs.langsearch.com/ ; https://serper.dev/
- https://openserp.org/ ; https://openserp.org/docs/ ; https://github.com/openserpapi/mcp ; https://github.com/openserpapi/mcp/blob/main/README.md ; https://github.com/karust/openserp

Community servers:
- https://www.npmjs.com/package/serper-search-mcp ; https://github.com/smjahid012/serper-search-mcp-server ; https://www.npmjs.com/package/mcp-server-serper ; https://github.com/marcopesani/mcp-server-serper ; https://github.com/GreXLin85/serper.dev-mcp ; https://github.com/garylab/serper-mcp-server ; https://github.com/Traia-IO/serper-api-mcp-server ; https://github.com/pipeworx-io/mcp-serper
- https://github.com/fusman60/langsearch-mcp-server ; https://glama.ai/mcp/servers/OJamals/langsearch-mcp-ts ; https://glama.ai/mcp/servers/OJamals/langsearch-mcp-python
- https://www.npmjs.com/package/@thejusdutt/google-search-mcp ; https://github.com/thejusdutt/google-search-mcp ; https://registry.npmjs.org/@adenot/mcp-google-search ; https://github.com/hunter-arton/google_search_mcp_server ; https://github.com/ayush-rudani/google-search-mcp-server ; https://github.com/limklister/mcp-google-custom-search-server
- https://github.com/leehanchung/bing-search-mcp ; https://github.com/microsoft/semanticworkbench/tree/main/mcp-servers/mcp-server-bing-search ; https://raw.githubusercontent.com/microsoft/semanticworkbench/main/mcp-servers/mcp-server-bing-search/README.md (read directly) ; https://github.com/drewelewis/ai-bing-grounding-mcp
- https://www.npmjs.com/package/mcp-searxng ; https://github.com/ihor-sokoliuk/mcp-searxng (read directly) ; https://github.com/ihor-sokoliuk/mcp-searxng/blob/main/package.json ; https://github.com/mcp/ihor-sokoliuk/mcp-searxng ; https://github.com/kassol/mcp-searxng
- https://github.com/vkfolio/orio-search ; https://github.com/vkfolio/orio-search/blob/039173f1/mcp-server/README.md ; https://github.com/vkfolio/orio-search/blob/039173f1/mcp-server/index.py
- https://github.com/drmikecrypto/WebSearchFree
- https://github.com/divyanshu-iitian/SearchForge ; https://github.com/divyanshu-iitian/SearchForge/blob/main/README.md
- https://github.com/vakovalskii/searcharvester ; https://github.com/MaYunFei/searcharvester-mcp
- https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search ; https://github.com/modelcontextprotocol/servers/blob/main/src/brave-search/README.md ; https://mcppedia.org/s/brave-search
- https://github.com/github/gh-aw/pull/24610 ; https://github.com/github/gh-aw/issues/24567 ; https://github.github.com/gh-aw/reference/web-search/