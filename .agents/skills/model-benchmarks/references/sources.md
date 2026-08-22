# Sources Reference

The live source registry for the skill: each source's endpoint, keyless vs keyed, fields returned, update cadence, and attribution. This is the fetch script's source configuration in human-readable form, plus the cache schema and name-normalization rules.

## Contents

- OpenRouter models list
- Chatbot Arena via HuggingFace datasets-server
- Artificial Analysis API (documented, not called)
- Cache schema
- Name normalization and matching
- Failure semantics

## OpenRouter models list

- **Endpoint:** `https://openrouter.ai/api/v1/models`
- **Keyless:** yes. No API key, no auth header beyond a User-Agent.
- **Fields used:** `id`, `name`, `context_length`, `architecture.modality`, `created` (unix), `pricing.prompt` / `pricing.completion` / `pricing.input_cache_read` (per-token strings; `input_cache_read` may be absent), `reasoning.supported_efforts` / `reasoning.default_effort`, `benchmarks.artificial_analysis.intelligence_index` / `coding_index` / `agentic_index` (numbers or null).
- **Cadence:** reflects whatever models OpenRouter currently lists — roughly 400 records, updated as models ship. Per-model `created` timestamps give release dates.
- **Attribution:** OpenRouter's public models endpoint; the provenance header in every query output cites `openrouter.ai models list` at the point of use.

## Chatbot Arena via HuggingFace datasets-server

- **Endpoint:** `https://datasets-server.huggingface.co/rows?dataset=lmarena-ai%2Fleaderboard-dataset&config=text_style_control&split=latest&offset=<OFFSET>&length=100` — paginated, 100 rows per request, up to `num_rows_total`.
- **Keyless:** yes. The script filters rows client-side to `category == "overall"`.
- **Fields returned:** `model_name`, `organization`, `license`, `rating` (ELO), `rating_lower` / `rating_upper` (95% CI), `variance`, `vote_count`, `rank`, `category`, `leaderboard_publish_date`. The script reads all of these except `license` and `variance`.
- **Cadence:** LMSYS publishes leaderboard snapshots on a rolling basis; each snapshot carries a `leaderboard_publish_date`, which the skill surfaces in every query header.
- **Attribution:** data is the `lmarena-ai/leaderboard-dataset` on HuggingFace (LMSYS); the provenance header cites `lmarena-ai Chatbot Arena` at the point of use.

## Artificial Analysis API (documented, not called)

- **Endpoint:** the Artificial Analysis API (https://artificialanalysis.ai).
- **Keyless:** no — requires an API key. This skill v1 does not call it: per-benchmark academic scores (GPQA, HLE, SciCode, MMLU-Pro, AIME, LiveCodeBench, τ²-Bench, Terminal-Bench) are unavailable in the keyless default. Say so plainly when a query needs them. The AA composite indices (intelligence, coding, agentic) are available keylessly via the OpenRouter models list instead.
- **Attribution:** per Artificial Analysis API terms when used on their site; this skill only surfaces their composite indices through OpenRouter's attribution-covered field.

## Cache schema

One JSON document at `cache/cache.json`:

```
{
  "fetched_at": "<ISO 8601>",
  "sources": [
    {"name": "openrouter", "url": "...", "fetched_at": "<ISO>", "status": "ok|failed", "error": "<if failed>"},
    {"name": "chatbot_arena", "url": "...", "fetched_at": "<ISO>", "status": "ok|failed", "error": "<if failed>"}
  ],
  "models": {
    "<canonical_name>": {
      "aliases": ["<lowercased variants from all sources>"],
      "creator": "<org>",
      "context_window": <int>,
      "modality": "<string>",
      "release_date": "<ISO date or null>",
      "reasoning": {"supported": <bool>, "efforts": [<str>], "default": "<str or null>"},
      "price": {"input_per_m": <float|null>, "output_per_m": <float|null>, "cache_read_per_m": <float|null>},
      "indices": {"intelligence": <float|null>, "coding": <float|null>, "agentic": <float|null>},
      "arena": {"elo": <float|null>, "elo_ci_lower": <float|null>, "elo_ci_upper": <float|null>,
                "votes": <int|null>, "rank": <int|null>, "category": "<str>", "publish_date": "<str>"}
    }
  }
}
```

Field notes:

- `price.*_per_m` — dollars per million tokens, converted from OpenRouter's per-token strings (×1,000,000, rounded to 3 decimals). Null when the source lacks a value.
- `indices.*` — the three Artificial Analysis composite indices, keyless via OpenRouter; null when not published for a model.
- `arena.*` — Chatbot Arena ELO, its 95% CI bounds, vote count, rank, and the leaderboard snapshot's publish date; all null for models absent from the arena.
- `aliases` — every name variant the sources used for this model (OpenRouter id and display name, Arena `model_name`), lowercased.

## Name normalization and matching

- **Canonical name:** lowercased; vendor prefixes stripped (`anthropic/`, `openai/`, `google/`, `meta-llama/`, `mistralai/`, `deepseek/`, `x-ai/`, `qwen/`, `cohere/`, `nvidia/`, `moonshotai/`, `ai21/`, `amazon/`); trailing date groups (`20260219`, `2026-02-19`) and a trailing `:free` suffix stripped; remaining non-alphanumeric runs collapse to a single `-`. Model-series digits are kept (`claude-sonnet-5` stays `claude-sonnet-5`).
- **Matching:** exact canonical match wins; otherwise case-insensitive substring match over canonical names and all aliases. Multiple matches produce a disambiguation list (canonical name + creator), never a silent pick. No fuzzy scoring beyond this — deterministic and debuggable.

## Failure semantics

- Each source fetch is independent. A failing source records `status: "failed"` plus an `error` message and reuses that source's records from the prior cache, so a transient outage never wipes known-good data.
- The query header notes any source in a failed/reused state.
- The script exits non-zero with one clear message only when every source failed and no usable cache exists.
