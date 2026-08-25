# Researcher B — Community Claude Skill Marketplaces: Prompt-Writing / Prompt-Refinement Skills

**Date:** 2026-08-18
**Scope:** Find and compare activatable agent skills (SKILL.md-format or platform equivalents) whose entire purpose is prompt writing / prompt refinement — ideally with an interactive Q&A workflow (skill interviews the user, then produces a polished ready-to-use prompt).
**Method:** Searched the requested indexes (travisvn/awesome-claude-skills, awesomeclaude.ai, skillmd.com, awesomeskill.ai, claudeskills.info, mcpmarket.com, chat2anyllm.github.io/awesome-claude-skills) plus GitHub search API and the claudeskills.info + skillmd.com JSON search APIs. Every candidate's actual SKILL.md / agent file was read (raw.githubusercontent.com or skillmd raw API), not just snippets.

---

## Summary of Findings

The market is **thin** for the exact use case (interactive prompt-refinement via Q&A). Only **two** skills genuinely implement the "interview the user, then produce a polished prompt" workflow:

1. **`boost-prompt`** (github/awesome-copilot, indexed on skillmd.com as `github/boost-prompt`) — **the single best match.** Interactive questioning via the Joyride extension, then copies the final markdown prompt to the clipboard. Requires the Joyride VS Code extension.
2. **`prompt-engineer`** (Sourabhj00/prompt-engineer) — Claude Code skill with a 6-step process that includes a mandatory "Context Gap Questions" step (asks targeted questions and waits for answers) before generating an XML-structured Master Prompt with per-change reasoning.

Everything else found is either **non-interactive** (analyzes + rewrites in one shot: `prompt-optimizer`, `Prompt Engineer` agent, `Prompt Builder` agent, `prompt-improver`, `finalize-agent-prompt`, `getsentry/prompt-optimizer`, `prompt-engineer-toolkit`, `cs-prompt-engineer`) or **interactive but for a different purpose** (intent extraction before building / spec prep / task refinement before executing: `interview-me`, `first-ask`, `grill`, `ask-questions-if-underspecified`).

**Named-skill hunt results:** `boost-prompt` ✅ found; `prompt-engineer` ✅ found (several variants); `prompt-improvement` ❌ no skill by that exact name (only a `prompt-improve` slash command and a `prompt-improver` agent); `prompt-refiner` / `prompt-refine` ❌ no SKILL.md skill (GitHub repos with those names are Python libraries / web tools, not agent skills); `prompt-polish` ❌ not found; `interview` ❌ no skill named exactly "interview" (closest: interview-me, first-ask, grill); "prompt interrogation" ❌ no skill under that name.

---

## TIER 1 — Interactive prompt-refinement skills (the target use case)

### 1. `boost-prompt` — BEST MATCH
- **Name / source:** `boost-prompt` — https://github.com/github/awesome-copilot/tree/main/skills/boost-prompt (indexed on skillmd.com as `github/boost-prompt`: https://skillmd.com/skills/github/boost-prompt)
- **Platform:** SKILL.md format → Claude Code, Claude.ai, Codex, Copilot. **Requires the Joyride extension** (VS Code) for the human-input tool and clipboard.
- **Install:** `npx skillmds add github/boost-prompt` (skillmd CLI) — or clone `github/awesome-copilot` and copy `skills/boost-prompt/`. Source repo install: `git clone https://github.com/github/awesome-copilot.git`.
- **Workflow (from the actual SKILL.md):**
  1. User hands over a prompt; the skill's goal is to iteratively refine it.
  2. Understands task scope and objectives; **at all times when clarification is needed, asks specific questions to the user via the `joyride_request_human_input` tool**.
  3. Defines expected deliverables and success criteria; may perform project explorations with available tools.
  4. Clarifies technical/procedural requirements; organizes the prompt into clear sections/steps.
  5. Produces the improved prompt as markdown, **copies it to the system clipboard via Joyride** (`vscode/env.clipboard.writeText`), and also types it in chat.
  6. Announces it's on the clipboard and asks if the user wants changes; repeats copy + chat + ask after revisions. **Never writes code.**
- **Interactive questions?** **YES** — explicitly uses `joyride_request_human_input` for iterative questioning.
- **Quality signals:** skillmd safety-reviewed (`verified: true`), avg rating 4.2/5 (5 ratings), install_count 0 on skillmd (new). Source repo `github/awesome-copilot` = **37,986 stars**, MIT license, actively maintained (pushed 2026-08-18). The SKILL.md body itself is short (~30 lines) — it leans on the Joyride tool rather than a rich checklist.
- **Pros vs. use case:** exact workflow (interrogate scope/deliverables/constraints → polished prompt); clipboard output is a nice touch; from a high-authority, actively-maintained repo (GitHub org).
- **Cons:** hard dependency on the Joyride extension (VS Code) — won't work in a plain terminal/opencode without it; thin skill body (no quality checklist, no change-reasoning); no file-save option (clipboard + chat only).

### 2. `prompt-engineer` (Sourabhj00) — strong second
- **Name / source:** `prompt-engineer` — https://github.com/Sourabhj00/prompt-engineer (README + SKILL.md read and verified)
- **Platform:** Claude Code skill (also usable in other SKILL.md-compatible agents).
- **Install:** `claude skill add Sourabhj00/prompt-engineer` — or `git clone https://github.com/Sourabhj00/prompt-engineer.git` and copy the `prompt-engineer/` folder into the skills dir.
- **Workflow (6 steps, from the actual SKILL.md):**
  1. **Critical Analysis** — "golden rule" litmus test; flags vague language, missing roles, unclear output expectations, unstated constraints.
  2. **Context Gap Questions** — **asks targeted questions** (audience/persona, output format, constraints/scope, tone, examples/edge cases, large-context handling) in a fixed `CONTEXT GAPS:` format; **waits for the user to respond before proceeding**; supports `[SKIP]` → proceeds with labeled `[ASSUMPTION: ...]`; identifies whether the prompt is system / user-turn / both.
  3. **Checklist Review** — evaluates against a 19-item checklist (`references/checklist.md`), each item marked present/missing/partial with a specific fix.
  4. **Master Prompt Generation** — XML-tagged structure (`<role> <task> <context> <instructions> <output_format> <constraints> <examples>`) with typed example tags; output branches by prompt type.
  5. **Reasoning Summary** — `[Change] → [Reason]` for every change + self-evaluation pass.
  6. **Iterative Refinement** — on feedback, patches the Master Prompt without restarting (re-runs checklist, shows only changed sections).
  - Hard constraint: never generates the Master Prompt before Steps 1–3 complete.
- **Interactive questions?** **YES** — Step 2 is a mandatory question-asking step that blocks until the user answers.
- **Quality signals:** 1 star, 4 commits, MIT; repo includes `references/checklist.md`, `examples/before-after.md`, `evals/evals.json` (20 trigger test cases), and Python tooling (quick_validate, run_eval, run_loop). Well-structured but **very low adoption** (1 star, no install counts discoverable).
- **Pros vs. use case:** the most complete structured workflow of all candidates; genuinely interactive; explains every change; handles system/user/both prompt types; iterative refinement loop; bundled checklist and examples.
- **Cons:** tiny community footprint (1 star — unproven); no clipboard/file output (prints in chat); Gemini Pro + Claude focused; no install-count evidence.

---

## TIER 2 — Non-interactive prompt optimizers (rank lower per the #1 criterion)

### 3. `prompt-optimizer` (github/awesome-copilot)
- **Name / source:** `prompt-optimizer` — https://github.com/github/awesome-copilot/tree/main/skills/prompt-optimizer (skillmd: `github/prompt-optimizer`)
- **Platform:** SKILL.md → Claude Code / Claude.ai / Codex / any chat LLM.
- **Install:** `npx skillmds add github/prompt-optimizer` or clone awesome-copilot.
- **Workflow:** one-shot rewrite. Turns a rough draft / vague idea / task description into a single finished, copy-pasteable prompt in a code block. Two hard rules: (1) **no placeholders ever** — output must be sendable as-is; (2) ship a finished prompt no matter the input (bake content in, or instruct the target LLM to ask for missing inputs). Internal 9-step rewrite workflow ("work through these in your head… you don't need to surface them"). Ends with a reasoning-depth closing line.
- **Interactive questions?** **NO** — explicitly does NOT surface questions; makes defensible assumptions instead.
- **Quality signals:** skillmd verified, **4.5/5** (4 ratings) — highest rating found; very detailed SKILL.md (principles, 5 worked examples, edge cases); source repo 37,986 stars.
- **Pros:** excellent output quality; no-placeholder guarantee; chat-interface focused (matches "give to any LLM"); strong examples.
- **Cons:** no interactivity; no explanation of changes unless the user asks afterward; no clipboard/file output (code block in chat).

### 4. `Prompt Engineer` agent (github/awesome-copilot)
- **Name / source:** `Prompt Engineer` — https://github.com/github/awesome-copilot/blob/main/agents/prompt-engineer.agent.md
- **Platform:** GitHub Copilot CLI agent (`.agent.md` chat mode — not a SKILL.md).
- **Workflow:** treats every user input as a prompt to improve; emits a `<reasoning>` analysis (simple-change check, reasoning/CoT placement, structure, examples, complexity, specificity, prioritization) based on OpenAI prompt-engineering best practices, then outputs the improved prompt verbatim with no commentary.
- **Interactive questions?** **NO** — single-pass analyze + rewrite.
- **Quality signals:** from github/awesome-copilot (37,986 stars); detailed framework; high confidence per claudeskills.info.
- **Pros:** strong analysis framework; clean verbatim output.
- **Cons:** no interactivity; Copilot-specific format (not portable to opencode/Claude Code as a skill).

### 5. `Prompt Builder` agent (microsoft/edge-ai, mirrored in awesome-copilot)
- **Name / source:** `Prompt Builder` — https://github.com/github/awesome-copilot/blob/main/agents/prompt-builder.agent.md (originally microsoft/edge-ai)
- **Platform:** GitHub Copilot CLI agent.
- **Workflow:** dual-persona (Prompt Builder + Prompt Tester). Research-driven: reads READMEs, GitHub repos, code, web docs, context7; identifies weaknesses; improves; then **mandatory validation** — Prompt Tester executes the improved prompt and reports in-conversation; iterate up to 3 cycles.
- **Interactive questions?** **NO** — no user questioning; self-validates via the Tester persona.
- **Quality signals:** from microsoft/edge-ai; mirrored in 37,986-star repo.
- **Pros:** rigorous research + validation loop; good for production prompts tied to a codebase.
- **Cons:** heavyweight (needs many tools); no interactivity; Copilot-specific; overkill for a simple "refine my prompt" ask.

### 6. `prompt-improver` (Dlaby23)
- **Name / source:** `prompt-improver` — https://github.com/Dlaby23/claude-agents-ultimate-collection/blob/main/agents/practices/001_prompt-improver.md
- **Platform:** Claude Code subagent (agent.md; `model: claude-sonnet-4-20250514`).
- **Workflow:** one-pass enhance/refine — clarity, grammar, structure, specificity, ambiguity resolution — while **strictly preserving original intent** (never adds features/requirements); provides before/after comparison and documents what changed.
- **Interactive questions?** **NO** — single-pass rewrite.
- **Quality signals:** repo ~1 star; simple single-file agent; clear "NEVER change / ALWAYS improve" rules.
- **Pros:** intent-preservation discipline; before/after output.
- **Cons:** no interactivity; minimal adoption; no install counts.

### 7. `finalize-agent-prompt` (github/awesome-copilot)
- **Name / source:** `finalize-agent-prompt` — https://github.com/github/awesome-copilot/tree/main/skills/finalize-agent-prompt (skillmd: `github/finalize-agent-prompt`)
- **Platform:** SKILL.md → Claude Code / Codex.
- **Workflow:** refines/polishes a **prompt file** (structure, wording, clarity) preserving front matter, encoding, markdown structure and original intent.
- **Interactive questions?** **PARTIAL** — asks for the prompt file if none is provided; otherwise no questioning.
- **Quality signals:** skillmd verified, 4.2/5 (5 ratings); short skill.
- **Pros:** good for polishing existing prompt files in place.
- **Cons:** file-oriented, not chat-prompt-oriented; minimal interactivity.

### 8. `prompt-optimizer` (getsentry)
- **Name / source:** `prompt-optimizer` — https://github.com/getsentry/prompt-optimizer (skillmd: `getsentry/prompt-optimizer`)
- **Platform:** SKILL.md pack → Claude Code / Codex.
- **Workflow:** eval-driven optimization: capture contract → inventory external context → choose model strategy → shape prompt → optimize with evals (baseline, cluster failures, generate 2–4 candidates, compare, validate on holdout) → return package (Target, Success Criteria, Optimized Prompt, Adapter Notes, Eval Set, Optimization Log, Residual Risks).
- **Interactive questions?** **NO** — systematic/evals workflow, not user Q&A.
- **Quality signals:** skillmd verified, 4.2/5 (5 ratings); from Sentry (high authority); pack with references.
- **Pros:** rigorous, production-grade; model-family porting (OpenAI/Claude/Gemini).
- **Cons:** no interactivity; heavy eval machinery — overkill for casual prompt refinement.

### 9. `prompt-engineer-toolkit` (alirezarezvani/claude-skills, marketing)
- **Name / source:** `prompt-engineer-toolkit` — https://github.com/alirezarezvani/claude-skills/blob/main/marketing-skill/skills/prompt-engineer-toolkit/SKILL.md
- **Platform:** SKILL.md (Claude Code / Codex / Gemini).
- **Workflow:** A/B prompt evaluation against structured test cases (`scripts/prompt_tester.py`), immutable versioning with diffs (`scripts/prompt_versioner.py`), marketing prompt templates, LLM-governance playbook.
- **Interactive questions?** **NO** — script-driven testing/versioning.
- **Quality signals:** from alirezarezvani/claude-skills (345-skill repo); MIT; versioned (1.0.0, updated 2026-03-06).
- **Pros:** measurable quality, versioning, regression safety.
- **Cons:** marketing-specific; no interactivity; tooling overhead.

### 10. `cs-prompt-engineer` (borghei/Claude-Skills)
- **Name / source:** `cs-prompt-engineer` — https://github.com/borghei/Claude-Skills/blob/main/agents/engineering/cs-prompt-engineer.md
- **Platform:** Claude Code subagent (agent.md) + two underlying skills (`senior-prompt-engineer`, `prompt-governance`).
- **Workflow:** senior prompt-engineering practice — agentic system design, prompt optimization via `prompt_optimizer.py`, RAG evaluation, prompt-catalog governance/auditing.
- **Interactive questions?** **NO** — engineering workflow agent.
- **Quality signals:** borghei/Claude-Skills (~325 stars); structured with scripts and knowledge bases.
- **Pros:** deep, production-grade prompt engineering.
- **Cons:** not a conversational refiner; no interactivity; heavy.

---

## TIER 3 — Adjacent interactive skills (interview-style, but NOT prompt refinement)

These ask the user questions interactively but produce something other than a polished prompt (intent statement, spec, plan, or task execution). Listed for completeness; they are the closest "interview" skills in the ecosystem.

### 11. `interview-me` (addyosmani)
- **Source:** https://github.com/addyosmani/agent-skills (skillmd: `addyosmani/interview-me`)
- **Workflow:** one-question-at-a-time interview, each question with an attached GUESS, until ~95% confidence; then restates intent (Outcome / User / Why now / Success / Constraint / Out of scope) and requires an explicit "yes".
- **Interactive?** **YES** — but output is a **confirmed statement of intent**, not a refined prompt. Explicitly warns against non-interactive contexts.
- **Quality:** high-quality, detailed SKILL.md from Addy Osmani; not skillmd-verified.

### 12. `first-ask` (github/awesome-copilot)
- **Source:** https://github.com/github/awesome-copilot/tree/main/skills/first-ask (skillmd: `github/first-ask`)
- **Workflow:** interrogates scope/deliverables/constraints via `joyride_request_human_input` **before carrying out the task**, then shows a plan, makes a todo list, and executes.
- **Interactive?** **YES** — but it then executes the task itself; it does not hand back a reusable prompt. Requires Joyride.

### 13. `grill` (JuliusBrussee/cavekit)
- **Source:** https://github.com/JuliusBrussee/cavekit/blob/main/skills/grill/SKILL.md
- **Workflow:** one question at a time with a recommended answer; lands answers into §G (goal) / §C (constraints); parks unknowns as `?`; hands off to a spec skill.
- **Interactive?** **YES** — but for sharpening a fuzzy idea into a spec, not refining an existing prompt.

### 14. `ask-questions-if-underspecified` (trailofbits)
- **Source:** https://github.com/trailofbits/skills (skillmd: `trailofbits/ask-questions-if-underspecified`)
- **Workflow:** asks targeted questions when a request has multiple plausible interpretations before implementing.
- **Interactive?** **YES** — but for clarifying requirements before implementation, not prompt refinement. skillmd-verified.

---

## Named-skill hunt results (explicit)

| Named skill | Found? | Notes |
|---|---|---|
| `boost-prompt` | ✅ | github/awesome-copilot `skills/boost-prompt`; indexed on skillmd.com as `github/boost-prompt`. Interactive + clipboard. **Top candidate.** |
| `prompt-engineer` | ✅ | Multiple: Sourabhj00/prompt-engineer (skill, interactive), github/awesome-copilot `agents/prompt-engineer.agent.md` (Copilot agent, non-interactive), jeffallan/prompt-engineer (pack), borghei cs-prompt-engineer (agent). |
| `prompt-improvement` | ❌ | No skill by that exact name. Closest: `prompt-improve` slash command (jeremylongshore/claude-code-plugins-plus-skills) and `prompt-improver` agent (Dlaby23). |
| `prompt-refiner` | ❌ | No SKILL.md skill. GitHub repos named prompt-refiner are Python libraries / web tools (JacobHuang91/prompt-refiner = token-optimization lib; rod-trent/Prompt_Refiner = web tool; farukalpay/prompt-refinery = Python lib/CLI/MCP). |
| `prompt-refine` | ❌ | No skill found. |
| `prompt-polish` | ❌ | No skill found (skillmd "polish" search returns unrelated skills). |
| `interview` | ❌ | No skill named exactly "interview". Closest: interview-me, first-ask, grill, grilling. |
| "prompt interrogation" | ❌ | No skill under that name in any searched index. |

---

## Marketplace coverage notes

- **skillmd.com** — richest source for this category (JSON API `api.skillmd.com/v1/search`). Safety-reviewed registry (5,538 skills). Found: boost-prompt, prompt-optimizer, finalize-agent-prompt, first-ask, interview-me, getsentry/prompt-optimizer, ask-questions-if-underspecified. Install via `npx skillmds add <owner>/<name>`.
- **claudeskills.info** — 42,815 indexed skills with JSON API (`/api/v1/search`). Found: Prompt Engineer agent, Prompt Builder agent, prompt-improver, prompt-engineer-toolkit, prompt-library, cs-prompt-engineer, prompt-improve command. Install via `npx skills add <owner>/<repo> --skill <name> --agent claude-code`.
- **travisvn/awesome-claude-skills** — curated list; **no dedicated prompt-refinement skill** listed (mostly official Anthropic skills + a handful of community skills).
- **awesomeclaude.ai/awesome-claude-skills** — 204-skill curated directory; **no dedicated prompt-refinement skill** found.
- **chat2anyllm.github.io/awesome-claude-skills** — metadata catalog (97,454 discoverable skills across 3,180 repos); not individually searched per-skill for prompt refiners (noted as a gap).
- **awesomeskill.ai** — marketplace exists (SearXNG snippet only); not deeply searched (gap).
- **mcpmarket.com** — MCP-server marketplace, not agent skills; out of scope for SKILL.md candidates (gap noted).

---

## Open questions / gaps

1. **Output delivery:** Only `boost-prompt` copies to clipboard (via Joyride). `prompt-optimizer` and `prompt-engineer` print in chat/code block. **No candidate saves to a file by default** — if file output is required, it would need to be added.
2. **Joyride dependency:** `boost-prompt` and `first-ask` require the Joyride VS Code extension (`joyride_request_human_input` tool). In a plain terminal / opencode / non-VS-Code harness, this tool won't exist — the skill would degrade to plain chat questioning (still workable, but clipboard copy breaks). This is the biggest practical caveat for the top candidate.
3. **Adoption data is thin:** install counts are only surfaced on skillmd (all 0 for these), and star counts are low for the interactive candidates (Sourabhj00/prompt-engineer = 1 star). No evidence of real-world usage for any interactive candidate.
4. **No "prompt interrogation" niche exists** as a named category — the interview-style skills that do exist (interview-me, grill, first-ask) target intent/spec extraction, not prompt refinement. A custom skill may be warranted if the exact workflow (interview → polished prompt) is required without Joyride.
5. **awesomeskill.ai and chat2anyllm per-skill search** were not exhaustively crawled (context budget); a deeper crawl of those two could surface additional long-tail candidates.
6. **`prompt-engineer` (Sourabhj00) trigger reliability** is unverified in practice — it ships eval tooling but no published pass-rate results.

---

## Sources read (primary, verified)

- https://github.com/github/awesome-copilot/tree/main/skills/boost-prompt (SKILL.md via skillmd raw API)
- https://api.skillmd.com/api/skills/github/boost-prompt/raw
- https://api.skillmd.com/v1/skills/github/boost-prompt (detail: source repo, install snippet, verified flag)
- https://github.com/Sourabhj00/prompt-engineer (README) + https://raw.githubusercontent.com/Sourabhj00/prompt-engineer/main/prompt-engineer/SKILL.md
- https://github.com/github/awesome-copilot/blob/main/agents/prompt-engineer.agent.md
- https://github.com/github/awesome-copilot/blob/main/agents/prompt-builder.agent.md
- https://raw.githubusercontent.com/Dlaby23/claude-agents-ultimate-collection/main/agents/practices/001_prompt-improver.md
- https://raw.githubusercontent.com/borghei/Claude-Skills/main/agents/engineering/cs-prompt-engineer.md
- https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/prompt-engineer-toolkit/SKILL.md
- https://raw.githubusercontent.com/JuliusBrussee/cavekit/main/skills/grill/SKILL.md
- https://api.skillmd.com/api/skills/github/prompt-optimizer/raw
- https://api.skillmd.com/api/skills/github/finalize-agent-prompt/raw
- https://api.skillmd.com/api/skills/getsentry/prompt-optimizer/raw
- https://api.skillmd.com/api/skills/github/first-ask/raw
- https://api.skillmd.com/api/skills/addyosmani/interview-me/raw
- https://github.com/josix/agent-flow/blob/main/skills/prompt-refinement/SKILL.md
- https://github.com/travisvn/awesome-claude-skills (README)
- https://awesomeclaude.ai/awesome-claude-skills (directory)
- https://claudeskills.info/skills/ (directory + /api/v1/search)
- https://skillmd.com/ (registry + /v1/search API)
- https://api.github.com/repos/github/awesome-copilot (repo stats)
