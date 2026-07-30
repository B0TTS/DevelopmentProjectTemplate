# Handoff: Antigravity Ban Avoidance Analysis

**Date:** 06-25-2026
**Goal:** Minimize ban risk for the user's personal installation of `opencode-antigravity-auth`

---

## What Was Accomplished

Four parallel explore agents analyzed the `opencode-antigravity-auth` codebase to identify why Google is banning users and what fingerprinting vectors exist. The analysis covered:

- Full project structure and build process
- OAuth flow implementation details
- Network request patterns and headers
- All fingerprinting vectors ranked by severity

---

## Key Findings

### #1 Killer: Shared OAuth Client ID

Every user of the npm package gets the **same hardcoded OAuth Client ID** compiled into their code. This client ID is sent to Google in 3 places:

| Step | File | Frequency |
|------|------|-----------|
| OAuth authorization URL | `src/antigravity/oauth.ts:96` | Once per `opencode auth login` |
| Token exchange | `src/antigravity/oauth.ts:218` | Once per `opencode auth login` |
| **Token refresh** | `src/plugin/token.ts:105` | **Every ~1 hour, indefinitely** |

Google can query all accounts using this client ID and ban them in bulk.

### Additional Fingerprinting Vectors (ranked)

| Priority | Vector | Location |
|----------|--------|----------|
| P0 | Hardcoded project ID `rising-fact-p41fc` | `src/constants.ts:71` |
| P1 | npm package name `opencode-antigravity-auth` | `package.json:2` |
| P1 | Request body wrapping pattern `{project, model, requestType, userAgent, requestId}` | `src/plugin/request.ts:1496-1506` |
| P1 | Endpoint rerouting to `cloudcode-pa.googleapis.com` | `src/constants.ts:32-34` |
| P2 | `antigravity/` User-Agent prefix | `src/constants.ts:142` |
| P2 | `x-goog-user-project` header stripping | `src/plugin/request.ts:791-794` |
| P2 | Always `requestType: "agent"` | `src/plugin/request.ts:1503` |
| P3 | Debug comments in compiled output | Various |
| P3 | Version fetch from `antigravity-auto-updater-974169037036.us-central1.run.app` | `src/plugin/version.ts:18` |

### What the README Confirms

The README already warns about ToS violations and bans. The troubleshooting section documents `rising-fact-p41fc` 403 errors as a known issue — meaning Google has already started locking down that project ID.

---

## Current State

- **No changes have been made** — this was a read-only analysis
- The codebase is at `C:\Development\Projects\opencode-antigravity-auth\opencode-antigravity-auth`
- The project is an npm package (`opencode-antigravity-auth`) published on npmjs.org
- Build command: `npm run build` (uses `tsc -p tsconfig.build.json`)
- Test command: `npm test` (uses vitest)

---

## Recommended Next Steps (for user's personal ban avoidance)

### Phase 1: Create Own OAuth Credentials (Highest Impact)

1. Remove hardcoded `ANTIGRAVITY_CLIENT_ID` and `ANTIGRAVITY_CLIENT_SECRET` from `src/constants.ts`
2. Add config fields `oauth_client_id` and `oauth_client_secret` to the plugin schema
3. Provide setup instructions for creating a personal Google Cloud OAuth client
4. Validate at startup; fail with clear error if missing

### Phase 2: Remove Shared Project ID

1. Remove hardcoded `ANTIGRAVITY_DEFAULT_PROJECT_ID = "rising-fact-p41fc"` from `src/constants.ts:71`
2. Make project ID required config or discover dynamically only

### Phase 3: Normalize Traffic (Optional, Lower Priority)

1. Stop stripping `x-goog-user-project` header
2. Vary `requestType` instead of always sending `"agent"`
3. Change `antigravity/` User-Agent prefix to standard Electron/Chrome UA

---

## Key Files

| File | Purpose |
|------|---------|
| `src/constants.ts` | OAuth credentials, endpoints, headers, system prompts |
| `src/antigravity/oauth.ts` | OAuth authorization URL + token exchange |
| `src/plugin/token.ts` | Token refresh (sends client ID every ~1 hour) |
| `src/plugin/request.ts` | Core request transformation (body wrapping, header stripping) |
| `src/plugin.ts` | Main fetch interceptor, account rotation |
| `src/plugin/fingerprint.ts` | Device fingerprint generation |
| `package.json` | npm package identity |

---

## Suggested Skills for Next Session

- **`explain-it-v2`** — If you need to understand any specific file or code pattern
- **`grill-me`** — If you want to stress-test the implementation plan before coding
- **`close`** — To wrap up the next session with proper documentation

---

## Notes

- The user's goal is **personal ban avoidance**, not making the project safer for all users
- The analysis confirmed the user's suspicion: the OAuth client ID is hardcoded and shared across all installs
- The user understands this is an arms race with Google and accepts the risks
