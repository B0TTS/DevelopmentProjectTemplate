# REFERENCES / RESEARCH — Antigravity Ban Avoidance

New research from this session only. Excludes directory listings, code style,
and anything inferable from the codebase or already in CONTEXT/PLAN.

---

## §1 Full vector inventory

Consolidates the prior handoff's findings with the 9 in-band broadcasts the
handoff missed. Grouped by layer, ordered by frequency (highest first within
each layer). This is the authoritative inventory referenced by PLAN Phase 0
grep audit and Phase 5 verification.

### Layer A — Credential (sent on auth + every token refresh)

| Identifier | Location (symbol + file) | Frequency | Why it matters |
|---|---|---|---|
| `ANTIGRAVITY_CLIENT_ID` | `ANTIGRAVITY_CLIENT_ID` in `src/constants.ts` → consumed by `authorizeAntigravity()`, `exchangeAntigravity()` in `src/antigravity/oauth.ts`, `refreshAccessToken()` in `src/plugin/token.ts` | Auth URL + token exchange (per login) + token refresh (~hourly) | Google can query all accounts using this client ID and ban in bulk — the #1 bulk-ban vector |
| `ANTIGRAVITY_CLIENT_SECRET` | `ANTIGRAVITY_CLIENT_SECRET` in `src/constants.ts` → `exchangeAntigravity()`, `refreshAccessToken()` | Token exchange + refresh | Same as above; secret is compiled into every install |
| `ANTIGRAVITY_DEFAULT_PROJECT_ID` (`"rising-fact-p41fc"`) | `ANTIGRAVITY_DEFAULT_PROJECT_ID` in `src/constants.ts` → fallback in `src/plugin.ts`, `src/plugin/project.ts` | Every request that fails project discovery | Shared GCP project ID; README confirms 403s on this project — Google already locking it down |
| `ANTIGRAVITY_REDIRECT_URI` (port `51121`) | `ANTIGRAVITY_REDIRECT_URI` in `src/constants.ts` → `authorizeAntigravity()`, `exchangeAntigravity()` | Per login | Tied to the shared OAuth client; personal client may need different port |

### Layer B — Transport (sent on every request as headers)

| Identifier | Location (symbol + file) | Frequency | Why it matters |
|---|---|---|---|
| `Client-Metadata` `ideType:"ANTIGRAVITY"` | `getAntigravityHeaders()`, `getRandomizedHeaders()` in `src/constants.ts`; `generateFingerprint()`, `collectCurrentFingerprint()` in `src/plugin/fingerprint.ts` | Every request | Broadcasts Antigravity identity on every request; trivially grep-able server-side |
| User-Agent `antigravity/` prefix | `getAntigravityHeaders()`, `getRandomizedHeaders()` in `src/constants.ts`; `generateFingerprint()` in `src/plugin/fingerprint.ts` | Every request | Non-standard UA prefix; no legit client uses it |
| `X-Goog-Api-Client` VSCode version pool | `ANTIGRAVITY_API_CLIENTS` in `src/constants.ts` → `getRandomizedHeaders()`; `SDK_CLIENTS` in `src/plugin/fingerprint.ts` | Every request | Claims specific VSCode IDE versions (`vscode_cloudshelleditor/0.1`, etc.) — recognizable non-standard pattern |

### Layer C — Payload (sent on every model request in the body)

| Identifier | Location (symbol + file) | Frequency | Why it matters |
|---|---|---|---|
| `ANTIGRAVITY_SYSTEM_INSTRUCTION` ("You are Antigravity...") | `ANTIGRAVITY_SYSTEM_INSTRUCTION` in `src/constants.ts` → injected in `src/plugin/request.ts` (6 call sites around line 1476-1491) | Every model request | Literal "You are Antigravity" string in `systemInstruction` — the single most detectable fingerprint; grep-able without client ID correlation |
| Body `userAgent:"antigravity"` field | Wrapped body in `src/plugin/request.ts` (around line 1504, guarded by `headerStyle === "antigravity"`) | Every antigravity-style model request | Separate from HTTP header; literal `"antigravity"` in JSON body |
| `requestType:"agent"` | Wrapped body in `src/plugin/request.ts` (around line 1503, antigravity-style path only) | Every antigravity-style model request | Non-standard `requestType` value; recognizable pattern |
| `requestId:"agent-" + UUID` prefix | Wrapped body in `src/plugin/request.ts` (around line 1505) | Every antigravity-style model request | `agent-` prefix is non-standard; trivially detectable |
| `ideType:"ANTIGRAVITY"` in `loadCodeAssist` body | `fetchProjectID()` in `src/antigravity/oauth.ts`; project discovery in `src/plugin/project.ts` | Project discovery (per login + on cache miss) | In-body identity broadcast, same risk as header version |
| `SKIP_THOUGHT_SIGNATURE` sentinel (`"skip_thought_signature_validator"`) | `SKIP_THOUGHT_SIGNATURE` in `src/constants.ts` → injected in `src/plugin/request.ts` (6 sites) + `src/plugin/request-helpers.ts` (2 sites) | Every request with thinking blocks | Non-standard sentinel string; identifies client as non-legit |
| `CLAUDE_TOOL_SYSTEM_INSTRUCTION` | `CLAUDE_TOOL_SYSTEM_INSTRUCTION` in `src/constants.ts` → injected in `src/plugin/request.ts` (around line 1310) | Every Claude tool request | Recognizable system instruction; identifies client as Antigravity-derived |

### Layer D — Auxiliary (sent infrequently or at startup)

| Identifier | Location (symbol + file) | Frequency | Why it matters |
|---|---|---|---|
| Version fetch URL `antigravity-auto-updater-974169037036.us-central1.run.app` | `VERSION_URL` in `src/plugin/version.ts` | Once at plugin startup | Unique Cloud Run endpoint; network fingerprint to a Google-operated but non-standard host |
| OAuth scope `cclog` | `ANTIGRAVITY_SCOPES` in `src/constants.ts` | OAuth scope set (per login) | Antigravity-specific scope; narrows identity |
| OAuth scope `experimentsandconfigs` | `ANTIGRAVITY_SCOPES` in `src/constants.ts` | OAuth scope set (per login) | Antigravity-specific scope; narrows identity |

**Count: 16 distinct shared identifiers** across 4 layers. The prior handoff
cataloged 5 (Layer A + 3 from Layer B/C). This session added 11 (the remaining
Layer B/C/D entries).

---

## §2 Personal OAuth client setup walkthrough

Referenced by PLAN Phase 1. Not yet executed — this is the procedure to follow
during Phase 1 implementation.

1. **Create a Google Cloud project** at `console.cloud.google.com` (or use an
   existing one). Note the project ID — this replaces `rising-fact-p41fc`.
2. **Enable the Cloud Code Assist API** in that project (APIs & Services →
   Library → search "Cloud Code Assist API" → Enable). [NEEDS CLARIFICATION:
   confirm the exact API name and whether personal projects are eligible — the
   upstream uses a Google-internal managed project.]
3. **Configure OAuth consent screen** (APIs & Services → OAuth consent screen):
   - User type: External (or Internal if workspace)
   - Add the 5 scopes from `ANTIGRAVITY_SCOPES` (or the reduced set once Open
     Question #4 is resolved)
   - Add yourself as a test user
4. **Create OAuth credentials** (APIs & Services → Credentials → Create
   credentials → OAuth client ID):
   - Application type: Web application
   - Authorized redirect URI: `http://localhost:51121/oauth-callback` (or a
     different port if 51121 conflicts — update `ANTIGRAVITY_REDIRECT_URI`
     accordingly)
5. **Copy credentials into `antigravity.json`**:
   ```json
   {
     "oauth_client_id": "<your-client-id>.apps.googleusercontent.com",
     "oauth_client_secret": "GOCSPX-<your-secret>",
     "project_id": "<your-gcp-project-id>"
   }
   ```
6. **Run `opencode auth login`** and verify the OAuth flow completes against
   your personal client ID (check the authorization URL — `client_id` param
   should match your credential, not `1071006060591-...`).

**Risk note:** personal OAuth clients for the Cloud Code Assist API may not be
eligible for the same quota/managed-project treatment as the upstream's
Google-internal project. [NEEDS CLARIFICATION: does `loadCodeAssist` return a
managed project for personal OAuth clients, or only for the upstream's
whitelisted client?] If `loadCodeAssist` returns no project, the
`project_id` config field becomes the fallback — this is why it's a required
config field, not optional.

---

## §3 Prior analysis gaps

What `b0ttsagent/handoffs/06-25-2026/antigravity-ban-avoidance-analysis.md` got
wrong or missed, with verification evidence from this session. Referenced by
CONTEXT "What I Already Know" gaps section.

### Corrections (handoff was wrong)

1. **Body-wrapping shape misstated.** Handoff said
   `{project, model, requestType, userAgent, requestId}`. Actual shape
   (verified at `src/plugin/request.ts` wrapped body construction): the shape
   is `{project, model, request, requestType, userAgent, requestId}` — there
   is a `request` field that wraps the payload. The `requestType`/`userAgent`/
   `requestId` fields are added only on the `headerStyle === "antigravity"`
   path.
2. **Endpoint target wrong.** Handoff said rerouting to
   `cloudcode-pa.googleapis.com` (prod). Actual: `ANTIGRAVITY_ENDPOINT` in
   `src/constants.ts` is set to `ANTIGRAVITY_ENDPOINT_DAILY`
   (`daily-cloudcode-pa.sandbox.googleapis.com`) — the daily sandbox is the
   primary; prod is a fallback. Hitting the daily sandbox is itself a
   fingerprint (legit Antigravity clients may not use it).
3. **"Always `requestType: agent`" overgeneralized.** Only true on the
   `headerStyle === "antigravity"` path; the `gemini-cli` path doesn't set
   `requestType` or `userAgent`.

### Major omission (handoff never analyzed)

The handoff focused on OAuth client ID + header fingerprinting but never
cataloged the **in-band identity broadcasts** — markers in the request body
and system instruction that identify the client as Antigravity-derived on
every request. These are arguably more detectable than the OAuth client ID
(present in every request, not just auth) and must be addressed for
de-bulking to be effective. The 9 missed broadcasts are Layer C + the
`loadCodeAssist` body ideType in §1 above.

### Conceptual gap in recommendations

The handoff's Phase 1 (own OAuth credentials) is necessary but insufficient.
Even with a personal OAuth client, all Layer B/C/D markers still broadcast
the Antigravity identity. The recommended order should be: strip Layer B/C
identity broadcasts FIRST (cheap, high-detection), then Layer A (credential,
higher-impact but more setup). PLAN.md uses a credential-first order because
the disguise principle (config-driven with fallback) makes the order
safety-irrelevant — but the detection-risk ordering is B/C → A → D.

---

## §4 Open Questions research notes

What's known about each Open Question to help resolve them during execution.
Referenced by PLAN Phases 2-4.

### OQ1 — System instruction (drop or replace?)

- The `ANTIGRAVITY_SYSTEM_INSTRUCTION` string begins "You are Antigravity, a
  powerful agentic AI coding assistant designed by the Google DeepMind team..."
  (`src/constants.ts`).
- It is injected into `systemInstruction` on every model request (6 call sites
  in `src/plugin/request.ts`).
- Unknown: whether the model expects an identity prompt to function, or
  whether it's cosmetic. The upstream README and CHANGELOG don't document a
  functional dependency on this specific string.
- **Safe path:** make config-driven via `system_instruction_mode` with values
  `"drop"` | `"neutral"` | `"custom"`. Test each mode with a live model call
  (PLAN Phase 5 smoke test). If `"drop"` works, prefer it — fully removes the
  fingerprint. If the model degrades, fall back to `"neutral"` with a generic
  "You are a coding assistant" prompt.

### OQ2 — `ideType` field (drop or replace?)

- `ideType:"ANTIGRAVITY"` appears in the `Client-Metadata` header
  (`src/constants.ts` getAntigravityHeaders/getRandomizedHeaders) and in the
  `loadCodeAssist` body (`src/antigravity/oauth.ts`, `src/plugin/project.ts`).
- `GEMINI_CLI_HEADERS` in `src/constants.ts` uses
  `"ideType=IDE_UNSPECIFIED,platform=PLATFORM_UNSPECIFIED,pluginType=GEMINI"`
  — suggesting `IDE_UNSPECIFIED` is a valid value Google accepts.
- **Safe path:** default config-driven `ide_type` to `"IDE_UNSPECIFIED"`.
  Verify the API still accepts the request (PLAN Phase 5 smoke test).

### OQ3 — Ban-free window

- Not short-term measurable. Defer. Set N=30 days as the operational signal
  once Phase 5 passes; track manually. Not a PLAN exit gate.

### OQ4 — OAuth scopes

- `ANTIGRAVITY_SCOPES` in `src/constants.ts` includes 5 scopes; 2 are
  Antigravity-specific: `cclog` and `experimentsandconfigs`.
- The other 3 (`cloud-platform`, `userinfo.email`, `userinfo.profile`) are
  standard Google OAuth scopes.
- Unknown: whether `cclog` / `experimentsandconfigs` are required for the
  Cloud Code Assist API to function, or only for Antigravity-specific
  features the user doesn't need.
- **Safe path:** make `oauth_scopes` config-driven with the full 5-scope set
  as the default fallback. Test with the 3 standard scopes only (PLAN Phase 5
  smoke test). If the API still works, drop the 2 Antigravity-specific scopes
  from the default.

### Additional OQ surfaced during research

- **SKIP_THOUGHT_SIGNATURE necessity.** The sentinel
  `"skip_thought_signature_validator"` is injected into thinking-block
  signatures. `src/constants.ts` documents it as "an officially supported
  Google API feature" used by gemini-cli and the .NET SDK. If it's an official
  feature, it's not a fingerprint (legit clients use it too) — but the
  upstream's specific sentinel string may be detectable. [NEEDS CLARIFICATION:
  is the sentinel value part of the public API, or an implementation detail
  the upstream reverse-engineered? If public, it's not a fingerprint and can
  stay. If reverse-engineered, it's a fingerprint and should be
  config-driven.]

---

## §5 Config field reference

The 10 new `antigravity.json` fields. Referenced by PLAN Phase 0 schema
extension. Fallback values are the current hardcoded constants — allowing
incremental rollout (de-bulk layer by layer without breaking auth before
config is populated).

| Field | Type | Fallback (current hardcoded value) | Consumed by phase |
|---|---|---|---|
| `oauth_client_id` | string | `ANTIGRAVITY_CLIENT_ID` (`1071006060591-...`) | Phase 1 |
| `oauth_client_secret` | string | `ANTIGRAVITY_CLIENT_SECRET` (`GOCSPX-...`) | Phase 1 |
| `project_id` | string | `ANTIGRAVITY_DEFAULT_PROJECT_ID` (`rising-fact-p41fc`) | Phase 1 |
| `redirect_uri` | string | `ANTIGRAVITY_REDIRECT_URI` (`http://localhost:51121/oauth-callback`) | Phase 1 |
| `ide_type` | string | `"ANTIGRAVITY"` | Phase 2 |
| `user_agent_prefix` | string | `antigravity/` | Phase 2 |
| `api_client_pool` | string[] | `ANTIGRAVITY_API_CLIENTS` (3 VSCode version strings) | Phase 2 |
| `system_instruction_mode` | `"drop"` \| `"neutral"` \| `"custom"` | (current behavior = inject `ANTIGRAVITY_SYSTEM_INSTRUCTION`) | Phase 3 |
| `request_id_prefix` | string | `"agent-"` | Phase 3 |
| `version_fetch_url` | string | `VERSION_URL` (`https://antigravity-auto-updater-...run.app`) | Phase 4 |
| `oauth_scopes` | string[] | `ANTIGRAVITY_SCOPES` (5 scopes) | Phase 4 |

**Note:** `SKIP_THOUGHT_SIGNATURE` and `CLAUDE_TOOL_SYSTEM_INSTRUCTION` are
not in this table because their handling depends on OQ resolutions (§4). If
they need to be config-driven, add fields `skip_thought_signature` (string)
and `claude_tool_instruction_mode` (same enum as
`system_instruction_mode`).

---

## §6 Patch re-apply map

For maintenance after upstream updates. Referenced by PLAN Phase 6. The
upstream package updates frequently — the config-driven seam is the
maintenance surface: re-apply = re-add config fields to the Zod schema in
`src/plugin/storage.ts` and `assets/antigravity.schema.json`; user values
persist in `antigravity.json` across reinstalls.

| File | Symbols to re-apply | Conflict risk |
|---|---|---|
| `src/constants.ts` | Remove `ANTIGRAVITY_CLIENT_ID`, `ANTIGRAVITY_CLIENT_SECRET`, `ANTIGRAVITY_DEFAULT_PROJECT_ID` exports; config-read in `getAntigravityHeaders()`, `getRandomizedHeaders()` | High — upstream frequently modifies headers |
| `src/antigravity/oauth.ts` | Config-read in `authorizeAntigravity()`, `exchangeAntigravity()`, `fetchProjectID()` (ideType) | Medium — OAuth flow is stable |
| `src/plugin/token.ts` | Config-read in `refreshAccessToken()` | Low — refresh logic is stable |
| `src/plugin/request.ts` | Config-read for body `userAgent`/`requestType`/`requestId`; `system_instruction_mode` handling; `CLAUDE_TOOL_SYSTEM_INSTRUCTION` injection | High — most-edited file upstream |
| `src/plugin/fingerprint.ts` | Config-driven `ideType`, `user_agent_prefix`, `api_client_pool` | Medium |
| `src/plugin/version.ts` | Config-driven `VERSION_URL` | Low |
| `src/plugin/storage.ts` | Zod schema for new config fields | Medium — schema evolves |
| `assets/antigravity.schema.json` | JSON Schema mirror of Zod fields | Medium |

**Re-apply procedure (high level — PLAN Phase 6 will validate):**
1. `git diff` the upstream changes against the last patched commit.
2. If `src/constants.ts`, `src/plugin/request.ts`, or `src/plugin/fingerprint.ts`
   changed, manually re-apply config-read calls (highest conflict risk).
3. If only other files changed, the patch likely applies cleanly.
4. Run `npm run build` + `npm test` — if green, patch is valid.
5. User's `antigravity.json` values are untouched (no re-config needed).

---

## §7 Test impact

Which test files will break, fix strategy, grep command. Referenced by PLAN
Phases 0-5.

**Concrete evidence (verified this session):**

- Only one test file imports a soon-to-be-removed constant directly:
  `src/plugin/request.test.ts` imports `SKIP_THOUGHT_SIGNATURE` (line 11,
  used at lines 884 + 924).
- No test file imports `ANTIGRAVITY_CLIENT_ID`, `ANTIGRAVITY_CLIENT_SECRET`,
  `ANTIGRAVITY_DEFAULT_PROJECT_ID`, `ANTIGRAVITY_SYSTEM_INSTRUCTION`, or
  `CLAUDE_TOOL_SYSTEM_INSTRUCTION` directly.
- Tests that exercise OAuth/token flow indirectly (e.g.,
  `src/plugin/token.test.ts`, `src/plugin/auth.test.ts`,
  `src/plugin/rotation.test.ts`) will need test fixtures that inject config
  values once the hardcoded constants are removed.

**Fix strategy:**

1. For `request.test.ts`: replace the `SKIP_THOUGHT_SIGNATURE` import with a
   test-fixture config value (or import from the config loader with a test
   override). Update the two assertions (lines 884, 924) to expect the
   test-fixture value.
2. For OAuth/token tests: add a test helper that constructs a config object
   with test OAuth credentials; inject via the config loader's test seam.
3. For header/fingerprint tests: add test fixtures for `ide_type`,
   `user_agent_prefix`, `api_client_pool`.

**Grep command to find references to removed constants (run during Phase 0
inventory and Phase 5 audit):**

```powershell
rg -n "ANTIGRAVITY_CLIENT_ID|ANTIGRAVITY_CLIENT_SECRET|ANTIGRAVITY_DEFAULT_PROJECT_ID|ANTIGRAVITY_SYSTEM_INSTRUCTION|CLAUDE_TOOL_SYSTEM_INSTRUCTION|SKIP_THOUGHT_SIGNATURE|rising-fact-p41fc|antigravity-auto-updater|cclog|experimentsandconfigs" src/
```

Also audit for the literal string values (not just symbol names):

```powershell
rg -n "1071006060591|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|skip_thought_signature_validator|You are Antigravity" src/
```

The second command catches cases where the literal value is inlined rather
than imported via the constant.
