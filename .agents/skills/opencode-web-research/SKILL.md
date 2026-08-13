---
name: opencode-web-research
description: ONLY for opencode agents — pi and other harnesses have their own web-access skills (e.g. pi-web-search). Conducts web research in opencode using its web tools — searxng_searxng_web_search, built-in websearch (Exa), the web_search metasearch2 plugin, webfetch, context7, and docs-mcp-server — to discover sources, read pages, look up current library/API docs, and synthesize answers with citations. Use when a task needs current info, news, prices, events, recent framework/library docs, or content from specific URLs, or when you'd otherwise have to say info is past your knowledge cutoff. Routes SearXNG-first with fallback to websearch then the metasearch2 plugin. NOT for editing code, local filesystem-only work, submitting secrets/PII to the search instance, or treating a search snippet as a substitute for reading the source behind a material claim.
---

# Web Research (opencode)

Conduct web research in opencode: discover sources, read pages, look up current library/API docs, and synthesize with citations. Six web-research tools exist; pick by job, not by guess. Option tuning for each tool lives in `references/tools.md`.

## CRITICAL rules (read first)

1. **Three different "web search" tools exist — use the exact name.** Mixing them up is the #1 failure mode.
   - `searxng_searxng_web_search` — SearXNG MCP, self-hosted, structured. **Use first.**
   - `websearch` — opencode built-in (Exa provider). **Fallback.**
   - `web_search` — `opencode-metasearch2` plugin, local Google/Bing/Brave scraper. **Last resort.**

   The double `searxng_searxng_` prefix on the SearXNG search tool is correct, not a typo.
2. **SearXNG is self-hosted** on a Tailscale VPS — it can be down. Fall back; don't stop.
3. **A search snippet is discovery evidence, not a source.** For any material claim, read the page (`searxng_web_url_read` or `webfetch`) *before* citing it. Never infer the content of an unread page.
4. **Never submit secrets, API keys, or PII** to any search tool — queries and URLs reach the configured search instance / hosted provider.
5. **Context budget — snippet-first.** Run searches, read only the 1–3 most promising pages, and paginate long pages (`searxng_web_url_read` `maxLength` / `startChar`) instead of pulling thousands of chars into context.

## Tool inventory (by job)

### Discovery (URL unknown)

| Want | First tool | Fallbacks |
|------|-----------|----------|
| Search results (any topic) | `searxng_searxng_web_search` | → `websearch` → `web_search` |
| Autocomplete a vague query | `searxng_searxng_search_suggestions` | — |
| Confirm which engines/categories the instance exposes | `searxng_searxng_instance_info` | — |

**SearXNG-first routing** (fall back on error, empty results, or unreachable instance):

1. `searxng_searxng_web_search` — richest (pagination, `time_range`, `categories`, `engines`, structured results). If it errors or returns nothing, fall back.
2. `websearch` (`type` `auto`/`fast`/`deep`; `livecrawl` `fallback`/`preferred`; `numResults`; `contextMaxCharacters`) — built-in, Exa-backed. Gated by `OPENCODE_ENABLE_EXA=1`.
3. `web_search` (`type` `all`/`images`) — metasearch2 plugin, scrapes public search UIs. CAPTCHA / IP-rate-limit risk under heavy use; emergency fallback only.

### Retrieval (URL known)

| Page type | Tool | Why |
|-----------|------|-----|
| Long article / docs | `searxng_web_url_read` with `section` / `paragraphRange` / `readHeadings` | Selective extraction, content-type aware |
| PDF (text, no OCR) | `searxng_web_url_read` | Auto-extracts (≤500 pp) |
| Quick single page | `webfetch` (`format` `markdown`/`text`/`html`) | Simplest, HTTP→HTTPS upgrade |
| docs-mcp indexed page | `docs-mcp-server_fetch_url` | Only after `docs-mcp-server_list_libraries` confirms the lib is indexed |

### Library / API / framework docs (lib known, URL unknown)

| Need | Tool |
|------|------|
| Current docs for a library/framework | `context7_resolve-library-id` → `context7_query-docs` |
| Versioned self-hosted docs (only if indexed) | `docs-mcp-server_find_version` → `docs-mcp-server_search_docs` |
| What's indexed right now | `docs-mcp-server_list_libraries` |

`context7` is authoritative for current library docs — prefer it over a generic web search for "how do I use X in library Y". `docs-mcp-server` is **conditionally available** (offline some sessions) — always probe with `list_mcp_resources` or `docs-mcp-server_list_libraries` before relying on it.

## Workflow

Decide the breadth yourself from the stakes — a debugging question needs one good source; a comparative decision needs several. There are **no fixed query-count tiers**; spend effort proportional to how much is genuinely unknown.

1. **Classify the request.** Discovery (find sources), retrieval (read specific URLs), docs lookup (specific library/API), or full research (some of each).
2. **Vague query?** Run `searxng_searxng_search_suggestions` once to sharpen keywords, then proceed.
3. **Discover sources** if the URL is unknown. Use the SearXNG-first routing above. Vary keywords/angles across queries; add an exact product/error/quoted phrase; set `language`/`time_range`/`categories` only when they matter (confirm category support with `searxng_searxng_instance_info` first). Don't pass `engines`/`categories` the instance doesn't expose.
4. **Refine one constraint at a time** if results are weak: drop words → drop `time_range` → broaden `language` → drop `categories` → split the question. Retries alone don't help.
5. **Read the sources behind material claims** — snippets aren't enough. `searxng_web_url_read` (section/heading/range extraction) for long pages, `webfetch` for quick reads. Paginate long pages (`maxLength`, `startChar`) to bound context.
6. **Library/API question?** Prefer `context7_resolve-library-id` + `context7_query-docs` over generic search. Use `docs-mcp-server_*` only after `docs-mcp-server_list_libraries` confirms the lib is indexed.
7. **Synthesize with citations.** Cite canonical URLs next to the claims they support. Distinguish evidence (read + supports) vs inference vs unknown. Never invent a citation, quote, or date. If sources conflict, report the disagreement (freshness/scope/method) — don't silently pick the convenient one.
8. **Stop when the question is answered**, not when a coverage target is met. If a claim couldn't be verified after reasonable effort, say so explicitly rather than asserting it.

## Checklist (copy into your reply, tick each)

- [ ] Used exact tool names (`searxng_searxng_web_search`, not `searxng_web_search` or `websearch`)
- [ ] SearXNG first; fell back only on failure
- [ ] Read every page cited for a material claim (not just snippets)
- [ ] No secrets/PII submitted to any search tool
- [ ] Citations on claims; source conflicts surfaced, not hidden
- [ ] Said "unknown" where evidence was missing instead of guessing
- [ ] Context bounded (didn't pull tens of thousands of chars of one page into context)

## Per-tool parameter reference

See `references/tools.md` for each tool's full parameter list, defaults, and gotchas.