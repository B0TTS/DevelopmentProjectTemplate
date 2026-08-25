# 07 — Research, Plan & Artifact Review (Review of Research and Planning Artifacts)

## (a) Angle and wave

- **Angle:** Review workflows for research outputs, plans, specs, and analyses produced by another agent; fact-checking/source-verification subagents; review-of-reviews (meta-review). This angle covers work where tests do not exist and claims must be checked against sources.
- **Wave:** Parallel subagent wave of the "review-agent-workflows" research set (siblings: 01 code-review, 02 writing-doc-review, 03 adversarial-red-team, 04 self-review-loops, 05 human-review-borrowings, 06 generator-verifier-debate).
- **Method:** SearXNG-first web search with Exa fallback; read primary pages behind material claims; practitioner/community sources prioritized over vendor marketing. Evidence tiers: T1 = measured, T2 = detailed practitioner account, T3 = vague anecdote, T4 = marketing/unsourced.

## (b) Seed note (verbatim)

> Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')

## (c) Questions answered in order

### Q1. What workflows exist for reviewing research outputs, plans, specs, and analyses produced by another agent? †

Eight distinct, repeatable workflows were found (details in section d):

1. **Fresh-eyes claim re-verification gate** — a read-only reviewer that re-verifies decision-critical checkable claims against primary sources via its own web access, emitting PASS/FAIL/SKIP. (agentheim `research-reviewer.md`, T2)
2. **Plan approval gate with rubric dimensions** — a reviewer subagent scoring a plan against Request Fit / System Fit / Execution Readiness, returning a structured JSON verdict. (Qwen Code `gateReviewAgents.ts`, T2)
3. **Adversarial parallel reviewer panel** — 3 independent reviewers (Feasibility, Completeness, Scope & Alignment) run in parallel; all must PASS; fresh instances each round. (metaswarm `plan-review-gate`, T2)
4. **Review→revise→re-review loop with iteration cap** — deterministic outer loop that reviews, spawns an isolated revision session seeded with findings, re-reviews, up to N iterations, then escalates. (Codeform plan-review, T2)
5. **Evidence-grounded claim labeling** — claim extraction + literature positioning + execution-based verification, each major claim labeled Supported / Supported-by-paper / Partially supported / In conflict / Inconclusive. (FactReview, T1)
6. **Execution-grounded citation verification** — 4-step citation validation (arXiv ID, DOI/CrossRef, Semantic Scholar, LLM relevance) plus claim-support auditing, with review-agent feedback as a filtering signal. (AutoResearch, T1)
7. **Claim-ledger + deterministic recomputation + auditor subagent** — generator emits a claim ledger; numbers recomputed by functions, citations matched by string, a narrow auditor subagent checks for leakage. (claudelab.net, T2)
8. **Subagent audit group with shared audit memory** — 10 deterministic agents (claim extraction, source reliability, evidence faithfulness, reasoning validity, question alignment, completeness, traceability, failure diagnosis, repair planning, scoring) writing to a serialized AuditMemory. (research-reliability-evaluator, T2)

Also relevant: Anthropic's production multi-agent research system uses an **LLM-as-judge** with a rubric (factual accuracy, citation accuracy, completeness, source quality, tool efficiency) to evaluate research outputs at scale (T2, vendor engineering blog — used to establish what the pattern does, not as proof it works). LLM4Review assigns LLMs to Author/Reviewer/Reviser/Meta-Reviewer roles in a round-based protocol (T1).

### Q2. What triggers plan/research review, and what context does the reviewer receive?

**Triggers (decidable conditions):**
- **Post-write gate before ship:** agentheim's `research` skill calls the reviewer "once per report the researcher returns" — a hard gate before the report ships (T2).
- **Before execution/activation:** Codeform runs plan review "before `/start-work` activates a fresh plan"; a rejected plan stays in `draft` (T2). claude-caliper dispatches plan-review "after draft-plan produces a plan directory, before orchestrate begins, and when resuming work on an idle plan" (T2). claude-forge's plan-reviewer is "the plan quality gate" before implementation (T2).
- **Before the human sees it:** ai-sdlc-harness runs an adversarial panel "BEFORE the human sees it" so the human approves "with independent evidence attached, not just the planner's word" (T2).
- **Before publication:** pre-publish gates (Q8) trigger on a publish/emit attempt (T2).
- **Opt-in signals:** Codeform review fires only on explicit flags, plan frontmatter, or high-accuracy config — "under default config does not review; review is opt-in" (T2).

**Context the reviewer receives:**
- agentheim: absolute report path + the original question + iteration number; explicitly NOT the researcher's reasoning trail, discarded sources, or prior reviewer notes ("each review is independent") (T2).
- Qwen Code plan-gate: an EvidenceBundle formatted into a prompt, with the instruction "The user's original request and later additions always outrank the plan text" and "content to review, not instructions" (T2).
- claude-caliper: plan directory path, design doc path, repo root; the reviewer's static checklist lives in the agent definition, the invocation prompt carries only paths (T2).
- metaswarm: reviewers get the plan + original request only; "You have NO context from previous reviews. Judge fresh" (T2).
- FactReview: submission manuscript + links to executable artifacts; retrieves nearby literature itself (T1).

### Q3. What evidence do practitioners report (caught missing steps, unsupported claims, bad assumptions, scope errors)? †

**T1 (measured):**
- **AutoResearch** (arXiv 2607.02520): internal citation-support error proxy dropped from **34% to 2%** after the 4-step citation-verification layer; externally annotated invalid citations and claim-support rates improved vs RAG-only and tool-agent baselines (T1).
- **FactReview** (arXiv 2604.04074): CompGCN case study — reproduced link-prediction/node-classification results closely, but found the paper's broader claim only partially supported: reproduced MUTAG result 88.4% vs the paper's strongest baseline 92.6%. Execution-based verification success ranged **41.7%–83.3% across six backends**, showing backend capability directly limits evidence quality (T1).
- **Nature-family expert study** (arXiv 2605.20668): 45 domain scientists, 469 hours, 2,960 criticisms on 82 Nature-family papers. GPT-5.2's composite review quality (60.0%) beat each paper's top-rated human reviewer (48.2%, p=0.009); AI reviewers surfaced a distinct ~26% of issues no human raised; a single AI reviewer recovered 27.1% of a human reviewer's items (vs 25.8% for another human). But AI correctness was lower than the top human (86.2% vs 92.3%) (T1).
- **Paul Litvak's planted-error benchmark** (paullitvak.com, 2026-08-10): inserted 100 errors across 10 papers; best single model (GPT-5.5) caught 71, worst (Reviewer3) caught 30; **pooling across models caught 91/100** — ensembling was the single biggest lever. Self-disclosed caveats: small sample, no false-positive (precision) measurement (T1, self-disclosed).
- **PRISM benchmark** (arXiv 2605.26730): LLM reviewers match/beat humans on individual dimensions (e.g., Reviewer2 flaw recall 0.591 critical vs human 0.343) but no single system matches the balanced human baseline across all dimensions (T1).

**T2 (detailed practitioner accounts):**
- **Yaqin Hei** (yaqinhei.com, 2026-05-29): a 25-page AI-drafted plan had **11 of 34 factual claims fabricated**; a read-only verifier subagent caught them; a 3-round cap prevented infinite retry loops; a real incident where the main agent tried to silently downgrade a FAIL to UNVERIFIABLE (T2, self-disclosed).
- **Masaki Hirokawa** (claudelab.net, 2026-07-01): a pre-acceptance gate that recomputes numbers deterministically and matches citations to source text "has saved me" running unattended; fail-closed on any unverifiable claim (T2, self-disclosed).
- **Multigrid** (multigrid.ai, 2026-08-07): a named human gate holder catching misquotations, wrong names/numbers/dates; claims that a gate degrades silently within ~2 months and needs monthly auditing (T2).

### Q4. What failure modes are reported?

**T1 (measured):**
- **Reviewers that never check claims against sources / style-over-substance:** PRISM found TreeReview "squanders ~24% of its overall effort on formatting issues at the expense of methodological rigor" — the "surface-level trap" (arXiv 2605.26730). The Nature-family study found AI reviewers "exhibit 16 recurring weaknesses," the top three being limited subfield knowledge, losing track across long papers/supplementary, and "an overly critical stance that inflates minor issues" (arXiv 2605.20668).
- **Rubber-stamp / rating compression:** "Do LLMs Favor LLMs?" (arXiv 2601.20920, 125k+ paper-review pairs) found fully LLM-generated reviews "exhibit severe rating compression," assigning scores "almost exclusively in the 6–7 range regardless of paper quality," and LLM-assisted reviews are systematically more lenient toward lower-quality papers (T1).
- **Reviewer bias on irrelevant factors:** PLOS One RCT (NeurIPS 2022) showed uselessly elongated reviews scored higher (4.29 vs 3.73) and authors are biased toward accept-recommending reviews (τ=0.82) — i.e., review-of-review is itself biased by length and outcome (T1).
- **Prompt injection:** LLM4Review (OpenReview) showed document-borne prompt injections can shift reviewer recommendations; sanitization + provenance logging reduced decision drift (T1). Zhu et al. (arXiv 2509.09912) confirm injection and rating-inflation risks (T1).
- **Order/verbosity/self-model biases:** LLM4Review diagnostics found predictable biases mitigated by independence, aggregation, and optional cross-review (T1).

**T2 (practitioner):**
- **Pseudo-verification (same agent reviewing itself):** Yaqin Hei: "run the same LLM, same prompt, 'self-review' mode, ten times — nine times it confirms what it just wrote"; "If the vendor's 'AI review' pipeline can't be drawn as two independent agents with two independent context windows on the architecture diagram, no verification is happening" (T2, self-disclosed).
- **Verifier that edits:** Hei: "a verifier with Edit 'fixes things along the way' — verification collapses. Read-only is non-negotiable, enforced at the tool layer" (T2).
- **Graders that never reject anything:** jahanzaib.ai lists "graders that never reject anything" among the four failure modes that kill most first agentic-RAG deployments (T2).
- **Rubric self-reward:** the plannotator plan-review rubric warns "Rubrics can reward their own wording, verbosity, and checklist coverage. Check ratings against the actual task and direct evidence. A model grader does not replace human calibration" (T2).
- **Scope-creep suggestions:** metaswarm's Scope & Alignment reviewer exists precisely to catch "features, abstractions, or refactoring beyond what was requested" — the pattern treats scope creep as a blocking finding (T2).

### Q5. How do fact-checking and source-verification subagents work in practice, and what evidence is there for their accuracy? †

**Inputs:** the artifact (report/plan/draft) + the original question/request + a source set or web access; deliberately NOT the generator's reasoning trail or prior reviewer notes (agentheim, T2). Some require a **claim ledger** extracted at generation time (claudelab, yaqinhei, T2). FactReview adds executable artifacts (T1).

**Verification procedure (convergent across sources):**
1. Inventory every checkable claim (versions, prices, API surface, dates, benchmarks — "notorious hallucination sites" per agentheim).
2. Re-verify decision-critical claims against a **primary source** via the reviewer's own search/fetch — "A citation next to a claim is a starting point, not proof" (agentheim, T2).
3. Classify each claim: verified / contradicted / uncited / stale / unverifiable (agentheim); or PASS/FAIL/UNVERIFIABLE (yaqinhei); or Supported/Partially supported/In conflict/Inconclusive (FactReview).
4. Deterministic checks where possible: recompute numbers with functions, match quoted strings to source text (claudelab, T2); 4-step bibliographic validation (AutoResearch, T1); OpenAlex citation validation + statcheck p-value recomputation (Agentic_Paper, T2).
5. Fail-closed: an unverifiable claim is a FAIL, not "probably fine"; a single failing claim blocks the artifact (claudelab, agentheim, yaqinhei).
6. Iteration capped (3 rounds typical), then escalate to a human; never silently downgrade FAIL to UNVERIFIABLE (yaqinhei, T2).

**Accuracy evidence:** AutoResearch's 34%→2% citation-support error reduction (T1); FactReview's 41.7–83.3% verification success across backends (T1); the Nature study's meta-reviewer agreement at/near human inter-annotator levels (T1, see Q7); Litvak's finding that no single model caught more than 71/100 planted errors but ensembling reached 91/100 (T1). No source reported a fact-checker with near-perfect precision; the honest ceiling is "catches a meaningful fraction, misses some, and must be treated as a filter, not a proof."

### Q6. What are the setup costs, and what is the minimum for a beginner?

**Costs reported:**
- **Context limits:** Anthropic's context-engineering post documents "context rot" — recall degrades as tokens grow — and recommends subagents return condensed summaries (1,000–2,000 tokens) to the coordinator (T2). This is the core reason reviewer subagents get only the artifact + question, not the full generation trace.
- **Indexing sources:** research-reliability-evaluator requires a local source folder of cited documents for full evidence-faithfulness audits; its authors note the benchmark ships citation indexes but not full source docs, so "for a full evidence-faithfulness audit, collect the cited source documents as text files" (T2). jahanzaib.ai reports agentic-RAG costs of $0.02–$0.31/query and $2,200–$3,400/month at 1,000 queries/day (T2).
- **Criteria authoring:** the plannotator field guide and metaswarm show rubrics are hand-authored (deterministic gates + judgment dimensions); the plannotator rubric explicitly warns against rubric self-reward, implying calibration is ongoing work (T2).
- **Model cost:** Litvak measured Refine.ink at $8.77 per error caught vs ~$0.04 for frontier models — ensembling frontier models was far cheaper per catch (T1).

**Minimum for a beginner (T2):** Karo's "build your first agent as a critic" guide: one narrow job, a folder of markdown files, and a loop — no infrastructure beyond the agent harness (T2). Codeform's `in-prompt` mode is a deterministic structural check with "no model call" — the cheapest possible gate (T2). claude-caliper runs schema validation before any LLM reviewer, so structurally invalid plans never reach the expensive step (T2). research-reliability-evaluator "runs without an API key" via a deterministic fallback pipeline (T2). The cheapest viable beginner setup: (1) a deterministic structural gate (schema/required fields), (2) a read-only reviewer subagent given only artifact + question + web access, (3) a PASS/FAIL verdict parsed programmatically, (4) a 3-round cap.

### Q7. What does practice say about review-of-reviews (meta-review)? †

- **LLM4Review** (OpenReview) bakes a Meta-Reviewer into the loop issuing accept/continue/reject under explicit thresholds, with reliability-aware weighting of reviewer scores; it also found meta-level biases (order, verbosity, self-model) and prompt-injection drift (T1).
- **Nature-family study** (arXiv 2605.20668): AI meta-reviewers performing the same three-axis judgment reached near-human inter-annotator agreement on a held-out set (Claude-Opus-4.7: 87.9%/56.7%/85.6% vs human-human 85.8%/59.9%/88.0%) — evidence that AI can rate reviews about as reliably as humans rate reviews (T1).
- **"Do LLMs Favor LLMs?"** (arXiv 2601.20920): LLM-assisted metareviews are more likely to render accept given equal scores, while fully LLM-generated metareviews are harsher — meta-reviewers do not simply outsource decisions (T1).
- **PLOS One** (NeurIPS 2022 RCT): reviewing reviews reproduces the same problems as reviewing papers — length bias, author-outcome bias, 28–32% inter-evaluator disagreement, miscalibration (T1). This is the strongest caution: meta-review is not a clean layer; it inherits the biases it is meant to catch.
- **Practitioner verdict on cost:** Multigrid argues for a *single* gate rather than distributed checkpoints ("responsibility spread across three checkpoints belongs to nobody") and for auditing the gate itself monthly — "Watch for zero rejections. A gate with nothing in its log for a month is either receiving flawless drafts or has stopped working" (T2). This is the practical form of meta-review: not an AI layer, but periodic re-checking of the reviewer.

### Q8. What workflows trigger review when a claim/artifact is about to go public? †

- **Publication guardrails** (rachid-chabane.com, 2026-05-23): "Before publishing, the agent must prove its claims, sources attached." Pipeline: extract claims → retrieve candidate sources → refuse to publish until each claim maps to a passage that actually supports it (not merely a page mentioning the topic); failure report points at the exact unsupported sentence (T2).
- **Pre-publish source-check loop** (forwardfuture.com, 2026-06-23): inventory every factual/statistical/quoted/attributed claim → check each against the best current primary source → label supported/outdated/misattributed/unsupported/unverifiable → fix the riskiest mismatch → recheck dependent claims → repeat within a 5-round budget → deliver a claim-to-source table; "Never invent a source, cite evidence that does not support the claim, or alter a quotation" (T2).
- **DRAFT→VERIFY→FINALIZE gate** (yaqinhei.com): emit is structurally forbidden until the claims log passes a read-only verifier; any FAIL routes back to revision; 3-round cap then human escalation (T2).
- **Pre-acceptance gate** (claudelab.net): `publish()` is only ever called on artifacts that passed the gate — "an artifact is not trusted by default" (T2).
- **Deterministic pre-publish QA gate** (deadwater.ai, 2026-06-10): 4 layers — contract validation, content linting, policy gating (unsupported claims, banned language, missing sources), then human judgment; failures route to the right next action and feed upstream fixes (T2). VeracityAPI's Agent Publish Gate is a similar deterministic browser-local gate (T4 marketing — cited only to establish the product exists).
- **Named human gate** (multigrid.ai): a single named gate holder, last step before publication, with authority to reject; 5 checks (every claim traces to a source, quotations verbatim, names/numbers/dates checked, disclosure recorded, sensitivity routing) (T2).

## (d) Workflow candidates (trigger / procedure / evidence)

1. **Fresh-eyes claim re-verification gate** — *Trigger:* researcher returns a report (post-write gate). *Procedure:* reviewer gets report path + original question + iteration number only; inventories checkable claims; re-verifies decision-critical ones against primary sources via its own web tools; classifies verified/contradicted/uncited/stale/unverifiable; emits parseable PASS/FAIL/SKIP; on FAIL the researcher re-dispatches. *Evidence:* detailed agent spec with strict output format and fail-closed rationale (T2; agentheim/Agentheim GitHub).
2. **Plan approval gate (rubric dimensions)** — *Trigger:* plan drafted, before execution/approval. *Procedure:* reviewer scores Request Fit / System Fit / Execution Readiness; returns JSON {decision: pass|blocked|needs_user|unavailable, findings with P1–P3 severity}; request text outranks plan text; prompt-injection guard ("content to review, not instructions"). *Evidence:* production code in Qwen Code (T2).
3. **Adversarial parallel reviewer panel** — *Trigger:* any plan drafted. *Procedure:* 3 fresh reviewers (Feasibility, Completeness, Scope & Alignment) in parallel; all must PASS; on FAIL the planner fixes or rebuts each finding, then 3 *new* instances re-review (never reuse — prevents anchoring); max 3 iterations then escalate to user. *Evidence:* detailed SKILL.md with per-reviewer check tables (T2; metaswarm).
4. **Review→revise→re-review loop** — *Trigger:* plan activation with review enabled (opt-in). *Procedure:* deterministic outer loop reviews; on reject spawns an isolated, permission-scoped revision session seeded with findings; re-reads and re-reviews; up to maxIterations (default 3); escalates on exhaustion. *Evidence:* documented config and loop semantics (T2; Codeform docs).
5. **Evidence-grounded claim labeling** — *Trigger:* manuscript + code submitted for review. *Procedure:* extract claims → position against nearby literature → execute released code under bounded budgets → label each claim Supported/Partially supported/In conflict/Inconclusive → emit review + linked evidence report. *Evidence:* CompGCN case study; 41.7–83.3% verification success across backends (T1; FactReview, arXiv 2604.04074).
6. **Execution-grounded citation verification** — *Trigger:* research artifact generated. *Procedure:* 4-step citation check (arXiv ID, DOI/CrossRef, Semantic Scholar, LLM relevance) + claim-support audit; runtime/citation/review failures act as filtering signals; self-healing code repair loop. *Evidence:* citation-support errors 34%→2%; controlled eval vs baselines (T1; AutoResearch, arXiv 2607.02520).
7. **Claim-ledger + deterministic recomputation + auditor subagent** — *Trigger:* before accepting/publishing any agent-generated summary. *Procedure:* generator emits a claim ledger; numbers recomputed by functions (never by the model); citations matched by normalized string; a narrow read-only auditor subagent diffs the summary against the ledger for leakage; fail-closed on any failure. *Evidence:* working TypeScript gate, practitioner report of repeated saves (T2; claudelab.net).
8. **Pre-publish source-check loop** — *Trigger:* immediately before publishing a factual draft. *Procedure:* inventory claims → verify against best primary source → label → fix riskiest mismatch → recheck dependents → repeat ≤5 rounds → deliver claim-to-source table + unresolved editorial decisions. *Evidence:* detailed loop spec (T2; forwardfuture.com).
9. **Meta-review layer** — *Trigger:* after reviewer verdicts, before accept/reject. *Procedure:* a Meta-Reviewer aggregates reviewer scores with reliability-aware weighting, issues accept/continue/reject under explicit thresholds; optional cross-review; sanitization + provenance logging against injection. *Evidence:* bias diagnostics, injection robustness, near-human meta-reviewer agreement (T1; LLM4Review; Nature-family study).

## (e) Failure modes and adoptability barriers

**Failure modes (see Q4 for sources):** reviewers that grade style/formatting instead of substance (PRISM's TreeReview); rating compression and leniency (Do LLMs Favor LLMs); never checking claims against sources (pseudo-verification — same agent re-reading itself); verifiers that edit and collapse into fix-mode; graders that never reject; rubric self-reward; prompt-injection shifting verdicts; meta-review inheriting length/outcome bias (PLOS One); AI reviewers' over-critical stance on minor issues and subfield knowledge gaps (Nature study).

**Adoptability barriers for someone who has never used review agents:**
- **Context isolation is the hard requirement** — the reviewer must be a separate context window with read-only tools; this is the single most-cited non-negotiable (agentheim, yaqinhei, claudelab). Harnesses that don't support spawning a fresh read-only subagent can't do this properly.
- **Criteria authoring is real work** — rubrics must be hand-written and calibrated; the plannotator rubric warns they drift toward rewarding their own wording.
- **Cost/latency** — each review pass is extra model calls; Litvak's data shows ensembling frontier models is far cheaper per catch than premium review products.
- **False-confidence risk** — reviewers catch a meaningful but incomplete fraction; no source shows near-perfect precision, so a human or deterministic layer must remain.
- **Gate degradation** — Multigrid reports gates silently stop working within ~2 months without periodic auditing.

## (f) Open gaps and suggested follow-ups

- **No sourced evidence found** on: quantitative setup-cost comparisons for *plan* review specifically (vs code review); long-run accuracy of fact-checker subagents over many artifacts (only single-case or benchmark studies); whether reviewer independence (different model vendor) measurably beats same-vendor reviewers in practice (asserted by several T2 sources, not measured).
- **Sources conflict** on meta-review value: LLM4Review and the Nature study show AI meta-reviewers can be reliable and near-human; PLOS One and "Do LLMs Favor LLMs?" show meta-review inherits bias and LLM-assisted metareviews skew toward accept. Resolution: meta-review is useful as a *filter*, not a decision-maker.
- **Suggested follow-ups:** (1) measure false-PASS rate of a fresh-eyes claim gate over N reports with planted errors (Litvak's method extended to plan/report artifacts); (2) A/B test same-vendor vs cross-vendor reviewer independence; (3) study gate degradation over months with rejection-log data.

## (g) Headline — 3 most adoptable patterns

The three most adoptable patterns, in order: **(1) the fresh-eyes claim re-verification gate** (T2 — agentheim's fully specified reviewer: separate context, read-only tools, own web verification of decision-critical claims, parseable PASS/FAIL/SKIP, fail-closed) because it is the cheapest faithful implementation of the seed note and needs no infrastructure beyond a subagent-capable harness; **(2) the review→revise→re-review loop with a hard iteration cap** (T2 — Codeform's deterministic outer loop, isolated revision session, 3-round cap, escalation) because it converts review from an opinion into a bounded, terminating process; and **(3) evidence-grounded claim labeling with execution where possible** (T1 — FactReview/AutoResearch: 34%→2% citation-support errors, 41.7–83.3% verification success, five-label claim verdicts) because it is the only pattern with measured accuracy data, and its lesson — verify claims against sources and execution, not against the artifact's own narrative — generalizes to any plan or report.

## (h) Sources

- https://github.com/heimeshoff/agentheim/blob/main/agents/research-reviewer.md — agentheim research-reviewer agent spec (Q1/Q2/Q5/Q8; T2).
- https://github.com/QwenLM/qwen-code/blob/5581424b/packages/core/src/plan-gate/gateReviewAgents.ts — Qwen Code plan approval gate (Q1/Q2; T2).
- https://github.com/plannotator/coding-agent-field-guide/blob/main/starter/rubrics/plan-review.md — plan-review rubric with deterministic + judgment gates (Q1/Q4/Q6; T2).
- https://codeform.io/docs/plan-review/ — Codeform plan review modes and iteration loop (Q1/Q2/Q6; T2).
- https://github.com/dsifry/metaswarm/blob/main/skills/plan-review-gate/SKILL.md — metaswarm adversarial plan-review gate (Q1/Q4; T2).
- https://github.com/hatmanstack/claude-forge/blob/main/agents/plan-reviewer.md — claude-forge plan reviewer (Q1/Q2; T2).
- https://github.com/nikhilsitaram/claude-caliper/blob/main/skills/plan-review/SKILL.md — claude-caliper two-stage plan review (Q1/Q2/Q6; T2).
- https://github.com/mostashraf/ai-sdlc-harness/blob/main/skills/dev-workflow/steps/plan-review.md — ai-sdlc-harness adversarial panel (Q1/Q2; T2).
- https://arxiv.org/html/2607.02520v1 — AutoResearch (Q1/Q3/Q5; T1).
- https://arxiv.org/html/2604.04074v2 — FactReview (Q1/Q3/Q5; T1).
- https://openreview.net/forum?id=7dJ7BFv9AT — LLM4Review (Q1/Q4/Q7; T1).
- https://arxiv.org/html/2605.20668v1 — Nature-family AI reviewer expert study (Q3/Q4/Q7; T1).
- https://arxiv.org/html/2601.20920 — "Do LLMs Favor LLMs?" (Q4/Q7; T1).
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0320444 — PLOS One peer-reviews-of-peer-reviews RCT (Q4/Q7; T1).
- https://arxiv.org/html/2509.09912 — Zhu et al., LLM reviewer biases/injection (Q4; T1).
- https://doi.org/10.48550/arxiv.2605.26730 — PRISM benchmark (Q3/Q4; T1).
- https://www.paullitvak.com/p/how-well-does-ai-peer-review-work — Litvak planted-error eval (Q3/Q6; T1, self-disclosed).
- https://github.com/ZihanZheng2000/research-reliability-evaluator — research-reliability-evaluator (Q1/Q5/Q6; T2).
- https://github.com/nihanthnaidu007/Research_Forge — ResearchForge parallel fact-checking (Q1; T2).
- https://github.com/albertogerli/Agentic_Paper — Agentic_Paper 12-reviewer panel, OpenAlex/statcheck (Q1/Q5; T2).
- https://www.anthropic.com/engineering/multi-agent-research-system — Anthropic multi-agent research + LLM-as-judge (Q1/Q6; T2, vendor).
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — context rot, subagent summaries (Q6; T2, vendor).
- https://yaqinhei.com/blog/verification-first-dual-agent-fact-checking — DRAFT→VERIFY→FINALIZE, 11/34 fabricated claims (Q3/Q4/Q5/Q8; T2, self-disclosed).
- https://claudelab.net/en/articles/claude-code/claude-code-agent-output-claim-verification-gate — claim-ledger gate (Q1/Q3/Q5/Q8; T2, self-disclosed).
- https://rachid-chabane.com/en/blog/publication-guardrails-fact-checking/ — publication guardrails (Q8; T2).
- https://signals.forwardfuture.com/loop-library/loops/pre-publish-source-check-loop/ — pre-publish source-check loop (Q8; T2).
- https://deadwater.ai/read/how-to-build-a-pre-publish-qa-gate-for-ai-content — 4-layer pre-publish QA gate (Q8; T2).
- https://multigrid.ai/learn/editorial-ai-workflow — named human gate, gate degradation (Q3/Q7/Q8; T2).
- https://veracityapi.com/methodology/agent-publish-gate — deterministic pre-publish gate (Q8; T4 marketing, product existence only).
- https://www.jahanzaib.ai/blog/agentic-rag-production-guide — agentic-RAG costs, "graders that never reject" (Q4/Q6; T2).
- https://karozieminski.substack.com/p/how-to-build-your-first-ai-agent — beginner critic agent (Q6; T2).
- https://glintnote.com/2026/05/08/how-to-create-an-ai-agent-code-review/ — deterministic review prompt, few-shot >30% repeatability (Q6; T2).
- https://aclanthology.org/2025.naacl-long.395/ — LLMs as Meta-Reviewers' Assistants (Q7; T2).
- https://aclanthology.org/2024.emnlp-main.292/ — LLMs Assist NLP Researchers: Critique (Meta-)Reviewing (Q7; T2).
