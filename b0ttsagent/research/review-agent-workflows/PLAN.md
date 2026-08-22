# Research Plan: Review-Subagent Workflows

**Plan date:** 2026-08-21 · **Authored by:** Lead researcher (planner role) · **Status:** Contract for the review-agent research program
**Reader task:** execute (researchers run their angle; orchestrator runs synthesis) · **Lifespan:** working/reference for this program

This plan is the full contract for a multi-angle research program on **review agents**: subagents that independently review work produced in another context. It defines the angles, the per-angle questions, the workflow criteria, the sourcing rules, the synthesis rules, and the wave budget. The plan is self-contained: a researcher given only their own angle section (sections 1 and 2 for that angle), the shared criteria (section 3), and the sourcing rules (section 4) must be able to complete their entire job.

---

## Seed note (verbatim, the seed this plan grows from)

> "Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')"

## Why this program exists

A practitioner uses no review agents today. The seed note is their only rule — and they have never executed it. They want to know: how do people actually use review agents, which workflows are worth adopting, and what is the cheapest reliable first step?

The research must be **harness-agnostic** (patterns of agent use, not features of any specific agent product). It combines live web research (practitioner blog posts, papers, community discussions — preferred over vendor marketing) with first-principles reasoning grounded in the seed note. A finding only counts as a workflow if it is a repeatable pattern with a trigger, a procedure, and evidence (section 3). Every web-research claim carries its source; claims are downgraded to what the source supports (section 4). The orchestrator synthesizes a ranked list of workflows by adoptability for a review-agent beginner, ending with a "start here" section (section 5).

## Shared definitions (bind all researchers)

| Term | Definition |
|---|---|
| **Review agent / review subagent** | An agent instance spawned into its **own separate context** whose job is to critically examine work produced elsewhere (by another agent or a human) and return findings. Harness-agnostic: the same pattern appears across OpenCode, Claude Code, Cursor, Codex, Gemini CLI, AutoGen, CrewAI, LangGraph, and others. Product names may appear as examples — never as the pattern itself. |
| **Separate context** | The reviewer does not share the author's working context, memory, or scratch state. It sees only what it is given: the artifact, diff, spec, rubric, or files. The seed note's core move is "reviewer in a separate context." |
| **Self-review** | The author agent reviews its own output in its own context (e.g., an explicit "critique your own work" pass), with no separate-context reviewer. |
| **Workflow** | A repeatable pattern satisfying all three criteria in section 3: trigger, procedure, evidence. |
| **Sourced claim** | A claim traceable to a named source (URL + author/venue + date). |
| **Reasoning** | The researcher's own first-principles analysis. Always labeled as reasoning; never presented as sourced fact. |

---

## 1. Research angles (7 total)

Seven angles. Wave mapping and rationale in section 6. Each researcher receives exactly one angle. Angles a–f run in wave 1, g in wave 2.

### a. Code review agents
**Scope:** Subagents that review code, diffs, and PRs produced in another context: triggers, reviewer prompts and context inputs, authority (read-only vs. edit), triage of findings, and reported outcomes.
**Why included:** Mandated. The most mature and most documented angle; likely the largest pool of practitioner workflows and the most quantitative evidence. Its findings anchor the whole program's adoptability rankings.
**Likely source surfaces (leads, not findings — verify everything yourself):** Hacker News threads on AI code review; r/ChatGPTCoding, r/ClaudeAI, r/cursor; GitHub Discussions/issues of agent CLIs and frameworks (review commands, review subagents); engineering blog posts ("we added an AI reviewer to our PRs"); academic/industry studies comparing LLM reviewers to human code review.

### b. Writing and document review agents
**Scope:** Subagents reviewing prose, docs, reports, READMEs, changelogs, and other non-code artifacts produced elsewhere: triggers, reviewer prompts (audience, purpose, style guide), rubrics/checklists, and reported outcomes.
**Why included:** Mandated. The closest analog to the seed note's generality ("when creating something") and the most likely source of "start here" candidates for a practitioner who is not code-heavy.
**Likely source surfaces (leads, not findings):** Personal-essay blogs about agentic editing and draft review; newsletter and forum commentary; tooling blog posts about doc/report review workflows; writing-community threads on AI editors vs. human editors.

### c. Adversarial and red-team reviewers
**Scope:** Subagents that attack, jailbreak-check, fact-check, security-review, or hunt failure modes in another agent's output: triggers, threat-model inputs, severity/evidence rules, and reported outcomes.
**Why included:** Mandated. The strongest counterweight to reviewer rubber-stamping, and the angle most likely to surface the failure-mode evidence other angles miss (reviewers that share the author's blind spots).
**Likely source surfaces (leads, not findings):** Red-teaming write-ups and security engineering blogs; AI-safety evaluation posts; adversarial-prompting guides and community collections; papers on red-teaming and evaluation of LLM outputs.

### d. Self-review loops
**Scope:** The agent reviewing its own output vs. a separate-context reviewer: what literature and practice say about self-review failure modes, when self-review is or is not enough, and the "fresh eyes" question at the center of the seed note.
**Why included:** Mandated. This angle tests the seed note's central claim ("do not trust your own summary"). Its evidence determines whether the whole rule is worth its cost — and it runs in wave 1 alongside angle f so the synthesis can cross-check practice against literature.
**Likely source surfaces (leads, not findings):** Papers on self-correction and self-verification (e.g., Self-Refine, Reflexion, "LLMs cannot self-correct reasoning" line of work — verify existence and content yourself); practitioner threads asking "does asking the model to double-check itself actually work?"; agent-framework docs on self-critique vs. external critics.

### e. Practices borrowed from human review workflows
**Scope:** Checklists, two-person rule, desk checks, fresh-eyes effect, PR culture, editorial review — mapped onto review subagents: what transfers, what does not, and with what evidence.
**Why included:** Mandated. Human review has a research base (code review studies, checklist studies in aviation/medicine, writing research) that can support or undermine the analogous agent patterns — giving the synthesis an evidence tier it cannot get from practitioner anecdotes alone.
**Likely source surfaces (leads, not findings):** Human code-review research (modern code review literature); checklist literature (aviation, medicine); engineering blogs explicitly mapping "two-person rule" or "desk check" onto agents; essays on PR culture and review etiquette.

### f. Multi-agent debate and generator-verifier patterns *(added angle)*
**Justification:** The seed note's rule rests on a falsifiable claim — separate-context review beats same-context review. That claim has a quantitative literature (debate, generator-verifier, critique-revise, and self-refine/reflexion lines of work) plus framework implementations (critic agents, review tasks/nodes, two-model setups). No other angle can supply measured evidence of *whether* fresh-context review improves output quality, *by how much*, and *at what cost*. This angle calibrates every other angle's anecdotal claims and is where "when is separate review not worth it" gets its answer. Cutting it would leave the synthesis unable to rank adoptability beyond anecdotes.
**Scope:** Papers and framework patterns for verifier/debate/critique-revise loops; practitioner deployments of those patterns; evidence of quality gains and cost growth; verifier quality itself.
**Likely source surfaces (leads, not findings — verify each yourself):** Debate (Irving et al.), multiagent debate (Du et al.), Self-Refine (Madaan et al.), Reflexion (Shinn et al.), Constitutional AI critique-revise, process-reward/verifier-model literature; AutoGen critic agents, CrewAI review tasks, LangGraph reviewer nodes; practitioner posts on "two-model" setups.

### g. Review of research and planning artifacts *(added angle)*
**Justification:** A large share of real "spawn a reviewer" usage targets plans, specs, research reports, and analyses — work where tests do not exist and claims must be checked against sources. The pattern set differs materially from code and prose review (fact-checking subagents with source access, plan review before execution gates, review-of-reviews). This angle also directly informs this program's own pipeline, and its findings are prime "start here" candidates for knowledge workers. It runs in wave 2 so it can build on what a–f uncovered and so wave 2 keeps gap-closing headroom.
**Scope:** Review workflows for research outputs, plans, specs, and analyses; fact-checking/source-verification subagents; review-of-reviews (meta-review).
**Likely source surfaces (leads, not findings):** AI-research-assistant write-ups ("DeepResearch + critic" posts); planning-agent blog posts and spec/plan review workflows; fact-checking-agent posts; academic work on LLMs reviewing scientific papers; GSD-style tooling's plan-review steps.

---

## 2. Questions per angle

Rules for answering: every answer cites sources with tiers (section 4); every gap is reported honestly ("no sourced evidence found"); first-principles analysis is labeled **Reasoning**. Questions marked with a dagger (†) are the ones the orchestrator most needs answered with *some* sourced evidence — if you can only fully answer a subset, prioritize the daggered questions.

### 2a. Code review agents (8 questions)

1. What concrete review-subagent workflows for code do practitioners describe? Identify at least 3 distinct patterns; for each, state the trigger, the procedure, and the evidence given. †
2. What triggers do practitioners report for spawning a code reviewer (PR opened, branch marked done, before merge, on demand), and what context does the reviewer receive (full diff, spec, test output, repo files, checklist)?
3. What evidence do practitioners cite that review subagents caught issues the author agent missed? Report specifics (incidents, counts, before/after comparisons) and their tiers. †
4. What failure modes are reported: false positives, rubber-stamping, the reviewer adopting the author's assumptions, review noise, the reviewer editing code directly against the author's intent?
5. How is the reviewer's authority scoped in practice — read-only, propose-diff, fix-inline? What do practitioners report about each, and which do they recommend?
6. What token/cost/latency overhead do practitioners report, and which mitigations do they use (diff-only review, single-pass review, checklist-scoped review, review batching)?
7. Which review findings do practitioners act on vs. dismiss, and how do they decide (severity tags, evidence requirements, thresholds, owner judgment)? †
8. What is the minimum viable setup for a beginner (one subagent, what prompt, what permissions), and what barriers do practitioners report (config, cost, trust, prompt quality)? †

### 2b. Writing and document review agents (8 questions)

1. What distinct patterns do practitioners describe for reviewing prose, docs, and reports with a separate-context reviewer? For each: trigger, procedure, evidence. †
2. What triggers are used (draft complete, publish-ready, size/length thresholds, before sharing with a human), and what context does the reviewer get (artifact, audience, purpose, style guide, prior feedback)?
3. What evidence do practitioners report: editing time saved, before/after quality comparisons, caught factual errors or inconsistencies — with tiers? †
4. What failure modes are reported: generic praise, voice-erasing rewrites, hallucinated "improvements," over-compliance with style guides, review that misses the document's actual purpose?
5. How do practitioners compare agent review to human editing or peer review — what do their accounts claim is better and worse?
6. What role do rubrics, checklists, and style guides play — are rubric-driven doc reviews reported as more reliable, and with what evidence?
7. What are the reported costs and adoptability barriers for a beginner (prompt crafting effort, evaluating review quality, cost per document)? †
8. Do practitioners differentiate document types (technical docs vs. creative prose vs. reports)? Which types get review agents, and does the pattern differ? †

### 2c. Adversarial and red-team reviewers (8 questions)

1. What adversarial-review workflows do practitioners describe: jailbreak checks, fact-checking, security review, edge-case hunting, "break this" passes on another agent's output? For each: trigger, procedure, evidence. †
2. What triggers adversarial review (deployment, publication, a claim going public, CI), and what does the adversarial reviewer receive (artifact, threat model, definition of "failure")?
3. What evidence exists that adversarial reviewers catch real failures: incident reports, eval/benchmark results, red-team reports — with tiers and sources? †
4. What failure modes are reported: over-flagging (everything is a risk), adversarial drift into unhelpful negativity, the reviewer sharing the author's blind spots (both miss the same failure)?
5. How do practitioners keep adversarial reviews useful: severity classification, evidence-required rules, scoring rubrics, persona constraints? Which are reported to work? †
6. What is the reported setup complexity of adversarial review (multiple personas, iteration loops, scoring schemes) vs. a plain reviewer — and is the added complexity reported as worth it?
7. What evidence exists about reviewer calibration — how often are adversarial findings wrong, and do practitioners track this?
8. What is the minimal adversarial pattern a beginner could adopt (e.g., a single "find the three most likely ways this fails" pass), and what do practitioners report about its payoff? †

### 2d. Self-review loops (7 questions)

1. What does the literature say about self-review and self-correction failure modes — which studies (with citations) show self-correction failing vs. succeeding, and under what conditions? †
2. What do practitioners report about same-context self-review vs. separate-context review — do their accounts claim fresh context changes outcomes, and what evidence do they give? †
3. Which self-review variants are reported to work despite the failure modes (rubric-driven self-review, checklist self-verification, test-based verification), and with what evidence?
4. What is the reported evidence for a "fresh eyes" effect in LLMs — new context, different prompt, changed sampling — vs. same-context review? †
5. What do practitioners report on the cost tradeoff (tokens/time) of separate-context vs. self-review, and at what stakes do they switch?
6. When do practitioners deliberately rely on self-review anyway (low stakes, rapid iteration, cheap checks), and what guardrails do they use?
7. What is the evidence for multi-pass review (review → fix → re-review) vs. single pass, from literature or practice?

### 2e. Practices borrowed from human review workflows (7 questions)

1. Which human review practices have practitioners explicitly mapped onto review subagents: checklists, two-person rule, desk checks, fresh-eyes review, PR culture, editorial review? List each mapping found. †
2. For each mapped practice: what is the trigger, how is it adapted to a subagent, and what evidence do practitioners report? †
3. What does the human-side research base say (code review studies, checklist studies in aviation/medicine, writing research) that plausibly transfers to agent review — and which human findings clearly would NOT transfer (e.g., social dynamics, accountability, domain experience)? Label transfer claims as reasoning unless a source makes the mapping explicitly.
4. What failure modes arise when human practices are borrowed: checklist fatigue in agents, rubber-stamp PR culture, process overhead without payoff?
5. What evidence do practitioners or literature offer for the fresh-eyes effect specifically — in humans and in agents? †
6. For each borrowed practice, what are the adoptability barriers for a beginner (checklist authoring effort, process weight, integration with existing habits)? †
7. Which borrowed practice has the best evidence-to-effort ratio for a beginner, per the sources — and what is the reasoning if the sources are silent? †

### 2f. Multi-agent debate and generator-verifier patterns (7 questions)

1. Which papers, frameworks, and implementations describe generator-verifier, debate, and critique-revise patterns (see the candidate surfaces in section 1f — verify each yourself)? What do their results actually show about separate-context verification? †
2. What practitioner workflows exist built on these patterns (critic agents, review tasks, reviewer graph nodes, "two-model" setups), and what triggers them?
3. What evidence shows verifier/debate loops improve output quality over single generation — metrics, benchmarks, detailed practitioner accounts — and what are the reported magnitudes? †
4. What failure modes are reported: verifier agreement collapse (reviewer rubber-stamps the generator), debate converging on wrong answers, cost growing with marginal gains?
5. At what task complexity or stakes do these patterns pay off, and when do practitioners report them as not worth it? †
6. How much setup complexity do these patterns require vs. a single review subagent — what is the minimal viable version, and who reports running it? †
7. What does the evidence say about verifier quality itself (how often reviewers/verifiers are wrong, how that is measured), and what does that imply for ad-hoc LLM reviewers? †

### 2g. Review of research and planning artifacts (7 questions)

1. What workflows exist for reviewing research outputs, plans, specs, and analyses produced by another agent (AI-research pipelines, plan-review agents, criteria-based reviewers)? For each: trigger, procedure, evidence. †
2. What triggers plan/research review (before execution, before approval gates, before code, before publication), and what context does the reviewer receive (artifact, criteria, source set, constraints)?
3. What evidence do practitioners report: caught missing steps, unsupported claims, bad assumptions, scope errors — with tiers and sources? †
4. What failure modes are reported: reviewers that never check claims against sources, scope-creep suggestions, rubber-stamp plan reviews, review based on style rather than substance?
5. How do fact-checking and source-verification subagents work in practice (what inputs, what verification procedure), and what evidence is there for their accuracy? †
6. What are the setup costs for research/plan review (indexing sources, criteria authoring, context limits), and what is the minimum for a beginner? †
7. What does practice say about review-of-reviews (meta-review) — who checks the reviewer, with what evidence, and is it reported as worth the cost?

---

## 3. Workflow criteria

A finding counts as a **workflow** if and only if it is a repeatable pattern satisfying **all three** of:

1. **Trigger** — a well-defined condition or event that starts the pattern, stated concretely ("when a PR is opened," "when a draft reaches final length," "before a claim goes public"). The trigger must be decidable without ambiguity.
2. **Procedure** — a step-by-step, reproducible process: what gets reviewed, by what kind of subagent, in what context (exactly what inputs the reviewer receives), with what instruction/rubric, and what happens to the findings (triage, fix, re-review). Specific enough that a beginner could replicate it from the description alone.
3. **Evidence** — observable support that the pattern produces its claimed result: a detailed practitioner account with specifics (incidents, counts, before/after, dates), quantitative data, or a documented comparison. Evidence is tiered per section 4. Findings below T2 may be reported as *candidates* but must be labeled as such and cannot enter the ranked synthesis on their own.

Additional requirements:

- **Agent-based:** the reviewer must be an agent in its own separate context reviewing work produced elsewhere (the seed note's move). Pure human-review practices count only as raw material for angle e's mapping — never as workflows by themselves.
- **Harness-agnostic:** the pattern must be describable without naming a product. Product names may appear as examples, not as the pattern.
- **Labeled:** every workflow finding states its evidence tier and flags any component that is the researcher's reasoning.

### Worked example that WOULD count

- **Trigger:** "When a feature branch is marked done, before merge."
- **Procedure:** "The authoring agent spawns a read-only reviewer in a fresh context, handing it the diff, the ticket spec, and a 5-item failure checklist (edge cases, error handling, security, spec deviation, test gaps). The reviewer returns findings tagged critical/major/minor with file:line evidence. The author fixes critical and major items and reruns the suite; minor items are logged for later."
- **Evidence:** "Blog post (URL, 2025-11) by a 2-person team: across 3 months, 14 of 39 review passes found at least one major issue the author agent had missed, including a null-pointer path that reached staging; they compare against the prior 2 months without review." — Satisfies all three criteria; T2.

### Worked example that WOULD NOT count

"The community generally agrees agents should review each other's code; our product does this automatically and users love it." (Vendor page, no specifics.) — No concrete trigger, no reproducible procedure, and the evidence is marketing without specifics (T4).

Other common non-qualifiers, for calibration:

- **Procedure without evidence:** an internal wiki documents a review workflow, but no one reports outcomes. It is a candidate at best — report it as "procedure only, no evidence found."
- **Trigger without procedure:** "I spawn a reviewer whenever I finish something" — no stated process, nothing to replicate.
- **One-off anecdote:** "I asked an agent to check my essay once and it suggested a better opening" — not repeatable, no trigger or procedure, T3 at best.

---

## 4. Sourcing rules

1. **Source hierarchy.** Practitioner/community sources — blog posts, forum threads (Hacker News, Reddit, Discord archives, GitHub Discussions/Issues), conference talks, papers, newsletters — are the primary evidence. Vendor marketing pages and product docs are admissible ONLY to establish what a product does (capability), never as evidence that a pattern works. Prefer primary sources; if only a secondary summary was accessible, say so explicitly.
2. **Every claim carries a source.** Every sourced claim in your report carries URL + author/venue + date (when available). Claims without sources are either labeled reasoning or deleted.
3. **Downgrade to what the source supports.** Distinguish "the source reports that X happened" from "X is true." A single practitioner's account is a single account — report it as one datapoint, not as consensus. If several independent sources report the same pattern, say "reported by N independent practitioners" — never silently upgrade to "this works."
4. **Label reasoning.** First-principles analysis (e.g., "a separate context cannot be contaminated by the author's assumptions") is valuable and encouraged, but must be written as **Reasoning**, never as sourced fact. Reasoning may connect sources or fill gaps, but a reasoning-filled gap must be identified as a gap, and you must say "no sourced evidence found" rather than fabricating.
5. **Evidence tiers.** Tag every finding with its tier:
   - **T1 — measured:** numbers, controlled or documented comparisons, benchmark or study results.
   - **T2 — detailed practitioner account:** specifics (counts, incidents, before/after, reproducible steps), dated and traceable.
   - **T3 — vague anecdote:** someone says something worked, no specifics.
   - **T4 — marketing/unsourced:** vendor claims, hearsay, unverifiable.
6. **Stay in your lane.** Cover your own angle. Material overlapping another angle should be noted briefly and flagged for the orchestrator — do not research it fully.
7. **Report format (your deliverable).** Return a markdown report containing: (a) angle and wave; (b) each question answered in order, with per-answer findings, sources, and tiers; (c) workflow candidates in the trigger/procedure/evidence format, each tagged with its tier; (d) a sources list (URL, author/venue, date, what it was used for); (e) failure modes and adoptability barriers observed; (f) open gaps — questions you could not answer with sourced evidence, plus suggested follow-ups (this feeds wave 2); (g) a one-paragraph headline naming the 3 most adoptable patterns you found, with their evidence tiers.

---

## 5. Synthesis rules (for the orchestrator)

**Adoptability** is defined for a beginner who uses no review agents today, scored on five concrete factors:

1. **Setup cost** — does it require one subagent and a copy-pasteable prompt, or new infrastructure (frameworks, custom tools, training data)?
2. **Overhead** — tokens, latency, and process weight per use. A single-pass review of one artifact beats a multi-round debate loop for a beginner.
3. **Reliability of payoff** — tier-weighted evidence that the review catches real issues more often than it produces noise.
4. **Skill required** — can a beginner run it from a template without prompt engineering or calibration work?
5. **Verifiability** — can the user tell whether the review helped (findings map to fixes, or are checkable against the artifact)?

**Ranking procedure:**

- Collect all workflow candidates from all angle reports. Merge duplicates (below). Drop candidates below T2 unless they are explicitly needed to answer a question the evidence base leaves open — then keep them, labeled as weak-evidence entries.
- Score each candidate on the five factors; rank. Every ranked entry must include: **what** it is, **when** to use it (trigger), **how** to run it (procedure at template level), **tradeoffs and risks**, a **concrete example**, and **evidence with sources and tiers**.
- If most findings are T2/T3 anecdotes, say so at the top of the ranked list — do not let the format imply a stronger evidence base than exists.

**Deduplication:** when two or more angles report the same underlying pattern (e.g., checklist-driven review appears in angles b, e, and f), merge into one entry, cite evidence from all angles, and note the overlap. When patterns are similar but differ in a load-bearing way (e.g., same-context vs. separate-context checklist review), keep them separate and name the difference.

**Contradictions:** never average. Present both sides with their evidence tiers. Prefer the higher-tier side for ranking; if tiers are equal and the claims conflict, mark the finding **contested** and give the practitioner a decision heuristic (e.g., "try it on a low-stakes artifact and check whether findings are actionable").

**The program's core question:** the synthesis must explicitly answer — per the evidence — when separate-context review beats self-review, because that determines whether the seed note's rule is worth its cost at all.

**"Start here" section (mandatory ending):** 2–3 highest-value patterns for a beginner, each with a minimal first-run script: the trigger, the exact prompt template to use, what evidence of success to look for, expected failure modes, and what to do when the reviewer is useless.

---

## 6. Wave budget

Constraint: **max 6 researcher subagents per wave, max 2 waves.** All researchers run in independent contexts, in parallel within a wave, reporting only to the orchestrator (no inter-researcher communication). Researchers receive: their angle sections (1.x + 2.x), sections 3 and 4 of this plan, and their wave assignment.

| Wave | Slots used | Angles / assignments |
|---|---|---|
| **Wave 1** | 6 of 6 | a. Code review agents · b. Writing/document review · c. Adversarial/red-team · d. Self-review loops · e. Human-review borrowings · f. Multi-agent debate / generator-verifier |
| **Wave 2** | ≤6 (expected 2–4) | g. Review of research/planning artifacts · gap-closing: questions wave 1 marked unanswered without sourced evidence; contradictions needing arbitration; adoptability barriers flagged as undercovered; high-value leads wave 1 surfaced but could not follow |

**Why f runs in wave 1:** its literature evidence is needed to calibrate d (self-review vs. separate-context) and c (adversarial review) at synthesis time. Without f in the same wave, d's central question would be answered from anecdotes alone.

**Why g is deferred to wave 2:** it is the most specialized angle, it benefits from knowing what a–f found (which review rubrics and fact-check patterns already exist), and wave 2 must reserve headroom for gap-closing — its explicit second role. The orchestrator should spawn only as many wave-2 researchers as needed; wave 2 is a budget, not a quota.

---

*End of plan. Each researcher executes sections 1–4 for their angle and returns the report format specified in section 4.7.*
