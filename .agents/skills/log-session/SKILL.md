---
name: log-session
description: Append the current conversation as a session-log entry to the project's JSONL resume index (b0ttsagent/sessionlogs/sessions.jsonl) via a script, for later resumption. Use when user says "log session", "log this session", "add this as a session log", "create session log", "session log this", or wants to save the current chat so it can be resumed later.
---

# Log Session

Append the current conversation as one entry to the project's JSONL session resume index. The index is append-only and lives outside the agent's context window — a script does the write, so the cost stays O(1) no matter how large the index grows.

## Target file

`b0ttsagent/sessionlogs/sessions.jsonl` — one JSON object per line.

If this file does **not** exist, **STOP**. Do not create it blindly. Alert the user. The index is seeded one-time from the legacy `AI Sesssions.md` by `scripts/migrate-to-jsonl.js` (run it only if the user confirms; it refuses to overwrite an existing file). If there is no legacy file to seed from, ask the user before creating a fresh empty index.

## Scripts (in this skill's `scripts/` dir)

Resolve all script paths against this skill's directory (the parent of this SKILL.md).

- `add-session.js` — append one entry (JSON on stdin); assigns `id` automatically. **Called by the workflow below.**
- `query-sessions.js` — read the index without loading the whole file into context. Use at resume time: `--latest N`, `--search TEXT`, `--harness NAME`, `--device NAME`, `--json`.
- `migrate-to-jsonl.js` — one-time seed from `AI Sesssions.md` (normally already done).

## Workflow

1. **Verify `sessions.jsonl` exists.** If missing, stop and alert (see Target file above).

2. **Detect your harness and resume command.** Introspect your environment to determine the agent harness and construct its resume command. If you cannot determine either, **STOP**. Do not guess. Ask the user. If the user gives a resume command explicitly, use it verbatim instead of the detected one.

   - **Pi:** exposes `PI_SESSION_ID` → `pi --session <id>`.
   - **opencode:** no env var exposes the session id — it must be pulled from the session DB, and `opencode --continue` can land on a subagent's session instead of the user's chat. See `references/opencode-resume.md` for the full procedure.

3. **Detect your device.** Run `hostname` for the raw hostname. Detect Docker: check for `/.dockerenv`; if absent, check `/proc/1/cgroup` for container indicators. If Docker is detected, annotate as `<hostname> (docker)`. If the hostname looks like an actual name, use it as-is. If it does not (e.g. a long hex hash), show the user the raw value as the default and **STOP and wait** for them to accept it or type a custom label. Detect fresh and ask again every session; do not persist custom labels.

4. **Get today's date.** Use `YYYY-MM-DD`.

5. **Draft 3 title options** from the conversation context. Present them as a numbered list. **STOP and wait** for the user to pick one.

6. **Draft the description.** A short, concise 1-3 sentence description that captures the core of the conversation. No review step — just write it.

7. **Append the entry.** Assemble a JSON object with these fields (do **not** include `id` — the script assigns it):

   - `title` — the user's chosen title (string)
   - `date` — `YYYY-MM-DD`
   - `resumeCommand` — the detected/confirmed command (string)
   - `agentHarness` — the detected harness (string)
   - `device` — the detected hostname/label, or `null`
   - `description` — the description (string; multi-line is allowed with `\n`)

   Pipe the JSON to the append script via a **quoted heredoc** (`<<'EOF'`) so any backticks or quotes in the title or description are not interpreted by the shell. Run from the project root:

   ```bash
   node .agents/skills/log-session/scripts/add-session.js <<'EOF'
   {
     "title": "<chosen title>",
     "date": "<YYYY-MM-DD>",
     "resumeCommand": "<detected command>",
     "agentHarness": "<detected harness>",
     "device": "<detected hostname or null>",
     "description": "<short 1-3 sentence description>"
   }
   EOF
   ```

8. **Confirm.** The script prints the appended record (with its new `id`) and the file path. Show the user the final entry.

## Notes

- Always append. Never edit, reorder, or rewrite existing lines — the index is append-only. Surgical changes only.
- The `description` is brief and concise — 1-3 sentences, a single string, not a bulleted list.
- Schema is exactly (key order): `id, title, date, resumeCommand, agentHarness, device, description`. Nothing else.
- To find an old session at resume time, use `query-sessions.js` rather than reading the file directly — it keeps the index out of your context window.