---
name: daily-trends-report
description: Generates a dated daily quick-scan digest of AI trends, software-engineering trends, and SWE productivity items, with source links, published dates, and a Still circulating section for streak-hit stories. Use when the user says "generate today's report", "daily trends report", "today's AI report", "daily AI digest", "SWE trends report", or wants today's AI/dev/productivity scan written to the daily-reports folder. NOT for weekly recaps, researching a single topic, personalized coaching, schedule changes, or publishing to a tracker.
disable-model-invocation: true
---

# Daily trends report

**One job:** generate today's quick-scan digest and write it to `b0ttsagent/reports/daily-reports/AI-Development Trends/<YYYY-MM>/<YYYY-MM-DD>/report.md`. Three main sections (AI trends, SWE trends, Productivity) of 1–5 items each, plus a Still circulating residue table when any exist. Fires only as an explicit `/skill:daily-trends-report`; hidden from auto-load.

- Runtime is opencode. Spawn subagents with the task tool using the existing agent definitions (`b0tts-general-agent`, `b0tts-lead-researcher`, `b0tts-researcher`, `b0tts-smart-agent`); no new agent definitions.
- Report files are the source of truth. `inventory.json` and `routed.json` are throwaway script outputs, rebuilt every run, never hand-edited.
- Both scripts are Python 3 stdlib-only, run via `python` on PATH; no installs.

## Refuse list

Refuse, and say so, when the request is:

1. A weekly recap or any non-daily cadence
2. A deep dive into one story
3. Editing a Schedule Spec
4. Personalization ("what this means for you")
5. Publishing to an issue tracker
6. "Also refresh yesterday" or backfilling other days

## Runbook

The orchestrator is a thin conductor: it sequences phase-owned agents and keeps only the ship phase for itself. It never reads `anchors.md`, `inventory.json`, or `routed.json` contents — heavy, disposable artifacts live and die inside phase-agent contexts. Each phase agent reads the contract it needs from `references/` itself; the orchestrator composes short spawn instructions, never templates.

**1. Setup — two parallel siblings, joined before research.** Spawn both in ONE message:

- **Explorer** (`b0tts-general-agent`) — run `scripts/build-inventory.py` (CLI in `references/wave-spec.md`), then author `wave-1.md` from the contract in `references/wave-spec.md` (folder layout, leaf schema, coverage domains, caps, write-boundaries) using path-references only — never read `anchors.md` or `inventory.json` contents. Return ≤150 words: inventory count, `wave-1.md` path, edge-case warnings.
- **Anchors wave** (`b0tts-lead-researcher`) — read the anchors contract in `references/wave-spec.md` and execute: fan out 2 `b0tts-researcher` leaves (HN front page / GitHub Trending), each writes its raw title/link list to its own file (`anchors-hn.md` / `anchors-github.md`) and returns only a count; the lead QC's existence + non-emptiness, reads the two small leaf files, and stitches them into `anchors.md`. Return ≤500 words: status, `anchors.md` path, counts, anomalies.

Wait for both. The orchestrator reads neither the leaf files nor `anchors.md`.

**2. Research wave.** Spawn `b0tts-lead-researcher` pointing at the Explorer-authored `wave-1.md`. It fans out 3 leaves (AI / SWE / Productivity) in one message, QA's disk outputs per `references/wave-spec.md`, and appends its wave report to `wave-1.md`. Per-leaf caps: 8 searches + 5 page-reads, fresh budget each wave. Return ≤500 words.

**3. Route + gap-fill** (`b0tts-smart-agent`). Run `scripts/route-and-verify.py route` (CLI in `references/wave-spec.md`); read survivors-per-section from the now-frozen `routed.json`; if any main section has 0–2 survivors, author exactly ONE gap-fill spec from `routed.json`'s exclusions, prior identities, and the thin section's empty domain hints (`references/wave-spec.md`), append it to `wave-1.md`, re-spawn the research lead for the thin section, and re-run `route`; then stop — no third wave. Still short → ship short. Return ≤250 words: survivors-per-section, whether a gap-fill wave ran, frozen `routed.json` path. The orchestrator never reads `routed.json` contents.

**4. Writer** (`b0tts-smart-agent`). Spawn with the frozen `routed.json` path + instruction to read `references/report-contract.md` and write `report.md` — wording only: no research, no routing, no rescue of rejects. Only the writer writes `report.md`; skeleton and field rules: `references/report-contract.md`. Return ≤250 words: `report.md` path, section/item counts, the 3 glance bullets, demoted count when Still circulating is non-empty.

**5. Ship** (orchestrator keeps). Run `scripts/route-and-verify.py verify` (CLI in `references/wave-spec.md`). Exit 0 = gates clean. Exit 1 = exactly one writer rewrite, then ship with a "verify failed" note — never loop. Then upsert `index.md` (create if missing, newest row on top; a same-day rerun updates today's row, never appends a duplicate) and post the chat pointer from the writer's summary: path + the 3 glance bullets + "N items demoted" when Still circulating is non-empty. Formats: `references/report-contract.md`.

Clock: "today" and the 7-day window run on the scripts' canonical UTC−10 offset; both scripts default `--today` to it. Pass `--today` explicitly only in fixtures and tests.

Same-day rerun: run the phases again. Today's folder is never treated as history, `report.md` is overwritten, and `index.md` upserts the existing row (no duplicate). Proof: `references/eval-fixtures.md`, Scenario 8.

Report quality bar: the markdown-doc-designs auto-mode checklist only; `DESIGN.md` does not apply to these reports.

## Copy-in checklist

Paste into the run and tick as you go:

- [ ] Explorer spawned (inventory + wave-1.md)
- [ ] Anchors wave spawned (anchors.md stitched)
- [ ] Setup joined
- [ ] Research lead spawned
- [ ] QA passed
- [ ] Route + gap-fill done (routed.json frozen)
- [ ] Writer spawned
- [ ] Verify script pass
- [ ] Index updated
- [ ] Chat pointer posted

## Degrees of freedom

| Freedom | What it covers |
|---|---|
| Low — locked, do not improvise | Identity, gates, dates, paths, verify script, section membership. The scripts own these; `references/routing-rules.md` documents them exactly. |
| Medium — constrained choices | Which 3–5 survivors to keep per section; the domain-spread preference (max 2 per domain per section); gap-fill queries. |
| High — your judgment | Headline phrasing and why-it-matters wording. The writer's judgment, bounded by the item-field rules in `references/report-contract.md` (why-it-matters ≤2 sentences / ~40 words) and the markdown-doc-designs quality bar. |

## Read which reference when

- `references/routing-rules.md` — read when you need to know where an item goes and why: identity, gates, update test, domain preference, and what verify enforces. The scripts are the executable truth; this doc matches them.
- `references/report-contract.md` — read when writing `report.md` or assembling the day folder, `index.md`, or the chat pointer: skeleton, item fields, glance block, word budget, Still circulating, and good vs rejected examples.
- `references/wave-spec.md` — read when sequencing the phases: day-folder layout, writers-of-record, leaf schema, caps, lead QA checklist, anchors-wave contract, gap-fill rules, bounded summaries, and the exact CLI lines. Phase agents read it themselves; the orchestrator composes spawn instructions from it — never templates.
- `references/eval-fixtures.md` — read before changing the deterministic layer or after a script edit: 8 runnable scenarios with commands and expected output (5 are the mandated minimum).
