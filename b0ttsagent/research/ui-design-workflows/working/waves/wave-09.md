# Wave 09 — Phase 2: Depth Docs (wave 3 of 3)

- Phase: 2 (Depth docs)
- Goal: `creators/<Name>.md` for the final 4 verified designers (ranking #9-12), each passing the depth gate; DEPTH-REJECT allowed with reason
- Research date: 2026-08-17
- Roster: 4 researchers, one designer each, parallel fanout
- Input: each researcher reads their designer's evidence JSON (`working/evidence/<slug>-2026-08-17.json`) for eligibility facts — **do NOT re-verify scale; that is settled**

## Depth gate (STRICT — applies to every workflow doc)

- **First-party:** documented by the designer themselves (own blog, website, YouTube, course, book, X threads, podcast appearances where they describe their own process).
- **Structured:** named, ordered steps/stages, with at least one explicit quality gate or iteration loop (e.g., self-crit rituals, v1→v2→v3 comparisons, specific tests the UI must pass).
- **Excluded:** "10 tips" listicles, portfolio case studies without process, secondhand descriptions (interviews where others describe the designer's process are supplementary only, never the anchor source).
- **Every step in the final doc carries a source link** to the exact first-party location.
- **Doc-currency:** older docs allowed only if the designer passed the 5-year test AND the workflow is confirmably still current (recent content references it). Record this check as one line in the Eligibility Evidence section.

## Deliverable schema — `creators/<Name>.md` (exact 4 sections)

1. **Eligibility Evidence** — scale/award evidence with dates + links (copy facts from the evidence JSON, do not re-verify), route (MAU/revenue/usage-stat/award) + source tier; 5-year in-window check; doc currency check (one line); product-type tag (consumer / B2B SaaS / marketing site / mobile / game / dev tool / niche); craft/growth tag (craft-first vs growth/experimentation — growth counts only if the designer documents their design process in depth, tagged accordingly).
2. **Step-by-Step Workflow** — the full named sequence: steps, gates, iteration loops; per-claim source links. Deep enough to use alone (~600-1200 words).
3. **What Makes It Distinct** — the non-generic signature elements (NOT generic advice restated).
4. **Sources** — canonical first-party links.

## Shared tooling (all researchers)

- Follow `.agents/skills/opencode-web-research/SKILL.md`: try `searxng_searxng_web_search` ONCE; on error/empty use `websearch` (Exa). `web_search` (metasearch2) is last resort only. For YouTube sources: transcripts are acceptable first-party evidence (the designer's own words).
- Read a page before citing it. Never invent a step, quote, or link. If on inspection the source is shallow (listicle, case study without process, secondhand-only) → DEPTH-REJECT with reason and stop spending budget on that designer. DEPTH-REJECT is a valid outcome.
- Efficiency: if any search/read tool hangs or returns nothing twice in a row, switch tools and move on. Budget ~60 minutes of tool work; never stall without writing your output file. Paginate long pages (maxLength/startChar).
- Write the doc to the exact output path. Final message <=250 words: DEPTH-PASS or DEPTH-REJECT + path + one-line reason.

## Researcher 1 — Ryan McLeod

- Output file: `creators/Ryan-McLeod.md`
- Task prompt (send verbatim):
  > Depth-doc Ryan McLeod (Blackbox / Blackbox for Vision). Read `b0ttsagent/research/ui-design-workflows/working/evidence/ryan-mcleod-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: Apple Developer feature "Blackbox: Rebooting an inventive puzzle game for visionOS" (Jan 2024, his words — developer.apple.com/news/?id=gvesi4wr); his Medium @warpling design-process posts (Medium may 403 bot-block — use web archives or cached copies; note in Sources if so); GDC talks/interviews where HE describes his process (supplementary). Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Ryan-McLeod.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 2 — Max Stoiber

- Output file: `creators/Max-Stoiber.md`
- Task prompt (send verbatim):
  > Depth-doc Max Stoiber (styled-components). Read `b0ttsagent/research/ui-design-workflows/working/evidence/max-stoiber-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: mxstbr.com/thoughts (design-rationale posts incl. CSS-in-JS); blog posts/talks where HE describes his API/design process; interviews where he describes his own process (first-party statements). Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Judge the depth gate honestly: if his content is design rationale without an ordered process → DEPTH-REJECT with reason (this is a known risk for this designer). Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Max-Stoiber.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 3 — Jared Palmer

- Output file: `creators/Jared-Palmer.md`
- Task prompt (send verbatim):
  > Depth-doc Jared Palmer (Formik / Turborepo). Read `b0ttsagent/research/ui-design-workflows/working/evidence/jared-palmer-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: jaredpalmer.com/blog (Formik posts); his talks/interviews describing his own process; any design-process content from his time as a designer. Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Known risk (from Phase 1 flag): the doc lead is a single 2018 blog post — if no ordered first-party process exists beyond launch stories → DEPTH-REJECT with reason. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Jared-Palmer.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 4 — Charli Marie Prangley

- Output file: `creators/Charli-Marie-Prangley.md`
- Task prompt (send verbatim):
  > Depth-doc Charli Marie Prangley (Kit brand/marketing site design). Read `b0ttsagent/research/ui-design-workflows/working/evidence/charli-marie-prangley-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: charlimarie.com/blog; CharliMarieTV (YouTube — full design-process videos, e.g. designing a site start-to-finish); Inside Marketing Design podcast (she hosts — her process statements + her interviews of others); Marketing Design Dispatch newsletter. Read the process content end to end; extract her actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Charli-Marie-Prangley.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Completion criteria

- 4 `creators/<Name>.md` files exist, each with all 4 sections
- Every workflow step carries a source link
- Every DEPTH-REJECT carries a reason
- `working/waves/report-09.md` written

## QA checklist (lead)

- [ ] All 4 docs exist with all 4 sections present
- [ ] Every workflow step has a source link (step with no link → flag for re-run)
- [ ] "What Makes It Distinct" is not generic advice restated
- [ ] Every DEPTH-REJECT carries a reason
- [ ] Eligibility Evidence section has route + tier + window + currency line + product-type tag + craft/growth tag
- [ ] `report-09.md` has per-researcher status + DEPTH-PASS/REJECT counts + anomalies
