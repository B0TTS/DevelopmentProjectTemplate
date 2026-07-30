# Mermaid-Diagram Skill Integration Gap

## Summary

The `systems-architecture-builder` skill emits mermaid diagrams without routing them through the `mermaid-diagrams` skill — despite the mermaid-diagrams skill explicitly requiring this (trigger #3: "Template hand-off"). This was discovered when a user asked to redesign the DAG in an existing Systems Architecture.md. Applying the mermaid-diagrams skill's rules to the same data produced a substantially better result, confirming the gap is real and the fix is warranted.

## What Was Accomplished

### Redesigned the Systems Architecture DAG

**File:** `C:\Development\GameProjects\Whack Grass\Design Docs Testing V2\Main\Project Systems\Systems Architecture.md`

**Before:** One monolithic `graph TD` diagram with 29 nodes crammed into 4 subgraphs — nearly 2× the mermaid-diagrams skill's 15-node budget. No colors, unquoted labels risking bracket collisions, no classDef styling.

**After:** Four split diagrams, each under 15 nodes:

| Diagram | Nodes | Purpose |
|---|---|---|
| Overview | 4 | Wave-level DAG (W0 → W1 → W2 → W3) with green/blue/amber/purple color progression |
| Wave 0 Detail | 9 | Foundation systems + internal `Teleporting → Areas` edge |
| Wave 1 Detail | 14 (10 + 4 refs) | Item/mechanic systems with gray ghost nodes for Wave 0 dependencies |
| Wave 2–3 Detail | 13 (9 + 4 refs) | Meta systems + Trading Plaza with gray ghost nodes for Wave 0/1 dependencies |

All diagrams use `flowchart TD`, double-quoted labels, `classDef`-based color palette, and no YAML frontmatter (stripped after hitting GitHub/VS Code parser errors).

### Fixed mermaid-diagrams REFERENCE.md

**File:** `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\REFERENCE.md`

Added a compatibility note above the YAML frontmatter example in the Flowchart section, flagging that `---` config blocks require Mermaid ≥ v10.8 and are not supported by GitHub/VS Code bundled renderers. Two safe fallbacks documented: `%%{init}%%` directive, or skipping config when `classDef` already handles styling.

## Root Cause: The Integration Gap

The `systems-architecture-builder` skill never invokes the `mermaid-diagrams` skill, at two levels:

1. **Template (`architecture-template.md`):** ships this bare scaffold:
   ```
   ```mermaid
   graph TD
       A[System A] --> B[System B]
   ```
   ```
   No classDef, no color palette, no double-quoted labels, no node budget guardrail. The diagram-construction skill's rules are completely absent.

2. **Skill instructions (`SKILL.md`):** the workflow says "Draft the full architecture doc using architecture-template.md" but never mentions the mermaid-diagrams skill — neither as a prerequisite read nor as a routing rule when writing the mermaid block.

Meanwhile, the mermaid-diagrams skill's **proactive trigger #3** says:
> "Template hand-off: you are filling in or extending a `mermaid` block that another skill's template ships (e.g. the `graph TD` scaffold in `systems-architecture-builder/architecture-template.md`). The parent skill's template does NOT satisfy this skill's safety rules — always route the diagram through this skill."

The trigger already anticipates this exact scenario, but it's a *passive* instruction aimed at the agent. The architecture-builder skill itself has no *active* reference or invocation rule, so an agent following it narrowly (reading the template, filling in the scaffold) will skip the mermaid-diagrams skill entirely.

## Open Decisions

1. **How should architecture-template.md change?** Options:
   - Replace the bare scaffold with the split-diagram structure (overview + wave details) as the new default template
   - Keep the bare scaffold but add a comment directing the agent to the mermaid-diagrams skill
   - Remove the mermaid block from the template entirely and replace with a placeholder like `<!-- ROUTE THROUGH mermaid-diagrams SKILL -->`

2. **How should the architecture-builder SKILL.md enforce routing?** Options:
   - Add a rule: "When writing the mermaid block, invoke the mermaid-diagrams skill and apply its GitHub-Safe Dialect Rules checklist"
   - Add to the workflow step 3: "Draft the mermaid diagram using the mermaid-diagrams skill's rules before presenting"

3. **Is the mermaid-diagrams skill's trigger #3 sufficient?** It currently relies on the agent noticing it applies. Should it be upgraded to a hard rule ("Never write a mermaid block from another skill's template without running the checklist") or is the current passive phrasing adequate when the parent skill also references it?

## Suggested Skills for Next Session

- **`systems-architecture-builder`** — to read current state and apply the fix
- **`mermaid-diagrams`** — reference for the rules that need to be enforced
- **`write-a-skill`** — if structural changes to either skill are needed beyond inline edits

## Key Files

| File | Role |
|---|---|
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\systems-architecture-builder\SKILL.md` | Skill that needs a routing rule added |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\systems-architecture-builder\architecture-template.md` | Template whose bare mermaid scaffold needs updating |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\SKILL.md` | Skill whose rules were applied in the redesign; trigger #3 references this gap |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\mermaid-diagrams\REFERENCE.md` | Updated with YAML frontmatter compatibility note |
| `C:\Development\GameProjects\Whack Grass\Design Docs Testing V2\Main\Project Systems\Systems Architecture.md` | The doc that received the redesigned diagrams (before/after evidence) |

## Evidence: Before vs. After

The redesign demonstrated measurable improvement from routing through the mermaid-diagrams skill:

- **Render safety:** unquoted `[Brackets]` → all `["double-quoted"]`
- **Budget compliance:** 29 nodes (over) → max 14 per diagram (under 15)
- **Visual hierarchy:** monochrome → 4-color semantic palette distinguishing execution waves
- **Cross-wave clarity:** all deps crammed into one graph → ghost ref nodes in each detail diagram make dependencies locally readable without scrolling across a 29-node tangle
- **Parser compatibility:** YAML `---` config blocks that break on GitHub/VS Code → stripped, with `classDef` carrying all styling
