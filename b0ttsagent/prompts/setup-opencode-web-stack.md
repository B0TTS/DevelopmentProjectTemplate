# Prompt: Set Up OpenCode Web Stack (Parity with Pi) — via b0tts-general-agent

> Paste everything below the line into a fresh OpenCode session in this repo (C:/Users/Jonah/DevelopmentProjectTemplate).

---

Set up OpenCode's web research stack to match Pi's newly updated web-access setup. You will NOT do the config work yourself — **spawn the `b0tts-general-agent` subagent and have it do all MCP config and skill config work end-to-end.** Your job is planning, handing it a precise task spec, and verifying its output.

## Context (verified facts — do not re-test)

- **SearXNG is deprecated. It does not work anymore.** Do not test it, do not call it, do not keep it in any routing order. Take this as given — the instance returns empty or Wikipedia-only results for nearly all real queries.
- Working search providers (verified on the Pi side): **exa, tavily, firecrawl, serper**. API keys for all four are already stored in `C:/Users/Jonah/.pi/web-search.json` (read that file for the key values — do not ask me for them, do not invent placeholders).
- Pi's equivalent skill (`C:/Users/Jonah/.pi/agent/skills/pi-web-search/SKILL.md`) was just updated: searxng forbidden, auto-routing bypassed in favor of explicit providers, You.com tools documented. Read it first as the reference for tone and structure — but OpenCode has no You.com tools; its stack is the built-in `websearch` (Exa), the `opencode-metasearch2` plugin, and the `context7` MCP server.
- The existing skill `.agents/skills/opencode-web-research/SKILL.md` currently routes "SearXNG-first" — that routing is now wrong and must be replaced.

## Spawn `b0tts-general-agent` with this task

Hand the subagent this spec (it may adapt phrasing, not scope):

1. **Disable the searxng MCP server** in `.opencode/opencode.json` — set `"enabled": false` on the `searxng` entry (or remove the entry entirely; do not touch the `context7` entry or anything else in the file). Surgical change only — no drive-by refactoring of the config.
2. **Wire the verified providers into the `opencode-metasearch2` plugin** config (in `.opencode/opencode.json` or wherever that plugin reads provider keys — check its docs in `node_modules` or its README). Add exa, tavily, firecrawl, and serper using the keys from `C:/Users/Jonah/.pi/web-search.json`. langsearch has a key but no usable provider slot — skip it.
3. **Rewrite the routing section of `.agents/skills/opencode-web-research/SKILL.md`**: remove every SearXNG reference and the searxng-first route. New routing order: built-in `websearch` (Exa) first → `opencode-metasearch2` providers (exa/tavily/firecrawl/serper) as fallback → `context7` for library/API docs → `webfetch` for known URLs. Keep the rest of that skill intact (its tool inventory, the 2/4/8 hard query minimums, the NOT-for boundaries). Add one line noting the searxng MCP server is deprecated and must not be re-enabled.

## Verification (do AFTER the subagent finishes)

- `node -e "require('./.opencode/opencode.json')"` (or equivalent JSON parse) — config still valid.
- Diff review: every changed line in `opencode.json` and the skill traces to the three tasks above.
- Confirm `context7` MCP entry untouched.
- **Do NOT run live searches against searxng to "confirm" it's broken — I already told you it is. Do NOT run extensive live-search test suites.** A single sanity search through the new default path (websearch/Exa) is allowed if needed.

## Constraints

- Follow `AGENTS.md` rules (check for applicable skills before implementing).
- Do not modify anything under `C:/Users/Jonah/.pi/` — Pi's config is already done and correct.
- Do not commit.
- Report back: what the subagent changed, file paths, verification results, and anything it could not complete.
