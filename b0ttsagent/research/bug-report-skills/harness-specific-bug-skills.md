# Harness-Specific Bug-Report / Bug-Triage Skills — Research Findings

Research date: 2026-08-19. Scope: publicly available, open-source bug-report / bug-triage / issue-reproduction skills and slash commands built FOR specific AI coding harnesses, with focus on interactive intake workflows (agent asks questions → shared understanding → structured bug write-up).

---

## What was searched

**Harnesses covered:** Anthropic Claude Code (skills, slash commands, plugins), OpenCode, Cursor (rules/skills/plugins/marketplace), GitHub Copilot agent skills, Gemini CLI, Cline, Zed, OpenHands (microagents/skills), Codex-ecosystem skill packs, plus GitHub issue bots (Sweep, Kiro, Sidekick) that do developer Q&A.

**Query angles used:** "claude code skill bug report", "bug triage claude code SKILL.md github", "claude code slash command bug report custom command", "opencode skill bug report slash command", "awesome-opencode-skills bug", "cursor rules bug triage skill pack", "agentskills.io bug report skill", "gemini cli skill bug triage", "github copilot agent skill bug awesome-copilot", "sweep kiro sidekick github issue bot asks developer questions", "openhands microagent bug triage", "aider cline roo zed bug report slash command", "claude code built-in /bug slash command".

**Platforms used:** SearXNG (self-hosted, primary) with fallback to opencode built-in `websearch` (Exa) — several SearXNG queries returned empty and were retried via fallback. GitHub API (`api.github.com`) used for repo/dir listings (anthropics/skills, EslamAbdelkader/cursor-bug-triage-plugin, neonwatty/qa-skills, addyosmani/agent-skills, OpenHands/extensions). Registries checked: skillsplayground.com, playbooks.com, skillsmp.com, agentskills.in, awesome-copilot.github.com, cursor.com/marketplace, remoteopenclaw.com, explainx.ai.

**Reading standard:** every candidate's SKILL.md or listing page was read (via `searxng_web_url_read`, `webfetch`, or full-text search capture) before being characterized. Claims below are marked [read] (page read directly), [captured] (full text captured via search engine render of the page), or [listing] (registry listing only).

---

## Per-harness findings

### Anthropic Claude Code

- **`bug-report` + `bug-triage` slash-command skills — Donchitos/Claude-Code-Game-Studios** [captured]
  - URL: https://github.com/Donchitos/Claude-Code-Game-Studios/blob/main/.claude/skills/bug-report/SKILL.md and .../bug-triage/SKILL.md
  - Format: user-invocable slash commands (`.claude/skills/*/SKILL.md`, `user-invocable: true`, `allowed-tools: Read, Glob, Grep, Write, Edit`).
  - Description: `/bug-report` has 4 modes — Description (draft structured bug report from a description), Analyze (scan a file for potential bugs), Verify (re-run repro steps against a fix), Close (mark verified-fixed with closure record). `/bug-triage` re-prioritizes the open bug backlog (severity vs priority), assigns to sprints, flags systemic trends, writes `production/qa/bug-triage-[date].md`.
  - Interactive Q&A: minimal — parses args; asks permission before writing/updating bug files ("May I update ...?"). No intake interview.
  - Writes/updates bug doc: YES — `production/qa/bugs/[BUG-ID].md` (report, verify verdict, closure record) and `production/qa/bug-triage-[date].md`.
  - Codebase investigation: YES (Grep/Glob to locate affected files; verify mode re-checks code paths).
  - Note: game-studio-specific workflow; strong doc lifecycle (file → verify → close).

- **`bug-triaging` skill — 0xhoneyjar/loa-freeside** [captured]
  - URL: https://github.com/0xhoneyjar/loa-freeside/blob/main/.claude/skills/bug-triaging/SKILL.md
  - Format: SKILL.md with zones/capabilities frontmatter (Claude Code agent-skill format).
  - Description: Triage a reported bug through structured phases: eligibility validation → **Hybrid Interview** (gap detection on reproduction_steps / expected / actual / severity; asks max 3–5 targeted follow-up questions; `/bug` with no args prompts interactively) → codebase analysis (test-runner detection, suspected files, fix hints) → micro-sprint creation + handoff contract for `/implement`.
  - Interactive Q&A: YES — explicit "Phase 2: Hybrid Interview" with gap-detection algorithm and question templates; interactive mode when invoked with no args.
  - Writes/updates bug doc: YES — `.run/bugs/{bug_id}/state.json`, `grimoires/loa/a2a/bug-{bug_id}/triage.md` + `sprint.md` (atomic writes, PII redaction).
  - Codebase investigation: YES (Phase 3).
  - Note: tied to the author's "loa" framework conventions, but the interview→triage-doc→handoff pattern is the closest to an interactive intake workflow found in the Claude Code ecosystem.

- **`issue-triage` skill — testdouble/han** [captured]
  - URL: https://github.com/testdouble/han/blob/main/han-research/skills/issue-triage/SKILL.md
  - Format: SKILL.md (Claude Code skill; part of the "han" skill suite).
  - Description: Triage a raw, vague issue/bug report into a structured document naming what is known, what is missing, and the recommended next step (e.g. "Clarify with reporter before proceeding" or `/investigate`). Classifies issue type, extracts known facts, lists missing info, assesses severity/reproducibility, identifies suspected areas.
  - Interactive Q&A: NO — it does not ask questions itself; it recommends clarifying with the reporter as a next step.
  - Writes/updates bug doc: YES — writes triage report to `~/.claude/triages/` (template-driven), serves as handoff doc.
  - Codebase investigation: minimal — reads CLAUDE.md / project-discovery.md only to sharpen "Suspected Areas"; explicitly does NOT trace code paths.

- **`bug` skill — shipshitdev/skills** [captured]
  - URL: https://github.com/shipshitdev/skills/blob/master/skills/bug/SKILL.md
  - Format: SKILL.md slash command (`/bug`), gh CLI based.
  - Description: Drafts a structured GitHub bug issue (summary, repro steps, expected vs actual, environment) from a rough description, previews it, requires explicit confirmation, then files via `gh issue create --type Bug` (fallback `bug` label). Never invents facts; marks unknowns.
  - Interactive Q&A: minimal — "Ask one concise follow-up only if the report is unusable"; otherwise draft-with-gaps + confirm gate.
  - Writes/updates bug doc: YES — creates a GitHub issue (not a local doc).
  - Codebase investigation: reads repo context for type/label detection only.

- **`github-bug-report-triage` skill — warpdotdev/oz-skills** [captured]
  - URL: https://github.com/warpdotdev/oz-skills/blob/main/.agents/skills/github-bug-report-triage/SKILL.md (also listed at https://claudeskills.info/skills/warpdotdev/oz-skills/github-bug-report-triage/)
  - Format: SKILL.md in `.agents/skills/` (cross-harness; installable into Claude Code via `npx skills add`).
  - Description: Evaluates GitHub bug issues for actionability against the repo's issue template (or bundled fallback template); determines "Ready" vs "Needs more info" and gives constructive feedback on what's missing.
  - Interactive Q&A: NO — evaluates and gives feedback; does not interview.
  - Writes/updates bug doc: NO (feedback only).
  - Codebase investigation: NO.

- **`triage-issue` skill — aden-hive/hive** [captured]
  - URL: https://github.com/aden-hive/hive/blob/main/.claude/skills/triage-issue/SKILL.md
  - Format: SKILL.md slash-command style.
  - Description: Analyzes a GitHub issue, verifies claims against the codebase, categorizes (valid bug / misunderstanding / duplicate / incomplete...), drafts a technical response, and — after user review via AskUserQuestion — posts and closes.
  - Interactive Q&A: confirmation-gated (AskUserQuestion: post-and-close / edit / skip); not an intake interview.
  - Writes/updates bug doc: writes GitHub comments/closes issues.
  - Codebase investigation: YES (Grep/Glob/Read to verify claims).

- **`bug-interview` skill — neonwatty/claude-skills (now neonwatty/qa-skills)** [captured, availability uncertain]
  - URL: https://playbooks.com/skills/neonwatty/claude-skills/bug-interview (page 404'd on direct fetch on 2026-08-19; repo renamed to neonwatty/qa-skills and the skill is no longer in `skills/` — full text captured from the playbooks.com listing dated 2026-01-25).
  - Format: SKILL.md.
  - Description: "Deeply interviews the user about a bug before investigating or fixing it" — 4–8 rounds of AskUserQuestion across reproduction, environment, timing/patterns, observed behavior, impact; then synthesizes and writes a detailed investigation/fix plan to `.claude/plans/bug-<bug-name>.md`.
  - Interactive Q&A: YES — the strongest pure-interview design found (question categories, stop conditions, "don't stop after 2–3 questions").
  - Writes/updates bug doc: YES — investigation/fix plan markdown.
  - Codebase investigation: light (plan includes "Affected Code" hypotheses; interview-first).
  - Caveat: current repo no longer ships it; treat as archived/removed.

- **Built-in `/bug` command (Claude Code itself)** [read]
  - URL: https://code.claude.com/docs/en/commands
  - Format: built-in slash command (not a skill).
  - Description: `/bug [report]` reports a bug or shares the conversation with Anthropic via a consent screen; on third-party providers writes a local archive under `~/.claude/feedback-bundles/`. Alias `/share`; previously `/feedback`.
  - Interactive Q&A: consent screen only. Writes: feedback bundle to Anthropic. Not an intake workflow — included for completeness.

- **Official anthropics/skills repo** [read — full `skills/` dir listing via GitHub API]
  - URL: https://github.com/anthropics/skills
  - Contains 18 skills (pdf, docx, xlsx, pptx, canvas-design, webapp-testing, mcp-builder, skill-creator, doc-coauthoring, frontend-design, internal-comms, slack-gif-creator, theme-factory, algorithmic-art, brand-guidelines, claude-api, academy-guide, discernment-nudge, web-artifacts-builder). **No bug-report or bug-triage skill.**

### OpenCode

- **`gh-issue-triage` skill — joelhooks/swarm-tools** [captured]
  - URL: https://github.com/joelhooks/swarm-tools/blob/main/.opencode/skill/gh-issue-triage/SKILL.md (also on agentskills.in marketplace: https://www.agentskills.in/marketplace/@joelhooks/gh-issue-triage)
  - Format: SKILL.md in `.opencode/skill/`.
  - Description: GitHub issue triage workflow "Analyze → Clarify → File → Tag → Implement → Credit". Decision matrix per issue type; for bugs missing repro it asks the reporter for steps ("Ask for repro steps, request context/versions — genuine questions, not interrogation") via GitHub comments; files a "cell" (hive), labels, implements, credits contributor.
  - Interactive Q&A: YES — CLARIFY step asks the reporter for missing repro/context (async, via issue comments).
  - Writes/updates bug doc: creates hive cells + GitHub labels/comments (not a local md doc).
  - Codebase investigation: partial (implement step).

- **`github-triage` skill — code-yeongyu/oh-my-opencode** [captured]
  - URL: https://github.com/code-yeongyu/oh-my-opencode/blob/dev/.opencode/skills/github-triage/SKILL.md (also listed on playbooks.com, explainx.ai, remoteopenclaw.com)
  - Format: SKILL.md in `.opencode/skills/`.
  - Description: Read-only triage orchestrator — fetches all open issues/PRs, classifies (ISSUE_BUG etc.), spawns one background subagent per item, each writes an evidence-backed report (`/tmp/{datetime}/issue-{N}.md`) where every claim needs a GitHub permalink; verdicts CONFIRMED_BUG / NOT_A_BUG / ALREADY_FIXED / UNCLEAR. Zero GitHub mutations.
  - Interactive Q&A: NO (fully automated analysis).
  - Writes/updates bug doc: YES — per-issue markdown reports + SUMMARY.md (in /tmp).
  - Codebase investigation: YES (grep/read/git log/blame to trace and find fixing commits).

- **OpenCode GitHub integration (built-in feature)** [listing]
  - URL: https://opencode.ai/docs/github/
  - "Triage issues: Ask OpenCode to look into an issue and explain it to you. Fix and implement..." — built-in GitHub app workflow, not a skill; no intake Q&A.

### Cursor

- **`bug-triage` skill + plugin — EslamAbdelkader/cursor-bug-triage-plugin** [read — full SKILL.md + repo]
  - URL: https://github.com/EslamAbdelkader/cursor-bug-triage-plugin
  - Format: Cursor plugin (`.cursor-plugin/`) wrapping a SKILL.md skill (`skills/bug-triage/SKILL.md`, 17.9 KB) + companion markdown files (jira-integration, feature-flows, test-accounts, device-detection, device-setup, login-flow, navigation-guide, recording-replay, triage-report) + Notion MCP.
  - Description: End-to-end autonomous triage of a bug report: gather context (Jira ticket via browser MCP, Notion docs, codebase grep), build a reproduction plan, pick a test account, reproduce on a real Android device via mobilecli, record a screen recording as evidence, produce a triage report (CONFIRMED / NOT REPRODUCED / BLOCKED / CONFIRMED-with-caveat), and write post-triage learnings to a memory file.
  - Interactive Q&A: minimal — "If you cannot determine a clear reproduction path, ask the user for clarification"; otherwise autonomous.
  - Writes/updates bug doc: YES — triage report per status templates (triage-report.md), plus appends to test-accounts.md and memory.md.
  - Codebase investigation: YES (Phase 1b Grep/Glob on navigation/screen code).
  - Note: SumUp/Global-Bank-specific; the most complete end-to-end triage skill found anywhere, but domain-locked and device-automation heavy.

- **`triage-issue` plugin — Atlassian (official, Cursor-verified)** [read]
  - URL: https://cursor.com/marketplace/skills/triage-issue (source: https://github.com/atlassian/atlassian-mcp-server)
  - Format: Cursor plugin with SKILL.md skills + Atlassian MCP.
  - Description: "Intelligently triage bug reports and error messages by searching for duplicates in Jira and offering to create new issues or add comments to existing ones."
  - Interactive Q&A: confirmation-gated ("offering to create") — not an intake interview.
  - Writes/updates bug doc: YES — Jira issues/comments.
  - Codebase investigation: NO (Jira-side search).

- **`issue-triage` skill — vig-os/scitadel** [read — skillsmp listing]
  - URL: https://skillsmp.com/creators/vig-os/scitadel/cursor-skills-issue-triage (repo: https://github.com/vig-os/scitadel)
  - Format: SKILL.md (Cursor skills format per listing).
  - Description: Triages open GitHub issues across priority, area, effort, SemVer impact, dependencies, release readiness; groups related issues into clusters; suggests milestone assignments; applies approved changes via gh CLI.
  - Interactive Q&A: approval gate only ("applies approved changes").
  - Writes/updates bug doc: applies labels/milestones via gh.
  - Codebase investigation: NO.

- **`triage-issue-reports` skill — cursor/plugins (Benny / pstack-automations)** [listing]
  - URL: https://skillsmp.com/creators/cursor/plugins/pstack-automations-benny-skills-triage-issue-reports (also ruleskill.com)
  - Format: SKILL.md in cursor/plugins repo.
  - Description: Triages Slack issue reports with one thread-only verdict, evidence review, cause-aware routing, tracker dedupe, fail-closed ticket creation. "Use only from the configured Benny triage automation."
  - Interactive Q&A: NO (automation). Writes: tracker tickets. Codebase: NO.

- **Cursor rules packs (general)** — e.g. https://github.com/spencerpauly/awesome-cursor-skills (curated list) and https://cursor-skills.vercel.app/ — no dedicated bug-report/bug-triage skill surfaced in these lists during searches. [listing]

### GitHub Copilot (agent skills)

- **`bug-reproduction-brief` skill — github/awesome-copilot** [read — full SKILL.md]
  - URL: https://awesome-copilot.github.com/skill/bug-reproduction-brief/ (source: https://github.com/github/awesome-copilot/blob/main/skills/bug-reproduction-brief/SKILL.md; adapted from MIT-licensed https://github.com/skyestrela/ai-agent-skill-preview)
  - Format: SKILL.md (install: `gh skills install github/awesome-copilot bug-reproduction-brief`).
  - Description: "Turn a vague, intermittent, or environment-specific bug report into a minimal evidence-backed reproduction before proposing a fix." Records observed failure, identifies environment, separates expected vs actual, reduces the reproduction to the smallest failing fixture, proves repeatability, and stops before repair. Outputs a structured Bug Reproduction Brief (target/commit, environment, expected, actual, minimal steps, fixture, reproduced yes/no/intermittent, evidence, unknowns, next hypothesis).
  - Interactive Q&A: NO — works from the report as given (labels second-hand descriptions unverified); does not interview the reporter.
  - Writes/updates bug doc: YES — produces the Brief as the deliverable (in-conversation; not a fixed file path).
  - Codebase investigation: YES (reduction requires running/isolating the failure).
  - Note: excellent evidence-discipline model; the "stop before repair" rule is a strong intake boundary.

- **`bug-receipt` skill — github/awesome-copilot** [read — full SKILL.md]
  - URL: https://awesome-copilot.github.com/skill/bug-receipt/ (source: https://github.com/github/awesome-copilot/blob/main/skills/bug-receipt/SKILL.md; originally https://github.com/lMysticl/bug-receipt, MIT)
  - Format: SKILL.md + assets (receipt template JSON, schema, validator script).
  - Description: Mandatory closeout receipt (BUG RECEIPT · VERIFIED | PARTIAL | BLOCKED) for every bug/incident closeout: Problem, Baseline, Root cause, Change, Proof, Gaps, Source. Establishes an evidence boundary before editing; requires concrete proof per surface (logic/UI/API/persistence/race); never invents results.
  - Interactive Q&A: NO.
  - Writes/updates bug doc: YES — receipt output (JSON artifact optional, validated by script).
  - Codebase investigation: YES (trace and repair phase).
  - Note: closeout-side, not intake-side — pairs naturally with an intake skill.

- **Awesome GitHub Copilot skills catalog** [read — index] — 410 skills; no other bug-report/bug-triage intake skill found in the index (only the two above plus generic "arch-linux-triage", "centos-linux-triage" OS-triage skills).

### Gemini CLI

- No dedicated bug-report/bug-triage skill surfaced in searches. Gemini CLI supports SKILL.md discovery in `~/.gemini/skills/` and `.agents/skills/` (verified via google-gemini/gemini-cli issues discussing skill loading, e.g. https://github.com/google-gemini/gemini-cli/issues/25693). The multi-harness repo addyosmani/agent-skills (https://github.com/addyosmani/agent-skills — ships `.agents/`, `.claude/`, `.codex/`, `.gemini/`, `.opencode/` variants) contains an `interview-me` skill and a `debugging-and-error-recovery` category but **no bug-report skill** [read — dir listing]. Verdict: harness supports the format; no notable public bug-intake skill found (UNKNOWN/negative result).

### Cline

- **`/reportbug` slash command — cline/cline** [read — docs + PRs]
  - URL: https://docs.cline.bot/core-workflows/using-commands (docs) and https://github.com/cline/cline/pull/3372 (original PR)
  - Format: built-in slash command (later removed).
  - Description: "Report a bug with diagnostic info" — gathered bug details conversationally ("It should ask you for details prior to attempting to use browser use") and opened a GitHub issue with a preview UI.
  - Interactive Q&A: YES — the PR description explicitly says the command asks the user for details before proceeding.
  - Writes/updates bug doc: created GitHub issues.
  - **Removed in April 2026** (PR https://github.com/cline/cline/pull/10211 "Remove /reportbug built-in slash command") — now points users to open GitHub issues manually. Notable case study: an interactive bug-intake slash command that shipped and was later deleted.

### Zed

- No bug-report skill found. Zed supports slash commands as reusable prompt templates (e.g. a "reproduce-bug" prompt example in https://qaskills.sh/blog/zed-ai-qa-engineers-guide) but has no native bug-intake workflow. [listing]

### OpenHands

- **Microagents / skills format** [read — OpenHands/extensions README + issues]
  - URL: https://github.com/OpenHands/extensions/tree/main/skills and https://github.com/OpenHands/OpenHands (microagents docs)
  - Format: `.openhands/microagents/` (V0: repo/knowledge/task agents) and `.agents/skills/` (V1 preferred) — SKILL.md-style markdown with frontmatter.
  - No dedicated bug-report/bug-triage skill in the official OpenHands/extensions catalog (verified via dir listing — closest are `linear-triage`, `incident-retrospective`, `jira-issue-to-pr`, `github-repo-monitor`). [read]
  - **`fix-bug` skill — rajshah4/openhands-petstore-demo** [captured] — repo-local `.agents/skills/fix-bug/`; GitHub issue tagged `oh:fix-bug` → OpenHands conversation → draft PR. Automation; no Q&A.
  - **`triage` skill — withastro/astro** [captured] — https://github.com/withastro/astro/blob/main/.agents/skills/triage/SKILL.md — real-world repo-level skill: "Triage a bug report end-to-end: reproduce, diagnose, verify whether behavior is intentional, attempt a fix" with subagents per step, working dir `triage/gh-<issue_number>`. No intake Q&A; strong repro→diagnose→verify→fix pipeline. Format is cross-harness (`.agents/skills/`).

### GitHub issue bots (developer Q&A angle)

- **Sweep** [read — docs + source] — https://github.com/sweepai/sweep — pure automation: issue must be "detailed enough for a junior engineer"; no clarifying-question loop before work (feedback happens via comments on the resulting PR). No intake Q&A.
- **Kiro** [read — docs] — https://kiro.dev/docs/web/using-the-agent/creating-tasks/ and https://kiro.dev/docs/web/github/ — hosted agent (kiro.dev; tracker repo kirodotdev/Kiro). GitHub integration: `kiro` label or `/kiro` comment assigns an issue; agent "listens to all comments for additional context"; task states include "Needs attention — the task needs input or the agent has a clarification question." Has a "Bug Fix" workflow that writes down current behavior, expected behavior, and unchanged behavior (https://dev.to/aws/7-kiro-features-youre-probably-not-using-2417). Interactive Q&A: YES — asks clarification questions in the issue thread. Writes: bug-fix brief/plan. Not open-source skill format (hosted product).
- **Sidekick** — no verifiable evidence of a developer Q&A intake flow found in searches; not characterized further (UNKNOWN).

### Other harnesses (Aider, Roo, Devin, Augment, SWE-agent, Codex)

- No bug-report/bug-triage skill or slash command surfaced for Aider, Roo, Devin, Augment, or SWE-agent in the searches run (these harnesses have no or minimal skill/slash-command culture). Codex-ecosystem: **jmerta/codex-skills `bug-triage`** [read — skillsplayground listing] — https://github.com/jmerta/codex-skills/tree/main/bug-triage — a 22-word prompt ("reproduce, isolate, and fix bugs... summarize root cause, fix, verification steps") installable into Claude Code, Cursor, Copilot, Windsurf, Cline etc. No Q&A, no doc writing — prompt-only.

---

## Closest matches (top 3)

1. **0xhoneyjar/loa-freeside `bug-triaging`** (Claude Code) — https://github.com/0xhoneyjar/loa-freeside/blob/main/.claude/skills/bug-triaging/SKILL.md
   The only skill found with an explicit, algorithm-driven **interactive intake interview** (gap detection → max 3–5 targeted questions → reproduction_strength rating) that then **writes a structured triage document + handoff contract** and does codebase analysis. Matches the "agent asks questions → shared understanding → structured bug write-up" target flow most completely. Caveat: coupled to the author's loa framework conventions (state dirs, micro-sprints), so it needs adaptation.

2. **EslamAbdelkader/cursor-bug-triage-plugin `bug-triage`** (Cursor) — https://github.com/EslamAbdelkader/cursor-bug-triage-plugin
   The most complete end-to-end triage pipeline found (context gathering → repro plan → device reproduction → evidence recording → statused triage report → learnings memory), with a full companion-file architecture and per-status report templates. Interactive Q&A is minimal (asks for clarification only when the repro path is unclear), and it is domain-locked to SumUp's Android app — but its phase structure and report templates are the best blueprint for a doc-producing triage skill.

3. **github/awesome-copilot `bug-reproduction-brief`** (GitHub Copilot / cross-harness) — https://awesome-copilot.github.com/skill/bug-reproduction-brief/
   Best evidence-discipline model for the intake side: turns a vague/intermittent report into a minimal verified reproduction with a fixed output brief (expected vs actual, minimal fixture, reproduced yes/no, unknowns, next hypothesis) and a hard "stop before repair" boundary. No interview, but the output contract is exactly the kind of structured bug document an intake skill should produce.

Honorable mention: **neonwatty `bug-interview`** (Claude Code) — the strongest pure interview design (4–8 rounds, question categories, stop conditions) but currently absent from the author's repo (renamed to qa-skills; skill no longer shipped) — treat as archived.

---

## Notable near-misses

- **Great Q&A, weak/no doc writing:**
  - neonwatty `bug-interview` — superb interview loop, writes only a plan file, and is currently unshipped.
  - Cline `/reportbug` — asked for details conversationally, but was removed in April 2026 (PR #10211).
  - Kiro (hosted) — asks clarification questions in GitHub issue threads and writes a bug-fix brief, but is a commercial product, not an open skill.
  - joelhooks `gh-issue-triage` — CLARIFY step asks the reporter for repro steps, but output is hive cells/labels rather than a bug document.
- **Great doc writing, no intake Q&A:**
  - Donchitos `bug-report`/`bug-triage` — full bug-file lifecycle (file → verify → close) + triage reports, but arg-parsed, no interview.
  - testdouble/han `issue-triage` — excellent structured triage document with "clarify with reporter" recommendation, but deliberately does not ask questions itself.
  - github/awesome-copilot `bug-receipt` — rigorous closeout receipt, but it's the end of the flow, not the intake.
  - withastro/astro `triage` — real-world repro→diagnose→verify→fix pipeline with per-step subagents, no interview.
- **Great codebase investigation, no Q&A/doc:**
  - code-yeongyu `github-triage` — evidence-permalink-required bug verdicts (CONFIRMED_BUG / ALREADY_FIXED), but fully automated and writes only to /tmp.
  - aden-hive `triage-issue` — verifies claims against code and drafts technical responses, but only confirmation-gated.
- **Pure automation (excluded by design):** Sweep, scitadel `issue-triage`, cursor/plugins `triage-issue-reports`, OpenHands `fix-bug` demo.

---

## Gaps / unknowns

- No open-source skill was found that combines (a) a real interactive intake interview, (b) a structured bug document written to a stable project path, and (c) codebase investigation — the three features are split across different projects. The closest single artifact is loa-freeside's `bug-triaging`.
- Gemini CLI, Zed, Aider, Roo, Devin, Augment, SWE-agent: negative/unknown results — searches surfaced no dedicated bug-intake skills; this is a genuine gap in those ecosystems, not a search failure (their skill formats were confirmed to exist where applicable).
- Sidekick (GitHub bot): no verifiable Q&A-intake evidence found.
- Several SearXNG queries returned empty and were retried via the Exa-backed fallback; results were consistent across engines where both ran.