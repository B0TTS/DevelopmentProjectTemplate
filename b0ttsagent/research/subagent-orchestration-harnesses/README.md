# Sub-Agent Orchestration Harnesses & 3-Tier Hierarchies

Research note — synthesized from 4 parallel research sub-agents, Aug 2026.
Sources verified by reading pages; links are canonical.

## The pattern you described (orchestrator → phase executor → worker subagents)

This is the classic **orchestrator-workers** pattern (Anthropic: "Building effective agents"). For a *3-tier* version — an orchestrator that spawns per-phase executors that themselves spawn workers — harness support breaks down like this:

| Harness | Subagent nesting depth | Parallel fanout | Context isolation | License/cost |
|---|---|---|---|---|
| **opencode** | `subagent_depth` config, default **1** (primaries only), **2** = one extra tier | Yes — multiple `task` calls in one message; experimental `background: true` | Fresh context per invocation; `task_id` resumes same subagent session | MIT, free |
| **Claude Code** | **3 layers** default (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`) | Yes — concurrent subagents, cap 20; background agents; `--worktree` + `isolation: worktree` | Fresh context per subagent (own model's window), auto-compaction, transcripts | Paid API |
| **Cursor** | **2 levels** (subagent → sub-subagent, no deeper) | Yes — parallel Task calls, foreground/background/cloud | Own context, resumable by agent ID | Proprietary |
| **Gemini CLI** | **None** (recursion protection) | Yes — parallel | Own loop, returns summary | OSS (Apache-2.0) |
| **Goose** | **None** | Yes — sequential or parallel, trigger keywords | Configurable return mode (full/summary), max turns | OSS (Apache-2.0) |
| **OpenHands** | Arbitrary (programmatic) | **No — sequential by design** | Resumable `task_id` | OSS (MIT) |
| **Codex CLI** | Undocumented | Yes — parallel, wait-all, concurrency cap | Fresh context | OSS (Apache-2.0) |
| **Amp** | Unknown (docs silent) | Yes | Fresh, final summary only | Paid SaaS |
| **Crush** | Unknown (loop detection only) | Yes (~10 concurrent observed) | Child sessions, cost rollup | OSS (custom) |
| **Aider** | None (architect/editor dual-model only) | No | — | OSS (Apache-2.0) |
| **Warp/Oz** | **Exactly 1 level** | Strong — fan-out/in, DAG, swarm, supervisor/worker | Parent/child runs, durable message bus | Paid |

**Best fits for a strict 3-tier tree today:** opencode (`subagent_depth: 2`), Claude Code (3 layers native), Cursor (2 levels native).

## opencode specifics (your harness)

- **Config:** agents defined in `opencode.json(c)` or Markdown in `.opencode/agent/` / `~/.config/opencode/agent/`. Fields: `description` (required), `prompt`, `model`, `temperature`, `steps`, `permission`, `mode` (`primary|subagent|all`), `hidden`.
- **Permissions per agent** (`allow|ask|deny`): `read`, `edit`, `glob`, `grep`, `list`, `bash`, `task`, `external_directory`, `todowrite`, `webfetch`, `websearch`, `lsp`, `skill`, `question`, `doom_loop`. `bash`/`task` accept glob patterns, last-match-wins.
- **Nesting:** global `subagent_depth` (default 1 → primaries can spawn; 2 → subagents can spawn; 0 → nobody can). Set **2** for orchestrator → executor → workers. Source walks the `parentID` chain to enforce it. Undocumented per-agent `task_budget` + `level_limit` (default 5) exist in a merged PR (#7756) but aren't in official docs.
- **Parallel:** the Task tool's own instructions tell agents to "launch multiple agents concurrently... a single message with multiple tool uses." `background: true` (experimental, `OPENCODE_EXPERIMENTAL_BACKGROUND_SUBAGENTS=true`) is the async variant.
- **Context:** every agent invocation starts fresh unless `task_id` is passed (resumes that subagent's session). Handoffs = task_id resume or files on disk.
- **Model assignment:** per-agent `model` override; subagents inherit the invoking agent's model if unset — useful for cheap worker models under an expensive orchestrator.
- **Community setups:** `oh-my-opencode-slim` (~7k stars — orchestrator + specialist agents, background dispatch with a job board), `aptdnfapt/opencode-parallel-agents` (`/multi @deepseek @claude @qwen` parallel fanout + synthesis), dev.to "Agent Orchestration in OpenCode" + Orchestrator.md gist (minimal permission-restricted orchestrator).

## Claude Code specifics

- **Config:** `.claude/agents/*.md` with YAML frontmatter: `name`, `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `isolation`.
- **Spawning:** the Agent tool (formerly Task); auto-delegation on `description` match or @-mention. Deny the Agent tool to block delegation.
- **Nesting:** default 3 subagent layers; `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` to change (1 = no nesting). At the limit the Agent tool is withheld.
- **Parallel:** concurrent subagents (cap 20), background subagents (default in SDK), `Ctrl+B`. `--worktree <name>` per-session git isolation; subagent frontmatter `isolation: worktree` gives each its own temp checkout; `/batch` skill splits work into 5–30 worktree-isolated subagents, each opening a PR.
- **Context:** fresh window per subagent (own model's context size), auto-compaction per subagent, transcripts at `~/.claude/projects/.../subagents/*.jsonl`. Agent SDK resume via `resume: sessionId`.
- **SDK:** no dedicated `spawnAgent()` — the model spawns via the Agent tool; you just include `"Agent"` in `allowedTools`. Reference: `anthropics/claude-agent-sdk-demos/research-agent` (Lead → parallel Researchers → Data Analyst → Report Writer).

## The phased-execution orchestrator you described

Your description (orchestrator dispatches per-phase executors that spawn subagents) is essentially what **GSD** already implements — which you have installed:
- Thin orchestrator → parallel researchers → planner → plan-checker loop → **executors with fresh ~200k context each**, atomic commit per task, main session kept at ~30–40% context.
- Waves of parallel-but-independent executors to avoid collisions (same idea as Claude Code `/batch` worktrees).
- References: github.com/gsd-build/get-shit-done, gsd-opencode port, `gsd-plan-phase` SKILL.md (orchestrator role: "spawn gsd-planner, verify with gsd-plan-checker, iterate until pass").

Other real-world examples of the same shape: Anthropic's multi-agent research system (lead spawns 3–5 parallel subagents; ~90% eval gain, ~15× token cost), Augment Intent (coordinator → implementors in dependency-ordered waves in isolated worktrees → verifier), OpenAI Codex CLI orchestrated via Agents SDK (project-manager → designer/frontend/backend/tester team).

## Context isolation & handoffs

- Fresh-context subagents keep the orchestrator's window clean; subagents return condensed summaries (~1–2k tokens per Anthropic's context-engineering guidance).
- `HANDOFF.md` conventions converge on: goal, completed/not-done, **failed approaches (mandatory)**, decisions, resume instructions. Reference repos: `willseltzer/claude-handoff`, `Lutren/agent-handoff-protocol`, `cellear/agent-handoff`.
- Session resume: opencode `--session <id>` / `--continue` / `--fork` / `opencode export <id>`; Claude Code `--continue` / `--resume`.

## Key guidance & caveats

- **"Building effective agents"** (Anthropic): orchestrator-workers only when subtasks can't be predefined and the work parallelizes; otherwise use plain parallelization or one agent.
- **Multi-agent costs ~3–15× tokens** — worth it only for high-value parallelizable work. Cheap-model workers under an expensive orchestrator (or model routing via claude-code-router) is the standard cost mitigation.
- **Context rot** (Anthropic "Effective context engineering"): curation/isolation/compaction are design tools — fresh executor contexts per phase are the isolation half of that.
- **Docs gaps found:** opencode subagent token limits (unknown), mid-tier `permissionMode` inheritance in Claude Code (unknown), Cursor/Codex/Crush nesting semantics partially undocumented.

## Top resources

1. Building effective agents — anthropic.com/engineering/building-effective-agents
2. Multi-agent research system — anthropic.com/engineering/multi-agent-research-system
3. Effective context engineering — anthropic.com/engineering/effective-context-engineering-for-ai-agents
4. opencode agents docs — opencode.ai/docs/agents · config — opencode.ai/docs/config
5. Claude Code subagents — code.claude.com/docs/en/sub-agents · worktrees — code.claude.com/docs/en/worktrees
6. Orchestrator-workers cookbook — github.com/anthropics/anthropic-cookbook (patterns/agents/orchestrator_workers.ipynb)
7. 6 orchestration patterns w/ configs — thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/
8. GSD — github.com/gsd-build/get-shit-done
9. oh-my-opencode-slim — github.com/alvinunreal/oh-my-opencode-slim
10. claude-code-router — github.com/musistudio/claude-code-router
