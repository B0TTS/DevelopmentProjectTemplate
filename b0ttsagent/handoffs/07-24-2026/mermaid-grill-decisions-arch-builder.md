# Mermaid Grill Decisions — Systems Architecture Builder Rework

## Summary

Follow-up to [mermaid-diagram-skill-integration-gap.md](mermaid-diagram-skill-integration-gap.md) (same folder — read it first for root-cause context). This session analyzed both original arc docs, then ran a `grill-me` session to lock design decisions for the rework. **Scope decision by user: improvements go mainly into `systems-architecture-builder`; `mermaid-diagrams` stays use-case-generic** (it's used for non-game-design docs too) — only generic rules may be added there.

### Arc doc findings (evidence base)

- **Deepseek doc confirmed the "before" state**: 28 nodes in 4 subgraphs under one `graph TD`, no styling, unquoted labels. Root cause was the template's bare scaffold + subgraph-based wave grouping fighting dagre.
- **GLM doc used the opposite arrow convention** from the handoff redesign (upstream→downstream vs depends-on), and was the only doc that documented its convention in prose. The redesign was internally inconsistent: overview chips used progression semantics, detail diagrams used depends-on.
- **The two docs diverge on modeling, not just rendering** (Grass Spawning W0 vs W1; Areas W0 vs W4; "Grass" catalog system included vs excluded). Root cause: the builder skill has no dependency-classification rule (design-time definition dep vs runtime API consumption). Until canonized, every rebuild produces a different DAG.
- **GLM doc's "How to read this doc" preamble and "Excluded from the index" section are excellent** and exist in neither the template nor the redesign — adopt both.
- **Live bug in mermaid-diagrams**: EXAMPLES.md templates #1 and #2 still ship `---` YAML config blocks — contradicts the REFERENCE.md compatibility fix from the prior session.

### User's reading context (drives all geometry decisions)

User reads docs in **VS Code split view** (source + preview); preview pane is ~600–900px wide. Mermaid SVGs scale to container width (`max-width: 100%`), so wide diagrams shrink to unreadable text; tall diagrams scroll for free. **Width is the scarce resource, height is free.**

## Locked Decisions (grill Q1–Q5)

| # | Decision | Rationale |
|---|---|---|
| Q1 | **Optimize diagrams for split-view narrow panes.** Tall-over-wide is a hard rule. | Wide = scaled down; tall = scrolls. Narrow-optimized diagrams still work full-width; not vice versa. |
| Q2 | **`flowchart LR` default for dependency/wave DAGs; `TD` only for linear chains** (overview chips). Rule: "chains go TD, DAGs go LR." | Under TD, fan-out ranks become wide rows. Under LR they become tall columns that scroll free. |
| Q3 | **Budgets: max 15 nodes AND ~20 edges per diagram. No per-rank cap** (dead under LR). Ghost ref nodes count toward both budgets. | Edge count predicts hairball better than node count — the Deepseek monolith (28n/27e) fails both; the redesign's wave details (≤14n/14e) pass both. |
| Q4 | **Rule-based split:** overview chips always; one detail diagram per wave; **merge** adjacent waves when combined ≤ budgets; **degenerate rule** — wave/merged group with < 2 edges gets no diagram (wave table row carries it); **escape hatch** — a single wave over budget splits at a natural theme boundary. | Mechanical rules → consistent output across models/rebuilds. Kills the redesign's pointless 9-node/1-edge Wave 0 diagram. Ghost nodes only appear in non-degenerate diagrams (nice emergent property). |
| Q5 | **Arrow semantics: upstream → downstream everywhere** (`A --> B` means "B depends on A"), with a mandatory one-line convention statement in the template preamble. | Only option where overview, details, LR geometry (foundation left, dependents right), and reading direction all agree. GLM doc proved it. |

## Open Decisions

- **Q6 (asked, unanswered): template structure.** My recommendation on record: **(a) full worked skeleton** in `architecture-template.md` — agents imitate template examples, not skill prose (the bare `graph TD` scaffold is what produced the Deepseek monolith). Skeleton = GLM-style preamble (waves = design order, arrow convention, runtime ≠ design dep) + TD overview example + LR wave-detail example with 1–2 ghost nodes + canonized palette + wave/interface tables + "Excluded from the index" section + HTML comments embedding the mechanical rules (budgets, merge, degenerate). Sub-decisions recommended (user may veto): pastel sequential ramp with dark text (GLM-style, e.g. `#b6d7a8`/`#a4c2f4`/`#ffe599`/`#d9d9d9`, extend for ≥5 waves) over saturated fills + white text; ghost style = light gray fill `#e2e8f0`, **dashed** gray stroke, dark gray text, label format `"Name<br/>(W0)"`.

## Implementation Plan (next session)

1. **Finish Q6** (quick confirm of the recommendation above, then build).
2. **`architecture-template.md`** — rework per Q6 outcome.
3. **`systems-architecture-builder/SKILL.md`** — add: (a) routing rule ("mermaid blocks MUST follow the mermaid-diagrams checklist"); (b) compressed split rules from Q2–Q5; (c) **dependency-classification rule** — design-time definition deps place waves; runtime API consumption does not (fixes the arc-doc modeling divergence).
4. **`mermaid-diagrams` (generic edits only, per user scope):** tall-over-wide line; edge-budget line; arrow-semantics rule (state convention in prose, keep consistent); palette-mapping guidance (ordinal data → sequential ramp); **fix EXAMPLES.md YAML frontmatter in templates #1 and #2** (live bug — breaks GitHub/VS Code per REFERENCE.md).
5. **Optional:** edge-audit step in the builder workflow — every interface-table "Consumes" entry ↔ DAG edge consistency check; declare the wave table authoritative so diagrams can be regenerated rather than hand-maintained.

## Suggested Skills for Next Session

- **`systems-architecture-builder`** — primary edit target
- **`mermaid-diagrams`** — secondary edit target (generic rules only)
- **`write-a-skill`** — if structural changes exceed inline edits
- **`grill-me`** — to close out Q6

## Key Files

| File | Role |
|---|---|
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\systems-architecture-builder\SKILL.md` | Needs routing rule, split rules, dependency-classification rule |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\systems-architecture-builder\architecture-template.md` | Primary rework target (bare `graph TD` scaffold = root cause) |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\SKILL.md` | Add generic lines only (tall-over-wide, edge budget, arrow semantics, palette mapping) |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\EXAMPLES.md` | **Live bug**: YAML frontmatter in templates #1 & #2 must be removed/replaced |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\REFERENCE.md` | Already fixed prior session (frontmatter compat note) — EXAMPLES.md must match it |
| `C:\Development\GameProjects\Whack Grass\Design Docs Skill Testing\Arc Docs\Testing V2 Run\Systems Architectureglm5-2.md` | GLM arc doc — source of the preamble, arrow convention, "Excluded" section to adopt |
| `C:\Development\GameProjects\Whack Grass\Design Docs Skill Testing\Arc Docs\Testing V2 Run\Systems Architecture Deepseekv4pro.md` | Deepseek arc doc — the "before" evidence (28-node subgraph monolith) |
| `C:\Development\GameProjects\Whack Grass\Design Docs Testing V2\Main\Project Systems\Systems Architecture.md` | Handoff-redesigned doc — split-pattern reference (minus its Wave 0 degenerate diagram) |
