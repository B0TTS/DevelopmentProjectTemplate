# Researcher A — Anthropic / Claude Code First-Party Ecosystem: Prompt-Writing & Prompt-Refinement Skills

**Date:** 2026-08-18
**Scope:** Official (first-party) Anthropic / Claude Code skills and platform capabilities whose purpose is prompt writing / prompt refinement — specifically the workflow: user activates skill → hands it an existing prompt → skill interviews user with questions → produces a polished ready-to-use prompt.

---

## Summary of findings (top of report)

**There is NO official Anthropic / Claude Code SKILL.md skill whose purpose is interactive prompt refinement** (i.e., take an existing prompt, interview the user with questions about scope/objectives/deliverables/constraints/edge cases, and output a polished prompt). This is the headline result.

What the official ecosystem DOES have:
1. **`anthropics/skills`** (official skills repo, ~170k stars, actively maintained) — 19 skills, **none** of which is a prompt-engineering / prompt-improvement / prompt-refinement / prompt-critique skill. Full top-level contents listed below.
2. **Anthropic Console "prompt improver"** — an official first-party *feature* (not a skill) that automatically refines existing prompts. It does **NOT** interview the user (NO interactive questioning).
3. **`anthropics/prompt-eng-interactive-tutorial`** — an official interactive *course* (Jupyter notebooks), educational, not a skill and not a prompt-refinement tool.
4. **Closest official skills** (partial matches, ranked): `skill-creator` (interviews user to build SKILL.md skills — prompt-adjacent), `doc-coauthoring` (structured Q&A workflow but for documents, not prompts), `discernment-nudge` (appends follow-up questions after the assistant's own answer — not prompt refinement).
5. **Prompt-engineering guidance docs** (platform.claude.com) — reference docs, not activatable skills.

**Bottom line for the caller's use case:** No first-party skill matches the "interactive prompt refinement via Q&A" workflow. The closest first-party *pattern* is `skill-creator`'s interview loop (but it outputs a SKILL.md, not a general prompt). Third-party skills exist (noted in gaps) but are out of this task's first-party scope.

---

## Official repo: `anthropics/skills` — full top-level contents

**Source (verified by reading GitHub API):** https://github.com/anthropics/skills
**Repo stats (GitHub API, read 2026-08-18):** 170,278 stars, 20,264 forks, created 2025-09-22, last pushed 2026-08-18 (active), license: none declared at repo root (skills individually licensed; doc skills source-available).

**Top-level contents:**
- `.claude-plugin/` (Claude Code plugin marketplace metadata)
- `.gitignore`
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `skills/` (the skill examples)
- `spec/` (the Agent Skills specification)
- `template/` (skill template)

**`skills/` directory — all 19 skills (verified via GitHub API):**
1. `academy-guide`
2. `algorithmic-art`
3. `brand-guidelines`
4. `canvas-design`
5. `claude-api`
6. `discernment-nudge`
7. `doc-coauthoring`
8. `docx`
9. `frontend-design`
10. `internal-comms`
11. `mcp-builder`
12. `pdf`
13. `pptx`
14. `skill-creator`
15. `slack-gif-creator`
16. `theme-factory`
17. `web-artifacts-builder`
18. `webapp-testing`
19. `xlsx`

**None of these is a prompt-engineering / prompt-improvement / prompt-refinement / prompt-critique skill.** The README confirms the repo is "demonstration and educational purposes only" and organizes skills into Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills.

**Install method (from README):**
```
/plugin marketplace add anthropics/skills
```
then browse/install the `document-skills` or `example-skills` plugin, or directly:
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

---

## Candidate 1 — `skill-creator` (official, closest interactive-Q&A pattern)

- **Name / URL:** `skill-creator` — https://github.com/anthropics/skills/tree/main/skills/skill-creator (SKILL.md: https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md)
- **Platform:** Claude Code / Claude.ai / Claude API (Agent Skills standard)
- **Install:** via the `anthropics/skills` marketplace (see above), or copy the folder into `.claude/skills/`.
- **Workflow (from SKILL.md headings):** Capture Intent → Interview and Research → Write the SKILL.md → (optional) run test cases / evals → improve → description optimization. The "Interview and Research" stage asks the user questions to gather requirements before writing the SKILL.md.
- **Interactive Q&A?** **YES** — it interviews the user (Capture Intent + Interview and Research stages) before producing output. This is the strongest first-party interactive-questioning pattern found.
- **Quality signals:** Official Anthropic skill, part of the 170k-star repo, actively maintained (repo pushed 2026-08-18). SKILL.md is comprehensive (multi-stage workflow, writing guide, test-case/evals section, description-optimization section).
- **Pros vs. use case:** Genuinely interactive; asks clarifying questions; produces a polished, structured artifact. The interview→refine→output loop is exactly the shape the caller wants.
- **Cons vs. use case:** It produces a **SKILL.md skill file**, not a general-purpose prompt for any agent/LLM. It's scoped to authoring Agent Skills (frontmatter, progressive disclosure, evals), so it's prompt-authoring-adjacent rather than a general prompt refiner. Overkill if the user just wants a one-off polished prompt.
- **Open questions:** Whether its interview questions (scope/objectives/deliverables/constraints/edge cases) map cleanly onto general prompt refinement is UNKNOWN without deeper reading; it's designed for skill authoring.

---

## Candidate 2 — `doc-coauthoring` (official, structured Q&A workflow, but for docs)

- **Name / URL:** `doc-coauthoring` — https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring (SKILL.md: https://raw.githubusercontent.com/anthropics/skills/main/skills/doc-coauthoring/SKILL.md)
- **Platform:** Claude Code / Claude.ai / Claude API
- **Install:** via `anthropics/skills` marketplace, or copy folder into `.claude/skills/`.
- **Workflow (from SKILL.md headings):** Stage 1 Context Gathering (Initial Questions, Info Dumping) → Stage 2 Refinement & Structure (Clarifying Questions, Brainstorming, Curation, Gap Check, Drafting, Iterative Refinement) → Stage 3 Reader Testing → Final Review.
- **Interactive Q&A?** **YES** — it explicitly asks "Initial Questions" and "Clarifying Questions" and runs a gap check. Strong interactive pattern.
- **Quality signals:** Official Anthropic skill, actively maintained repo.
- **Pros vs. use case:** The interview→refine→iterate loop with clarifying questions and gap-checking is structurally very close to what the caller wants.
- **Cons vs. use case:** It targets **co-authoring documents** (docs, guides), not refining an existing prompt. Output is a document, not a prompt. Would need adaptation.
- **Open questions:** Whether it accepts a pre-existing draft as input and refines it (vs. building from scratch) is UNKNOWN from headings alone.

---

## Candidate 3 — `discernment-nudge` (official, but NOT prompt refinement)

- **Name / URL:** `discernment-nudge` — https://github.com/anthropics/skills/tree/main/skills/discernment-nudge (SKILL.md: https://raw.githubusercontent.com/anthropics/skills/main/skills/discernment-nudge/SKILL.md)
- **Platform:** Claude Code / Claude.ai / Claude API
- **Install:** via `anthropics/skills` marketplace, or copy folder into `.claude/skills/`.
- **Workflow (from SKILL.md, read in full):** After the assistant gives a substantive answer, append 2–3 short follow-up questions tied to specifics in that answer, helping the user check facts, probe reasoning, and notice missing context. At most once per conversation.
- **Interactive Q&A?** **PARTIAL** — it generates follow-up questions, but they are appended *after* the assistant's own answer to prompt the *user* to reflect; it does not interview the user to refine a prompt.
- **Quality signals:** Official Anthropic skill, actively maintained.
- **Pros vs. use case:** Demonstrates Anthropic's official pattern for generating targeted clarifying questions (fact-checking, reasoning-probing, missing-context) — a useful ingredient for a prompt-refinement skill.
- **Cons vs. use case:** Wrong direction — it critiques the assistant's answer, not the user's prompt. Not a prompt refiner.
- **Open questions:** None material.

---

## Candidate 4 — Anthropic Console "prompt improver" (official feature, NOT a skill, NO Q&A)

- **Name / URL:** "Improve your prompts in the developer console" — https://claude.com/blog/prompt-improver (announced 2024-10-14)
- **Platform:** Anthropic Console (developer console), not Claude Code / not a SKILL.md skill.
- **Install:** N/A — built into the Anthropic Console (console.anthropic.com).
- **Workflow (from blog, read):** Developer pastes an existing prompt; Claude automatically refines it via: (1) chain-of-thought reasoning section, (2) example standardization to XML, (3) example enrichment with CoT, (4) rewriting for clarity/grammar, (5) prefill addition to enforce output format. User can then give feedback on what works/doesn't.
- **Interactive Q&A?** **NO** — automatic refinement; it does not interview the user with questions.
- **Quality signals:** Official Anthropic product feature; first-party; documented in official blog.
- **Pros vs. use case:** It is the only official first-party capability that takes an *existing prompt* and produces a *refined prompt*. Directly on-target for "refine a prompt I already have."
- **Cons vs. use case:** No interactive questioning (the #1 criterion); it's a console UI feature, not an activatable skill; not portable to other agents/LLMs; output is shown in the console (clipboard/save behavior UNKNOWN).
- **Open questions:** Whether the console improver is still available/current in 2026, and its exact output-delivery (copy/save) — UNKNOWN.

---

## Candidate 5 — `anthropics/prompt-eng-interactive-tutorial` (official course, NOT a skill)

- **Name / URL:** `anthropics/prompt-eng-interactive-tutorial` — https://github.com/anthropics/prompt-eng-interactive-tutorial
- **Platform:** Jupyter notebooks (Anthropic 1P folder) + Google Sheets version; educational, not a Claude Code skill.
- **Install:** Clone the repo; run notebooks; or use the Google Sheets version.
- **Workflow (from README, read):** 9 chapters + appendix (Basic Prompt Structure → Being Clear and Direct → Assigning Roles → Separating Data from Instructions → Formatting Output → Precognition/CoT → Using Examples → Avoiding Hallucinations → Building Complex Prompts), each with exercises and an "Example Playground." Teaches how to build prompts from scratch.
- **Interactive Q&A?** **PARTIAL** — it's an interactive *course* with exercises, but it does not take the user's existing prompt and interview them to refine it.
- **Quality signals:** Official Anthropic repo; well-structured course.
- **Pros vs. use case:** Official, high-quality prompt-engineering methodology that a prompt-refinement skill could encode.
- **Cons vs. use case:** It's a learning course, not an activatable skill; no "refine my prompt" workflow; no Q&A interview of the user's specific prompt.
- **Open questions:** None material.

---

## Candidate 6 — Official prompt-engineering guidance docs (reference, not skills)

- **Name / URL:** Prompt engineering overview — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview ; Prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Platform:** Anthropic platform docs (reference).
- **Install:** N/A.
- **Workflow:** Reference guidance (clarity, examples, XML structuring, thinking, agentic systems). Not an activatable skill; no Q&A.
- **Interactive Q&A?** **NO.**
- **Quality signals:** Official, authoritative, current.
- **Pros vs. use case:** Canonical source of the techniques a prompt-refinement skill should apply.
- **Cons vs. use case:** Not a skill; no interactive refinement.
- **Open questions:** None.

---

## Open questions / gaps

1. **No first-party interactive prompt-refinement skill exists.** The caller's exact workflow (activate skill → hand it an existing prompt → skill interviews user → outputs polished prompt) has **no official Anthropic/Claude Code implementation**. This is the central gap.
2. **Output delivery is unspecified everywhere:** For the console prompt improver, whether the refined prompt is copied to clipboard, saved to file, or only shown in the console is UNKNOWN. No official skill defines this.
3. **`skill-creator` and `doc-coauthoring` are the closest interactive patterns** but target SKILL.md authoring and document co-authoring respectively — neither refines a general-purpose prompt. Whether their interview question sets (scope/objectives/deliverables/constraints/edge cases) transfer to prompt refinement is UNKNOWN without deeper reading of their full bodies.
4. **Third-party (out of first-party scope, noted for the caller's broader goal):** Several non-official Claude Code skills match the use case and would be worth a follow-up researcher: `christabone/claude-prompt-improvement` (https://github.com/christabone/claude-prompt-improvement), `severity1/claude-code-prompt-improver` (https://github.com/severity1/claude-code-prompt-improver — asks 1–6 grounded questions), `refine-prompts` (https://skills.rest/skill/refine-prompts), and mcpmarket's `refine-prompt` (https://mcpmarket.com/tools/skills/refine-prompt). These were NOT verified in depth (out of scope) and their interactive-Q&A behavior is UNKNOWN here.
5. **Freshness caveat:** The Anthropic Console prompt improver was announced 2024-10-14; its current availability in 2026 is UNKNOWN. The `anthropics/skills` repo is actively maintained (pushed 2026-08-18), so its skill list is current as of that date.
