---
name: grill-me-v2
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree, while logging every question and answer to a structured JSON artifact for session handoff. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me", and wants the grilling Q&A captured as JSON for the next agent.
disable-model-invocation: true
---

# Grill Me v2

Grill the user exactly like grill-me v1, but capture the entire session as a structured JSON artifact so the next agent can pick up with full context. Nothing is being built — the goal is shared understanding, then handoff.

## JSON Schema

| Field | Type | Notes |
|---|---|---|
| `topic` | string | Short description of what the user is trying to do, from the initial prompt |
| `initialPrompt` | string | The user's initial prompt, verbatim — preserves intent in the user's own words |
| `startedAt` | string (ISO 8601) | When the log was created |
| `qAndA` | array | Raw transcript, one entry per exchange, appended immediately after each answer |
| `qAndA[].question` | string | Agent's question, verbatim |
| `qAndA[].answer` | string | User's answer, verbatim |
| `qAndA[].timestamp` | string (ISO 8601) | When the exchange was logged |
| `status` | `"active"` \| `"complete"` | `active` while grilling or paused; `complete` once closed |
| `summary` | string \| `null` | Agent-drafted, user-approved closing summary; `null` until written |

## Append helper script

All transcript writes go through the script at `scripts/append.js` (resolve it to an absolute path against this skill directory before invoking). The point: the read-modify-write of the growing `qAndA` array happens inside the script and never enters the agent's context — only the script's one-line confirmation does. Without this, the agent would `read` the whole transcript back into context every turn even though the chat already holds every exchange. Node-only; no `jq` required.

| Subcommand | Purpose |
|---|---|
| `append` | Reads `GRILL_QUESTION` + `GRILL_ANSWER` env vars, timestamps the exchange, pushes one verbatim entry into `qAndA[]`, rewrites the file. Refuses if `status` is not `"active"`. |
| `remove` | Deletes one `qAndA` entry by 1-based `#N` (the same `#N` the `append` confirmation prints). Without `--yes`, prints the entry as a preview and exits without deleting — the agent must show this preview to the user, get confirmation, then re-run with `--yes`. Works on `active` and `complete` sessions. |
| `close` | Sets `status: "complete"` and `summary` from `--summary "<approved text>"`. |
| `state` | Prints meta only: `topic`, `startedAt`, `status`, entry count, `summary`. Use for a quick look without loading the transcript. |

Invocation shape:

```bash
GRILL_QUESTION="<full question>" GRILL_ANSWER="<full answer>" \
  node <skill-dir>/scripts/append.js append "<session-path>"
```

```bash
# Preview only (no --yes): prints the entry, does not delete
node <skill-dir>/scripts/append.js remove "<session-path>" --entry N
# After the user confirms, re-run with --yes to actually delete
node <skill-dir>/scripts/append.js remove "<session-path>" --entry N --yes
```

## Workflow

### 1. Create the session log

Immediately after the user's initial prompt:

- Derive a short `<slug>` from the prompt (lowercase, hyphenated, e.g. `grill-me-v2-skill-design`).
- Target path: `b0ttsagent/handoffs/<MM-DD-YYYY>/grill-session-<slug>.json` (current date; create the folder if missing).
- If the file already exists, append a numeric suffix: `-2`, `-3`, etc. Never overwrite, never invent a different name.
- Write the initial JSON with `topic`, `initialPrompt` (verbatim), `startedAt`, empty `qAndA`, `status: "active"`, `summary: null`.

Initial file shape:

```json
{
  "topic": "Design grill-me-v2 skill",
  "initialPrompt": "I wanna edit grill-me-v2. Heres how im thinking the skill will work: Log down the users initial prompt...",
  "startedAt": "2025-07-29T14:32:00Z",
  "qAndA": [],
  "status": "active",
  "summary": null
}
```

### 2. Grill

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.


Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

Immediately after each answer is given, append the exchange to `qAndA` by running the append helper script. Do NOT `read` the session file and rewrite it yourself — reading the growing transcript back into context every turn is pure bloat, since the chat already holds every exchange. The script's read-modify-write stays out of your context; only its one-line confirmation enters it. The exchange is stored verbatim — no consolidation, no summarizing.

### 3. Detect the end

When the decision tree is exhausted (the natural conclusion of a grill-me session), ask: "Ready to handoff?"

### 5. Close the session

Draft the `summary`, show it to the user, and get approval before writing. (This approval flow applies whether the user said yes to handoff or chose "close without handoff" below.) On approval, run the helper's close subcommand — never hand-edit `status` or `summary` into the file:

```bash
node <skill-dir>/scripts/append.js close "<session-path>" --summary "<approved summary>"
```

- **User says yes (to "Ready to handoff?")** → session closes via the script; proceed to step 6.
- **User says no** → clarify intent:
  - Resume later → leave `status: "active"`, no summary, no close call.
  - Close without handoff → same summary-approval flow, then the close subcommand above.

### 6. Bridge to handoff

End with: "Ready to activate handoff? Say yes." When the user invokes the `handoff` skill (same session), make sure the handoff document references the JSON artifact by full path. The chat context carries the path — no marker file or other bridging mechanism.

## Removing an entry logged in error

If you logged a question or answer in error (wrong text, duplicate exchange, etc.), use the `remove` subcommand instead of hand-editing the session file. The numbered `#N` shown in each `append` confirmation is the `--entry N` you pass to `remove`.

1. **Preview** first, without `--yes`:
   ```bash
   node <skill-dir>/scripts/append.js remove "<session-path>" --entry N
   ```
   This prints the full entry (`question`, `answer`, `timestamp`) and exits without deleting.
2. **Show the preview to the user** and get explicit confirmation before deleting. Never pass `--yes` without that confirmation.
3. **Delete** only after the user confirms:
   ```bash
   node <skill-dir>/scripts/append.js remove "<session-path>" --entry N --yes
   ```

Removal is allowed on both `active` and `complete` sessions — correcting the historical record is a legitimate use. Deleting entry `#N` renumbers every later entry down by one, so the `#N` you used is no longer valid for the next removal — always confirm against the entry's **content**, not its number.

## Edge cases

- **Filename collision** → suffix `-2`, `-3`, etc. Never overwrite, never rename.
- **"No" to handoff** → clarify: resume later (`active`, no summary) vs. close (`complete` + approved summary).
- **Session abandoned mid-grill** → file stays `active`; the partial transcript is the resume point.
- **Resuming a session** → if the user points at an existing `active` grill-session file, `read` it in full once to rebuild your footing (you have no chat history of the prior exchanges), then continue append-only via the helper script. Do not re-read it on every later turn — after that first footing read, only append.
- **Deleting renumbers later entries** → after `remove --entry N --yes`, every entry after `#N` shifts down by one. The next removal's `#N` may differ — always preview by content, not by number.
