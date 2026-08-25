# Wave 02 — Writing and Document Review Agents

**Research angle:** Subagents reviewing prose, docs, reports, READMEs, changelogs, and other non-code artifacts produced elsewhere: triggers, reviewer prompts (audience, purpose, style guide), rubrics/checklists, reported outcomes.

**Seed note (verbatim):**
> Subagent Review
> When creating something, stop allowing agents to review their own products. Always instruct agents to spawn review subagents on their work. (say 'spawn a read-only reviewer in a separate context; do not trust your own summary')

---

## Q1. Distinct patterns practitioners describe (trigger / procedure / evidence)

**P1 — Read-only reviewer subagent in a fresh context (the core pattern).** Trigger: draft complete, before publish/sharing. Procedure: the writer saves the artifact to a file; the orchestrator spawns a reviewer that reads the file with a clean context and no memory of how it was produced; the reviewer reports findings only and must not rewrite. Evidence: Zeikar (2026-05-04) runs a 3-agent doc pipeline (`content-writer`, `content-reviewer`, `consistency-checker`) where "the saved file is the handoff boundary" and the reviewer "reads the file fresh with its own context"; he reports that a single agent drafting *and* self-checking "finds nothing, or it finds nits that don't matter" and collapses by document ten (**T2**). ClaudeKit (vendor, 2026-07-16) describes the same mechanism — "the reviewer can't rationalize a mistake it never witnessed being made" — and scopes the reviewer read-only because "a reviewer that can edit will quietly 'fix' things instead of flagging them" (**T4** evidence, but a precise mechanism description). Ken Muse (2026-05-08) adds the adversarial framing variant: instructions like "assume the plan and implementation are wrong" so the critic "has no prior investment in the output" (**T2**).

**P2 — Parallel one-dimension-per-reviewer.** Trigger: review of a multi-dimensional artifact (e.g., blog post). Procedure: orchestrator spawns N reviewers in parallel, each with a tailored checklist (technical accuracy; writing quality; SEO). Evidence: Ken Muse reports asking for "three subagents" to review a post and getting three independent reports covering "ground a single pass would have missed," with the orchestrator's decomposition producing "more precise, targeted instructions" than the original request (**T2**).

**P3 — Writer–editor revision loop with structured verdicts.** Trigger: draft exists; loop runs until approval, human stop, or round cap. Procedure: writer drafts/revises; editor returns a machine-parseable verdict (`VERDICT: APPROVED` / `VERDICT: REVISE` + numbered feedback); unparseable output defaults to REVISE; human-in-the-loop check each round; per-call token/cost logging. Evidence: Daehnhardt (2026-07-13) implements this in Python with interchangeable backends; defaults to REVISE on ambiguous output deliberately — "an unnecessary revision round is cheaper than publishing a draft that a confused editor waved through" (**T2**).

**P4 — Sequential specialist chain + merged report.** Trigger: pre-publish "second opinion." Procedure: reviewer A (readability/structure/audience fit) then reviewer B (technical correctness, commands, claims), B receives A's review as context; outputs merged into a prioritized action list and revised draft; dated run folder per review. Evidence: Suedbroecker (2026-06-28) built this as a local CLI (Claude then Codex) for his own blog; "it does not replace my review process. It gives me structured feedback" (**T2**).

**P5 — Read-only reviewers + integrator agent.** Trigger: improving one shared artifact with multiple agents. Procedure: fact-checker, expression reviewer, and structural reviewer run in parallel on the same snapshot, return only a "Unified Feedback List" (columns: source/severity/location/before/after/rationale); an integrator agent dedupes, resolves conflicts, and applies all edits in batch; human does the final read. Evidence: tomokusaba (2026-04-26) on GitHub Copilot CLI; motivation is preventing write conflicts and "natural language impressions" becoming "diff candidates" (**T2**).

**P6 — Rubric-gated quality gate with pass/fail routing.** Trigger: doc complete, before publish. Procedure: reviewer scores the artifact on fixed dimensions with explicit thresholds; score below minimum routes back to the writer with targeted fix instructions; pass routes to publish. Evidence: iamraghuveer (2026-04-25) — five 0–100 dimensions (technical accuracy 80-min, depth 75, formatting 90, SEO 80, code quality 85), weighted average, Pydantic-validated JSON report; revision prompt cites failed dimensions only, "reduces API cost (the writer does not redo the research)" (**T2**). Zeikar's pass/polish/rewrite gate with "if the verdict is borderline, grade down" (**T2**).

---

## Q2. Triggers and reviewer context

**Triggers (all sourced):** pre-publish (Suedbroecker; Ken Muse; lyndonkl/claude editor agent: "before any draft moves to `corpus/published/`"); draft complete (Daehnhardt's loop starts with a draft); before release / after bulk doc generation / periodic doc-health checks (eliteai.tools `doc-quality-review` skill: "Before releases… After bulk doc generation… Periodic quality check"); before trusting an agent's work (ClaudeKit); writer-agent stop event (Zeikar's orchestrator branches on the reviewer's verdict).

**Context the reviewer receives:** (1) the artifact (file path or text — Zeikar: file as handoff boundary); (2) audience + doc type (eliteai: "identify the audience… identify the doc type — reference, tutorial, guide, explanation, or README" — these change dimension weights); (3) style guide / brand rules / glossary / voice profile (lyndonkl editor loads `voice-profile.md`, `style-guide.md`, `analogy-catalog.md`, `glossary.md` every run and refuses to review if any is missing; Glean (vendor, 2026-06-01): brand voice must be "specific, testable rules… approved terminology, sentence patterns, reading-level targets"); (4) rubric + thresholds (iamraghuveer); (5) prior feedback (Daehnhardt: revise-against-feedback mode; Zeikar: reviewer-specified concrete patch is applied without re-review); (6) machine-parseable output contract so the orchestrator can branch (Zeikar's `<!-- REVIEW_SUMMARY overall: pass|polish|rewrite … -->`); (7) verification evidence rather than full files (Kohler, 2026-06-29: reviewer receives "a compact write manifest and verification evidence instead of full file contents").

---

## Q3. Reported evidence (with tiers)

- **T1 — agent-style benchmark (yzhao062/agent-style):** 10 fixed prose tasks × 2 generations × 2 conditions on flagship models; with the 21-rule style ruleset loaded at generation time, mechanical "AI-tell" violations fell 47% (Claude Opus 4.7: 88→47), 46% (GPT-5.4 via Codex CLI: 48→26), 86% (Gemini 3 Flash: 65→9); GitHub Copilot CLI showed no change (52→52, treated as noise control). Caveats self-disclosed: covers 7 of 21 rules (mechanical only), directional not statistically significant, 40 calls per model arm.
- **T1 — FeedbackWriter RCT (Lu et al., CHI 2026, arXiv:2602.16820):** N=354 students, 11 TAs, 1,366 essays, switch-back randomization; students receiving AI-mediated feedback (AI suggestions vetted by human TAs) produced significantly higher-quality revisions than human-only feedback (Cohen's d = 0.50 ≈ 50th→70th percentile; ~5% higher revision quality, p<0.001). TAs agreed with 88% of AI rubric judgments and corrected 12% (U-Michigan news release). This is human-plus-AI review, not pure agent review.
- **T1 — Paper research report (content.paper.co):** human-expert-rated comparison of 514 AI/human feedback pairs: AI feedback had 28.7% more inquiry-based comments, 18.5% fewer encouraging comments, 14.3% more specific comments; AI never produced standalone praise (vs 8.9% human); AI comments were 5.5% inaccurate (incl. hallucinated mistakes and style rules) vs <1% for humans.
- **T1 — EdWorkingPapers ai25-1193 (qualitative):** LLM feedback vs 12 expert teachers: LLMs stayed "stuck at the sentence level," gave generic/perfunctory praise ("Good start"), sometimes contradictory feedback; teachers gave multi-level, dialogic feedback.
- **T2 — cost numbers:** Kohler measured one 3-file subagent run at 35,005 tokens, over half consumed by the reviewer (plan+proposal duplicated in system and user messages) — his fix ("divide judgment, not work") cut reviewer input to a compact manifest. Daehnhardt tracks per-round cost and runs a cheap local writer (Qwen2.5-7B) with a stronger editor model, "reviewing is the opposite: the editor reads a lot and writes very little."
- **T3 — time-saved claims:** AI Career Lab rubric example claims "total review and correction time: under three minutes" for one clinical note; Digital Applied claims 12-point rubric scoring takes 8–12 minutes per piece. Anecdotal, self-reported; no controlled time studies found for doc-review agents specifically.
- **No sourced evidence found** for before/after quality comparisons of agent-reviewed vs non-reviewed published docs (only the education-domain RCTs above), and no vendor-independent measurements of "editing time saved."

---

## Q4. Failure modes reported

1. **Generic praise / sycophancy:** EdWorkingPapers (LLMs' "Good start," perfunctory praise); Paper report (0% standalone praise despite prompts requesting compliments — "including an instruction within a prompt does not guarantee the expressed output"); PAIRR students found AI feedback "sometimes too general or 'surface-level.'"
2. **Voice-erasing / over-rewriting:** the single most common practitioner guardrail is "never rewrite the draft — produce findings" (eliteai skill's anti-pattern list; lyndonkl editor: "You never rewrite the draft," max 2 rewrite options per flag; tomokusaba read-only constraint; ClaudeKit). HN "Slop Cop" thread (item 47806845): critics call pattern-flagging tools "performative self-censorship," "the cure is worse than the disease," and "It's not a good argument for why I should rewrite a particular sentence in context."
3. **Hallucinated improvements / false flags:** Paper report (5.5% inaccurate comments incl. hallucinating mistakes); voice-humanizer SKILL catalogs "hallucinated data / fake citations" as a top tell; HN thread: "False positives are a given"; agent-style includes a rule for citation discipline as "the critical one."
4. **Review missing the document's actual purpose:** PAIRR students: AI feedback "did not match their purpose"; one student: "too general and sometimes does not make sense"; EdWorkingPapers: LLM feedback missed global structure while "correcting" sentences. Glean (vendor) claims require citations/source references "to catch hallucinations before they reach an editor's desk" (product claim, not evidence).
5. **Self-review bias (the pattern's raison d'être):** ClaudeKit, Ken Muse, Zeikar, nxflo all describe it; Zeikar: "The writer is attached to its draft… asking it to find what's wrong is asking it to disagree with itself."
6. **Role-boundary crossing:** Zeikar's sharpest reported failure — a consistency-checker agent "helpfully" writing missing content, bypassing the reviewer, so "the harness silently grows documents that nobody graded"; fixed with an explicit fence.
7. **Over-compliance with style guides / rule absolutism:** HN Slop Cop thread ("these tools only narrow the scope of our expression"); agent-style ships an Orwellian escape hatch ("Break any of these rules sooner than say anything outright barbarous") and rules flagged as "style preferences are not findings" (eliteai). No controlled study found; practitioner-invented mitigations are the evidence.

---

## Q5. Agent review vs human editing / peer review

- **Education RCTs say AI feedback (human-vetted) can beat human-only feedback** on revision outcomes (d=0.50, FeedbackWriter), with AI feedback rated more actionable and supportive of independent learning — but the design keeps humans in the loop (88% agreement, 12% corrected).
- **AI feedback quality is more specific but less warm and more error-prone:** Paper report numbers above (specificity +14.3%, encouragement −18.5%, inaccuracy 5.5% vs <1%).
- **Practitioner consensus: agent review supplements, not replaces, human judgment.** Suedbroecker: "the tool does not replace my review process"; tomokusaba: "the most important thing is that a human reads the artifact again at the end and takes responsibility"; Daehnhardt keeps a human stop button; PAIRR students found peers better at context/audience while AI was more constructive and actionable — and when both agreed, students were reassured.
- HN practitioner (Slop Cop thread): a final "critical review of all produced content as a quality gate… catches a lot of baseless claims, and other slop" (T3, single account).

---

## Q6. Rubrics, checklists, style guides

Rubric-driven review is the dominant pattern for technical docs and the most-reported as *reliable*:
- iamraghuveer (T2): rubric makes the gate "deterministic enough to trust — without a rubric, two reviewer runs on the same post can produce different pass/fail decisions"; provides a calibration procedure (score 10–20 existing posts, adjust dimension descriptions; "depth" is the common calibration problem).
- Zeikar (T2): three-tier verdict with "if borderline, grade down" to stop rubric inflation.
- Digital Applied (T3, agency blog): 12-point/120-scale rubric, publish ≥84, 60-day calibration sessions claiming inter-reviewer variance <4 points; "without calibration, two reviewers will score the same piece 8–12 points apart within a quarter."
- eliteai skill (T2/T3): five dimensions with weights varying by doc type (e.g., readability weight differs for reference vs tutorial).
- FeedbackWriter RCT (T1, education): rubric-anchored AI suggestions produced better outcomes than rubric-less human feedback — the strongest evidence that *explicit criteria improve review output*, though in a human-vetting setup.
- Reported in PAIRR: Steiss et al. 2024 found ChatGPT feedback comparable to human feedback "when criteria are used" (secondary citation — not read directly).

Checklists alone are reported insufficient: Zeikar — "A nine-item checklist still ships broken anchors. A fifteen-second script doesn't" (agents self-report "checked, all valid" while wrong); his fix is a deterministic link-check hook that hard-fails the agent (T2).

---

## Q7. Costs and adoptability barriers for a beginner

- **Token cost is real and can surprise:** Kohler's measured 35k-token run with >50% in the reviewer (T1 measurement of a T2 workflow); mitigations: compact manifests, read-only tools, cheaper/stronger model split (Daehnhardt), revision prompts that don't redo research (iamraghuveer).
- **Prompt-crafting effort:** reviewers need concrete checklists; Ken Muse notes the orchestrator's decomposition is a "lossy compression step" — if it drops a constraint, the reviewer never knows. Output contracts (Zeikar) and JSON schemas (iamraghuveer, Kohler's `response_format`) are required when orchestrators branch on verdicts — "telling an agent to 'include the grade clearly' isn't enough."
- **Calibration effort:** 10–20 posts (iamraghuveer), periodic calibration sessions (Digital Applied) to keep scores aligned with judgment.
- **Evaluating review quality is itself hard:** HN threads show reviewers disagree about what good review is (false positives "a given"); PAIRR: a quarter of student reflections expressed skepticism of AI feedback.
- **Privacy:** Suedbroecker's motivating barrier — unpublished drafts are sensitive; his local-first CLI still sends drafts to provider APIs; mock mode exists for testing (T2).
- **Tooling fragility:** CLI-version dependence (Suedbroecker), structured-output schema enforcement (Kohler), hook setup (Zeikar).
- No sourced per-document dollar figures found.

---

## Q8. Document-type differentiation

Practitioners do differentiate:
- **Technical docs / reference / READMEs / specs / ADRs:** review agents are common; the pattern is rubric+threshold gates, claim/code verification, consistency checks (eliteai dimension weighting by doc type; Zeikar's 33-doc interview guide; tomokusaba explicitly generalizes to "design documents, READMEs, specifications, and ADRs"; Suedbroecker's Codex reviewer checks commands/architecture claims).
- **Technical blog posts:** the most-written-about type (Ken Muse, Daehnhardt, iamraghuveer, Suedbroecker) — multi-dimensional review (accuracy, style, SEO/formatting).
- **Creative/personal prose and newsletters:** the pattern shifts to voice preservation — "never rewrite, flag only, quote the voice profile" (lyndonkl's editor agent; timsimpsonjr/copydesk `prose-review.md` with banned-phrase hard fails + advisory table; dannwaneri's voice-humanizer with a corpus-based voice fingerprint; hannsxpeter/humanizer with "faithfulness over liveliness" guards against inventing facts during rewrites).
- **Reports/essays (education):** the academic evidence base (FeedbackWriter, Paper, PAIRR, EdWorkingPapers) — criteria-based review comparable or superior to human in specificity/actionability, worse in tone/encouragement and accuracy.
- Pattern difference: technical docs get **gates and scores** (pass/fail routing); personal prose gets **flags and advisories** (voice drift, AI tells); both share the read-only, fresh-context reviewer.

---

## Workflow candidates (trigger / procedure / evidence)

**W1 — Fresh-context read-only reviewer gate (adoptable now).** Trigger: artifact complete, pre-publish/share. Procedure: writer saves file; orchestrator spawns reviewer with only (artifact, audience, doc type, rubric, style guide, output-contract for verdict); reviewer returns findings + verdict, never edits; human applies or routes. Evidence: Zeikar T2; ClaudeKit T4; Ken Muse T2. Tradeoffs: lossy context compression; needs output contract if automated routing.
**W2 — Parallel one-dimension reviewers.** Trigger: multi-dimensional artifact. Procedure: N reviewers in parallel with tailored checklists; merge reports. Evidence: Ken Muse T2. Tradeoff: orchestrator blind spots become coverage gaps.
**W3 — Writer–editor loop with parseable verdict + human brake.** Trigger: draft complete. Procedure: draft → review → REVISE/APPROVED verdict → revise → repeat; human stop; cost log. Evidence: Daehnhardt T2; default-to-REVISE asymmetry. Tradeoff: token burn if no round cap.
**W4 — Rubric-scored quality gate with calibration.** Trigger: publish/release. Procedure: score fixed dimensions vs thresholds; below-min routes to targeted revision; calibrate on 10–20 exemplars. Evidence: iamraghuveer T2; Digital Applied T3; agent-style bench T1 (mechanical rules reduce violations 46–86% directionally). Tradeoff: rubric quality limits gate quality; drift needs recalibration.

---

## Headline

Three most adoptable patterns, by evidence: **(1) the fresh-context, read-only reviewer gate** — the closest thing to a consensus mechanism, backed by T2 practitioner accounts (Zeikar, Ken Muse) and consistent with the seed note; **(2) rubric-scored gates with calibration** — T2 accounts (iamraghuveer) plus T1 directional benchmark evidence (agent-style) and T1 education RCT support for criteria-based review (FeedbackWriter); **(3) the writer–editor loop with a parseable verdict and a human brake** — T2 (Daehnhardt), cheapest to start (two prompts, one file). All three share the same load-bearing idea as the seed note: independence of the reviewer's context, read-only scope, and a human owning the final decision.

## Open gaps / follow-ups

1. **No vendor-independent time-saved data** for doc review agents (only T3 self-reports). Suggested: run a small within-repo experiment (with/without reviewer, word-level edit counts, time to publish).
2. **No direct studies of rubric vs no-rubric review reliability for agent review** outside education (FeedbackWriter) and the agent-style mechanical bench. Follow-up: benchmark same doc corpus under rubric vs free-form reviewer instructions, measure verdict stability across runs.
3. **Voice-erasure / over-compliance** documented only as practitioner guardrails and HN criticism; no measurement. Follow-up: diff-level analysis of accepted vs rejected reviewer suggestions.
4. **Cost per document** reported only as token counts (Kohler) and per-round tracking (Daehnhardt); no normalized $/1,000-word figures found.

## Sources

- kenmuse.com/blog/multiple-subagents-the-surprising-reasons-it-works/ (Ken Muse, 2026-05-08) — P1/P2 patterns, adversarial framing, lossy compression.
- zeikar.dev/blog/three-agents-one-document/ (Zeikar's Lab, 2026-05-04) — 3-agent doc pipeline, output contracts, borderline-grades-down rule, role fences, hook verification.
- daehnhardt.com/blog/2026/07/13/writer-editor-agents/ (E. Daehnhardt, 2026-07-13) — writer–editor loop, VERDICT parsing, human-in-loop, cost tracking, cheap-writer/strong-editor.
- suedbroecker.net/2026/06/28/building-a-local-first-blog-review-agent-chain-with-claude-and-codex/ (T. Suedbroecker, 2026-06-28) — sequential two-reviewer chain, privacy barrier, mock mode.
- zenn.dev/tomokusaba/articles/a599cb645ca2c5 (tomokusaba, 2026-04-26) — read-only reviewers + integrator, Unified Feedback List schema, human final read.
- nxflo.io/blog/ai-quality-assurance-reviewer-agent (nxflo, 2026-03-28) — vendor; pattern description only (separate context/objectives/model config).
- getclaudekit.com/blog/guide/agents/verification-loops (ClaudeKit, 2026-07-16) — vendor; separate-context mechanism, read-only scoping rationale.
- paulkohler.me/blog/2026-06-29-subagent-orchestration/ (P. Kohler, 2026-06-29) — measured token costs (35,005; reviewer >50%), manifest-not-files fix.
- iamraghuveer.com/posts/reviewer-agent-scoring-rubric/ (2026-04-25) — rubric gate, JSON report, revision-prompt cost saving, calibration.
- eliteai.tools/agent-skills/doc-quality-review — rubric skill; triggers; dimension weights by doc type; anti-patterns.
- github.com/yzhao062/agent-style/ — 21-rule ruleset; measured bench (47%/46%/86% reduction; caveats); escape hatch.
- github.com/lyndonkl/claude/blob/main/agents/editor.md — voice-gate editor agent: two-pass, never rewrites, verdict tiers, voice profile.
- github.com/timsimpsonjr/copydesk/blob/main/agents/prose-review.md — prose review agent: hard-fail banned phrases, advisory table, 24 AI-tell patterns.
- github.com/dannwaneri/voice-humanizer/blob/main/SKILL.md — corpus-based voice fingerprint; hallucination-tell catalog.
- github.com/hannsxpeter/humanizer — faithfulness-over-liveliness guards against invented facts in rewrites.
- news.ycombinator.com/item?id=47806845 (Slop Cop thread) — failure-mode criticism (false positives, self-censorship); one quality-gate success account.
- news.ycombinator.com/item?id=42909042 ("Why does AI slop feel so bad") — voice/averageness critique context.
- arxiv.org/abs/2602.16820 (Lu, Ju, Dudley, Sano, Wang; CHI 2026) — FeedbackWriter RCT, d=0.50.
- news.umich.edu/ai-helps-instructors-give-better-feedback-but-cant-replace-them/ (2026-04-16) — 88% TA agreement stat.
- content.paper.co/hubfs/AI%20Research_Study%201_AI%20compared%20to%20human%20feedback.pdf — AI vs human feedback quality numbers (5.5% vs <1% inaccuracy etc.).
- edworkingpapers.com/sites/default/files/ai25-1193.pdf — LLM vs teacher feedback qualitative study (sentence-level, generic praise).
- frontiersin.org/journals/communication/articles/10.3389/fcomm.2025.1615752/full (2025-09-16) — PAIRR model; student perceptions; cites Steiss et al. 2024 (secondary).
- glean.com/perspectives/how-to-implement-an-ai-content-review-workflow (2026-06-01) — vendor; layered review order, testable brand rules, citation requirements.
- digitalapplied.com/blog/ai-content-quality-rubric-12-point-scoring-system (2026-04-26) — 12-point rubric, calibration protocol (T3).
- theaicareerlab.com/blog/human-review-rubric-ai-documentation (2026-03-30) — human rubric example with "under three minutes" claim (T3).
- newname.ai/products/hold-your-voice (2026-08-07) — vendor marketing; voice-score claims (used only to show product category, not as evidence).
