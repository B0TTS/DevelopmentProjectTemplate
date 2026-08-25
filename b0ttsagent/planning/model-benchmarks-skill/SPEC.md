# Spec: `model-benchmarks` skill

## Problem Statement

As a coding agent, I am constantly asked questions that depend on current AI-model facts — "which model leads on Chatbot Arena?", "how do claude-sonnet-5 and gpt-5 compare on price and context window?", "what's the ELO of model X?". My training-time knowledge of model rankings, benchmark scores, prices, and context windows is stale the moment it is written, because new models and benchmark versions ship continuously. When I answer from memory I guess, and when I ad-hoc browse the web I burn tokens scrolling JS-rendered leaderboard sites and still often fail to land on a machine-readable number. There is no fast, trustworthy, zero-config way for me to pull a current, comparable number and drop it into my answer.

## Solution

A coding-agent skill, `model-benchmarks`, that fetches current benchmark data and model specs from public, keyless, machine-readable sources and composes them into compact, composable markdown tables on demand. The agent runs one deterministic script to refresh a local normalized cache, then queries that cache for a top-N leaderboard, a single model's specs, or a side-by-side comparison. Everything the skill returns states where it came from and how old it is, so the agent never presents a stale or unattributed number as current. No API keys, no third-party packages, no curated model roster — the skill pulls whatever models the live sources currently list.

## User Stories

1. As a coding agent, I want to ask "which model leads the Chatbot Arena text leaderboard?" and get the top-ranked model name, its ELO, vote count, and how old the data is, so that I can answer the user without guessing from memory.
2. As a coding agent, I want to ask for the top-N models on a given leaderboard and get a compact ranked table, so that I can show the user the current frontier without dumping raw data.
3. As a coding agent, I want to look up a single model's specs — price per million tokens, context window, modality, reasoning support, release date — by name, so that I can cite concrete numbers in a recommendation.
4. As a coding agent, I want to compare two or three models side by side on price, context window, and composite quality indices, so that I can help the user pick between specific candidates.
5. As a coding agent, I want the skill to work with zero configuration — no API keys, no pip installs beyond the Python standard library — so that it works in any fresh environment.
6. As a coding agent, I want every returned number to carry its source URL and a fetch timestamp, so that I never present an unattributed or undated fact as current.
7. As a coding agent, I want cached data to report how old it is, so that I can decide whether to refresh before answering or warn the user that the figure is N hours old.
8. As a coding agent, I want the skill to refresh its cache automatically when the data is stale, so that I do not have to remember a separate "update" step before every query.
9. As a coding agent, I want to force a refresh on demand, so that I can pull the latest numbers when the user explicitly wants "current as of right now".
10. As a coding agent, I want a query for a model name that doesn't match exactly to still find the right model via tolerant name matching, so that "claude sonnet 5", "claude-sonnet-5", and "anthropic/claude-sonnet-5" all resolve to the same record.
11. As a coding agent, when a model name is ambiguous (matches several models), I want the skill to return a short disambiguation list rather than silently picking one, so that I do not report the wrong model's numbers.
12. As a coding agent, I want prices normalized to dollars per million tokens regardless of how the source reports them, so that comparisons across models and sources are directly comparable.
13. As a coding agent, I want Chatbot Arena ELO returned with its 95% confidence interval and vote count, so that I do not overstate the precision of a close ranking.
14. As a coding agent, I want the Artificial Analysis composite indices (intelligence, coding, agentic) for a model when available, so that I can give a one-line quality summary without needing per-benchmark detail.
15. As a coding agent, I want a clear answer to "what does GPQA measure and where do current GPQA scores live?", so that I can explain a suite and point the user at the authoritative source even when the skill does not auto-fetch that suite's scores.
16. As a coding agent, I want the skill to tell me plainly when a requested suite (e.g. GPQA Diamond, MMLU-Pro, AIME) requires the optional Artificial Analysis API key and is therefore unavailable in the default keyless setup, so that I do not fabricate a score or silently omit it.
17. As a coding agent, I want the skill to gracefully use the Artificial Analysis API when an API key is present in the environment, so that users who have a key get enriched per-benchmark academic scores without a different command.
18. As a coding agent, I want a failed network fetch to produce a clear, single error message naming the source that failed, so that I can relay the failure to the user instead of emitting a partial or garbled table.
19. As a coding agent, I want the cache stored as plain JSON I can inspect, so that I can sanity-check a number or hand-edit a record in a pinch.
20. As a coding agent, I want the query output to be a few lines or a small markdown table — never a raw multi-megabyte dump — so that the answer stays compact and composable into my reply.
21. As a coding agent, I want the skill to declare its Python-standard-library-only dependency upfront, so that I do not attempt to run it in an environment missing `urllib`/`json`.
22. As a coding agent, I want the skill to expose a single subcommand that refreshes and prints a short summary, so that a "just update and tell me the state" one-liner exists.
23. As a coding agent, I want the skill's reference docs to explain each benchmark suite's scale, cadence, judge type, and contamination approach, so that I can contextualize a number rather than reporting it naked.
24. As a coding agent, I want the skill's reference docs to list every live source, whether it is keyless or keyed, what fields it returns, and its update cadence, so that I can reason about freshness and coverage without re-reading the script.
25. As a user talking to a coding agent, I want the agent to be able to give me a current, sourced model comparison in one turn, so that I do not have to go hunt down a leaderboard myself.
26. As a user, I want the agent to tell me when its benchmark data is stale and offer to refresh, so that I am not misled by an old cache during a fast-moving model release week.
27. As a skill author, I want the skill to pass three fresh-agent evaluations end to end, so that I have evidence it loads and works for someone who has never seen it before.
28. As a skill author, I want the skill to follow the write-a-skill-v2 constraints — SKILL.md under 500 lines, one job, forward-slash paths, no time-sensitive facts in the body — so that it loads optimally and does not rot.
29. As a skill author, I want the query/formatting logic to be testable offline against a committed fixture cache, so that the composition behavior is deterministic and verifiable without hitting the network.
30. As a skill author, I want the fetch logic to degrade safely when a source is temporarily unreachable, so that one source being down does not wipe the whole cache or crash the agent.

## Implementation Decisions

- **Skill identity.** A new skill directory `model-benchmarks/` under the project's trusted skills folder, containing `SKILL.md`, a `scripts/` directory with one fetch/query script, a `references/` directory with two reference docs, and a runtime-writable `cache/` directory. Name is gerund-free per the existing project convention (`pdf`, `log-session`) but matches the parent directory and uses only lowercase letters and hyphens. One job only: look up current benchmark data and model specs and compose compact comparisons.

- **Data sources (verified, keyless by default).**
  - *OpenRouter models list* — keyless, returns ~400 models with: identity (id, name, creator), `context_length`, modality, `pricing` (prompt/completion/input-cache-read as per-token string values), `top_provider` (context length, max completion tokens), `created` timestamp, `reasoning` (supported efforts, default effort), and a `benchmarks` object containing `artificial_analysis` composite indices and `design_arena` per-category ELO/win-rate/rank. This is the primary source for specs (price, context, modality, reasoning) and for AA composite indices.
  - *Chatbot Arena (LMSYS) leaderboard* — served keyless as JSON via the HuggingFace datasets-server rows endpoint against the `lmarena-ai/leaderboard-dataset` dataset, config `text_style_control`, split `latest`. Each row carries `model_name`, `organization`, `license`, `rating` (ELO), `rating_lower`/`rating_upper` (95% CI), `variance`, `vote_count`, `rank`, `category`, `leaderboard_publish_date`. The `latest` split is large (all categories × models), so the script paginates and filters client-side to `category == 'overall'` (and other standard categories on demand). This is the primary source for arena ELO and rank.
  - *Artificial Analysis API (optional enrichment)* — requires a free API key (env var). When the key is absent the skill runs in keyless mode and omits per-benchmark academic scores; when present the skill additionally pulls per-benchmark academic scores (GPQA, HLE, SciCode, MMLU-Pro, AIME, LiveCodeBench, τ²-Bench, Terminal-Bench), the Math/Openness/Multilingual composite indices, and throughput/latency percentiles. Keyless mode is the contract; the keyed path is purely additive.

- **No curated model roster.** Per an explicit product decision, the skill pulls on demand whatever models the live sources currently list. There is no static frontier shortlist to maintain. (A separate curated doc describing *suites* and *sources* remains, because those are slow-changing and not model rosters.)

- **Single script, subcommand CLI.** One Python script exposes: a `fetch` subcommand (the default when no subcommand is given) that pulls all configured sources, normalizes, and writes the cache; and a `query` subcommand with `--top N`, `--model <name>`, and `--compare A B [C...]` flags. A bare invocation with no subcommand refreshes and prints a short state summary. The script is pure Python standard library (`urllib.request`, `json`, `argparse`, `time`, `os`, `sys`, `re`) — no third-party packages, declared in SKILL.md.

- **Normalization to a single record shape.** Records from both keyless sources are normalized into one schema per model, keyed by a canonical name. The cache is a single JSON document:

  ```
  {
    "fetched_at": "<ISO 8601 local>",
    "sources": [
      {"name": "openrouter", "url": "https://openrouter.ai/api/v1/models",
       "fetched_at": "<ISO>", "status": "ok|failed", "error": "<if failed>"},
      {"name": "chatbot_arena", "url": "<HF datasets-server rows URL>",
       "fetched_at": "<ISO>", "status": "ok|failed", ...},
      {"name": "artificial_analysis", "url": "...", "fetched_at": "<ISO>",
       "status": "ok|skipped_no_key|failed", ...}
    ],
    "models": {
      "<canonical_name>": {
        "aliases": ["<all names this model is known by across sources>"],
        "creator": "<org>",
        "context_window": <int tokens>,
        "modality": "<string>",
        "release_date": "<ISO or null>",
        "reasoning": {"supported": <bool>, "efforts": [...], "default": "<str>"},
        "price": {"input_per_m": <float>, "output_per_m": <float>,
                  "cache_read_per_m": <float|null>},
        "indices": {"intelligence": <float|null>, "coding": <float|null>,
                    "agentic": <float|null>},
        "arena": {"elo": <float|null>, "elo_ci_lower": <float|null>,
                  "elo_ci_upper": <float|null>, "votes": <int|null>,
                  "rank": <int|null>, "category": "<str>", "publish_date": "<ISO>"}
      },
      ...
    }
  }
  ```

  Price normalization: OpenRouter gives per-token string prices; multiply by 1,000,000 to store dollars per million tokens. This schema is the decision-rich prototype artifact; field names are stable and the script and reference docs refer to them consistently.

- **Name normalization and matching.** A canonical name is derived by lowercasing, stripping vendor prefixes and date/version suffixes, and collapsing separators. Lookup is case-insensitive substring match against both canonical names and the `aliases` list (which holds every variant each source used, so an OpenRouter slug, an Arena `model_name`, and an AA name can all resolve to one record). When a query matches multiple records, the script returns a disambiguation list of the matching canonical names and their creators instead of picking one. There is no fuzzy scoring beyond substring + alias membership — simple, deterministic, debuggable.

- **Cache freshness.** The cache records `fetched_at`. A query auto-refreshes when the cache is older than a staleness threshold (default 12 hours) or missing; `--force` refreshes regardless; `--no-refresh` forces use of the existing cache (useful offline / in tests). Every query output includes a line naming each source used and the age of its data ("data fetched 3h ago from openrouter.ai + lmarena HF dataset; Arena publish date 2026-08-19").

- **Source attribution and failure handling.** Each source fetch is independent. If a keyless source fails (network error, non-200, JSON parse error), the script records `status: "failed"` with the error message for that source, preserves the other sources' fresh data, and reuses the prior cache entry for the failed source if one exists (so a transient outage does not wipe known-good data). The query output notes any source currently in a failed/reused state. The script never raises an unhandled exception for a single-source failure; it only exits non-zero with a single clear message if *all* configured sources fail and no usable cache exists.

- **Output shape (compact, composable).** Query output is a short markdown table or a few lines — never the raw cache. `--top N` prints a ranked table with the rank, model, creator, score/ELO, and votes/CI. `--model` prints a single compact spec block. `--compare` prints a side-by-side table across the dimensions available for those models. Each output is prefixed by a one-line provenance/age header.

- **Reference docs (two, one level deep).**
  - `references/suites.md` — for each suite the skill knows about (Chatbot Arena text/vision/agent, LiveBench, GPQA Diamond, MMLU / MMLU-Pro, AIME, HLE, SciCode, LiveCodeBench, HumanEval/MBPP, τ²-Bench, Terminal-Bench, SWE-bench Verified, Scale SEAL, Aider leaderboard, Artificial Analysis composite indices): what it measures, scale/cadence, judge type (human vote / LLM judge / exact match), contamination approach, the authoritative source URL, and whether the skill auto-fetches it (keyless), fetches it when keyed (AA), or surfaces it as an on-demand web source only (JS-rendered, no clean keyless JSON). No versioned scores in this doc.
  - `references/sources.md` — the live source registry: each source's endpoint, keyless vs keyed, fields returned, update cadence, attribution requirement, and the env var name for the optional key. This doubles as the fetch script's source configuration in human-readable form.

- **SKILL.md body discipline.** Under 500 lines. No time-sensitive facts in the body (no "current top model", no dated numbers, no "latest version") — all such facts come from the cache at query time. The body contains: the trigger-router description, the one-paragraph capability, the workflow (refresh-or-use-cache → query → compose), the script's CLI reference, the dependency declaration, the provenance/age contract, and pointers to the two reference docs. Consistent terminology throughout ("cache", "source", "suite", "record", "query").

- **Trigger surface (description).** Third person, "Use when…" phrasing matching how agents actually ask. Triggers: "which model leads on [Chatbot Arena / LiveBench / coding]", "compare [X] and [Y] on [GPQA / price / context]", "what's the ELO of [model]", "top models on [benchmark]", "model specs / price / context window for [model]". NOT-for boundary: forecasting future releases, running benchmarks yourself, evaluating a local/private model, recommending a specific provider for a specific app, or scraping an uncovered source from scratch (point to general web tools instead).

## Testing Decisions

- **What makes a good test here.** Test only external behavior — what the agent observes when it runs the script — not the script's internal helpers. The script's external behavior is its CLI output and the cache file it writes. A good test asserts on the shape and content of that output (a table with the right columns, a provenance header naming the source and age, numbers that parse as numbers) without coupling to the exact current values (which change daily).

- **The single primary seam: the script's CLI, exercised by a fresh agent.** Per the write-a-skill-v2 evaluation requirement, the real test is whether a fresh agent session — one that has never seen this skill — can load the skill and pull current benchmark data end to end. This is the highest seam and the one that matters: it covers discovery (description triggers), loading, running the script against live sources, and composing a compact answer. At least three such evaluations are run before the skill is considered done.

- **An offline, deterministic sub-seam for the composition logic.** Because live fetches are non-deterministic, the query/formatting and name-matching logic is also verified against a committed fixture cache (a small, hand-built JSON in the right schema, checked into the repo under a test/fixtures path) using `--no-refresh`. This lets the formatting, normalization, disambiguation, and provenance-header behavior be asserted exactly and repeatably without network. This is the same single CLI seam, just driven by a frozen cache instead of a live one — not a new seam.

- **Modules tested.** The fetch/query script as a whole (via its CLI), and the SKILL.md trigger/loading behavior (via the fresh-agent evaluations). The reference docs are not unit-tested; they are reviewed for the no-time-sensitive-facts and one-level-deep constraints.

- **Prior art.** The existing `pdf` skill in this repo established the layout (SKILL.md + scripts/ + references/) and the pattern of deterministic scripts invoked by the agent; this skill follows that convention. No application test framework exists in this repo (it is a markdown/agent-config repo), so tests are script invocations plus fresh-agent evaluations, not a unit-test suite.

## Out of Scope

- Forecasting future model releases, dates, or price changes.
- Running any benchmark or evaluation locally (the skill reads published results; it does not generate them).
- Evaluating a local, private, or fine-tuned model not listed by the public sources.
- Recommending a specific provider for a specific application — the skill reports comparable numbers; routing decisions are the agent's and user's.
- Scraping a source the skill does not cover (SWE-bench Verified, Scale SEAL, Aider, Open LLM Leaderboard are JS-rendered with no clean keyless JSON): the skill documents these in `references/suites.md` as on-demand web sources and points the user at the authoritative URL, but does not auto-fetch them.
- Caching historical time series or trend data — the cache holds the current snapshot only.
- A curated frontier model roster — per explicit product decision, the skill pulls on demand whatever the live sources list; there is no `models.md` to maintain.
- Image, video, speech, and music model benchmarks beyond what the keyless OpenRouter `benchmarks.design_arena` data and the optional AA media endpoints expose incidentally — full multimodal benchmark coverage is not a goal of v1.
- A unit-test framework or CI pipeline — this repo has none; verification is via script invocation and fresh-agent evaluations.

## Further Notes

- **Why keyless is the contract.** A skill that silently requires an API key fails in every fresh environment and erodes trust. OpenRouter's keyless models list and the HuggingFace datasets-server's keyless JSON rows make specs, AA composite indices, and Chatbot Arena ELO available with zero setup. The Artificial Analysis per-benchmark academic scores are genuinely valuable but genuinely gated, so they are structured as additive enrichment behind an env var rather than a baseline requirement. This keeps the default path working everywhere and lets users with a key opt into deeper data without a different command.

- **Why one script, not a library.** The agent runs commands, not imports. A single subcommand CLI keeps the SKILL.md instructions short (one tool to teach), makes the external behavior obvious, and matches the `pdf`-skill prior art in this repo. Internal helpers stay inside the one file; if it grows past comfortable size the split would be into `scripts/` modules, not a separate package.

- **Why a fixture cache for offline tests.** Live leaderboard data changes daily, so assertions against live values are flaky by construction. A committed fixture cache in the exact cache schema lets the composition, normalization, disambiguation, and provenance-header behavior be verified deterministically with `--no-refresh`, while the fresh-agent evaluations cover the live path. Same CLI seam, two modes.

- **Attribution.** OpenRouter data is used per its public models endpoint; Chatbot Arena data is the `lmarena-ai/leaderboard-dataset` on HuggingFace (LMSYS); Artificial Analysis data (when keyed) requires attribution per its API terms. The provenance header in every query output satisfies the attribution requirement at the point of use, and `references/sources.md` records each source's attribution expectation.

- **Verifiable success criteria for the build session.** (1) `fetch` writes a valid cache JSON with all configured keyless sources `status: "ok"` and a `fetched_at` timestamp; (2) `query --top 5` prints a 5-row ranked table with a provenance/age header; (3) `query --model <name>` resolves a tolerant name to one record and prints a compact spec block; (4) `query --compare A B` prints a side-by-side table; (5) `query --no-refresh` against the fixture cache reproduces the same output shape deterministically; (6) three fresh-agent evaluations pass end to end. Each criterion maps to a runnable check, not a vibe.
