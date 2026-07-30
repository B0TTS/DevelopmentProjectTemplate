# Docs MCP Skill — Design (In Progress)

Handing off a **grilling session** to design a `docs-mcp` skill (self-hosted Context7 alternative — the `mcp_docs_*` tool family). The v1 skill already drafted and **rejected by user**; we are mid-grill redesigning the operating model before rewriting it. Use the `grill-me` skill to continue interviewing the user one question at a time.

## What is Docs MCP

The `mcp_docs_*` tools are a self-hosted, version-aware documentation index. Two-phase model:

1. **Scrape** a library's docs site (async job, writes to local DB, returns `jobId`).
2. **Search** the index with semantic BM25 search, version-pinned.

Currently only `prettier` is indexed. Official docs: https://mintlify.wiki/arabold/docs-mcp-server (GitHub: arabold/docs-mcp-server).

### Tool inventory (all 10)

| Tool | Purpose | Destructive |
|------|---------|-------------|
| `mcp_docs_list_libraries` | See indexed libraries + versions | No |
| `mcp_docs_find_version` | Resolve best matching version (X-Range: `"18.x"`, `"18.2.x"`, exact, or omit for latest) | No |
| `mcp_docs_search_docs` | BM25 semantic search within indexed docs | No |
| `mcp_docs_fetch_url` | Fetch single page as Markdown (no indexing) | No |
| `mcp_docs_scrape_docs` | Index a new library/version from URL (async) | Yes |
| `mcp_docs_refresh_version` | Re-scrape, updating only changed pages | Yes |
| `mcp_docs_remove_docs` | Delete a library/version from index | Yes |
| `mcp_docs_list_jobs` | List scraping jobs (filter by status) | No |
| `mcp_docs_get_job_info` | Get job progress/detail | No |
| `mcp_docs_cancel_job` | Cancel a running/queued job | Yes |

Key mechanics the design depends on:
- `scrape_docs` is **async** — returns `jobId`, poll with `get_job_info`. Job lifecycle: `queued → running → completed` (or `failed`/`cancelled`).
- `scope` param (`subpages` | `hostname` | `domain`) is the **URL fence**, not depth. `maxDepth` is link-hops. Different knobs.
- `includePatterns` / `excludePatterns` accept regex wrapped in slashes: `/pattern/`.
- `search_docs` version arg: omit for latest, `"18.x"` for X-Range, `"18.2.0"` for exact.

## LOCKED decisions (do not re-litigate)

1. **Operating model: C — autonomous scraping with quality guardrails.** Model scrapes what it needs, no consent prompts. The entire skill is about *the guardrails*, not the happy path.

2. **Scrape gate: evidence-based.** Model must find the library as a real project dependency (in `package.json`/`go.mod`/`Cargo.toml`/`requirements.txt`/`pyproject.toml`/`pom.xml`/`build.gradle`/source imports) before scraping. No evidence → fall back to `fetch_url` / `web_search` / `code_search`, do NOT pollute the index.

3. **Pre-scrape prerequisites (hard gates):**
   - `mcp_docs_list_libraries` — confirm the library/version isn't already indexed (also `mcp_docs_find_version` to catch close-enough existing versions, e.g. don't scrape `18.2.0` if `18.2.1` is present).
   - `mcp_docs_list_jobs` filtered `status: "running"` + `"queued"` — confirm no active scrape for that library. No duplicate jobs.

4. **Scope strategy: C — filtered hostname.** `scope: "hostname"` from the library's docs **root** URL, with `includePatterns` targeting actual docs paths (`/reference`, `/learn`, `/guide`, `/api`) and `excludePatterns` for non-docs noise (`/blog`, `/showcase`, `/community`, version-switcher query strings). One job → one version → cheap `refresh_version` later.
   - Model decides whether to do pre-scrape recon (`fetch_url` the root to map the site's URL structure). Known site → scrape directly with known patterns. Unknown site → recon first, then scrape with discovered patterns.

## IN-PROGRESS (resume here)

### Question 3 coupled sub-decisions — proposed defaults, NOT yet confirmed
- **Root URL:** the library's docs root (e.g. `https://react.dev/`, `https://nextjs.org/docs`), not a deep reference page.
- **`maxPages`:** 2000 (above 1000 default so big libs don't silently truncate; include filter keeps it from being 2000 pages of junk).
- **`maxDepth`:** 5–8 (cheap once scope is fenced).
- **`scrapeMode`:** `"auto"` (Playwright for JS-rendered docs, fast `fetch` for static).
→ **Action: confirm these or challenge them.**

### Question 4 — which version to scrape (OPEN)
Given a manifest range like `"react": "^18.2.0"` (a range, not a version), three options were proposed:
- **A** (recommended) — scrape the **lockfile's exact resolved version** (`package-lock.json` says `18.2.4` → index `18.2.4`). Most honest mirror of what's installed; patch doc-drift is theoretical.
- **B** — scrape the range floor (`^18.2.0` → `18.2.0`), the minimum the range accepts.
- **C** — scrape the latest version satisfying the range (look up current releases, pick newest in range).

User just asked "what even is a lockfile" — concept was explained (manifest = range/contract; lockfile = exact installed version, pins transitive deps too). User has **not yet** picked A/B/C. Resume by re-asking which option, now that the lockfile concept is clear.

**Coupled sub-decision (proposed, NOT confirmed):** at *search time*, pass the lockfile version as the `version` arg to `search_docs` instead of an X-Range, to avoid ambiguity if a second same-major version ever lands in the index.

### Question 5 — lockfile reading efficiency (OPEN, depends on Q4 answer)
User's refinement (locked): the model re-derives the version from the lockfile at **every `search_docs` call** and at **every scrape**, not carried across session memory. Rationale: lockfiles change mid-session (bumps, branch switches, model edits); multiple projects may be indexed with different versions of the same lib.

Problem: lockfiles can be 5k–50k lines. Reading the whole file per search burns tens of thousands of tokens. Proposed solution **B** (recommended): bundle a `scripts/get-version.sh` with deterministic `jq`/`grep`/`yq` extraction per lockfile format, near-zero tokens per call. Need to know **which ecosystems the user actually works in** to scope the script:
- Evident: Node (`package.json`).
- Unknown: Python, Rust, Go, Java/Kotlin, .NET, Ruby, PHP, Elixir, Swift?
→ **Action: ask which ecosystems to support; confirm bundled-script approach.**

## Explicitly OUT OF SCOPE for next session
- The old v1 SKILL.md (`C:\Users\Jonah\.pi\agent\skills\docs-mcp\SKILL.md`) is **rejected**. Do not patch it — rewrite from scratch once Q3–Q5 resolve.

## Suggested skills for next session
- `grill-me` — continue one-question-at-a-time interviewing to resolve Q3 sub-decisions, Q4, Q5.
- `write-a-skill` — once decisions are locked, rewrite SKILL.md (under 100 lines) and optionally bundle `scripts/get-version.sh`. Skill dir: `C:\Users\Jonah\.pi\agent\skills\docs-mcp\`.

## Key paths
- Skill directory (to be rewritten): `C:\Users\Jonah\.pi\agent\skills\docs-mcp\SKILL.md`
- Docs MCP official docs: https://mintlify.wiki/arabold/docs-mcp-server
- Source repo: https://github.com/arabold/docs-mcp-server
