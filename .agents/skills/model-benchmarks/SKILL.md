---
name: model-benchmarks
description: Fetches current AI model benchmark data and specs (Chatbot Arena ELO, Artificial Analysis composite indices, price, context window, modality, reasoning support) from keyless public sources and composes them into compact, sourced markdown tables on demand. Use when asked which model leads a leaderboard or Chatbot Arena, for a model's ELO, benchmark scores, price, context window, modality, or reasoning support, to compare two or three models side by side, or when any current model fact needs a source URL and timestamp. NOT for forecasting future releases, running benchmarks locally, evaluating local or private models, recommending providers, or scraping sources the skill does not cover.
---

# Model Benchmarks

Pull current benchmark data and model specs from two keyless public sources — the OpenRouter models list and the LMSYS Chatbot Arena leaderboard (via the HuggingFace datasets-server) — normalize them into one local JSON cache, and query that cache for a top-N leaderboard, one model's specs, or a side-by-side comparison. Every number the skill returns carries its source and age, so a figure is never presented as unattributed or current when it is not.

The skill needs no API keys and no third-party packages. It queries whatever models the live sources currently list — there is no static model roster to maintain.

## Workflow

1. Pick the query shape: `--top N` for a leaderboard, `--model NAME` for one model, `--compare A B [C...]` for two or three models.
2. Run the script (below). It refreshes the cache automatically when the cache is missing or older than 12 hours; pass `--force` when the user wants figures current as of right now; pass `--no-refresh` to work offline or against a fixture cache.
3. Compose the answer. Always relay the provenance header the script prints (sources + data age). If the data is stale and the refresh failed, say so to the user instead of presenting the number as current. Keep the answer compact: the script output is already the table.

## Script

One entry point: `scripts/model_benchmarks.py`. Run from the skill directory with `python`.

```
# refresh all sources, then print a short state summary (same as `fetch`)
python scripts/model_benchmarks.py

# top N models on the Chatbot Arena leaderboard
python scripts/model_benchmarks.py query --top 5

# one model's specs, by tolerant name
python scripts/model_benchmarks.py query --model "claude sonnet 5"

# side-by-side comparison of 2-3 models
python scripts/model_benchmarks.py query --compare gpt-5 claude-sonnet-5

# refresh regardless of cache age (user wants current-as-of-now)
python scripts/model_benchmarks.py query --top 5 --force

# use the cache as-is, never hit the network (offline / fixture tests)
python scripts/model_benchmarks.py query --top 5 --no-refresh

# point at a specific cache file (default: cache/cache.json)
python scripts/model_benchmarks.py query --top 5 --no-refresh --cache tests/fixtures/cache.json
```

- `fetch` (or no subcommand): fetch all sources, normalize, write `cache/cache.json`, print a state summary.
- `query` requires exactly one of `--top N`, `--model NAME`, `--compare A B [C...]`, plus optional `--no-refresh` / `--force` and the global `--cache PATH` option.
- Name matching is tolerant: case-insensitive, works on canonical names and all aliases, so "claude sonnet 5", "claude-sonnet-5", and "anthropic/claude-sonnet-5" resolve to the same record. If a name matches several records, the script prints a short disambiguation list and picks none — do not report one model's numbers when the query was ambiguous.
- Exit codes: 0 on success (including a disambiguation list); 1 with one clear error line when nothing matches, the cache is missing under `--no-refresh`, or every source failed with no usable cache.

## Dependencies

Python 3, standard library only (`urllib.request`, `json`, `argparse`, `pathlib`, `datetime`, `time`, `re`, `sys`, `os`). No API keys, no pip installs. Run with `python` on Windows; use `python3` on Unix. A full refresh makes one request to OpenRouter and paginates the Arena dataset in batches of 100 rows with politeness delays and retries, so it can take a few minutes — the cache makes repeat queries instant.

## Provenance and age contract

Every query output starts with a one-line provenance header, e.g.:

```
Data: openrouter.ai models list + lmarena-ai Chatbot Arena (fetched 3h ago); Arena publish date <snapshot date>
```

- The header names the sources, how old the fetched data is, and the Arena leaderboard publish date.
- If a source failed and its previous cache entry was reused, the header says so. Never quote a number without its provenance line.
- Before answering with cached data older than the staleness window (12h), either refresh (the script does this by default) or tell the user the figure is N hours old.

## Cache

Plain JSON at `cache/cache.json`, one record per canonical model name. It is safe to inspect or hand-edit in a pinch. Full field reference and normalization rules: `references/sources.md`.

## Reference docs

- `references/suites.md` — what each benchmark suite the skill knows about measures, its scale, judge type, contamination approach, authoritative URL, and whether the skill auto-fetches it.
- `references/sources.md` — the live source registry (endpoint, fields, cadence, attribution), the cache schema, and name-normalization rules.
