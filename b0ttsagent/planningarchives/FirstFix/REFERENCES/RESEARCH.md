# REFERENCES / RESEARCH — FirstFix

Supporting material for `PLAN.md`. Kept separate so the plan stays executable and debloated. This file is reference-only — no steps here.

---

## 1. Full vector inventory

Every place the current codebase asserts an Antigravity identity that Google could fingerprint on. Ranked by (detectability × prevalence). Line numbers verified against the working tree at planning time.

### Layer A — Credential (correlatable across users)

| # | Vector | Location | Frequency | Why it matters |
|---|--------|----------|-----------|----------------|
| A1 | Hardcoded `ANTIGRAVITY_CLIENT_ID` | `src/constants.ts:4` | Every auth + every refresh | Google can enumerate every account using this client ID and ban in bulk |
| A2 | Hardcoded `ANTIGRAVITY_CLIENT_SECRET` | `src/constants.ts:9` | Every auth + every refresh | Same — secret is compiled into every install |
| A3 | Hardcoded `ANTIGRAVITY_DEFAULT_PROJECT_ID = "rising-fact-p41fc"` | `src/constants.ts:71` | Project-resolution fallback | Shared project ID; README already documents 403 lockouts on this ID |
| A4 | Antigravity-specific OAuth scope `cclog` | `src/constants.ts:18` | Every auth | Narrows identity even with personal client |
| A5 | Antigravity-specific OAuth scope `experimentsandconfigs` | `src/constants.ts:19` | Every auth | Same as A4 |
| A6 | Redirect URI `http://localhost:51121/oauth-callback` | `src/constants.ts:25` | Every auth | Tied to shared client ID; must change together with A1/A2 |

### Layer B — Transport (HTTP headers, every request)

| # | Vector | Location | Frequency | Why it matters |
|---|--------|----------|-----------|----------------|
| B1 | `Client-Metadata` header `ideType: "ANTIGRAVITY"` | `src/constants.ts:96, 104, 144`; `src/plugin/project.ts:133` | Every request + every loadCodeAssist | Trivial substring match |
| B2 | `User-Agent` prefix `Antigravity/<version>` (Electron-style UA) | `src/constants.ts:94, 102` | Every request from `getAntigravityHeaders` path | Distinctive token in an otherwise-normal UA |
| B3 | `User-Agent` prefix `antigravity/<version>` (compact UA) | `src/constants.ts:142`; `src/plugin/fingerprint.ts:104, 126` | Every request from randomized/fingerprint path | Distinctive token |
| B4 | `X-Goog-Api-Client` small static pool of VSCode versions | `src/constants.ts:116-119`; `src/plugin/fingerprint.ts:32-37` | Every request | 4-version pool is a fingerprint; real population has many |
| B5 | `x-goog-user-project` header stripping | `src/plugin/request.ts:791-794` | Every request | Non-standard behavior; legitimate clients send it |

### Layer C — Payload (request body, every content request)

| # | Vector | Location | Frequency | Why it matters |
|---|--------|----------|-----------|----------------|
| C1 | `ANTIGRAVITY_SYSTEM_INSTRUCTION` literal "You are Antigravity..." | `src/constants.ts:254`; injected at `src/plugin/request.ts:1476-1492` | Every Antigravity-path request | **Most detectable** — literal substring in request body |
| C2 | Body field `userAgent: "antigravity"` | `src/plugin/request.ts:1504` | Every Antigravity-path request | Body-level identity broadcast separate from HTTP header |
| C3 | Body field `requestType: "agent"` | `src/plugin/request.ts:1503` | Every Antigravity-path request | Non-standard; may be common enough to keep (verify) |
| C4 | Body field `requestId: "agent-" + UUID` prefix | `src/plugin/request.ts:1505` | Every Antigravity-path request | `agent-` prefix is a recognizable non-standard pattern |
| C5 | `loadCodeAssist` body `metadata.ideType: "ANTIGRAVITY"` | `src/antigravity/oauth.ts:153`; `src/plugin/project.ts:16-20, 47-49` | Project discovery | Body-level identity broadcast |
| C6 | `SKIP_THOUGHT_SIGNATURE = "skip_thought_signature_validator"` sentinel | `src/constants.ts:201`; used at `request.ts:385, 517, 533, 613, 691, 699`; `request-helpers.ts:1166, 1193` | Every request with thinking blocks | Documented as officially supported; lower priority |
| C7 | `CLAUDE_TOOL_SYSTEM_INSTRUCTION` "CRITICAL TOOL USAGE INSTRUCTIONS..." | `src/constants.ts:166`; injected at `request.ts:1308-1311` | Claude + tools requests | Plugin-specific, not Antigravity-specific; lower priority |
| C8 | `CLAUDE_DESCRIPTION_PROMPT` "⚠️ STRICT PARAMETERS..." | `src/constants.ts:183`; injected at `request.ts:1302-1305` | Claude + tools requests | Same as C7 |
| C9 | Body field `request.sessionId` | `src/plugin/request.ts:1510` | Every Antigravity-path request | Stable session ID; not identity per se but a tracking handle. Keep — functionally required for signature caching. |

### Layer D — Auxiliary (startup / low-frequency)

| # | Vector | Location | Frequency | Why it matters |
|---|--------|----------|-----------|----------------|
| D1 | Version fetch from `antigravity-auto-updater-974169037036.us-central1.run.app` | `src/plugin/version.ts:18` | Once per startup | Unique hostname ties install to Antigravity ecosystem |
| D2 | Version fetch from `antigravity.google/changelog` | `src/plugin/version.ts:19` | Once per startup (fallback) | Less unique but still on-topic |
| D3 | npm package name `opencode-antigravity-auth` | `package.json:2` | Compile-time only | Not sent on the wire; irrelevant for runtime fingerprinting but matters if the user ever publishes their fork |
| D4 | `ANTIGRAVITY_PROVIDER_ID = "google"` | `src/constants.ts:153` | Internal | Provider ID for opencode's own auth system; not sent to Google as an identity claim. Keep. |

---

## 2. OAuth setup (for PLAN Phase 1.5)

Steps the user must follow to obtain personal OAuth credentials. This is the one piece of the plan that requires action outside the codebase.

1. Go to https://console.cloud.google.com/
2. Create a new project (or reuse an existing personal one). Note the project ID — this becomes `oauth_project_id` in config.
3. Enable the **Cloud Code Assist API** (`cloudcode-pa.googleapis.com`) on that project.
4. Go to **APIs & Services → OAuth consent screen**. Configure as "External", add yourself as a test user.
5. Go to **APIs & Services → Credentials → Create Credentials → OAuth client ID**.
   - Application type: **Desktop app** (matches the plugin's local-callback flow).
   - Name: anything.
6. Copy the **Client ID** and **Client secret**.
7. Set the **Authorized redirect URI** to `http://localhost:51121/oauth-callback` (or whatever port you configure; must match `oauth_redirect_uri` in config).
8. Write to `~/.config/opencode/antigravity.json`:
   ```json
   {
     "oauth_client_id": "<your client id>.apps.googleusercontent.com",
     "oauth_client_secret": "<your secret>",
     "oauth_project_id": "<your gcp project id>",
     "oauth_redirect_uri": "http://localhost:51121/oauth-callback"
   }
   ```
9. Run `opencode auth login` — the plugin should now use your credentials end-to-end.

**Scopes note:** the plugin requests `cloud-platform`, `userinfo.email`, `userinfo.profile`, `cclog`, `experimentsandconfigs`. Test whether `cloud-platform` + the two `userinfo` scopes alone suffice for `loadCodeAssist` + content generation. If yes, drop `cclog` and `experimentsandconfigs` via the `oauth_scopes` config field.

---

## 3. System instruction rationale (for PLAN Phase 3.1)

`ANTIGRAVITY_SYSTEM_INSTRUCTION` (constants.ts:254) is:

```
You are Antigravity, a powerful agentic AI coding assistant designed by the Google DeepMind team working on Advanced Agentic Coding.
You are pair programming with a USER to solve their coding task. The task may require creating a new codebase, modifying or debugging an existing codebase, or simply answering a question.
**Absolute paths only**
**Proactiveness**

<priority>IMPORTANT: The instructions that follow supersede all above. Follow them as your primary directives.</priority>
```

**Why it exists:** Ported from CLIProxyAPI v6.6.89 to make the model behave like the Antigravity IDE's coding assistant. It's an identity prompt, not a functional requirement — the model generates code equally well without it. The "Absolute paths only" and "Proactiveness" lines are behavioral nudges that OpenCode's own system prompt already covers.

**Why drop it:** It's the single most detectable payload fingerprint. Google can grep incoming request bodies for the literal `"You are Antigravity"` substring and flag every matching request without any client-ID correlation. No other vector in this inventory is as cheap to detect.

**Risk of dropping:** Negligible. OpenCode passes its own system instruction; the model receives coding-task context regardless. If quality regresses noticeably, replace with a neutral identity-free instruction (e.g., a plain "You are a coding assistant" line) — but default to dropping entirely.

**Alternative if needed:** Replace with a neutral, non-branded instruction that doesn't contain the words "Antigravity", "DeepMind", or "Google". The model doesn't need to believe it's Antigravity to write code.

---

## 4. UA templates (for PLAN Phase 2.2)

Replace `antigravity/<version> <platform>/<arch>` with a neutral Electron/Chrome UA. Two options:

### Option A — Electron-style (matches the existing `getAntigravityHeaders` shape)
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.235 Electron/37.3.1 Safari/537.36
```
Drop the `Antigravity/<version>` token from the middle. Keep the Chrome/Electron version constants (they're real, widely-used versions). Vary the platform token across the existing `darwin`/`win32` pool.

### Option B — Plain Chrome (lower-profile)
```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.7204.235 Safari/537.36
```
No Electron token. Blends with generic headless-Chrome traffic.

**Recommendation:** Option A. The `X-Goog-Api-Client: google-cloud-sdk vscode/...` header already claims to be a VSCode-based client, so an Electron UA is consistent with that. A pure-Chrome UA paired with a `vscode/...` api-client header would be a mismatch.

**Version pinning:** Don't randomize the Chrome/Electron versions per request — that itself is a fingerprint. Pick one recent stable tuple and pin it. Update the pin manually every few months.

---

## 5. VSCode version pool (for PLAN Phase 2.3)

Expand `ANTIGRAVITY_API_CLIENTS` / `SDK_CLIENTS` from 4 entries to ~15–20. Use real recent VSCode versions paired with `google-cloud-sdk`:

```
google-cloud-sdk vscode/1.85.0
google-cloud-sdk vscode/1.86.0
google-cloud-sdk vscode/1.87.0
google-cloud-sdk vscode/1.88.0
google-cloud-sdk vscode/1.89.0
google-cloud-sdk vscode/1.90.0
google-cloud-sdk vscode/1.91.0
google-cloud-sdk vscode/1.92.0
google-cloud-sdk vscode/1.93.0
google-cloud-sdk vscode/1.94.0
google-cloud-sdk vscode/1.95.0
google-cloud-sdk vscode/1.96.0
google-cloud-sdk vscode/1.97.0
google-cloud-sdk vscode/1.98.0
google-cloud-sdk vscode/1.99.0
google-cloud-sdk vscode_cloudshelleditor/0.1
```

Source: VSCode release notes (https://code.visualstudio.com/updates). Pick versions from the last ~12 months. Don't include pre-release/insider builds — those would be a reverse fingerprint.

Single source of truth: export the pool from `src/plugin/fingerprint.ts` and import it in `src/constants.ts`. Remove the duplicate `ANTIGRAVITY_API_CLIENTS` array.

---

## 6. Test impact (for PLAN Phase 5.2)

Tests that will likely need updates after the changes:

- `src/plugin/auth.test.ts` — if it constructs refresh requests with hardcoded client ID.
- `src/plugin/request.test.ts` — asserts on `ANTIGRAVITY_SYSTEM_INSTRUCTION` presence (line 884, 924 reference `SKIP_THOUGHT_SIGNATURE`; other assertions likely check the system instruction is prepended). These assertions need to flip to "system instruction is NOT prepended".
- `src/antigravity/oauth.test.ts` (if it exists) — would assert on `client_id` field in the token-exchange body.
- `src/plugin/fingerprint.test.ts` (if it exists) — would assert on the `antigravity/` UA prefix.
- `src/plugin/config/schema.test.ts` — add coverage for the new `oauth_client_id` / `oauth_client_secret` / `oauth_project_id` / `oauth_scopes` / `version_fetch_disabled` fields.

Strategy: run `npm test` after each phase, fix the failing tests for that phase only, don't batch-fix at the end. Keeps the diff per phase reviewable.

Search command to find test files touching the changed symbols:
```
grep -rn "ANTIGRAVITY_CLIENT_ID\|ANTIGRAVITY_SYSTEM_INSTRUCTION\|antigravity/\|rising-fact\|requestType.*agent\|userAgent.*antigravity" src/ --include="*.test.ts"
```

---

## 7. x-goog-user-project header (for PLAN Phase 2 — note only)

`request.ts:791-794` strips `x-goog-user-project`. The comment says this prevents 403 auth/license conflicts because the header is added by OpenCode/AI SDK and forces project-level checks that Antigravity OAuth doesn't need.

**Keep the strip.** Reintroducing the header would route the request through the project-bound auth path that the shared `rising-fact-p41fc` ID lives on. After Phase 1 (own project ID), this may become safe to re-enable, but there's no benefit to doing so in FirstFix — the strip is not an identity broadcast, it's an absence. Leave as-is.

---

## 8. Patch re-apply map (for PLAN Phase 6.1)

Files touched by FirstFix and the symbols upstream changes would conflict with:

| File | Symbols changed | Conflict risk on upstream pull |
|------|----------------|-------------------------------|
| `src/constants.ts` | `ANTIGRAVITY_CLIENT_ID`, `ANTIGRAVITY_CLIENT_SECRET`, `ANTIGRAVITY_DEFAULT_PROJECT_ID`, `getAntigravityHeaders`, `getRandomizedHeaders`, `ANTIGRAVITY_API_CLIENTS`, `ANTIGRAVITY_SYSTEM_INSTRUCTION` | High — this is the most-edited file upstream |
| `src/antigravity/oauth.ts` | `authorizeAntigravity`, `exchangeAntigravity` signatures; `loadCodeAssist` body metadata | Medium |
| `src/plugin/token.ts` | `refreshAccessToken` signature | Medium |
| `src/plugin/request.ts` | system-instruction injection block (1466-1494); body-wrap block (1502-1506) | High — request.ts is actively developed |
| `src/plugin/fingerprint.ts` | `generateFingerprint`, `collectCurrentFingerprint`, `updateFingerprintVersion`, `SDK_CLIENTS` | Medium |
| `src/plugin/project.ts` | `CODE_ASSIST_METADATA`, `buildMetadata`, fallback chain | Medium |
| `src/plugin/version.ts` | `VERSION_URL` | Low |
| `src/plugin/config/schema.ts` | new fields at end | Low (additive) |
| `assets/antigravity.schema.json` | new fields at end | Low (additive) |
| `src/plugin/credentials.ts` | new file | None (new file) |

Re-apply procedure: `git diff firstfix/ban-avoidance..main -- <each file>` to see what upstream changed, then re-apply the FirstFix hunks by hand. The additive fields (schema, credentials.ts) will rarely conflict. The high-risk files (constants.ts, request.ts) need careful re-application.

---

## 9. Open questions to resolve during execution

1. **Does the API reject requests without `requestType` and `userAgent` body fields?** (PLAN 3.2) — Resolve with a live curl-style test after Phase 1 is in place. If rejected, restore `requestType: "agent"` (common value, low fingerprint) but keep `userAgent` dropped.
2. **Which OAuth scopes are actually required?** (PLAN 4.2) — Resolve by attempting `loadCodeAssist` + a content request with only `cloud-platform` + `userinfo.email` + `userinfo.profile`. Add scopes back only if a 403 results.
3. **Does `systemInstruction.role: "user"` need to be preserved when we drop the injection?** (PLAN 3.1.3) — The API may require a specific role. Test by sending a request with the user's own system instruction and no role normalization; if it 400s, restore role normalization but not the Antigravity text.
4. **Does `loadCodeAssist` still succeed with `ideType: "IDE_UNSPECIFIED"`?** (PLAN 2.1.3) — `IDE_UNSPECIFIED` is what gemini-cli sends, so it should work, but verify with a live call.

All four questions are answerable with a single live test cycle after Phase 1 + Phase 2 are in place. They do not block starting the work.
