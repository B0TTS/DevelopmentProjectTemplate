# opencode-agents research — b0tts-lead-researcher / b0tts-researcher build

Research date: 2026-08-17. Findings backing the two agent files in `.opencode/agents/`.

## opencode agent format facts (verified)

- Valid frontmatter fields: `description, mode, model, variant, prompt, temperature, top_p, steps, permission, disable, hidden, color, options`. `tools` is DEPRECATED — use `permission` instead. Unknown fields pass through silently as provider model options (that is why `reasoningEffort` works in opencode.json agent config). Source: https://opencode.ai/docs/agents/
- `.opencode/agents/` is scanned RECURSIVELY (`{agent,agents}/**/*.md`); nested .md files become agents named by subpath. **Never put research/notes .md files under `.opencode/agents/`** — that is why build research lives here, not in an `agents/<name>/research/` subfolder.
- `mode: subagent` = invocable via task/@-mention, not Tab-selectable, cannot be `default_agent`. Default mode is `all`.
- `subagent_depth` is top-level config only (project has 2). Default 1. No per-agent override — leaf spawning is blocked per-agent via `permission: { task: deny }`.
- `permission: { task: deny }` removes targets from the Task tool description; `{ task: { "*": allow } }` opens spawning. Last matching rule wins; agent permission overrides top-level.
- Model inheritance: subagent without `model` uses the invoking agent's model. The task tool has no model-override parameter → per-agent model pinning happens in `opencode.json` `agent.<name>.model`.
- MCP tools are available to subagents by default (gate via permission wildcards, e.g. `searxng_*`).
- If `permission`/`tools` is omitted the agent gets ALL tools — restriction must be explicit.

## Design patterns adopted (cross-harness, sourced)

- Lead plans/spawns/synthesizes; leaf researches. Lead gets spawn capability, no web tools (Anthropic multi-agent research system).
- Delegate with a full spec: objective, output format, tool/source guidance, boundaries (Anthropic multi-agent research system).
- Leaf: narrow tool surface = blast radius; persists full findings to disk, returns lightweight refs; final message condensed/structured — status, paths, verdict, one-line reason (Anthropic multi-agent research system + effective context engineering).
- Orchestrator/lead sees summaries only; never full outputs (Anthropic multi-agent research system).
- Retry transient failures once; second failure → record and move on; disk = memory for resume (manifest → spec → recent files re-read order) (Anthropic managed-agents cookbook; CCA community guide).
- Standing role prompt stays domain-agnostic; per-task specifics injected via spec files (Claude Code subagents docs).

## Update instructions for these agents

- Agent behavior changes → edit the `.md` file directly; restart opencode (config loads once at startup).
- Model changes → `opencode.json` `agent.<name>.model` (leaf is pinned to `opencode-go/deepseek-v4-flash`; lead inherits parent at spawn).
- To widen/narrow tool surface → edit `permission` frontmatter; never add nested .md files under `.opencode/agents/`.
- Verify format changes against https://opencode.ai/config.json and https://opencode.ai/docs/agents/.
