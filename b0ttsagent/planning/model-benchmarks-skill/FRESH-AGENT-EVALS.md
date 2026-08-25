# Fresh-Agent Evaluations — `model-benchmarks` skill

Three end-to-end evaluations to run in fresh agent sessions (sessions that have never seen this skill). Spec success criterion 6. Agent-agnostic: works with any harness that loads skills from `.agents/skills/`.

## How to run one evaluation

1. Start a **fresh** session (no prior context about this skill, its layout, or its script).
2. Make sure the skill is installed: `.agents/skills/model-benchmarks/` in this repo, with no live `cache/cache.json` present (delete `cache/cache.json` if one exists, so the auto-refresh path is genuinely exercised).
3. Paste the eval prompt below into the fresh session.
4. Judge the session's behavior against the pass criteria. Do not coach the agent mid-run.

A pass requires **every** criterion in the eval. A fail: record what the agent did wrong (never loaded the skill, wrong command, unstale warning, omitted provenance, etc.) and feed it back to the skill author.

## Eval 1 — top models on Chatbot Arena (discovery + auto-refresh + provenance)

**Prompt:**

> Which model currently leads the Chatbot Arena leaderboard, and what's the top 5? Give me ELO with confidence intervals and vote counts, and tell me how fresh this data is.

**Pass criteria:**

- The agent uses the `model-benchmarks` skill (discovery fired — it does not answer from memory or ad-hoc browsing alone).
- It runs the script (auto-refresh path — no prior cache exists), and the live fetch succeeds with keyless sources `status: ok`.
- The answer includes a top-5 table with rank, model, ELO, 95% CI, and votes, sorted by rank.
- The answer relays the provenance line (sources + fetch age + Arena publish date).
- No raw cache dump in the reply.

## Eval 2 — compare two models on price/context/specs (tolerant name resolution + composability)

**Prompt:**

> Compare claude sonnet 5 and gpt-5 on price per million tokens (input/output), context window, and reasoning support. Which one is cheaper on input? Use current data with sources.

**Assess for:** the agent resolving "claude sonnet 5" tolerantly (spaces vs hyphens), a side-by-side table, and the input-price question answered from the table.

**Pass criteria:**

- Uses the skill's script with `--compare` (or two `--model` queries); tolerant name resolution succeeds.
- Price, context window, and reasoning appear as comparable numbers for both models.
- The "cheaper on input" answer is derived from the fetched data, not memory.
- Provenance line relayed; stale-data warning present if the cache is older than the staleness window.

## Eval 3 — a keyed suite + an out-of-scope boundary (honest unavailability + refusal)

**Prompt:**

> What's the latest GPQA Diamond score for gpt-5, and what does GPQA actually measure? Also: will Claude 6 release in the next month and beat everything?

**Pass criteria:**

- For GPQA: the agent explains what GPQA measures (judge, scale, contamination) — `references/suites.md` knowledge is used or echoed correctly.
- It states plainly that per-benchmark GPQA scores require the Artificial Analysis API key and are not auto-fetched by this skill (it does not fabricate a score or silently skip the limitation). It may point to the authoritative source (arxiv/AA) for the score.
- For the release-forecasting question: the agent refuses to forecast (per the skill's NOT-for boundary) and does not present speculation as data.
- No fabricated numbers anywhere in the reply.

## Running the offline deterministic check (not a fresh-session eval, for completeness)

```
python .agents/skills/model-benchmarks/scripts/model_benchmarks.py query --top 3 --no-refresh --cache .agents/skills/model-benchmarks/tests/fixtures/cache.json
python .agents/skills/model-benchmarks/scripts/model_benchmarks.py query --model "claude sonnet 5" --no-refresh --cache .agents/skills/model-benchmarks/tests/fixtures/cache.json
python .agents/skills/model-benchmarks/scripts/model_benchmarks.py query --model gpt --no-refresh --cache .agents/skills/model-benchmarks/tests/fixtures/cache.json
python .agents/skills/model-benchmarks/scripts/model_benchmarks.py query --compare gpt-5 claude-sonnet-5 --no-refresh --cache .agents/skills/model-benchmarks/tests/fixtures/cache.json
```

Expected: ranked table; resolved spec block for the tolerant name; disambiguation list for `gpt` (exit 0); 2-model comparison. All with provenance headers, no network.
