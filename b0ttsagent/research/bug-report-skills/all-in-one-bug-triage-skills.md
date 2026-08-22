# All-in-One Bug Triage Skills — Research Findings

**Date:** 2026-08-19
**Researcher:** b0tts-researcher leaf agent
**Mission:** Find open-source agent "skills" (SKILL.md or equivalent) that perform an ALL-IN-ONE bug triage flow end-to-end:
1. Q&A session between developer and agent to reach shared understanding of a bug,
2. Agent writes the bug down as a structured bug report document (or appends to an existing one),
3. Agent investigates the codebase to hypothesize root cause,
4. Agent writes the suspected cause into that same bug document.

**Target flow shorthand:** Q&A → write bug doc → investigate codebase → write cause into doc.

---

## What was searched

**Query angles (SearXNG first, then Exa `websearch` fallback):**
- `bug report skill agent SKILL.md claude code`
- `bug triage agent skill github open source`
- `agentskills.io bug report skill`
- `bug report skill` (simple probe)
- `bug triage agent skill github "SKILL.md"`
- `awesome-claude-code-skills bug report root cause skill`
- `agentskills.io bug report skill registry`
- `obra superpowers systematic-debugging skill SKILL.md`
- `wshobson agents awesome-claude-code-skills bug fixer skill`

**Platforms / registries used:**
- SearXNG MCP (`searxng_searxng_web_search`) — instance reachable but returned **zero results for every query** (engine-side failure), so all discovery fell through to Exa `websearch`.
- Exa `websearch` (opencode built-in) — primary discovery tool; returned rich GitHub + registry results.
- skills.sh registry API (`https://skills.sh/api/search?q=...`) — searched `bug`, `triage`, `bug report`. This was the single most productive source (install counts, repo links).
- skills.sh skill pages (`https://www.skills.sh/<org>/<repo>/<skill>`) — read SKILL.md content (truncated for long skills).
- GitHub raw file reads + GitHub REST API (`api.github.com`) for repo metadata, license, and file paths.
- GitHub web code search — attempted but requires sign-in; not usable.

**Dead ends / anomalies:**
- SearXNG returned no results on any query despite instance being reachable — noted, not a content finding.
- `mattpocock/skills` raw paths at repo root 404'd; actual skill paths live under `skills/engineering/` (found via `plugin.json`).
- GitHub code search UI requires login — used REST API + raw files instead.

---

## Candidate skills found

Coverage legend for the 4-step flow: **Q&A** (step 1), **BugDoc** (step 2 — writes/updates a bug report doc), **Investigate** (step 3 — codebase investigation), **Cause→Doc** (step 4 — writes suspected cause into the same doc). ✅ = explicitly in the skill; ◐ = partial/indirect; ❌ = absent; ? = not verified (page not fully read).

### 1. `bug-triaging` — 0xHoneyJar/loa-freeside
- **URL:** https://github.com/0xhoneyjar/loa-freeside/blob/main/.claude/skills/bug-triaging/SKILL.md
- **Harness/format:** Claude Code skill (`.claude/skills/bug-triaging/SKILL.md`), custom frontmatter (zones, capabilities, cost-profile).
- **Description:** "Triage a reported bug through structured phases: validate eligibility, gather details, analyze codebase, and produce a handoff contract for `/implement`."
- **4-step coverage:** Q&A ✅ (Phase 2 "Hybrid Interview" — gap-detection algorithm asks max 3–5 targeted questions for missing fields: repro steps, expected/actual behavior, severity); BugDoc ✅ (Phase 4 writes `triage.md` from template, filling placeholders from Phases 1–3); Investigate ✅ (Phase 3 "Codebase Analysis" — stack-trace parsing, keyword grep, dependency mapping, test discovery, suspected-files list with confidence); Cause→Doc ✅ (Phase 4 fills `triage.md` with Phase 1–3 results including suspected files / fix strategy / fix hints).
- **License:** AGPL-3.0 (verified via GitHub license API).
- **Stars/activity:** 8 stars, 0 forks (GitHub page). Small/niche repo ("Platform layer of the Loa protocol"). Last-updated not captured.
- **Notes:** Closest structural match to the exact 4-step flow found. Heavily coupled to the repo's own "Loa" workflow (ledger, beads, micro-sprints) — not portable as-is.

### 2. `triage` — withastro/astro
- **URL:** https://github.com/withastro/astro/blob/main/.agents/skills/triage/SKILL.md (sub-docs: `reproduce.md`, `diagnose.md`, `verify.md`, `fix.md`)
- **Harness/format:** OpenCode/agentskills-style skill (`.agents/skills/triage/`), standard SKILL.md + sub-doc progressive disclosure.
- **Description:** "Triage a bug report end-to-end: reproduce the bug, diagnose the root cause, verify whether the behavior is intentional, and attempt a fix."
- **4-step coverage:** Q&A ❌ (input is `issueTitle`/`issueBody` args or `gh issue view` — no interview); BugDoc ✅ (reproduce step writes `report.md`; diagnose step **must** read and append to `report.md`); Investigate ✅ (reproduce + diagnose: locate source files, instrumentation, root-cause identification); Cause→Doc ✅ (diagnose.md: "Append your diagnosis findings to the existing `report.md`" — root cause, affected files w/ line numbers, suggested fix, confidence).
- **License:** MIT (Astro repo; standard, widely known — not re-verified this session).
- **Stars/activity:** 61.9k stars, 3.7k forks (GitHub page). High-profile, actively maintained.
- **Notes:** Covers steps 2–4 cleanly and writes cause into the same doc. Missing step 1 (Q&A) — assumes the bug report already exists.

### 3. `diagnosing-bugs` — mattpocock/skills
- **URL:** https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md
- **Harness/format:** Claude Code plugin skill (`.claude-plugin` marketplace; path `skills/engineering/diagnosing-bugs/SKILL.md`), standard SKILL.md.
- **Description:** "Diagnosis loop for hard bugs and performance regressions. Use when the user says 'diagnose'/'debug this', or reports something broken/throwing/failing/slow."
- **4-step coverage:** Q&A ◐ (Phase 3 shows ranked hypotheses to the user for re-ranking; asks user for artifacts/access when no repro loop can be built — but no structured bug-gathering interview); BugDoc ❌ (no bug report document written); Investigate ✅ (Phases 1–4: build feedback loop, reproduce+minimise, hypothesise, instrument); Cause→Doc ◐ (Phase 6: "The hypothesis that turned out correct is stated in the commit / PR message" — writes cause into commit/PR, not a bug doc).
- **License:** MIT (plugin.json `"license": "MIT"`).
- **Stars/activity:** 427.7k installs on skills.sh; repo 223.6k stars (skills.sh page). Very popular.
- **Notes:** Best-in-class debugging discipline; deliberately does NOT produce a bug-report artifact.

### 4. `triage` (a.k.a. github-triage) — mattpocock/skills
- **URL:** https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md (also surfaced as `github-triage/SKILL.md`)
- **Harness/format:** Claude Code plugin skill, standard SKILL.md.
- **Description:** "Triage GitHub issues through a label-based state machine... review incoming bugs or feature requests, prepare issues for an AFK agent."
- **4-step coverage:** Q&A ◐ (Step 4 runs a `/domain-model` interview session to flesh out underspecified issues); BugDoc ◐ (posts triage-notes / agent-brief comments on the GitHub issue rather than a local doc); Investigate ✅ (Step 3 "Bug reproduction" — explores codebase, traces code paths, attempts repro); Cause→Doc ◐ (findings go into GitHub comments, not a persistent bug doc).
- **License:** MIT (same repo as #3).
- **Stars/activity:** 622.1k installs on skills.sh (highest of any triage skill found).
- **Notes:** Strong on maintainer-facing GitHub triage; the interview + reproduction pieces are close to the target flow but output is GitHub comments/labels.

### 5. `systematic-debugging` — obra/superpowers
- **URL:** https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md (installable via `npx skills add`).
- **Description:** "Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes." Four-phase root-cause discipline (Investigate → Pattern Analysis → Hypothesis → Implementation).
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ✅ (Phase 1 root-cause investigation: read errors, reproduce, check recent changes, trace data flow); Cause→Doc ❌ (no doc artifact; cause lives in the fix).
- **License:** MIT (verified via GitHub license API, © Jesse Vincent 2025).
- **Stars/activity:** 230.2k installs on skills.sh; superpowers repo is a well-known collection.
- **Notes:** Methodology-only; no bug-report artifact at all.

### 6. `bug-hunter` — sickn33/agentic-awesome-skills
- **URL:** https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/bug-hunter/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md (community, `category: development`, `risk: safe`).
- **Description:** "Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevents regression."
- **4-step coverage:** Q&A ◐ (step 1 "Reproduce" asks for env/browser/actions/logs if it can't reproduce — light Q&A); BugDoc ◐ (has a "Documentation Template" — Symptom / Root Cause / Fix / Files Changed / Testing / Prevention — but it's written *after* fixing, not as a triage artifact); Investigate ✅ (reproduce → evidence → hypothesis → root cause); Cause→Doc ◐ (doc template includes Root Cause, but post-fix).
- **License:** not stated in frontmatter (community skill; license field absent — UNKNOWN).
- **Stars/activity:** listed on claudeskills.info; install count not captured.
- **Notes:** Decent all-rounder; the doc template is the closest thing to "writes cause into a bug doc" among the debugging-discipline skills, but ordering differs from the target flow.

### 7. `bugshot` — Sreelal727/bugshot-skill
- **URL:** https://github.com/Sreelal727/bugshot-skill
- **Harness/format:** Claude Code skill (`.claude/skills/bugshot/SKILL.md`) + MCP browser tools (Claude in Chrome).
- **Description:** "Vibe coding bug fixer — autonomous screenshot, console error capture, diagnosis & auto-fix."
- **4-step coverage:** Q&A ❌ (fully autonomous, "no forms, no tickets"); BugDoc ◐ ("GitHub Issue Mode — auto-file... full bug report + AI root cause analysis" via `gh`; also Report Mode HTML); Investigate ✅ (CAPTURE → DIAGNOSE: correlate errors to source, classify root cause); Cause→Doc ◐ (root cause goes into the auto-filed GitHub issue / HTML report, not a persistent local bug doc).
- **License:** not verified this session (UNKNOWN).
- **Stars/activity:** not captured.
- **Notes:** Browser/UI-bug specific; interesting because it *does* write a bug report containing root cause, but no Q&A and no local doc.

### 8. `github-bug-report-triage` — warpdotdev/oz-skills
- **URL:** https://github.com/warpdotdev/oz-skills/blob/main/.agents/skills/github-bug-report-triage/SKILL.md
- **Harness/format:** OpenCode skill (`.agents/skills/`), standard SKILL.md.
- **Description:** "Triage GitHub bug reports for actionability. Evaluate whether a bug issue has sufficient detail and identify missing information from the reporter."
- **4-step coverage:** Q&A ◐ (identifies missing info and gives constructive feedback to the reporter — but as a written response, not an interactive interview); BugDoc ❌; Investigate ❌; Cause→Doc ❌.
- **License:** MIT (frontmatter `license: MIT`).
- **Stars/activity:** 316 installs on skills.sh.
- **Notes:** Issue-quality evaluation only — no codebase work.

### 9. `sw-triage` — shopware/shopware
- **URL:** https://github.com/shopware/shopware/blob/trunk/.agents/skills/sw-triage/SKILL.md
- **Harness/format:** OpenCode/Claude Code skill (`.agents/skills/`), standard SKILL.md + shared policy file.
- **Description:** "Triage a Shopware 6 GitHub bug issue... identify the affected code area via rg/git/gh, check for related fixes or duplicates, then emit a Markdown summary with disposition, severity, labels, confidence, reasoning, evidence."
- **4-step coverage:** Q&A ❌; BugDoc ◐ (emits a Markdown triage summary as its single output — a report, but not a persistent bug doc); Investigate ✅ (rg/git/gh code-area identification); Cause→Doc ◐ (summary includes reasoning/evidence but is a one-shot message, not appended to a bug doc).
- **License:** MIT (frontmatter `license: MIT`).
- **Stars/activity:** Shopware monorepo (large, active); install count not captured.
- **Notes:** Repo-specific; strong investigation, no Q&A, no persistent doc.

### 10. `triage-bug` — spencerpauly/skills-repo
- **URL:** https://github.com/spencerpauly/skills-repo/blob/main/skills/triage-bug/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md.
- **Description:** "Take a raw bug report and turn it into a clean, prioritized ticket with a title, repro steps, and severity."
- **4-step coverage:** Q&A ❌; BugDoc ◐ (produces a structured ticket — title/severity/area/repro/expected-vs-actual — but from an existing report, no investigation); Investigate ❌; Cause→Doc ❌.
- **License:** MIT (frontmatter `license: MIT`).
- **Stars/activity:** not captured.
- **Notes:** Report-normalization only.

### 11. `triage-issues` — microsoft/fluentui
- **URL:** https://github.com/microsoft/fluentui/blob/master/.agents/skills/triage-issues/SKILL.md
- **Harness/format:** OpenCode skill (`.agents/skills/`).
- **Description:** "Triage newly-filed GitHub issues on the Fluent UI repo following the Shield triage guidelines... classify each (bug vs feature, product area, repro quality, a11y), recommend label changes and area-owner assignment."
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ◐ (validates repros via playwright-cli for flagged bugs); Cause→Doc ❌.
- **License:** Microsoft repo (MIT, standard — not re-verified this session).
- **Stars/activity:** Fluent UI monorepo (large, active).
- **Notes:** Maintainer label/assign workflow; no root-cause doc.

### 12. `github-triage-agent` — yu-iskw/github-project-skills
- **URL:** https://github.com/yu-iskw/github-project-skills/blob/main/agents/github-triage-agent/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md (agent-style).
- **Description:** "Expert triage agent... categorize, label, and assign new issues."
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ❌; Cause→Doc ❌. (Label/assign/comment only.)
- **License:** not verified (UNKNOWN).
- **Stars/activity:** not captured.

### 13. `github-project-triage` — steipete/agent-scripts
- **URL:** https://github.com/steipete/agent-scripts/blob/main/skills/github-project-triage/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md.
- **Description:** "GitHub issue/PR triage: queues, CI, blockers, risk, proof, next actions."
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ◐ (requires "identify root cause before recommending fix/merge" for bugs); Cause→Doc ❌.
- **License:** not verified (UNKNOWN).
- **Stars/activity:** not captured.

### 14. `find-bugs` — getsentry/skills
- **URL:** https://github.com/getsentry/skills/blob/main/skills/find-bugs/SKILL.md
- **Harness/format:** agentskills.io-standard SKILL.md.
- **Description:** "Find bugs, security vulnerabilities, and code quality issues in local branch changes."
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ◐ (diff/attack-surface review, not a reported-bug investigation); Cause→Doc ❌.
- **License:** not verified (UNKNOWN).
- **Stars/activity:** 5,088 installs on skills.sh.
- **Notes:** Code-review/security-audit skill; not a bug-triage flow.

### 15. `5-whys-skill` — awesome-skills/5-whys-skill
- **URL:** https://github.com/awesome-skills/5-whys-skill
- **Harness/format:** Claude Code skill.
- **Description:** "Systematic 5-Whys root cause analysis — trace problems to fundamental causes (Toyota Production System methodology)."
- **4-step coverage:** Q&A ◐ (iterative "why" questioning); BugDoc ❌; Investigate ◐ (methodology, not codebase tooling); Cause→Doc ❌.
- **License:** not verified (UNKNOWN).
- **Stars/activity:** not captured.

### 16. `debugging-strategies` — wshobson/agents
- **URL:** https://github.com/wshobson/agents (skill under `plugins/*/skills/debugging-strategies/`; docs: https://github.com/wshobson/agents/blob/main/docs/agent-skills.md)
- **Harness/format:** Multi-harness marketplace (Claude Code source-of-truth; emits Codex/Cursor/OpenCode/Antigravity/Copilot artifacts), agentskills.io-standard SKILL.md.
- **Description:** "Master systematic debugging techniques, profiling tools, and root cause analysis."
- **4-step coverage:** Q&A ❌; BugDoc ❌; Investigate ✅ (systematic debugging techniques); Cause→Doc ❌.
- **License:** not verified (UNKNOWN).
- **Stars/activity:** 11,276 installs on skills.sh; repo is a large multi-harness marketplace (181 skills).
- **Notes:** Methodology skill; no bug-doc artifact.

### 17. `reproduce-bug-report` — warpdotdev/common-skills
- **URL:** https://github.com/warpdotdev/common-skills (skill `skills/reproduce-bug-report/`)
- **Harness/format:** agentskills.io-standard SKILL.md.
- **Description:** "Use when the current context is a GitHub issue, support report, Linear ticket, or user prompt describing a specific bug... Launch one or more Oz cloud agents with computer use enabled so they can run the relevant app, interact with it, and capture visual evidence."
- **4-step coverage:** Q&A ❌; BugDoc ◐ (produces visual evidence / reproduction for the report); Investigate ◐ (reproduces via cloud agents, UI-focused); Cause→Doc ❌.
- **License:** not verified (UNKNOWN).
- **Stars/activity:** 20,053 installs on skills.sh; repo 163 stars.
- **Notes:** Reproduction-focused; UI-bug specific; no root-cause doc.

### 18. `ce-report-bug` — everyinc/compound-engineering-plugin
- **URL:** https://github.com/EveryInc/compound-engineering-plugin (skill path not resolved — 404 on guessed paths; repo structure not fully enumerated)
- **Harness/format:** Multi-harness plugin (`.claude`, `.codex-plugin`, `.cline`, `.agy` dirs present).
- **Description:** (from skills.sh) "report bug" skill — content NOT read (path unresolved).
- **4-step coverage:** ? (unverified — could not read the SKILL.md).
- **License:** not verified (UNKNOWN).
- **Stars/activity:** 1,748 installs on skills.sh.
- **Notes:** Listed for completeness; flagged as unverified.

---

## Closest matches

Ranked by coverage of the exact 4-step flow (Q&A → write bug doc → investigate → write cause into doc):

### #1 — `bug-triaging` (0xHoneyJar/loa-freeside)
The only skill found that implements all four steps in one flow: Phase 2 "Hybrid Interview" is a genuine Q&A gap-filling interview; Phase 3 is codebase analysis producing suspected files; Phase 4 writes `triage.md` (bug doc) filled with Phase 1–3 results including suspected cause/fix hints. Caveats: AGPL-3.0, 8 stars, tightly coupled to the repo's own Loa workflow (ledger, beads, micro-sprints) — a design reference more than a drop-in skill.

### #2 — `triage` (withastro/astro)
Cleanest production-grade implementation of steps 2–4: reproduce writes `report.md`, diagnose **must** append root cause (files, line numbers, suggested fix, confidence) to that same `report.md`. High-profile (61.9k stars), MIT, actively maintained. Missing step 1 (Q&A) — it consumes an existing issue body rather than interviewing the developer.

### #3 — `diagnosing-bugs` (mattpocock/skills)
Best-in-class debugging discipline (427k installs, MIT) covering step 3 deeply and step 1 partially (hypothesis re-ranking checkpoint with the user). But it deliberately produces no bug-report document — the cause is written into the commit/PR message, not a bug doc. If the target flow's step 2/4 (persistent bug doc) is optional, this is the strongest investigation engine.

**Honorable mentions:** `triage` (mattpocock, 622k installs — interview + reproduction, but GitHub-comment output); `bug-hunter` (sickn33 — debugging + a post-fix documentation template with root cause); `bugshot` (Sreelal727 — auto-files a GitHub issue containing root cause, but no Q&A).

---

## Gaps

What the 4-step flow needs that no existing skill fully provides:

1. **Q&A + persistent bug doc in one artifact.** Skills split into two camps: (a) debugging disciplines (superpowers, mattpocock diagnosing-bugs, bug-hunter) that investigate but write no bug doc, and (b) report/ticket writers (spencerpauly triage-bug, warpdotdev github-bug-report-triage) that write docs but don't investigate. Only loa-freeside bridges both, and it's non-portable. **No portable, harness-agnostic skill does Q&A → doc → investigate → append-cause end-to-end.**

2. **The bug doc as a living, append-only artifact.** Astro's `report.md` pattern (reproduce writes it, diagnose appends) is the right shape, but it's repo-internal and not packaged as a reusable skill. No standalone skill ships a bug-report template + "append your findings" contract that downstream steps (fix, verify, comment) read from.

3. **Structured Q&A that is optional/skippable.** loa-freeside's Hybrid Interview is the only real gap-filling interview found, but it's hard-wired to its own field schema. No skill offers a configurable interview (max-question budget, skip-if-report-is-complete) that works across harnesses.

4. **Cause-confidence + evidence tracking in the doc.** Astro records confidence (high/medium/low) and loa-freeside records suspicion confidence per file, but no single skill combines: suspected-files list → hypothesis → verified root cause → confidence → evidence trail, all in the same document.

5. **Harness portability.** The strongest matches are Claude-Code-specific (loa-freeside) or repo-specific (astro, shopware). No agentskills.io-standard, multi-harness skill implements the full 4-step flow.

6. **License/portability of the best match.** The only full-flow skill (loa-freeside) is AGPL-3.0 and entangled with a bespoke workflow — reusing it requires extraction/rewrite.

---

## Evidence notes

- Every material claim about a skill's behavior above was read from the skill's SKILL.md (raw file or skills.sh page) or its repo metadata — not from search snippets. Skills whose content could not be read are explicitly marked UNKNOWN/unverified (e.g., `ce-report-bug`).
- Install counts are from the skills.sh registry API (self-reported by the registry, not authoritative).
- Star counts are from GitHub pages/API at time of research.
- SearXNG was unreachable-for-results this session; all discovery used the Exa `websearch` fallback per the opencode-web-research skill routing.
