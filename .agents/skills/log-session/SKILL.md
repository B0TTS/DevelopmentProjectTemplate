---
name: log-session
description: Append the current conversation as a session log entry to a hardcoded Obsidian file for later resumption. Use when user says "log session", "log this session", "add this as a session log", "create session log", "session log this", or wants to save the current chat so it can be resumed later.
---

# Log Session

Append the current conversation as a session-log entry to a single hardcoded Obsidian file.

## Target file

`b0ttsagent\sessionlogs\AI Sesssions.md`

If this file does not exist, **STOP**. Do not create it. Alert the user that the target file is missing and suggest possible solutions (check the path, restore from backup, create the file manually with the template below).

## Workflow

1. **Verify the target file exists.** If missing, stop and alert (see above).

2. **Detect your harness and resume command.** Introspect your own environment to determine what agent harness you are running under and construct the appropriate resume command for that harness (e.g. Pi exposes `PI_SESSION_ID` → `pi --session <id>`). If you cannot determine the harness or resume command, **STOP**. Do not guess. Alert the user and ask how they want to resume this session.

3. **Detect your device.** Run the `hostname` command to get the raw hostname. Detect Docker: check for a `/.dockerenv` file first; if absent, check `/proc/1/cgroup` for container indicators. If Docker is detected, annotate the hostname as `<hostname> (docker)`. Apply judgment to the result — if it looks like an actual name, use it as-is. If it does not (e.g. a long hex hash or other incomprehensible string), notify the user with the raw value as the default and let them accept or type a custom label; **STOP and wait** for their answer. Do not persist custom labels — detect fresh and ask again every session.

4. **Get today's date.** Use `YYYY-MM-DD`.

5. **Draft 3 title options** from the conversation context. Propose them to the user as a numbered list. **STOP and wait** for the user to pick one. Do not continue until they choose.

6. **Draft the description.** Write a short, brief, concise 1-3 sentence description that captures the core of the conversation. No review step — just write it.

7. **Append the entry to the bottom of the file** using the template below. Do not touch any existing entries.

8. **Confirm** the entry was added and show the user the final entry.

## Entry template

```
## <Title chosen by user>
#### Date: <YYYY-MM-DD>
#### Resume Command: `<detected command>`
#### Agent Harness: <detected harness>
#### Device: <detected hostname or user label>
#### Description:
- <Short 1-3 sentence description>

---
```

## Notes

- Always append to the bottom. Never prepend, never reorder existing entries.
- Never edit, rewrite, or "improve" existing entries — surgical changes only.
- The Description is brief, concise, and short — 1-3 sentences on a single `- ` line, not a bulleted list of bullets.
- If the user gives you a specific resume command explicitly, use that verbatim instead of the detected one.