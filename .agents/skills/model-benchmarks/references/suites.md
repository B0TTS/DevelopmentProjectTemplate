# Benchmark Suites Reference

What each benchmark suite the skill knows about actually measures, so a number can be contextualized instead of reported naked. No versioned scores live here — scores come from the cache at query time.

## Contents

- Chatbot Arena (LMSYS)
- LiveBench
- GPQA Diamond
- MMLU / MMLU-Pro
- AIME
- Humanity's Last Exam (HLE)
- SciCode
- LiveCodeBench
- HumanEval / MBPP
- τ²-Bench
- Terminal-Bench
- SWE-bench Verified
- Scale SEAL
- Aider leaderboard
- Artificial Analysis composite indices

Availability modes used below:

- **keyless auto-fetch** — the skill's script pulls this data with no API key.
- **keyed, not auto-fetched** — per-benchmark academic scores require the Artificial Analysis API key; this skill does not call that API, so these are unavailable in the keyless default. Say so plainly rather than omitting the fact.
- **on-demand web only** — no clean keyless JSON; the agent should use general web tools and point the user at the authoritative URL below.

## Chatbot Arena (LMSYS)

- **Measures:** crowd-ranked preference between two anonymous model responses; per-category ELO with 95% CI and vote counts.
- **Scale/cadence:** leaderboard snapshots published on a rolling basis, each with a publish date; the skill's cache records that date.
- **Judge:** pairwise human votes.
- **Contamination:** anonymized responses, prompts contributed by the community.
- **Authoritative source:** https://lmarena.ai/leaderboard — data served keylessly via the HuggingFace `lmarena-ai/leaderboard-dataset`.
- **Availability:** keyless auto-fetch (text category, "overall"). Vision/agent-style categories are on-demand web only.

## LiveBench

- **Measures:** a contamination-controlled suite spanning math, coding, reasoning, language, data analysis, and instruction following; publishes per-model scores on a live leaderboard.
- **Scale/cadence:** questions refreshed in releases over time.
- **Judge:** mostly rule-based/verifiable, some LLM-judged.
- **Contamination:** questions released on a delayed schedule specifically to limit train-time leakage.
- **Authoritative source:** https://livebench.ai
- **Availability:** on-demand web only.

## GPQA Diamond

- **Measures:** graduate-level science questions in physics, chemistry, and biology that domain experts find hard.
- **Scale/cadence:** 198-question Diamond set; static release.
- **Judge:** exact match against a known answer.
- **Contamination:** authors filtered by agreement rates; public exposure is monitored by the maintainers.
- **Authoritative source:** https://arxiv.org/abs/2311.12022
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores). Cite the suite's own paper/site when asked where GPQA scores live.

## MMLU / MMLU-Pro

- **Measures:** broad multi-subject multiple-choice knowledge; MMLU-Pro uses harder, expert-level questions with 10 options.
- **Scale/cadence:** static question sets (MMLU ~14k questions; MMLU-Pro ~12k).
- **Judge:** exact match against a known answer.
- **Contamination:** known to be partially contaminated over time; prefer MMLU-Pro or report with that caveat.
- **Authoritative source:** https://github.com/hendrycks/test (MMLU), https://github.com/TIGER-AI-Lab/MMLU-Pro
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## AIME

- **Measures:** hard competition-level math (American Invitational Mathematics Examination), 30-question editions, integer answers.
- **Scale/cadence:** one edition per year.
- **Judge:** exact match on integer answers.
- **Contamination:** widely reported by providers; treat scores as time-indexed to the model's knowledge cutoff.
- **Authoritative source:** https://maa.org (exam); https://artificialanalysis.ai (model scores)
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## Humanity's Last Exam (HLE)

- **Measures:** ~2,500+ frontier expert questions across many disciplines, written to resist current models.
- **Scale/cadence:** static release; per-subject breakdowns available.
- **Judge:** exact match against reference answers.
- **Contamination:** crowd-written with private answers until release.
- **Authoritative source:** https://lastexam.ai
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## SciCode

- **Measures:** whether a model can write code that reproduces published scientific results; judged by generated-code execution against hidden tests.
- **Scale/cadence:** static benchmark of research problems.
- **Judge:** execution against reference tests.
- **Contamination:** derived from papers; low public exposure at release.
- **Authoritative source:** https://scicode-bench.github.io
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## LiveCodeBench

- **Measures:** code generation on a contamination-controlled, time-windowed mix of competitive-programming and real-world problems.
- **Scale/cadence:** rolling question windows; results grouped by date range.
- **Judge:** execution against reference tests, some with LLM-judged output comparison.
- **Contamination:** questions drawn from releases after the model's cutoff, grouped by time window.
- **Authoritative source:** https://livecodebench.github.io
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## HumanEval / MBPP

- **Measures:** classic function-level code generation from docstrings (HumanEval 164 problems, MBPP ~1k crowd-written problems).
- **Scale/cadence:** static sets.
- **Judge:** execution against unit tests (pass@k).
- **Contamination:** heavily leaked into training corpora by now; only useful as a historical baseline.
- **Authoritative source:** https://github.com/openai/human-eval
- **Availability:** on-demand web only.

## τ²-Bench

- **Measures:** agentic tool-use in a simulated world (airline customer-service environment) across many sequential tasks.
- **Scale/cadence:** scenario packs, 500+ tasks across variants.
- **Judge:** verifiable state checks plus LLM-judged outcomes.
- **Contamination:** closed scenario details; low exposure.
- **Authoritative source:** https://github.com/sierra-research/tau-bench
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## Terminal-Bench

- **Measures:** agentic use of a terminal to solve tasks (system administration, file ops, programming) in isolated environments.
- **Scale/cadence:** ~100 task suite with cross-platform variants.
- **Judge:** execution-based task completion checks.
- **Contamination:** relatively new; low exposure.
- **Authoritative source:** https://github.com/laude-institute/t-bench
- **Availability:** keyed, not auto-fetched (Artificial Analysis per-benchmark scores).

## SWE-bench Verified

- **Measures:** real GitHub issue resolution from Python repos (500 verified tasks), judged by hidden tests.
- **Scale/cadence:** static curated set.
- **Judge:** execution of the repo's test suite.
- **Contamination:** issues are public; contamination risk varies by model cutoff.
- **Authoritative source:** https://www.swebench.com
- **Availability:** on-demand web only.

## Scale SEAL

- **Measures:** private, expert-curated evaluation across coding, math, instruction following, and safety.
- **Scale/cadence:** curated by Scale AI; details mostly closed.
- **Judge:** undisclosed expert/automated mix.
- **Contamination:** private leaderboard; strong anti-contamination by design.
- **Authoritative source:** https://scale.com/leaderboard
- **Availability:** on-demand web only.

## Aider leaderboard

- **Measures:** polyglot code-editing benchmark run by the Aider project across many models and editors.
- **Scale/cadence:** rolling leaderboard, updated as new models ship.
- **Judge:** pass rate across a fixed exercise set.
- **Contamination:** exercise details public.
- **Authoritative source:** https://aider.chat/docs/leaderboards/
- **Availability:** on-demand web only.

## Artificial Analysis composite indices

- **Measures:** composite indices that aggregate a provider's suite coverage — intelligence, coding, agentic — each a weighted mix of the suites above.
- **Scale/cadence:** updated as models ship; published per model.
- **Judge:** composite of underlying suite judges.
- **Contamination:** inherits the underlying suites' approaches.
- **Authoritative source:** https://artificialanalysis.ai
- **Availability:** keyless auto-fetch — the three composite indices (intelligence, coding, agentic) arrive with the OpenRouter models list. Per-benchmark academic scores behind them are keyed, not auto-fetched.
