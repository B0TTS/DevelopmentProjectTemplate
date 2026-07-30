---
name: grill-me-v2
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree, while logging every question and answer to a structured JSON artifact for session handoff. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me", and wants the grilling Q&A captured as JSON for the next agent.
disable-model-invocation: true
---

# Grill Me v2

Grill the user exactly like grill-me v1, but capture the entire session as a structured JSON artifact so the next agent can pick up with full context. Nothing is being built — the goal is shared understanding, then handoff.

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

Interview the user relentlessly about every aspect of the plan until reaching shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. Ask **one question at a time**, and provide your recommended answer with each question. If a question can be answered by exploring the codebase, explore the codebase instead.

### 3. Log every exchange

Immediately after each question is answered, append the raw exchange to `qAndA` — every question, every answer, verbatim. No consolidation, no summarizing.

### 4. Detect the end

When the decision tree is exhausted (the natural conclusion of a grill-me session), ask: "Ready to handoff?"

### 5. Close the session

- **User says yes** → draft the `summary`, show it to the user, and get approval before writing. On approval: set `status: "complete"` and write `summary`.
- **User says no** → clarify intent:
  - Resume later → leave `status: "active"`, no summary.
  - Close without handoff → same summary-approval flow, then `status: "complete"`.

### 6. Bridge to handoff

End with: "Ready to activate handoff? Say yes." When the user invokes the `handoff` skill (same session), make sure the handoff document references the JSON artifact by full path. The chat context carries the path — no marker file or other bridging mechanism.

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

## Edge cases

- **Filename collision** → suffix `-2`, `-3`, etc. Never overwrite, never rename.
- **"No" to handoff** → clarify: resume later (`active`, no summary) vs. close (`complete` + approved summary).
- **Session abandoned mid-grill** → file stays `active`; the partial transcript is the resume point.
- **Resuming a session** → if the user points at an existing `active` grill-session file, keep appending to it instead of creating a new one.
