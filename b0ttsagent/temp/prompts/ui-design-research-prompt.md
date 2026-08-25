# UI Designer Workflow Research — Main Orchestrator Prompt

## Mission

Research publicly documented, in-depth UI design workflows/formulas from verified top designers, orchestrated through a 3-tier wave pattern of subagents. Deliver per-designer workflow docs plus a synthesis with parallels under `b0ttsagent/research/ui-design-workflows/`.

We want **craft-first** workflows: step-by-step formulas top designers use to consistently produce exceptional UI. Growth/experimentation workflows count only when the same designer documents their design process in depth (tagged accordingly). Genre/style doesn't matter (consumer apps, B2B SaaS, marketing sites, mobile, games, dev tools) — tag product type per designer.

## Verification standard (STRICT — reject if not met)

An individual designer qualifies only if:

1. Their **name** is publicly tied (portfolio, LinkedIn, credits, press, "designed by") to at least one shipped product with **public scale evidence within the last 5 years**:
   - ≥1M monthly active users navigating their UI (credible public source), OR
   - the project publicly generates thousands of dollars/month (credible source).
2. No public scale evidence found → **REJECT**. Never assume, never fill gaps. Log the rejection reason.
3. Design-system/team processes (Material, Polaris, Carbon, etc.) don't qualify — individual attribution required.
4. "Doing well within the last 5 years" means the scale evidence itself falls inside the 5-year window (research date minus 5 years). A decade-old hit with nothing in-window → leave out.

## Depth gate (STRICT — applies to every accepted workflow)

A workflow qualifies only if:

- **First-party:** documented by the designer themselves (own blog, website, YouTube, course, book, X threads, podcast appearances where they describe their own process).
- **Structured:** named, ordered steps/stages, with at least one explicit quality gate or iteration loop (e.g., self-crit rituals, v1→v2→v3 comparisons, specific tests the UI must pass).
- **Excluded:** "10 tips" listicles, portfolio case studies without process, secondhand descriptions (interviews where others describe the designer's process are supplementary only, never the anchor source).
- Every step in the final doc carries a source link.
- Older docs are allowed **only if** the designer passes the 5-year scale test AND the workflow is confirmably still current (recent content references it). Record this check as one line in the eligibility evidence either way.

## Targets

- **≥8 verified designers** with full depth docs; ceiling ~12.
- **Depth-first:** never lower a gate to hit a count. If a candidate fails during Phase 2, replenish from spares.

## Orchestration — 3-tier wave pattern

You are the **main orchestrator** (primary agent). Keep your own context under 60–80k tokens at all times. Spawn waves **sequentially**: one wave-lead `task` call at a time; each blocks until the lead returns its final message.

Requires opencode config: `subagent_depth: 2` (so wave leads can spawn researchers), plus two subagent roles — `ui-research-lead` (subagent, `task` allowed) and `ui-researcher` (subagent, `task` denied). Model assignment: you = best model, leads = mid model, researchers = cheapest competent model.

### Wave lifecycle

1. Before each wave, write the wave spec: `working/waves/wave-0N.md` — wave goal, roster (names/URLs), per-researcher task prompt (≤150 words each, with exact output paths and required return format), completion criteria, QA checklist.
2. Spawn the lead with:
   > You are Wave N lead. Read `working/waves/wave-0N.md` and execute it exactly. Spawn all researchers in ONE message (parallel fanout). Wait for all to finish. Read each researcher's final summary only — never read their full docs into your context. Write `working/waves/report-0N.md` (per-researcher status, verdicts, anomalies, next actions). Final message: ≤500 words.
3. **QA gate:** verify every expected file exists, verdicts match the evidence, the report is written. Then append one line to `working/MANIFEST.md` (wave number, result, counts, next wave).
4. On resume or context compaction: read `working/MANIFEST.md` first — disk is your memory.

### Context budget rules (bake into every subagent prompt)

- **Researchers:** full work product goes to disk only. Final message ≤250 words (status, file paths, verdict). Never paste doc content into the final message.
- **Wave leads:** context = wave spec + researcher summaries only. Never read full docs.
- **You:** only wave summaries enter your context (~500 words per wave). Specs live on disk, not in your working memory.

### Failure handling

- Lead dies mid-wave → resume its session via `task_id`, or re-spawn fresh with "resume from `working/MANIFEST.md`".
- Researcher fails → verdict `FAIL-UNKNOWN`; retry once with the same spec.

## Phases

- **Phase 0 — Candidate discovery (1 wave):** 3 discovery researchers → `working/candidates.md`: ≥20 candidates, each with name, claimed products, scale-evidence leads, first-party doc URLs.
- **Phase 1 — Verification (waves of 3–4 candidates):** one researcher per candidate: run the verification test; write `working/evidence/<name>-dated.json` plus a verdict (PASS/REJECT + reason) into the wave report. Continue until ≥8 PASS (prefer 10–12 for margin) or candidates are exhausted.
- **Phase 2 — Depth docs (waves of 3–4 verified designers):** one researcher per designer → `creators/<Name>.md`. If the documentation turns out shallow on inspection (fails the depth gate) → REJECT with reason; replenish from spares if the verified count would drop below 8.
- **Phase 3 — Synthesis (one final subagent):** read all `creators/*.md` + wave reports; write `SYNTHESIS.md` and `INDEX.md`.

## Deliverables

`b0ttsagent/research/ui-design-workflows/`

### `creators/<Name>.md`
1. **Eligibility Evidence** — scale evidence with dates + links; 5-year in-window check; doc currency check; product-type tag; craft/growth tag.
2. **Step-by-Step Workflow** — the full named sequence: steps, gates, iteration loops; per-claim source links.
3. **What Makes It Distinct** — the non-generic signature elements.
4. **Sources** — canonical links.

### `SYNTHESIS.md`
1. **Headline answer** — bottom line up front.
2. **Method** — how it was derived, with QA notes (weak/boundary verifications flagged).
3. **Per-framework depth sections** — one per verified designer, deep enough to use alone.
4. **Parallels section** — creators × elements matrix + per-element writeups: near-universal practices, the biggest divergence, and elements found only in the top-ranked workflows.

### `INDEX.md`
Ranked creators table. Ranking method: (1) **verification strength** — scale of shipped evidence + margin on the 5-year test, (2) **documentation depth/structural completeness**, (3) **workflow specificity/transferability**. Bottom of file: "Rejected candidates" section (name + one-line reason). Note the research date.

## Hard rules

- Every scale claim links to public evidence. No public evidence → REJECT, never assume.
- Never lower the verification or depth gates to hit counts.
- Working files only under `working/`. Final docs only at the paths above.
- Only summaries flow into orchestrator contexts — never full docs.
