# Test Report — `model-benchmarks` skill

Date: 2026-08-21 · Harness: opencode · Orchestrator + fresh subagent sessions (`b0tts-general-agent`) · Spec: `SPEC.md` (verifiable success criteria 1–6) + `FRESH-AGENT-EVALS.md`

## Summary

| Check | Result |
|---|---|
| Offline deterministic check (4 commands vs fixture) | PASS |
| Success criterion 1 — valid cache, keyless sources `status: ok` | PASS |
| Fresh-agent Eval 1 — arena top 5 (discovery + auto-refresh + provenance) | PASS |
| Fresh-agent Eval 2 — compare specs (tolerant names + composability) | PASS |
| Fresh-agent Eval 3 — keyed suite + out-of-scope boundary | PASS |

**Overall: all pass** after one follow-up bug found during a freshness contract probe — fixed and re-verified (see §6). No eval failures to feed back to the skill author.

## Method

- Deleted live `cache/cache.json` before the fresh-agent evals so the auto-refresh path was genuinely exercised.
- Three fresh `b0tts-general-agent` sessions (no prior context of the skill) each received one eval prompt verbatim, plus instructions to behave as a normal coding agent (skills mandated by AGENTS.md). No layout/script hints given.
- Evals ran in parallel; each agent independently loaded the skill and ran its script against live sources.

## 1. Offline deterministic check (fixture cache, no network)

Ran directly by the orchestrator with `--no-refresh --cache tests/fixtures/cache.json`:

| Command | Expected | Actual |
|---|---|---|
| `query --top 3` | ranked table + provenance header | ranked table (rank/model/creator/ELO 95% CI/votes), provenance header present |
| `query --model "claude sonnet 5"` | tolerant name resolves to one spec block | resolved to `claude-sonnet-5` spec block |
| `query --model gpt` | disambiguation list, exit 0 | 2-item disambiguation list (`gpt-5`, `gpt-5-mini`), exit 0, no silent pick |
| `query --compare gpt-5 claude-sonnet-5` | side-by-side table | 2-model table (price, context, reasoning, AA indices, arena) |

All outputs prefixed with the provenance line (`openrouter.ai models list + lmarena-ai Chatbot Arena (fetched 31h ago); Arena publish date 2026-08-19`). No network traffic.

## 2. Success criterion 1 — cache validity (live)

After the evals, the live cache written by the script was verified:

- `fetched_at: 2026-08-21T06:22:17-10:00` present
- Sources: `openrouter: ok`, `chatbot_arena: ok`
- 718 model records — no curated roster, reflects the live source lists

## 3. Fresh-agent Eval 1 — PASS

Prompt: *"Which model currently leads the Chatbot Arena leaderboard, and what's the top 5? Give me ELO with confidence intervals and vote counts, and tell me how fresh this data is."*

| Criterion | Verdict |
|---|---|
| Skill discovery fired (loaded `model-benchmarks`) | PASS |
| Ran script with live fetch, both keyless sources `status: ok` | PASS — `query --top 5 --force`, header showed "fetched 8m ago", cache verified ok/ok |
| Top-5 table: rank, model, ELO, 95% CI, votes, sorted by rank | PASS |
| Provenance line relayed (sources + fetch age + Arena publish date 2026-08-19) | PASS |
| No raw cache dump | PASS |

Notable: agent additionally flagged that #2 sits inside #1's CI — correct statistical reading of the fetched CI data.

## 4. Fresh-agent Eval 2 — PASS

Prompt: *"Compare claude sonnet 5 and gpt-5 on price per million tokens (input/output), context window, and reasoning support. Which one is cheaper on input? Use current data with sources."*

| Criterion | Verdict |
|---|---|
| Used skill's script (`--compare`) | PASS |
| Tolerant name resolution | PASS — `"claude sonnet 5"` matched `claude-sonnet-5` AND `claude-sonnet-5-batch`; script returned the disambiguation list, agent correctly picked none and reran with the canonical name — exactly the contract's no-silent-pick behavior |
| Price, context window, reasoning as comparable numbers for both | PASS — side-by-side table (in $2/$1.25, out $10/$10, cache read, 1M vs 400K context, reasoning efforts/defaults) |
| "Cheaper on input" derived from fetched data | PASS — GPT-5 at $1.25/M vs Claude Sonnet 5 at $2/M, stated as such |
| Provenance relayed; stale warning if needed | PASS — data fetched 5m ago, no stale warning needed |

## 5. Fresh-agent Eval 3 — PASS

Prompt: *"What's the latest GPQA Diamond score for gpt-5, and what does GPQA actually measure? Also: will Claude 6 release in the next month and beat everything?"*

| Criterion | Verdict |
|---|---|
| GPQA explanation matches `references/suites.md` (judge: exact match; scale: 198-question Diamond set; contamination: expert filtering) | PASS |
| States plainly per-benchmark GPQA scores are keyed (AA API), not auto-fetched by this skill; no fabrication, no silent omission | PASS — agent read the reference docs and said exactly this; reported the score (85.7% w/ reasoning) only via cited primary sources (OpenAI launch post, Epoch AI, Vellum, OpenRouter/AA leaderboards) |
| Points to authoritative sources (arxiv/AA) | PASS — arXiv:2311.12022, artificialanalysis.ai, openrouter.ai/benchmarks |
| Refuses to forecast release; does not present speculation as data | PASS — no definitive forecast; gave sourced prediction-market odds (~1% before Oct 2026), explicitly labeled "beats everything" as unverifiable marketing language |
| No fabricated numbers | PASS — every figure carries a source URL |

## Artifacts

- Commands run by eval agents: `python scripts/model_benchmarks.py query --top 5 --force`, `... --compare "claude sonnet 5" gpt-5 --force` (disambiguation) then `... --compare claude-sonnet-5 gpt-5 --force`, `... --model "gpt-5" --force` — all from the skill directory.
- Live cache regenerated at `.agents/skills/model-benchmarks/cache/cache.json` (valid, both sources ok).

## Notes / observations (non-blocking)

- Eval 2's ambiguity (claude-sonnet-5 vs claude-sonnet-5-batch) was handled correctly by both script and agent; it made the run longer but demonstrated the disambiguation path under real data.
- All three agents chose `--force` — acceptable and within the skill's guidance ("current as of right now").

## 6. Follow-up: freshness-contract bug found, fixed, re-verified

The fresh-agent evals all used `--force`, so the **default auto-refresh path** (no flags; refresh when cache missing/stale) was never exercised by them. A direct probe exposed a real bug:

**Bug.** `cache_is_fresh()` keyed the 12h staleness check on the cache **file's mtime**, not the recorded `fetched_at`. Consequences:

1. Hand-editing the cache (explicitly supported — SKILL.md: "safe to inspect or hand-edit in a pinch") resets mtime, so a 13h-old cache was treated as fresh: the query served stale data and never auto-refreshed.
2. `run_fetch`'s partial-failure path stamped the file-level `fetched_at = now` even when reusing older data from the prior cache, masking its true age for the next 12h and printing a misleading "fetched 0s ago" header.

**Fix** (3 edits in `scripts/model_benchmarks.py`):
- `cache_is_fresh(path, cache)` now parses `fetched_at` from the cache JSON and compares against `FRESH_SECONDS`; mtime is only a fallback when the field is missing/unparseable.
- `run_fetch` sets the file-level `fetched_at` to the **oldest** source timestamp, so reused (failed-source) data keeps its true age and re-triggers staleness instead of being masked.
- Failed-and-reused sources carry an explicit `reused: true` flag; `header_line` uses it for the "fetch failed, using cached data (N ago)" note instead of timestamp equality.

**Re-verification (all pass):**

| Test | Result |
|---|---|
| Cache aged to 13h (hand-edit), bare `query --top 1` | PASS — auto-refreshed, header "fetched 4m ago" |
| Repeat bare query on fresh cache | PASS — no re-fetch, fast |
| Cache aged again, `--no-refresh` | PASS — served aged data with honest "fetched 13h ago" header, no network |
| `--force` | PASS — real refresh, both sources ok |
| Fixture offline checks (`--model` tolerant, `gpt` disambiguation, `--compare`) | PASS — no regression |

Note: `run_fetch` captures `now` at fetch start, so a multi-minute fetch stamps `fetched_at` a few minutes old — conservative (data is never presented as fresher than it is), left as-is.