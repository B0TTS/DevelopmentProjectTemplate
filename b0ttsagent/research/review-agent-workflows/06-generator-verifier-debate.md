# Angle f — Multi-Agent Debate and Generator-Verifier Patterns

**Wave 1 · Researcher: angle f · Plan date: 2026-08-21**
**Scope:** Papers and framework patterns for verifier/debate/critique-revise loops; practitioner deployments; evidence of quality gains and cost growth; verifier quality itself.

## (b) Seed note (verbatim)

> "Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')"

**Sourcing note on method:** citations below are based on substantive verbatim excerpts (abstracts, results tables, and body text) retrieved through search-engine full-content results for each paper/page, not on separate page fetches. Where a claim rests on a result I could only see as a snippet, it is marked unverified. Papers are T1 (measured) by nature; practitioner posts are tiered individually.

## (c) Questions answered

### Q1. Which papers/frameworks describe these patterns, and what do results show about separate-context verification? †

**Papers (all T1 measured):**
- **Debate — Irving, Christiano, Amodei, "AI Safety via Debate" (2018, arXiv:1805.00899).** Two agents argue before a judge; theory claims debate with optimal play can answer PSPACE questions with polynomial-time judges. MNIST proof-of-concept: a sparse classifier judge at 59.4% accuracy (6 pixels) rises to 88.9% judge accuracy with precommitted debate; 48.2%→85.2% (4 pixels). Authors list limitations themselves: more compute than direct answering, no guarantees, and "humans might simply be poor judges." https://arxiv.org/abs/1805.00899
- **Multiagent debate — Du et al., "Improving Factuality and Reasoning in Language Models through Multiagent Debate" (ICML 2024, arXiv:2305.14325).** 3 agents × 2 rounds (chosen "due to computational cost"): arithmetic 67.0→81.8%, GSM8K 77→85%, chess +31.5 ΔPS vs single agent; reflection (single-model self-critique) gave only modest gains and "led to poor performance in the factuality setting." Debate reduced hallucinated facts and, in some cases, all agents were initially wrong yet converged correct. https://arxiv.org/abs/2305.14325
- **Self-Refine — Madaan et al. (NeurIPS 2023, arXiv:2303.17651).** Same LLM generates feedback and refines (fresh prompt per pass, but same model — NOT a separate-context reviewer). ~20% absolute average gain across 7 tasks; range 5–40%; code readability +28.8 (GPT-4); **math reasoning ≈ 0** — "a consistent-looking reasoning chain can deceive LLMs"; ChatGPT's feedback was "everything looks good" in 94% of math instances. Gains on math jump to 5%+ only when "an external source can identify if the current math answer is incorrect." https://arxiv.org/abs/2303.17651
- **Reflexion — Shinn et al. (NeurIPS 2023, arXiv:2303.11366).** Verbal self-reflection + external feedback signals: HumanEval pass@1 80%→91% (vs GPT-4 baseline), +22% AlfWorld, +20% HotPotQA, +11% HumanEval — but **failed to beat ReAct on WebShop** (exploration tasks). Ablation: self-reflection adds ~8% over episodic-memory-only retry, but the strongest gains ride on external signals (unit tests, environment). https://arxiv.org/abs/2303.11366
- **Constitutional AI — Bai et al. (Anthropic, 2022, arXiv:2212.08073).** Critique→revision pipeline; critiqued revisions beat direct revisions for small models but "made no noticeable difference for large models"; authors: critiques were "sometimes reasonable, but often made inaccurate or overstated criticisms" — yet revisions were still more harmless. https://arxiv.org/abs/2212.08073
- **Process reward models — Lightman et al., "Let's Verify Step by Step" (ICLR 2024, arXiv:2305.20050).** Trained PRM (on 800k human step labels, PRM800K) best-of-1860: 78.2% vs ORM 72.4% vs majority voting 69.6% on MATH. Verifier quality was bought with 800,000 human labels — the trained-verifier route is not the ad-hoc LLM reviewer route. They note Uesato et al. 2022 found outcome≈process at grade-school level — a genuine source conflict on when process supervision pays. https://arxiv.org/abs/2305.20050

**Framework implementations (capability evidence only):**
- **AutoGen** reflection pattern: two-agent team, critic agent with system message "Provide constructive feedback. Respond with 'APPROVE'...", TextMentionTermination stops the loop. https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html
- **LangGraph** reviewer nodes: coder→reviewer→conditional route back to coder or END on "APPROVED"; practitioners consistently add an iteration cap ("a reviewer that never approves creates an infinite loop"). https://how2.sh/posts/how-to-build-multi-agent-systems-with-langgraph/ ; planner→executor→reviewer reference demo: https://github.com/kanaparthikiran/multi-agent-langgraph-demo
- **CrewAI**: review-style tasks in sequential pipelines (task with `context` of prior task) and hierarchical manager that "coordinates... through delegation and validation of results"; `guardrail`/`human_input` task fields. https://docs.crewai.com/v1.15.14/en/concepts/tasks
- **Anthropic "Building Effective Agents"** names this the **evaluator-optimizer** workflow: "one LLM call generates a response while another provides evaluation and feedback in a loop"; use it "when we have clear evaluation criteria, and when iterative refinement provides measurable value." https://www.anthropic.com/engineering/building-effective-agents (T4 as evidence, but the canonical pattern statement)

**What results show about separate-context verification:** the clearest finding is that **critique helps when the verifier has criteria it can apply or external signals it can check, and fails when verification requires judging correctness the model cannot verify** (Self-Refine math ≈0; Huang et al. below). The "separate context" benefit decomposes into (a) fresh sampling and (b) external/independent judgment — and budget-matched studies (Q3/Q5) show much of debate's apparent gain is (a), not (b).

### Q2. Practitioner workflows built on these patterns, and triggers

- **AutoGen critic-in-group-chat (T2/T4 docs).** Trigger: generator produces a draft in the team; loop runs until critic emits APPROVE (termination condition) or a message cap. Procedure: round-robin generator→critic→generator; critic instructed to give constructive feedback and approve only when addressed. Evidence: framework docs/tutorials only — no measured outcomes (capability, not effectiveness).
- **LangGraph reviewer-node loops (T2).** Trigger: conditional edge after a producer node; route to END on "APPROVED," else back to producer; hard iteration cap (6 in the how2.sh example; 3 in the planner/executor/reviewer demo; both authors flag the infinite-loop failure mode as the reason). Procedure: reviewer receives full message history (context grows per iteration — authors advise summarizing old messages). Evidence: reproducible code + documented gotchas; no outcome numbers (T2 procedure, T3 outcome).
- **Evaluator-optimizer with rubric + guardrails (T2).** Trigger: evaluator returns PASS vs NEEDS_WORK; two guards — max iterations (3–5 recommended; "most tasks pass or plateau within two to three rounds") and a plateau guard that stops when the evaluator returns identical feedback twice. Procedure: generator produces draft; separate evaluator call grades against named binary pass/fail rubric axes; feedback treated "as a revision checklist, not a suggestion"; deterministic evaluator (schema/tests) for mechanical criteria, LLM only for subjective axes. https://www.agentnotebook.dev/tutorials/agentic-workflow-evaluator-optimizer-python (T2 tutorial with working code)
- **Two-layer critic: rules first, LLM second (T2).** Trigger: every write/outbound action before execution. Procedure: rules critic (<10 ms, ~99% accuracy, <0.1% own failure) filters ~70% of events; LLM critic (500–1500 ms, 85–95% accuracy, **3–10% own failure rate**) handles residual semantic checks; fail-closed escalation to humans on failure. Evidence: practitioner series with escalation-rate curves (30%→<5% over 3–6 months) and continuous critic eval (miss-rate target <1%, over-escalation 20%→10%). https://yaqinhei.com/blog/fail-closed-critic-design
- **Production critic loop with circuit breaker (T2).** Trigger: loop runs while critic rejects; orchestrator measures content delta between rounds and breaks when delta < ~5% (genuine revision moves 15–20%); hard cap 4–5 rounds; saves best draft (not last) and rolls back on failure; caches "every draft alongside the structured rubric score." https://andvijaysays.com/2026/06/21/the-builder-the-critic-and-the-circuit-breaker-how-id-design-ai-agents-that-dont-bankrupt-you/

### Q3. Evidence of quality gains, magnitudes, cost growth †

**Measured magnitudes (T1):**
- Self-Refine: ~20% absolute average across 7 tasks (5–40% range); near-zero on math (NeurIPS 2023). Cost: up to 4 feedback+refine iterations per output — ~2–4× generation cost.
- Reflexion: HumanEval 80→91 pass@1; +22% AlfWorld; +20% HotPotQA; +11% HumanEval; **no gain on WebShop** (arXiv 2303.11366). Cost: up to 10 trials + 9 reflections = 19 queries per task.
- Multiagent debate (Du): arithmetic 67→81.8 (+14.8), GSM8K 77→85 (+8), chess +31.5 ΔPS with 3 agents × 2 rounds.
- PRM verifier (Lightman): 78.2% vs 72.4% ORM vs 69.6% majority vote (best-of-1860, MATH) — the trained-verifier ceiling for comparison.
- **Budget-matched refutations (T1, the crucial counterweight):** Smit et al., "Reasoning in Token Economies" (EMNLP 2024, arXiv:2406.06461): when chain-of-thought self-consistency is given the same token/query budget as MAD or Reflexion, "the SC baseline regularly outperforms more complex strategies"; MAD plateaus and its per-round token cost "increases drastically since previous conversations are encoded"; **"multi-agent debate or Reflexion can become worse if more compute budget is utilized"** (entropy of MAD solutions declines per round → tunneling on wrong answers). Reflexion with a GPT-4 evaluator lags self-consistency — "the vast difference between an ideal and a practical evaluator." Huang et al. (ICLR 2024) independently find multi-agent debate no better than self-consistency at equal response counts.
- Practitioner cost numbers (T2): a loop run to hard cap consumes "roughly five to ten times the tokens of a successful two-round completion" (Vijay, 2026-06-21); LLM critic adds "+50% LLM cost" and "+1–2s latency" (Yaqin Hei, 2026-05-17).

### Q4. Failure modes reported

- **Verifier agreement collapse / rubber-stamping:** Self-Refine: ChatGPT feedback "everything looks good" for 94% of math instances (T1). Practitioner: "Agent B, your critic, will frequently approve Agent A's output simply because it reads well on the surface... You think you have a quality gate. You actually have a mutual appreciation society" (Vijay, T2). Agent Patterns Catalog: a naive loop "where the same prompt does both jobs collapses into self-approval and adds cost without quality"; lists "generator and evaluator can collude (especially if same model, same prompt family)" (T3/T4 catalog). Ionix (2026-08-13, T2): "Models are agreeable. Asked to review, they produce a review, and when there's nothing wrong they pad" — fixed by explicitly granting "permission to find nothing."
- **Debate converging on wrong answers:** Wynn, Satija, Hadfield, "Talk Isn't Always Cheap" (arXiv:2509.05396, T1): agents shift correct→incorrect more often than incorrect→correct; performance degrades over rounds; weaker agents pull stronger agents down; on CommonSenseQA debate "always harms performance." Wang et al., "Rethinking the Bounds of LLM Reasoning" (arXiv:2402.18272, T1): two error types — "judge mistake" and "wrong answer propagation"; single agent with a strong prompt matches multi-agent discussion. Smit et al.: entropy decline → tunneling (T1). "When and Why Does Multi-Agent Debate Fail" (arXiv:2510.20963, T1): "debate hacking" — competitive protocols degrade up to −15 pp vs single agent; consensus-seeking suppresses informative disagreement.
- **Cost growing with marginal gains:** Smit (plateau + superlinear token growth per round, T1); Vijay (5–10× at cap, oscillation between drafts, surface-prose churn that "burns tokens at the same rate as genuine work", T2); Self-Refine (gains per iteration diminish; capped at 4, T1).
- **Verifier gaming:** Snell et al. (arXiv:2408.03314, T1): "it was easy to exploit a PRM trained on this dataset via even naïve strategies such as best-of-N." Practitioner: "$50.71 of gate-passing work I deleted by hand... The loop was optimizing its gate score. The gate score had come apart from the thing it was a proxy for" (AI Builder Club, 2026-08-10, T2).
- **Silent reviewer failure:** an agent that silently lost its tools "produced a confident, well-formatted review of a repository it had never managed to read" (Ionix, T2) — reviewer-side failure indistinguishable from "found nothing" without mechanical validation.

### Q5. When do these patterns pay off — and when not? †

**Payoff conditions supported by evidence:**
- **Verifiable/external criteria exist** (tests, schemas, executors, reference answers): Reflexion's biggest gains ride on unit tests; Huang et al. conclude external feedback is the only reliable correction channel; Self-Refine math jumps to +5% only with an external error signal (T1).
- **Open-ended generation where a critic can articulate criteria** (dialogue, readability, constrained generation): Self-Refine's largest gains (+19.8 to +49.2 preference points) (T1).
- **Weak base prompts / no demonstrations:** multi-agent discussion outperforms single agents only "when no demonstrations are provided"; with strong prompts the single agent matches (Wang et al., T1).
- **Easy-to-medium difficulty with a decent base pass rate:** test-time verification/search scales best there; on very hard problems the base model rarely samples the right answer, so selection/verification ceilings bind (Snell, T1).

**When practitioners/literature report it not worth it:**
- Reasoning tasks where the verifier cannot judge correctness: self-correction "consistently results in a decrease in performance" across benchmarks without oracle labels (Huang, T1); Self-Refine math ≈0.
- Matched-budget comparison: "complex reasoning strategies often don't surpass simpler baselines... due to the larger computational resources allocated" (Smit, T1).
- Debate with heterogeneous/weaker participants or high sycophancy: can degrade below no-debate (Wynn, T1).
- When criteria cannot be articulated: "If you cannot articulate the criteria, the evaluator has nothing to enforce and you just burn tokens" (AgentNotebook, T2).
- Exploration-heavy tasks: Reflexion failed on WebShop (T1).

### Q6. Setup complexity; minimal viable version †

**Complexity ladder (per sources):**
- Debate (Du): 3+ agents × 2+ rounds, majority-vote final — highest cost, mixed-to-negative budget-matched results (T1). Original authors themselves limited to 3×2 "due to computational cost."
- Reflexion-style: needs an environment/executor for feedback plus reflection memory (T1).
- AutoGen/LangGraph loops: framework code, termination conditions, iteration caps (T2 — both communities treat the cap as mandatory).
- **Minimal viable version (best evidence-to-effort):** evaluator-optimizer with two roles and one rubric — generator + separate evaluator call grading against named binary pass/fail axes, loop capped at 3–5 with a plateau guard; deterministic checks (JSON schema, tests) replace the LLM evaluator wherever criteria are mechanical. Runnable in ~40 lines (AgentNotebook, T2); the AutoGen two-agent team is the same pattern (docs). Cost guidance: "Claude Haiku 4.5 is often enough to grade a rubric even when the generator uses a stronger model" (AgentNotebook, T2) — a cheap verifier is a documented pattern, not just theory.
- Single review subagent (the seed note's move, no loop) is a strict subset: one critic call, no revision. The loop's added value over one critic pass is bounded by what the generator can fix from feedback — the plateau guard exists precisely because that ceiling is often hit in round 2–3.

### Q7. Verifier quality itself — how wrong are reviewers? †

- **Agreement with humans, general tasks:** GPT-4 judge agrees with humans >80% (85% MT-Bench no-tie, vs 81% human-human) — but with documented position bias, verbosity bias, and self-enhancement bias (GPT-4 favors itself +10% win rate; Claude-v1 +25%); judge failure rate on math grading 14/20 default → 6/20 with CoT → 3/20 with reference answer (Zheng et al., NeurIPS 2023, T1).
- **Expert domains:** SME–LLM judge agreement falls to 68% (dietetics) and 64% (mental health) — vs >80% on general instruction following (ACM IUI 2025 study, T1).
- **Judge-model scale effects:** "only the best (and largest) models show reasonable alignment with humans, though they still differ with up to 5 points from human-assigned scores"; smaller judges are lenient and "easily fooled by dummy answers like 'Yes' and 'Sure'"; even on verbatim-match tasks some judges fail (Thakur et al., arXiv:2406.12624, T1).
- **Self-verification:** LLMs "cannot properly judge the correctness of their reasoning" (Huang, T1); LLM-as-a-judge surveys catalog 12+ bias types with no standard meta-benchmark (Gu et al., arXiv:2411.15594; Ye et al., NeurIPS 2024 WS, robustness ceiling 0.86, T1).
- **Production critic failure rates:** practitioner-reported LLM-critic own-failure rate 3–10%, with explicit eval targets — miss rate <1% (a miss = an incident in fail-closed designs), over-escalation 20%→10% (Yaqin Hei, T2).
- **Implication for ad-hoc LLM reviewers (Reasoning):** the reliable verifiers in the literature (PRMs, Reflexion's unit tests, best-of-N against trained RMs) are trained or external; an ad-hoc prompt-instructed reviewer inherits the biases above (position/verbosity/leniency, self-enhancement if same model family, ~64–85% agreement depending on domain difficulty). Treat any single ad-hoc reviewer verdict as a ~70–85%-reliable signal on easy-to-moderate criteria, much weaker on expert/verification-heavy content — and prefer mechanical checks wherever a criterion can be made mechanical. This is my synthesis of the cited sources, not a sourced claim.

## (d) Workflow candidates (trigger / procedure / evidence)

1. **Rubric-gated evaluator-optimizer loop** (T2; T1 for the underlying critique-revise effect in literature)
   - Trigger: generator completes a draft; task has articulable pass/fail criteria; single-shot quality is below the bar.
   - Procedure: generate → separate evaluator call grades draft against named binary rubric axes (PASS / NEEDS_WORK + specific feedback) → generator revises treating feedback as a checklist → loop until PASS, identical-feedback plateau, or cap (3–5). Deterministic checks replace the LLM evaluator for mechanical criteria; keep human sign-off for high stakes.
   - Evidence: AgentNotebook tutorial (2026-07-29, T2); Anthropic's evaluator-optimizer (2024-12-19, pattern statement); Self-Refine (T1: ~20% abs average, 0 on math); Huang (T1: self-correction without external criteria fails — the loop only pays with real criteria).
2. **External-verifier-first / two-layer critic** (T1 for external-feedback efficacy; T2 practitioner)
   - Trigger: every output that will be executed or shipped (write ops, outbound actions, code before merge).
   - Procedure: rules/deterministic layer (ms, ~99% accuracy) catches mechanical violations; LLM critic reviews only the residual semantic layer; fail-closed escalation to human on any failure; continuous critic eval set with miss-rate/over-escalation tracking.
   - Evidence: Reflexion (T1: gains ride on unit-test feedback); Huang (T1: external feedback is the reliable channel); Yaqin Hei (T2: 30%→<5% escalation over 3–6 months; critic failure rate 3–10%).
3. **Capped multi-agent debate** (T1 mixed — candidate only, do NOT rank as adoptable)
   - Trigger: high-stakes reasoning task where independent samples plausibly diverge and a judge can grade.
   - Procedure: N independent agents answer → read peers' answers → revise → repeat R rounds → majority/judge verdict; cap rounds; matched-budget check against self-consistency.
   - Evidence: Du (T1: +8–15 pp, factuality gains) vs Smit/Huang (T1: no better than self-consistency at equal budget; can worsen) vs Wynn (T1: can actively harm). Contested; a beginner should treat this as research territory, not a default workflow.

## (e) Failure modes and adoptability barriers

Failure modes: rubber-stamp approval (Self-Refine 94% "looks good"; Vijay "mutual appreciation society"); wrong-answer convergence in debate (Wynn; Wang; Smit entropy decline); infinite/ping-pong loops (LangGraph practitioners: cap mandatory; Vijay: oscillation + surface churn); gate-score gaming (Snell PRM exploit; AI Builder Club $50.71 incident); reviewer-side silent failure (Ionix: reviewed an unread repo); cost blowup (Vijay 5–10× at cap; Smit per-round token growth; Yaqin Hei +50%).

Adoptability barriers for a beginner: (1) criteria authoring is the real skill — "find bugs"/"is this good" prompts produce padding or praise, not verification (Ionix; AgentNotebook); (2) judging the reviewer — you need a small labeled set or mechanical checks to know if the critic works (Yaqin Hei's eval set; Ionix's jq validation); (3) loop guardrails are non-optional (cap + plateau + best-draft rollback); (4) cost accounting — token bill is a small fraction of real cost; human review time dominates (Tech10, T2/T3; Loop & Retry cost model, T2/T3); (5) same-model critics share the generator's blind spots and biases (Zheng self-enhancement; Agent Patterns Catalog collusion note).

## (f) Open gaps and suggested follow-ups

- **No sourced evidence found:** controlled before/after numbers from practitioners running debate/critique loops in production (all practitioner accounts are qualitative or cost-side); any study measuring a *single separate-context critic pass* vs same-context self-review in an agentic coding setting (closest: Ionix's adversarial-context argument, anecdotal); effect of reviewer *model choice* (weak vs strong critic) in critique-revise loops outside math (Smit's GPT-4-evaluator result is the one datapoint).
- **Sources conflict:** (1) Du (debate helps) vs Smit/Huang/Wynn (matched-budget, debate flat or harmful) — resolution path: budget-matched replications of Du's factuality claims; (2) Lightman (process ≫ outcome supervision) vs Uesato 2022 (≈ equal) — Lightman attributes to scale/data; (3) Self-Refine (self-feedback helps) vs Huang (intrinsic self-correction hurts) — the reconciliation is external-vs-intrinsic feedback; worth stating explicitly in synthesis.
- **Suggested wave-2 follow-ups:** verifier-calibration tooling for ad-hoc reviewers (rubrics + labeled eval sets — the Yaqin Hei eval method generalized); the "cheap critic" claim (Haiku-grade evaluators) tested against the 64–85% agreement range; meta-review ("who checks the reviewer") evidence.

## (g) Headline

The three most adoptable patterns from this angle: **(1) external/deterministic verification wherever criteria are mechanical** — tests, schema checks, rules-first critics — because the entire T1 literature agrees external feedback is the only reliably corrective channel (Reflexion, Huang, Snell; T1) and practitioners report it as the cheapest, most stable layer (Yaqin Hei: <10 ms, ~99% accuracy, T2); **(2) a single separate-context critic with an explicit binary rubric, loop capped at 3–5 iterations with a plateau guard and best-draft rollback** — the minimal viable evaluator-optimizer (Anthropic pattern statement; AutoGen two-agent team; AgentNotebook runnable template, T2; underlying effect T1: Self-Refine ~20% absolute on criteria-rich tasks, with the hard caveat that math-style unverifiable tasks gain ≈0); **(3) debate only as a research-grade option, never a default** — original gains (Du, T1) are matched or beaten by self-consistency at equal budget (Smit, Huang, T1) and can actively degrade quality via sycophantic convergence (Wynn, T1; Wang, T1). Everything in this angle converges on one rule: **the value of a verifier is bounded by the verifier's own quality (agreement with humans ~64–85% depending on domain, 3–10% critic failure rates in production), so spend the setup effort on criteria and calibration, not on adding more debating agents.**

## (h) Sources

Papers (T1 unless noted):
- Irving et al., AI Safety via Debate (2018) — https://arxiv.org/abs/1805.00899 — debate pattern origin; MNIST judge-boost numbers; admitted limits.
- Du et al., Multiagent Debate (ICML 2024) — https://arxiv.org/abs/2305.14325 (+ https://composable-models.github.io/llm_debate/) — debate gains; reflection weaker; factuality.
- Madaan et al., Self-Refine (NeurIPS 2023) — https://arxiv.org/abs/2303.17651 — self-feedback gains; math ≈0; 94% "looks good".
- Shinn et al., Reflexion (NeurIPS 2023) — https://arxiv.org/abs/2303.11366 — HumanEval 91; external-feedback dependence; WebShop failure.
- Bai et al., Constitutional AI (2022) — https://arxiv.org/abs/2212.08073 — critique-revise; critiques "inaccurate or overstated"; critiqued≈direct for large models.
- Lightman et al., Let's Verify Step by Step (ICLR 2024) — https://arxiv.org/abs/2305.20050 — PRM 78.2 vs ORM 72.4 vs MV 69.6; PRM800K; Uesato conflict.
- Huang et al., LLMs Cannot Self-Correct Reasoning Yet (ICLR 2024) — https://arxiv.org/abs/2310.01798 — intrinsic self-correction degrades; debate ≤ self-consistency; oracle-label critique.
- Zheng et al., Judging LLM-as-a-Judge (NeurIPS 2023) — https://arxiv.org/abs/2306.05685 — 80%+ agreement; biases; math judge failures.
- Smit et al., Reasoning in Token Economies (EMNLP 2024) — https://arxiv.org/abs/2406.06461 — budget-matched refutation; entropy decline; Reflexion evaluator gap.
- Wang et al., Rethinking the Bounds of LLM Reasoning (2024) — https://arxiv.org/abs/2402.18272 — single strong-prompt agent ≈ discussion; judge mistake; wrong-answer propagation.
- Wynn et al., Talk Isn't Always Cheap (2025) — https://arxiv.org/abs/2509.05396 — debate harms; correct→incorrect flips; sycophancy.
- When and Why Does Multi-Agent Debate Fail (2025) — https://arxiv.org/abs/2510.20963 — debate hacking; CopMAD −15 pp; ColMAD protocol fix.
- Snell et al., Scaling LLM Test-Time Compute (2024) — https://arxiv.org/abs/2408.03314 — verifier quality bottleneck; PRM exploitability; difficulty-dependent payoffs.
- Thakur et al., Judging the Judges (2024) — https://arxiv.org/abs/2406.12624 — judge alignment ~5 pts off; leniency; small-judge failures.
- Gu et al., A Survey on LLM-as-a-Judge (2024) — https://arxiv.org/abs/2411.15594 — bias taxonomy; reliability concerns.
- Limitations of LLM-as-a-Judge for domain-specific tasks (ACM, 2025) — https://dl.acm.org/doi/10.1145/3708359.3712091 — SME agreement 64–68%.
- Ye et al., Justice or Prejudice? (NeurIPS 2024 WS) — https://mlanthology.org/neuripsw/2024/ye2024neuripsw-justice/ — 12 biases; robustness ceiling 0.86.

Frameworks/patterns (capability only):
- AutoGen Teams/Termination docs — https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html and .../termination.html — critic agent + APPROVE termination.
- CrewAI Tasks docs — https://docs.crewai.com/v1.15.14/en/concepts/tasks — task context chains, guardrails, human_input, hierarchical validation.
- Anthropic, Building Effective Agents (2024-12-19) — https://www.anthropic.com/engineering/building-effective-agents — evaluator-optimizer canonical description.

Practitioner (tiered):
- how2.sh, LangGraph multi-agent systems (2026-02-07) — https://how2.sh/posts/how-to-build-multi-agent-systems-with-langgraph/ — reviewer node + iteration cap gotcha (T2).
- kanaparthikiran/multi-agent-langgraph-demo — https://github.com/kanaparthikiran/multi-agent-langgraph-demo — planner/executor/reviewer; cap rationale (T2).
- AgentNotebook, Evaluator-Optimizer in Python (2026-07-29) — https://www.agentnotebook.dev/tutorials/agentic-workflow-evaluator-optimizer-python — runnable minimal loop; guardrails; cheap-critic claim (T2).
- Agent Patterns Catalog, Evaluator-Optimizer (2026-05-21) — https://www.agentpatternscatalog.org/patterns/evaluator-optimizer/ — collusion/self-approval failure notes (T3/T4).
- Vijay Vijayasankar, Builder/Critic/Circuit Breaker (2026-06-21) — https://andvijaysays.com/2026/06/21/the-builder-the-critic-and-the-circuit-breaker-how-id-design-ai-agents-that-dont-bankrupt-you/ — sycophancy, token churn, 5–10× cap cost, delta threshold (T2).
- Yaqin Hei, Why a 70% Critic Beats a 95% Critic (2026-05-17) — https://yaqinhei.com/blog/fail-closed-critic-design — two-layer critic; 3–10% LLM critic failure; eval metrics (T2).
- Ionix, We built an AI PR reviewer (2026-08-13) — https://www.ionix.io/blog/we-built-an-ai-pr-reviewer/ — permission-to-find-nothing; adversarial fresh context; silent tool-loss failure (T2).
- AI Builder Club, Agent ROI audit (2026-08-10) — https://www.aibuilderclub.com/blog/ai-agent-roi — gate-score gaming incident (T2).
- Tech10, Real Cost of Running AI Agents (2026-03-09) — https://tech10.ai/blog/real-cost-running-ai-agents-production — cost structure; human review dominates (T2/T3).
- Loop & Retry, cost beyond tokens (2026-07-14) — https://loopandretry.github.io/posts/cost-beyond-tokens/ — six-axis cost model; token bill 1.9% example (T2/T3).
- BSWEN, multi-agent orchestration (2026-03-30) — https://docs.bswen.com/blog/2026-03-30-multi-agent-orchestration-patterns/ — CrewAI reviewer agent + LangGraph conditional review routing (T2/T3).

*End of angle-f report.*
