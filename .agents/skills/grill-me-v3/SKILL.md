---
name: grill-me-v3
description: Interview the user about a plan or design until reaching shared understanding — building the full decision tree internally before grilling, so only branches that genuinely need the user's input become questions. Logs every question and answer to a structured JSON artifact for session handoff. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me", and wants the grilling Q&A captured as JSON for the next agent without endless questioning.
disable-model-invocation: true
---

# Grill Me v3

Grill the user exactly like grill-me, but build the decision tree internally before grilling so only branches that genuinely need the user become questions. The session is still captured as a structured JSON artifact so the next agent can pick up with full context. Nothing is being built — the goal is shared understanding, then handoff.

**Two artifacts, two owners — never confuse them:**
- **Session log** — the JSON this skill creates and closes (steps 1–5). Owned by this skill.
- **Handoff document** — the markdown written only by the `handoff` skill. Never written from memory, never written without explicit user confirmation (step 6).

Closing the session log ends this skill's job. It is not authorization to build, plan, or implement anything discussed — that always requires a separate, explicit user instruction.

## JSON Schema

| Field | Type | Notes |
|---|---|---|
| `topic` | string | Short description of what the user is trying to do, from the initial prompt |
| `initialPrompt` | string | The user's initial prompt, verbatim — preserves intent in the user's own words |
| `startedAt` | string (ISO 8601) | When the log was created |
| `qAndA` | array | Raw transcript — one entry per exchange or self-resolved decision — appended immediately |
| `qAndA[].question` | string | Agent's question, verbatim — or the stated decision for self-resolved entries |
| `qAndA[].answer` | string \| `null` | User's answer, verbatim; `null` while a logged question is awaiting its answer; or `(self-resolved — user may veto)` for self-resolved entries |
| `qAndA[].timestamp` | string (ISO 8601) | When the question or self-resolved decision was logged |
| `qAndA[].answeredAt` | string (ISO 8601), optional | When a logged question received its answer |
| `status` | `"active"` \| `"complete"` | `active` while grilling or paused; `complete` once closed |
| `summary` | string \| `null` | Agent-drafted, user-approved closing summary; `null` until written |

## Append helper script

All transcript writes go through the script at `scripts/append.js` (resolve it to an absolute path against this skill directory before invoking). The point: the read-modify-write of the growing `qAndA` array happens inside the script and never enters the agent's context — only the script's one-line confirmation does. Without this, the agent would `read` the whole transcript back into context every turn even though the chat already holds every exchange. Node-only; no `jq` required.

| Subcommand | Purpose |
|---|---|
| `ask` | Reads `GRILL_QUESTION`, timestamps the question, and pushes `{ question, answer: null }` into `qAndA[]` before the question is shown to the user. Refuses if another question is awaiting an answer. |
| `answer` | Reads `GRILL_ANSWER`, fills the one pending entry's `answer`, and records `answeredAt`. Refuses if no question is awaiting an answer. |
| `decision` | Reads `GRILL_QUESTION` and appends a completed self-resolved entry using the standard placeholder answer. |
| `append` | Backward-compatible alias for `decision`; it only accepts self-resolved decisions. |
| `remove` | Deletes one `qAndA` entry by 1-based `#N` (the same `#N` the `append` confirmation prints). Without `--yes`, prints the entry as a preview and exits without deleting — the agent must show this preview to the user, get confirmation, then re-run with `--yes`. Works on `active` and `complete` sessions. |
| `close` | Sets `status: "complete"` and `summary` from `--summary "<approved text>"`. |
| `state` | Prints meta only: `topic`, `startedAt`, `status`, entry count, `summary`. Use for a quick look without loading the transcript. |

Invocation shape:

```bash
GRILL_QUESTION="<full question>" \
  node <skill-dir>/scripts/append.js ask "<session-path>"
```

Before asking a user question, log it with `ask`. The question written by `ask` is the canonical question: display that exact text to the user without shortening or paraphrasing. Never ask a question first and log it afterward. Make your questions look nice to read before showing them to the user though, add formatting, make your user facing questions look nice.

After the user answers, record the answer with:

```bash
GRILL_ANSWER="<full answer>" \
  node <skill-dir>/scripts/append.js answer "<session-path>"
```

**Set `GRILL_ANSWER` to the user's exact words — word-for-word, never summarized.** Copy the answer character-for-character: every word, every typo, and the full multi-paragraph answer — nothing trimmed, cleaned, or rephrased. Quote the value so line breaks and special characters survive the shell intact.

For a self-resolved decision, state the decision first, then record it with:

```bash
GRILL_QUESTION="<stated decision>" \
  node <skill-dir>/scripts/append.js decision "<session-path>"
```

The `decision` command supplies the literal answer `(self-resolved — user may veto)` automatically.

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

### 2. Build the decision tree internally

Before asking anything, map the decision tree for the topic yourself:

- Explore the codebase and any referenced docs first — resolve every branch answerable from the materials.
- For each remaining branch, draft your recommended answer, then decide whether the user's input would actually change the outcome.
- Mark a branch as **needs-user** only when its answer is a genuine preference fork, a requirement only the user knows, or a tradeoff you cannot settle from the materials. Every other branch is **self-resolved** — state your decision during the session instead of asking; the user can veto anything. Log each self-resolved decision via the append script the moment you state it — the decision as `GRILL_QUESTION`, `(self-resolved — user may veto)` as `GRILL_ANSWER` — so the session log keeps the full decision trail, not just the asked questions.
- Order the needs-user branches by dependency, so earlier answers settle later branches.

### 3. Grill

Interview the user about each **needs-user** branch until we reach a shared understanding. Walk down those branches of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.


Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

If a user's answer contradicts an earlier self-resolved decision, flag the conflict and revise the decision explicitly; log the revision as a new self-resolved entry. Never let a stated decision silently stand after an answer invalidates it.

Before each user question, run the helper's `ask` command with the complete question, then display that exact question to the user. Do not ask first and log later. The write-ahead question entry prevents the agent from reconstructing or summarizing the question after the answer arrives.

Immediately after each user answer is given, run the helper's `answer` command. Do NOT `read` the session file and rewrite it yourself — reading the growing transcript back into context every turn is pure bloat, since the chat already holds every exchange. The script's read-modify-write stays out of your context; only its one-line confirmation enters it. Pass the user's answer into `GRILL_ANSWER` word-for-word per the verbatim rule — never summarize it. The pending entry already contains the exact question, so never provide a replacement question when recording the answer.

### 4. Detect the end

When the decision tree is exhausted (the natural conclusion of a grill-me session), say so and ask how to close. This is the only closing question — there is no second handoff question later:

"Decision tree exhausted. How do you want to close?
- **(a) Close and hand off** — close the session log, then (with your go-ahead) the handoff document gets written via the `handoff` skill.
- **(b) Close without handoff** — close the session log; no handoff document.
- **(c) Leave it active** — keep the session log open to resume later."

### 5. Close the session

Draft the `summary`, show it to the user, and get approval before writing. (This approval flow applies to both (a) and (b) — every close gets an approved summary.) On approval, run the helper's close subcommand — never hand-edit `status` or `summary` into the file:

```bash
node <skill-dir>/scripts/append.js close "<session-path>" --summary "<approved summary>"
```

- **(a) Close and hand off** → session closes via the script; proceed to step 6.
- **(b) Close without handoff** → session closes via the script; step 6's hard-stop rules still apply.
- **(c) Leave it active** → leave `status: "active"`, no summary, no close call.

### 6. Terminal state — handoff consent, then stop

After the close subcommand runs, state the session log's full path, then stop. What happens next requires explicit user instruction — never proceed on your own.

**Hard-stop rules (apply after every close, whichever exit the user took):**
- Never start building, planning, or implementing anything from the grilling. Closing the session log is not authorization to build.
- Never write the handoff document without an explicit user yes to the question below.
- Never write the handoff document from memory — it is governed by the `handoff` skill.

**If the user chose (a) close and hand off**, ask once: "Session log closed. Want me to write the handoff document now?"
- **Yes** → load the `handoff` skill (read its SKILL.md) and follow it exactly — including its filename-confirmation step — and make sure the handoff document references the session log by full path. The chat context carries the path — no marker file or other bridging mechanism.
- **No / anything else** → do nothing further. The user can also invoke the `handoff` skill directly later (`/skill:handoff`); either way, that skill governs the document, not this one.

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
- **Closing preference** → the three exits live in step 4 and are asked once. Never re-ask "ready to handoff?" at any later point — step 4 is the only closing question.
- **Session abandoned mid-grill** → file stays `active`; the partial transcript is the resume point.
- **Resuming a session** → if the user points at an existing `active` grill-session file, `read` it in full once to rebuild your footing (you have no chat history of the prior exchanges), then continue through the helper script. If the final entry has `answer: null`, that question is still awaiting the user's answer; do not ask another question. After that first footing read, do not re-read the transcript on every later turn.
- **Deleting renumbers later entries** → after `remove --entry N --yes`, every entry after `#N` shifts down by one. The next removal's `#N` may differ — always preview by content, not by number.
