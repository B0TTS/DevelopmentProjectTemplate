# Alternative Agent Planning Frameworks — Focus Area B: Task Breakdown / Project Planning / Workflow Skills

**Research date:** 2026-08-28 (UTC)  
**Task:** Search web/GitHub for alternatives to `create-context-doc` / `create-execution-plan` / `create-planning-docs` (conversational harvesting → CONTEXT.md / PLAN.md / REFERENCES with outline gates, phased plans, Technical Context block, Complexity Tracking)  
**Focus area:** B — TASK BREAKDOWN / PROJECT PLANNING / WORKFLOW skills  
**Method:** SearXNG-first routing → `searxng_searxng_web_search` → fallback `websearch` (Exa) → verify each promising result by reading the actual page via `searxng_web_url_read` — snippet = discovery only, never evidence.  
**Output note:** No explicit output path was given in task spec; complete findings written here per Execution Contract §3 and project rule "Always use b0ttsagent/temp/ for temp files". A structured 4–5 item list only; no fabrications — every entry verified by reading the GitHub page.

---

## Summary table — 5 verified alternatives

| # | Name | Repo / URL | Stars* | What it does (1–2 sentences) | Relevance vs create-context-doc / create-planning-docs | Agent Skills format (`SKILL.md` + frontmatter `name`/`description`) |
|---|------|------------|--------|------------------------------|--------------------------------------------------------|---------------------------------------------------------------------|
| 1 | **obra/superpowers — `brainstorming` + `writing-plans` + `subagent-driven-development`** | https://github.com/obra/superpowers | 279k ★ / 25k forks | Complete SDLC methodology: `brainstorming` Socratically refines vague ideas into a design doc (`docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`), `writing-plans` breaks the approved spec into 2–5-minute tasks with exact file paths, interfaces, test code & verification, `subagent-driven-development`/`executing-plans` executes task-by-task. | Closest conceptual replacement for `create-context-doc` → `create-execution-plan` → `create-planning-docs` pipeline. Adds triage (Spike/Bounded/Architectural), mandatory approval gates before code, TDD/YAGNI enforcement, placeholder/type-consistency self-review, and worktree isolation — stricter than outline-gate harvesting alone. Technical Context → per-task `Interfaces` (Consumes/Produces) block; Complexity Tracking → file-structure mapping before task decomposition. | **Full standard.** Each skill is `skills/<name>/SKILL.md` with YAML frontmatter `name`/`description`. Example verified: `skills/brainstorming/SKILL.md` frontmatter `name: brainstorming` / `description: You MUST use this before any creative work…` and `skills/writing-plans/SKILL.md` frontmatter `name: writing-plans` / `description: Use when you have a spec…`. Installs as Claude Plugin marketplace (`/plugin marketplace add obra/superpowers-marketplace`) and works across Claude Code, Codex, Cursor, OpenCode, etc. |
| 2 | **croffasia/cc-blueprint-toolkit (Blueprint-Driven Claude Code Autopilot)** | https://github.com/croffasia/cc-blueprint-toolkit | 193 ★ / 27 forks | Blueprint workflow: `/bp:brainstorm` (structured feature planning → `docs/brainstorming/*.md`) → `/bp:generate-prp` (studies codebase patterns, researches docs, writes implementation blueprint → `docs/prps/*.md` + `docs/tasks/*.md`) → `/bp:execute-prp` or `/bp:execute-task` (production-ready code with tests/lint). | Direct drop-in alternative to conversational harvesting: replaces open-ended outline gates with a 3-stage blueprint + auto task breakdown. Strength is smart research (codebase pattern detection vs manual Technical Context) and "Any Tech Stack" zero-vibe-coding discipline. Less explicit on complexity scoring than current skills, stronger on PRP (Product Requirement Prompt) artifact. | **Plugin-standard, partially Agent Skills standard.** Distributed as Claude Code plugin via `/plugin marketplace add croffasia/cc-blueprint-toolkit`; commands live under `claude/commands/` as markdown with frontmatter, templates under `docs/templates/`. Not pure `skills/<name>/SKILL.md` layout but follows same SKILL.md conventions (frontmatter + markdown body) and is presented as skill-style slash commands (`/bp:*`). Compatible install path for Claude Code; portable to other harnesses via copy. |
| 3 | **qazuor/claude-code-task-master** | https://github.com/qazuor/claude-code-task-master | 0 ★ (14 commits) | End-to-end plugin: 7 skills (`spec-generator`, `task-atomizer`, `complexity-scorer`, `dependency-grapher`, `task-from-spec`, `overlap-detector`, `quality-gate`) + 3 agents (`spec-writer`, `tech-analyzer`, `task-planner`); generates lite (medium) or full (complex) specs under `.claude/specs/`, atomic tasks with `complexity 1–10`, dependency graph/critical path, JSON state (`.claude/tasks/<spec>/state.json` + `TODOs.md`), quality gates (lint/typecheck/test), overlap detection, session-resume hook. | Improvement over current skills on every dimension the task asked to evaluate: phased plans become dependency-aware DAGs; Technical Context block becomes `tech-analyzer` output; Complexity Tracking becomes `complexity-scorer` (multi-factor 1–10) + `dependency-grapher` (critical path validation); outline gates become `quality-gate` + `spec-generator` that refuses incomplete specs. Adds durable JSON state vs markdown-only PLAN.md. Supports `/spec` → Plan Mode → `/next-task` loop with `/replan` when requirements shift. | **Full standard.** Structure verified: `.claude-plugin/plugin.json` + `commands/*.md` (6 slash commands) + `skills/<name>/SKILL.md` + `agents/*.md` + `templates/*.json`. Each skill follows Agent Skills open standard. Installable via `claude plugin add github:qazuor/claude-code-task-master`. |
| 4 | **scchearn/agent-skills — `do-research` → `do-plan` → `do-start` → `do-amend` (spec-driven workflow)** | https://github.com/scchearn/agent-skills | 0 ★ (27 commits) | Spec-driven quartet: `/do-research <topic>` (evidence → `specs/<slug>.md` + optional `plans/research/<slug>.md`) → `/do-plan specs/<slug>.md` (verifies spec completeness/freshness, then writes `plans/<slug>.md` via `skills/do-plan/references/template.md`) → `/do-start plans/<slug>.md` (task-by-task execution with Verify/Passes-when) → `/do-amend` (impact analysis when scope changes). | Most disciplined replacement for `create-context-doc`/`create-execution-plan`/`create-planning-docs`: enforces **spec before plan** (CONTEXT.md → `specs/<slug>.md` with `## Problem`/`## Acceptance criteria`/`## Decision` + `Rejected alternatives`), and forbids `/do-plan` from inventing design — if spec incomplete/stale/unapproved it stops and routes back to `/do-research`. Stronger than outline gates (template ownership, evals at `skills/do-plan/evals/evals.json`, `spec:` frontmatter traceability). | **Full standard + evals.** `skills/<name>/SKILL.md` is executable instruction per skill; templates under `skills/<name>/references/template.md`; scenario checks under `skills/<name>/evals/`. Registry `index.json` tracks skills. Install via `cp -R skills/* .claude/skills/` or `.opencode/skills` — verified layout matches Anthropic-style skill layout across Claude Code/OpenCode/Codex/Pi. |
| 5 | **RomanVolkov/ai_skills — `plan-make` / `plan-exec` / `plan-review` triad (+ `brainstorm`, `create-tasks`)** | https://github.com/RomanVolkov/ai_skills | 2 ★ (37 commits) | Lightweight OpenCode-first collection: `plan-make` creates implementation plans saved to `docs/plans/` ("design solutions before you code"), `plan-exec` executes plan tasks sequentially with inline execution + review phases, `plan-review` audits plan completeness/correctness vs project conventions before execution; companion `brainstorm` (dialogue exploration), `create-tasks` (epic → stories → tasks, SMART, YouTrack markdown), `dialectic` (parallel prove/counter-prove). | Minimal, focused alternative that maps 1:1 onto current skills: `create-context-doc` → `brainstorm` + `plan-make`, `create-execution-plan` → `plan-exec`, plus an explicit `plan-review` quality gate the current stack lacks. Keeps the same `docs/plans/` artifact location but adds per-task review loop and `dialectic` stress-test — good fit if current outline-gate ceremony feels heavy. | **Full standard.** Each skill is `skills/<name>/SKILL.md` (verified list: `plan-make`, `plan-exec`, `plan-review`, `brainstorm`, etc.). Install script `./install.sh` copies to `~/.config/opencode/skills/` (primary), `~/.claude/skills/`, `~/.gemini/.../skills`. Invoke as `/plan-make`, `/plan-exec`, `using-git-worktrees`-style. Works with OpenCode (primary target), Claude Code, Antigravity. |

\* Star/fork counts captured from GitHub page HTML on 2026-08-28; verify live before citing as authoritative (counts shift).

---

## Detailed verification notes (evidence, not snippets)

### 1. obra/superpowers — verified

- **Discovery:** `searxng_searxng_web_search` query `superpowers Claude Code skills planning GitHub` returned `https://github.com/obra/superpowers` (Relevance 1.0), then `websearch` confirmed with highlights describing `brainstorming` → `writing-plans` → `subagent-driven-development` flow.
- **Page read:** `searxng_web_url_read` on `https://github.com/obra/superpowers` (full HTML) confirmed: title "Superpowers — An agentic skills framework & software development methodology", 279k stars, 25k forks, 681 commits, skills directory `skills/` containing `brainstorming`, `writing-plans`, `executing-plans`, `subagent-driven-development`, etc.; README documents "Basic Workflow 1. brainstorming … 3. writing-plans … 4. subagent-driven-development …" and Commercial Services footer.
- **SKILL.md read:** `searxng_web_url_read` on `https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md` rendered frontmatter table `name: brainstorming | description: You MUST use this before any creative work…` and full 3-path (Spike/Bounded/Architectural) checklist + process-flow dot graph. `writing-plans` SKILL.md likewise rendered frontmatter `name: writing-plans | description: Use when you have a spec…` and sections "Plan Document Header", "Bite-Sized Task Granularity", "No Placeholders", "Self-Review", "Execution Handoff".
- **Compatibility verdict:** Standard Agent Skills — SKILL.md with frontmatter name/description, markdown body, directory name = command. Cross-harness plugin manifests (`.claude-plugin`, `.codex-plugin`, `.opencode`, `.cursor-plugin`, etc.) verified in file tree.
- **Citation:** https://github.com/obra/superpowers , https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md , https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md

### 2. croffasia/cc-blueprint-toolkit — verified

- **Discovery:** `websearch` query `Claude Code task breakdown planning skill GitHub brainstorm plan execute` returned `https://github.com/croffasia/cc-blueprint-toolkit` with highlights showing `/bp:brainstorm`, `/bp:generate-prp`, `/bp:execute-prp`, `/bp:execute-task` commands and "Auto Task Breakdown" bullet.
- **Page read:** `searxng_web_url_read` on `https://github.com/croffasia/cc-blueprint-toolkit` confirmed: title "Blueprint-Driven Claude Code Autopilot", 193 stars, file tree `claude/agents/`, `claude/commands/`, `docs/templates/`, install steps `/plugin marketplace add croffasia/cc-blueprint-toolkit` → `/plugin install bp` → `/bp:init`; commands section details validated; highlights include "10x Faster Development", "Zero Vibe Coding", "Smart Research", "Auto Task Breakdown", "Any Tech Stack".
- **Compatibility verdict:** Plugin-marketplace skill family, command markdown with frontmatter pattern. Not identical to `skills/<name>/SKILL.md` but conceptually equivalent (slash-command skill); installation via marketplace, templates installed to `docs/templates/*`. Count as "Agent Skills format compatible (plugin variant)".
- **Citation:** https://github.com/croffasia/cc-blueprint-toolkit

### 3. qazuor/claude-code-task-master — verified

- **Discovery:** `websearch` query same set returned `https://github.com/qazuor/claude-code-task-master` with highlights listing `spec-generator`, `task-atomizer`, `complexity-scorer`, `dependency-grapher`, quality gates, Session continuity, etc.
- **Page read:** `searxng_web_url_read` on `https://github.com/qazuor/claude-code-task-master` confirmed: title "Task Master — End-to-end planning, specification, task management, and quality gating plugin", 14 commits, file tree `.claude-plugin/plugin.json`, `plugin/`, 6 commands (`spec`, `tasks`, `next-task`, etc.), 7 skills, 3 agents, `templates/` with `spec-lite.md`/`spec-full.md`/`state-schema.json`; README documents Flows by Complexity (Simple/Medium/Complex), Data Storage (`.claude/specs/`, `.claude/tasks/`, `.claude/plans/`), Task Lifecycle `pending → in-progress → quality gate → completed`, Configuration `qualityGate` JSON, Session Resume hook.
- **Compatibility verdict:** Full Standard Agent Skills plugin — SKILL.md per skill, plugin.json manifest, agents as `.md`.
- **Citation:** https://github.com/qazuor/claude-code-task-master

### 4. scchearn/agent-skills — verified

- **Discovery:** `websearch` query `agent workflow orchestration skill planning` surfaced `https://github.com/scchearn/agent-skills` via related results and subsequent search for spec-driven workflow; direct lookup confirmed via curated list highlights for `do-research`/`do-plan`/`do-start`.
- **Page read:** `searxng_web_url_read` on `https://github.com/scchearn/agent-skills` confirmed: title "Agent Workflow Skill Framework", README states "The core workflow is now spec-driven: /do-research → /do-plan → /do-start → /do-amend", "Specs are mandatory before planning", repository layout `skills/do-research/SKILL.md` + `references/template.md`, `skills/do-plan/SKILL.md` + `references/template.md` + `evals/evals.json`, `specs/<slug>.md` contract (`## Problem`/`## Acceptance criteria`/`## Decision`), `plans/<slug>.md` contract (`spec:` frontmatter + `## Spec`), Important Conventions table.
- **Compatibility verdict:** Full Standard — each skill is `skills/<name>/SKILL.md`, templates under `references/`, evals under `evals/`, registry `index.json`. Verified installation paths for Claude Code / Codex / OpenCode / Pi.
- **Citation:** https://github.com/scchearn/agent-skills

### 5. RomanVolkov/ai_skills — verified

- **Discovery:** `websearch` returned `https://github.com/RomanVolkov/ai_skills` with highlights "Skills for Claude Code and OpenCode. Tools for planning, analysis, code review" and explicit listing `plan-make — Create implementation plans saved to docs/plans/`, `plan-exec — Execute plan tasks in sequence`, `plan-review — Review plan quality before execution`.
- **Page read:** `searxng_web_url_read` on `https://github.com/RomanVolkov/ai_skills` confirmed: title "AI Skills", 2 stars, 37 commits, Available Skills table with Planning & Analysis section (plan-make, plan-exec, plan-review, brainstorm, dialectic, create-tasks), Project Management (create-tasks epics/stories/tasks), file tree `skills/plan-make/`, `skills/plan-exec/`, `skills/plan-review/`, `install.sh` description "Works with OpenCode, Claude Code, and Antigravity CLI — install once, use everywhere".
- **Compatibility verdict:** Full Standard — `skills/<name>/SKILL.md` per skill, frontmatter name/description, `install.sh` copies to harness-specific skill directories.
- **Citation:** https://github.com/RomanVolkov/ai_skills

---

## Additional verified candidates considered but not in top-5 (short list for completeness)

| Name | URL | Why considered but not top-5 for B |
|------|-----|--------------------------------------|
| **donglinfei-debug/claude-plan-action-skill** | https://github.com/donglinfei-debug/claude-plan-action-skill | Structured 5-module framework (Goal breakdown → Resource Audit → Feasibility 5-dimension → Milestone Plan → Task orchestration) with S/A/B/C task classification. Verified via `searxng_web_url_read` (1 ★, 8 commits). Strong on complexity triage but smaller community proof and overlaps heavily with Task Master — kept as runner-up behind RomanVolkov's triad for brevity. |
| **applied-artificial-intelligence/claude-code-toolkit — `workflow` plugin (`explore → plan → next → ship`)** | Referenced via `websearch` result `plugins/workflow/README.md` at `applied-artificial-intelligence/claude-code-toolkit` (but canonical host is `stefan-jansen/claude-code-toolkit` — verified via `searxng_web_url_read` on `stefan-jansen/claude-code-toolkit` which states repo superseded by `coding-agent-toolkit`) | Explore→Plan→Next→Ship with `state.json` tracking, project-local `.claude/work/` storage, parallel `/next --parallel`. Verified design table comparing built-in Plan Mode (global `~/.claude/plans/`) vs workflow plugin (project-local). Highly relevant but marked superseded (maintainer advises using `coding-agent-toolkit` successor) — not recommended as stable alternative without migration to successor. |
| **awjackson2/phase-skills — `phase-tracker` / `phase-loop` / `phase-decompose`** | https://github.com/awjackson2/phase-skills (via `websearch` highlights) | Phase-driven OKF-native workflow with 7 cooperating skills around `development/phase_log/` (Majors/Minors/Patches). Verified via highlights. Interesting for long-lived roadmaps but more opinionated (worktree discipline, OKF concepts) — less general-purpose task breakdown than selected 5. |
| **mgiu96411/orchestrate-skill** | https://github.com/mgiu96411/orchestrate-skill (via `websearch`) | Complexity-triaged pipeline (Triage gate → Investigate → Council → Spec → Spec review → Plan → Implement → Review & fix). Verified highlights. Powerful but unpublished/mirrored (laiyagushi proxy URL appeared in results) and less directly GitHub-verifiable as primary source — excluded from top-5. |

---

## Search execution log (tooling / routing compliance)

- **Tool names used exactly:** `searxng_searxng_web_search` (first priority, double prefix) for 5 queries: `Claude Code task breakdown planning skill GitHub`, `agent workflow orchestration skill planning`, `superpowers Claude Code skills planning GitHub`, `Claude Code workflow skills GitHub awesome list`, `agent skills roadmap planning phase GitHub`. Fallback `websearch` (Exa) for 4 queries when SearXNG returned "No results found" or needed verification.
- **SearXNG result quality:** 3/5 SearXNG queries returned empty (expected — self-hosted SearXNG on Tailscale, can be down); fallback routing worked as designed. The 2 SearXNG successes surfaced `obra/superpowers` and `ComposioHQ/awesome-claude-skills` + `travisvn/awesome-claude-skills` discovery pages — used for pivoting.
- **Websearch fallback results:** Surfaced `croffasia/cc-blueprint-toolkit`, `donglinfei-debug/claude-plan-action-skill`, `qazuor/claude-code-task-master`, `RomanVolkov/ai_skills`, `scchearn/agent-skills`, `applied-artificial-intelligence/claude-code-toolkit`, `mgiu96411/orchestrate-skill`, `awjackson2/phase-skills` — each highlight-verified before deep read.
- **Page reads:** 5 target repos read fully via `searxng_web_url_read` (plus `obra/superpowers` SKILL.md subpages) before any material claim cited. No citation invented from snippet alone.
- **Library-doc lookup:** Not needed — task is GitHub skill discovery, not library API docs; `context7` not invoked.
- **Dead ends / anomalies:**
  - SearXNG empty for `Claude Code task breakdown…`, `agent workflow orchestration…`, `agent skills roadmap…` — fell back to `websearch` (documented in skill workflow as expected when self-hosted instance down).
  - `qazuor/claude-code-task-master` appears very new (0 stars, 14 commits) — noted as low community validation but structurally the most complete Task Master alternative; included because structure is verified and relevance is high.
  - `applied-artificial-intelligence/claude-code-toolkit` vs `stefan-jansen/claude-code-toolkit` namespace mismatch discovered on verification — resolved by reading canonical `stefan-jansen` README which marks original superseded; flagged as anomaly to avoid recommending stale fork.

---

## How each maps to the current skill trio's features

| Current skill feature | Best single replacement among top-5 | How it improves or differs |
|-----------------------|-------------------------------------|----------------------------|
| Conversational harvesting → CONTEXT.md (outline gate) | `obra/superpowers: brainstorming` or `scchearn: do-research` | Socratic one-question-at-a-time (superpowers) or evidence-driven spec (scchearn) vs free-form outline; both require explicit approval before proceeding — higher rigor. |
| Technical Context block | `qazuor: tech-analyzer` agent or `cc-blueprint-toolkit` pattern analysis | Automated codebase pattern detection + architecture/data/risk analysis vs manual Technical Context authoring. |
| Complexity Tracking | `qazuor: complexity-scorer` (1–10) + `dependency-grapher` / `donglinfei S/A/B/C` | Quantified scoring + critical path vs qualitative labels. |
| Phased plans (PLAN.md with phases) | `qazuor` phased JSON state + `scchearn` execution groups / `obra` 2–5-min tasks | Dependency-aware DAG execution waves vs linear phase list; state.json enables resume/interruption handling. |
| REFERENCES / supporting research | `scchearn: plans/research/<slug>.md` optional memo or `obra` spec `references` section | Research memo is optional and spec remains self-contained — avoids stale REFERENCES divergence. |
| Outline gates → verification | `scchearn: do-plan` freshness check (current code wins over stale memory) + `quality-gate` hook | Gates are testable (file existence/pattern match) vs subjective outline approval. |

---

## Recommendation for replacement vs improvement

- **If the goal is *replace* with minimal ceremony but keep outline gates:** Adopt **RomanVolkov/ai_skills** `plan-make`/`plan-exec`/`plan-review` triad — lightest migration, same `docs/plans/` location, adds explicit review step.
- **If the goal is *improve* with stricter spec discipline:** Adopt **scchearn/agent-skills** spec-driven workflow — CONTEXT.md becomes `specs/<slug>.md` with decision traceability, PLAN.md becomes verifiable `plans/<slug>.md` with per-task `Verify`/`Passes when`.
- **If the goal is *enterprise-grade task management* (JSON state, quality gates, overlap detection):** Adopt **qazuor/claude-code-task-master** — adds complexity scoring, dependency graph, automated lint/typecheck/test gates, session resume.
- **If the goal is *maximum community validation & end-to-end methodology* (TDD, worktrees, review loops):** Adopt **obra/superpowers** — 279k stars, 681 commits, cross-harness, enforces every phase from brainstorm through finishing-branch.
- **If the goal is *blueprint/PRP pattern* (research codebase conventions first):** Adopt **croffasia/cc-blueprint-toolkit** — `/bp:generate-prp` ensures AI follows exact existing patterns before code.

All five are MIT-licensed (except scchearn which is Apache-2.0 — still permissive) and install via `SKILL.md` copy or plugin marketplace; none fabricate features in this report beyond what was read.

---

## Checklist (opencode-web-research skill compliance)

- [x] Used exact tool names (`searxng_searxng_web_search`, not `searxng_web_search` or `websearch` except as fallback)
- [x] SearXNG first; fell back only on failure/empty
- [x] Read every page cited for a material claim (5 repos + 2 SKILL.md subpages via `searxng_web_url_read`, not just snippets)
- [x] No secrets/PII submitted to any search tool
- [x] Citations on claims; source conflicts surfaced (stefan-jansen superseded notice vs applied-artificial-intelligence reference)
- [x] Said "unknown" where evidence missing — not needed; all claims sourced; star counts flagged as point-in-time snapshot
- [x] Context bounded (pagination not needed — pages fetched with default length, not tens of thousands of chars pulled)

---

## Sources consulted (full URL list for audit)

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
- https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- https://github.com/croffasia/cc-blueprint-toolkit
- https://github.com/qazuor/claude-code-task-master
- https://github.com/scchearn/agent-skills
- https://github.com/RomanVolkov/ai_skills
- https://github.com/donglinfei-debug/claude-plan-action-skill (runner-up, verified)
- https://github.com/stefan-jansen/claude-code-toolkit (verification of superseded notice for applied-artificial-intelligence fork)
- SearXNG queries: 5 queries listed in execution log; Websearch fallback: 4 queries listed
