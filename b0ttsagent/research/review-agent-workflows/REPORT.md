# Review-Agent Workflows: How People Use Independent Review Subagents, Ranked for a Beginner

**Date:** 2026-08-21 · **Research program:** review-agent-workflows · **Author:** orchestrator synthesis
**Method:** 2 waves · 8 researcher subagents in independent contexts (6 angles in wave 1, 1 planned angle + 1 gap-closer in wave 2) · each report read in full by the orchestrator · every workflow below has a trigger, a procedure, and evidence with sources and tiers.

**Seed note (the note this research grows from):**

> "Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')"

---

## Evidence tiers used throughout

- **T1 — measured:** numbers, controlled or documented comparisons, benchmark or study results.
- **T2 — detailed practitioner account:** specifics (counts, incidents, before/after, reproducible steps), dated and traceable.
- **T3 — vague anecdote:** someone says something worked, no specifics.
- **T4 — marketing/unsourced:** vendor claims, hearsay, unverifiable.

**Honesty note on the evidence base:** most practitioner findings are T2. Genuine T1 evidence exists for the seed note's core claim, for reviewer error rates, and for cost numbers — but several key numbers come from single-account measurements or single-author preprints. This is stated inline wherever it matters.

---

## The core question, answered: when does separate-context review beat self-review?

The seed note's central claim ("do not trust your own summary") is **now supported by direct controlled evidence, not just anecdote**:

- **Cross-Context Review (CCR), arXiv 2603.12123 (2026, single-author preprint):** 30 artifacts, 150 injected errors, 360 reviews across four conditions. A fresh-session reviewer seeing only the artifact achieved F1 28.6% vs. 24.6% for same-session self-review (p=0.008, d=0.52). The decisive control: **repeated same-session self-review did not improve on single self-review (p=0.11)** — so the benefit comes from context separation, not from reviewing more. Gains concentrated on critical errors (+11 pp). **Caveats:** no replication yet, and absolute performance is low — even the best condition missed roughly two-thirds of injected errors. **(T1, un-replicated)**
- **D-CCR, arXiv 2603.16244 (2026):** a single fresh-context pass is optimal; extra interactive rounds add "false positive pressure" — reviewers fabricate findings when real errors run out. **(T1, un-replicated)**
- **Adjacent T1 literature agrees:** intrinsic self-correction degrades reasoning without external feedback (Huang et al., arXiv 2310.01798); LLM evaluators recognize and favor their own generations — GPT-4 recognizes its own output 73.5% of the time, and self-preference follows (Panickssery et al., NeurIPS 2024, arXiv 2404.13076); self-evaluation bias measured with human ground truth (+4.3 to +9.4 points self-inflation, Arize 2025-10-08); role-relabeling an erroneous claim from the model's own thought to an external role raises correction rates 23–93 pp (arXiv 2606.05976).
- **T2 practitioner incidents converge on the same mechanism:** a writer session waved through a duplicate-event blocker that a fresh-context reviewer caught (Secades, 2026-07-07); a fresh reviewer found 17 bugs in code that had been reviewed 7 times by the same reviewer (Payne, 2026-04-16); when a harness made subagent forking (context inheritance) the default, the reviewer silently became a rubber stamp and "independence cannot be restored through instructions" (Hirokawa, claudelab.net, 2026-08-17).

**The boundary, per the evidence:** self-review is *not worthless*. Same-context self-review found real bugs in at least one T2 account (Payne), a "verify first" prompt can flip self-correction from degrading to neutral (Liu & Meng, arXiv 2604.22273, T1), and practitioners deliberately use it below a stakes threshold (~300 diff lines, non-sensitive paths). The literature's consistent thread: what self-review lacks is an **independent signal** — external evidence (tests, sources, a fresh context) supplies it. **Practical reading of the seed note: separate-context review pays whenever a missed defect or bad claim costs more than one extra review call; below that, self-review with a rubric and a verify-first step is fine.**

---

## Ranked workflows

Ranking criterion: adoptability for someone who today uses **no** review agents — scored on setup cost, per-use overhead, reliability of payoff (tier-weighted), skill required, and verifiability. Patterns below T2 are excluded except where noted. **#1–#3 are the "start here" set.**

---

### 1. Fresh-context read-only review pass (the seed note made concrete)

**What it is:** when a piece of work is done, spawn one reviewer subagent in a separate, clean context. It receives only the artifact plus its evaluation criteria — never the author's reasoning, chat history, or scratch state. It is read-only (no edit tools). It returns findings; the author decides what to fix.

**When to use it (trigger):** any artifact declared done before it is merged, shared, or acted on — a branch marked done, a draft complete, a plan before execution, a report before it ships. This is the default pattern; everything else in this list is a variant or an upgrade of it.

**How to run it (procedure, template level):** commit a reviewer definition to the repo/folder so every run is identical. Prompt core: "You did not write this and have no stake in it. Pull the artifact/diff yourself; read surrounding context; report only findings that change behavior or correctness, with severity (blocker / should-fix / nit) and file:line evidence. If nothing real, say 'approved' and list what you checked — never pad." Grant read/grep/glob tools only. Two rounds max, then a human. (Assembled from Secades 2026-07-07 and agentheim's research-reviewer spec.)

**Tradeoffs and risks:** ~30k tokens per review pass with ~600 returned (Secades, T2). Same-model blind spots survive the split — "context independence, not model independence" (Secades, T2). The top silent killer: **harness context inheritance** — verify your harness actually gives the reviewer a clean context; several products default to sharing it, and instructions cannot restore independence (Hirokawa, 2026-08-17, T2). Expect roughly two-thirds of real errors to still be missed even in the best case (CCR, T1).

**Concrete example:** Secades' writer/reviewer split — the writer session had "reviewed" a diff minutes earlier and waved through a retry-path bug that duplicated charge/audit events; the fresh-context reviewer, same model, same diff, caught it (claudecodesessions.com/claude-code-writer-reviewer/, 2026-07-07, T2).

**Evidence:** T1 (CCR; D-CCR; Panickssery; Arize), T2 (Secades; Zeikar's 3-agent doc pipeline, zeikar.dev, 2026-05-04; Ken Muse, kenmuse.com, 2026-05-08; Payne; GitHub issue anthropics/claude-code#20304; HN 46524125/46905770).

---

### 2. Checklist/rubric-scoped review with severity ladder and evidence-required findings

**What it is:** the same fresh-context pass, but the reviewer gets a short, fixed checklist (5–7 items) or scoring rubric instead of an open "find problems" instruction, must tag severity, and must cite file:line evidence for anything above the lowest tier.

**When to use it (trigger):** every review you run, from the first one. This is a modifier of #1, not a replacement — but it is the single highest-leverage addition, because it converts the reviewer from a puffer into a filter.

**How to run it:** checklist of the 5–7 failure categories that matter for your artifact (for code: dependency authenticity, scope vs. ticket, tests asserting the requirement not the implementation, secrets, error/empty paths — Abrar Qasim, 2026-05-16, T2; dreaming.press, 2026-07-24, T2). Constraints in the prompt: "only flag changed lines," "no style nits," "if a category is clean, say so — do not invent issues," severity ladder (e.g., RED/YELLOW/GREEN or blocker/should-fix/nit), and "if you cannot cite evidence, downgrade or omit" (Castro, platformtoolsmith.com, 2026-03-09, T2). For docs, score fixed dimensions against thresholds and route pass/fail (iamraghuveer.com, 2026-04-25, T2); calibrate the rubric on 10–20 exemplars before trusting it.

**Tradeoffs and risks:** rubrics drift — they "can reward their own wording, verbosity, and checklist coverage" (plannotator plan-review rubric, T2). The human-side literature adds a load-bearing caveat: checklists work when genuinely enforced and fail when ceremonial (WHO surgical checklist, Haynes et al., NEJM 2009: mortality 1.5%→0.8%; vs. mandated Ontario rollout, Urbach et al., NEJM 2014: no significant effect) — so the gate around the checklist (human triage, skip log) matters as much as the checklist.

**Concrete example:** Manish J ran a two-reviewer checklist-scoped CI review across hundreds of PRs; after ~2 weeks of prompt iteration (mostly "telling it what NOT to flag"), "about 60–70% of findings are actionable" (manishj.com/garden/running-ai-code-review-ci-gemini-claude, 2026-03-30, T2).

**Evidence:** T2 (Manish J; Abrar Qasim; Castro; iamraghuveer; eliteai.tools doc-quality-review), T1 directional (agent-style benchmark: mechanical-rule violations fell 46–86% with a loaded ruleset, github.com/yzhao062/agent-style, self-disclosed caveats; FeedbackWriter RCT, arXiv 2602.16820: rubric-anchored AI feedback beat rubric-less human feedback, d=0.50, in a human-vetted education setting), T1 (Haynes vs. Urbach).

---

### 3. Adversarial-framed minimal pass ("assume it's wrong; find the 2–3 most likely ways this fails")

**What it is:** the cheapest adversarial variant — a single fresh-context pass whose instruction is not "review" but "this is probably wrong; find the most likely failure modes."

**When to use it (trigger):** when the cost of a wrong outcome is high relative to the artifact's size — a plan you'll execute, a claim you'll publish, a deploy path, anything where approval-feeling output is the danger.

**How to run it:** "You are a skeptical senior reviewer. Assume this is wrong until proven otherwise. List the 2–3 most likely ways this fails; for each, name the concrete input or trigger that causes it, where failure shows up first, and whether it's reversible. Do not praise. Default to CHANGES_REQUESTED" (assembled from execute25's Author→Reviewer loop, dev.to, 2026-06-25; Zangwei Zheng's universal critical-review prompt, zangwei.dev; Claude Blattman's plan stress-test, claudeblattman.com). The T1 catch: critique **without external evidence can degrade output** (Huang et al.) — so pair every claimed failure with a concrete trigger, and where possible have the reviewer verify rather than assert (Multigrid's `trigger` field and `evidence` array, multigrid.ai, T2).

**Tradeoffs and risks:** over-flagging ("everything is a risk") and framing sensitivity — a negatively-framed prompt made one user's model "almost excessively negative" (HN 44837789, T2); escape hatches matter — a reviewer stuck on impossible constraints "will just start deleting tests or rewriting the entire codebase" (HN 47535814, T2). Personas alone ("you are a senior security engineer with 20 years") do nothing functional — they create false confidence (Vinny Carpenter, vinny.dev, 2026-05-17, T2).

**Concrete example:** permoon's 5-dimension red-team prompt (hidden assumptions, dependency failures, boundary inputs, misuse paths, rollback/blast radius, ≥2 scenarios each) found 7 flaws in a real BigQuery pipeline case, with different models catching different flaws (github.com/permoon/multi-model-redteam, T2).

**Evidence:** T2 (execute25; Zangwei; Blattman; permoon; redpanda's gated adversarial reviewer), T1 for the underlying critique-revise effect and its limits (Self-Refine ~20% absolute average on criteria-rich tasks, near 0 on math, arXiv 2303.17651; Huang et al.).

---

### 4. Capped review→fix→re-review loop (evaluator-optimizer)

**What it is:** #1 plus a bounded loop: reviewer returns findings, author fixes **only reported defects**, then a re-review — capped at 3–5 rounds, with a plateau guard and escalation to a human.

**When to use it (trigger):** high-stakes changes where you want a terminating process rather than a single opinion (money paths, auth, data migrations, artifacts you'll act on). Not worth it when one pass plus your own judgment suffices.

**How to run it:** generator produces draft → separate evaluator call grades against named binary pass/fail rubric axes → generator revises treating feedback as a checklist → loop until PASS, identical-feedback plateau, or cap (3–5); save the best draft, not the last. **On re-review after a fix round, the measured default is a resumed reviewer (or a fresh reviewer handed the settled-findings list), not a fresh reviewer from scratch:** Shopware measured a resumed session re-validating a fix at ~42k tokens vs. 137–312k fresh, and it worked — it noticed the fix, stood by open findings, and re-checked the code (shopware.com, 2026-05-08, T1); Cloudflare runs exactly this at scale (131,246 review runs, 48,095 MRs, strict re-review rules on fixed/unfixed/won't-fix findings, blog.cloudflare.com, 2026-04-20, T1/T2). The "fresh reviewer each round" advice (ClaudeKit, T2/T3) targets independence from the *author's* reasoning — which context isolation achieves without discarding the reviewer's own findings. Freshness matters against the author, not against the reviewer's own history. Do not run extra rounds on an unchanged artifact: they add 62% more false positives (D-CCR, T1).

**Tradeoffs and risks:** a loop run to cap consumes "roughly five to ten times the tokens of a successful two-round completion" (andvijaysays.com, 2026-06-21, T2); loops can oscillate between drafts, churning surface prose; **if auto-fixing, the fixer's quality dominates** — Imbue measured an auto-fixer overreaching and dropping a task from 16/17 to 8/17; softened instructions ("address when confident, skip otherwise") and summary-only comments eliminated the regressions (imbue.com, 2026-04-29, T1).

**Concrete example:** Shopware's loop experiment — reviewer + fix rounds with resumed re-validation at ~1/3–1/7 the token cost, plus their rule that "no load-bearing result counts until a second, independent worker has confirmed it" after one of seven known defects surfaced in only 1 of 6 identical runs (T1).

**Evidence:** T1 (Self-Refine; D-CCR; Shopware; Imbue), T2 (AgentNotebook runnable template, agentnotebook.dev, 2026-07-29; Codeform plan-review loop, codeform.io; Daehnhardt writer–editor loop with parseable VERDICT, daehnhardt.com, 2026-07-13; Cloudflare).

---

### 5. Cross-model / different-vendor second opinion (for load-bearing results)

**What it is:** a second independent reviewer from a **different model family or vendor** — ideally reviewing the artifact cold — used where a wrong result is expensive.

**When to use it (trigger):** load-bearing results: auth/payments/migration changes, a "pass" verdict you'll rely on, research claims you'll act on. Reserve it — it is the highest-cost entry in the adoptable set.

**How to run it:** second model from a different vendor reviews the cold diff/artifact; findings land where the human reviews; the author must fix or rebut on record (one finding → one commit → one comment); the human is the final judge; **never auto-merge on AI approval** (Agnishotry, p.agnihotry.com, 2026-04-23, T2). Start with two models, not three; the reported minimum is a two-model variant.

**Tradeoffs and risks:** 2–4× cost and latency (a four-vendor setup ran ~$200/month at ~110 PRs, blog.comfy.org, 2026-06-09, T2). Family diversity matters more than model size: same-family judges share biases and inflate their own outputs (T1: Panickssery; Arize), and a same-family judge let its own model's bad queries through until a different family was routed in (TDS, towardsdatascience.com, 2026-08-20, T2). The human-side two-person rule transfers as an error-correlation argument: "we use one LLM to generate code and another to 'LGTM' it… we are correlating the errors" (lamis73.substack.com, 2026-05-31, T2).

**Concrete example:** Nolan Lawson's multi-model PR review — three independent reviewers (separate tools), the main agent waits for all three before verifying itself, fixes only what survives cross-checking; reports "tons of bugs… false positive rate near zero" with strong HN corroboration (nolanlawson.com, 2026-05-25, HN 695 points, T2). Counterweight: budget-matched literature shows debate-class patterns can be beaten by simple sampling at equal cost (Smit et al., EMNLP 2024) — but this entry is parallel independent review, not iterative debate, and Shopware's measured 1-of-6 defect directly justifies a second independent run.

**Evidence:** T2 (Lawson; Agnishotry; Comfy; Matsuzaki's ledger of 17 cross-vendor catches, dev.to, 2026-07-14, self-declared no control group), T1 (Panickssery; Arize; Shopware 1-of-6).

---

### 6. Claim/source verification gate for facts and plans

**What it is:** a fresh-context reviewer that does not grade style — it inventories every checkable claim in the artifact and re-verifies each against primary sources (via its own search/fetch), recomputes numbers deterministically where possible, and fails closed on anything unverifiable.

**When to use it (trigger):** before any artifact containing numbers, dates, citations, versions, or claims ships or is acted on — research reports, plans, specs, publish-ready drafts. This is the highest-value pattern for non-code work.

**How to run it:** generator emits the artifact plus a claim ledger; the reviewer receives only the artifact + original question + source access (never the author's reasoning trail); it classifies each claim verified / contradicted / uncited / stale / unverifiable; a citation next to a claim is "a starting point, not proof" (agentheim research-reviewer, github.com/heimeshoff/agentheim, T2). Deterministic checks first where possible: recompute numbers with functions, match quoted strings to source text (Hirokawa's claim-ledger gate, claudelab.net, 2026-07-01, T2); bibliographic validation via CrossRef/arXiv/Semantic Scholar (AutoResearch, T1). Fail-closed: an unverifiable claim is a FAIL; never silently downgrade FAIL to UNVERIFIABLE (Yaqin Hei, yaqinhei.com, 2026-05-29, T2).

**Tradeoffs and risks:** verification success is backend-dependent — 41.7–83.3% across six execution backends (FactReview, arXiv 2604.04074, T1). No source reports near-perfect precision; treat the gate as a filter, not a proof. Fail-closed gates create friction; a named human gate holder plus a monthly audit of the gate itself (watch for zero rejections — "a gate with nothing in its log for a month is either receiving flawless drafts or has stopped working," multigrid.ai, 2026-08-07, T2) is the reported maintenance.

**Concrete example:** Yaqin Hei's DRAFT→VERIFY→FINALIZE gate — a 25-page AI-drafted plan contained 11 of 34 fabricated factual claims; a read-only verifier subagent caught them; a 3-round cap prevented retry loops; a real incident where the main agent tried to silently downgrade a FAIL to UNVERIFIABLE was blocked (T2). Measured analog: citation-support errors fell 34%→2% with a 4-step citation-verification layer (AutoResearch, arXiv 2607.02520, T1).

**Evidence:** T1 (AutoResearch; FactReview; Litvak's planted-error eval — no single model caught more than 71/100, pooling across models caught 91/100, paullitvak.com, 2026-08-10, self-disclosed), T2 (agentheim; Hirokawa; Yaqin Hei; publication guardrails, rachid-chabane.com, 2026-05-23; forwardfuture pre-publish source-check loop, 2026-06-23).

---

### 7. Calibrate before you trust (decoy exam / answer-key run)

**What it is:** before adopting any reviewer — a model, a subscription, or your own prompt — run it once against a known-answer test to measure whether it can actually discriminate.

**When to use it (trigger):** once, whenever you adopt or change a reviewer, or when you start doubting it. One afternoon, under a dollar.

**How to run it:** light version — build a decoy set of ~20–50 items mixing true claims with logic-inverted fakes; set the bar in advance (e.g., agree with more than 50% of the fakes → reject the candidate); run the candidate as judge; measure discrimination (Matsuzaki, dev.to, 2026-07-14/24, T2 — a frontier model agreed with 60% of the fakes, "on par with a local 8B model," and was declined for <$1). Heavy version — Shopware's answer-key run: freeze code with known defects, plant a canary only careful reading catches, hide the fix commit, disable reviewer memory, score against the key (shopware.com, 2026-05-08, T1).

**Tradeoffs and risks:** an hour of setup; the exam only measures what you put in it; benchmark numbers (e.g., tool-level F1 ~51%) calibrate expectations but not your specific setup.

**Concrete example:** Matsuzaki's failed hire, above — the calibration decision process itself is the example.

**Evidence:** T2 (Matsuzaki), T1 (Shopware answer-key), T2/T3 (continuous critic eval sets: miss-rate <1%, over-escalation <20%→<10% over 3 months, Yaqin Hei, 2026-05-17).

---

### 8. Stakes-gated escalation

**What it is:** a decision rule that routes work by stakes: self-review (or no review) below a threshold; fresh-context review above it; a second vendor's model at the top.

**When to use it (trigger):** per artifact, based on measurable signals — diff size, security-sensitive paths, money, deploy risk.

**How to run it:** the most-cited threshold is ~200–300 diff lines or security-sensitive paths (Payne's <300-line/security-path rule with a CI label gate that blocks merge, nathanpayne.com, 2026-04-16, T2; redpanda's gate: review fires only if diff >200 lines, a prior CRITICAL finding, or auth/security paths touched, github.com/redpanda-data/ui-harness, T2). Keep the cheap layers always-on (lint, tests, schema checks) so the LLM reviewer only sees what those cannot judge (T2: tatteddev.com "Four Reviewers and a Gauntlet"; Cato's two-stage critic).

**Tradeoffs and risks:** thresholds are proxies and can skip real issues below the line; but the human-side evidence (SmartBear's 200–400 LOC / 60–90 min review limits, 2006 study, T1) and the practitioner accounts agree escalation beats uniform heavyweight review, which "trains people to ignore the bot" (Comfy, T2).

**Concrete example:** Payne's CI label gate — a PR cannot merge without external review when it crosses the size/security threshold; below it, same-conversation self-review with a reviewer persona (which "measurably" improved over default self-review across three harnesses, T2).

**Evidence:** T2 (Payne; redpanda; tatteddev; Cato — vendor-adjacent), T1 human analog (SmartBear).

---

### 9. Mechanical/deterministic checks before any LLM review

**What it is:** run tests, schema validation, linters, and rules-based checks first; the LLM reviewer handles only the residual semantic layer.

**When to use it (trigger):** every review pipeline — it is the cheapest quality layer and the only one with near-perfect reliability in scope.

**How to run it:** a rules layer (<10 ms, ~99% accuracy in scope) filters ~70% of events before the LLM critic (500–1500 ms, 85–95% accuracy, 3–10% own failure rate) sees the rest, with fail-closed escalation to humans (Yaqin Hei, 2026-05-17, T2). For docs: deterministic hooks (e.g., a link-check that hard-fails) beat checklists — "a nine-item checklist still ships broken anchors; a fifteen-second script doesn't" (Zeikar, T2). The literature says why: external feedback — tests, executors, references — is the one correction channel that reliably works (Reflexion's gains ride on unit tests, arXiv 2303.11366; Huang et al., T1).

**Tradeoffs and risks:** none beyond the setup of the checks themselves; the failure mode is the opposite — skipping them because an LLM reviewer "feels" equivalent.

**Concrete example:** Yaqin Hei's two-layer critic with measured escalation curves (30%→<5% over 3–6 months) and continuous eval of the critic itself.

**Evidence:** T2 (Yaqin Hei; Zeikar), T1 (Reflexion; Huang et al.; Snell et al. — verifiers trained on PRM datasets were easily gamed by best-of-N, arXiv 2408.03314, a caution that even trained verifiers need the external layer).

---

### 10. Meta-review / periodic reviewer audit (check the checker)

**What it is:** a scheduled re-examination of the reviewer itself — either an automated meta-reviewer aggregating verdicts, or (the practical form) periodic audits of the reviewer's log.

**When to use it (trigger):** after the reviewer has run for a while (monthly, per the main T2 account), or whenever a reviewer's verdict gates something important.

**How to run it:** the practical version is not an extra AI layer but a monthly audit: track rejection and actioned rates, watch for zero rejections and bar softening, sample findings for genericity (Multigrid, T2; Antigravity Lab's per-severity actioned-rate thresholds — HIGH ≥85% actioned / <3% FP — antigravitylab.net, 2026-07-04, T2). The automated version exists and is measured: AI meta-reviewers reached near-human inter-annotator agreement on a held-out set (87.9%/56.7%/85.6% vs. human-human 85.8%/59.9%/88.0%, Nature-family study, arXiv 2605.20668, T1) and LLM4Review's meta-reviewer loop works with reliability-aware weighting (OpenReview, T1) — but meta-review inherits biases (length and outcome bias reproduced in reviewing reviews, PLOS One RCT, T1), so it is a filter, not a decision-maker.

**Tradeoffs and risks:** an AI meta-reviewer doubles the calls and can rubber-stamp in a new form (Do LLMs Favor LLMs? — LLM-assisted metareviews skew toward accept, arXiv 2601.20920, T1); the audit version costs discipline, not tokens, and is the better first step.

**Concrete example:** Antigravity Lab's six-month instrumentation — 7% false positives but 58% fatigue dismissals; hiding INFO-only comments lifted HIGH actioned-rate from 72% to 89%; dedupe cut volume 40% (T2).

**Evidence:** T1 (Nature-family study; LLM4Review; PLOS One; Do LLMs Favor LLMs?), T2 (Multigrid; Antigravity Lab).

---

### 11. Review batching (cost amortization)

**What it is:** amortize the shared context across several reviews — one sitting, shared system prompt (provider caching), or a "librarian" digest summarizing the artifact for reviewers — while keeping each review's context isolated from the other artifacts.

**When to use it (trigger):** several pending reviews at once, or a recurring review bot on a cold-start budget.

**How to run it:** put the shared context in the system message so the provider caches it (measured: 5 specialist reviewers on a 16K-token PR, $1.32 naive → $0.45 with shared-prompt caching, $0.49 with a digest; caching only pays on warm back-to-back series, the digest pays regardless — Main Branch, mainbranch.dev, 2026-05-29, T1); or batch-review several agents' diffs in one sitting with per-change re-entry cards (github.com/darkroomengineering review-batch, T2/T3).

**Tradeoffs and risks:** never amortize the *reviewer's accumulated context* across different artifacts — by the fifth PR "your validator has seen four prior diffs and is subtly influenced by them" (MindStudio, T3/T4); longer batch windows mean staler branches.

**Concrete example:** the Main Branch measurement above.

**Evidence:** T1 (Main Branch), T2/T3 (review-batch skill; Cloudflare scale economics: median review 3m39s, 2.7 reviews per MR).

---

### 12. Multi-agent debate — research-grade, do not adopt as a default

**What it is:** N independent agents answer, read each other's answers, revise, repeat; a judge or majority vote decides.

**When to use it:** almost never, for a beginner. Kept on the list only so the ranking is honest about it.

**Evidence, both sides:** original results are positive (Du et al., ICML 2024: arithmetic 67.0→81.8, GSM8K 77→85, factuality gains — T1), but budget-matched replications are flat or negative (Smit et al., EMNLP 2024: self-consistency at equal budget regularly beats MAD and Reflexion; Huang et al., ICLR 2024; Wynn et al., 2025: debate shifts correct→incorrect more often than the reverse and harms on CommonSenseQA — T1). "Debate hacking" can degrade quality by up to −15 pp vs. a single agent (arXiv 2510.20963, T1).

**Verdict:** contested. If you want more compute on a review, run **independent parallel reviews** (#5) rather than iterative debate — the evidence is far more consistent for parallel than for iterative.

---

## Contested findings (presented per the plan's arbitration rule: never average, prefer the higher tier, give a heuristic)

| Contradiction | Sides (tier) | Arbitration |
|---|---|---|
| Fresh reviewer each round (ClaudeKit) vs. resumed reviewer (Shopware) | T2/T3 procedural vs. T1 measured | **Resumed reviewer + settled-findings list wins for re-review-after-fix** (T1: 42k vs 137–312k tokens, zero re-flags with the list; Cloudflare at scale). Freshness matters against the *author's* context, which isolation achieves. Heuristic: re-use the reviewer session for fix rounds; spawn fresh only when switching artifacts or when independence from the author is in doubt. |
| Noise rate of review findings: 7% (Daily Agent) vs. 13% (Indpro) vs. 50–80% (daily.dev) vs. ~50% precision (Martian) | T2/T2/T2/T1-ish | Not a true contradiction — a spread driven by prompt specificity and reviewer architecture. **Plausible band: 10–40% of production comments are noise; controlled injected-error settings run 20–70%; recall of real defects ~27–53%.** High-severity findings are the reliable tail (85%+ actioned, <3% FP). Heuristic: tighten the checklist and evidence rules until actioned rate clears ~50–60% (the T2 net-positive marker). |
| Debate improves quality (Du et al.) vs. no better/harmful at matched budget (Smit, Huang, Wynn) | T1 vs. T1 | Budget-matched side wins (their comparisons include the budget; Du's did not). Heuristic: parallel independent reviews, not debate. |
| Checklists work (Haynes, WHO) vs. no effect under mandate (Urbach, Ontario) | T1 vs. T1 | Both true — enforcement is the difference. Heuristic: a checklist prompt without a human gate (triage, skip log) is ceremonial. |
| Human fresh-eyes effect exists (Worman 1979; 1993) vs. replication failure (2022) and no peer-vs-self difference (Covill 2010) | T1 vs. T1 | Mixed; smaller than folklore. Agent-side, the analogous effect is T1-measured (CCR; Panickssery). Heuristic: don't over-weight "fresh eyes" claims on either side; rely on the checklist and evidence rules. |
| "AI never rubber-stamps" (caimito) vs. measured uncalibrated-agreement rubber stamp (Matsuzaki) | T3 assertion vs. T2 measured | Measured account wins. |
| Self-feedback helps ~20% (Self-Refine) vs. intrinsic self-correction degrades (Huang) | T1 vs. T1 | Reconciled in the literature: Self-Refine's gains are on criteria-rich tasks with actionable feedback; Huang's degradation is on reasoning without external signals. Heuristic: self-review only with a rubric and a verify-first step; never as the final gate. |

---

## Uncovered gaps (marked explicitly; no speculation used to fill them)

1. **No replicated controlled study of same-context vs. separate-context review** — the CCR/D-CCR preprints (T1, un-replicated) are the only direct evidence; absolute F1 is low (28.6%).
2. **No controlled A/B of resumed vs. fresh reviewer in a fix loop** — D-CCR's nearest condition tested re-review of an *unchanged* artifact.
3. **No vendor-independent "editing time saved" measurements** for document review agents; no normalized per-document costs.
4. **No direct study of rubric vs. no-rubric reliability for agent review** outside education (FeedbackWriter) and a mechanical benchmark.
5. **Longitudinal reviewer-accuracy tracking exists in exactly one T2 account** (Antigravity Lab); reviewer "staleness"/drift over months is otherwise unmeasured.
6. **Martian benchmark headline numbers (F1 ≈51%) unverifiable this program** (JS-only dashboard) — treated as secondary.
7. **No sourced workflow mapping a human "desk check" onto subagents** (only a T3 candidate).
8. **Cross-vendor reviewer independence is asserted (T2, multiple) but not measured** (no A/B isolating vendor difference).

---

## Start here: the first three things to try

### Step 1 — The read-only fresh-context reviewer (workflow #1)

**First run:** pick one finished artifact (a diff before merge, or a draft before sharing). Spawn a reviewer subagent with a clean context, read-only tools, and this prompt:

> "You did not write this and have no stake in it. Pull the artifact/diff yourself; read surrounding context. Report only findings that change behavior, correctness, or factual accuracy, each with severity (blocker / should-fix / nit) and evidence (file:line or the exact passage). If a category is clean, say so — never pad. If nothing real, say 'approved' and list what you checked."

**What success looks like:** at least one finding you act on in the first few runs — or a credible "approved" that names what was checked. **Expected failure mode:** generic praise, or findings that miss the point — then add a 5-item checklist (#2) or adversarial framing (#3). **When it's useless:** first verify the harness actually isolated the reviewer's context (the #1 silent killer); then check whether the artifact simply has no checkable criteria.

### Step 2 — Add the checklist and severity ladder (workflow #2)

**First run:** write 5–7 concrete failure items for your artifact type (for code: edge cases, error handling, security, spec deviation, test gaps). Add: "only flag what violates these; cite file:line; if you cannot cite evidence, downgrade or omit." Expect to iterate the checklist twice — the T2 accounts converge on "telling it what NOT to flag matters more than what to flag," and ~60–70% actionable findings is the realistic bar, not 100%.

### Step 3 — Run the decoy exam once (workflow #7)

**First run:** build a 20-item decoy set (10 true statements about your domain, 10 with a logic-inverted falsehood), decide the rejection bar in advance, and run your reviewer against it. Under a dollar, one afternoon. If it passes, you have calibrated trust; if it fails, you just saved yourself from trusting a rubber stamp.

**Ordering note:** these three compose — 1 is the pattern, 2 is its quality lever, 3 is its trust check. Everything above them in the ranking (cross-vendor review, claim gates, loops) is an escalation to add when stakes rise.

---

## Sources

Per-angle full source lists (URL + author/venue + date + usage) are in the report files in this folder:

- `01-code-review-agents.md` (20 sources) — code review workflows, Imbue T1, Martian benchmark, Lawson, Secades, Castro, Indpro, LogRocket, daily.dev
- `02-writing-doc-review.md` (26 sources) — doc review patterns, FeedbackWriter RCT, agent-style benchmark, rubric gates
- `03-adversarial-red-team.md` (35 sources) — adversarial workflows, AgentHarm, Self-Refine, judge-bias literature, "17x" claim debunked
- `04-self-review-loops.md` (24 sources) — self-correction literature, Shopware, context-inheritance failure, Payne
- `05-human-review-borrowings.md` (32 sources) — two-person rule mappings, SmartBear, Haynes/Urbach, Bacchelli & Bird, fresh-eyes studies
- `06-generator-verifier-debate.md` (28 sources) — debate literature, budget-matched refutations, evaluator-optimizer, verifier quality
- `07-research-plan-artifact-review.md` (35 sources) — plan/research review, claim gates, meta-review, publication triggers
- `08-reviewer-reliability-calibration.md` (28 sources) — CCR/D-CCR preprints, calibration practices, accuracy bands, cost measurements

The plan that governed the program: `PLAN.md` (angles, questions, workflow criteria, sourcing and synthesis rules, wave budget).

*Key T1 anchors cited in this report: CCR (arXiv 2603.12123); D-CCR (arXiv 2603.16244); Huang et al. (arXiv 2310.01798); Panickssery et al. (arXiv 2404.13076); Arize self-evaluation bias (2025-10-08); Shopware review experiment (2026-05-08); Imbue fixer study (2026-04-29); Main Branch cost measurements (2026-05-29); Self-Refine (arXiv 2303.17651); Du et al. debate (arXiv 2305.14325); Smit et al. (arXiv 2406.06461); AutoResearch (arXiv 2607.02520); FactReview (arXiv 2604.04074); FeedbackWriter (arXiv 2602.16820); Haynes NEJM 2009 / Urbach NEJM 2014; SmartBear 2006.*
