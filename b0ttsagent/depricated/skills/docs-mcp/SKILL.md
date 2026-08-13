---
name: docs-mcp
description: Search and index up-to-date library documentation via Docs MCP (self-hosted Context7 alternative). Use when user asks a library-specific question, needs API reference with exact signatures, wants version-pinned docs, or says "check the docs", "look up the API", "what's the latest on X", "how do I use Y". Prefer over web_search when the library is (or can be) indexed — this gives structured, version-aware results without ads or SEO spam. Also use when the model suspects its training data may be stale.
---

# Docs MCP — Versioned Documentation Search

## Tool Inventory

| Tool | Purpose | Destructive |
|------|---------|-------------|
| `mcp_docs_list_libraries` | See all indexed libraries + versions | No |
| `mcp_docs_find_version` | Resolve best matching version | No |
| `mcp_docs_search_docs` | Semantic search within indexed docs | No |
| `mcp_docs_fetch_url` | Fetch single page as Markdown (no indexing) | No |
| `mcp_docs_scrape_docs` | Index a new library/version from URL | Yes (writes) |
| `mcp_docs_refresh_version` | Re-scrape, updating only changed pages | Yes |
| `mcp_docs_remove_docs` | Delete a library/version from index | Yes |
| `mcp_docs_list_jobs` | List scraping jobs (filter by status) | No |
| `mcp_docs_get_job_info` | Get job progress/detail | No |
| `mcp_docs_cancel_job` | Cancel a running/queued job | Yes |

## Core Workflow

### 1. Check what's indexed

Always start with `mcp_docs_list_libraries`. Currently only `prettier` is indexed — most queries will require scraping first.

### 2. Find the right version

Use `mcp_docs_find_version` to discover available versions. Supports X-Range patterns:
- `"18.x"` → highest 18.x.x
- `"18.2.x"` → highest 18.2.x
- `"18.2.0"` → exact match
- omit → latest available

### 3. Search or scrape

**If the library IS indexed**: use `mcp_docs_search_docs` with a specific query. Good queries name concrete APIs or concepts: `"hooks lifecycle"`, `"ReturnType example"`, `"form validation"`. Avoid broad queries like `"react"`.

**If the library is NOT indexed**: ask the user if they want to scrape it, then use `mcp_docs_scrape_docs`:
```
library: "react"
version: "18.2.0"      // or "18.x" for latest 18.x
url: "https://react.dev/reference/react"
maxPages: 500
maxDepth: 3
scope: "subpages"       // or "hostname" for whole site
```

Scraping is async — returns a `jobId`. Use `mcp_docs_get_job_info` to monitor progress. Once COMPLETED, search results are available.

### 4. Fetch single pages (no indexing)

Use `mcp_docs_fetch_url` for one-off lookups — converts any URL to Markdown without storing it. Good for: testing URLs before scraping, reading private docs (with `headers`), converting local files (`file://`).

## Version Targeting Strategy

| User says | Use version |
|-----------|-------------|
| "how do I use React hooks" | omit (latest) |
| "React 18 hooks" | `"18.x"` |
| "React 18.2 hooks" | `"18.2.x"` |
| "useState in React 18.2.0" | `"18.2.0"` |

## When NOT to use Docs MCP

- **General web research** → use `web_search`
- **Code examples / Stack Overflow** → use `code_search`
- **Library is obscure / no docs site** → `web_search` or `code_search`
- **Conceptual questions** ("what is a monad") → `web_search`
- **Comparing libraries** → `web_search` (multiple angles via `queries`)

## Anti-Patterns

- Searching before checking if library is indexed
- Using version `"latest"` string — omit the version parameter instead
- Waiting synchronously for scraping — use `get_job_info` to poll
- Scraping huge sites at `maxDepth: 10` — start shallow, add depth if needed
- Using `search_docs` for queries better suited to `code_search` (how-to patterns with code snippets)

## Job Management

Scraping jobs flow: `queued → running → completed` (or `failed`/`cancelled`).

After starting a scrape with `waitForCompletion: false` (default for MCP), check progress:
1. `mcp_docs_list_jobs` (optionally filter `status: "running"`)
2. `mcp_docs_get_job_info` with the `jobId`
3. If stuck or too slow, `mcp_docs_cancel_job`

Failed jobs leave the version in `FAILED` state. Re-scrape by calling `scrape_docs` again with `clean: true`.
