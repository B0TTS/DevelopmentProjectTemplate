# Review Report: model-benchmarks script + fixture

Reviewer: opencode (review role — no files edited)
Date: 2026-08-21
Contract: `b0ttsagent/planning/model-benchmarks-skill/SPEC.md` (Implementation Decisions, Testing Decisions, Verifiable success criteria)
Artifacts: `.agents/skills/model-benchmarks/scripts/model_benchmarks.py`, `.agents/skills/model-benchmarks/tests/fixtures/cache.json`

---

## A. Offline behavioral checks (fixture-driven, `--no-refresh`)

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| A1 | `query --top 3 --no-refresh --cache <fixture>` | **PASS** | Exit 0. Provenance header: `Data: openrouter.ai models list + lmarena-ai Chatbot Arena (fetched 30h ago); Arena publish date 2026-08-19`. 3-row table `Rank\|Model\|Creator\|ELO (95% CI)\|Votes`, rows 1/2/3 = claude-sonnet-5 / gpt-5 / gpt-5-mini sorted by rank. gemini-3-pro (null arena) excluded. |
| A2 | `--model "claude sonnet 5"` (tolerant alias) | **PASS** | Exit 0. Single spec block, canonical name `claude-sonnet-5`, 11 field rows (price $3/$15/$0.3, context 200,000, ELO 1438.8 (1420.2-1457.4), votes 45123, rank 1). |
| A3 | `--model gpt-5` (exact canonical beats substring) | **PASS** | Exit 0. Single gpt-5 block; no disambiguation list despite `gpt-5-mini` containing the substring. |
| A4 | `--model gpt` (ambiguous) | **PASS** | Exit 0. Disambiguation list: `gpt-5 - openai`, `gpt-5-mini - openai`; no pick. |
| A5 | `--model nonexistent-model-zz` | **PASS** | Exit 1, single stderr line `no model matches 'nonexistent-model-zz'`. |
| A6 | `--compare gpt-5 claude-sonnet-5` and 3-way with gemini-3-pro | **PASS** | Exit 0 both. 13-metric side-by-side tables; 3-way shows `-` for gemini-3-pro Arena ELO / ELO CI / votes. |
| A7 | `--top 3 --no-refresh` default cache path (confirmed absent) | **PASS** | `Test-Path` = False. Exit 1, single clear error: `no cache at <default path> and --no-refresh given`. |
| A8 | `--top 0` and `--compare gpt-5` | **PASS** | Both exit 2 with argparse-style single error: `--top must be a positive integer` / `--compare requires at least 2 model names`. |
| A9 | `--help` and `query --help` | **PASS** | Root help: fetch/query, `--cache` with default path. Query help: `--top`, `--model`, `--compare`, `--no-refresh`, `--force`. (`--cache` is SUPPRESSed on sub-help — see NIT-2.) |

All nine offline checks PASS.

## B. Static code checks

| Check | Result | Evidence |
|-------|--------|----------|
| Imports stdlib only | **PASS** | `argparse, datetime, json, pathlib, re, sys, urllib.error, urllib.request` (top), `time` (in `__main__` guard). All stdlib; no third-party. |
| Written cache schema matches SPEC | **PASS** | `merge()` emits exactly the schema keys: aliases/creator/context_window/modality/release_date/reasoning{supported,efforts,default}/price{input_per_m,output_per_m,cache_read_per_m}/indices{intelligence,coding,agentic}/arena{elo,elo_ci_lower,elo_ci_upper,votes,rank,category,publish_date}. Null defaults always present via `(o or {}).get(...) or {default}`. `sources` entries carry name/url/fetched_at/status (+`error` only when failed). Verified on live cache: 0 key/type mismatches in sampled records; `modality` is a string. |
| Name normalization | **PASS (1 edge flagged)** | Verified: `anthropic/claude-sonnet-5`→`claude-sonnet-5`; `Claude Sonnet 5`→`claude-sonnet-5`; `gpt-4o-2024-11-20`→`gpt-4o`; `openai/gpt-5:free`→`gpt-5`; series digits kept (`gpt-5`, `deepseek-r1-0528`). **FLAG:** `~anthropic/foo`→`anthropic-foo` — leading tilde prevents vendor-prefix strip (see MINOR-2). |
| Failure isolation | **PASS** | Per-source try/except (`fetch_openrouter`/`fetch_arena`); failed source → `status:"failed"` + `error`; prior-cache reuse via `openrouter_fields_from_cache`/`arena_fields_from_cache` (verified live: arena 429 on retry kept `fetched_at 05:41:01` and preserved data); exit non-zero with exactly one message only when all sources fail and no cache (`run_fetch` returns None before `write_cache` — no partial cache written). |
| Provenance header | **PASS** | Names both sources, age (`fetched 30h ago`), arena publish date (2026-08-19), failed/reused note `[chatbot arena fetch failed, reused cache]`. (Wording nit in MINOR-3.) |
| ASCII-safe output | **PASS** | 0 non-ASCII bytes in script; all observed outputs ASCII (no em-dashes/unicode). |
| No unhandled single-source-failure path; no raw dumps; numeric cells | **PASS** | Live arena failure twice: exit 0, no traceback. All outputs are formatted tables/lines; never raw cache. Table numbers parse as numbers. |
| Constants/dead code/comments | **PASS (2 nits)** | All constants commented/justified (TIMEOUT, FRESH_SECONDS, PAGE_SIZE, USER_AGENT); no dead code (all helpers referenced); only constant-justification comments. Nits: `1e-9` epsilon in `fmt_num` uncommented (NIT-3); `1_000_000` in `_price` justified by SPEC price-normalization decision. |

## C. Live check (network permitting)

**PARTIAL / NOT-FULLY-VERIFIED** — network is up on this box but the arena source fails through the script.

- Run 1 (bare): `openrouter: ok (405 models)`; `chatbot_arena: failed (The read operation timed out)`. Exit 0. Cache written: valid JSON, 405 models, schema-clean (verified).
- Direct probe: HF datasets-server IS reachable from this box — `num_rows_total: 10359` with a 90s timeout. The script's 30s per-request timeout + 104 sequential pages (100 rows × 103.6) without backoff is the likely cause of the timeout; subsequent retries hit `HTTP 429` (rate-limited by the pagination burst).
- Runs 2–3: `chatbot_arena: failed (HTTP 429)` both times; prior cache entry reused (correct degradation per SPEC).
- `query --top 5 --no-refresh` against live cache: exit 0, provenance header with the failed-source note, empty table (0 ranked rows — correct given no arena data).

The spec's success criterion (1) — both keyless sources `status: "ok"` — could NOT be demonstrated on this box. This is not fabricated data; it is the actual observed behavior, with the network caveat that OpenRouter worked and the arena endpoint answered only under a longer timeout. The script's failure handling worked exactly as designed; the fetch's own timeout budget is the robustness concern (see MAJOR-1).

## D. Fixture audit

**PASS.** `tests/fixtures/cache.json`:
- Schema matches SPEC exactly (all record keys, nesting, null defaults; `sources` entries with name/url/fetched_at/status; same 2-source shape the script actually writes).
- Deterministic: fixed `fetched_at`/source timestamps `2026-08-20T09:00:00+00:00`, plausible ELOs/votes/prices.
- Both sources `status: "ok"`.
- Substring-collision pair present: `gpt-5` + `gpt-5-mini` (aliases `openai/gpt-5`, `gpt 5`, `openai/gpt-5-mini`, `gpt-5 mini`).
- One null-arena model: `gemini-3-pro` (all arena values null, `category: ""`, `publish_date: null`) — matches merge() null defaults and correctly excluded from `--top`.
- Tolerant-alias resolution exercised: `claude sonnet 5` ∈ aliases of `claude-sonnet-5`.

---

## Findings

### MAJOR-1 — Arena fetch is not reliable enough on this network
- `model_benchmarks.py:14,166-176`
- The arena source is 10,359 rows = 104 sequential page requests, each with the 30s `TIMEOUT` and no retry/backoff. On this box the first fetch timed out (`The read operation timed out`) and every retry was rate-limited (`HTTP 429`) — a probe with a 90s timeout succeeded. Result: the arena source — one of only two keyless sources — fails reliably here, so `query --top N` on a fresh fetch yields an empty table.
- Fix: raise the arena timeout (e.g. 90s) and/or add per-page retry with backoff for the pagination loop, and treat HTTP 429 with a short sleep + retry. At minimum, document the arena fetch as heavy.

### MINOR-2 — Leading `~` breaks vendor-prefix canonicalization
- `model_benchmarks.py:45-54` vs `:106` (inconsistent: creator extraction does `oid.split("/",1)[0].lstrip("~")`, `canonical()` does not)
- `canonical("~anthropic/foo")` → `"anthropic-foo"` (prefix not stripped, tilde collapses to a separator). Live impact confirmed: 12 of 405 OpenRouter ids are `~`-prefixed (e.g. `~anthropic/claude-sonnet-latest`, `~deepseek/deepseek-v4-flash-latest`), producing canonical names like `anthropic-claude-sonnet-latest` instead of `claude-sonnet-latest`. No wrong answers today (resolvable via substring), but the SPEC's canonical-name contract ("vendor prefixes stripped") is violated and would produce spurious duplicates/disambiguation if a non-tilde variant of the same slug appears.
- Fix: `s = s.lstrip("~")` after lowercasing/stripping, before prefix matching.

### MINOR-3 — "reused cache" note can be misleading
- `model_benchmarks.py:331-343`
- The header note `[chatbot arena fetch failed, reused cache]` is emitted whenever a source is failed, even on a first fetch where there was no prior cache for that source (nothing was reused — the source simply contributes no records). Verified live on run 1.
- Fix: track whether reuse actually occurred (prior cache present for that source) and word the note accordingly (e.g. "no data for source X").

### NIT-1 — `artificial_analysis` source entry absent from written cache
- `model_benchmarks.py:266-302`; SPEC.md:67-69
- The SPEC schema sketch lists three `sources` entries including `artificial_analysis` with `status: "skipped_no_key|ok|failed"`. The script writes only the two keyless sources. Defensible (keyed path is additive-only per SPEC.md:51), but the written schema deviates from the sketch.
- Fix: either add a `skipped_no_key` entry when no key, or amend the SPEC schema to note the third entry is keyed-only.

### NIT-2 — `--cache` hidden from subcommand help
- `model_benchmarks.py:565-566`
- `--cache` is duplicated on subparsers with `help=argparse.SUPPRESS`, so `query --help` does not document it (it is functional). A fresh agent reading help won't discover the fixture-driven path.
- Fix: give the sub-level `--cache` real help text.

### NIT-3 — Uncommented magic epsilon
- `model_benchmarks.py:372` (`1e-9` in `fmt_num`)
- The SPEC demands "no voodoo numbers; no comments except constant justifications". The float-integrality epsilon is a magic number with no justification comment.
- Fix: extract to a named constant with a one-line justification.

---

## Verdict: **READY-WITH-FIXES**

All offline behavioral checks (A1–A9), the fixture audit (D), and the bulk of the static checks (B) pass. The script's failure isolation, schema conformance, ASCII safety, and CLI contract are all as specified. The live check (C) is PARTIAL: OpenRouter and cache-writing work, but the arena source fails through the script's own 30s/104-page fetch on this box (MAJOR-1) — the spec's "both sources ok" criterion could not be demonstrated. MAJOR-1 should be addressed (or its timeout budget explicitly justified) before calling the skill complete; MINORs are cheap follow-ups. No BLOCKERs.
