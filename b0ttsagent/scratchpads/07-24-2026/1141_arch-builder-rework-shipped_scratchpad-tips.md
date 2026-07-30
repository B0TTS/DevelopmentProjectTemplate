# Scratchpad — Branch 4: Helpful Tips
**Session:** arch-builder-rework-shipped
**Date:** 07-24-2026 11:41

Dedup note: the user's decision-delegation preference is proposed in Branches 1 & 3 — excluded here per the dedup rule. Handoff-structure conventions are covered by the Branch 2 handoff-authoring skill proposal — excluded here.

## Categories identified
- decision-presentation-formats
- validation-tooling-gaps
- evidence-grounding-habits

## Extraction

### decision-presentation-formats
- Presenting the final design questions as a compact table (one row per property: recommendation | alternative, with a short "why" paragraph) got instant, unqualified approval ("yeah that works sounds good"). Context: the ghost-style + palette-ramp question bundled fill/text/stroke/label + 6 ramp hexes into one small table after the user asked to speed up. Reason: tables compress multi-property design decisions into one scannable approval unit — a quick-win format habit for any future design-decision presentation, inside or outside grill sessions.

### validation-tooling-gaps
- No mermaid syntax validation was possible this session: `npx @mermaid-js/mermaid-cli` pulls Puppeteer/Chromium, too heavy to run ad hoc, so verification was limited to grep/sed read-backs and pattern-matching against known-good diagrams. Context: explicit reasoning during the build phase ("skip; note manual verification instead"). Reason: the template and EXAMPLES.md now ship mermaid blocks that future sessions will copy and mutate — a one-time install of a local validator (global mermaid-cli, a VS Code mermaid linter task, or a small validate script in the repo) would let future diagram edits be machine-checked instead of eyeballed. Error-reduction tooling idea.

### evidence-grounding-habits
- Grepping the actual `classDef` lines from both real arc docs before asking the palette question turned an abstract taste question into a concrete comparison (real hexes, real contrast math) and made the recommendation defensible. Context: Q6.1 — the grep took one tool call and the user approved without pushback. Reason: cheap habit with outsized payoff for any design question about existing artifacts — pull the real values first, then ask. Adjacent to grill-me's existing "explore the codebase" rule but generalizes to all decision presentations, not just grill questions.

## Gleaning Pass

### decision-presentation-formats
- Re-checked both decision-presentation messages (Q6 options list, Q6.1 contrast argument, final batched table): the table-format item is the only presentation-format lesson. The options-list format for Q6 (a/b/c with rationale) also worked but is standard practice; not extracted separately.

### validation-tooling-gaps
- Re-checked the build and verification phase: the mermaid-validation gap is the only tooling gap encountered. Date/time lookup for file paths (bash `date`) was trivial and not a gap. No other missing tool was wished for during the session.

### evidence-grounding-habits
- Re-checked all three question/answer cycles: evidence-grounding happened once (palette) and is captured. Reading write-a-skill to check applicability was diligence, not an artifact-grounding decision; not a tip. No additional habit items qualify.

## Triple-check note
Not activated — gleaning confirmed non-empty categories with justifications.
