# Evergreen Markdown Principles

Research-backed rules for writing an **evergreen-lifespan** note — a long-lived, reusable knowledge document the reader returns to across many sessions. Distilled from the project's Markdown document-writing research findings. Read this before writing the note; apply it while writing.

This file is one level deep from `SKILL.md`. Do not chain further.

## Contents

1. [What "evergreen" means](#what-evergreen-means)
2. [Start with the reader's task](#start-with-the-readers-task)
3. [Put the bottom line near the top](#put-the-bottom-line-near-the-top)
4. [Headings are a retrieval map](#headings-are-a-retrieval-map)
5. [One question per section](#one-question-per-section)
6. [Separate action from explanation](#separate-action-from-explanation)
7. [Layer evidence and interpretation](#layer-evidence-and-interpretation)
8. [Remove what does not earn its place](#remove-what-does-not-earn-its-place)
9. [Use visual elements semantically](#use-visual-elements-semantically)
10. [Design for multiple reading depths](#design-for-multiple-reading-depths)
11. [Transform, do not transcribe](#transform-do-not-transcribe)
12. [Carry the evergreen maintenance signals](#carry-the-evergreen-maintenance-signals)

---

## What "evergreen" means

Evergreen is a document lifespan class, not a folder. It means: **the reader expects to revisit and reuse this across many future sessions.** That expectation earns the extra structure below — source traceability, related links, a maintenance footer, and carefully chosen visual structure. A throwaway note should carry none of this; an evergreen note should carry all of it.

Optimize for: stable headings, searchable terms, examples, retrieval aids, maintenance signals, clear scope.

## Start with the reader's task

Identify which task the note serves — the same subject may need a different note depending on the task:

- `learn` — understand and later recall a concept
- `decide` — choose between options
- `do` — execute a procedure
- `remember` — look up reference facts

State the task and "when to use" near the top. It orients the reader and forces the note to stay scoped.

## Put the bottom line near the top

Readers scan before they commit to deep reading. Reveal the practical answer before the background. The opening `>` line should give the reusable answer, not describe the topic.

Good: `> Use a table when the reader is comparing options across the same fields.`
Bad:  `> This note is about tables in Markdown.`

State the conclusion first when the reader needs a decision; background comes after.

## Headings are a retrieval map

Headings communicate what a section contains, not that a section exists. A reader viewing VS Code's Outline should understand the note's structure without opening every section.

Prefer:

```
## Choose the recording format
## When this framework fails
## Three steps for the opening
```

Over:

```
## Thoughts
## More information
## Important
```

The first words of a heading matter — readers may see only a slice while scanning. Begin headings with the information-bearing phrase.

Test each heading: *if I saw only this heading in an outline, would I know what I would find there?*

## One question per section

Each section should answer one meaningful question:

- What is this?
- Why does it matter?
- How do I use it?
- When should I use it?
- When should I avoid it?
- What are the tradeoffs?
- What should I do next?

If a section answers three unrelated questions, split it.

## Separate action from explanation

Do not bury a procedure inside theory. Present the action first when the reader needs to act, then explain why it works. For a `do` note, the steps come before the rationale. For a `learn` note, the explanation may lead — but the "how to apply it" still belongs in its own section, not buried in prose.

## Layer evidence and interpretation

For research-derived notes, keep these layers distinct so the reader can tell what is known from what is being recommended:

1. **Source finding** — what the evidence says
2. **Interpretation** — what it means in general
3. **Personal recommendation** — what to do, for this reader
4. **Personal adaptation** — how to tailor it
5. **Uncertainty** — where the evidence is weak or conditions-dependent
6. **Open question** — what remains unresolved

Do not let a confident-sounding recommendation exceed the evidence. Put caveats next to the claim they qualify.

## Remove what does not earn its place

Ask of each section, list, and visual:

> Does this improve understanding, retrieval, trust, decision-making, or action?

If not, it is research residue, repetition, or decoration. Do not repeat the same message in the title, intro, callout, and conclusion unless each repetition serves a different retrieval or action purpose.

Concision and objectivity reduce reader work. Remove throat-clearing. Use precise verbs and concrete nouns. Avoid inflated claims ("the ultimate," "revolutionary") unless clearly framed as personal opinion.

## Use visual elements semantically

Pick the medium by the job:

| Element | Use for |
|---|---|
| Table | comparisons across the same fields |
| Diagram | sequence, dependencies, branching, relationships |
| Callout | warnings, definitions, decisions, shortcuts, limitations |
| List | discrete items or ordered steps |
| Prose | reasoning and nuance |

Do not use one medium for all jobs. Do not add a diagram to look advanced — a decorative visual merely fills space. Signaling works through **selective** emphasis; if everything is bold or boxed, the signals lose contrast.

## Design for multiple reading depths

A strong note supports:

| Depth | Reader need |
|---|---|
| Glance | identify purpose and main answer |
| Scan | find headings, keywords, and actions |
| Normal read | understand the explanation |
| Deep read | inspect rationale, sources, limitations |
| Action | follow a clear next step |

The bottom-line `>` line serves glance. Headings serve scan. Body serves normal/deep read. A clear action or next-step serves action.

## Transform, do not transcribe

The note should transform information, not transcribe the session. Move through:

```
Session output
 → interpretation (what does it mean for me?)
 → personal relevance (when will I hit this again?)
 → recommended action or reusable rule
 → retrieval-friendly structure
```

A dump of what happened in the session is a session log, not an evergreen note. If the content answers "what did I do today," it belongs in `log-session`, not here.

## Carry the evergreen maintenance signals

Because the note is meant to be revisited, it carries a maintenance footer — this is what distinguishes it from an ephemeral note and is justified by the lifespan, not redundant:

- **Source** — where this came from (session id, handoff, date, or citations)
- **Last reviewed** — `YYYY-MM-DD` of last review/update
- **Related** — links to other evergreen notes, or `none`

Add a `## Sources` section near the end for any research-derived note, listing source links or citations. This preserves traceability without cluttering the main body.
