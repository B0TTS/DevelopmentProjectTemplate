# Handoff — OpenCode Web-Access Skill

**Date:** 07-21-2026
**Session goal:** Add free web-search + "use my browser" capabilities to OpenCode (mirroring pi's ExaSearch + fetch_content), then create a skill teaching agents how to use them.

## What was accomplished

### 1. Deep research (complete)
Researched free/OSS plugins + MCP servers that give OpenCode pi-style web access on Windows. Findings:

**Web search (free, no API key):**
- **`opencode-metasearch2`** (chosen) — MIT, OpenCode plugin, ships prebuilt `win32-x64` binary, local metasearch2 engine aggregating Google/Bing/Brave, no API key. Exposes `web_search` tool.
- Alternatives: `opencode-scout` (Exa/TinyFish/Gemini), `opencode-search` (DDG/Wikipedia/MDN), SearXNG MCP (self-hosted), DuckDuckGo/free-search MCPs.
- Freemium: Brave (2k/mo), Tavily (1k/mo), Exa (already installed), Jina Reader.

**Browser / "use my browser":**
- **Playwright MCP** (`@playwright/mcp`, Apache-2.0) — official Microsoft, `--cdp-endpoint http://localhost:9222` attaches to real logged-in Chrome. Best free/OSS fit.
- **Browser MCP by Agent360** (`@agent360/browser-mcp`, MIT) — real Chrome + CAPTCHA solving + 2FA handling, Chrome extension required. Top upgrade.
- **browser-mcp-cdp** (`zhiqi-li/browser-mcp-cdp`, MIT) — real Chrome via CDP with profile-snapshot isolation.
- **opencode-cloak-fetch** — plugin is MIT but the CloakBrowser *binary* is not fully free (delayed free-release; v146 free/stale, Pro $19-49/mo). Rejected per "free" requirement.

### 2. Config change (complete)
Added `opencode-metasearch2` to `C:/Users/Jonah/DevelopmentTemplate/.opencode/opencode.json`:
```jsonc
"plugin": ["opencode-metasearch2"]
```
JSON validated; existing MCPs (context7, docs-mcp-server, exa) + 35 agents intact. Takes effect on next OpenCode restart.

### 3. Skill creation (IN PROGRESS — not started writing)
Invoked `write-a-skill` skill, then `grill-me` to stress-test the design. Grilling surfaced 3 codebase facts that reshape the skill:

1. **OpenCode natively supports skills** — loaded on-demand via `skill` tool from `.opencode/skills/<name>/SKILL.md` (project) or `~/.config/opencode/skills/<name>/SKILL.md` (global). Frontmatter: `name` + `description` (1-1024 chars). Name must match dir, regex `^[a-z0-9]+(-[a-z0-9]+)*$`.
2. **User publishes an npm skills package** `@b0tts/opencode-skills` synced to `~/.config/opencode/opencode-skills/skills/` via `skills-lock.json` (contains grill-me, write-a-skill, to-prd, caveman, etc.).
3. **Researcher agents already embed web-lookup guidance inline** — see `C:/Users/Jonah/DevelopmentTemplate/.opencode/agents/gsd-phase-researcher.md` `<documentation_lookup>` block: Context7-first with `ctx7` CLI fallback, `[VERIFIED]/[CITED]/[ASSUMED]` provenance tags.

### Critical finding — tool-name collision bug (affects skill design)
Documented OpenCode bug: the **mimo-v2.5** model (used by ~33 of the user's 35 agents via `xiaomi-token-plan-sgp/mimo-v2.5-pro`) calls **phantom tool names** `websearch` and `web_search_exa` instead of the real wrapped names:
- `websearch_web_search_exa` (OpenCode's wrapped Exa search)
- `websearch_web_fetch_exa` (wrapped Exa fetch)
- `web_search` (from metasearch2 plugin — coexists)
- `mcp__context7__*`, `webfetch` (built-in)

## Current state & open decisions

**Open question posed to user (unanswered when session ended):** Skill vs. inline-patch vs. both?

Recommended answer (was being grilled):
- **Skill** (`web-access`) → routing logic: which tool for which job (free vs paid, docs vs web, fetch vs search). Load-on-demand, reusable → candidate for `@b0tts/opencode-skills` package.
- **Inline patch** to researcher agent `.md` files → one-line tool-name pin (correctness fix, must be always-on, matches existing inline convention in `gsd-phase-researcher.md`).
- **Recommendation: both**, split by purpose.

Grilling was at Q1 of the decision tree. Next questions to resolve (per grill-me skill, one at a time):
- Q2: Where does the skill live — project `.opencode/skills/` or global `~/.config/opencode/skills/` (or published via `@b0tts/opencode-skills`)?
- Q3: Scope — full web-access stack (search + docs + fetch + browser) or just the free search tools?
- Q4: Should the skill also encode the provenance-tag convention (`[VERIFIED]/[CITED]/[ASSUMED]`) from the researcher agents, or leave that in the agent files?
- Q5: Browser MCP — do we add Playwright MCP / Browser MCP by Agent360 to config now, or leave out of scope for this skill cycle?

## Suggested skills for the next session

- **`write-a-skill`** (`.agents/skills/write-a-skill/SKILL.md`) — already invoked; follow its process: gather reqs → draft → review with user. SKILL.md template + structure rules there.
- **`grill-me`** (`.agents/skills/grill-me/SKILL.md`) — resume grilling the design tree one question at a time; finish Q1, then Q2-Q5.
- **`create-nav-guide`** (`.agents/skills/create-nav-guide/SKILL.md`) — optional: the research roundup (free search + browser MCP landscape with ready-to-paste configs) is worth saving as a reusable NavGuide in `b0ttsagent/NavGuides/`. Was offered to user, not yet actioned.

## Key files, paths, and commands

**Config (edited this session):**
- `C:/Users/Jonah/DevelopmentTemplate/.opencode/opencode.json` — added `"plugin": ["opencode-metasearch2"]`. Existing MCPs: context7, docs-mcp-server (remote, `http://100.122.184.37:6280/mcp`), exa (`https://mcp.exa.ai/mcp`).
- `C:/Users/Jonah/.config/opencode/opencode.jsonc` — global OpenCode config (Ollama provider only).

**Skill locations (OpenCode native skill discovery):**
- Project: `.opencode/skills/<name>/SKILL.md`
- Global: `~/.config/opencode/skills/<name>/SKILL.md`
- Published package: `~/.config/opencode/opencode-skills/skills/<name>/SKILL.md` (synced via `skills-lock.json`, source = `npm:@b0tts/opencode-skills`)

**Existing inline web-guidance (the convention to match):**
- `C:/Users/Jonah/DevelopmentTemplate/.opencode/agents/gsd-phase-researcher.md` — see `<documentation_lookup>` + provenance tag rules.
- Other researcher agents with similar blocks: `gsd-project-researcher.md`, `gsd-ui-researcher.md`, `gsd-ai-researcher.md`, `gsd-domain-researcher.md`, `gsd-advisor-researcher.md`, `gsd-research-synthesizer.md`.

**pi reference (the experience to mirror):**
- `C:/Users/Jonah/.pi/web-search.json` — `{"provider":"exa","workflow":"auto-summary",...}`
- `C:/Users/Jonah/.pi/agent/mcp.json` — pi's docs + context7 MCPs.
- `C:/Users/Jonah/.pi/agent/settings.json` — pi packages incl. `pi-web-access`.

**Useful commands:**
- Validate opencode.json: `cd C:/Users/Jonah/DevelopmentTemplate && node -e "require('./.opencode/opencode.json')" && echo OK`
- List OpenCode skills a session sees: check `skill` tool's `<available_skills>` block at session start.
- Apply config change: restart OpenCode (plugin auto-installs via Bun to `~/.cache/opencode/node_modules/`).

## Residual risks / things to verify next session

- **mimo tool-name bug unconfirmed in user's exact build** — the bug reports are from `anomalyco/opencode` issues; verify whether the user's OpenCode version still exhibits it before deciding inline patch is necessary. If fixed upstream, skill-only may suffice.
- **metasearch2 Windows first-run** — confirm `@galelmalah/metasearch2-win32-x64` optional dependency installs cleanly via Bun on Windows; fallback is `cargo install metasearch` (needs Rust). User hasn't restarted OpenCode yet to test.
- **metasearch2 rate-limiting** — scrapes public search UIs; heavy/bursty use triggers Google CAPTCHAs/IP blocks (transient, falls back to Bing/Brave). Fine for normal agent use; keep Exa for bulk research.
- **Scope creep** — browser MCP was researched but not added to config; decide explicitly whether it's in this skill's scope or a separate follow-up.
