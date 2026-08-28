---
name: system-design-doc-loop
description: Fill out a single system design doc through an interview loop — targeted questions, a structured draft (dependencies, interface, user-story flows, risks), feedback-driven revision, then architecture-doc updates — with on-the-fly stub creation for referenced systems, full-scope insertion of brand-new primary systems at sign-off, and a completeness checklist gating "done". Use when the user wants to work on, plan, or flesh out a specific system design doc (including systems not yet in the architecture index), asks which systems still need planning, or mentions the design-doc loop.
---

# System Design Doc Loop

Fills one system design doc at a time using [doc-template.md](doc-template.md). Requires `Systems Architecture.md` (built by the `systems-architecture-builder` skill).

## Step 0 — Preconditions

- Locate the project's system-design-docs folder and `Systems Architecture.md`.
- **If the architecture doc doesn't exist, STOP this loop.** Invoke the `systems-architecture-builder` skill and run it to completion — including its question and review rounds. Resume this loop only after the user has explicitly approved the architecture doc.
- Establish which system this loop is for (the user names it, or it's inferred from the request), then look it up in the architecture index:
  - **Found** → run the loop normally; the system is already tracked.
  - **Not found (new system)** → flag the loop as **new-system mode**. Do **not** create a stub or touch the architecture doc now — the full-scope insert happens at Done sign-off via the **New-system insert sub-routine**. Proceed with the loop; the system's wave, DAG edges, and interface are determined from the questions and draft.
- If the user asks "what still needs planning?": list every system with status Stub or In Progress from the architecture index. Done.

## The loop

1. Load `Systems Architecture.md` for DAG/interface context.
2. Ask **2–4 targeted questions** (default; adjust as needed) grounded in the system's DAG position — its dependencies, dependents, and wave. Don't ask what the architecture doc already answers.
3. User answers.
4. Propose a full draft of all 4 sections using [doc-template.md](doc-template.md). Any existing doc content goes **verbatim** under `## Original Notes`.
5. User gives feedback.
6. Ask clarifying questions about the feedback.
7. Revise the draft.
8. Repeat 5–7 until the user approves.
9. Run the **completeness checklist** below. On pass — and only with explicit user sign-off — write the doc file (if not already on disk), set status **Done**, and update `Systems Architecture.md`:
   - **Tracked system** (was in the index at Step 0) — update the existing index entry, DAG/wave, and interface cross-reference.
   - **New-system mode** — run the **New-system insert sub-routine** (full-scope insert: index row, wave placement, DAG edges, wave-table row, interface row, regenerated diagram, edge-integrity check).

## Stub-creation sub-routine

Triggers whenever drafting references a system with no doc or no index entry — during any of steps 2–8:

1. **Pause the loop.** Ask: "&lt;System&gt; has no doc. What notes/description do you want to leave for it?" The user may instead decide it isn't a real system — then fold it into the current doc.
2. Create the doc: full template with **empty sections** + the user's notes **verbatim** under `## Original Notes`.
3. Add it to the architecture index: name, one-liner derived from the notes, status **Stub**.
4. Resume the loop where it left off.

## New-system insert sub-routine

Runs at **Done sign-off** (step 9) when the loop was opened in **new-system mode** — the primary system had no architecture-index entry at Step 0. Distinct from the stub-creation sub-routine above (which handles *referenced* systems found mid-draft and creates stubs immediately); this one inserts the fully-designed primary system into the architecture doc all at once, end-only:

1. **Index row** — append to the System Index: name, one-liner (derived from the approved draft), status **Done**.
2. **Wave placement** — assign the wave from the design-time dependencies established during the loop: the lowest wave strictly greater than all its design-time dependencies' waves. Runtime-only API consumption never moves the wave.
3. **DAG edges** — add one edge per design-time dependency (`dependency --> this`), upstream → downstream. Runtime-only consumption adds no edge.
4. **Wave-table row** — add the system to its wave's row. The wave table is authoritative; diagrams are regenerated from it.
5. **Interface row** — add a row to the Interface Cross-Reference: Exposes / Consumes from the approved draft, tagging each Consumes entry as *design dep* or *runtime only*.
6. **Diagram regeneration** — invoke the **mermaid-diagrams** skill to regenerate **only the affected wave's detail diagram** from the wave table (never hand-edit). If the system creates a **brand-new wave**, also add its overview chip to the overview diagram. Follow the budget/dialect/edge rules embedded in `Systems Architecture.md` and the `systems-architecture-builder` skill. If regenerating would push the wave's diagram over budget (max 15 nodes / ~20 edges), **do not split it ad-hoc** — stop and tell the user to run a full `systems-architecture-builder` refresh instead.
7. **Edge-integrity check** — verify every edge in every diagram still points lower-wave → higher-wave. A violation means a misclassified dependency or a real circular dependency — surface it to the user, do not silently draw it.

## Completeness checklist — gates "Done"

- [ ] All 4 template sections filled (no empty placeholders)
- [ ] Every system named in Dependencies/Interface exists as a doc AND is in the architecture index
- [ ] Bidirectional consistency: if X lists "depended on by Y", Y's doc lists "depends on X"
- [ ] User Story has ≥1 numbered flow covering the primary player path (plus one flow per major alternate experience)
- [ ] Risks & Edge Cases has ≥2 entries, each with severity AND mitigation
- [ ] Architecture doc updated (index, DAG/wave, interface table)
- [ ] If **new-system mode**: affected wave's diagram regenerated via the **mermaid-diagrams** skill and edge-integrity check passed
- [ ] Explicit user sign-off on the final draft

## Rules

- `## Original Notes` is **verbatim always** — never edit, clean up, or reformat it. At Done sign-off the user may choose, per doc, to delete it. Never delete automatically.
- Status lives only in the architecture index — never inside system docs.
- User Story is **flows**, not prose: `### Flow N: <Name>`, numbered steps alternating player action / system response.
- Treat tunables (question counts, flow minimums) as defaults, not gospel — follow the user's lead in-session.
