# 08 — Reviewer Reliability, Calibration, and Cost Arbitration

## (a) Angle and wave

**Angle:** Gap-closing (wave 2) — reviewer reliability, calibration, and cost arbitration. Closes six gaps (G1–G6) left by wave 1: fresh-vs-resumed reviewer contradiction, reviewer pre-screening, quantified reviewer accuracy, reviewer model choice, controlled evidence for same-context vs separate-context review, and review batching. Method: live web research (SearXNG + Exa fallback; every material claim read in full) + first-principles reasoning, labeled as such. **Date:** 2026-08-21.

## (b) Seed note (verbatim)

> "Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')"

## (c) Gaps

### G1 — Contradiction to arbitrate: fresh reviewer per round vs. resumed reviewer

**Findings.** The two original sources stand as described: ClaudeKit recommends a **new** reviewer each round ("a reviewer that already passed round one is biased toward passing round two") — a procedural recommendation with no measurements (T3; site sells kits, treat as vendor-adjacent) — while Shopware **measured** a resumed reviewer session re-validating a fix at ~42,000 tokens vs 137,000–312,000 for a fresh review of the same scope, and it worked: it noticed the applied fix, stood by still-open findings, and re-checked the actual code rather than trusting memory (T1, Martin Bens, Principal SWE, Shopware, 2026-05-08). New evidence found this wave:

- **Cloudflare (T1/T2, 2026-04-20)** runs re-review at production scale as an **incremental re-review aware of its own previous findings**: 131,246 review runs across 48,095 merge requests in 5,169 repos in the first 30 days; average MR reviewed 2.7 times; strict re-review rules (fixed findings omitted, unfixed re-emitted, "won't fix" respected, "I disagree" → coordinator argues back). This is the resumed-reviewer side, at the largest scale found anywhere.
- **Abysim (T2, 2026-02-22)** reports the fresh side: when review iterations shared context, the reviewer "verifies that problems from the first pass are fixed… but never looks at the code from scratch"; after switching to per-iteration context isolation (only input + instructions, no memory of prior passes) "it started catching new problems on each pass."
- **herdr-review-loop (T2/T3, GitHub, mikhail-angelov)** wipes both sessions before every turn (fresh side) **but** carries a durable `review-summary.md` (applied/rejected/deferred findings) into the fresh reviewer so settled points are not re-litigated — a middle ground: fresh context + durable decision record.
- **D-CCR paper (T1, Song Tae-Eun, arXiv 2603.16244, 2026-03-17)** — controlled experiment: a completely fresh second review of the *same unchanged artifact* (condition 2c) performed **worst** (F1 0.263 vs 0.376 single-pass); extra rounds raise recall but generate 62% more false positives ("false positive pressure" — reviewers fabricate findings when real errors are exhausted). Caveat: no fixes were applied between rounds, so this tests repeated review of an unchanged artifact, not re-review-after-fix.
- **Shopware ablation (T1):** with a list of already-settled findings in the brief, re-reviews produced **zero re-flags**; without it, models re-flagged settled items.

**Verdict: contested as a universal rule, but the cost-arbitrated synthesis is now evidence-backed.** For re-validation *after fixes*, the resumed reviewer (or fresh reviewer carrying the settled-findings record) is the measured default: T1 (Shopware tokens + worked) and T1/T2 (Cloudflare scale). The fresh-reviewer-per-round advice is T2/T3 (Abysim, herdr, ClaudeKit) and targets independence from the *author's* reasoning — which the T1 evidence shows is best achieved by context isolation from the author, not by discarding the reviewer's own prior findings. The T1 D-CCR result warns that extra rounds on *unchanged* artifacts add noise regardless of freshness. **At stakes:** high-stakes loops should carry the settled-findings record and re-ground the reviewer in the actual code; the cheapest correct re-check is a resumed session (~1/3–1/7 cost, T1).

### G2 — Reviewer pre-screening (try-before-trust)

**Findings.** The practice is documented, with procedure and outcomes:

- **Ryosuke Matsuzaki (T2, dev.to, 2026-07-14 and 07-24)** "interviews" a candidate reviewer before adopting it: a decoy exam mixing true claims with logic-inverted false ones, run across 20 judge runs, with the bar set in advance (agree with more than 50% of the fakes → no judge duty). Gemini failed — 60% agreement with the fakes, "discrimination on par with a local 8B model" — and was declined. Cost: ~¥100 (under $1) of API calls vs the ~$20/month subscription skipped. He also reports the measurement principle: "uncalibrated agreement is basically a rubber stamp… measure the fraction of bad things it actually flagged as bad (TPR)," and a cross-vendor blind spot (a fake claim dressed in "numbers + statistical vocabulary + a cautious tone" passed both Codex and Gemini) that led to the rule: quantitative claims are never settled by AI votes.
- **Shopware (T1, 2026-05-08)** documents the heavier version: an answer-key calibration run — freeze code with 7 hand-verified defects, plant a canary (a comment/code mismatch only careful reading catches), park the fix commit outside visible history, disable reviewer memory, score every review against the key. Results: no model found all 7; the canary was found 5/5 by one model; one defect surfaced in only 1 of 6 identical runs.
- **Yaqin Hei (T2, 2026-05-17)** describes continuous critic calibration: an eval set of historical incidents + counter-examples (must score 100% — any miss is a pre-launch bug) plus random sampling of 500–1000 happy-path approvals to measure over-escalation; targets: miss rate <1%, over-escalation <20% at start dropping below 10% in 3 months; eval set updated weekly.
- **T3 corroboration:** aipatternbook.com (calibrate a judge against 50–100 human labels; the gold set catches rubric drift before production metrics move) and agentnotebook.dev ("always calibrate the judge against a small set of human labels before you trust its absolute numbers").

**Verdict: closed.** Try-before-trust is a real, cheap, repeatable practice (T2 with a concrete failed hire; T1 methodology from Shopware).

### G3 — Quantified reviewer accuracy

**Findings.** A band is now estimable from several independent measurements:

- **Martian Code Review Bench (T1 structure, github.com/withmartian/code-review-benchmark):** open-source benchmark — 50 PRs from 5 OSS repos with human-verified golden comments (offline) plus a continuous online benchmark on fresh PRs; precision/recall via LLM judge; 19 tools evaluated. The headline numbers cited in wave-1 report 01 (best tool F1 ≈51.2%, precision ≈49.2%, recall ≈53.5%) could **not be re-verified this session** (dashboard is JS-only; README carries no numbers) — treat as unverified secondary.
- **CCR paper (T1, arXiv 2603.12123):** best condition (fresh-context review) achieved precision 31.5%, recall 27.1%, F1 28.6% on injected errors — i.e., even the best condition caught <1/3 of errors and ~2/3 of its findings were noise.
- **Antigravity Lab (T2, Masaki Hirokawa, 2026-07-04):** production reviewer, six months of instrumentation: false-positive rate 7%, but **fatigue dismissals were 58% of all comments**; per-severity actioned-rate thresholds (HIGH ≥85% actioned / <3% FP; MEDIUM ≥50% / <8%; LOW ≥20%); hiding INFO-only comments lifted HIGH actioned-rate from 72% to 89%; dedupe cut comment volume 40%.
- **Tian Pan (T3, 2026-05-05 and 04-17):** "first-generation AI review tools got 20% actionable rates on a good day"; industry FP rates "between 5% and 15%"; net-positive deployments report comment action rates >55%.
- **T3/T4 targets:** Visdom Code Review (FP <15%, actionable >80%); Tenki (FP >30–40% is a serious problem; 50%+ in the first two weeks → engagement never recovers).
- **Judge-human agreement:** TDS (T2, 2026-08-20) measured low-to-mid 80s percent (self-reported, rough); aipatternbook (T3) claims ~80% "in published research."

**Verdict: closed with a band.** Plausible band for "how often review findings are wrong or noise": **false-discovery (noise) rates of roughly 10–40% of comments in production, 20–70% in controlled injected-error settings; recall of real defects roughly 27–53%.** High-severity findings are the reliable tail (85%+ actioned, <3% FP, T2). Longitudinal tracking exists only in Antigravity's account (T2).

### G4 — Reviewer model choice (weaker/cheaper critic vs stronger generator)

**Findings.**

- **agentnotebook.dev (T3, Ren Okabe, 2026-07-20/22/29):** three tutorials consistently use the cheapest tier as judge — `claude-haiku-4-5` judging `claude-opus-4-8` output: "judging is a read-then-classify task, not a generation task"; "Claude Haiku 4.5 is often enough to grade a rubric even when the generator uses a stronger model"; escalate to sonnet "when the rubric needs deeper reasoning." Recommendations, no measurements.
- **Shopware (T1, 2026-05-08):** "The default assumption, take the biggest model for everything, did not survive the data." The smallest model (luna) uniquely found installed-library-internal defects; the mid model became the default reviewer; the flagship (sol) marked *every* finding as blocking, making its severity labels useless. Cost is rate × tokens: luna burned ~2× sol's tokens yet cost less (1/5 the rate). Caveat: all runs used maximum reasoning effort — cheaper settings unmeasured.
- **Yaqin Hei (T2, 2026-05-17) — correction to the gap's framing:** "a 70% critic beats a 95% critic" is about **automation rate** (fail-closed escalation: 70% automation with safe escalation beats 95% with pass-through), not critic model quality. The article's model-relevant data: rules critics are 99%+ accurate in scope vs LLM critics 85–95%, with LLM critic failure rates of 3–10%.
- **Against blind cheapness:** Arize (T1, 2025-10-08) measured self-evaluation bias — all four evaluators scored their own outputs higher on their own scales (+4.3 to +9.4 points); after calibration against human scores only Google's inflation survived (+37.1). TDS (T2, 2026-08-20) hit a production incident from a same-family judge and fixed it by routing judgment to a different family. G-Eval (T1, via wave-1 report 04): judge-model capability dominates rubric mechanics (+0.113 vs +0.014). Matsuzaki (T2): a frontier model failed the decoy interview with discrimination "on par with a local 8B model."

**Verdict: closed.** Evidence supports a cheaper critic for rubric-graded, read-then-classify review (T1 Shopware routing; T3 tutorials), with two qualifiers: **model-family diversity matters more than model size** for independence (T1 Arize/Panickssery; T2 TDS), and capability still matters for hard semantic review (T1 G-Eval; Shopware's smallest model found fewer defects in the broad sweep).

### G5 — Same-context vs separate-context review: controlled evidence

**Findings.** Wave 1 found no controlled study of this exact question. This wave closes it:

- **Cross-Context Review (T1, Song Tae-Eun, arXiv 2603.12123, submitted 2026-03-12):** controlled experiment — 30 artifacts (code, technical documents, presentation scripts) with 150 injected errors, four conditions, 360 reviews: same-session Self-Review (SR), repeated Self-Review (SR2), context-aware Subagent Review (SA, fresh context + generation prompt), and Cross-Context Review (CCR, fresh session, artifact only). CCR F1 28.6% beat SR 24.6% (p=0.008, d=0.52), SR2 21.7% (p<0.001, d=0.72), SA 23.8% (p=0.004, d=0.57). The key control: **SR2 ≈ SR (p=0.11)** — reviewing twice in the same session does not help, ruling out repetition as the explanation; the benefit comes from context separation itself. Gains concentrated on critical errors (+11 pp) and code artifacts (+4.7 F1).
- **D-CCR (T1, arXiv 2603.16244, 2026-03-17):** single-pass fresh-context review is optimal; multi-turn interaction degrades it (false positive pressure, review-target drift).
- **Adjacent T1:** Panickssery, Bowman & Feng, "LLM Evaluators Recognize and Favor Their Own Generations" (arXiv 2404.13076, 2024) — self-recognition correlates with self-preference; Arize (2025) — self-evaluation bias measured with human ground truth. **T3 theoretical:** Brilliant, "Limits of Self-Correction in LLMs" (preprint 2026-01-13) — correlated-error argument that fresh-context same-model review is more independent than same-context self-critique; no empirical results. **T4:** Augment's vendor guide cites a self-correction study (verifier higher recall on others' outputs, lower on its own) — unverified secondary citation.

**Verdict: closed.** The seed note's core claim ("do not trust your own summary") now has direct controlled support (T1): separate-context review beats same-context review, and same-context repetition does not. Caveats: single-author preprint, no replication, and absolute performance is low (F1 28.6%; ~2/3 of findings are noise even in the best condition).

### G6 — Review batching / cost mitigation

**Findings.**

- **Main Branch (T1, Andrea Griffiths, 2026-05-29):** measured — five specialist reviewers on one 16K-token PR: naive $1.32; shared system-message prompt caching $0.45 (66% off); "librarian" digest (one agent summarizes the diff, reviewers read the digest) $0.49. Caching only pays on warm back-to-back series and collapses to naive on cold starts (the operational reality for PR bots); the digest pattern pays regardless. Also measured: cache activation is non-deterministic below ~4–16K tokens of shared prefix.
- **GitHub Agentic Workflows docs (T3/T4):** official guidance — "batch instead of reacting to events": a scheduled batch run sends the shared system prompt once, so providers cache it across items, reducing AI Credits.
- **darkroomengineering review-batch skill (T2/T3, GitHub):** batch-reviewing several agents' diffs in one sitting with per-change re-entry cards: "Reviewing 4 agents in one sitting is much cheaper than checking one, leaving, and returning cold to the next"; tradeoff — longer leash means staler branches.
- **Matsuzaki (T2, 2026-07-29 comment):** "the review layer runs async/batch, and the one hiring decision it touched was settled by about a dollar of API calls."
- **Counterpoint:** MindStudio (T3/T4, 2026-04-24) warns against reusing one session across many PRs — "by the fifth PR, your validator has seen four prior diffs and is subtly influenced by them. Always start fresh sessions."
- **Cloudflare (T1/T2):** scale economics — median review 3m39s, 2.7 reviews per MR.

**Verdict: closed.** Batching to amortize shared context is a measured cost mitigation (T1), with a consistent constraint: amortize the *shared context* (caching, digests, one sitting), never the *reviewer's accumulated context* across different artifacts (T3/T4 MindStudio; T2 Abysim).

## (d) Workflow candidates (trigger / procedure / evidence)

1. **Reviewer pre-screening interview (decoy exam).** *Trigger:* before adopting any reviewer/judge model or subscription. *Procedure:* build ~20–50 items mixing true claims with logic-inverted fakes; set the bar in advance (e.g., agree with >50% of fakes → reject); run the candidate as judge; measure discrimination (TPR on fakes); log the result. *Evidence:* T2 — Matsuzaki (2026-07-14/24): Gemini failed at 60% agreement with fakes, declined; cost <$1. Adoptability: high — one afternoon, no infrastructure.
2. **Answer-key calibration run (planted errors + canary).** *Trigger:* before trusting a reviewer on a codebase, or when review quality is doubted. *Procedure:* take fixed bugs you can un-fix, plant a canary only careful reading catches, hide the fix commit, disable reviewer memory, score findings against the key; repeat at least one condition. *Evidence:* T1 — Shopware (2026-05-08): 7 defects; canary 5/5 by one model; one defect in 1 of 6 runs. Adoptability: medium — needs a git repo and a log file; "an afternoon of building an answer key pays for itself" (Shopware).
3. **Resumed-reviewer re-validation with settled-findings list.** *Trigger:* after a fix round in review→fix→re-review. *Procedure:* resume the reviewer's session (or hand a fresh reviewer the settled-findings list); instruct it to re-check the actual code, stand by open findings, not re-flag settled ones. *Evidence:* T1 — Shopware (42k vs 137–312k tokens; zero re-flags with the list); T1/T2 — Cloudflare (incremental re-review at 48k MRs). Adoptability: high — a session-resume or a list in the prompt.
4. **Fresh-context single-pass review (CCR).** *Trigger:* any artifact where a missed error is expensive. *Procedure:* review in a fresh session receiving only the artifact + rubric; one pass; if more compute is available, run independent parallel reviews rather than sequential rounds. *Evidence:* T1 — CCR (F1 28.6 vs 24.6, p=0.008); T1 — D-CCR (one round optimal; extra rounds add noise). Adoptability: high — "costs only one extra session."
5. **Batch review with shared-context amortization.** *Trigger:* multiple PRs/artifacts pending; cold-start environment. *Procedure:* put shared context in the system message (cache) or digest-first (librarian); run reviews back-to-back; keep each review's context isolated from other artifacts. *Evidence:* T1 — Main Branch ($1.32 → $0.45/$0.49); T3/T4 — GitHub docs; T2/T3 — review-batch skill. Adoptability: medium — requires harness support for caching or a digest step.
6. **Actioned-rate instrumentation (longitudinal calibration).** *Trigger:* after deploying a reviewer; weekly thereafter. *Procedure:* bucket every comment into actioned/discussed/ignored; separate false positives from fatigue dismissals (one emoji label at resolution); per-severity thresholds; throttle INFO/LOW first, dedupe per file. *Evidence:* T2 — Antigravity Lab (2026-07-04): FP 7%, fatigue 58%, HIGH actioned 72→89% after hiding INFO, dedupe −40% volume. Adoptability: medium — needs a small script and team discipline.

## (e) Failure modes and adoptability barriers

- **Rubber-stamping and self-preference** are now measured, not anecdotal: T1 (Panickssery 2024; Arize 2025) — same-family judges inflate their own outputs; T2 (TDS) — a same-family judge let its own model's bad queries through until a different-family judge was routed in.
- **False positive pressure:** extra review rounds on an exhausted artifact fabricate findings (T1, D-CCR) — the mechanism behind "review noise."
- **Fatigue dismissals, not false positives, kill production reviewers:** 58% of comments ignored despite 7% FP (T2, Antigravity). Volume control (caps, dedupe, severity gating) is the fix.
- **Context rot in reused sessions** (T3/T4 MindStudio; T2 Abysim) — the reason batch review must amortize shared context, not reviewer memory.
- **Barriers for a beginner:** calibration requires a small labeled set (human work, but ~1 hour per the T2 accounts); benchmark numbers are tool-level, not subagent-level, so they calibrate expectations, not your setup; harness context isolation must be verified (several products default to sharing context); cost data is mostly single-account (Shopware, Main Branch).

## (f) Remaining open gaps

- Martian benchmark headline numbers unverified this session (JS dashboard); the wave-1 numbers remain secondary.
- No direct controlled A/B of **resumed vs fresh reviewer in a review→fix→re-review loop** — D-CCR-2c is the nearest (fresh second review of an *unchanged* artifact, worst result). Suggested follow-up: fix-application variant of the CCR protocol.
- CCR/D-CCR are single-author preprints; no replication, and absolute F1 is low (28.6%).
- Cheaper reasoning-effort settings unmeasured (Shopware caveat).
- Longitudinal reviewer-accuracy tracking exists in exactly one account (Antigravity, T2).
- Augment's vendor-cited self-correction study unverified.

## (g) Headline

**The most adoptable calibration pattern found is the try-before-trust reviewer interview (T2):** before you trust any reviewer — model, subscription, or prompt — run it once against a decoy set of true claims mixed with logic-inverted fakes, with the bar set in advance, and measure discrimination. It costs under a dollar, takes an afternoon, needs no infrastructure, and it demonstrably changes decisions (a frontier model was rejected on this basis; Matsuzaki, dev.to, 2026-07-14/24). For higher stakes, upgrade to the answer-key calibration run — freeze code with known defects, plant a canary, score the reviewer against the key (T1, Shopware, 2026-05-08) — which also doubles as the honest way to measure any reviewer's recall. Both patterns are harness-agnostic, and both directly answer the beginner's first question: "can I trust this reviewer at all?" — before spending tokens or trust on it.

## (h) Sources

- https://www.shopware.com/en/news/an-experiment-with-ai-agents/ — Martin Bens (Principal SWE, Shopware), 2026-05-08. G1/G2/G3/G4: measured answer-key experiment; resumed reviewer 42k vs 137–312k tokens; model routing; canary; settled-findings ablation.
- https://getclaudekit.com/blog/guide/agents/verification-loops — ClaudeKit, 2026-07-16. G1: fresh-reviewer-per-round recommendation (T3, vendor-adjacent).
- https://blog.cloudflare.com/ai-code-review/ — Cloudflare, 2026-04-20. G1/G6: incremental re-review aware of previous findings at scale; 131,246 runs / 48,095 MRs.
- https://abysim.com/blog/context-isolation-in-ai-code-review — Abysim, 2026-02-22. G1: per-iteration context isolation catches new problems.
- https://github.com/mikhail-angelov/herdr-review-loop — G1: wiped sessions + durable review-summary.md.
- https://www.mindstudio.ai/blog/automated-code-review-multiple-ai-agents — MindStudio, 2026-04-24. G1/G6: fresh sessions; context rot across PRs (T3/T4).
- https://dev.to/ryosuke_matsuzaki_64cd24a/getting-ais-to-review-each-other-was-easy-the-hard-part-was-measuring-whether-i-could-trust-the-4o55 and https://dev.to/ryosuke_matsuzaki_64cd24a/before-you-run-the-ai-debate-200-times-measure-the-die-temperature-diversity-vs-vendor-diversity-587j — Ryosuke Matsuzaki, 2026-07-14/24 (+ comment 07-29). G2/G4/G6: decoy-exam interview (Gemini failed, <$1); die bias; batch/async review layer.
- https://yaqinhei.com/blog/fail-closed-critic-design — Yaqin Hei, 2026-05-17. G2/G4: critic eval set (miss <1%, over-escalation <20%); rules vs LLM critic; "70% vs 95%" is automation rate, not model quality.
- https://github.com/withmartian/code-review-benchmark — Martian, 2026. G3: benchmark structure (T1); headline numbers unverified this session.
- https://arxiv.org/abs/2603.12123 — Song Tae-Eun, 2026-03-12. G3/G5: CCR controlled experiment (F1 28.6 vs 24.6, p=0.008; SR2≈SR).
- https://arxiv.org/abs/2603.16244 — Song Tae-Eun, 2026-03-17. G1/G5: D-CCR — single-pass optimal; fresh second review worst; false positive pressure.
- https://arxiv.org/abs/2404.13076 — Panickssery, Bowman & Feng, 2024. G4/G5: self-preference bias (T1).
- https://arize.com/blog/should-i-use-the-same-llm-for-my-eval-as-my-agent-testing-self-evaluation-bias/ — Sanjana Yeddula, Arize, 2025-10-08. G4/G5: measured self-evaluation bias with human ground truth.
- https://antigravitylab.net/en/articles/agents/ai-code-review-agent-comment-fatigue-actioned-rate-field-notes — Masaki Hirokawa, 2026-07-04. G3: FP 7%, fatigue 58%, per-severity actioned-rate thresholds.
- https://tianpan.co/blog/2026-05-05-llm-code-review-production-diff-pipeline and https://tianpan.co/blog/2026-04-17-ai-code-review-at-scale-false-positive-trap — Tian Pan, 2026. G3: 20% actionable "on a good day"; FP 5–15%; action rate >55% for net-positive.
- https://virtuslab.github.io/visdom-code-review/reference/metrics/ — Visdom. G3: FP <15%, actionable >80% targets (T3/T4).
- https://www.tenki.cloud/blog/ai-code-review-roi-metrics — Tenki. G3: FP >30–40% serious (T3).
- https://towardsdatascience.com/the-llm-judge-that-kept-agreeing-with-itself/ — Priyansh Bhardwaj, 2026-08-20. G3/G4: same-family judge incident; different-family fix; judge-human agreement low-to-mid 80s.
- https://www.agentnotebook.dev/tutorials/llm-as-a-judge , /tutorials/ai-agent-testing , /tutorials/agentic-workflow-evaluator-optimizer-python — Ren Okabe, 2026-07-20/22/29. G4: cheapest-tier judge "often enough to grade a rubric" (T3).
- https://mainbranch.dev/articles/stop-paying-for-the-same-tokens-twice/ — Andrea Griffiths, 2026-05-29. G6: measured caching/digest cost cuts ($1.32 → $0.45/$0.49).
- https://github.github.com/gh-aw/reference/cost-management/ — GitHub docs. G6: batch-to-cache guidance (T3/T4).
- https://github.com/darkroomengineering/cc-settings/blob/main/skills/review-batch/SKILL.md — G6: batch review in one sitting (T2/T3).
- https://github.com/chrisarmitt/agent-review-orchestrator — G6/G1: split pipeline 25–40% of naive token cost; devil's-advocate fresh-context challenge (T2/T3).
- https://aipatternbook.com/llm-as-judge — G2/G3: calibrate against 50–100 human labels; ~80% judge-human agreement (T3).
- https://futureagi.com/blog/ai-code-review-tools-precision-recall/ — 2026-08-10. G2/G3: self-scoring method; false-discovery vs false-positive distinction.
- https://doi.org/10.20944/preprints202601.0892.v1 — Andrew Brilliant, 2026-01-13. G5: correlated-error theory, no empirics (T3).
- https://www.augmentcode.com/guides/adversarial-code-review — Augment, 2026-07-24. G5: vendor guide; unverified study citation (T4).