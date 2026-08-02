---
name: create-evergreen-note
description: Distill the current session's durable, reusable knowledge into one evergreen Markdown note filed in b0ttsagent/Notes/Evergreen/ and register it in index.jsonl. Use when the user explicitly says "save this as an evergreen note", "make a knowledge note from this", "this is worth keeping", or wants to capture a cross-session lesson as a long-lived note. NOT for session logs (use log-session), next-session handoffs (use handoff), reference docs for configured systems/services (use create-nav-guide), or throwaway/ephemeral notes.
license: MIT
disable-model-invocation: true
---

# Create Evergreen Note

Distill the **durable, reusable knowledge** from the current session into one evergreen Markdown note, then register it in a lightweight JSONL index so it stays findable across future sessions. This skill captures **cross-session knowledge**, not session memory.

`disable-model-invocation: true` — this skill never auto-loads. It fires only on explicit user intent (`/skill:create-evergreen-note` or a clear request like "save this as an evergreen note"). Evergreen notes are an intentional act, not a default.

## Boundary — read first

| If the content is… | Use this instead |
|---|---|
| What this session did | `log-session` |
| Instructions for the next session | `handoff` |
| A reference doc for a configured system/service | `create-nav-guide` |
| A throwaway / ephemeral scratch | none — just write it |
| Reusable knowledge answering "how do I handle X whenever it comes up" | **this skill** |

The rule: **session logs answer "what did I do today." Evergreen notes answer "how do I handle X whenever it comes up."** If the content does not pass the gate in step 1, stop and point the user at the right skill.

## Target locations

- Notes: `b0ttsagent/Notes/Evergreen/<kebab-case-name>.md`
- Index: `b0ttsagent/Notes/Evergreen/index.jsonl` (one JSON object per line, append-only)

Paths in the index are relative to the project root (e.g. `b0ttsagent/Notes/Evergreen/foo.md`), so they stay grep-friendly and portable.

## Scripts (in this skill's `scripts/` dir)

Resolve all script paths against this skill's directory (the parent of this SKILL.md).

- `add-note.js` — append one entry (JSON on stdin) to `index.jsonl`; assigns `id` automatically. **Called by the workflow below.**

No query script by design — for a small index, read or `grep` `index.jsonl` directly. Add one only if the index grows enough to matter.

## Workflow

1. **Gate: is this evergreen-worthy?** Apply the hardest test: *will this be reusable across at least three future sessions?* If no, stop and tell the user — suggest `log-session` for session memory or a plain file for ephemeral notes. Do not produce a note that will rot.

2. **Classify the task type.** Pick one (from the reader-task model in `references/evergreen-markdown-principles.md`):
   - `learn` — understand and later recall a concept
   - `decide` — choose between options
   - `do` — execute a procedure
   - `remember` — lookup reference facts

3. **Draft 3 title options** from the session. Present as a numbered list. **STOP and wait** for the user to pick one. Titles should be information-bearing (the note's actual subject), not vague ("Thoughts on notes").

4. **Pick the filename.** Kebab-case, descriptive, matches the title's subject. e.g. `structuring-roblox-retention-systems.md`. Do not date-prefix the filename — `date` lives in the index and the note footer.

5. **Read `references/evergreen-markdown-principles.md`.** It holds the research-backed rules for an evergreen-lifespan note. Apply them while writing — this is the load-bearing step.

6. **Write the note** to `b0ttsagent/Notes/Evergreen/<filename>.md` using the template below. Transform, do not transcribe: extract the reusable lesson, do not dump the session.

7. **Append to the index.** Assemble a JSON object (do **not** include `id` — the script assigns it):

   - `title` — the user's chosen title (string)
   - `date` — `YYYY-MM-DD` (today)
   - `file` — relative path to the note (string)
   - `taskType` — one of `learn` / `decide` / `do` / `remember`
   - `source` — optional: session id, handoff path, or short provenance (string, or omit for `null`)
   - `related` — optional: array of related note titles or ids (array of strings, or omit for `[]`)

   Pipe the JSON to the script via a **quoted heredoc** (`<<'EOF'`) so backticks/quotes are not interpreted. Run from the project root:

   ```bash
   node .agents/skills/create-evergreen-note/scripts/add-note.js <<'EOF'
   {
     "title": "<chosen title>",
     "date": "<YYYY-MM-DD>",
     "file": "b0ttsagent/Notes/Evergreen/<filename>.md",
     "taskType": "<learn|decide|do|remember>",
     "source": "<session id or handoff, or omit>",
     "related": ["<related note title or id>", "..."]
   }
   EOF
   ```

8. **Confirm.** The script prints the appended record (with its new `id`) and the file path. Show the user the final index entry and the note path.

## Note template

```markdown
# <Title>

> <One-sentence bottom line — the reusable answer, not the topic.>

**Task:** learn | decide | do | remember
**When to use:** <the situations this note applies to.>

## <Section heading phrased as the question it answers>

<Content. One meaningful question per section. Action before explanation.>

## <Next section>

<...>

## Sources

- <source link or citation, if research-derived>
- <...>

---
**Source:** <session id / handoff / date>
**Last reviewed:** <YYYY-MM-DD>
**Related:** <none | links to other evergreen notes>
```

Notes on the template:
- The opening `>` line is the inverted-pyramid bottom line — write the answer, not a description of the topic.
- Headings are a retrieval map; each should make sense in VS Code's Outline view alone.
- The footer is the **evergreen maintenance signal** (source traceability, related links, last-reviewed) — justified by the evergreen lifespan, not redundant metadata.
- Use semantic visuals (a table for comparisons, a diagram for flow/dependencies) only when they clarify. Never decorative.

## Checklist (copy into your reply, tick each)

- [ ] Passed the 3-session reuse gate
- [ ] taskType classified
- [ ] Title chosen from 3 options by the user
- [ ] Filename is kebab-case, no date prefix
- [ ] `references/evergreen-markdown-principles.md` read and applied
- [ ] Note has a bottom-line `>` line, retrieval-map headings, action-before-explanation
- [ ] Maintenance footer present (source, last-reviewed, related)
- [ ] Index entry appended; `id` printed and shown to user

## Evaluations

Test in a fresh session (skills load at start). Each scenario should fail or degrade without this skill and succeed with it.

1. **Reuse-gate rejection.** User says "save this as an evergreen note" after a session that only debugged a one-off config typo. Pass = the skill declines, explains the 3-session reuse test, and points to `log-session` or a plain file instead of producing a note.
2. **Research-derived guide (taskType = learn).** User asks to capture lessons from a research session (e.g. the markdown-writing research). Pass = note has a bottom-line `>` line, retrieval-map headings, evidence/interpretation layers, a `## Sources` section, and the maintenance footer; index entry appended with `taskType: learn` and a non-empty `source`.
3. **Procedure note (taskType = do).** User asks to save a reusable procedure. Pass = steps come before rationale, action is separated from explanation, headings are numbered/verb-led, and the index entry uses `taskType: do`.

For each: confirm the index line was appended (run `cat b0ttsagent/Notes/Evergreen/index.jsonl`), the `id` auto-incremented, and the note file exists at the path recorded in `file`.

## Notes

- Append-only. Never edit, reorder, or rewrite existing index lines. Surgical changes only.
- If `index.jsonl` does not exist, the script creates it (and its parent dir). Safe on a fresh clone.
- One note per invocation. If a session yields multiple distinct lessons, run the skill once per lesson — keep notes atomic.
- If the user asks to *update* an existing evergreen note, edit the `.md` file and update its `last-reviewed` date; do **not** append a duplicate index line.
