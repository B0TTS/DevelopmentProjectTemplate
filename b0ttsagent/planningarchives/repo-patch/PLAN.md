# PLAN — Antigravity 

## Technical Context

| Field | Value |
|---|---|
| Language/Version | TypeScript (strict, ESNext, `verbatimModuleSyntax`, `noUncheckedIndexedAccess`) |
| Primary Dependencies | `zod ^4`, `@opencode-ai/plugin`, `@openauthjs/openauth`, `proper-lockfile`, `xdg-basedir` |
| Storage | `~/.config/opencode/antigravity.json` (config) + `antigravity-accounts.json` (creds) |
| Testing | Vitest 3 (colocated `*.test.ts`, ESM) |
| Target Platform | Node (win32/darwin) |
| Performance Goals | No regression vs baseline (same request count, same latency profile) |
| Constraints | Config-driven; local build only; de-bulk not blend-in; build stays green; no new shared constants — see `CONTEXT.md` Constraints & Principles |
| Scale/Scope | Single repo, ~10 files touched, ~6 phases |

## Strategy

**Layer ordering: credential → transport → payload → auxiliary.**

Each layer sheds shared identifiers independently, so partial progress still
reduces ban risk. The ordering is chosen so the highest-impact, lowest-risk
changes ship first:

- **Credential layer** (Phase 1) is highest-*impact* — it de-correlates the user
  from every other plugin install at the OAuth-account level (the #1 bulk-ban
  vector identified in the prior analysis).
- **Payload layer** (Phase 3) is highest-*detection* — the in-band identity
  broadcasts (`ANTIGRAVITY_SYSTEM_INSTRUCTION`, body `userAgent`, `requestId`
  prefix, `ideType` in `loadCodeAssist` body) are present in every model
  request and are trivially grep-able by Google. Phase 3 comes after
  credential because it is more likely to break the live API and requires
  resolving Open Questions #1 and #2.
- **Transport layer** (Phase 2) sits between — header changes are lower-risk
  than body changes but depend on the config loader from Phase 0.
- **Auxiliary** (Phase 4) is independent and parallelizable with Phase 1.

**The disguise principle:** config-driven replacements mean each layer can be
rolled back via a config flip (not a code revert) if it breaks the live API.
This makes the irreversible-looking changes safely reversible.

---

## Phase 0 — Prep & baseline

- [ ] Capture test baseline: run `npm test` in `opencode-antigravity-auth/`,
  save pass/fail snapshot for comparison
- [ ] Grep inventory: enumerate every occurrence of shared identifiers across
  `src/` — `ANTIGRAVITY_CLIENT_ID`, `ANTIGRAVITY_CLIENT_SECRET`,
  `ANTIGRAVITY_DEFAULT_PROJECT_ID` (`rising-fact-p41fc`), `ANTIGRAVITY_SYSTEM_INSTRUCTION`,
  `"ANTIGRAVITY"` (ideType), `"antigravity"` (body userAgent), `requestType: "agent"`,
  `"agent-"` (requestId prefix), `SKIP_THOUGHT_SIGNATURE`,
  `CLAUDE_TOOL_SYSTEM_INSTRUCTION`, `antigravity-auto-updater` URL,
  `cclog` / `experimentsandconfigs` scopes. Document in REFERENCES §1.
- [ ] Extend config schema in `src/plugin/storage.ts` (Zod schema) and
  `assets/antigravity.schema.json` with optional fields:
  `oauth_client_id`, `oauth_client_secret`, `project_id`, `ide_type`,
  `system_instruction_mode`, `user_agent_prefix`, `api_client_pool`,
  `version_fetch_url`, `request_id_prefix`, `oauth_scopes`
- [ ] Add config loader helpers: read new fields with fallback to current
  hardcoded values (allows incremental rollout — de-bulk layer by layer
  without breaking auth before config is populated)
- [ ] Update affected tests: any test importing the soon-to-be-removed
  constants needs to be updated to pass new config values via test fixtures

**Exit gate:** `npm run build` + `npm test` + `npm run typecheck` exit 0;
inventory documented in REFERENCES §1; schema accepts new fields; config
loader returns hardcoded fallback values when fields absent.

---

## Phase 1 — Credential layer [P]

- [ ] Add config resolution for `oauth_client_id` / `oauth_client_secret` via
  the Phase 0 loader
- [ ] Rewire `authorizeAntigravity()` in `src/antigravity/oauth.ts` to read
  client ID from config (not `ANTIGRAVITY_CLIENT_ID` constant)
- [ ] Rewire `exchangeAntigravity()` in `src/antigravity/oauth.ts` to read
  client ID + secret from config
- [ ] Rewire `refreshAccessToken()` in `src/plugin/token.ts` to read client ID
  + secret from config
- [ ] Remove `ANTIGRAVITY_CLIENT_ID` and `ANTIGRAVITY_CLIENT_SECRET` exports
  from `src/constants.ts`
- [ ] Add config resolution for `project_id`; remove
  `ANTIGRAVITY_DEFAULT_PROJECT_ID` (`"rising-fact-p41fc"`) from `src/constants.ts`
- [ ] Make `ANTIGRAVITY_REDIRECT_URI` config-driven (personal OAuth client may
  require a different port than `51121`)
- [ ] Write setup docs: personal Google Cloud OAuth client walkthrough (see
  REFERENCES §2) — Web application type, redirect URI, enable Cloud Code Assist
  API, copy client ID/secret into `antigravity.json`
- [ ] Update tests: `src/antigravity/oauth.test.ts` (if exists),
  `src/plugin/token.test.ts` (if exists) — inject test config values

**Exit gate:** No hardcoded OAuth credentials or project ID in `src/`;
`opencode auth login` succeeds with personal credentials; token refresh
succeeds.

**[P]:** parallelizable with Phase 4 (different files, no deps).

---

## Phase 2 — Transport layer

- [ ] Resolve Open Question #2 (ideType): make `Client-Metadata` `ideType`
  config-driven; default to `"IDE_UNSPECIFIED"` [NEEDS CLARIFICATION: what does
  legit Gemini CLI traffic send?] or a user-supplied value
- [ ] Update `getAntigravityHeaders()` in `src/constants.ts` to read `ide_type`
  from config (not hardcoded `"ANTIGRAVITY"`)
- [ ] Update `getRandomizedHeaders()` in `src/constants.ts` to read `ide_type`
  from config
- [ ] Update `generateFingerprint()` in `src/plugin/fingerprint.ts` to use
  config-driven `ideType` (not hardcoded `"ANTIGRAVITY"`)
- [ ] Update `collectCurrentFingerprint()` in `src/plugin/fingerprint.ts`
  likewise
- [ ] Make User-Agent prefix config-driven via `user_agent_prefix` (replace
  `antigravity/` with config value or neutral Chrome UA)
- [ ] Update `buildFingerprintHeaders()` in `src/plugin/fingerprint.ts` to use
  the config-driven UA prefix
- [ ] Make `X-Goog-Api-Client` pool config-driven via `api_client_pool`
  (custom list or neutral default — not `vscode_cloudshelleditor/0.1` etc.)
- [ ] Update tests covering headers + fingerprint

**Exit gate:** No `"ANTIGRAVITY"` string in any header path; headers work with
config-driven values.

---

## Phase 3 — Payload layer

- [ ] Resolve Open Question #1 (system instruction): drop or replace
  `ANTIGRAVITY_SYSTEM_INSTRUCTION` based on decision; make config-driven via
  `system_instruction_mode` (`"drop"` | `"neutral"` | `"custom"`)
  [NEEDS CLARIFICATION: does the model expect an identity prompt to function,
  or is it cosmetic?]
- [ ] Remove body `userAgent: "antigravity"` field in the wrapped body
  (`src/plugin/request.ts`) or make config-driven
- [ ] Remove hardcoded `requestType: "agent"` in `src/plugin/request.ts` or
  make config-driven (only affects `headerStyle === "antigravity"` path)
- [ ] Remove `"agent-"` requestId prefix in `src/plugin/request.ts` or make
  config-driven via `request_id_prefix`
- [ ] Strip `ideType: "ANTIGRAVITY"` from `loadCodeAssist` body in
  `src/antigravity/oauth.ts` (`fetchProjectID`) and `src/plugin/project.ts`
  — use config-driven value from Phase 2
- [ ] Address `SKIP_THOUGHT_SIGNATURE` sentinel (`"skip_thought_signature_validator"`)
  in `src/constants.ts`: make config-driven or replace with non-sentinel
  approach [NEEDS CLARIFICATION: is the sentinel required for the API to accept
  thinking blocks, or can it be omitted?]
- [ ] Address `CLAUDE_TOOL_SYSTEM_INSTRUCTION` in `src/constants.ts`: drop or
  make config-driven via `system_instruction_mode`
- [ ] Update `src/plugin/request.test.ts` and `src/plugin/request-helpers.test.ts`
  (if exists) to reflect removed/config-driven payload fields

**Exit gate:** No `"antigravity"` / `"ANTIGRAVITY"` / `"agent-"` strings in
request bodies or system instructions; model call returns a completion.

**Risk / Rollback:** if Phase 3 breaks the live API, revert order:
1. Restore `requestType` (most likely to affect API routing)
2. Restore body `userAgent` field
3. Restore `ANTIGRAVITY_SYSTEM_INSTRUCTION`
Each is independently revertible — config-driven makes this a config flip in
`antigravity.json`, not a code revert. Keep the fallback values in the config
loader precisely so this rollback path exists.

---

## Phase 4 — Auxiliary vectors [P]

- [ ] Make version fetch URL config-driven via `version_fetch_url` in
  `src/plugin/version.ts` (`VERSION_URL`) — replace
  `antigravity-auto-updater-974169037036.us-central1.run.app` with a
  user-supplied URL or neutral fallback (changelog scrape only)
- [ ] Resolve Open Question #4 (OAuth scopes): make `ANTIGRAVITY_SCOPES` in
  `src/constants.ts` config-driven via `oauth_scopes`; drop `cclog` and
  `experimentsandconfigs` if not required for Cloud Code Assist API
  [NEEDS CLARIFICATION: are these scopes required for the API to function,
  or only for Antigravity-specific features the user doesn't need?]
- [ ] Update tests covering version fetch + OAuth scopes

**Exit gate:** No `antigravity-auto-updater` URL in source; OAuth scopes
resolved (either dropped or config-driven).

**[P]:** parallelizable with Phase 1 (different files, no deps).

---

## Phase 5 — Verification & hardening

- [ ] `npm run build` exits 0
- [ ] `npm run typecheck` exits 0
- [ ] `npm test` exits 0 (matches or exceeds Phase 0 baseline)
- [ ] Live smoke test: `opencode auth login` with personal credentials, then
  a model call (`opencode run "Hello" --model=google/antigravity-gemini-3-flash`)
  returns a completion
- [ ] Grep audit: confirm no shared identifier from upstream reaches outgoing
  requests — `grep` `src/` for each identifier string cataloged in REFERENCES §1
- [ ] Verify success criteria 1-3 from `CONTEXT.md` all pass

**Exit gate:** All three CONTEXT success criteria pass.

---

## Phase 6 — Maintenance

- [ ] Write patch re-apply docs: how to re-apply changes after an upstream
  `opencode-antigravity-auth` update (the upstream package updates frequently)
- [ ] Document upstream-drift warning + the config-driven seam as the
  maintenance surface (re-apply = re-add config fields to schema; values
  persist in `antigravity.json` across reinstalls)
- [ ] Test re-apply procedure on a clean upstream checkout

**Exit gate:** Maintenance docs written; re-apply procedure validated.

---

## What we are explicitly NOT doing

1. Blend-in strategy (mimicking legit Antigravity IDE traffic)
2. Upstream PR to `NoeFabris/opencode-antigravity-auth`
3. Multi-account fingerprint randomization beyond existing behavior
4. Reverse-engineering legit Antigravity traffic
5. Ban-free-window measurement (Open Question #3 — deferred, not short-term
   measurable)

---

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| Config-driven for static strings (system instruction, sentinel) | Survives upstream rebases; user can toggle without rebuild | Hardcode replacement: lost on npm reinstall of upstream; brittle to diffs |
| Optional config fields with hardcoded fallback | Allows incremental rollout (de-bulk layer by layer without breaking auth before config is populated) | Immediate removal: breaks auth flow before user populates `antigravity.json` |
| Config-driven OAuth scopes (rather than fixed minimal set) | User may need different scopes for different Google Cloud project configurations; avoids re-coding when Google changes scope requirements | Fixed minimal set: requires code change + rebuild when Google changes requirements |

---

## Sequencing summary

| Phase | Layer | Parallelizable | Risk reduced | Effort |
|---|---|---|---|---|
| 0 — Prep & baseline | — | no | none (enables later phases) | S |
| 1 — Credential | credential | yes (with 4) | OAuth client ID correlation (P0) | M |
| 2 — Transport | transport | no | header fingerprinting (P2) | S |
| 3 — Payload | payload | no | in-band identity broadcasts (P0/P1) | M |
| 4 — Auxiliary | auxiliary | yes (with 1) | version fetch URL, OAuth scopes (P3) | S |
| 5 — Verification | — | no | none (validates) | S |
| 6 — Maintenance | — | no | none (sustains) | S |

Effort: S = small (< 1 hour), M = medium (1-3 hours), L = large (> 3 hours).
