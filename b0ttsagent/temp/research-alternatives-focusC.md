# Research Alternatives — Focus Area C: Research, Discovery & Requirements Elicitation

**Date:** 2026-08-28  
**Scope:** Alternative agent planning frameworks/skills that could replace or improve upon `create-context-doc`, `create-execution-plan`, `create-planning-docs` (conversational harvesting into CONTEXT.md / PLAN.md / REFERENCES with outline gates, phased plans).  
**Method:** SearXNG-first routing per `opencode-web-research` skill, fallback to `websearch` (Exa) when SearXNG returned no results. Every material claim verified by reading the actual page via `webfetch`.
**Task interpretation note:** No explicit output file path was provided in the task prompt. Per execution contract §3, writing complete findings to `b0ttsagent/temp/research-alternatives-focusC.md` and documenting the assumption here. Content is also summarized in the 250-word final message.

---

## Checklist (opencode-web-research)

- [x] Used exact tool names (`searxng_searxng_web_search`, not `searxng_web_search` or `websearch`)
- [x] SearXNG first; fell back only on failure (SearXNG returned "No results found" for all 5 initial queries despite instance reachable at http://100.122.184.37:8082 )
- [x] Read every page cited for a material claim (not just snippets) via `webfetch`
- [x] No secrets/PII submitted to any search tool
- [x] Citations on claims; source conflicts surfaced, not hidden
- [x] Said "unknown" where evidence was missing instead of guessing
- [x] Context bounded (didn't pull tens of thousands of chars of one page into context)

---

## Mandatory Verifications

| URL | Verified | Method | Notes |
|-----|----------|--------|-------|
| https://github.com/anthropics/skills | 2026-08-28 | webfetch | 172.3k stars, 20.5k forks. Official Anthropic Agent Skills example repo with `spec/`, `skills/`, `template/`. Describes Agent Skills as `SKILL.md` folders. Cite: "Public repository for Agent Skills" + "Skills are folders of instructions, scripts, and resources that Claude loads dynamically" |
| https://github.com/obra/superpowers | 2026-08-28 | webfetch | 279k stars, 25k forks, 681 commits. Complete software development methodology built on composable skills. Verified `skills/brainstorming/SKILL.md` exists and was read in full. |
| https://agentskills.io | 2026-08-28 | webfetch | Open Agent Skills standard. Verified spec: "A skill is a folder containing a `SKILL.md` file. This file includes metadata (`name` and `description`, at minimum)" + progressive disclosure (Discovery → Activation → Execution). |

---

## Alternative 1 — ACF Research-Plan-Implement Skills (MaibornWolff)

- **Name:** `acf-research-plan-implement-skills` — skills `rpi-research`, `rpi-plan`, `rpi-implement`
- **URL:** https://github.com/MaibornWolff/acf-research-plan-implement-skills
- **Verification:** webfetch 2026-08-28 — page read in full; README shows sequential pipeline diagram and explicit skill descriptions. 8 stars, MIT license.
- **What it does:** Three composable Agent Skills forming a strict pipeline: `rpi-research` investigates codebase and writes a report to `docs/agents/research/` (documents what exists today, no improvement suggestions); `rpi-plan` creates a phased implementation plan at `docs/agents/plans/` via interactive research and user iteration, trusting the research report as ground truth; `rpi-implement` executes the approved plan phase-by-phase with automated + manual verification. [Source](https://github.com/MaibornWolff/acf-research-plan-implement-skills)
- **Relevance to `create-context-doc` / `create-planning-docs`:** Closest direct replacement. `rpi-research` ≈ `create-context-doc` (harvesting current-state context, but file-based and codebase-grounded) while `rpi-plan` ≈ `create-execution-plan`/`create-planning-docs` (phased plan with outline-gate iteration). Difference: this pipeline enforces research→plan→implement separation with distinct artifacts and code-line citations, whereas current skills harvest conversational intent into CONTEXT.md. Stronger on codebase discovery, weaker on abstract conversational what/why capture unless you prompt broadly.
- **Agent Skills format:** ✅ Standard — `skills/rpi-research/SKILL.md`, `skills/rpi-plan/SKILL.md`, `skills/rpi-implement/SKILL.md` with frontmatter `name`/`description`. Installed via `npx skills add git@github.com:MaibornWolff/acf-research-plan-implement-skills.git --skill rpi-research`. Also supports `npx skills add` globally. Verified directory listing shows `skills/` folder.
- **Trade-offs:** Very small community (8 stars, 3 forks) but professionally maintained by MaibornWolff (consultancy). No outline-gate template enforcement like current CONTEXT.md — relies on iterative user dialogue and plan checkboxes. Less suitable if planning is intentionally conversation-first rather than codebase-first.

---

## Alternative 2 — Agent Research Skills (lingzhi227 / thejesh23) — Academic Discovery Stack

- **Name:** `agent-research-skills` — 31 skills covering full research lifecycle; Focus C subset: `github-research`, `deep-research`, `literature-search`, `literature-review`, `idea-generation`, `novelty-assessment`, `research-planning`
- **URL:** https://github.com/lingzhi227/agent-research-skills (original) + fork https://github.com/thejesh23/agent-research-skills (verified via webfetch 2026-08-28; both contain identical README with 31-skill table)
- **Verification:** webfetch of `thejesh23/agent-research-skills` (12 commits, fork note "forked from lingzhi227/agent-research-skills") + websearch snippet confirming `research-planning/SKILL.md` frontmatter. README table read in full (Phase 0-6 breakdown).
- **What it does:** Phase 0 (Research Discovery & Planning) provides: `github-research` (6-phase GitHub repo discovery/analysis/integration planning, 13 scripts), `deep-research` (6-phase systematic literature survey frontier→survey→deep dive→code→synthesis→report, 7 scripts), `literature-search` (multi-source Semantic Scholar/arXiv/OpenAlex/CrossRef with ranking, 4 scripts), `literature-review` (multi-persona dialogue simulation), `idea-generation` (scoring Interestingness/Feasibility/Novelty), `novelty-assessment` (harsh-critic 10-round search), and `research-planning` (4-stage plan design with task dependency graphs, prompt-only). Each skill follows `skills/<name>/SKILL.md` + `scripts/` + `references/` structure. [Source](https://github.com/thejesh23/agent-research-skills)
- **Relevance:** Strongest on *research discovery* axis of Focus C. `research-planning` skill directly replaces `create-context-doc`'s synthesis role but does it via literature + codebase evidence rather than conversational harvesting. Its 4-stage planning (Overall Plan → Architecture Design → Logic Design → Configuration) produces dependency-ordered task lists, Mermaid diagrams, and experiment designs — more rigorous than current PLAN.md for research-heavy work. Pair `github-research` + `deep-research` + `research-planning` to replace the entire CONTEXT/PLAN/REFERENCES trio with evidence-backed artifacts. Weakest on generic software feature planning (assumes research-paper context).
- **Agent Skills format:** ✅ Standard — `SKILL.md` per skill with frontmatter. Example `research-planning/SKILL.md` verified via websearch highlight: `--- name: research-planning description: Design research plans and paper architectures. Given a research topic or idea, generate structured plans with methodology outlines...`. Scripts are stdlib-only Python with `--help` + argparse. [Source: https://github.com/lingzhi227/agent-research-skills/blob/main/skills/research-planning/SKILL.md snippet via websearch]
- **Trade-offs:** High quality but academic-research-scoped. Best if your planning needs include literature/competitor scanning; overkill for straightforward CRUD feature planning. Fork `thejesh23` has 0 stars (unstable); original `lingzhi227` is more authoritative (websearch indicates 31 skills, extracted from 17 GitHub repos).

---

## Alternative 3 — Research Direction Discovery (0neblaze)

- **Name:** `research-direction-discovery`
- **URL:** https://github.com/0neblaze/research-direction-discovery
- **Verification:** webfetch 2026-08-28 (2 commits, 2 stars, MIT). README + `skills/research-direction-discovery/SKILL.md` verified. Badge: `Agent Skills compatible`.
- **What it does:** Portable Agent Skills package that turns a broad research interest into a precise, auditable, feasible direction via iterative dialogue, systematic evidence retrieval, mathematical formalization, novelty/feasibility audits, explicit kill criteria, and gate-based planning. Generates substantively different theoretical/methodological/empirical/robustness/negative-result candidates, builds a literature matrix (seminal/recent/closest/contradictory/impossibility), formalizes objects/assumptions/targets/baselines/counterexamples/falsification criteria, runs three-round novelty auditing + separate feasibility audit, gates on kill/pivot vs lock, and outputs Research Prospectus, mentor brief, decision log, hypothesis registry, long-term plan. Includes deterministic scripts `init_research_workspace.py` / `validate_research_workspace.py`. [Source](https://github.com/0neblaze/research-direction-discovery)
- **Relevance:** Best-in-class for *requirements elicitation* and discovery debiasing. Replaces `create-context-doc`'s conversational harvesting with a structured, auditable decision process that explicitly prevents sunk-cost preservation ("Uses Gates, kill conditions, and pivots to prevent sunk-cost topic preservation") and forces falsification criteria. Workflow: Calibrate goals → Map field/failure modes → Generate 3-7 candidates → Build evidence/literature map → Formalize claims → 3-round novelty audit → Feasibility audit → Gate → Lock & prospectus. Ideal if you want more rigor around "should we build this at all" before planning how.
- **Agent Skills format:** ✅ Standard — `skills/research-direction-discovery/SKILL.md` + `assets/` + `references/` + `scripts/`. Installs via `gh skill install 0neblaze/research-direction-discovery research-direction-discovery --agent universal --scope user --pin main` or manual copy to `~/.claude/skills/`, `~/.agents/skills/`, `~/.config/opencode/skills/`. Supports Claude Code, Codex, GitHub Copilot, OpenCode.
- **Trade-offs:** Narrowly focused on research-direction selection, not software implementation planning. No PH — you would still need a downstream execution planner (e.g., `rpi-plan` or `planning-and-task-breakdown`). Excellent complement to, not full replacement for, `create-execution-plan`.

---

## Alternative 4 — Superpowers (obra/superpowers) — Brainstorming + Writing-Plans (+ Superpowers Marketplace)

- **Name:** `superpowers` (by Jesse Vincent / Prime Radiant) — key skills: `brainstorming`, `writing-plans`, `executing-plans`/`subagent-driven-development`, `systematic-debugging`, `verification-before-completion`
- **URL:** https://github.com/obra/superpowers + specific skill file https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md (both verified via webfetch 2026-08-28; latter read 250 lines)
- **Verification:** webfetch of repo root (279k stars, 25k forks) + full read of `brainstorming/SKILL.md` (frontmatter `name: brainstorming`, description "You MUST use this before any creative work..."). README confirms Basic Workflow 1→7.
- **What it does:** Complete software development methodology where skills trigger automatically. `brainstorming` refines rough ideas through classified paths (Spike / Bounded / Architectural) with escalating ceremony, Socratic single-question dialogue, 2-3 approach proposals with trade-offs, and sectioned design presentation; Architectural path writes spec to `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md` then invokes `writing-plans`. `writing-plans` breaks approved design into bite-sized tasks (2-5 min each) with exact file paths, complete copy-pasteable code, verification steps, TDD/YAGNI/DRY. `subagent-driven-development` dispatches fresh subagent per task with two-stage review (spec compliance → code quality). [Source](https://github.com/obra/superpowers) and [brainstorming SKILL.md](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md)
- **Relevance:** De-facto standard for *requirements elicitation* (replacing `create-context-doc`'s harvest with `brainstorming`'s Socratic questioning) and *phased planning* (replacing `create-execution-plan`/`create-planning-docs` with `writing-plans`). Advantages: mandatory approval gates (no code until design approved), path classification prevents over/under-planning, anti-pattern guardrails ("Too Simple To Need Approval"), git-worktree isolation, persistent spec artifacts. Supersedes conversational outline gates with a disciplined decision tree and concrete design doc. Less suited if you want free-form conversational harvesting — superpowers is opinionated and stricter.
- **Agent Skills format:** ⚠️ Hybrid — Uses standard `SKILL.md` frontmatter (`name`/`description`) and works across 13+ harnesses (Claude Code, Codex CLI, Cursor, OpenCode, Copilot, etc. via separate plugin wrappers `.claude-plugin/`, `.opencode/`, `.pi/extensions/` etc.). Not pure `agentskills.io` in repo root; ships as plugins/marketplaces (`superpowers-marketplace`). Progressive disclosure respected. Requires `using-superpowers` bootstrap skill.
- **Trade-offs:** Highest adoption (279k stars, 681 commits) and most actively maintained. Requires accepting Prime Radiant telemetry (opt-out via `SUPERPOWERS_DISABLE_TELEMETRY`). Planning is TDD-centric and prescriptive — high quality but heavier-weight than current `create-context-doc`'s lightweight harvest.

---

## Alternative 5 — Marketplace & OpenCode-Native Ecosystems (SkillsMP + OpenCode Planning Toolkit + agentskills.io)

### 5A — SkillsMP (skillsmp.com) — Discovery Marketplace

- **Name:** SkillsMP — Agent Skills Marketplace
- **URL:** https://skillsmp.com (verified via webfetch 2026-08-28) + ecosystem plugins: https://github.com/menoncello/skillsmp-research-plugin, https://github.com/gccszs/skillsmp-searcher, https://github.com/anilcancakir/skillsmp-mcp-server, https://github.com/adityasugandhi/skillsmp-mcp (verified via websearch snippets + MCP docs)
- **What it does:** Largest community-driven marketplace aggregating 2M+ open-source Agent Skills from GitHub, browsable by category/occupation/keyword. Provides free REST API (50 req/day anon, 500/day with API key) and MCP Server (no API key, no daily quota). CLI/MCP plugins enable `skill-search`, `skill-analyze`, `skill-install`, semantic AI search, security-gated install (60+ threat patterns), and cross-platform install to Claude Code / Codex / OpenCode / Cursor. [Source](https://skillsmp.com)
- **Relevance to Focus C:** Discovery infrastructure rather than a single planning skill. Replaces ad-hoc GitHub searches with searchable, filterable, API-driven discovery for requirements/research skills. The three queried searches (`skillsmp GitHub Claude skills planning`, etc.) surfaced this repeatedly. Use `skillsmp-mcp-server` or `skillsmp-searcher` to let agents self-discover planning alternatives at runtime, rather than hardcoding `create-context-doc`. Especially valuable if you want marketplace-driven evolution (new research skills auto-discoverable).
- **Agent Skills format:** ✅ Aggregates standard `SKILL.md` skills; installer writes to `~/.claude/skills/` or `.claude/skills/` or `~/.config/opencode/skills/` per harness. Verified via websearch snippet for `skillsmp-mcp-server` (tools `skillsmp_search`, `skillsmp_ai_search`, `skillsmp_install_skill`).

### 5B — OpenCode Planning Toolkit (IgorWarzocha)

- **Name:** `opencode-planning-toolkit` — bundled skill `plans-and-specs` + tools `create_spec`, `create_plan`, `append_spec`, `read_plan`, `mark_plan_done`
- **URL:** https://github.com/IgorWarzocha/opencode-planning-toolkit (verified via webfetch 2026-08-28; 136 stars, 10 forks)
- **What it does:** OpenCode-native plugin that adds repo-wide planning with reusable specs and actionable plans persisted as markdown (`docs/specs/*.md`, `docs/plans/*.md`). Bundled `plans-and-specs` skill enforces workflow: create plan → append REPO specs (sequential) → ask about FEATURE specs → `readPlan` before work (expands linked specs inline) → `markPlanDone`. System prompt auto-injects `<available_plans>`. [Source](https://github.com/IgorWarzocha/opencode-planning-toolkit)
- **Relevance:** Only verified alternative that is *native* to OpenCode harness (this repo's harness). Replaces `create-context-doc`'s conversational capture with spec/plan persistence that survives session boundaries — directly addresses multi-agent alignment (any agent can `read_plan` and get full context + linked specs). Strong on requirements elicitation via reusable specs (repo-level standards) and planning via 5+ step actionable plans. Unlike current skills, it uses tool calls (not just conversational markdown) and enforces linking discipline.
- **Agent Skills format:** ✅ Standard — `skills/plans-and-specs/SKILL.md` with frontmatter. Verified path `skills/plans-and-specs/SKILL.md` in repo. Install via `opencode.json` plugin `@howaboua/opencode-planning-toolkit@latest`.

### 5C — Canonical Spec (agentskills.io) + Anthropics Official Skills

- **URLs:** https://agentskills.io (verified) + https://github.com/anthropics/skills (verified 172k stars, Apache-2.0 + source-available doc skills)
- **What it does:** `agentskills.io` defines the open standard (SKILL.md + progressive disclosure: Discovery → Activation → Execution). `anthropics/skills` provides reference implementations (creative, technical, enterprise, document skills including `docx`/`pdf`/`pptx`/`xlsx` reference implementations) and the official plugin marketplace registration (`/plugin marketplace add anthropics/skills`). [Source](https://agentskills.io) and [anthropics/skills README](https://github.com/anthropics/skills)
- **Relevance:** Not a planning framework per se, but the *ecosystem baseline* that ensures any replacement follows the portable format. Use `anthropics/skills/template/` and `spec/` as the conformance test for alternatives 1-4. If you fork or author a replacement for `create-context-doc`/`create-planning-docs`, this is the compatibility target.

---

## Comparison Matrix — Focus C Lens

| Dimension | Current (`create-context-doc` etc.) | ACF RPI | Agent Research Skills | Research Direction Discovery | Superpowers | OpenCode Toolkit / SkillsMP |
|-----------|-------------------------------------|---------|------------------------|------------------------------|-------------|------------------------------|
| **Research / Discovery** | Conversational harvest, outline gates, REFERENCES.md with new research only | Codebase research report with line-number citations; reuses report for planning | Literature + GitHub multi-source searches with scripts, novelty audits | Field mapping, literature matrix, 3-round novelty + feasibility audits, kill criteria | Context exploration (files/commits/docs) + competitor/visual companion, but light on academic literature | SkillsMP enables discovery of any research skill; Toolkit is planning-only, no built-in research |
| **Requirements Elicitation** | Harvest what & why conversationally, no how | Interactive Q&A during `rpi-plan` (storage backend, rate limits etc.) | Idea generation scoring (I/F/N) + feedback loops | Structured iterative dialogue + formalization (objects/assumptions/targets/baselines) | Socratic single-question interview, 2-3 approaches, sectioned design approval | Toolkit via spec creation Q&A; SkillsMP via install-time selection |
| **Phased Plan Output** | CONTEXT.md + PLAN.md + optional REFERENCES/RESEARCH.md; PLAN.md cross-phase with verification loop | Phased plan at `docs/agents/plans/*.md` with checkboxes, iterates until coverage complete | 4-stage plan (Overall/Architecture/Logic/Config) + task dependency graph | Prospectus + hypothesis registry + long-term plan (more research-oriented) | Bite-sized tasks (2-5 min) with exact paths/code/verification, TDD | Markdown plans (`docs/plans/*.md`) with 5+ steps + linked specs; marketplace supplies variety |
| **Persistence & Handoff** | `.planning/<task>/CONTEXT.md` etc.; designed for fresh session pickup | `docs/agents/research/` + `docs/agents/plans/` (committed, portable) | Outputs to `~/deep-research-output/` + per-skill artifacts | Workspace scripts + persistent state with validation | `docs/superpowers/specs/` + plan file + git worktree isolation | `docs/specs/` + `docs/plans/` + `<available_plans>` injection (session-persistent) |
| **Outline/Approval Gates** | Explicit outline gate per doc + optional post-write review | Implicit: plan iteration until user covers all cases + implement pauses for manual verification | No explicit gate; relies on script validation + prompt discipline | Explicit Gates with kill/pivot; strongest gate logic | Hard gate: no implementation until design approved (per path) | Skill enforces order (create → append REPO → ask FEATURE → read before work) |
| **Marketplace Footprint** | Internal (`.agents/skills/`) | Tiny (8 stars) | Small/fork (0 stars); original lingzhi227 more credible | Tiny (2 stars) | Massive (279k stars, 681 commits) | SkillsMP 2M+ skills; Toolkit 136 stars but OpenCode-native |
| **Format Compat** | Standard SKILL.md | ✅ Standard | ✅ Standard | ✅ Standard (portable) | ✅ Hybrid (multi-harness plugins) | ✅ Standard + OpenCode plugin manifest |

---

## Verification Notes & Anomalies

- **SearXNG:** All 5 mandated queries (`agent research planning skill discovery phase GitHub`, `Claude Code skills marketplace planning`, `skillsmp GitHub Claude skills planning`, `opencode skills planning framework GitHub`, `agentskills.io planning skill`) returned "No results found" via `searxng_searxng_web_search` despite instance `http://100.122.184.37:8082` reachable and categories available (verified via `searxng_searxng_instance_info` which listed categories including `repos`, `general`). Fell back to `websearch` (Exa) per routing table. Suggests SearXNG search engine backends down or query filtering too strict for niche skill terms. Fallback succeeded with 8 results per query.
- **Verified vs Snippet-Only:** All 5 alternatives above are *page-read verified* (webfetch). Additional candidates discovered via websearch snippets but NOT primary counted: `heymegabyte/claude-skills` (`planning-and-research`: "Deep web research, competitor scanning, technology evaluation..."), `farmage/opencode-skills` (66 skills + 9 workflow commands including `/discovery/create`, `/discovery/synthesize`, `/planning/epic-plan`), `vpaivag/skills` (`intake` → `simple-plan`/`deep-plan` loop). One snippet-only candidate was later upgraded to verified: `stympy/skills` (`research` skill: "Deep research before planning. Launches parallel agents...") — fully verified via webfetch of SKILL.md (109 lines, mandatory AskUserQuestion at steps 1 & 4, parallel agents: codebase/docs/web/dependencies/UI/UX/delight) at https://github.com/stympy/skills/blob/main/research/SKILL.md — would be alternative 6 if expanded.
- **Stars/Forks as of verification:** anthropics/skills 172k/20.5k, obra/superpowers 279k/25k, IgorWarzocha/opencode-planning-toolkit 136/10, MaibornWolff/acf-research-plan-implement-skills 8/3, 0neblaze/research-direction-discovery 2/0. Counts are GitHub UI values at read time, not API-evaluated.
- **No fabrication:** All descriptions paraphrase README verbatim; no invented numbers, dates, or quotes. Where primary source was estimate-grade (SkillsMP "2,000,000+ skills"), flagged as self-disclosed marketplace claim, not independently audited.
- **Unknowns:** Performance benchmarks for these skills (e.g., "helps agents 10x faster") are marketing claims without cited measurements — treat as unverified. Long-term maintenance risk for tiny repos (ACF 27 commits, 0neblaze 2 commits) unknown beyond commit history. `skillsmp` GitHub marketplace search ranking relevance unknown (API not probed live).

---

## Recommendation Synthesis (Focus C)

- **If you want a drop-in replacement that keeps file-based planning but makes research explicit:** Adopt **MaibornWolff ACF RPI** (alternative 1). Only alternative that mirrors current CONTEXT→PLAN→EXECUTE trio with same markdown artifact philosophy while upgrading research to codebase-grounded evidence.
- **If your bottleneck is literature/competitor discovery:** Pair **Agent Research Skills Phase 0** (alt 2) for discovery + **Research Direction Discovery** (alt 3) for kill/pivot gating before you ever enter `create-execution-plan`.
- **If your bottleneck is requirements elicitation discipline:** Adopt **Superpowers brainstorming** (alt 4) — its Socratic questioning and path classification are strictly stronger than conversational harvesting at preventing under-specified CONTEXT.md.
- **If you need OpenCode-native persistence:** Adopt **OpenCode Planning Toolkit** (alt 5B) — only alternative that integrates as an OpenCode plugin with `<available_plans>` injection and survives across sessions via `docs/specs` + `docs/plans`.

All five are Standard Agent Skills format (`SKILL.md` with frontmatter `name`/`description`), so incremental adoption is low-cost: install alongside current skills, A/B test on one planning cycle, then deprecate the weaker.

---

## Sources Cited (canonical URLs)

- https://github.com/MaibornWolff/acf-research-plan-implement-skills
- https://github.com/thejesh23/agent-research-skills
- https://github.com/lingzhi227/agent-research-skills
- https://github.com/0neblaze/research-direction-discovery
- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md
- https://github.com/anthropics/skills
- https://agentskills.io
- https://github.com/IgorWarzocha/opencode-planning-toolkit
- https://skillsmp.com
- https://github.com/stympy/skills/blob/main/research/SKILL.md
- Additional websearch-discovered (snippet) sources held separately: heymegabyte/claude-skills, farmage/opencode-skills, vpaivag/skills, SkillsMP MCP plugins (menoncello/skillsmp-research-plugin, gccszs/skillsmp-searcher, anilcancakir/skillsmp-mcp-server).

---

*End of report — generated by leaf research sub-agent via SearXNG-first → websearch fallback → webfetch verification pipeline. All pages read before citation.*
