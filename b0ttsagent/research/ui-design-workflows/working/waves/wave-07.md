# Wave 07 — Phase 2: Depth Docs (wave 1 of 3)

- Phase: 2 (Depth docs)
- Goal: `creators/<Name>.md` for 4 verified designers, each passing the depth gate; DEPTH-REJECT allowed with reason
- Research date: 2026-08-17
- Roster: 4 researchers, one designer each, parallel fanout, in ranking order (strongest verification first)
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
- Efficiency: if any search/read tool hangs or returns nothing twice in a row, switch tools and move on. Budget ~60 minutes of tool work; never stall without writing your output file. Paginate long pages (maxLength/startChar), don't pull whole books into context.
- Write the doc to the exact output path. Final message <=250 words: DEPTH-PASS or DEPTH-REJECT + path + one-line reason.

## Researcher 1 — Adam Wathan

- Output file: `creators/Adam-Wathan.md`
- Task prompt (send verbatim):
  > Depth-doc Adam Wathan (Tailwind CSS / Tailwind UI). Read `b0ttsagent/research/ui-design-workflows/working/evidence/adam-wathan-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: adamwathan.me blog; tailwindcss.com/blog design posts (e.g. "Designing Tailwind UI Ecommerce"); Refactoring UI book/videos (co-authored with Steve Schoger — joint first-party content is fine, credit both). Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop (e.g., his "build the ugly version first / design in cycles" ideas, decision loops). Apply the depth gate from the wave spec — listicle-only or case-study-only content → DEPTH-REJECT. Every step source-linked to the exact first-party location. Write `b0ttsagent/research/ui-design-workflows/creators/Adam-Wathan.md` per the 4-section schema in the wave spec. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 2 — Mark Otto

- Output file: `creators/Mark-Otto.md`
- Task prompt (send verbatim):
  > Depth-doc Mark Otto (Bootstrap). Read `b0ttsagent/research/ui-design-workflows/working/evidence/mark-otto-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: markdotto.com blog (design deep-dives: "Designing Bootstrap", GitHub UI design posts); talks ("Designing Bootstrap" conference talk). Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Apply the depth gate from the wave spec — listicle-only or case-study-only content → DEPTH-REJECT. Every step source-linked. Note: his blog went quiet ~Jun 2024 — record the doc-currency line honestly in Eligibility Evidence. Write `b0ttsagent/research/ui-design-workflows/creators/Mark-Otto.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 3 — Mike Bostock

- Output file: `creators/Mike-Bostock.md`
- Task prompt (send verbatim):
  > Depth-doc Mike Bostock (D3.js / Observable). Read `b0ttsagent/research/ui-design-workflows/working/evidence/mike-bostock-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: bost.ocks.org/mike essays (e.g. "Object Constancy", "Thinking with Joins", "Towards Reusable Charts", "Visualizing Algorithms", "How to Infer Topology"); Observable notebooks where he documents his design/refinement process. Read the process content end to end; extract his actual named, ordered design workflow (his essays describe explicit iteration/refinement loops — v1→v2→v3 comparisons) with >=1 explicit quality gate. Apply the depth gate from the wave spec. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Mike-Bostock.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 4 — shadcn

- Output file: `creators/shadcn.md`
- Task prompt (send verbatim):
  > Depth-doc shadcn (shadcn/ui). Read `b0ttsagent/research/ui-design-workflows/working/evidence/shadcn-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: ui.shadcn.com/docs (design principles — "Beautiful Defaults", design philosophy pages); shadcn.com blog/talks if any; his X posts and interviews where HE describes his process (interviews with him are first-party statements). Read the process content end to end; extract his actual named, ordered design/build workflow with >=1 explicit quality gate or iteration loop. Apply the depth gate from the wave spec — if it's only principles without ordered process → DEPTH-REJECT with reason. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/shadcn.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Completion criteria

- 4 `creators/<Name>.md` files exist, each with all 4 sections
- Every workflow step carries a source link
- Every DEPTH-REJECT carries a reason
- `working/waves/report-07.md` written

## QA checklist (lead)

- [ ] All 4 docs exist with all 4 sections present
- [ ] Every workflow step has a source link (step with no link → flag for re-run)
- [ ] "What Makes It Distinct" is not generic advice restated
- [ ] Every DEPTH-REJECT carries a reason
- [ ] Eligibility Evidence section has route + tier + window + currency line + product-type tag + craft/growth tag
- [ ] `report-07.md` has per-researcher status + DEPTH-PASS/REJECT counts + anomalies
