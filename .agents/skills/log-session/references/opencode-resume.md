# OpenCode Resume Detection

How to find the current session's id and build the `resumeCommand` when logging a session from opencode.

## Facts

- **No environment variable exposes the session id.** `OPENCODE_PID` is the server PID, not a session id. Do not look for one.
- Session data lives in a SQLite database:
  - Windows: `C:\Users\<user>\.local\share\opencode\opencode.db`
  - Linux/macOS: `~/.local/share/opencode/opencode.db`
  - Print the exact path with `opencode db path`.
- Session ids look like `ses_` + 26 mixed-case alphanumeric chars, e.g. `ses_ffdc2ef77ffe5tt6AtoKtHFjXD`.
- Schema: table `session` has columns `id`, `parent_id`, `title`, `agent`, `model`, `time_created`, `time_updated` (epoch milliseconds). Newest session = highest `time_updated`.

## Commands

- `opencode session list` — list sessions (id, title, updated time).
- `opencode db "<sql>"` — run SQL against the session DB.
- `opencode --session <id>` (or `-s <id>`) — resume a specific session. This is the preferred resume form.
- `opencode --continue` (or `-c`) — resume the session with the highest `time_updated`. See the pitfall below.

## Pitfall: subagent sessions pollute `--continue`

Subagent sessions (spawned via the Task tool) also get `session` rows, and they are often the *newest* rows. `opencode --continue` therefore frequently resumes a subagent's session, not the user's interactive chat. Do not use `--continue` unless no id can be found.

## Procedure

1. List the most recent sessions (raise the `LIMIT` if a burst of recent subagent rows hides the target):

   ```
   opencode db "SELECT id, parent_id, title, agent, time_updated FROM session ORDER BY time_updated DESC LIMIT 5"
   ```

2. Identify the row for the conversation being logged by matching `title` against what the conversation has actually covered (you cannot see your own title a priori — the title is a description of the content you have seen, so pick the row whose title best describes that content). If the conversation being logged is itself a subagent task, its row is a subagent row — that is still the correct row.

3. Cross-check with `parent_id`: a subagent row's `parent_id` points at the interactive chat that spawned it. If two rows both plausibly match (a subagent row and its parent) and the conversation being logged is the interactive chat, take the root row (the parent). Fork chains create several root rows with near-identical titles — among same-title roots, take the one with the highest `time_updated` (subagent `parent_id`s also converge on the true parent). If genuinely ambiguous, **STOP** and ask the user which session — do not guess.

4. Build the resume command as:

   ```
   opencode --session <id>
   ```

## Verify

Before writing the JSONL entry, confirm the chosen row's `title` matches the conversation you are logging. When in doubt, prove the pick by checking the session's latest user message text against the conversation content:

```
opencode db "SELECT data FROM part WHERE session_id = '<id>' AND type = 'text' ORDER BY id DESC LIMIT 3"
```

(The `model` column on `session` can be stale or mismatched — do not use it to identify the chat.)
