# Review: `model-benchmarks` skill docs vs SPEC.md + write-a-skill-v2

Date: 2026-08-21 · Reviewer role: read + verify + report (no files edited)

## Checklist

1. **Frontmatter — PASS.** `name: model-benchmarks` (13 chars ≤64, lowercase-hyphen, matches parent dir `.agents/skills/model-benchmarks/`). `description` 693 chars (≤1024), third person ("Fetches…/Use when…/NOT for…"), includes what + triggers + boundary, no first person. Note: name is not gerund form, but SPEC.md's Implementation Decisions explicitly overrides gerund form per project convention (`pdf`, `log-session`) — contract-compliant.

2. **Trigger surface — PASS.** Description covers all spec-required triggers: "which model leads a leaderboard or Chatbot Arena" (Chatbot Arena/LiveBench/coding), "a model's ELO" (what's the ELO of), "benchmark scores", "price, context window, modality, reasoning support" (model specs/price/context), "compare two or three models side by side" (compare X and Y; the "on [GPQA/price/context]" dimension is covered by the combination of "compare side by side" + "benchmark scores/price/context window"). NOT-for boundary matches spec verbatim: forecasting, running benchmarks locally, local/private models, recommending providers, scraping uncovered sources.

3. **SKILL.md body < 500 lines — PASS.** 73 lines total, 70 body lines after frontmatter (spec: <500; write-a-skill-v2: <5000 tokens is trivially met).

4. **No time-sensitive facts — PASS (1 NIT).** No "current top model", no dated scores, no "latest version" anywhere in SKILL.md, suites.md, or sources.md. Cadence/scale descriptions ("rolling basis", "roughly 400 records", "updated as models ship") are structural, not rot-prone. NIT: SKILL.md:59 example provenance header embeds a concrete date (`Arena publish date 2026-08-19`) — clearly labeled "e.g.", but a date-in-body per write-a-skill-v2; suggest a `<Arena publish date>` placeholder.

5. **Body structure — PASS.** Contains: one-paragraph capability (SKILL.md:8-10), workflow refresh-or-use-cache → query → compose (SKILL.md:12-16), script CLI reference (SKILL.md:18-48), dependency declaration "Python 3, standard library only… Run with `python`" (SKILL.md:50-52), provenance/age contract (SKILL.md:54-64), pointers to both reference docs (SKILL.md:70-73).

6. **CLI reference matches script — PASS (2 NITs).** Verified live: `fetch`/no-subcommand default ✓; `query` mutually-exclusive required `--top/--model/--compare` ✓; `--no-refresh`/`--force` ✓; global `--cache` (root and post-subcommand both work) ✓; staleness window 12h (`FRESH_SECONDS = 12*60*60` at model_benchmarks.py:15 matches "older than 12 hours" SKILL.md:15) ✓; tolerant name matching + alias resolution ✓; disambiguation prints list, picks none, exit 0 ✓; exit 1 with one clear line on no-match, missing cache under `--no-refresh`, all-sources-failed ✓ (all three verified by execution); argparse usage errors (`--top 0`, single-`--compare`) exit 2, not contradicted by SKILL.md. NITs: (a) `query --help` hides `--cache` (`help=argparse.SUPPRESS` at model_benchmarks.py:566) — documented in SKILL.md so low risk, but a fresh agent relying on `--help` can't discover it; (b) SKILL.md:42 example `query --top 5 --cache tests/fixtures/cache.json` omits `--no-refresh`, so against the current (30h-old) fixture it triggers a live refresh, weakening the "point at a specific cache file" illustration.

7. **Reference docs one level deep — NIT.** SKILL.md links directly to both references ✓. But suites.md:35 contains `(see sources.md)` — a reference-to-reference cross-link. Soft pointer (the dataset name and primary URL are inline; both docs are reachable from SKILL.md), but it deviates from the checklist's literal "neither reference links to another reference". Suggest inlining the datasets-server note or dropping the pointer.

8. **Forward slashes only — PASS.** No backslashes found in SKILL.md, suites.md, or sources.md (verified by scan). (The `%2F` in sources.md:24 is URL encoding, not a path.)

9. **Consistent terminology — PASS.** "cache", "source", "suite", "record", "query" used consistently across all three docs; "endpoint" is the single term in sources.md; no "route/path" drift; no "leaderboard data" vs "arena data" mixing; ELO capitalization consistent.

10. **suites.md covers all suites — PASS.** All 15 section headers present (spec's "16" counts Chatbot Arena text/vision/agent as 3; vision/agent are explicitly covered in the Chatbot Arena section, availability "on-demand web only"). Each of the 15 sections has: measures, scale/cadence, judge type, contamination approach, authoritative URL, availability mode. Table of contents at top (suites.md:5-21). Availability-mode legend at top (suites.md:23-27).

11. **sources.md coverage — PASS (1 NIT).** Covers: endpoint per source, keyless vs keyed, fields returned, update cadence, attribution; cache schema; name normalization; failure semantics. Table of contents at top (sources.md:5-12). NIT: sources.md:26 lists `license` and `variance` under "Fields used" for Arena, but the script never reads either (arena_records at model_benchmarks.py:132-155 consumes rating/rating_lower/rating_upper/vote_count/rank/category/leaderboard_publish_date/model_name/organization only). Either the script should capture them or the doc should say "fields available".

12. **User story 16 — PASS.** suites.md availability modes define "keyed, not auto-fetched" with "Say so plainly rather than omitting the fact"; GPQA Diamond (suites.md:54), MMLU-Pro (63), AIME (72), HLE (81), SciCode (90), LiveCodeBench (99), τ²-Bench (117), Terminal-Bench (126) all state the keyed/unavailable-in-keyless-default status. sources.md:33 (Artificial Analysis) states plainly the API is not called in v1 and per-benchmark academic scores are unavailable keylessly. No fabricated scores, no silent omission.

13. **Cache schema matches spec AND script — PASS.** sources.md:38-69 schema matches the script's `merge()` output exactly (aliases, creator, context_window, modality, release_date, reasoning{supported,efforts,default}, price{input_per_m,output_per_m,cache_read_per_m}, indices{intelligence,coding,agentic}, arena{elo,elo_ci_lower,elo_ci_upper,votes,rank,category,publish_date}) and the spec's schema (minus the spec's aspirational `artificial_analysis` sources entry, which v1 never emits — consistent with sources.md "documented, not called"). Verified against fixture and live `--top/--model/--compare` output.

14. **Runtime cache gitignored, fixture not ignored — PASS (1 NIT).** `git check-ignore -v` confirms `.agents/skills/model-benchmarks/cache/cache.json` → ignored via `.gitignore:73`. Fixture path → no ignore match (not ignored) ✓. Fixture file present (tests/fixtures/cache.json, 3741 bytes, valid JSON matching schema) ✓. NIT: `git ls-files` shows the fixture is currently UNtracked — the whole skill dir is untracked (`??`) — so the `.gitignore:72` comment "Offline test fixture stays tracked" is aspirational until the skill is `git add`ed. Ensure the fixture is committed with the skill, or the offline deterministic-test seam (spec Testing Decisions, user story 29) is missing for fresh agents.

## Findings (severity)

- **BLOCKER:** none.
- **MAJOR:** none.
- **MINOR:** none.
- **NIT (recommended, non-blocking):**
  1. `SKILL.md:59` — example provenance header embeds concrete date `2026-08-19`; replace with placeholder (e.g. `<Arena publish date>`) to honor the no-dates-in-body rule.
  2. `suites.md:35` — `(see sources.md)` cross-reference between references; inline the detail or drop the pointer to strictly satisfy one-level-deep.
  3. `sources.md:26` — `license` and `variance` listed as "Fields used" but never read by the script; align doc with script (or capture them).
  4. `SKILL.md:42` — fixture `--cache` example lacks `--no-refresh`; add it so the example stays offline/illustrative.
  5. `model_benchmarks.py:566` — `--cache` hidden from subcommand help (`argparse.SUPPRESS`); acceptable since SKILL.md documents it, but consider not suppressing.
  6. `.gitignore:71-72` + git state — fixture not yet committed; `git add` it with the skill so the "stays tracked" comment holds.

## Verdict

**READY-WITH-FIXES** — all contract-critical checks PASS; no BLOCKER/MAJOR/MINOR issues. Six cosmetic NITs, all optional; item 7's reference-to-reference pointer is the only literal checklist deviation and is non-blocking. The skill is shippable as-is; apply the NITs at leisure before final commit.
