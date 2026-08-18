# Researcher C — Cross-Platform / Other Ecosystems: Prompt-Writing & Prompt-Refinement Skills

**Date:** 2026-08-18
**Scope:** Activatable agent skills (SKILL.md-format or platform equivalents) whose entire purpose is prompt writing / prompt refinement via interactive questioning — opencode ecosystem, OpenAI Codex, other agent platforms, and standalone prompt-refinement workflows. Companion to researcher-a.md (Anthropic/Claude Code first-party) and researcher-b.md.

---

## Summary of findings (top of report)

**The exact workflow the caller wants (activate skill → hand it an existing prompt → skill interviews the user → outputs a polished ready-to-use prompt) EXISTS in the third-party ecosystem, in several well-maintained implementations.** Unlike the first-party Anthropic ecosystem (see researcher-a.md: no official skill matches), the community has built at least 5 skills that do interactive Q&A prompt refinement:

**Top candidates (interactive Q&A = YES):**
1. **`clarify` (owainlewis/agent-skills)** — interviews ONE question at a time, each with a recommended answer + one-line reason; emits a self-contained `Final prompt:` block. Closest structural match to the caller's use case. 42★, actively pushed (2026-08-15).
2. **`prompt-architect` (ckelsoe)** — 31 frameworks / 7 intent categories; scores the prompt 1–10 on 5 dimensions; asks 3–5 targeted questions at a time; iterative; outputs copy-paste-ready prompt in a fenced block. 277★, MIT, npm installer, works with Claude Code / Codex / Gemini CLI / Cursor / Copilot / ChatGPT / 30+ tools. Most complete and most portable.
3. **`prompt-improver` (ndpvt-web)** — uses `AskUserQuestion` "as many times as needed" to resolve doubts/assumptions, then applies an Aristotelian first-principles framework; "quick improve" mode skips questions. 85★, MIT, installs via `npx skills add`.
4. **`promptify` (ravnhq/ai-toolkit)** — AskUserQuestion with structured options for clarifying questions (only when major gaps) and for delivery choice (execute now / save to file). Repo is **archived** (health concern).
5. **`prompt-improver` (severity1/claude-code-prompt-improver)** — research-grounded 1–6 multiple-choice questions via AskUserQuestion, but then **executes the task** rather than outputting a prompt (partial match).

**Partial (limited questioning):** `prompt-optimizer` (affaan-m/ECC, up to 3 questions only if 3+ gaps), `prompt-refinement` (v1truv1us/ai-eng-system, at most ONE blocking question).

**Non-interactive prompt-refinement skills (ranked lower):** `prompt-refiner` (Notysoty/openagentskills), `prompt-improvement` (melodic-software — removed from repo, mirrored on LobeHub), `prompt-engineer` (Jeffallan/claude-skills 11k★ + opencode forks), `prompt-enhance` (owainlewis, explicitly one-shot), `improve-prompt` (christabone, edits in-place, no interview).

**Platform equivalents (not skills):** Anthropic Console prompt improver (NO Q&A — see researcher-a.md), Promptheus CLI/MCP tool (YES interactive Q&A), Prompt Perfect GPT (NO), OpenAI Codex internal `gpt-5-4-prompting` skill (internal, NO).

**Standalone workflows (not activatable skills, lower rank):** Martin Fowler's "Interrogatory LLM", the "Flipped Interaction" prompt pattern (White et al. catalog) + derived "Requirements Elicitation Facilitator" / "Question Refinement" patterns, "Interview Prompts" (Applied AI Society), Socratic-prompt templates.

**Ecosystem notes:** opencode has NO official skills registry (feature request open: anomalyco/opencode#8386); skills are installed by copying folders (`.opencode/skills/`, `.claude/skills/`, `.agents/skills/` — verified at opencode.ai/docs/skills). Community registries: skills.sh (Vercel), LobeHub, skillsmd.dev, opencodeskills.pages.dev, skillhub.club, skillregistry.io, agentskills.io. OpenAI's official `openai/skills` catalogue (verified via GitHub API) contains **no** prompt-refinement skill (only .system: imagegen, openai-docs, plugin-creator, skill-creator, skill-installer; .curated: dev/figma/notion/security/etc.).

---

## Candidate 1 — `clarify` (owainlewis/agent-skills)

- **Name / URL:** `clarify` — https://github.com/owainlewis/agent-skills (SKILL.md: https://raw.githubusercontent.com/owainlewis/agent-skills/main/skills/clarify/SKILL.md)
- **Platform:** Claude Code, Codex, Cursor, and other agents supported by the `skills` CLI (per repo README).
- **Install:** `npx skills@latest add owainlewis/agent-skills` (installs all skills; invoke via `/clarify` in Claude Code or the agent's skill picker).
- **Workflow (SKILL.md read in full):** 1) Read input + discoverable context (AGENTS.md, CLAUDE.md, README, file tree, code). 2) Optionally emit `Cleaned ask:`. 3) Ask ONE unresolved decision at a time. 4) Each question includes a recommended answer + one-line reason. 5) After each answer, re-check for new ambiguity. 6) Stop when a fresh agent could execute the prompt cold, or when the user says write it. 7) Emit one self-contained block under `Final prompt:` (goal, exact paths, inputs/outputs, dependencies, failure behavior, success criteria, out-of-scope; must "read cold" — no references to the conversation). "Just do it" mode: state assumptions once, bake them in, act.
- **Interactive Q&A?** **YES** — one question at a time, with recommendations; stops when ambiguity is gone.
- **Quality signals:** Repo 42★ / 7 forks (GitHub API, 2026-08-18), created 2025-10-18, pushed 2026-08-15 (active), no license declared. SKILL.md is compact (~90 lines) and precise. Companion skill `prompt-enhance` is the one-shot (non-interview) variant — the repo explicitly distinguishes them.
- **Pros vs. use case:** The closest structural match: interview → final prompt deliverable. Recommended-answer-per-question reduces user burden. Output contract (cold-read, self-contained) is exactly "polished, ready-to-use prompt for any agent."
- **Cons vs. use case:** Personal repo ("My personal agent skills") — no license, no tests, small adoption. No explicit scope/objective/deliverable/constraint question taxonomy (it's decision-driven, not checklist-driven). Output is printed in chat (no clipboard/file option defined).
- **Open questions:** Whether `npx skills` CLI installs work on opencode specifically — UNKNOWN (README lists Claude Code, Codex, Cursor "and others").

---

## Candidate 2 — `prompt-architect` (ckelsoe)

- **Name / URL:** `prompt-architect` — https://github.com/ckelsoe/prompt-architect (SKILL.md: https://raw.githubusercontent.com/ckelsoe/prompt-architect/main/skills/prompt-architect/SKILL.md; README read in full)
- **Platform:** Claude Code, ChatGPT (native Agent Skills upload), Gemini CLI, Cursor, GitHub Copilot, Windsurf, OpenAI Codex, and 30+ Agent Skills–compatible tools (per README; agentskills.io standard).
- **Install:** `npx @ckelsoe/prompt-architect` (interactive installer, detects agents); Claude Code: `/install-skill https://github.com/ckelsoe/prompt-architect/tree/main/skills/prompt-architect` or `/plugin marketplace add ckelsoe/prompt-architect`; Codex: `$skill-installer install <url>`; other agents: copy `skills/prompt-architect/` to `~/.agents/skills/prompt-architect/`; ChatGPT: upload release `.zip`; any LLM: paste `adapters/system-prompt.md`.
- **Workflow (SKILL.md read in full):** 1) Score prompt 1–10 on clarity/specificity/context/completeness/structure (show scores). 2) Select framework from 31 across 7 intents (CREATE/TRANSFORM/REASON/CRITIQUE/RECOVER/CLARIFY/AGENTIC) with discriminating questions. 3) Ask targeted clarifying questions (3–5 at a time, framework-specific question sets; Reverse Role Prompting = AI-led interview variant). 4) Apply framework via templates; never default facts about the user's world (emit `[you fill this in: …]` placeholders). 5) Present: analysis → usage instructions ("new chat: copy the prompt…") → revised prompt as the LAST element in a fenced code block, copy-paste verbatim. 6) Iterate on feedback.
- **Interactive Q&A?** **YES** — progressive 3–5-question batches, iterative refinement, plus a dedicated AI-led interview framework (FATA-based Reverse Role Prompting).
- **Quality signals:** 277★ / 32 forks (GitHub API 2026-08-18), MIT, created 2025-11-24, pushed 2026-07-24, v3.5.1, npm package `@ckelsoe/prompt-architect`, 0 open issues. Very complete: 30 framework reference docs + 30 templates + adapters. Research-cited frameworks (FATA arXiv 2508.08308, RPEF EMNLP 2025, etc.).
- **Pros vs. use case:** Most complete and most portable candidate; explicit question sets per framework cover scope/objectives/deliverables/constraints/edge cases; scoring gives before/after evidence; output contract (fenced block, nothing after) is purpose-built for copy-paste.
- **Cons vs. use case:** Heavier than needed for simple refinements (framework selection ceremony); questions are framework-driven rather than a free-form interview; no clipboard/file save (chat output only, though "execute now" is offered as usage instruction).
- **Open questions:** None material. (Note: repo description says "31 frameworks"; SKILL.md frontmatter description says "27" in one older mirror — current SKILL.md says 31.)

---

## Candidate 3 — `prompt-improver` (ndpvt-web)

- **Name / URL:** `prompt-improver` — https://github.com/ndpvt-web/prompt-improver (SKILL.md: https://raw.githubusercontent.com/ndpvt-web/prompt-improver/main/SKILL.md; also listed on skills.sh: https://www.skills.sh/ndpvt-web/prompt-improver/prompt-improver)
- **Platform:** Claude Code (uses `AskUserQuestion`); installable via the Vercel `skills` CLI for other agents.
- **Install:** `npx skills add https://github.com/ndpvt-web/prompt-improver --skill prompt-improver` (per skills.sh); or copy SKILL.md + references/ into `.claude/skills/prompt-improver/`.
- **Workflow (SKILL.md read in full):** 1) Gather context — "Use AskUserQuestion as many times as needed to resolve any doubts or assumptions". 2) Analyze — identify unclear/missing/ambiguous. 3) Improve — apply the Aristotelian first-principles framework (crafts a prompt that instructs the receiving LLM to reason from first principles: REASONING DIRECTIVE / GIVEN AXIOMS / TASK / METHOD / VERIFICATION sections). 4) Present — improved prompt with key changes explained. 5) Refine — ask if user wants adjustments. References: aristotelian.md, examples.md, anti-patterns.md, framework.md. A "quick improve" mode that skips questions is described in the repo's marketing copy (README/skills.sh snippet) — not in SKILL.md itself.
- **Interactive Q&A?** **YES** — unbounded AskUserQuestion loop until doubts are resolved.
- **Quality signals:** 85★ / 12 forks (GitHub API 2026-08-18), MIT, created 2026-03-10, pushed 2026-05-15. skills.sh: 16 installs, first seen 2026-05-04, security audits pass (Agent Trust Hub, Socket, Snyk).
- **Pros vs. use case:** Explicit "ask until no assumptions remain" behavior is the strongest interview guarantee found; output includes analysis + improved prompt; quick mode for impatient users.
- **Cons vs. use case:** The Aristotelian first-principles output style is opinionated (every improved prompt forces the receiving LLM into axiom-based reasoning — may not suit all target agents/LLMs); no structured question taxonomy; output printed in chat (no file/clipboard option).
- **Open questions:** "Quick improve" behavior is documented in repo marketing copy but not in SKILL.md — verify in README before relying on it.

---

## Candidate 4 — `promptify` (ravnhq/ai-toolkit)

- **Name / URL:** `promptify` — https://github.com/ravnhq/ai-toolkit (SKILL.md: https://raw.githubusercontent.com/ravnhq/ai-toolkit/main/skills/assistant/promptify/SKILL.md)
- **Platform:** Claude Code (allowed-tools: Bash, Read, Write, Edit, Grep, Glob, Agent, AskUserQuestion).
- **Install:** Copy `skills/assistant/promptify/` into the agent's skills directory (repo is a shared team toolkit; no one-line installer documented in SKILL.md).
- **Workflow (SKILL.md read in full):** 1) Analyze request (intent, missing context, unstated constraints, output format). 2) Decide mode: clear → rewrite directly; 1–2 minor gaps → `[Assumption: X]` placeholders; major gaps → clarifying questions via AskUserQuestion (structured options, never prose); multiple objectives → split. 3) Structure with four-block pattern (Context/Task/Constraints/Output Format). 4) Draft per rules (measurable requirements, success criteria, explicit assumptions). 5) Self-check against checklist (max 2 passes). 6) Output prompt as labeled markdown block. 7) AskUserQuestion delivery choice: Execute now / Save to file (`promptify-<epoch>.md`).
- **Interactive Q&A?** **YES** — but conditional: only when major gaps exist; otherwise proceeds with assumptions. Delivery choice is always interactive.
- **Quality signals:** Repo 16★ / 15 forks, created 2026-01-16, pushed 2026-06-10, **archived: true** (GitHub API 2026-08-18 — health concern), no license. SKILL.md is mature (version 10, status ready, positive/negative trigger lists, troubleshooting section).
- **Pros vs. use case:** The only candidate with an explicit **save-to-file** delivery option; structured-options questioning; assumption-marking discipline; trigger/anti-trigger design.
- **Cons vs. use case:** Repo archived (no further maintenance); org-internal toolkit; conditional questioning means it may skip the interview entirely for "clear enough" prompts.
- **Open questions:** Whether archived status affects availability of the skill content (content itself is still fetchable).

---

## Candidate 5 — `prompt-improver` (severity1/claude-code-prompt-improver)

- **Name / URL:** `prompt-improver` — https://github.com/severity1/claude-code-prompt-improver (SKILL.md: https://raw.githubusercontent.com/severity1/claude-code-prompt-improver/main/skills/prompt-improver/SKILL.md)
- **Platform:** Claude Code (plugin with UserPromptSubmit hook + AskUserQuestion + TodoWrite).
- **Install:** Claude Code plugin marketplace (`.claude-plugin/` present); or copy `skills/prompt-improver/` into `.claude/skills/`.
- **Workflow (SKILL.md read in full):** Auto-invoked by a hook when a prompt is judged vague. Phase 1 Research (conversation history → codebase → docs/web; questions must be grounded in findings). Phase 2 Generate 1–6 targeted multiple-choice questions (2–4 concrete options each, trade-off explanations; count scales with complexity). Phase 3 AskUserQuestion. Phase 4 **Execute the original request with the clarified context** (does NOT output a polished prompt as the deliverable).
- **Interactive Q&A?** **YES** — 1–6 research-grounded questions via AskUserQuestion.
- **Quality signals:** Repo has README (19.5KB), CHANGELOG (14.6KB), tests/, hooks/, nudges/, scripts/ — appears well-engineered; star count not fetched (UNKNOWN); last push UNKNOWN (not fetched).
- **Pros vs. use case:** Research-grounded questions (options come from actual codebase findings, not assumptions) — highest-quality question content found; bounded question count (1–6).
- **Cons vs. use case:** **Wrong output shape for the caller** — it enriches the prompt and then EXECUTES the task; it does not hand back a polished prompt. Auto-invocation via hook (not user-activated). Claude Code-specific (AskUserQuestion/TodoWrite).
- **Open questions:** Star count / freshness UNKNOWN (not fetched); whether a "prompt-only" mode exists — UNKNOWN from SKILL.md.

---

## Candidate 6 — `prompt-optimizer` (affaan-m/ECC, formerly everything-claude-code)

- **Name / URL:** `prompt-optimizer` — https://github.com/affaan-m/ECC (SKILL.md: https://raw.githubusercontent.com/affaan-m/ECC/main/skills/prompt-optimizer/SKILL.md; LobeHub mirror: https://lobehub.com/skills/affaan-m-everything-claude-code-prompt-optimizer)
- **Platform:** Claude Code / Codex / opencode / Cursor (ECC = "Everything Claude Code" harness; repo description lists all four).
- **Install:** Via ECC marketplace/CLI (LobeHub lists install via marketplace CLI; repo README not fetched).
- **Workflow (SKILL.md read in full):** Advisory-only (never executes the task). 6-phase pipeline: Phase 0 project detection (CLAUDE.md, tech stack) → Phase 1 intent detection (9 categories) → Phase 2 scope assessment → Phase 3 ECC component matching (commands/skills/agents per intent+stack) → Phase 4 missing-context detection (11-item checklist; **if 3+ items missing, ask the user up to 3 clarification questions**) → Phase 5 workflow & model recommendation. Output: 5 sections — Prompt Diagnosis (strengths/issues/needs-clarification), Recommended ECC Components, Optimized Prompt (full, fenced, self-contained), Optimized Prompt (quick version), Enhancement Rationale.
- **Interactive Q&A?** **PARTIAL** — conditional, capped at 3 questions, only when 3+ critical items are missing.
- **Quality signals:** Repo (ECC) reports 240,961★ / 36,544 forks via GitHub API (2026-08-18) — **anomalously high for a repo created 2026-01-18; treat star count as unreliable/inflated**. MIT, pushed 2026-08-18 (active). LobeHub: 208 installs, 4.7★ (6 reviews). SKILL.md is detailed (bilingual triggers, examples).
- **Pros vs. use case:** Advisory-only design (never drifts into execution); explicit missing-context checklist (scope, acceptance criteria, error handling, security, testing, performance, UI/UX, DB, patterns, boundaries); outputs a ready-to-paste prompt; multi-platform.
- **Cons vs. use case:** Questioning is minimal (≤3, conditional) — weaker interview than Candidates 1–3; output is heavily ECC-specific (recommends /plan, /tdd, tdd-workflow skill, Sonnet 5, etc.) — the optimized prompt is tuned for the ECC harness, not any agent/LLM.
- **Open questions:** Star count anomaly (240k in 7 months) — flagged, not resolved. Install method for opencode specifically UNKNOWN.

---

## Candidate 7 — `prompt-refinement` (v1truv1us/ai-eng-system)

- **Name / URL:** `prompt-refinement` — https://github.com/v1truv1us/ai-eng-system (SKILL.md: https://raw.githubusercontent.com/v1truv1us/ai-eng-system/main/skills/prompt-refinement/SKILL.md; also mirrored at playbooks.com/skills/v1truv1us/ai-eng-system/prompt-refinement)
- **Platform:** Claude Code (model-invoked by `/ai-eng/research|plan|work|specify` commands).
- **Install:** Copy `skills/prompt-refinement/` into `.claude/skills/` (part of the ai-eng-system command suite).
- **Workflow (SKILL.md read in full):** Convert request into TCRO (Task/Context/Requirements/Output) with phase-specific constraints; "Default output: return the refined prompt only. **Ask at most one blocking question**" — only when a missing answer changes architecture, security, compatibility, or irreversible behavior. Refinement rules: preserve user wording, infer reversible details from repo context, replace vague terms with measurable checks, remove duplicated context. Template: Task/Context/Requirements(+Non-goal)/Output/Verify.
- **Interactive Q&A?** **PARTIAL** — deliberately minimal (max 1 blocking question).
- **Quality signals:** Repo 8★ / 3 forks, MIT, created 2025-11-28, pushed 2026-08-16 (active). SKILL.md v2.0.0, compact.
- **Pros vs. use case:** Fast, low-friction; TCRO structure is a clean prompt skeleton; explicit non-goal field.
- **Cons vs. use case:** Almost no interview (opposite of the caller's Q&A-driven requirement); tied to the ai-eng-system command suite.
- **Open questions:** None material.

---

## Candidate 8 — `prompt-refiner` (Notysoty/openagentskills)

- **Name / URL:** `prompt-refiner` — https://github.com/Notysoty/openagentskills (SKILL.md: https://github.com/Notysoty/openagentskills/blob/main/skills/prompt-refiner/SKILL.md — read in full)
- **Platform:** Claude Code / Cline (copy to `.agents/skills/prompt-refiner/`), Cursor (`.cursorrules`), Codex (paste instructions).
- **Install:** Copy SKILL.md per platform instructions in the skill itself.
- **Workflow (SKILL.md read in full):** 1) Analyze original prompt for 9 weakness classes (vague task, no role, missing output format, missing context, ambiguous pronouns, conflicting instructions, no examples, no constraints, negative-only instructions). 2) Identify present weaknesses. 3) Rewrite applying best practices. 4) Explain every change in a "Changes Made" section (principle/before/after/why). 5) Optional variations. Output format: Original Prompt Analysis → Refined Prompt → Changes Made → Optional Variations.
- **Interactive Q&A?** **NO** — one-shot rewrite; the skill asks the user to include context up front ("Include what the prompt is for…") but does not interview.
- **Quality signals:** Repo 9★ / 1 fork (page read 2026-08-18). SKILL.md is well-written (174 lines, worked example, per-change rationale).
- **Pros vs. use case:** Excellent educational output (explains every change); multi-platform instructions built in; weakness taxonomy is a good checklist.
- **Cons vs. use case:** No questioning at all — fails the #1 criterion; no iteration loop.
- **Open questions:** None material.

---

## Candidate 9 — `prompt-improvement` (melodic-software/claude-code-plugins)

- **Name / URL:** `prompt-improvement` — https://lobehub.com/skills/melodic-software-claude-code-plugins-prompt-improvement (SKILL.md read in full via LobeHub mirror; canonical repo path `plugins/claude-ecosystem/skills/prompt-improvement/` **404s on GitHub as of 2026-08-18 — the skill has been removed from the repo**; mirrors: eliteai.tools/agent-skills/prompt-improvement, agentskills.to, aimcp.info, skillzwave.ai)
- **Platform:** Claude Code (plugin marketplace; companion agent `prompt-improver` + `/improve-prompt` slash command with `--feedback` and `--generate-examples` flags).
- **Install:** Via the melodic-software Claude Code plugin marketplace (repo `.claude-plugin/marketplace.json` — note: current marketplace.json no longer lists this plugin; install via LobeHub mirror or historical plugin versions).
- **Workflow (SKILL.md read in full):** Mandatory docs-management lookup first (query Anthropic docs for CoT/XML/multishot/Claude 4.x guidance; verification checkpoint). Then 4-step improvement: (1) identify examples, (2) initial draft with XML tags (`<instructions>/<context>/<examples>/<formatting>`), (3) chain-of-thought refinement (`<thinking>/<analysis>/<answer>`), (4) example enhancement. Decision trees, keyword registries, trade-off warnings (latency/cost), performance expectations (30% accuracy gain, 100% word-count adherence — labeled illustrative).
- **Interactive Q&A?** **NO** — a transformation workflow; no user interview (the `/improve-prompt` command takes input modes but doesn't interview).
- **Quality signals:** LobeHub: v1.0.2, 17 installs, last updated 2025-12-03. Repo (melodic-software/claude-code-plugins): 7★, created 2026-06-22, 62 open issues, pushed 2026-08-18 (active repo, but skill removed from it).
- **Pros vs. use case:** Replicates Anthropic's official prompt-improver methodology (CoT + XML + examples); docs-grounded (anti-hallucination); companion agent + slash command.
- **Cons vs. use case:** No questioning; **removed from its canonical repo** (availability risk — only mirrors remain); Claude-specific (Anthropic docs grounding, Claude 4.x focus).
- **Open questions:** Why it was removed from the repo (renamed? deprecated?) — UNKNOWN; whether mirrors stay current — UNKNOWN.

---

## Candidate 10 — `prompt-engineer` (Jeffallan/claude-skills + opencode forks)

- **Name / URL:** `prompt-engineer` — https://github.com/Jeffallan/claude-skills (SKILL.md: https://raw.githubusercontent.com/Jeffallan/claude-skills/main/skills/prompt-engineer/SKILL.md — read in full, v1.2.0). opencode forks: https://github.com/farmage/opencode-skills (118★, fork of Jeffallan/claude-skills, "66 specialized AI skills + 9 workflow commands for OpenCode") and https://github.com/synapse-ai-hub/opencode-skills (0★ fork, v1.1.0 of the same skill).
- **Platform:** Claude Code (original); opencode (forks, `compatibility: opencode` in frontmatter).
- **Install:** Copy `skills/prompt-engineer/` into `.claude/skills/` or `.opencode/skills/` (fork READMEs not fetched for a one-liner; standard copy-folder install).
- **Workflow (SKILL.md read in full):** Expert prompt-design skill: 1) Understand requirements (task, success criteria, constraints, edge cases) → 2) Design initial prompt (pattern choice) → 3) Test & evaluate (validation checkpoint <80% accuracy) → 4) Iterate & optimize (one change at a time) → 5) Document & deploy. Reference files for patterns/optimization/evaluation/structured outputs/system prompts (+context management in v1.2.0). Output templates: final prompt + test cases + usage instructions + metrics + limitations.
- **Interactive Q&A?** **NO** — no interview loop; "understand requirements" is a design step, not a Q&A protocol.
- **Quality signals:** Jeffallan/claude-skills: **11,062★** / 1,047 forks (GitHub API 2026-08-18), MIT, pushed 2026-08-07 (active). farmage/opencode-skills: 118★, pushed 2026-03-17. synapse-ai-hub fork: 0★.
- **Pros vs. use case:** Highest-adoption prompt skill found; the opencode forks are the only opencode-native prompt skills found; solid prompt-engineering methodology and reference library.
- **Cons vs. use case:** No interactive questioning (fails #1 criterion); oriented to designing/evaluating prompts for production LLM apps (test suites, metrics) rather than refining a user's existing prompt via Q&A.
- **Open questions:** None material.

---

## Candidate 11 — `prompt-enhance` (owainlewis/agent-skills)

- **Name / URL:** `prompt-enhance` — https://github.com/owainlewis/agent-skills (same repo as Candidate 1; README read)
- **Platform:** Claude Code / Codex / Cursor via `skills` CLI.
- **Install:** `npx skills@latest add owainlewis/agent-skills`.
- **Workflow (from README):** Takes a draft prompt or messy text and rewrites it into a refined, agent-ready prompt (explicit scope, no contradictions, output contract, success criteria). "One-shot: it improves the prompt, it doesn't interview you (that's `clarify`)."
- **Interactive Q&A?** **NO** — explicitly one-shot, by design.
- **Quality signals:** Same repo as Candidate 1 (42★, active).
- **Pros vs. use case:** Fast one-shot refinement when the user doesn't want an interview; pairs with `clarify` for the interview path.
- **Cons vs. use case:** No questioning.
- **Open questions:** SKILL.md content not fetched (README description only) — workflow details UNKNOWN beyond the README summary.

---

## Candidate 12 — `improve-prompt` (christabone/claude-prompt-improvement)

- **Name / URL:** `improve-prompt` — https://github.com/christabone/claude-prompt-improvement (SKILL.md: https://raw.githubusercontent.com/christabone/claude-prompt-improvement/main/skills/improve-prompt/SKILL.md — read in full)
- **Platform:** Claude Code (uses Edit tool, Python check scripts).
- **Install:** Copy `skills/improve-prompt/` into `.claude/skills/`.
- **Workflow (SKILL.md read in full):** Locate prompt in source file → run automated checks (xml_tags.py, variables.py) → apply 10-item judgment checklist with visible `<thinking>` reasoning → **edit the prompt in-place in the source file** → output a summary of changes (no separate file). Includes over-engineering warnings and task-decomposition guidance.
- **Interactive Q&A?** **NO** — no user interview; edits files directly.
- **Quality signals:** Repo structure verified (README 7KB, skills.md 15KB, data/, fetcher/, test/); star count UNKNOWN (not fetched).
- **Pros vs. use case:** In-place editing is useful for prompts embedded in code; visible reasoning; anti-over-engineering rules.
- **Cons vs. use case:** No questioning; modifies files rather than handing back a prompt (different workflow shape).
- **Open questions:** Star count / freshness UNKNOWN.

---

## Platform equivalents (not SKILL.md skills)

### Candidate 13 — Anthropic Console "prompt improver"
- **URL:** https://claude.com/blog/prompt-improver (headings read; full detail in researcher-a.md Candidate 4)
- **Platform:** Anthropic Console (web feature). **Interactive Q&A? NO** — automatic refinement (CoT section, XML examples, prefills). Not activatable, not portable. Lower rank.

### Candidate 14 — Promptheus (abhichandra21)
- **URL:** https://github.com/abhichandra21/Promptheus (README content read via search result; repo metadata via GitHub API: 17★, MIT, created 2025-11-06, pushed 2026-03-17)
- **Platform:** Standalone CLI + web UI + **MCP server** (works with Claude Code, Codex, Gemini, etc. via MCP clients).
- **Install:** `pip install` / clone (exact command UNKNOWN — README not fetched in full).
- **Workflow (from README content):** `refine_prompt` tool with adaptive questioning — returns `clarification_needed` with structured questions (options, multiSelect) for the client's AskUserQuestion, then `refined` prompt after answers; interactive mode auto-asks when AskUserQuestion is available; `-s` flag skips questions.
- **Interactive Q&A?** **YES** — structured Q&A refinement loop, MCP-native.
- **Pros vs. use case:** The only tool found that implements the exact interview→refined-prompt loop as a reusable MCP service; multi-provider.
- **Cons vs. use case:** Not a SKILL.md skill (requires running a Python service); small adoption (17★); last push 2026-03-17 (6 months stale).

### Candidate 15 — Prompt Perfect (ChatGPT GPT / extension)
- **URL:** https://promptperfect.xyz/gpt (and chatgpt.promptperfect.xyz)
- **Platform:** ChatGPT GPT + Chrome extension (also Gemini/Claude via extension).
- **Workflow:** Type "perfect" before your prompt; it rewrites for clarity/depth/precision; prompt library; rating feedback.
- **Interactive Q&A?** **NO** — automated rephrasing (per bestaitools.com summary; primary site not fetched in depth).
- **Quality signals:** Commercial product; UNKNOWN install counts.
- **Cons vs. use case:** No interview; closed platform; not a skill.

### Candidate 16 — OpenAI Codex internal `gpt-5-4-prompting` skill (openai/codex-plugin-cc)
- **URL:** https://github.com/openai/codex-plugin-cc (SKILL.md path `plugins/codex/skills/codex-cli-runtime/SKILL.md` mentions it: "You may use the gpt-5-4-prompting skill to rewrite the user's request into a tighter Codex prompt before the single task call.")
- **Platform:** Internal to OpenAI's Codex↔Claude plugin; not user-installable.
- **Interactive Q&A?** **NO** — internal prompt drafting.
- **Note:** OpenAI's public `openai/skills` catalogue (verified via GitHub API) has NO prompt-refinement skill. Community Codex skills exist (e.g., Notysoty prompt-refiner via paste, ckelsoe prompt-architect via `$skill-installer`), but no interactive Codex-native prompt-refinement skill was found.

---

## Standalone workflows (NOT activatable skills — lower rank, labeled as such)

1. **Interrogatory LLM (Martin Fowler)** — https://martinfowler.com/bliki/InterrogatoryLLM.html. The canonical writeup: prompt the LLM to interrogate the human (one question at a time — attributed to Harper Reed's blog) to build context, then produce a context report for another session. Technique, not a skill. Interactive: YES by design.
2. **Flipped Interaction pattern (White et al., prompt patterns catalog)** — https://www.dre.vanderbilt.edu/~schmidt/PDF/ADA-User-Journal.pdf. "I would like you to ask me questions to achieve X… ask me the questions one at a time." Derived patterns: **Requirements Elicitation Facilitator** (generate requirements via Q&A) and **Question Refinement** (suggest a better version of the user's question). The academic origin of the interview-first pattern.
3. **Interview Prompts (Applied AI Society)** — https://docs.appliedaisociety.org/docs/concepts/interview-prompts. Prompt-design pattern: name the variables, infer from context first (cwd, CLAUDE.md, git state, conversation), then interview one question at a time for gaps only; stopping condition + review gate. Includes a reusable template.
4. **Flipped Interaction Pattern: Agent Asks First (nosistech.com, 2026-05-27)** — https://nosistech.com/flipped-interaction-pattern-agentic-ai/. Reference implementation with MAX_QUESTIONS (default 7) and CONTEXT_THRESHOLD early-exit env vars; question-plan generation then one-at-a-time asking.
5. **Socratic prompt templates (Towards AI, 2026-01-01)** — https://towardsai.com/p/machine-learning/the-socratic-prompt-how-to-make-a-language-model-stop-guessing-and-start-thinking. "Interrogate first, answer later" 3-phase template (questions only → assumptions check → answer).
6. **Clarify-before-answer gate (NewPrompt guide, 2026-07-09)** — https://newprompt.net/guides/make-ai-ask-clarifying-questions-before-answering. Rules for when to ask vs. assume (cap 3–5 questions, require "why it matters" per question, assumptions-used section).

These confirm the interview-first pattern is well-established as a *technique*, but none is an activatable skill — they are templates/patterns the user would paste or implement.

---

## Near-misses (checked, not prompt-refinement skills)

- **`brainstorming` (obra/superpowers)** — https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md (read via search result). Interactive YES (one question at a time, multiple-choice preferred, approval gates), but it refines *ideas into design specs* before coding — output is a design doc, not a polished prompt; not for refining an existing prompt. Install: `/plugin marketplace add obra/superpowers-marketplace` + `/plugin install superpowers@superpowers-marketplace` (Claude Code), or `npx skills add obra/superpowers --skill brainstorming`.
- **`LLM Prompting` (opencodeskills.pages.dev, No. 074)** — https://opencodeskills.pages.dev/skills/ai-ml/llm-prompting/ — opencode skill teaching prompting techniques; educational, not a refiner. Install: `curl -LO …/downloads/ai-ml/llm-prompting.zip` → unzip to `~/.config/opencode/skills/`.
- **`Skill Optimizer` (opencodeskills.pages.dev, No. 015)** — https://opencodeskills.pages.dev/skills/workflow/skill-optimizer/ — mines/audits/generalizes SKILL.md files, not prompts.
- **`define-goal` (openai/skills .curated)** — goal definition for tasks, not prompt refinement (verified present in the official catalogue listing).
- **`skill-creator` / `doc-coauthoring` (anthropics/skills)** — interactive interview loops but output SKILL.md files / documents (see researcher-a.md).

---

## Ecosystem notes (verified)

- **opencode skills install:** copy a folder with `SKILL.md` into `.opencode/skills/<name>/`, `~/.config/opencode/skills/<name>/`, `.claude/skills/`, or `.agents/skills/` (project or global) — verified at https://opencode.ai/docs/skills/ (read in full; frontmatter rules: `name` + `description` required, name regex `^[a-z0-9]+(-[a-z0-9]+)*$`, description ≤1024 chars; permissions via `permission.skill`).
- **No official opencode registry:** feature request open — https://github.com/anomalyco/opencode/issues/8386 ("Skill Registry + Installer"). Community directories: opencodeskills.pages.dev (150+ skills), skillsmd.dev, skills.sh (Vercel), skillhub.club, skillregistry.io, lobehub.com/skills, agentskills.io (spec site).
- **OpenAI Codex:** official catalogue `openai/skills` (verified via GitHub API 2026-08-18) = `.system` (imagegen, openai-docs, plugin-creator, skill-creator, skill-installer) + `.curated` (dev/deploy/figma/notion/security/etc.) — **no prompt-refinement skill**. Codex installs community skills via `$skill-installer` (per codex.danielvaughan.com guide) or AGENTS.md.
- **ChatGPT:** natively supports Agent Skills on Business/Enterprise/Edu/Healthcare plans (per ckelsoe README) — so SKILL.md skills are uploadable there.

---

## Open questions / gaps

1. **Output delivery is chat-only in most candidates.** Only `promptify` (save-to-file option) and `prompt-architect` (usage instructions for new-chat paste) define delivery; clipboard behavior is UNKNOWN everywhere. If the caller needs clipboard/file output, this is a gap to design around.
2. **No candidate is opencode-native with interactive Q&A.** The opencode ecosystem's only prompt skills (`prompt-engineer` forks) are non-interactive. All interactive candidates target Claude Code (AskUserQuestion) or are agent-agnostic by convention. AskUserQuestion is a Claude Code tool — skills relying on it need adaptation for opencode (which has no AskUserQuestion; it would use plain chat questions).
3. **Star counts are a weak signal here** (small repos dominate the interactive category; the 11k★ repo is non-interactive; affaan-m/ECC's 240k★ is anomalous and treated as unreliable).
4. **Unverified leads** (from researcher-a.md, not fetched): `refine-prompts` (skills.rest/skill/refine-prompts), mcpmarket `refine-prompt` (mcpmarket.com/tools/skills/refine-prompt), `gpt-prompt-engineer` (ms-sambol — CLI that generates candidate prompts and asks the user to pick; interactive-ish, not a skill). Interactive behavior UNKNOWN.
5. **"Prompt interrogation" as a named standalone workflow** did not surface as a widely-used term (SearXNG returned zero results for quoted variants); the concept lives under "Flipped Interaction", "Interrogatory LLM", "interview prompts", and "Socratic prompting" instead.
6. **Freshness:** all GitHub API data read 2026-08-18. melodic-software's prompt-improvement skill was removed from its repo before this date; ravnhq/ai-toolkit is archived — both are availability risks.