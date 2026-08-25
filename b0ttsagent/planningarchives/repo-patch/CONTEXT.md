# CONTEXT — Antigravity Ban Avoidance

## What I Want

Minimize personal ban risk by removing all shared hardcoded identifiers from my
local `opencode-antigravity-auth` install, so Google cannot correlate my traffic
with other plugin users and ban me in bulk. The goal is **de-bulking** — shedding
the shared identity surface — not mimicking legit Antigravity IDE traffic.

## Scope

**In:** Strip or replace every shared hardcoded identity marker in the local
source build — OAuth client ID/secret, project ID, `"ANTIGRAVITY"` strings in
headers/body/system instruction, sentinel values. Make each replacement
config-driven via `antigravity.json` so changes survive upstream rebases and
stay maintainable.

**Out:**

1. Mimicking legit Antigravity IDE traffic (blend-in strategy — rejected; see
   Assumptions).
2. Contributing changes upstream to `NoeFabris/opencode-antigravity-auth`.
3. Making the project safer for all users (personal ban avoidance only).
4. Multi-account fingerprint randomization beyond existing behavior.
5. Reverse-engineering legit Antigravity traffic.

## What Success Looks Like

1. **No shared identifier reaches Google.** Given the modified local build,
   When an auth flow + a model call is captured, Then no hardcoded value
   identical across all upstream plugin installs appears in any outgoing
   request (verifiable by code grep for each identifier + traffic inspection).
2. **Plugin functions end-to-end.** Given the modified build installed, When
   `opencode auth login` runs, Then OAuth completes and credentials persist;
   and When a model call is made, Then a completion returns.
3. **Build green.** Given the modified source, When `npm run build`,
   `npm run typecheck`, and `npm test` run, Then all exit 0.

> A fourth criterion — zero bans within N days of normal use — is deferred to
> Open Questions; it's a real signal but not short-term measurable.

## What I Already Know

Cited by path; not re-summarized here.

- `b0ttsagent/handoffs/06-25-2026/antigravity-ban-avoidance-analysis.md` —
  Prior analysis identifying the shared OAuth client ID as the primary bulk-ban
  vector, a ranked fingerprint table, and a 3-phase recommendation. Confirmed
  accurate against the live codebase in this session, with the gaps below.

**Gaps found in the prior analysis (verified this session):**

1. Body-wrapping shape was misstated — the actual shape is
   `{project, model, request, requestType, userAgent, requestId}`; the handoff
   omitted the `request` field.
2. Endpoint target was wrong — the handoff said prod
   (`cloudcode-pa.googleapis.com`); the primary is actually
   `daily-cloudcode-pa.sandbox.googleapis.com` (prod is a fallback).
3. "Always `requestType: agent`" is only true on the `headerStyle === "antigravity"`
   path; the `gemini-cli` path doesn't set it.

**Major omission in the prior analysis — in-band identity broadcasts:**

The handoff analyzed the OAuth client ID and header fingerprinting but never
cataloged the in-band markers that identify the client as Antigravity-derived in
every request. These are arguably more detectable than the client ID (present in
every request, not just auth) and MUST be addressed for de-bulking to be
effective:

- `ANTIGRAVITY_SYSTEM_INSTRUCTION` — literal "You are Antigravity..." string
  injected into `systemInstruction` on every model request.
- `Client-Metadata` header — broadcasts `ideType:"ANTIGRAVITY"` on every
  request.
- Body `userAgent` field — set to `"antigravity"` in the wrapped request body.
- `loadCodeAssist` body — `ideType:"ANTIGRAVITY"` in project-discovery calls.
- `requestId` prefix — `"agent-" + UUID` is a non-standard recognizable pattern.
- `X-Goog-Api-Client` header — claims specific VSCode IDE versions
  (`vscode_cloudshelleditor/0.1`, etc.).
- `SKIP_THOUGHT_SIGNATURE` sentinel — `"skip_thought_signature_validator"` string
  injected into thinking-block signatures.
- OAuth scopes — `cclog` and `experimentsandconfigs` are Antigravity-specific.
- `CLAUDE_TOOL_SYSTEM_INSTRUCTION` — additional recognizable system instruction
  injected for Claude tool-usage hardening.

The prior Phase 1 (own OAuth credentials) is necessary but insufficient: even with
a personal OAuth client, all in-band markers above still broadcast the
Antigravity identity.

## Constraints & Principles

Task-specific constraints that gate the plan:

1. **Config-driven.** Replacements live in `antigravity.json` (or equivalent
   plugin config), never as new hardcoded constants in source.
2. **Local build only.** Changes apply to the personal install only; never
   published to npm.
3. **De-bulk, not blend-in.** Remove shared identifiers; do not attempt to
   mimic legit Antigravity IDE traffic.
4. **Build stays green.** `npm run build`, `npm run typecheck`, `npm test` must
   pass throughout — cite `opencode-antigravity-auth/AGENTS.md` for commands.
5. **No new shared constants.** Every replacement is per-install config, never
   compiled into source.

## Key Terms

- **De-bulk vs blend-in** — the chosen strategy (shed shared identifiers) vs the
  rejected one (mimic legit Antigravity traffic).
- **Shared identifier** — a hardcoded value identical across all plugin installs.
- **Identity broadcast** — an in-band marker identifying the client as
  Antigravity-derived, present in every request.
- **OAuth client ID correlation** — Google's ability to query all accounts using
  a given client ID and ban them in bulk.

## Assumptions

Decided-by-default; override if wrong.

1. User has or will create a Google Cloud project with OAuth credentials (Web
   application type, redirect URI `http://localhost:51121/oauth-callback`).
2. User accepts that de-bulking reduces but does not eliminate ban risk (arms
   race with Google).
3. Upstream's existing multi-account + fingerprint-rotation features stay in
   place; de-bulking is orthogonal to them.
4. No upstream contribution — user maintains a local patch.
5. Local build + install via `npm run build` and local-path install into
   opencode config (no fork, no republish).

## Open Questions

Must resolve before or during execution:

1. **System instruction.** Drop `ANTIGRAVITY_SYSTEM_INSTRUCTION` entirely, or
   replace with a neutral prompt? [NEEDS CLARIFICATION: does the model expect an
   identity prompt to function, or is it cosmetic?]
2. **`ideType` field.** Drop `"ANTIGRAVITY"` from `Client-Metadata` and
   `loadCodeAssist` body, or replace with a generic value? [NEEDS CLARIFICATION:
   what does legit Gemini CLI traffic send — `IDE_UNSPECIFIED`?]
3. **Ban-free window.** What's N days for the operational signal? (Deferred as
   not short-term measurable.)
4. **OAuth scopes.** Drop `cclog` and `experimentsandconfigs`, or are they
   required for the Cloud Code Assist API to function?
5. **`SKIP_THOUGHT_SIGNATURE` sentinel.** Is `"skip_thought_signature_validator"`
   a public Google API feature (used by legit clients like gemini-cli, as
   `src/constants.ts` documents) or a reverse-engineered implementation detail?
   If public, it's not a fingerprint and can stay; if reverse-engineered, it's
   a fingerprint and must be config-driven. [NEEDS CLARIFICATION: is the
   sentinel value part of the public API contract, or an internal detail the
   upstream reverse-engineered?]

## Non-Goals

1. Making requests indistinguishable from legit Antigravity IDE traffic.
2. Contributing changes upstream.
3. Making the project safer for all users.
4. Multi-account fingerprint randomization beyond existing behavior.
5. Reverse-engineering legit Antigravity traffic.
