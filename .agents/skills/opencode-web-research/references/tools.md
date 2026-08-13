# Web Research Tools — Parameter Reference

One-level reference loaded on demand from `../SKILL.md`. Names are the exact, fully-qualified tool names opencode registers.

## Table of contents

- [Discovery — searxng_searxng_web_search](#discovery--searxng_searxng_web_search)
- [Suggestions — searxng_searxng_search_suggestions](#suggestions--searxng_searxng_search_suggestions)
- [Instance info — searxng_searxng_instance_info](#instance-info--searxng_searxng_instance_info)
- [Page read — searxng_web_url_read](#page-read--searxng_web_url_read)
- [Built-in search — websearch](#built-in-search--websearch)
- [Plugin search — web_search](#plugin-search--web_search)
- [Built-in fetch — webfetch](#built-in-fetch--webfetch)
- [Library docs — context7](#library-docs--context7)
- [Self-hosted docs — docs-mcp-server](#self-hosted-docs--docs-mcp-server)

---

## Discovery — `searxng_searxng_web_search`

Primary web search. Self-hosted SearXNG. **Note the double `searxng_searxng_` prefix — it is correct.**

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `query` | yes | — | The search string |
| `pageno` | no | `1` | Page number, min 1 |
| `time_range` | no | — | `day` / `week` / `month` / `year`; only when freshness matters |
| `language` | no | instance default | Language code (`en`, `fr`, …) or `all` |
| `safesearch` | no | instance default | `0` none / `1` moderate / `2` strict |
| `min_score` | no | — | `0.0`–`1.0`; filter out results below this relevance |
| `num_results` | no | instance | `1`–`20`; capped by `SEARXNG_MAX_RESULTS` |
| `categories` | no | — | Comma-separated SearXNG categories; confirm with `instance_info` first |
| `engines` | no | — | Comma-separated engine names; confirm with `instance_info` |
| `response_format` | no | `text` | `text` (agent-formatted) or `json` (raw) |
| `result_detail` | no | `full` | `full` keeps metadata; `compact` returns title/url/content only |

**Gotchas**
- If the SearXNG VPS is down, calls error or hang — fall back to `websearch`, then `web_search`.
- `engines` / `categories` are best-effort; unknown values are ignored. Confirm support via `searxng_searxng_instance_info` before relying on a specific engine.

## Suggestions — `searxng_searxng_search_suggestions`

Autocomplete for vague/partial queries.

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `query` | yes | — | Partial or complete query |
| `language` | no | `all` | Language code |

## Instance info — `searxng_searxng_instance_info`

Discover what the reachable SearXNG instance supports. Use when choosing `categories`/`engines` or deciding which instance to lean on.

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `category` | no | — | Filter to one category |
| `includeEngines` | no | `false` | Include enabled engine names (and disabled if `includeDisabled`) |
| `includeDisabled` | no | `false` | Include disabled engines too |
| `refresh` | no | `false` | Bypass process cache, fetch fresh `/config` |

## Page read — `searxng_web_url_read`

Read a specific URL as markdown. Content-type aware (HTML→md, JSON pretty-printed, PDF text extraction ≤500 pp, no OCR). SSRF-protected. **Single `searxng_` prefix — correct.**

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `url` | yes | — | URL to read |
| `startChar` | no | `0` | Start position (min 0); paginate large pages |
| `maxLength` | no | — | Max chars to return (min 1) |
| `section` | no | — | Extract content under a heading (heading text match) |
| `paragraphRange` | no | — | e.g. `1-5`, `3`, `10-` |
| `readHeadings` | no | — | Return only a list of headings (mutually exclusive with the filters above) |

**Gotchas**
- `section` / `paragraphRange` / `readHeadings` are mutually exclusive with each other and with full content. Use them to bound context on big pages.
- If a page is unavailable, binary, or incomplete, choose another source — don't infer from a partial snippet that it proves an unread claim.

## Built-in search — `websearch`

opencode built-in. Exa provider (hosted). Gated by `OPENCODE_ENABLE_EXA=1` (set in this environment).

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `query` | yes | — | Web search query |
| `numResults` | no | `8` | How many results to return |
| `livecrawl` | no | `fallback` | `fallback` (live crawl only if cached unavailable) or `preferred` (prioritize live crawl) |
| `type` | no | `auto` | `auto` (balanced) / `fast` (quick) / `deep` (comprehensive) |
| `contextMaxCharacters` | no | `10000` | Max chars of context per result for the LLM |

**Gotchas**
- Do not assume which provider backs this in any given session — treat it as "hosted, possibly available". If it errors/returns nothing, fall back to `web_search`.
- Returns synthesized snippets; a snippet is still not a substitute for reading the source for a material claim.

## Plugin search — `web_search`

`opencode-metasearch2` plugin. Local Rust binary aggregating Google/Bing/Brave/marginalia. **Single name — but it is the plugin tool, not the built-in `websearch`.**

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `query` | yes | — | The search string |
| `type` | no | `all` | `all` (web) or `images` |

**Gotchas**
- Scrapes public search UIs → CAPTCHA / IP rate-limit risk under heavy or bursty use; transient, falls back across engines. Reserve for emergency fallback.
- Returns raw JSON: `search_results` (each with `engines` + `score`), `featured_snippet`, `answer`, `infobox`.

## Built-in fetch — `webfetch`

Simple URL → markdown. Simplest retrieval tool; use when `searxng_web_url_read`'s sectioning isn't needed.

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `url` | yes | — | URL to fetch |
| `format` | no | `markdown` | `markdown` / `text` / `html` |
| `timeout` | no | — | Seconds, max 120 |

**Gotchas**
- HTTP URLs auto-upgraded to HTTPS.
- Large pages may be summarized; for full content use `searxng_web_url_read` with pagination.

## Library docs — `context7`

Authoritative current library/framework/SDK documentation. **Prefer over generic web search for "how do I use X in Y".**

Resolve the library ID first, then query its docs.

`context7_resolve-library-id`

| Parameter | Required | Notes |
|-----------|----------|-------|
| `query` | yes | What to look up (scoped to one concept; be specific) |
| `libraryName` | yes | Official library name (`Next.js`, `Django`, `Prisma`) |

`context7_query-docs`

| Parameter | Required | Notes |
|-----------|----------|-------|
| `libraryId` | yes | From `context7_resolve-library-id` (or `/org/project` or `/org/project/version`) |
| `query` | yes | A single concept; split multi-concept questions into separate calls |

**Gotchas**
- Do not query more than 3 times per question.
- Good: "How to set up authentication with JWT in Express.js". Bad: "auth" (too vague).
- If a `query` spans multiple distinct concepts, make a separate call per concept rather than combining.

## Self-hosted docs — `docs-mcp-server`

Versioned, always-current docs index you scrape yourself. **Conditionally available — probe before relying on it.**

Probe first: `docs-mcp-server_list_libraries` (no params) shows what's indexed this session. If the library isn't listed or the call errors, the server is down/unconfigured — skip it.

`docs-mcp-server_find_version`

| Parameter | Required | Notes |
|-----------|----------|-------|
| `library` | yes | Library name |
| `targetVersion` | no | Exact or X-Range pattern |

`docs-mcp-server_search_docs`

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `library` | yes | — | Library name |
| `query` | yes | — | Documentation search query |
| `version` | no | — | Exact or X-Range (`5.x`, `5.2.x`); omit for latest |
| `limit` | no | `5` | Max results |

`docs-mcp-server_fetch_url`

| Parameter | Required | Notes |
|-----------|----------|-------|
| `url` | yes | URL to fetch and convert to markdown |

**Gotchas**
- Index state persists across sessions, but availability of the *server* does not — it's flaky. Always probe (`list_mcp_resources` or `list_libraries`) first.
- `scrape_docs` / `refresh_version` / `remove_docs` mutate the index — only on explicit user request.