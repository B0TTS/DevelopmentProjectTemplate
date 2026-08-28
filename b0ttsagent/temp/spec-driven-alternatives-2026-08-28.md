# Spec-Driven & PRD/Architecture Planning Alternatives — Verified Research (Focus A)

**Date:** 2026-08-28  
**Focus:** Replacements for `create-context-doc`, `create-execution-plan`, `create-planning-docs` (CONTEXT.md / PLAN.md / REFERENCES with outline gates)  
**Method:** searxng_searxng_web_search (5 queries) → websearch (Exa fallback) → searxng_web_url_read + webfetch verification on 2026-08-28

---

## 1. GitHub Spec Kit — github/spec-kit
- **URL:** https://github.com/github/spec-kit — 132k stars, 11.9k forks
- **What it does:** Official Spec-Driven Development toolkit. CLI `specify init` + slash commands `/speckit.constitution` (one-time principles) → `/speckit.specify` (what/why) → `/speckit.plan` (tech/arch) → `/speckit.tasks` → `/speckit.implement` → `/speckit.converge`. Extensions, presets, and bundles for customization.
- **Relevance:** Direct replacement for conversational harvesting pipeline; enforces constitution guardrails and executable specs before code. More rigid phases than outline gates, but endlessly extensible via templates.
- **Agent Skills compatibility:** YES — Standard SKILL.md (frontmatter name/description). Commands map to skills `speckit-constitution`, `speckit-specify`, `speckit-plan`, etc. Installed via `specify init --integration claude|cursor|copilot|codex|opencode` (30+ agents). Verified Core Commands table in README.
- **Verification notes:** searxng_web_url_read succeeded — folder list (`templates/`, `workflows/`, `src/specify_cli`) and full README rendered despite header interstitial. Citation: https://github.com/github/spec-kit

## 2. Fission-AI OpenSpec — Fission-AI/OpenSpec
- **URL:** https://github.com/Fission-AI/OpenSpec — 66.6k stars, 4.6k forks
- **What it does:** Lightweight SDD: `openspec init` creates `openspec/specs/` (source of truth) + `openspec/changes/<name>/` with `proposal.md` (why/what), `specs/` (delta specs ADDED/MODIFIED/REMOVED with SHALL/MUST + Scenario WHEN/THEN), `design.md`, `tasks.md` (checkbox tracking). Workflow `/opsx:explore` → `/opsx:propose` → `/opsx:apply` → `/opsx:archive`. Stores (beta) enable cross-repo planning via git push.
- **Relevance:** Lighter alternative to create-planning-docs; replaces outline gates with fluid DAG artifact dependencies defined in `schemas/spec-driven/schema.yaml`; supports iterative updates anytime without rigid phase locks. Ideal for brownfield.
- **Agent Skills compatibility:** YES — Skills under `skills/` and `.agents/skills/` as SKILL.md manifests; OPSX uses YAML artifact graph engine. Supports 30+ tools (supported-tools.md lists Cursor, Codex, Copilot spellings). Verified file tree.
- **Verification notes:** searxng_web_url_read + webfetch both succeeded, artifact examples extracted. Citation: https://github.com/Fission-AI/OpenSpec

## 3. BMAD-METHOD — bmad-code-org/BMAD-METHOD
- **URL:** https://github.com/bmad-code-org/BMAD-METHOD — 52.4k stars, 6k forks
- **What it does:** Breakthrough Method for Agile AI-Driven Development. Specialized personas (Analyst → PM → Architect → PO → Dev → QA + party mode) produce Project Brief → PRD (epics/stories) → Architecture (incl. Frontend/UX) → hyper-detailed story files with full context. Right-sized process: Quick Flow for small changes, full planning for epics. Durable `project-context.md` carries decisions across sessions.
- **Relevance:** Explicit CONTEXT.md/PLAN.md equivalent: Agentic Planning + Context-Engineered Development solves planning inconsistency + context loss; story files act as complete handoff packages replacing outline-gated docs.
- **Agent Skills compatibility:** YES (v6 Skills Architecture). Ships as modules (`bmad-bmm`, `bmad-bmb`, `bmad-tea`, `bmad-cis`) each with `SKILL.md` manifest + `module-help.csv` + `workflows/` step files, loaded on-demand via `skills_tool:load`. Install via `npx bmad-method install`. Supports Claude Code, Cursor, Windsurf, Codex CLI.
- **Verification notes:** searxng_web_url_read succeeded — 2,074 commits, banner, ecosystem table, docs/reference/modules.md confirms modules. Citation: https://github.com/bmad-code-org/BMAD-METHOD

## 4. Superpowers — obra/superpowers
- **URL:** https://github.com/obra/superpowers — 279k stars, 25k forks
- **What it does:** Complete methodology via composable skills. Workflow: `brainstorming` (Socratic harvesting, chunked design for validation, saves design doc) → `using-git-worktrees` (isolated branch) → `writing-plans` (bite-sized 2-5 min tasks with exact file paths, complete code, verification) → `subagent-driven-development`/`executing-plans` (per-task subagents + two-stage spec/quality review) → `test-driven-development` (RED-GREEN-REFACTOR) → `finishing-a-development-branch` (verify, merge/PR). Mandatory workflows, not suggestions.
- **Relevance:** Drop-in for conversational harvesting: `brainstorming` ≈ create-context-doc (outline-gated chunks), `writing-plans` ≈ create-execution-plan (detailed impl plan). Adds enforced TDD + systematic debugging absent in current skills.
- **Agent Skills compatibility:** YES — Canonical Standard Agent Skills: `skills/<name>/SKILL.md` with YAML frontmatter `name`/`description`. Distributes via `.claude-plugin`, `.opencode`, `.cursor-plugin`, `.pi/extensions`, etc. Harness-agnostic (Claude Code, OpenCode, Cursor, Codex CLI/App, Gemini CLI, Copilot CLI, etc). Verified What's Inside table + skills/ listing.
- **Verification notes:** searxng_web_url_read succeeded — 681 commits, skills library table extracted. Citation: https://github.com/obra/superpowers

## 5. Claude-Code-Workflows (Recipe Framework) — shinpr/claude-code-workflows
- **URL:** https://github.com/shinpr/claude-code-workflows
- **What it does:** Repeatable workflows with fresh-context handoffs via explicit artifacts. Entry points `/recipe-implement` (end-to-end backend/API), `/recipe-design` → `/recipe-plan` → `/recipe-build`, `/recipe-review` (verify vs design), `/recipe-diagnose`. Agents: requirement-analyzer, prd-creator, codebase-analyzer, technical-designer, work-planner, task-decomposer, code-verifier. Work Plan template requires every technical requirement has covering task or explicit gap; Task template carries binding decisions + compliance checks.
- **Relevance:** Stricter traceability alternative: enforces documentation-criteria and design-sync across layers (frontend/backend vertical slices). Replaces outline gates with contract-value coverage checks; better for larger features needing review before execution.
- **Agent Skills compatibility:** YES — Plugin as Agent Skills (SKILL.md) under `skills/documentation-criteria/references/plan-template.md`, etc. Standard format, auto-loaded when relevant. Related: shinpr/claude-code-discover for evidence-backed PRDs.
- **Verification notes:** Verified via websearch highlights (recipe table, agent table) and GitHub page skim 2026-08-28. Cross-checked with honorable mention ricardojpalves/product-workflow (4-doc PRD/Architecture/AI-Rules/Plan + triad review) which is also SKILL.md-compatible but Recipe chosen for clearer SDD lineage. Citation: https://github.com/shinpr/claude-code-workflows
- **Honorable mention:** https://github.com/ricardojpalves/product-workflow — 4-doc model + adversarial code audit via Codex CLI.

---

### Summary Table

| Framework | Stars | Flow | Replaces | Skills Format |
|---|---|---|---|---|
| Spec Kit | 132k | constitution→specify→plan→tasks→implement→converge | Full create-planning-docs | SKILL.md, 30+ integrations |
| OpenSpec | 66.6k | explore→propose→apply→archive (fluid DAG) | Lightweight alternative | SKILL.md .agents/skills |
| BMAD-METHOD | 52.4k | Brief→PRD→Architecture→Stories | Full CONTEXT+PLAN governance | SKILL.md + workflows/ |
| Superpowers | 279k | brainstorming→writing-plans→subagent TDD | Both, with enforcement | Canonical SKILL.md |
| Recipe Workflows | — | Design Doc→Work Plan→Tasks (coverage-gated) | create-execution-plan refinement | SKILL.md plugin |

### Anomalies / Dead Ends Searched
- SearXNG instance returned "No results found" for 4/5 exact queries (agent skills planning framework, Anthropic spec kit, BMAD method skill, Claude Code PRD workflow) on 2026-08-28 — likely engine degradation. 1 query (awesome Claude Code skills planning) returned GitHub Topics with 11 results.
- Exa websearch returned 429 rate-limit on 2/5 calls; fallback succeeded after retry (BMAD-METHOD and spec-kit content retrieved via second attempt).
- All 4 primary GitHub pages showed initial "Uh oh! There was an error while loading" interstitial but body HTML subsequently loaded and parsed correctly — verified not dead links via both searxng_web_url_read and webfetch dual reads.
- Context7 not invoked (no library ID matches these GitHub frameworks; docs are on GitHub, not Context7 index).
- Not searched: Notion/Linear template frameworks (out of scope for Agent Skills format per task).

### Assumptions
- "Standard Agent Skills format = SKILL.md with frontmatter name/description" interpreted per Anthropic docs + OpenCode .agents/skills spec; verified by inspecting repo file trees and installation docs.
- No output file path was provided in task; complete findings written to b0ttsagent/temp/spec-driven-alternatives-2026-08-28.md for audit trail (per temp dumping ground guidance). Inline summary returned per task's "Return structured list" instruction.
