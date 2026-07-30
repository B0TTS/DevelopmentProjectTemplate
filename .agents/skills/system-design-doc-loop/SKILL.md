---
name: system-design-doc-loop
description: Fill out a single system design doc through an interview loop — targeted questions, a structured draft (dependencies, interface, user-story flows, risks), feedback-driven revision, then architecture-doc updates — with on-the-fly stub creation for referenced systems and a completeness checklist gating "done". Use when the user wants to work on, plan, or flesh out a specific system design doc, asks which systems still need planning, or mentions the design-doc loop.
---

# System Design Doc Loop

Fills one system design doc at a time using [doc-template.md](doc-template.md). Requires `Systems Architecture.md` (built by the `systems-architecture-builder` skill).

## Step 0 — Preconditions

- Locate the project's system-design-docs folder and `Systems Architecture.md`.
- **If the architecture doc doesn't exist, STOP this loop.** Invoke the `systems-architecture-builder` skill and run it to completion — including its question and review rounds. Resume this loop only after the user has explicitly approved the architecture doc.
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
9. Run the **completeness checklist** below. On pass — and only with explicit user sign-off — set status **Done** and update `Systems Architecture.md` (index entry, DAG/wave, interface cross-reference).

## Stub-creation sub-routine

Triggers whenever drafting references a system with no doc or no index entry — during any of steps 2–8:

1. **Pause the loop.** Ask: "&lt;System&gt; has no doc. What notes/description do you want to leave for it?" The user may instead decide it isn't a real system — then fold it into the current doc.
2. Create the doc: full template with **empty sections** + the user's notes **verbatim** under `## Original Notes`.
3. Add it to the architecture index: name, one-liner derived from the notes, status **Stub**.
4. Resume the loop where it left off.

## Completeness checklist — gates "Done"

- [ ] All 4 template sections filled (no empty placeholders)
- [ ] Every system named in Dependencies/Interface exists as a doc AND is in the architecture index
- [ ] Bidirectional consistency: if X lists "depended on by Y", Y's doc lists "depends on X"
- [ ] User Story has ≥1 numbered flow covering the primary player path (plus one flow per major alternate experience)
- [ ] Risks & Edge Cases has ≥2 entries, each with severity AND mitigation
- [ ] Architecture doc updated (index, DAG/wave, interface table)
- [ ] Explicit user sign-off on the final draft

## Rules

- `## Original Notes` is **verbatim always** — never edit, clean up, or reformat it. At Done sign-off the user may choose, per doc, to delete it. Never delete automatically.
- Status lives only in the architecture index — never inside system docs.
- User Story is **flows**, not prose: `### Flow N: <Name>`, numbered steps alternating player action / system response.
- Treat tunables (question counts, flow minimums) as defaults, not gospel — follow the user's lead in-session.
