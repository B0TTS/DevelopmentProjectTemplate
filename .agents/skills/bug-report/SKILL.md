---
name: bug-report
description: Turn a spoken bug report into a structured, searchable bug record plus a read-only codebase investigation. Runs extraction-first intake Q&A (at most ~4 questions, only for gaps; "unknown" never blocks), writes a Markdown bug document under b0ttsagent/bugs/open/ and appends one line to b0ttsagent/bugs/bugs.jsonl, then dispatches read-only explorer sub-agents to investigate suspect areas and appends suspected causes (confidence + file:line evidence). Also handles "I fixed X, mark it fixed" by moving the doc to b0ttsagent/bugs/fixed/ and appending a closed registry line. Use when the user reports a bug ("there's a bug", "this breaks", "X is crashing"), says "mark it fixed" / "I fixed X", or wants to search the backlog via scripts/query-bugs.js. NOT for feature requests, NOT for fixing the bug (stops at suspected causes), NOT for git-blame investigation, NOT for auto-filling environment details.
license: MIT
---

# Bug Report Skill

Turn a spoken bug report into a durable, searchable bug record **and** a read-only codebase investigation. One job: capture the bug, then hypothesize about it. Never fix it.

## Two modes

- **Mode A — Report a bug** (Steps 1–4): intake → record → investigate → append causes.
- **Mode B — Mark a bug fixed**: "I fixed X, mark it fixed" → move doc to `fixed/`, close the registry entry.

Route on the user's phrasing. If unsure which mode, ask once.

## What this skill refuses

NOT feature requests. NOT fixing the bug (the skill stops at suspected causes). NOT git history / blame as a suspect generator. NOT auto-filling environment details (the user answers the environment question). If the user wants any of these, say so and stop — do not partly comply.

## Storage layout

```
b0ttsagent/bugs/
├── open/             # state: open | in progress
├── fixed/            # state: closed
└── bugs.jsonl        # one JSON object per line, append-only, latest-wins
```

- Bug documents: `YYYY-MM-DD-slug.md` (date = today; slug from the title).
- If `b0ttsagent/bugs/open/` or `b0ttsagent/bugs/fixed/` does not exist, create the folders (plain filesystem, not git) before the first write.
- Registry `filepath` is **project-root-relative** (e.g. `b0ttsagent/bugs/open/2025-08-18-login-crash.md`).
- Registry is **append-only, latest-wins**: never edit an existing line; append a new one. The last line per `id` is authoritative.
- Every appended line must be valid **UTF-8 (no BOM)**. PowerShell `Add-Content` defaults to ANSI and corrupts non-ASCII — write with an explicit UTF-8 no-BOM writer or keep registry strings ASCII-safe.

## Registry schema

One JSON object per line, camelCase, matching the `sessions.jsonl` precedent:

```json
{
  "id": "2025-08-18-login-crash",
  "state": "open",
  "title": "Login crashes on empty password",
  "description": "Submitting the login form with a blank password throws instead of validating.",
  "causes": ["login.ts:142 does not guard empty input before calling crypto"],
  "filepath": "b0ttsagent/bugs/open/2025-08-18-login-crash.md",
  "severity": "high",
  "created_at": "2025-08-18",
  "updated_at": "2025-08-18",
  "related": []
}
```

- `id` = the document stem (`YYYY-MM-DD-slug`), stable for the bug's lifetime including the open→fixed move.
- `state` ∈ `open` | `in progress` | `closed`. The agent writes `open` at creation and **never changes state on its own**. `in progress` = owner is working the fix; `closed` = fixed (Mode B).
- `severity` ∈ `low` | `medium` | `high` | `critical` | `unknown`.
- `causes` = short strings, one per suspected cause; mirrored from the document. Empty until Step 4.
- `related` = ids of duplicates/related bugs (from the dedupe step).
- Dates are `YYYY-MM-DD`.

---

## Mode A — Report a bug

### Step 1 — Intake Q&A

1. **Dedupe first.** Before any questions, search for an existing match:
   - `node scripts/query-bugs.js --search "<keywords from the report>"`
   - and grep the bug docs: `rg -l -i "<keywords>" b0ttsagent/bugs/open b0ttsagent/bugs/fixed` (if `rg` is not on PATH, use the agent's grep tool over those two folders instead)
   If a candidate duplicate/related bug is found, surface it (title, id, state, filepath) and ask whether to **link** (add to the new bug's `related[]`) instead of filing new. If the user says file new anyway, proceed.
2. **Extract first.** Harvest from the user's initial report everything already present. Never re-ask what was stated.
3. **Ask only for gaps**, in this order, **batched into one numbered list**:
   1. Reproduction steps
   2. Expected vs actual behavior
   3. Environment
   4. Impact

   *Hybrid batching:* ask all routine missing fields in one numbered batch. Only probe an individual field separately if an answer is ambiguous or contradictory.
4. **Question cap:** at most ~4 questions total. Once minimal reproduction and impact are captured, stop — even if other fields are "unknown".
5. **Skip rule:** any field may be answered "unknown" — a missing detail never blocks the report.
6. **Title:** propose 2–3 title candidates distilled from the report; the user picks or edits one. The chosen title drives the slug and the `id`.
7. **Severity:** infer `low/medium/high/critical` from the impact answer (e.g. "blocks all users" → critical; "cosmetic" → low). If impact is "unknown", severity = `unknown`.
8. **Read-back:** before touching disk, present a short summary — proposed `id`, title, severity, description, repro, expected/actual, environment, impact, and target filepath. Ask the user to confirm or edit. Only write after confirmation.

### Step 2 — Record

1. **Derive the slug** from the chosen title: lowercase; split on spaces/punctuation; drop stopwords (`a`, `an`, `the`, `and`, `of`, `in`, `to`, `for`); cap at ~5 words / ~40 chars; hyphen-joined.
2. Form `id = YYYY-MM-DD-slug` and filename `YYYY-MM-DD-slug.md`. Ensure the filename is unique under **both** `open/` and `fixed/`; if it collides, suffix the slug (`-2`, `-3`, …). If the mechanical slug disagrees with the read-back-confirmed `id`, the confirmed `id` wins.
3. **Write the Markdown document** to `b0ttsagent/bugs/open/<filename>` by hand, following `references/bug-template.md`. Front matter: `id`, `title`, `severity`, `state: open`, `created_at` (today). Leave the `## Suspected Causes` and `## Ruled Out & Open Questions` sections empty/placeholder for Step 4.
4. **Append one registry line** to `b0ttsagent/bugs/bugs.jsonl` by hand (a single JSON object on one line). `state: open`, `causes: []`, `created_at = updated_at = today`, `related` from the dedupe step. No scaffold script — write the line directly.
5. **Never change `state`** after this on your own. State transitions belong to the owner.

### Step 3 — Investigate (read-only)

1. **Derive entry points from the reproduction steps** — the repro is the map of where to look. One suspect area per repro step / symptom.
2. **Dispatch read-only explorer sub-agents**, one per suspect area. (In a harness without sub-agents, run the focused read-only passes yourself.) Parallelize where areas are independent. **Strictly read-only** — never use edit/write, never modify any file.
3. **Multiple causes:** document every suspected cause, not just the top one. For each cause record:
   - `confidence`: `low` | `medium` | `high`
   - `evidence`: file and line, e.g. `src/auth/login.ts:142` — what it shows
   - `what would confirm this`: the check or test that would verify the cause
4. **Bounded effort:** investigate to well-supported hypotheses, not to a fix. Stop when you have supported hypotheses, or when the investigation is inconclusive.
5. **If inconclusive:** record what was ruled out and what remains open (Step 4 writes these under `## Ruled Out & Open Questions`).
6. **Do NOT use git history** (blame / recently-changed files) as a suspect generator.
7. **Do NOT attempt to fix the bug.** The skill ends at suspected causes.

### Step 4 — Append suspected causes

1. **Append to the document** — add a new `### Investigation — YYYY-MM-DD` subsection under `## Suspected Causes`. Each cause is a block (cause string, confidence, evidence `file:line`, confirm-test). If the investigation ruled anything out or left things open, also append an `### As of YYYY-MM-DD` block under `## Ruled Out & Open Questions`. **Never rewrite earlier subsections** — each run appends, so the document is a trail of reasoning over time.
2. **Append a new registry line** to `bugs.jsonl` with the same `id`, `state: open` (unchanged), refreshed `updated_at`, and `causes` = the current full list of short cause strings. Existing registry lines are never edited.

---

## Mode B — Mark a bug fixed

Triggered by phrasing like "I fixed X, mark it fixed" / "mark bug X as fixed".

1. **Find the bug:** run `node scripts/query-bugs.js --search "<X>"`; confirm with the user which bug (id + filepath) is meant.
2. **Move the document** from `b0ttsagent/bugs/open/` to `b0ttsagent/bugs/fixed/` (same filename) with a plain filesystem move — not `git mv`.
3. **Update the document's front matter** `state` to `closed` with a targeted front-matter-only edit — never rewrite the body. Leave `id`, `title`, `severity`, `created_at` unchanged.
4. **Append a new registry line:** same `id`, `state: closed`, `filepath` now under `fixed/`, `updated_at` = today. Carry all other fields forward from the latest line for that id.
5. The owner may also do any of this manually — append-only latest-wins means both paths are safe.

## Query script

`scripts/query-bugs.js` — list and search the registry without loading it all into context. Used for the dedupe check (Step 1) and for owner queries.

```bash
# Latest 10 bugs (default)
node scripts/query-bugs.js
# All open bugs
node scripts/query-bugs.js --state open
# Critical bugs
node scripts/query-bugs.js --severity critical
# Keyword search (title + description + causes)
node scripts/query-bugs.js --search "login"
# One bug by id
node scripts/query-bugs.js --id 2025-08-18-login-crash
# Raw JSONL for scripting
node scripts/query-bugs.js --state open --json
```

The script collapses to the last line per `id` (latest-wins) before filtering, so results always reflect current state.

## Manual edits

The owner may append registry lines or edit bug docs by hand. Rules that keep both paths safe:

- Always **append** a new registry line for any change; never edit an existing line.
- `filepath` always project-root-relative.
- `id` stable across the bug's lifetime (including the open→fixed move).
- `state` is the owner's to transition; the agent only ever writes `open`.

## Testing

See `references/evaluations.md` for the three evaluation scenarios (Seams 1–3) and the self-test checklist. Per `write-a-skill-v2`, run them in a **fresh** runner session and watch what the runner actually does — which files it reads, which rules it skips, whether it over- or under-explains. Feed observations back into this file.
