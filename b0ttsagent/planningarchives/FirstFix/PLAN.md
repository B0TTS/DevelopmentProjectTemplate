# PLAN — FirstFix

Executable plan for personal ban-avoidance hardening of `opencode-antigravity-auth`.

**Target codebase:** `C:\Development\Projects\opencode-antigravity-auth\opencode-antigravity-auth`
**Context:** See `CONTEXT.md` (the *what* and *why*). This document is the *how*.
**References:** See `REFERENCES/RESEARCH.md` for the full vector inventory, code excerpts, and rationale.

---

## Strategy

The plugin broadcasts the "Antigravity" identity on **three layers**. The fix must address all three, in this order, because each layer is independently detectable:

1. **Credential layer** — the shared OAuth client ID/secret (correlatable across all users)
2. **Transport layer** — HTTP headers that say "ANTIGRAVITY" on every request
3. **Payload layer** — request-body fields and string literals that say "Antigravity" on every request

Swapping only the OAuth client ID (the prior plan's Phase 1) leaves layers 2 and 3 fully intact and trivially detectable. We do all three.

**Disguise principle:** Wherever the plugin currently asserts a static, shared, non-standard identity string, we either (a) source it from the user's own config, (b) randomize it to match a legitimate client distribution, or (c) drop it if it is not functionally required. We never replace one shared constant with another shared constant.

---

## Phase 0 — Prep & baseline

**Goal:** Establish a green build and a clean diff baseline before any changes.

- [ ] 0.1 Run `npm install` and `npm run build` from the target codebase; confirm it compiles clean.
- [ ] 0.2 Run `npm test`; record the pass count. All subsequent phases must keep this green.
- [ ] 0.3 Create a new git branch: `firstfix/ban-avoidance` (do not commit anything yet; this is our isolation boundary).
- [ ] 0.4 Snapshot the current `package.json` version so we can re-detect upstream drift later.

**Exit gate:** Build and tests green on the unmodified codebase. If they aren't, stop and fix the environment first — we cannot measure regression against a broken baseline.

---

## Phase 1 — Credential layer: shed the shared OAuth client

**Goal:** No two installs share the same OAuth client ID/secret. Mine comes from my own Google Cloud project.

### 1.1 Add config fields for personal OAuth credentials

**Files:** `src/plugin/config/schema.ts`, `assets/antigravity.schema.json`

- [ ] 1.1.1 Add to the Zod schema in `src/plugin/config/schema.ts`:
  - `oauth_client_id: z.string().optional()`
  - `oauth_client_secret: z.string().optional()`
  - `oauth_redirect_uri: z.string().optional()` (defaults to the existing localhost callback; user can change if their Cloud console requires a different port)
  - `oauth_scopes: z.array(z.string()).optional()` (defaults to the current scope set; advanced users can trim)
- [ ] 1.1.2 Mirror the three fields in `assets/antigravity.schema.json` so editor validation still works.
- [ ] 1.1.3 Do **not** mark these `default(...)` — absence must remain distinguishable from presence so we can detect "user hasn't configured their own yet" at startup.

### 1.2 Make constants config-aware

**File:** `src/constants.ts`

- [ ] 1.2.1 Keep `ANTIGRAVITY_CLIENT_ID` / `ANTIGRAVITY_CLIENT_SECRET` as compile-time fallbacks (do not delete — they're still needed for the "unconfigured" error path and for any tests that construct requests without a config).
- [ ] 1.2.2 Add a new module `src/plugin/credentials.ts` that exports `getOAuthCredentials(config): { clientId, clientSecret, redirectUri, scopes }`. Logic:
  - If `config.oauth_client_id` and `config.oauth_client_secret` are both set, return them.
  - Otherwise throw a typed `MissingOAuthCredentialsError` with a message pointing the user at the setup guide (see REFERENCES/RESEARCH.md §OAuth setup).
  - Never silently fall back to the shared constants in production paths. The fallback constants are only for unit tests that explicitly opt in via a test-only export.

### 1.3 Rewire the three call sites

**Files:** `src/antigravity/oauth.ts`, `src/plugin/token.ts`

- [ ] 1.3.1 `src/antigravity/oauth.ts:96` — `authorizeAntigravity` currently imports `ANTIGRAVITY_CLIENT_ID` directly. Change it to accept a `credentials` param (passed in by the caller in `plugin.ts`).
- [ ] 1.3.2 `src/antigravity/oauth.ts:218` — `exchangeAntigravity` body uses `ANTIGRAVITY_CLIENT_ID` / `ANTIGRAVITY_CLIENT_SECRET`. Same change: accept `credentials`.
- [ ] 1.3.3 `src/plugin/token.ts:105` — `refreshAccessToken` imports the constants at module top. Change to accept `credentials` as a param (passed by the caller; this is the **hourly** leak so it's the most important).
- [ ] 1.3.4 Update the callers in `src/plugin.ts` (auth.login flow + the refresh queue) to thread `getOAuthCredentials(config)` through. Search for `authorizeAntigravity(`, `exchangeAntigravity(`, and `refreshAccessToken(` to find all call sites.
- [ ] 1.3.5 Redirect URI: thread `credentials.redirectUri` into `authorizeAntigravity` and the OAuth callback server (`src/plugin/server.ts`) so the localhost port matches the user's Cloud console config.

### 1.4 Remove the hardcoded default project ID

**File:** `src/constants.ts:71`, `src/plugin/project.ts`

- [ ] 1.4.1 Remove `ANTIGRAVITY_DEFAULT_PROJECT_ID = "rising-fact-p41fc"`. This is a shared project ID Google can enumerate.
- [ ] 1.4.2 In `src/plugin/project.ts:249, 296`, the fallback chain currently bottoms out at `ANTIGRAVITY_DEFAULT_PROJECT_ID`. Replace with: if no project ID resolves from `loadCodeAssist` / `onboardUser` / stored refresh parts, **throw a clear error** instructing the user to set `oauth_project_id` in config (new optional field from 1.1.1) or re-run `auth login`.
- [ ] 1.4.3 Add `oauth_project_id: z.string().optional()` to schema + JSON schema (same files as 1.1).

### 1.5 Document the setup path

- [ ] 1.5.1 Add a `docs/FIRSTFIX-SETUP.md` covering: creating a Google Cloud project, enabling the Cloud Code Assist API, creating an OAuth 2.0 client (type: desktop app), pasting the client ID/secret into `~/.config/opencode/antigravity.json`. Link to this from the top-level README's troubleshooting section only in *my* fork (do not push upstream).

**Exit gate:** With my own credentials in config, `opencode auth login` completes and a token refresh succeeds **without** the shared client ID appearing in any network request. Verified by inspecting debug logs (`debug: true`) for `client_id` value.

---

## Phase 2 — Transport layer: strip ANTIGRAVITY from HTTP headers

**Goal:** No HTTP header on any outbound request asserts the Antigravity identity.

### 2.1 Neutralize `Client-Metadata` header

**Files:** `src/constants.ts:92-98, 101-105, 131-146`, `src/plugin/project.ts:128-134, 16-20`

- [ ] 2.1.1 The `Client-Metadata` header is built in three places (`getAntigravityHeaders`, the deprecated `ANTIGRAVITY_HEADERS`, and `getRandomizedHeaders`). All three hardcode `"ideType":"ANTIGRAVITY"`.
- [ ] 2.1.2 Replace `ideType: "ANTIGRAVITY"` with `ideType: "IDE_UNSPECIFIED"` everywhere it appears in headers. (This matches the `GEMINI_CLI_HEADERS` shape at `constants.ts:110` — `IDE_UNSPECIFIED` is a legitimate value Google's own gemini-cli sends.)
- [ ] 2.1.3 In `src/plugin/project.ts:16-20`, the `CODE_ASSIST_METADATA` constant and `buildMetadata()` also send `ideType: "ANTIGRAVITY"` in the `loadCodeAssist`/`onboardUser` **request body**. Change to `IDE_UNSPECIFIED`. (Note: this is technically payload-layer but lives in the project-discovery transport path; grouping it here keeps the ideType change atomic.)
- [ ] 2.1.4 In `src/antigravity/oauth.ts:153`, same change to the `loadCodeAssist` body metadata.

### 2.2 Neutralize the `antigravity/` User-Agent prefix

**Files:** `src/constants.ts:94, 102, 142`, `src/plugin/fingerprint.ts:104, 126`

- [ ] 2.2.1 `getAntigravityHeaders()` (constants.ts:94) builds a full Electron-style UA: `Mozilla/5.0 (...) Antigravity/<version> Chrome/... Electron/... Safari/...`. Replace the `Antigravity/<version>` token with nothing (drop it) — leaving a generic Electron-on-Windows UA. This matches real VSCode/Electron-based editor traffic.
- [ ] 2.2.2 `getRandomizedHeaders()` (constants.ts:142) builds `antigravity/<version> <platform>/<arch>`. Replace with a neutral UA built from the same OS/arch pool but without the `antigravity/` token. Use a real Chrome/Electron UA string template; see REFERENCES/RESEARCH.md §UA templates.
- [ ] 2.2.3 `src/plugin/fingerprint.ts:104, 126` — `generateFingerprint()` and `collectCurrentFingerprint()` build `userAgent: "antigravity/<version> <platform>/<arch>"`. Same replacement: drop the `antigravity/` token, use a neutral UA template. Existing stored fingerprints in `antigravity-accounts.json` will have old UAs — add a migration in the fingerprint loader that rewrites `antigravity/` to the new template on load.
- [ ] 2.2.4 `updateFingerprintVersion()` in `fingerprint.ts:142-153` matches `^(antigravity/)([\d.]+)`. Update the regex to match the new UA template's version slot (or remove version-rewriting if the new template has no version slot — preferred, since a static version is a fingerprint).

### 2.3 `X-Goog-Api-Client` claims specific VSCode versions

**Files:** `src/constants.ts:95, 103, 116-119`, `src/plugin/fingerprint.ts:32-37`, `src/plugin/project.ts:132`

- [ ] 2.3.1 The current values `google-cloud-sdk vscode_cloudshelleditor/0.1`, `vscode/1.96.0`, `vscode/1.95.0`, etc. are a small static pool. A real population would have many versions.
- [ ] 2.3.2 Expand the pool in `fingerprint.ts:32-37` to ~15–20 recent VSCode versions (see REFERENCES/RESEARCH.md §VSCode version pool). Keep `google-cloud-sdk` prefix since that's what the legitimate gemini-cli client sends.
- [ ] 2.3.3 In `constants.ts:116-119`, the `ANTIGRAVITY_API_CLIENTS` static array is used by `getRandomizedHeaders`. Sync it with the expanded pool in fingerprint.ts (single source: export the pool from `fingerprint.ts` and import it in `constants.ts`).
- [ ] 2.3.4 Keep `project.ts:132` (the `loadCodeAssist` path) on a single stable value — `loadCodeAssist` is a low-frequency call, so a static value is fine there, just make sure it's one of the pool values, not a unique sentinel.

**Exit gate:** `grep -r "ANTIGRAVITY" src/ --include="*.ts"` in header-building code returns only the (now-unused) deprecated `ANTIGRAVITY_HEADERS` constant. Debug-log a request and confirm no header contains the substring `ANTIGRAVITY` or `antigravity/`.

---

## Phase 3 — Payload layer: strip Antigravity from request bodies

**Goal:** No request body field or string literal asserts the Antigravity identity.

### 3.1 Remove the `ANTIGRAVITY_SYSTEM_INSTRUCTION` injection

**Files:** `src/constants.ts:254`, `src/plugin/request.ts:1466-1494`

- [ ] 3.1.1 The block at `request.ts:1468-1494` prepends the literal string `"You are Antigravity, a powerful agentic AI coding assistant designed by the Google DeepMind team..."` to `systemInstruction.parts[0].text` on every Antigravity-path request. This is the single most detectable payload fingerprint.
- [ ] 3.1.2 **Decision required (see REFERENCES/RESEARCH.md §System instruction rationale):** drop the injection entirely, or replace with a neutral instruction. Default plan: **drop entirely**. The model receives the user's own system instruction via OpenCode; the Antigravity identity preamble is not functionally required for code generation.
- [ ] 3.1.3 Remove the `if (headerStyle === "antigravity")` block at 1468-1494. Leave the user's existing `systemInstruction` untouched. Keep the `role: "user"` normalization only if the API requires it (verify with a single live request after the change).
- [ ] 3.1.4 Delete `ANTIGRAVITY_SYSTEM_INSTRUCTION` from `constants.ts:254`. Search for any other importers; remove the import from `request.ts:53`.

### 3.2 Remove body `userAgent: "antigravity"` and `requestType: "agent"`

**File:** `src/plugin/request.ts:1502-1506`

- [ ] 3.2.1 The `if (headerStyle === "antigravity")` block sets three body fields:
  - `wrappedBody.requestType = "agent"` → drop the field (the API does not require it for content generation; verify with a live request).
  - `wrappedBody.userAgent = "antigravity"` → drop the field. This is a dead giveaway.
  - `wrappedBody.requestId = "agent-" + crypto.randomUUID()` → keep the `requestId` field (useful for tracing) but change the prefix from `"agent-"` to a non-distinctive value. Use a bare UUID with no prefix, or `crypto.randomUUID()` alone.
- [ ] 3.2.2 Confirm with a live request that dropping `requestType` and `userAgent` does not cause a 400. If the API rejects the request, restore `requestType: "agent"` (it's a common value) but still drop `userAgent: "antigravity"`.

### 3.3 Remove the `SKIP_THOUGHT_SIGNATURE` sentinel

**Files:** `src/constants.ts:201`, `src/plugin/request.ts:385, 517, 533, 613, 691, 699`, `src/plugin/request-helpers.ts:1166, 1193`

- [ ] 3.3.1 The sentinel string `"skip_thought_signature_validator"` is injected into thinking-block `signature` fields on every request that has thinking blocks. It's documented as an "officially supported Google API feature" — meaning legitimate clients also send it — so it's **lower priority** than 3.1/3.2. Keep for now unless we find evidence Google specifically targets it.
- [ ] 3.3.2 **Defer this.** Mark as a follow-up in REFERENCES/RESEARCH.md. Do not change in FirstFix unless live testing shows it's safe to remove.

### 3.4 Claude tool-hardening instructions

**Files:** `src/constants.ts:166, 183`, `src/plugin/request.ts:1300-1312`

- [ ] 3.4.1 `CLAUDE_TOOL_SYSTEM_INSTRUCTION` ("CRITICAL TOOL USAGE INSTRUCTIONS: ...") and `CLAUDE_DESCRIPTION_PROMPT` ("⚠️ STRICT PARAMETERS: ...") are injected for Claude models with tools. These are recognizable string literals but they're **plugin-specific, not Antigravity-specific** — Google would have to fingerprint on this plugin's hardening text, not on Antigravity's identity.
- [ ] 3.4.2 **Defer this.** Lower priority. Already gated by `claude_tool_hardening` config (user can disable). Document in REFERENCES/RESEARCH.md as a possible future vector.

**Exit gate:** `grep -r "Antigravity" src/ --include="*.ts"` returns only type names, file names, and comments — no string literals sent on the wire. Live `opencode run "Hello"` succeeds against a Gemini model and a Claude model.

---

## Phase 4 — Auxiliary vectors

### 4.1 Version fetch endpoint

**File:** `src/plugin/version.ts:18`

- [ ] 4.1.1 The plugin fetches the latest Antigravity version from `https://antigravity-auto-updater-974169037036.us-central1.run.app` at startup. This is a unique hostname that ties the install to the Antigravity ecosystem.
- [ ] 4.1.2 Change the default to rely on the changelog scrape (line 19, `https://antigravity.google/changelog`) and the hardcoded fallback (`constants.ts:73`) only. Remove the auto-updater URL as the primary source. The version is only used to build the UA string, and we're removing the `antigravity/<version>` token from the UA in Phase 2 anyway, so the version fetch becomes low-value.
- [ ] 4.1.3 Add a config flag `version_fetch_disabled: z.boolean().default(false)` so the user can skip all network version checks and pin the fallback version.

### 4.2 OAuth scopes

**File:** `src/constants.ts:14-20`

- [ ] 4.2.1 The scope `https://www.googleapis.com/auth/cclog` is Antigravity-specific. Even with personal OAuth credentials, requesting this scope narrows identity.
- [ ] 4.2.2 Confirm via live test which scopes are actually required for `loadCodeAssist` + content generation. Drop `cclog` and `experimentsandconfigs` if not required. If `cloud-platform` alone suffices, drop everything else.
- [ ] 4.2.3 Wire this through the `oauth_scopes` config field from 1.1.1 so the user can control their scope set.

**Exit gate:** Startup network log shows no request to the auto-updater hostname. OAuth flow requests the minimal scope set.

---

## Phase 5 — Verification & hardening

- [ ] 5.1 Run `npm run build` — must pass clean.
- [ ] 5.2 Run `npm test` — must pass with the same (or better) count as Phase 0 baseline. Update any tests that hard-coded the old constants (expected; see REFERENCES/RESEARCH.md §Test impact).
- ] 5.3 Run `npm run typecheck` — must pass.
- [ ] 5.4 Live smoke test:
  - `opencode auth login` with personal OAuth credentials → completes, stores token.
  - `opencode run "say hello" --model=google/antigravity-gemini-3-flash` → returns a response.
  - `opencode run "say hello" --model=google/antigravity-claude-sonnet-4-6` → returns a response.
  - Wait 1 hour (or shorten token TTL for testing) → token refresh succeeds without the shared client ID.
- [ ] 5.5 Fingerprint audit: with `debug: true`, capture one full request cycle and grep the debug log for `antigravity`, `Antigravity`, `ANTIGRAVITY`, `rising-fact`, `agent-`, `skip_thought_signature_validator`. Only acceptable hits: file paths in log lines (not on-the-wire content), and the `SKIP_THOUGHT_SIGNATURE` sentinel if deferred from 3.3.
- [ ] 5.6 Confirm `~/.config/opencode/antigravity-accounts.json` does not store the shared client ID anywhere (it stores refresh tokens + project IDs; verify no constant leakage).
- [ ] 5.7 Commit the branch `firstfix/ban-avoidance` with one commit per phase (5 commits). Do **not** push, do **not** open a PR (personal fork only).

---

## Phase 6 — Maintenance

- [ ] 6.1 Write a short `docs/FIRSTFIX-PATCH-REAPPLY.md` describing how to re-apply these patches after pulling upstream: the patch is small (~10 files), conflicts will be at known sites (constants.ts, request.ts, oauth.ts, token.ts, fingerprint.ts, project.ts, version.ts, schema.ts). List the exact symbols upstream changes to these files would touch.
- [ ] 6.2 Pin a note in `b0ttsagent/planning/FirstFix/` that this patch set must be re-verified after any upstream version bump that touches the OAuth, request, or fingerprint modules.

---

## What we are explicitly NOT doing in FirstFix

- No network-level obfuscation (no proxy rotation, no IP hopping).
- No `SKIP_THOUGHT_SIGNATURE` removal (deferred to follow-up — see 3.3).
- No Claude tool-hardening text removal (deferred — see 3.4).
- No distribution packaging. Patches stay on my local fork.
- No upstream PRs.
- No changes to account rotation, quota, recovery, or thinking-block logic — those are functional, not identity, surfaces.

---

## Sequencing summary

| Phase | Layer | Risk reduced | Effort |
|-------|-------|-------------|--------|
| 0 | — | Baseline | S |
| 1 | Credential | Shared client ID correlation (the bulk-ban vector) | M |
| 2 | Transport | Header-level "ANTIGRAVITY" broadcasts | M |
| 3 | Payload | Body-level "Antigravity" string broadcasts | S |
| 4 | Auxiliary | Auto-updater hostname, OAuth scopes | S |
| 5 | — | Verification | S |
| 6 | — | Maintenance docs | S |

If time-constrained, Phases 1 + 2 + 3 together close the currently-known high-priority vectors. Phase 4 is polish.
