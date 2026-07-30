---
name: systems-architecture-builder
description: Build or rebuild a master Systems Architecture doc from a project's folder of system design docs — canonical system index with statuses, dependency DAG with execution waves, and an interface cross-reference table — drafted first from existing docs, then refined through targeted user questions. Use when the user wants to map out project systems, create or refresh a systems architecture doc, bootstrap design documentation ("session 0"), or when a system design-doc workflow needs the architecture doc and it is missing.
---

# Systems Architecture Builder

Builds the master `Systems Architecture.md` that the `system-design-doc-loop` skill depends on. **Draft-first**: infer from existing docs, then ask only about what inference couldn't resolve. Do not run a top-down interview — correcting a wrong draft is faster than dictating from scratch.

## Workflow

1. **Locate the docs folder.** Find the project's folder of system design docs (e.g. `Project Systems/`). Ask the user when ambiguous. The architecture doc defaults to `Systems Architecture.md` inside that folder.
2. **Read everything.** Read every system doc, including empty stubs and subfolders — even 1–7 line stubs imply dependencies.
3. **Draft the full architecture doc** using [architecture-template.md](architecture-template.md):
   - Infer dependencies from doc content: mentioning another system, shared currency/items, purchase/quest gating = dependency.
   - **Classify every dependency.** *Design-time definition deps* (X's design is defined in terms of Y's concepts) place waves and draw DAG edges. *Runtime API consumption* (X calls Y's API/events at runtime) goes in the interface table only — it never moves a wave and never draws an edge.
   - Group into execution waves: wave 0 = no dependencies; wave N depends only on waves < N.
   - Status every doc **Stub** (status tracks the design-doc loop, not content volume), unless the user says otherwise.
   - Build the diagrams per the template's embedded diagram rules, and route every `mermaid` block through the **mermaid-diagrams** skill's GitHub-Safe Dialect Rules checklist before presenting.
   - **Present the full draft to the user, then STOP and wait.** Do not write the file yet and do not treat the doc as finished.
4. **Ask 3–5 targeted questions — at least one round, never zero.** Focus on where inference was uncertain (unclear dependency direction, systems nothing references, wave conflicts). If inference resolved everything, ask the user to confirm DAG edges and wave placement instead — "inference felt certain" is not a reason to skip. Never re-ask what the docs already answer.
5. **User reviews the draft.** The DAG and wave placement are where the user's mental model matters most — expect corrections there.
6. **Revise until the user explicitly approves, then write the file.** This skill is complete only on explicit user approval of the architecture doc — producing the file is not completion.

## Bootstrap mode — empty or near-empty docs folder

If there are few or no docs to read, inference has no basis — **do not fabricate a draft.** Ask 5–8 scoping questions first (what systems exist, what each depends on, what must be designed first), then draft from the user's answers and follow the workflow from step 3.

## Refresh mode

If the architecture doc already exists and the user wants a rebuild: re-derive from current docs, but **preserve existing statuses** and previously user-corrected dependency info where docs haven't changed. Show a diff summary of what changed.

## Diagram & DAG rules (compressed)

Full rules with rationale live as HTML comments inside [architecture-template.md](architecture-template.md); this is the working summary:

- **Geometry:** linear chains → `flowchart TD`; fan-out DAGs → `flowchart LR`. Width is the scarce resource (narrow editor panes shrink wide diagrams to unreadable); height scrolls free.
- **Budgets:** max 15 nodes AND ~20 edges per diagram — ghost ref nodes count toward both. Edge count predicts hairball better than node count.
- **Split:** overview chips always; one detail diagram per wave. Merge adjacent waves when combined counts fit budget. A wave/merged group with < 2 edges gets no diagram — its wave-table row carries it. A single wave over budget splits at a natural theme boundary.
- **Arrows:** upstream → downstream everywhere (`A --> B` = "B depends on A"); the template preamble states the convention in prose.
- **Authority:** the wave table is the single source of truth — diagrams are regenerated from it, never hand-maintained. Before shipping, run the **edge-integrity check**: every edge must point lower-wave → higher-wave. A violation means a misclassified dependency or a real circular dependency — surface it to the user.

## Rules

- Content/data entries, strategy docs, and process/framework docs are NOT systems — exclude them from the index. Ask the user when a doc's category is ambiguous.
- The architecture doc is the single source of truth for system status. Never store status inside individual system docs.
- New systems discovered later (via the design-doc loop's stub-creation) are appended to the index with status Stub.

## Anti-Rationalization

Ignore these thoughts:

- "The draft looks plausible, so it's done."
- "No uncertainties found — skip the questions."
- "The parent skill is waiting — write the file quickly."
