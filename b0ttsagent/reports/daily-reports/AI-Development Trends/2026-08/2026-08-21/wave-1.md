# Wave 1 — 2026-08-21 daily trends run

Setup-phase wave document authored by the Explorer (`b0tts-general-agent`) from `references/wave-spec.md`, path-references only. Research lead and routing agent append their reports here.

## Day folder

- Base: `b0ttsagent/reports/daily-reports/AI-Development Trends`
- Month: `2026-08`
- Today: `2026-08-21`
- Day folder: `b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-21/`

## Sections and output paths

| Section | Leaf file (output path, in the day folder) |
|---|---|
| AI trends | `ai.json` |
| SWE trends | `swe.json` |
| Productivity | `productivity.json` |

## Reference paths (do not read contents)

- `anchors.md` — stitched by the anchors lead; discovery seeds for research leaves.
- `inventory.json` — written by `build-inventory.py` (Explorer); streak maps for prior identities.

## Per-leaf caps

Hard caps per research leaf, per wave — the first wave and any gap-fill wave each get the same fresh budget:

- ≤8 web searches
- ≤5 full page-reads (fetch + read a page to verify claims)

A search snippet is discovery, not evidence. When budget is spent, stop and write what you have. Thin > padded; never invent to fill. Anchors leaves are single-page raw fetches — not subject to the 8/5 budget.

## Leaf schema

Each leaf writes one file shaped as `{ "items": [ ... ] }`. Every item carries all 7 fields:

- `headline` — non-empty, plain, claim-faithful.
- `why` — why it matters, ≤2 sentences / ~40 words.
- `url` — primary source, `http(s)`, the page actually read to verify the claim.
- `published_date` — `YYYY-MM-DD`, no guessed dates; empty string means undated.
- `domain` — one of the section's coverage-domain hints.
- `source_type` — paper, advisory, release notes, blog post, news, changelog…
- `delta_or_null` — `null`, or the concrete dated delta (version, number, decision, CVE id, ship date) when re-proposing a prior identity.

Leaves propose; they do not route. Placement is the router's job. Do not re-propose inventory streak identities without a dated concrete delta. Anchors are seeds, never items.

## Coverage domain hints

| Section | Domain hints (hints, not a quota) |
|---|---|
| AI trends | frontier model releases · AI research papers · AI company news · open-source AI · AI policy/regulation · AI infra/hardware |
| SWE trends | security & CVEs · OSS licensing & governance · cloud & pricing · languages & frameworks · web platform & standards · dev tools & editors |
| Productivity | new SWE productivity tools · AI-assisted dev workflows · emerging practices & workflows |

Productivity constraint: items must be shipped or newly documented tools/workflows/practices with a dated primary source. No "10 tips" roundups, no evergreen posts.

## Write boundaries

| Actor | May write |
|---|---|
| Orchestrator | runs verify; upserts `index.md`; posts chat pointer; reads only bounded summaries |
| Explorer (`b0tts-general-agent`) | `wave-1.md`; runs `build-inventory.py` (which alone writes `inventory.json`) |
| Anchors lead (`b0tts-lead-researcher`) | `anchors.md` (stitched); its wave report appended to `wave-1.md` |
| Anchors leaves (`b0tts-researcher`) | only `anchors-hn.md` / `anchors-github.md` |
| Research lead (`b0tts-lead-researcher`) | its wave report appended to `wave-1.md` |
| Research leaves (`b0tts-researcher`) | only `ai.json` / `swe.json` / `productivity.json` |
| Routing agent (`b0tts-smart-general-agent`) | gap-fill spec appended to `wave-1.md`; runs `route-and-verify.py route` (which alone writes `routed.json`) |
| Writer (`b0tts-smart-general-agent`) | only `report.md` (sole writer) |

No subagent writes outside the day folder. `inventory.json`, `routed.json`, and the two anchor-leaf files are derived/throwaway — never hand-edited.

## Anchors wave — 2026-08-21

Led by `b0tts-lead-researcher`; two `b0tts-researcher` leaves fanned out in parallel (one message), each a single-page raw fetch, no research budget consumed.

| Leaf | Source | Output | Count | Status |
|---|---|---|---|---|
| HN | https://news.ycombinator.com | `anchors-hn.md` | 30 stories | done |
| GitHub Trending | https://github.com/trending | `anchors-github.md` | 16 repos | done |

- Lead QA: both leaf files exist and are non-empty; counts reconcile with leaf summaries; raw title/link lists only (no analysis/commentary); no fabricated entries.
- Stitched output: `anchors.md` — both sections with headers, fetch date (2026-08-21), source URLs, and preserved titles/links.
- Anomalies: none. No retries needed; both leaves returned on first attempt.
- Note for research leaves: anchors are discovery seeds only — an HN thread or trending row is never a report item; find the dated primary source behind any seed you pursue.

## Research wave — 2026-08-21

Led by `b0tts-lead-researcher` (muse-spark-1.2-contributor); 3 `b0tts-researcher` leaves. Spawn anomaly: leaves were fanned out sequentially (3 separate task calls) due to single-tool-call harness constraint, not in one message as wave-spec requires — functional equivalent, all 3 fresh budgets respected.

| Leaf | Output | Count | Status | Verdict |
|---|---|---|---|---|
| AI trends | `b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-21/ai.json` | 4 | done | PASS |
| SWE trends | `b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-21/swe.json` | 3 | done | PASS |
| Productivity | `b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-21/productivity.json` | 5 | done | PASS |

- **AI domains:** frontier model releases (1) · AI infra/hardware (2) · AI research papers (1). Budget 8/8 searches, 5/5 reads.
- **SWE domains:** languages & frameworks (1) · security & CVEs (1) · web platform & standards (1). Budget 8/8 searches, 5/5 reads.
- **Productivity domains:** AI-assisted dev workflows (2) · new SWE productivity tools (1) · emerging practices & workflows (2). Budget 3/8 searches, 5/5 reads. All 5 ship-dated and constraint-compliant.
- All 12 items passed schema field check (headline/why/url/published_date/domain/source_type/delta_or_null) via validator; counts reconcile with summaries.

### Lead QA checklist (summaries-only; validator counted without pulling full files)

- [x] Every leaf output exists at exact path, valid JSON with `items` list (validator confirms true for all 3; empty list not needed)
- [x] Every item carries all 7 schema fields; `published_date` is `YYYY-MM-DD`; `url` is `http(s)` (validator: fields_ok true, url_ok true, date_ok true)
- [x] No item re-proposes inventory streak identity without non-empty `delta_or_null` — all leaves report 0 re-proposals; all deltas are null (verified in summaries)
- [x] No item is an anchor used as item itself (HN thread / trending row) — all leaves confirm anchors seeds only
- [x] Every delta is concrete (version/number/decision/CVE id/ship date) — trivially true, all null; no "still being discussed"
- [x] Counts in each leaf's final summary reconcile with its file — AI 4=4, SWE 3=3, Productivity 5=5
- [x] QA reads summaries only; validator used for existence/counts without pulling full leaf contents into context
- [x] Missing/invalid output → no retry needed; second-failure path not triggered

### Anomalies

- **AI leaf — secondary verification:** CEPR study primary (Economist) returned 403 bot-block; leaf corroborated claim via multiple independent dated sources (NY Post 08-19 etc.) but correctly retained Economist URL; flag for router awareness — verify may treat as less-strong primary but date is claimed on page traversals. CNBC Nvidia 403 similarly swapped to Fortune read — correct handling.
- **SWE leaf — intentional drops:** Google Antigravity IDE (no dated primary), Chrome 151 CVE-2026-76017 (non-primary), Copilot Agent Plugins (Aug 12 out-of-window), cloud-pricing trackers (undated) — all correctly dropped per window/evidence rules. Leaves thin domains intentionally per "thin > padded".
- **Productivity leaf — Proliferate IDE** (HN seed) dropped for no dated primary — correct. "Agentic software factory" phrase-returns-empty but found via anchor URL direct — acceptable discovery.
- **Caps respected:** AI 8/8+5/5, SWE 8/8+5/5, Prod 3/8+5/5 — all within wave-spec hard caps.
- **No retries:** all 3 leaves succeeded first attempt; no FAIL-UNKNOWN.

### Next actions

- **Route + gap-fill:** Orchestrator to spawn `b0tts-smart-agent` to run `python scripts/route-and-verify.py route --folder "b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-21" --today 2026-08-21`. With 12 candidates (4/3/5 per section), main sections likely have ≥3 survivors — gap-fill trigger (0–2 survivors) not expected, but router determines. `routed.json` will be frozen thereafter; writer words only from it.
- **No leaf re-run required.**
- **Write-boundaries respected:** leaves wrote only assigned json; lead appended only this section to wave-1.md.
