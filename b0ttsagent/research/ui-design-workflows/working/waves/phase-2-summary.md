# Phase 2 Summary — ui-design-workflows depth docs (END QA)

- Research date: 2026-08-17
- Waves: 07–09 (3 depth-doc waves), all run to completion
- Goal: 12 full depth docs (floor 10) from the 12 verified PASS pool, in ranking order
- Result: **11 DEPTH-PASS / 1 DEPTH-REJECT (shadcn)**

## Phase gate

| Check | Result |
|-------|--------|
| 11 DEPTH-PASS docs on disk, all 4 sections + per-step source links | **PASS** — 11/11 have all 4 sections; every workflow subsection carries source links (steps grouped under subsection-level sources; intro paragraphs excluded) |
| shadcn DEPTH-REJECT record carries a reason | **PASS** — `creators/shadcn.md` carries verdict + reason: principles-only, no named ordered first-party workflow with ≥1 explicit quality gate/iteration loop; currency explicitly NOT the reason |
| Every Eligibility Evidence has route + tier + window + currency line + product-type tag + craft/growth tag | **PASS** — 12/12 files (incl. shadcn) verified via targeted scan |
| 11 >= floor 10 (target 10–12) — no replenishment needed | **PASS** — 11 delivered, no spares required |

**Phase 2 gate verdict: PASS. 11 DEPTH-PASS / 1 DEPTH-REJECT (shadcn).**

## Final deliverable set (11 designers)

1. **Adam Wathan** (Tailwind CSS / Tailwind UI) — component-kit workflow; "work in cycles" loop
2. **Mark Otto** (Bootstrap) — code-native design; abstraction-and-docs stage; dogfood gate
3. **Mike Bostock** (D3 / Observable) — design-as-search; prototype-hypothesis gate
4. **Lea Verou** (Prism.js / Color.js / Mavo) — North-Star-first framework; consensus + user-testing gates
5. **Steve Schoger** (Heroicons / Tailwind UI / Refactoring UI) — book-TOC workflow; "supercharge the defaults" gate
6. **Philipp Stollenmayer** (Kamibox) — "housewife test" gate; jazz-improvisation loop
7. **Curtis Herbert** (Slopes) — MVP lens, gut-check, future-self, 80%-polish gates
8. **Ryan McLeod** (Blackbox) — "observable change" test; anti-touch constraint; ship gate
9. **Max Stoiber** (styled-components) — taste workflow; "make it work/right/fast" gate
10. **Jared Palmer** (Formik / Turborepo / v0) — generative-UI loop + designer-era prototype loop; "no slop" gate
11. **Charli Marie Prangley** (Kit) — content-before-design; grey-box wireframes; "sleep on it" gate

## Depth-reject

- **shadcn** — DEPTH-REJECT (wave 07): first-party content is design *principles* and system specification only; no named, ordered design/build workflow with an explicit quality gate or iteration loop documented by the designer himself. Doc currency was fine (docs live 2026-08-17); the rejection is the absence of ordered process.

## Flags carried into Phase 3 synthesis

- **Prangley — weak revenue route.** T2 revenue via Kit's own newsroom + estimate-tracker only; no independent T1 press figure. Synthesis should lean on first-party process content, not the revenue route.
- **Palmer — thin sources.** Designer-era loop rests on Madrona/Latent Space interviews + the v0 launch post; the 2018 Phase-1 lead is one of few anchor docs. Treat depth claims that are single-anchor with caution.
- **Verou / Stoiber — credit framing.** Designer credentials are judgment calls (Verou: graphic-design background + standards roles; Stoiber: styled-components co-creator with Glen Maddern, Moxy claim unverified). Frame credits precisely in synthesis.
- **Doc-currency warnings.** Mark Otto blog stale since Jun 2024; Adam Wathan 2021 flagship post (product rebranded Tailwind Plus 2025); Ryan McLeod Medium recency UNKNOWN (bot-block). Cite current lineage where possible.
- **Em-dash encoding artifacts.** All 12 files are UTF-8 clean on disk (zero U+FFFD verified byte-level), but non-UTF-8 readers (PowerShell 5.1 default ANSI decode) display em-dash/arrow mojibake. Phase 3 must read files as UTF-8; files do not need fixing.
- **Bare-URL source style.** Inconsistent citation styles across docs: Ryan McLeod's 9 bare-label "Source: Going Indie transcript" refs (URL only in Sources), Curtis Herbert's bare parenthetical URLs, and "Source: same." cross-references in several docs. Links resolvable; normalize style during synthesis.

## Rejected candidates (verification phase, for INDEX.md)

- Karri Saarinen (tier3-only), Mike Kus (SOTM contradicted), Matt Perry (engineering credit), Tobias Ahlin Bjerrome (no public MAU), Zach Gage (finalist only), Michael Flarup (out-of-window self-claim), Sindre Sorhus (FAIL-UNKNOWN — recommend targeted re-run).
