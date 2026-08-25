# Wave 08 — Phase 2: Depth Docs (wave 2 of 3)

- Phase: 2 (Depth docs)
- Goal: `creators/<Name>.md` for 4 verified designers (ranking #5-8), each passing the depth gate; DEPTH-REJECT allowed with reason
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
- Efficiency: if any search/read tool hangs or returns nothing twice in a row, switch tools and move on. Budget ~60 minutes of tool work; never stall without writing your output file. Paginate long pages (maxLength/startChar), don't pull whole books into context.
- Write the doc to the exact output path. Final message <=250 words: DEPTH-PASS or DEPTH-REJECT + path + one-line reason.

## Researcher 1 — Lea Verou

- Output file: `creators/Lea-Verou.md`
- Task prompt (send verbatim):
  > Depth-doc Lea Verou (Prism.js / Color.js / Mavo). Read `b0ttsagent/research/ui-design-workflows/working/evidence/lea-verou-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: lea.verou.me blog (API/UI design process posts), CSS Secrets (O'Reilly book — process-adjacent content), conference talks where SHE describes her design/API-design process (first-party statements). Read the process content end to end; extract her actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Frame her designer credentials precisely (graphic-design background + web standards design roles). If no ordered first-party process exists → DEPTH-REJECT with reason. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Lea-Verou.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 2 — Steve Schoger

- Output file: `creators/Steve-Schoger.md`
- Task prompt (send verbatim):
  > Depth-doc Steve Schoger (Heroicons / Tailwind UI / Refactoring UI). Read `b0ttsagent/research/ui-design-workflows/working/evidence/steve-schoger-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: Refactoring UI book + video walkthroughs (co-authored with Adam Wathan — joint first-party content, credit both); his X design-tip threads (synthesize into ordered steps, link each step to the specific post); YouTube UI breakdowns/redesign videos. Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop (e.g., his specific redesign decision rules). Beware: standalone tip threads alone are listicle-grade — the ordered process must come from the book/videos or systematic series. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Steve-Schoger.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 3 — Philipp Stollenmayer

- Output file: `creators/Philipp-Stollenmayer.md`
- Task prompt (send verbatim):
  > Depth-doc Philipp Stollenmayer / Kamibox (Song of Bloom, PBJ – The Musical, o k a y?). Read `b0ttsagent/research/ui-design-workflows/working/evidence/philipp-stollenmayer-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: kamibox.de/songofbloom-files (his own design documentation of how Song of Bloom was made); Apple's "Behind the Design" features (his words); any GDC/talk transcripts or interviews where HE describes his process; kamibox.de project pages. Read the process content end to end; extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop. Note language: verify English availability; German-only sources are acceptable if you translate carefully and link them. Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Philipp-Stollenmayer.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Researcher 4 — Curtis Herbert

- Output file: `creators/Curtis-Herbert.md`
- Task prompt (send verbatim):
  > Depth-doc Curtis Herbert (Slopes). Read `b0ttsagent/research/ui-design-workflows/working/evidence/curtis-herbert-2026-08-17.json` for eligibility facts (do not re-verify scale). First-party leads: Slopes Diaries series (blog.curtisherbert.com) — long-running build-in-public posts documenting design decisions and iterations; Apple "Behind the Design" (Slopes, his words); interviews where HE describes his process (supplementary). Read the process content end to end (paginate — the series is long); extract his actual named, ordered design workflow with >=1 explicit quality gate or iteration loop (his diaries document concrete v1→v2 iterations and decision tests). Every step source-linked. Write `b0ttsagent/research/ui-design-workflows/creators/Curtis-Herbert.md` per the 4-section schema. Final message <=250 words: DEPTH-PASS/DEPTH-REJECT + path + one-line reason.

## Completion criteria

- 4 `creators/<Name>.md` files exist, each with all 4 sections
- Every workflow step carries a source link
- Every DEPTH-REJECT carries a reason
- `working/waves/report-08.md` written

## QA checklist (lead)

- [ ] All 4 docs exist with all 4 sections present
- [ ] Every workflow step has a source link (step with no link → flag for re-run)
- [ ] "What Makes It Distinct" is not generic advice restated
- [ ] Every DEPTH-REJECT carries a reason
- [ ] Eligibility Evidence section has route + tier + window + currency line + product-type tag + craft/growth tag
- [ ] `report-08.md` has per-researcher status + DEPTH-PASS/REJECT counts + anomalies
