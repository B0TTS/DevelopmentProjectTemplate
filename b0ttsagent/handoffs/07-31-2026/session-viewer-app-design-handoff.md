# Session Viewer App — Design Handoff

## Handoff source

This handoff was produced from the completed grill session recorded at:

- **Repository-relative session log:** `grill-session-quick-app-current-session-log.json` (its in the same directory as this handoff doc)

The grill is complete. No implementation has been started or authorized by closing the grill; this document captures the approved design for a later planning/implementation session.

## What was accomplished

The design was narrowed from a quick wrapper around the existing session-log script into a private, VPS-hosted web application for browsing both session metadata and full Pi transcripts.

The approved direction is:

- A web app rather than a CLI/TUI or desktop application.
- VPS-first deployment on the Contabo VPS.
- A persistent browser-launchable viewer at `sessions.b0tts.dev`.
- Cloudflare used for DNS only for this subdomain; traffic should not pass through Cloudflare Proxy or Cloudflare Tunnel.
- The DNS-only record points to the VPS Tailscale IP `100.122.184.37`.
- Caddy handles HTTPS on the VPS.
- Tailscale ACLs restrict access to the intended Tailnet devices/users.
- A private ingestion token protects the session-upload endpoint.
- The existing VPS PostgreSQL 17 infrastructure is reused, but session data is isolated in its own database and role.
- Postgres is the sole canonical store. JSONL is not part of the running system.

## Approved product scope

### v1 viewer

The home screen should prioritize a session library and transcript detail view:

- Searchable session list.
- Sorting/filtering by metadata such as date, title, harness, and device.
- Session metadata header.
- Full transcript detail view.
- Tool calls and tool results retained but collapsed by default for readability.
- Metadata-only search: title, description, date, harness, and device. Do not search message text or raw tool payloads in v1.
- Analytics are explicitly out of scope for v1 and may be considered for v2.

### Writes and deletion

- The `log-session` skill is the only normal write trigger.
- The web UI does not create sessions, manually import sessions, or edit metadata.
- Re-running `log-session` updates the existing session rather than creating a duplicate.
- The UI may hard-delete a session after explicit confirmation.
- Hard deletion removes the live session row and its transcript events; existing VPS backup retention is a separate concern.

## Ingestion design

When `log-session` is explicitly run:

1. The skill continues collecting the title, description, device, harness, resume/session information, and current Pi session path from the environment.
2. It sends the selected session metadata and transcript to the private app API.
3. The backend performs an idempotent metadata-and-transcript upsert in one transaction.
4. `PI_SESSION_ID` is the stable identity for the session.
5. If the VPS or Tailnet is unavailable, the skill reports a clear failure and does not claim success. The user reruns it later.
6. There is no filesystem watcher, background capture, JSONL fallback, or local queue in v1.

Future ingestion is not permanently restricted to one device; any device may be accepted when the skill is explicitly run.

## Database design direction

Reuse the existing PostgreSQL 17 instance documented in `b0ttsagent/NavGuides/PostgrestApiGuide.md`, but isolate this application from the existing Roblox/PostgREST data:

- Separate database: `sessionlog`.
- Dedicated application role, tentatively `sessionlog_app`.
- Do not place private transcripts in the existing public `api` schema.
- Do not reuse the Roblox/PostgREST role or public API surface.
- The Node/TypeScript backend is the application’s database client.

Initial logical model:

- `sessions`: one row per `PI_SESSION_ID`, containing session metadata and timestamps.
- `session_events`: ordered event rows linked to `sessions`, preserving the Pi event stream.
- Preserve each original event payload as JSONB so transcript rendering does not lose information.
- Use foreign-key cascading so hard deletion of a session removes its event rows.
- Enforce uniqueness on `PI_SESSION_ID` for idempotent retries.

The exact column names, indexes, migrations, and event normalization remain implementation work.

## Historical migration

Perform a one-time migration before normal operation:

- Import only existing records whose device is exactly `b0tts-laptop`.
- Ignore sessions logged from all other devices.
- The current index contains three matching `b0tts-laptop` records.
- All three currently have matching raw Pi session files available for transcript import.
- After migration, the old JSONL files are no longer part of normal operation.

The migration parser must map the existing session index metadata to the new database and locate matching raw Pi session JSONL files by their session ID.

## Deployment and access

### Viewer URL

Use:

```text
https://sessions.b0tts.dev
```

Cloudflare configuration should use a specific DNS-only record for `sessions.b0tts.dev` pointing to `100.122.184.37`. Do not use the Cloudflare orange-cloud proxy for this viewer if strict Tailnet-only access is required.

### VPS path

Follow the conventions in `b0ttsagent/NavGuides/VpsNavGuide.md`:

- Docker Compose deployment.
- App-specific system user and `/home/<appname>/` data directory.
- Existing PostgreSQL service/network reused where appropriate.
- No public host port should be opened for the viewer.
- Access should arrive through the VPS Tailscale interface.

### Caddy and HTTPS

Caddy should provide the HTTPS front door and route `sessions.b0tts.dev` to the application container. The current VPS guide notes that the Tailscale Serve `:443` slot is already used by Vaultwarden, so the final deployment must reconcile that existing mapping—likely by using a Caddy front door for hostname-based routing or by choosing an explicitly documented alternate arrangement.

Because the custom domain is DNS-only, the VPS must obtain a browser-trusted certificate itself, likely through a Let’s Encrypt DNS-01 challenge using a narrowly scoped Cloudflare DNS API token. Do not expose or record any token values in project files or this handoff.

### Quick launch

Quick launch means:

- The VPS app remains running under Docker Compose.
- The user opens it through a browser bookmark/shortcut.
- Docker Compose provides the repeatable start/restart path.
- A local Docker/development mode remains available for development and recovery.

## Suggested implementation shape

Use one Node/TypeScript full-stack service containing:

- The web UI.
- The private read API.
- The authenticated ingestion endpoint used by `log-session`.
- The confirmed hard-delete endpoint.
- Direct access to the isolated `sessionlog` database.

The exact UI framework is intentionally still open. Select the smallest framework that provides the required searchable library, transcript detail view, and server-side API without creating separate frontend and backend deployments.

## Existing files and references

### Session logging

- `.agents/skills/log-session/SKILL.md` — current logging workflow and metadata collection.
- `.agents/skills/log-session/scripts/add-session.js` — legacy JSONL append script; expected to be replaced or bypassed by the Postgres API integration.
- `.agents/skills/log-session/scripts/query-sessions.js` — legacy JSONL query helper; no longer part of the target runtime design.
- `b0ttsagent/sessionlogs/sessions.jsonl` — one-time migration source only.

### Infrastructure

- `b0ttsagent/NavGuides/VpsNavGuide.md` — VPS Docker, system-user, Tailscale, Caddy/Tailscale Serve, and deployment conventions.
- `b0ttsagent/NavGuides/PostgrestApiGuide.md` — existing PostgreSQL 17, PgBouncer, PostgREST, backup, and Cloudflare Tunnel architecture. Use its PostgreSQL/backup context, but keep private session data outside its public API surface.

### Pi session source

- The active raw session path is available through the `PI_SESSION_FILE` environment variable.
- `PI_SESSION_ID` is the stable identity to use for idempotent ingestion.
- The raw session format is JSONL with session metadata, model/thinking-level changes, messages, tool calls, and tool results.

## Open implementation decisions

These were intentionally left for the planning/build session:

1. Select the exact Node/TypeScript UI framework.
2. Define SQL migrations, indexes, and precise columns for `sessions` and `session_events`.
3. Decide whether the backend connects directly to the isolated database or through the existing PgBouncer path inside the VPS network.
4. Implement the migration parser and validate the three `b0tts-laptop` records against their raw session files.
5. Define ingestion-token storage, rotation, and local skill configuration without committing secrets.
6. Configure the DNS-only Cloudflare record and Caddy’s DNS-01 certificate flow.
7. Reconcile Caddy with the existing Tailscale Serve `:443` Vaultwarden mapping.
8. Add the required Tailscale ACL/grant for the session viewer service.
9. Define the transcript event rendering rules and delete-confirmation UX.
10. Decide how database backup retention should be documented relative to live hard deletes.

## Suggested skills for the next session

- `create-planning-docs` — create a formal context/plan set before implementation.
- `karpathy-guidelines` — keep the implementation minimal and verifiable.
- `docs-mcp` — consult exact, version-specific framework/Postgres/Caddy library documentation after the stack is selected.
- `mermaid-diagrams` — use if the planning or architecture documentation needs a deployment/data-flow diagram.

## Explicit non-goals for v1

- No public Cloudflare proxy or Cloudflare Access as the viewer’s primary access boundary.
- No public exposure of session transcripts.
- No automatic filesystem watcher.
- No local offline queue.
- No JSONL runtime compatibility layer.
- No user-account system.
- No analytics dashboard.
- No MCP adapter yet.
- No metadata editing or manual session creation in the web UI.

## Handoff status

The grill session is complete, its summary was approved, and the session log is closed. This handoff is the authorized continuation artifact; implementation still requires a separate explicit user instruction.
