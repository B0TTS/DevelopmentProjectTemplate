# Handoff: Debug Pi ntfy Notifications Extension

## Summary of what was accomplished

User wanted to port an OpenCode notification plugin (`Setup/Plugins/Notifications.js`) to Pi Agent. Work happened in two phases:

1. **Planning (lightweight, in-conversation)** — Analyzed the OpenCode plugin and PI's extension system. Established the key architectural difference: OpenCode emits rich built-in events (`session.idle`, `session.error`, `permission.asked`, `question.asked`) because it has built-in permission popups and question flows. PI is deliberately minimal — those behaviors are built *as extensions*, not emitted as events. So only `session.idle` maps cleanly; the other three require building the missing behavior (a `tool_call` gate / question tool) or accepting they won't fire. User chose the lightweight path (direct implementation) and minimal scope (just the "response ready" buzz).

2. **Implementation** — Created a new Pi extension at `~/.pi/agent/extensions/notifications.ts` (global, auto-discovered). The original OpenCode plugin was left untouched per user request.

## Current state

The extension file exists and reads back correctly, but **the user reports it is not working** — no ntfy push arrives when Pi finishes a run. Root cause is unknown as of this session; debugging is deferred to the next session.

## Open decisions (already made — preserved for context)

- **Scope:** minimal — only "response ready" notification wired.
- **Idle event:** `agent_settled` chosen over `agent_end` (avoids duplicate buzzes on retry/compaction/queued follow-ups).
- **Skipped events:** `session.error`, `permission.asked`, `question.asked` — no clean PI equivalent. Each is documented in the extension file with rationale and how to add later.
- **Config:** env vars (`NTFY_USE_CLOUD`, `NTFY_BASE_URL`, `NTFY_TOPIC`, `NTFY_AUTH`) with hardcoded fallback defaults so it works out of the box.
- **Placement:** global (`~/.pi/agent/extensions/`) — applies to all projects.
- **Language:** TypeScript (idiomatic, loaded via jiti, no build step).

## Debug focus for the next session

The extension isn't firing/buzzing. Likely failure points to investigate, roughly in order of probability:

1. **ntfy endpoint reachability.** The self-hosted backend URL is a **Tailnet-only hostname** (`https://vmi3326176.tailf94009.ts.net:3000`). If the machine running Pi is not on the Tailnet at that moment, the `fetch` silently fails (caught by `catch {}`). Test the URL directly with `curl` from the Pi host. Fallback: set `NTFY_USE_CLOUD=true` to use the public `ntfy.sh` backend and rule out networking.
2. **Auth / headers.** Verify Basic auth header is accepted by the self-hosted server. The cloud topic is unauthenticated by design.
3. **`agent_settled` actually firing.** Confirm via Pi's lifecycle that `agent_settled` is the right hook for this Pi version — check `docs/extensions.md` "Agent Events" section. `agent_end` is the fallback (buzzes per-run, may duplicate on retry).
4. **Extension auto-discovery + `/reload`.** Confirm `~/.pi/agent/extensions/notifications.ts` is being loaded — Pi auto-discovers `~/.pi/agent/extensions/*.ts`. May need a full Pi restart rather than just `/reload` if the file was added after startup.
5. **jiti TS loading.** Pi loads extensions via jiti; TS should work without compilation. Check Pi's startup logs for load errors on the extension.
6. **Silent `catch {}`.** Temporarily replace the empty catch with `console.error` logging to surface any fetch/auth/network failure that's currently being swallowed.

## Key files and paths

- **New extension (the thing being debugged):** `~/.pi/agent/extensions/notifications.ts` (global Pi extensions dir)
- **Original OpenCode plugin (untouched — do not modify):** `Setup/Plugins/Notifications.js`
- **Pi extension docs:** `C:\Users\Jonah\AppData\Roaming\npm\node_modules\@earendil-works\pi-coding-agent\docs\extensions.md` — see "Agent Events" (`agent_settled` / `agent_end`) and "Extension Locations"
- **Pi example for reference (built-in terminal notify):** `...\examples\extensions\notify.ts` — uses `agent_end`, native terminal OSC/Windows-toast (only works in a terminal, unlike the ntfy approach here)
- **Other relevant examples:** `permission-gate.ts` (`tool_call` gate pattern), `question.ts` (custom question tool) — only needed if extending to the three skipped events later

## Commands relevant to continuing

- `/reload` — hot-reload extensions in an auto-discovered location (may not pick up brand-new files; full restart is safer)
- Full Pi restart to ensure the new extension is discovered
- `curl -v <ntfy-endpoint>/<topic>` from the Pi host to test endpoint reachability and auth directly, bypassing the extension

## Suggested skills for the next session

- **`create-planning-docs`** — if debugging turns into a larger effort (e.g., deciding to build the permission-gate+notify or question-detection extensions), formalize it with CONTEXT.md / PLAN.md in `b0ttsagent/planning/`.
- **`karpathy-guidelines`** — for surgical debugging changes; avoid over-engineering the fix.
- **`docs-mcp`** — to look up authoritative Pi extension/event API details if the local docs are ambiguous about `agent_settled` behavior.

## Notes

- Credentials are intentionally redacted from this handoff. The extension file itself still contains fallback creds in source (outside the repo, so not in git, but not ideal). When debugging concludes, recommend setting the `NTFY_*` env vars and blanking the source defaults.
- The ntfy approach is complementary to Pi's built-in `notify.ts` — it works in headless/rpc/json/print modes where terminal OSC/toast notifications can't fire.
