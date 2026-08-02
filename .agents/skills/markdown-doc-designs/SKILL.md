---
name: markdown-doc-designs
description: Apply a research-backed rubric to Markdown documents to improve psychological efficiency, scanability, evidence traceability, and visual restraint. Use when creating or writing any Markdown document (silently advises the writer before and during drafting — no report, no diff), OR when the user says "review this doc", "audit this markdown", "check this guide's readability", "is this note any good", or wants a quality pass on an existing personal note, practical guide, or research-derived document (produces a findings report and offers a diff). NOT for generating new documents from scratch (use the markdown notes generator), NOT for structural/syntax linting (use markdownlint), and NOT for enforcing a specific doc type's own conventions — CONTEXT.md, PLAN.md, nav guides, ADRs, system design docs defer to their owning skills for structure; this skill only adds the human-reader quality layer.
---

# Markdown Doc Designs

A research-backed human-reader quality layer for Markdown documents. The full rubric lives in `references/rubric.md`; this file carries the compact checklist used in auto mode and the workflow used in manual mode.

Primary render target: **VS Code Markdown Preview**. Prefer portable Markdown as the semantic core; treat renderer-specific polish (custom CSS, Mermaid, math) as optional and only when it materially aids comprehension. Do not recommend features that break in CommonMark/GitHub.

## Two modes

**Auto mode — silent advisory.** Fires when an agent is creating or writing any Markdown document. Before and while drafting, apply the pre-write checklist below. Do not produce a report. Do not show a diff to the user. The document just comes out better. Load `references/rubric.md` for substantial or research-derived docs; for quick/temp notes the checklist alone is enough.

**Manual mode — review report + offered diff.** Fires when the user asks to review an existing document. Read the document, evaluate it against `references/rubric.md`, produce a prioritized findings report, then offer to apply fixes as a diff the user approves.

## Auto-mode pre-write checklist

Apply this while writing any Markdown doc. Copy nothing to the user; just write the doc against it.

1. **Reader task** — learn, decide, do, remember, find, capture, or explain? Structure follows the task.
2. **Lifespan** — ephemeral, working, reference, or evergreen? Ceremony scales with lifespan.
3. **Top of doc** — purpose and the main answer/recommendation appear near the top, before sustained reading is required.
4. **Headings as a map** — every heading meaningful in isolation (VS Code Outline shows them). No "Thoughts" / "Misc" / "Important".
5. **One question per section** — each section answers one meaningful question.
6. **Action before explanation** — when the reader needs to act, give the action first, then the why.
7. **Semantic visuals** — table for compare, diagram for relationships/flow, callout for warnings/definitions/decisions/shortcuts/limitations, list for steps, prose for nuance. Never one medium for all jobs. No decorative visuals.
8. **Evidence layers** — in research-derived docs, keep source finding, interpretation, recommendation, personal adaptation, and uncertainty visibly separate.
9. **Restraint** — if everything is bold/callouted/boxed, signals lose contrast. Emphasize selectively.
10. **Earn its place** — every section and visual must improve understanding, retrieval, trust, decision, or action. Cut the rest.

For ephemeral/temp docs, items 1–2, 5, and 10 usually suffice — do not impose ceremony. That is the principle: match ceremony to lifespan, not to a universal template.

For substantial or research-derived docs, load `references/rubric.md` and apply the full rubric.

## Manual-mode review workflow

1. **Read the whole document** and note its type (personal note, practical guide, research-derived guide, CONTEXT, PLAN, nav guide, ADR, system design doc, handoff, other).
2. **Detect doc-type conventions.** If the doc is a type with an owning skill, do not flag its structural conventions as problems — that structure is the owning skill's job. Only evaluate the human-reader quality layer: scanability, evidence traceability, redundancy, visual restraint, actionability. See the deferral table below.
3. **Load `references/rubric.md`** and evaluate the doc against the principles and the reading-depth table.
4. **Produce a findings report** using the format below. Each finding cites its rubric principle and the evidence tier the principle rests on.
5. **Offer to apply fixes.** Do not edit until the user approves. Present the proposed edits (diff or summary) and wait.

### Findings report format

```markdown
# Review: <filename>

**Doc type:** <personal note | practical guide | research-derived guide | CONTEXT | PLAN | nav guide | ADR | system design doc | handoff | other>
**Reader task:** <learn | decide | do | remember | find | capture | explain>
**Lifespan:** <ephemeral | working | reference | evergreen>

## Findings

### [Blocker] <one-line problem>
- **Principle:** <rubric principle name>
- **Evidence:** <Tier 1 | Tier 2 | Tier 3 | Tier 4>
- **Where:** <heading or line>
- **Fix:** <concrete suggested change>

### [Major] ...

### [Minor] ...

### [Nitpick] ...

## Summary
- <n> blocker(s), <n> major, <n> minor, <n> nitpick
- Top 3 to fix first: ...

## Offer
Apply fixes? (I'll show the diff before writing.)
```

### Severity definitions

- **Blocker** — the doc fails its primary reader task: purpose never stated, action buried, evidence presented as fact when it is interpretation, or structure blocks scanning.
- **Major** — the doc works but a section or visual significantly degrades comprehension, retrieval, or trust; or it violates a Tier 1/2-backed principle.
- **Minor** — readability or restraint issue; low-cost to fix; Tier 3-backed.
- **Nitpick** — style or preference; Tier 4 or no evidence; fix only if cheap.

When two findings conflict (e.g. "add a callout for the warning" vs "too many callouts"), resolve toward the reader task and the strongest evidence tier — not toward adding or removing decoration in isolation.

## Doc-type deferral table

If the doc is a type with an owning skill, defer structure to that skill and evaluate only the human-reader layer.

| If the doc is... | Defer structure to... | You evaluate... |
|---|---|---|
| CONTEXT.md | create-context-doc | human-reader layer only |
| PLAN.md | create-execution-plan | human-reader layer only |
| Nav guide | create-nav-guide | human-reader layer only |
| ADR | write-adr (or current equivalent) | human-reader layer only |
| System design doc | system-design-doc-loop | human-reader layer only |
| Handoff | handoff skill conventions | human-reader layer only |
| Session log / scratchpad | close / log-session conventions | human-reader layer only |
| Personal note / practical guide / research-derived guide | no owning skill | full rubric |

If a doc has no owning skill, evaluate the full rubric.

## Evidence tiers (cited in findings)

Briefly cite the tier each principle rests on. Full definitions and source links are in `references/rubric.md`.

- **Tier 1** — systematic reviews, meta-analyses, established cognitive theory
- **Tier 2** — individual peer-reviewed studies
- **Tier 3** — applied usability / information-architecture research, mature tool docs
- **Tier 4** — popular practice, community convention (carry less weight; do not let these override stronger evidence)

## What this skill never does

- Generate a new document from scratch — that is the markdown notes generator's job.
- Structural or syntax linting — that is markdownlint's job.
- Enforce a doc type's own conventions — that is the owning skill's job.
- In auto mode: produce a report, show a diff, or surface anything to the user.
- In manual mode: edit before the user approves.
- Recommend decorative visual features that harm comprehension or rendering portability.
- Run external linters or assume installed tools.

## Evaluations

Run these in fresh sessions to validate the skill loads and behaves. Each is a scenario that should fail without this skill.

1. **Auto mode on a quick temp note.** An agent is asked to "jot a quick temp note about today's friction." Without the skill: a wall of prose. With it: purpose at top, lifespan-ephemeral means minimal ceremony, headings meaningful. Expect no report or diff to the user.
2. **Manual mode on a research-derived guide.** The user says "review this video-making guide" where the doc transcribes source material verbatim. Without the skill: a vague "looks good." With it: a findings report flagging missing evidence/interpretation separation (Blocker, Tier 2), buried action (Major, Tier 3), decorative callout overuse (Minor, Tier 1 signaling principle), plus an offered diff — and no edit before approval.
3. **Manual mode on a CONTEXT.md.** The user says "review my CONTEXT.md." Without the skill: flags the doc's structure as wrong. With it: defers CONTEXT structure to create-context-doc and only reports human-reader-layer findings (e.g. headings not meaningful in isolation, purpose not near top).
