# R3 — Self-Hosted / Free-Forever Web Search Options for an AI Agent Harness

**Date:** 2026-09-03 · **Scope:** self-hosted, no-key, no-paywall options · **Method:** SearXNG instance search returned empty for all queries this session, so all discovery ran through the Exa-backed `websearch` tool; repo metadata (stars, license, last push) was read directly from the GitHub API (`api.github.com/repos/...`) and the 4get Gitea instance. Every claim below carries the URL that was actually fetched/read.

**Headline context for the harness:** the existing self-hosted SearXNG is the only mature, actively-maintained metasearch core; the "Tavily-compatible adapter" ecosystem is real but young (most projects are weeks-to-months old, small star counts). Whoogle — the best-known alternative — was **archived in July 2026 because Google blocked it**, which is direct evidence of the upstream-scraping fragility that also explains the local engine failures (brave/ddg/startpage rate limits) already observed.

---

## (a) Summary table

| Project | What it is | API surface | License | Maintenance | URL |
|---|---|---|---|---|---|
| **SearXNG** | Metasearch aggregating 70+ engines; the de-facto self-hosted standard | Native JSON/CSV/RSS API (`/search?format=json`), GET+POST; own JSON format (not Tavily) | AGPL-3.0 | Very active: pushed 2026-09-03, 36,485 stars | https://github.com/searxng/searxng · https://docs.searxng.org |
| **OrioSearch** | Tavily-compatible API layer over SearXNG + Redis (FastAPI); content extraction, optional LLM answers | Tavily-compatible `POST /search`, `/search/stream`, `/extract`, `GET /tool-schema` | README claims MIT; **no LICENSE file in repo (GitHub API: null)** | Young: created 2026-03-06, pushed 2026-06-07, 42 stars | https://github.com/vkfolio/orio-search · https://www.oriosearch.org |
| **WebSearchFree** | Single C++ binary: keyless Tavily-shaped search+extract; metasearch over DDG HTML, Brave HTML, Wikipedia, optional SearXNG | Tavily-shaped `POST /search` + `/extract` (own HTTP server `wsf serve`) | MIT | Very new: created 2026-08-03, pushed 2026-08-17, 5 stars | https://github.com/drmikecrypto/WebSearchFree |
| **SearchForge** | TypeScript REST API + MCP server; intent-routed search (SearXNG/Wikipedia/GitHub/Crossref/HN/Jina Reader) | Own REST API + MCP `web_search`/`read_url` tools (not Tavily) | MIT | New: created 2026-07-23, pushed 2026-07-25, 2 stars; v0.2.0 release | https://github.com/divyanshu-iitian/SearchForge |
| **Searcharvester** | FastAPI Tavily-compatible search + markdown extract + deep-research agent over SearXNG (100+ engines) + trafilatura | Tavily-compatible `POST /search`, `/extract`, `/research` | AGPL-3.0 | Active-ish: created 2025-09-11, pushed 2026-04-27, 258 stars | https://github.com/vakovalskii/searcharvester |
| **OpenSERP** | Go SERP API + CLI; browser-rendered scraping of Google, Bing, Yandex, Baidu, DDG, Ecosia; page extraction | Own REST: `GET /{engine}/search`, `/mega/search`; JSON/markdown/text/ndjson (not Tavily) | MIT | Active: created 2023-06-23, pushed 2026-07-22, 1,338 stars | https://github.com/karust/openserp · https://openserp.org |
| **Whoogle** | Google-proxy metasearch UI | No JSON API (HTML only) | MIT | **ARCHIVED 24 Jul 2026 — "no longer returns search results"**; final release v1.2.4 (2026-04-15); 11.5k stars | https://github.com/benbusby/whoogle-search |
| **4get** | Lightweight PHP proxy metasearch with rotating proxies per scraper | JSON API: `GET /api/v1/web`, `/images`, `/videos`, `/news`, `/music` (own format, not Tavily) | AGPL-3.0-only | Very active: last commit 2026-09-02 | https://git.lolcat.ca/lolcat/4get · https://4get.ca |
| **YaCy** | Decentralized P2P search engine with own crawler + index (Java/Solr); federated swarm | JSON API (`yacysearch.json`), OpenSearch (own format) | GPL-2.0+ (some LGPL parts) | Active: last push 2026-07-07, ~4k stars | https://github.com/yacy/yacy_search_server · https://yacy.net |
| **LibreY** | PHP metasearch (fork of LibreX); scrapes Google, DDG, Brave, Ecosia, Yandex, Mojeek | JSON API (`api.php`) — own format, not Tavily | AGPL-3.0 | Moderate: pushed 2026-06-10, 316 stars | https://github.com/Ahwxorg/LibreY |

**Additional finds (brief, see §B.11):** trawl (Tavily wire-compatible, SearXNG/DDGS), tavily-open/TrailSearch (Tavily-like, SearXNG+Crawl4AI), agent-search (FastAPI over SearXNG, own REST), qsearch (corpus-first, Brave BYOK + SearXNG), YagoSeek (Go YaCy node with Tavily-compatible API), searxng-docker-tavily-adapter (one-shot, 0 stars).

---

## (b) Detail per project

### 1. SearXNG — the incumbent core

- **What it is:** free internet metasearch engine aggregating results from 70+ search services; users neither tracked nor profiled. Source: https://github.com/searxng/searxng (repo description, read via GitHub API https://api.github.com/repos/searxng/searxng)
- **JSON API:** two endpoints `/` and `/search`, GET (query params) and POST (form data); `format=json|csv|rss` must be enabled in `settings.yml` under `search:`; requesting an unset format returns 403; many public instances disable JSON. Source: https://docs.searxng.org/dev/search_api.html
- **Response shape (own format, not Tavily):** `query`, `number_of_results`, `results[]` (url, title, content, engine, score, positions, category…), `answers`, `corrections`, `infoboxes`, `suggestions`, `unresponsive_engines`. Source: https://gist.github.com/wnoronha/b5e31f0e21f8ddf6238e286740b5f147 (auto-generated OpenAPI spec of the Search API)
- **License:** AGPL-3.0. Source: https://api.github.com/repos/searxng/searxng
- **Activity:** pushed_at 2026-09-03; 36,485 stars; 3,328 forks; Python. Source: https://api.github.com/repos/searxng/searxng. No GitHub releases (releases API returns `[]` — versioning via docs build tags, current docs build "2026.9.3+a1144dda3"). Sources: https://api.github.com/repos/searxng/searxng/releases?per_page=2 , https://docs.searxng.org/dev/search_api.html
- **Rate-limit/CAPTCHA reality (documented):** the limiter docs state verbatim: "The intention of rate limitation is to limit suspicious requests from an IP. The motivation behind this is the fact that SearXNG passes through requests from bots and is thus classified as a bot itself. As a result, the SearXNG engine then receives a CAPTCHA or is blocked by the search engine (the origin) in some other way." Source: https://docs.searxng.org/admin/searx.limiter.html
- **Limiter config:** enable via `server: limiter: true` + Valkey (formerly Redis) URL; methods configured in `/etc/searxng/limiter.toml` (ip_lists, ip_limit, link_token, probe headers); `pass_ip` list gives unrestricted access (e.g. private ranges). Source: https://docs.searxng.org/admin/searx.limiter.html
- **API rate limits when limiter on:** `API_MAX = 4` requests per IP per `API_WINDOW = 3600` s for API requests (`format != html`); burst 15/20 s, long 150/600 s; suspicious-IP window 2,592,000 s. Source: https://docs.searxng.org/src/searx.botdetection.html
- **Public-instance blocking (documented):** searx.space: "Public instances listed here may yield less accurate results as they have much higher traffic and consequently have a higher chance of being blocked by search providers such as Google, Qwant, Bing, Startpage, etc. Hosting your own instance … may give you a more consistent search experience." Source: https://searx.space/
- **Deployment:** official Docker image; limiter needs Valkey; no own index/storage beyond cache. Free, no key. (Docker image claim is standard SearXNG packaging; not separately verified this session — see UNVERIFIED.)

### 2. OrioSearch — Tavily-compatible adapter over SearXNG

- **What it is:** "Self-hosted, Tavily-compatible web search and content extraction API. Drop-in replacement for Tavily." Stack: SearXNG (metasearch) + FastAPI + Redis caching; multi-tier extraction (trafilatura + readability-lxml); optional LLM answers (Ollama/OpenAI/Groq); FlashRank reranking; SSE streaming; DuckDuckGo auto-fallback if SearXNG down. Sources: https://github.com/vkfolio/orio-search , https://www.oriosearch.org/
- **API surface:** Tavily-compatible `POST /search`, `POST /search/stream`, `POST /extract`, `GET /tool-schema`; `api_key` optional (empty string works). Source: https://github.com/vkfolio/orio-search
- **Deployment:** `docker compose up --build` starts 3 services: API (:8000), SearXNG (:8080), Redis (:6379). Source: https://github.com/vkfolio/orio-search
- **License discrepancy:** README and marketing site say "MIT License", but the GitHub API reports `license: null` and the `/license` endpoint returns 404 — i.e. **no LICENSE file detected in the repo**. Flag for legal review before adoption. Sources: https://api.github.com/repos/vkfolio/orio-search , https://api.github.com/repos/vkfolio/orio-search/license , https://github.com/vkfolio/orio-search
- **Maintenance:** created 2026-03-06, pushed 2026-06-07, 42 stars, 17 forks; several forks exist (e.g. majid-rafei, Kayruchi, kaka-sangi) — fork activity suggests community interest but the upstream has been quiet ~3 months. Sources: https://api.github.com/repos/vkfolio/orio-search , https://github.com/majid-rafei/orio-search
- **Free:** yes — no key, no quota; only optional LLM provider needs a key if you use AI answers.

### 3. WebSearchFree — keyless Tavily-shaped binary

- **What it is:** "Free open-source Tavily alternative — keyless web search + content extraction for AI agents, RAG, LangChain, MCP." C++20 library + CLI + optional localhost HTTP server (`wsf serve`); metasearch across DuckDuckGo HTML, Brave Search HTML, Wikipedia, optional self-hosted SearXNG, DDG news; extractive (non-LLM) `answer`; readability-style extraction; no telemetry, outbound HTTPS only to public engines. Sources: https://github.com/drmikecrypto/WebSearchFree , https://github.com/drmikecrypto/WebSearchFree/blob/main/README.md
- **API surface:** Tavily-shaped `POST /search` + `/extract` at `http://127.0.0.1:8080`; no Authorization header required; supports `max_results`, `search_depth` (basic|advanced), `topic` (general|news), `include_domains`/`exclude_domains`, `include_answer`. Source: https://github.com/drmikecrypto/WebSearchFree
- **License:** MIT. Source: https://api.github.com/repos/drmikecrypto/WebSearchFree
- **Maintenance:** created 2026-08-03, pushed 2026-08-17, 5 stars, C++. **Very new (1 month old) — treat as unproven.** Source: https://api.github.com/repos/drmikecrypto/WebSearchFree
- **Deployment:** Docker/GHCR image (`ghcr.io/drmikecrypto/websearchfree:latest`), compose, Windows/Linux one-liner install scripts. Source: https://github.com/drmikecrypto/WebSearchFree
- **Free:** yes — no keys, no quota, no vendor cloud.

### 4. SearchForge — intent-routed REST + MCP

- **What it is:** "Open-source web search API and MCP server for LLMs, AI agents, and RAG." TypeScript; routes each query by intent (`auto`, `web`, `code`, `academic`, `community`, `read_url`) across no-key sources: Wikipedia, GitHub search, Crossref, Hacker News (Algolia), Jina Reader; broad web metasearch via an included private SearXNG stack; Brave optional keyed backend. Sources: https://github.com/divyanshu-iitian/SearchForge , https://github.com/divyanshu-iitian/SearchForge/blob/main/README.md
- **API surface:** own REST API (bearer `SEARCHFORGE_API_KEY` optional, rate limit 60 req/min/client default) + MCP stdio tools `web_search`, `read_url`, `search_status` + CLI + TypeScript SDK. **Not Tavily-compatible.** Source: https://github.com/divyanshu-iitian/SearchForge
- **License:** MIT. Source: https://api.github.com/repos/divyanshu-iitian/SearchForge
- **Maintenance:** created 2026-07-23, pushed 2026-07-25, 2 stars; v0.2.0 release ("Free capability-routed search"). New and low-adoption. Sources: https://api.github.com/repos/divyanshu-iitian/SearchForge , https://github.com/divyanshu-iitian/SearchForge/releases/tag/v0.2.0
- **Notable stance:** "SearchForge intentionally does not configure public SearXNG instances. They often disable JSON or limit automated traffic; the Docker stack is the stable free path." — corroborates the public-instance fragility. Source: https://github.com/divyanshu-iitian/SearchForge
- **Free:** yes, no keys by default.

### 5. Searcharvester — Tavily-compatible search + extract + research

- **What it is:** "Self-hosted search + markdown harvester for AI agents. SearXNG (100+ engines) + FastAPI + trafilatura." Three services: `POST /search` (Tavily-compatible via SearXNG), `POST /extract` (URL → clean markdown via trafilatura, size presets s/m/l/f + pagination), `POST /research` (deep-research agent spawning a Hermes Agent container). Pre-built GHCR images (`ghcr.io/vakovalskii/searcharvester:2.1.0`). Sources: https://github.com/vakovalskii/searcharvester , https://github.com/vakovalskii/searcharvester/blob/main/docs/en/api.md
- **API surface:** Tavily-compatible `POST /search` (fields: query, max_results, include_raw_content, engines, categories) — works with the official `tavily-python` client via `base_url` override; `api_key` accepted but ignored. Source: https://github.com/vakovalskii/searcharvester/blob/main/docs/en/api.md
- **Caveat (self-disclosed):** "`/search` score is fake (`0.9 - i*0.05`). Don't use it for ranking." Source: https://github.com/vakovalskii/searcharvester/blob/main/docs/en/api.md
- **License:** AGPL-3.0. Source: https://api.github.com/repos/vakovalskii/searcharvester
- **Maintenance:** created 2025-09-11, pushed 2026-04-27, 258 stars, 43 forks — the most-adopted adapter found. Source: https://api.github.com/repos/vakovalskii/searcharvester
- **Free:** yes — `/search` and `/extract` need no keys; `/research` needs an OpenAI-compatible LLM endpoint.

### 6. OpenSERP — self-hosted SERP API (browser-rendered scraping)

- **What it is:** "free, open-source SERP API and CLI for Google, Yandex, Baidu, Bing, DuckDuckGo, and Ecosia" with browser rendering and optional page-content extraction; positioned as SerpApi/Serper alternative; also usable as LLM/agent search tool. Sources: https://github.com/karust/openserp , https://openserp.org/
- **API surface:** own REST: `GET /{engine}/search` (google|yandex|baidu|bing|duck|ecosia) + `GET /mega/search` (multi-engine, modes balanced/any/fast); `format=json|markdown|text|ndjson`; `extract` param embeds cleaned page content; official SDKs (Python, JS, MCP, n8n). **Not Tavily-compatible.** Sources: https://github.com/karust/openserp , https://github.com/karust/openserp/blob/main/docs/openapi.yaml
- **License:** MIT. Sources: https://api.github.com/repos/karust/openserp , https://github.com/karust/openserp/blob/main/docs/openapi.yaml
- **Maintenance:** created 2023-06-23, pushed 2026-07-22, 1,338 stars, 153 forks — the most mature project in this list after SearXNG/YaCy. Source: https://api.github.com/repos/karust/openserp
- **Deployment:** self-hosted server (default port 7000); a paid hosted cloud exists (same API) but the OSS version is free, no keys, no rate limits. Sources: https://github.com/karust/openserp , https://openserp.org/
- **Caveat:** browser-rendered scraping of Google/Bing/Yandex is exactly the CAPTCHA-prone category the harness already hit; OpenSERP supports proxy headers for mitigation (per openapi.yaml `ProxyURLHeader` etc.). Source: https://github.com/karust/openserp/blob/main/docs/openapi.yaml

### 7. Whoogle — ARCHIVED, not viable

- **Status:** repo archived; banner: "Whoogle has reached the end of the road — 24 Jul 2026. Whoogle no longer returns search results, and that isn't something this project can fix." Final release v1.2.4 (2026-04-15). MIT, ~11.5k stars. Sources: https://github.com/benbusby/whoogle-search , https://github.com/benbusby/whoogle-search/releases
- **API:** no JSON API (HTML UI only; LibreY's comparison table marks Whoogle as having no API). Source: https://github.com/Ahwxorg/LibreY
- **Verdict:** dead end — Google blocked it; do not select.

### 8. 4get — active lightweight proxy metasearch with JSON API

- **What it is:** "4get is a proxy search engine that doesn't suck" — PHP metasearch proxying major engines, with rotating proxies on a per-scraper basis, bot protection, no-JS interface, favicon caching; RAM ~100–400 MB. Sources: https://git.lolcat.ca/lolcat/4get , https://git.lolcat.ca/lolcat/4get/src/branch/master/README.md
- **API surface:** JSON API, GET endpoints: `/api/v1/web?s=…`, `/api/v1/images`, `/api/v1/videos`, `/api/v1/news`, `/api/v1/music`; pagination via `npt` token (expires after use or 15 min). Own format, not Tavily. Sources: https://4get.ca/api.txt , https://git.lolcat.ca/lolcat/4get/src/branch/master/api/v1/index.php (the v1 index.php is a 404 "Unknown endpoint" stub — real endpoints are routed elsewhere)
- **License:** AGPLv3-only. Sources: https://git.lolcat.ca/lolcat/4get , https://git.lolcat.ca/lolcat/4get/src/branch/master/license.txt
- **Maintenance:** very active — last commit 2026-09-02 ("scrape google sublinks…"), 458 commits; 24 open issues. Source: https://git.lolcat.ca/lolcat/4get
- **Deployment:** Docker config in repo (`docker/` dir); official instance 4get.ca + instance list. Source: https://git.lolcat.ca/lolcat/4get/src/branch/master/README.md
- **Free:** yes. Caveat: single-maintainer project on a personal Gitea (2 stars there); Google-scraper churn visible in commit history.

### 9. YaCy — own-index P2P engine (heaviest option)

- **What it is:** "free search engine software for local search, organization-wide search portals, and a decentralized peer-to-peer web index" — crawls and indexes the web itself (Java + Solr), federated swarm of peers. Sources: https://yacy.net/ , https://github.com/yacy/yacy_search_server
- **API surface:** own JSON API (`yacysearch.json`) + OpenSearch endpoints; not Tavily-compatible. (Endpoint claim from project docs/README — partially UNVERIFIED this session; see §c.)
- **License:** GPL-2.0-or-later with some LGPL elements per-file. Source: https://github.com/yacy/yacy_search_server
- **Maintenance:** active — last push 2026-07-07 (Jetty 12 migration commit 2026-07-12), ~4k stars, 80 contributors. Sources: https://github.com/yacy/yacy_search_server , https://github.com/yacy/yacy_search_server/commit/554911a88f8c5084146a8a098965f18e67416525
- **Deployment:** Java + Solr — heavy (the YagoSeek author cites "Java + Solr (heavy to run and hack on)" as the reason for a rewrite); Docker available; needs its own index/storage and crawl time before results are good. Sources: https://community.searchlab.eu/t/hey-mom-i-rewrote-yacy-in-go/3411 , https://www.reddit.com/r/vibecoding/comments/1ux1fuc/i_wanted_a_free_selfhosted_tavily_so_i_wrote_a/
- **Free:** yes.

### 10. LibreY — lightweight PHP metasearch

- **What it is:** fork of LibreX; "Framework and JS free privacy respecting meta search engine"; text results from Google, DuckDuckGo, Brave Search, Ecosia, Yandex Search, Mojeek; images from Qwant; torrents; no logs. Source: https://github.com/Ahwxorg/LibreY
- **API surface:** has an API (`api.php` on the official instance; README comparison table marks "API ✅") — own format, not Tavily. Source: https://github.com/Ahwxorg/LibreY , https://librey.org/
- **License:** AGPL-3.0. Source: https://api.github.com/repos/Ahwxorg/LibreY
- **Maintenance:** created 2023-08-02, pushed 2026-06-10, 316 stars, 30 forks, 23 open issues. Source: https://api.github.com/repos/Ahwxorg/LibreY
- **Free:** yes. Caveat: same upstream-scraping fragility (Google/DDG/Brave scrapers).

### 11. Additional finds (brief)

- **trawl** — "self-hosted, Tavily-compatible search API for local development"; reimplements Tavily's full HTTP API (`/search`, `/extract`, `/crawl`, `/map`) on SearXNG (bundled) or DDGS fallback; wire-compatible with official Tavily SDKs via base-URL override. MIT, 1 star, created+pushed 2026-07-11. Sources: https://github.com/adityaparab/trawl , https://api.github.com/repos/adityaparab/trawl
- **tavily-open (TrailSearch)** — "Open-source replacement for Tavily, powered by SearXNG and Crawl4AI"; Tavily-like `POST /tavily/search` + `/tavily/extract`; local SQLite FTS reuse, Redis caching, optional Brave fallback. MIT, 31 stars, created 2026-01-08, pushed 2026-07-27. Sources: https://github.com/jianjungki/tavily-open , https://api.github.com/repos/jianjungki/tavily-open
- **agent-search** — FastAPI layer over SearXNG with 17 endpoints (dedup, cross-engine scoring, extraction, query expansion, prompt-injection scrubbing, optional Tor stack); own REST + MCP, not Tavily. MIT, 78 stars, created 2026-02-18, pushed 2026-08-31. Its README corroborates engine fragility: "Google, Startpage, Yahoo, and Reddit are best-effort explicit sources rather than defaults because they are commonly blocked or empty." Sources: https://github.com/brcrusoe72/agent-search , https://api.github.com/repos/brcrusoe72/agent-search
- **qsearch** — corpus-first hybrid search for agents (Meilisearch + Qdrant, Crawl4AI); Brave BYOK + optional SearXNG; MCP-over-HTTP; Apache-2.0, 2 stars, pushed 2026-09-03 (active today). README notes: "SearXNG rate limits. Self-host required — public instances get blocked by Google." Sources: https://github.com/theYahia/qsearch , https://api.github.com/repos/theYahia/qsearch
- **YagoSeek (D4rk4/yago)** — pure-Go reimplementation of a YaCy peer: own sharded Bleve index + federated YaCy swarm + optional DDGS fallback (off by default); **Tavily-compatible `/search`, `/extract`, `/crawl`, `/map`** with scoped API keys, plus YaCy-compatible endpoints; alpha (v0.0.5, 2026-07-11). AGPL-3.0, 19 stars, created 2026-07-01, pushed 2026-08-31. Sources: https://github.com/D4rk4/yago , https://api.github.com/repos/D4rk4/yago , https://github.com/D4rk4/yago/releases/tag/v0.0.5 , https://community.searchlab.eu/t/hey-mom-i-rewrote-yacy-in-go/3411
- **searxng-docker-tavily-adapter (luculli)** — ready Docker Compose stack (SearXNG + Tavily-compatible adapter + Redis); AGPL-3.0, 0 stars, created AND pushed 2026-04-14 (single-day project, effectively abandoned). Sources: https://github.com/luculli/searxng-docker-tavily-adapter , https://api.github.com/repos/luculli/searxng-docker-tavily-adapter

---

## (c) Unverified / Not Found

- **Named adapters:** all five named candidates **exist** — OrioSearch, WebSearchFree, SearchForge, Searcharvester, OpenSERP. None NOT FOUND. (Note: "SearchHarvester" resolves to **Searcharvester** — vakovalskii/searcharvester; no separate "SearchHarvester" project was found.)
- **OrioSearch license:** README/site claim MIT, but GitHub API reports `license: null` and `/license` returns 404 — no LICENSE file detected. Reported as a discrepancy, not resolved. Sources: https://api.github.com/repos/vkfolio/orio-search , https://api.github.com/repos/vkfolio/orio-search/license
- **SearXNG latest release tag:** GitHub releases API returns `[]` (SearXNG does not publish GitHub releases); current version inferred from docs build "2026.9.3+a1144dda3" and pushed_at 2026-09-03. UNVERIFIED: exact Docker tag name.
- **SearXNG official Docker image name** (`searxng/searxng`): standard knowledge, not re-verified this session — UNVERIFIED here.
- **YaCy JSON API endpoint details** (`yacysearch.json`): asserted in secondary sources only; exact endpoint path not read from primary docs this session — UNVERIFIED.
- **4get API endpoint paths** beyond `/api/v1/web|images|videos|news|music` (from https://4get.ca/api.txt): the repo's `api/v1/index.php` is a 404 stub; routing implementation not inspected — partially UNVERIFIED.
- **WebSearchFree / SearchForge / trawl / qsearch / YagoSeek / agent-search / tavily-open / OpenSERP** — all verified to exist with repo metadata from the GitHub API; deeper claims (exact response schemas, runtime behavior) rest on their READMEs/docs, which were read via search-result page content, not full-page fetches.

---

## (d) Source list (all fetched/read this session)

**SearXNG**
- https://docs.searxng.org/dev/search_api.html
- https://docs.searxng.org/admin/searx.limiter.html
- https://docs.searxng.org/src/searx.botdetection.html
- https://searx.space/
- https://api.github.com/repos/searxng/searxng
- https://api.github.com/repos/searxng/searxng/releases?per_page=2
- https://gist.github.com/wnoronha/b5e31f0e21f8ddf6238e286740b5f147

**Adapters (named candidates)**
- https://github.com/vkfolio/orio-search · https://www.oriosearch.org/ · https://api.github.com/repos/vkfolio/orio-search · https://api.github.com/repos/vkfolio/orio-search/license · https://github.com/majid-rafei/orio-search
- https://github.com/drmikecrypto/WebSearchFree · https://github.com/drmikecrypto/WebSearchFree/blob/main/README.md · https://api.github.com/repos/drmikecrypto/WebSearchFree
- https://github.com/divyanshu-iitian/SearchForge · https://github.com/divyanshu-iitian/SearchForge/blob/main/README.md · https://github.com/divyanshu-iitian/SearchForge/releases/tag/v0.2.0 · https://api.github.com/repos/divyanshu-iitian/SearchForge
- https://github.com/vakovalskii/searcharvester · https://github.com/vakovalskii/searcharvester/blob/main/docs/en/api.md · https://api.github.com/repos/vakovalskii/searcharvester
- https://github.com/karust/openserp · https://github.com/karust/openserp/blob/main/docs/openapi.yaml · https://openserp.org/ · https://api.github.com/repos/karust/openserp

**Expansion candidates**
- https://github.com/benbusby/whoogle-search · https://github.com/benbusby/whoogle-search/releases
- https://git.lolcat.ca/lolcat/4get · https://git.lolcat.ca/lolcat/4get/src/branch/master/README.md · https://git.lolcat.ca/lolcat/4get/src/branch/master/license.txt · https://git.lolcat.ca/lolcat/4get/src/branch/master/api/v1/index.php · https://4get.ca/api.txt
- https://github.com/yacy/yacy_search_server · https://yacy.net/ · https://github.com/yacy/yacy_search_server/commit/554911a88f8c5084146a8a098965f18e67416525
- https://github.com/Ahwxorg/LibreY · https://librey.org/ · https://api.github.com/repos/Ahwxorg/LibreY

**Additional finds**
- https://github.com/adityaparab/trawl · https://api.github.com/repos/adityaparab/trawl
- https://github.com/jianjungki/tavily-open · https://api.github.com/repos/jianjungki/tavily-open
- https://github.com/brcrusoe72/agent-search · https://api.github.com/repos/brcrusoe72/agent-search
- https://github.com/theYahia/qsearch · https://api.github.com/repos/theYahia/qsearch
- https://github.com/D4rk4/yago · https://api.github.com/repos/D4rk4/yago · https://github.com/D4rk4/yago/releases/tag/v0.0.5 · https://community.searchlab.eu/t/hey-mom-i-rewrote-yacy-in-go/3411 · https://www.reddit.com/r/vibecoding/comments/1ux1fuc/i_wanted_a_free_selfhosted_tavily_so_i_wrote_a/
- https://github.com/luculli/searxng-docker-tavily-adapter · https://api.github.com/repos/luculli/searxng-docker-tavily-adapter