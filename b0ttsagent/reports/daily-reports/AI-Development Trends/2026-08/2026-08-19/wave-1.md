# Research wave 1 — 2026-08-19

Day folder: `b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-19/`

## Inputs (reference paths only — never read into context)

- Anchors: `.../2026-08-19/anchors.md` (stitched by anchors lead)
- Inventory: `.../2026-08-19/inventory.json` (written by build-inventory.py)

## Sections & leaf outputs (leaves write exactly their own file)

| Section | Leaf file |
|---|---|
| AI trends | `.../2026-08-19/ai.json` |
| SWE trends | `.../2026-08-19/swe.json` |
| Productivity | `.../2026-08-19/productivity.json` |

## Leaf schema

Follow the leaf schema, coverage domains, and field rules in `references/wave-spec.md` (Leaf schema + Coverage domains). Anchors are seeds, never items; do not re-propose prior identities from `inventory.json` without a dated, concrete `delta_or_null`.

## Per-leaf caps (per research leaf, per wave)

- ≤8 web searches
- ≤5 full page-reads

Thin > padded; never invent to fill.

## Write-boundaries

- Research leaves write ONLY their assigned leaf file (`ai.json` / `swe.json` / `productivity.json`).
- Anchors leaves wrote only `anchors-hn.md` / `anchors-github.md` (throwaway-intermediate); anchors lead wrote `anchors.md`.
- The research lead appends its wave report to `wave-1.md` (this file); it does not write leaf files.
- Routing agent appends gap-fill spec here if triggered. `routed.json` is written only by `route-and-verify.py`.
- No subagent writes outside the day folder. `inventory.json` and `routed.json` are never hand-edited.

## Anchors wave report (anchors lead, 2026-08-19)

- Status: done. Both anchors leaves completed on first attempt; no retries needed.
- HN leaf: 30 stories written to `anchors-hn.md` (raw title/link list).
- GitHub Trending leaf: 13 repos written to `anchors-github.md` (raw repo/link list).
- Stitched `anchors.md` from both leaf files (sections: Hacker News Front Page, GitHub Trending). Non-empty.
- Anomalies: none. Both leaf files existed and were non-empty at QC. Discovery seeds only — no item was promoted from an anchor.

## Research wave report (research lead, 2026-08-19)

- Status: done. All three leaves completed on first attempt; no retries needed. (Resume run: previous wave was interrupted before any leaf wrote; all three leaves were fanned out fresh.)
- AI leaf → `ai.json`: 4 items. AI company news (OpenRouter/Stripe $7B+ acquisition, 08-19), AI policy/regulation (OpenAI pauses RL training 2 weeks, 08-18), open-source AI (Unsloth Dynamic 3.0 GGUFs, 08-19), AI research papers (Ornith-1.5 open-weights, 08-19). Budget: 8/8 searches, 5/5 reads. SearXNG returned empty on all queries — discovery ran via websearch fallback. Domains uncovered: frontier model releases, AI infra/hardware (kept thin).
- SWE leaf → `swe.json`: 3 items. languages & frameworks (Go 1.27.0, 08-19), cloud & pricing (Stripe/OpenRouter $8B+, 08-17), OSS licensing & governance (Google gates Pixel kernel source, 08-17). Budget: 7/8 searches, 5/5 reads. Thin domains: security/CVEs, web platform & standards, dev tools & editors.
- Productivity leaf → `productivity.json`: 3 items. new SWE productivity tools (Vercel fx, 08-18; OneCLI v2, 08-18), emerging practices & workflows (CHAP 0.2 protocol, 06-08). Budget: 5/8 searches, 5/5 reads. Domain thin: AI-assisted dev workflows.
- Lead QA (summaries + programmatic schema check only): all 3 files exist at exact paths, valid JSON, `items` arrays, all 7 schema fields present, `published_date` YYYY-MM-DD, `url` http(s), no anchor-as-item, no prior-identity re-proposal without delta (inventory streak maps empty — 0 prior identities), counts reconcile with leaf summaries (4/3/3). PASS.
- Anomalies for router: (1) CHAP item dated 2026-06-08 — outside 7-day recency window; router may demote/drop. (2) Go 1.27 date conflict — official go.dev says 08-19; two blogs claim 08-02; leaf used official source. (3) Stripe/OpenRouter figure conflict — Axios $8B+ vs Bloomberg/TechCrunch $7B+; leaf used Axios (page read). (4) SearXNG instance returned empty results across all leaves — all discovery fell back to websearch; consider flagging to operator.
- Next actions: route + gap-fill (routing agent) — check survivors per section; Productivity has 2× same-domain cluster and 1 dated 06-08 (likely dropped for recency), so a gap-fill wave may be triggered.

## Gap-fill spec (routing agent, 2026-08-19)

- Trigger: Productivity ended wave 1 with **2 survivors** (`survivor_counts.Productivity = 2`) → within the 0–2 threshold.
- Thin section: **Productivity** — one gap-fill leaf, targeting **exactly 3** new items.
- Empty domain hints (coverage domains with zero survivors): **"AI-assisted dev workflows"** and **"emerging practices & workflows"**. Domain "new SWE productivity tools" already has 2 survivors (Vercel fx, OneCLI v2) — do **not** over-add there; keep it at its current 2.
- Exclusions (do **not** re-propose these identities unless a dated, concrete delta exists): the 10 identities in `routed.json.exclusions`, notably for Productivity the CHAP 0.2 protocol arxiv/2606.09751 (excluded "older than 7 days"; no dated delta exists — skip).
- Prior identities: none (`prior_identities` empty; 0 prior reports).
- Fresh caps (same budget as wave 1): ≤8 web searches / ≤5 full page-reads. Thin > padded; never invent.
- Output rule: the gap-fill leaf writes its section's leaf file `productivity.json` as a **merge**, not a replace — keep the 2 in-window survivors that already routed to main (Vercel fx 08-18, OneCLI v2 08-18), **drop** the out-of-window CHAP item (06-08, already excluded by the router), and append the 3 new in-window items. Result = 5 items.
- Re-route after the leaf returns: routing agent re-runs `route-and-verify.py route`.

## Gap-fill wave report (research lead, 2026-08-19)

- Status: done. Productivity gap-fill leaf completed on first attempt; no retries.
- Productivity leaf → `productivity.json` (merged): kept the 2 wave-1 survivors (Vercel fx, OneCLI v2), dropped the out-of-window CHAP item, added 3 new in-window items: emerging practices & workflows (Warp Factories, 08-18), AI-assisted dev workflows (UiPath Maestro Flow, 08-19; GitLens 19, 08-13).
- Budget: 3/8 searches, 3/5 page-reads (all three primary sources page-verified for date + claim).
- Lead QA: file valid JSON, `items` length 5, all 7 schema fields present, `published_date` YYYY-MM-DD, `url` http(s), no exclusion re-proposal, no prior-identity re-proposal, counts reconcile. PASS.
- Anomalies: none new. Empty domains now covered: AI-assisted dev workflows (2), emerging practices & workflows (1). No domain exceeds 2.
- Next action: routing agent re-runs `route-and-verify.py route`.
