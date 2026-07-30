# CONTEXT — FirstFix

## What I Want

I want to keep using `opencode-antigravity-auth` (the plugin that routes OpenCode to Google Antigravity models) **without my Google accounts getting banned or shadow-banned**.

Google is actively detecting and suspending accounts that use this plugin. The README already warns about it; users in the community are reporting bans; and the troubleshooting section documents `rising-fact-p41fc` 403 lockouts, which means Google has already started clamping down on the shared fingerprints this plugin broadcasts.

I want my **personal installation** to stop looking like every other `opencode-antigravity-auth` user in the eyes of Google's detection systems.

## Scope

**In scope:** Modifying my local copy of the `opencode-antigravity-auth` codebase at `C:\Development\Projects\opencode-antigravity-auth\opencode-antigravity-auth` so that traffic originating from my machine does not match the fingerprints Google is currently using to mass-ban users.

**Out of scope:**
- Making the upstream npm package safer for other users. This is **personal ban avoidance**, not a public fix. I will not be submitting PRs upstream.
- Supporting other users' setups. The solution only needs to work for me, on my machine, with my accounts.
- Reimplementing the plugin from scratch. I want the smallest set of changes that removes the detectable fingerprints while keeping the plugin functional.
- Defeating every conceivable future detection vector. This is an arms race; I accept that. The goal is to close the vectors that are *currently* obvious and cheap for Google to detect.

## What Success Looks Like

1. My accounts stop getting banned/shadow-banned when using the plugin for normal coding work.
2. The plugin still works — auth login, token refresh, model requests, multi-account rotation all still function.
3. The build passes (`npm run build`) and tests pass (`npm test`).
4. No new hardcoded shared identifiers are introduced in the process (e.g., I don't swap one shared OAuth client ID for another shared one).
5. The changes are isolated to my local checkout — I can pull upstream updates and re-apply my patches without a full rewrite.

## What I Already Know

A prior analysis (see `b0ttsagent/handoffs/06-25-2026/antigravity-ban-avoidance-analysis.md`) identified the **shared hardcoded OAuth Client ID** as the primary ban vector. Every install of the npm package sends the same `ANTIGRAVITY_CLIENT_ID` to Google during auth, token exchange, and hourly token refresh — Google can enumerate and ban all accounts using that client ID in bulk.

A follow-up review of that analysis found it was **incomplete**. It missed several identity broadcasts that are arguably just as dangerous and present in *every* request, not just auth flows:

- The literal string `"You are Antigravity..."` injected into `systemInstruction` on every request
- `"ideType":"ANTIGRAVITY"` in the `Client-Metadata` header on every request
- `"userAgent":"antigravity"` as a field in the request *body* (separate from the HTTP header)
- `"ideType":"ANTIGRAVITY"` in `loadCodeAssist` and project-discovery request bodies
- The `agent-` prefix on `requestId` values
- The `antigravity/` User-Agent prefix
- Antigravity-specific OAuth scopes (`cclog`, `experimentsandconfigs`)
- A non-standard `SKIP_THOUGHT_SIGNATURE` sentinel string in thinking-block signatures
- Version fetch from a known Antigravity auto-updater endpoint

Swapping only the OAuth client ID (the prior plan's Phase 1) would leave all of these in place. A complete first fix has to address the full set of identity leaks, not just the client ID.

## Constraints & Assumptions

- **I accept the ToS risk.** Using this plugin violates Google's Terms of Service regardless of fingerprinting. The goal is risk reduction, not ToS compliance.
- **I accept this is an arms race.** Google can add new detection vectors at any time. This fix targets the *currently known* vectors.
- **I must keep the plugin functionally equivalent.** Account rotation, quota fallback, thinking-block recovery, multi-account load balancing, etc. must all still work. The fix is about *disguise*, not *features*.
- **I am willing to provision my own Google Cloud OAuth client** if that's what it takes to shed the shared client ID.
- **Build must stay green.** `npm run build` and `npm test` must pass after the changes.

## Non-Goals

- Removing the system instruction entirely if doing so degrades model behavior. (The instruction may need to be *replaced* with a neutral one, not deleted, if the model expects an identity prompt.)
- Hiding the fact that I'm hitting Google's Cloud Code Assist API at all. Network-level obfuscation (proxies, IP rotation, etc.) is out of scope for this fix.
- Bundling changes for distribution. I'm patching my local checkout.
