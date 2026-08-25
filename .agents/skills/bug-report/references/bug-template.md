# Bug Document Template

Copy this structure when writing a bug document. Fill every section; use
`unknown` for any field the user could not answer — never guess, never auto-fill.

Filename: `YYYY-MM-DD-slug.md` (date = today; slug from the title). Lives in
`b0ttsagent/bugs/open/` until closed, then moves to `b0ttsagent/bugs/fixed/`.

The `id` equals the filename stem and never changes (including across the
open→fixed move). The registry line mirrors these fields.

```markdown
---
id: YYYY-MM-DD-slug
title: <short title>
severity: low | medium | high | critical | unknown
state: open
created_at: YYYY-MM-DD
---

# <title>

## Description
<1–3 sentences. What is broken, in plain language.>

## Expected vs Actual
- **Expected:** <what should happen>
- **Actual:** <what happens instead>

## Reproduction Steps
1. <step>
2. <step>
3. <step>

## Environment
<OS / runtime / version / config — or "unknown". Only what was reported; never guessed.>

## Impact
<Who/what is affected and how badly. Drives severity. Or "unknown".>

## Suspected Causes
<!-- Each investigation run appends a dated subsection here. Never edit an
     earlier subsection — the document is a trail of reasoning over time.
     Leave empty until Step 4. -->

### Investigation — YYYY-MM-DD
<!-- One block per suspected cause. Multiple causes allowed — keep less-obvious
     ones. Each cause string is mirrored in the registry causes[] array. -->

**Cause:** <one short string>
- **Confidence:** low | medium | high
- **Evidence:** `<file:line>` — <what it shows>
- **What would confirm this:** <the check or test that would verify this cause>

**Cause:** <…>
- **Confidence:** <…>
- **Evidence:** `<file:line>` — <…>
- **What would confirm this:** <…>

## Ruled Out & Open Questions
<!-- Filled only when an investigation is inconclusive. Each run appends a dated
     block. Leave empty if all causes are well-supported. -->

### As of YYYY-MM-DD
- **Ruled out:** <what this investigation checked and dismissed, or "nothing ruled out yet">
- **Open questions:** <what remains unresolved, or "none">
```

## How investigations append

- Step 4 appends **one** `### Investigation — YYYY-MM-DD` block under
  `## Suspected Causes` per run, and (if inconclusive) **one** `### As of
  YYYY-MM-DD` block under `## Ruled Out & Open Questions`.
- Never rewrite or reorder earlier blocks. The document is append-only
  reasoning over time.
- A new registry line is appended in the same step (same `id`, refreshed
  `updated_at`, updated `causes[]`). Registry lines are never edited either.
