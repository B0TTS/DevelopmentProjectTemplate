# Research Findings — Creative-Brainstorm Skill

**Date:** 2026-07-12
**Session type:** Research phase (companion to the grill handoff)
**Companion artifact:** `b0ttsagent/handoffs/07-12-2026/creative-brainstorm-skill-design-grill.md` (the locked design spec)
**Status:** Research complete. Recommendation below. **No skill was built this phase.**

---

## TL;DR — Recommendation

**Build new via `write-a-skill`. No existing skill fits the locked spec well enough to adopt or adapt.**

The space is crowded — I found 20+ "creative ideation / brainstorm" skills, commands, and prompts. But every candidate misses the locked spec on at least one **load-bearing** design decision from the grill. The closest three are instructive but insufficient:

- **`scdenney/diverge-skills`** is the closest in *philosophy* (research-grounded via Ismayilzada et al. EMNLP 2025; "differ in mechanism, not vocabulary"; "at least one surprising"; diverge-before-select) — but it's a lightweight code-oriented "hold for selection" with no framing layer, no reasoning layer, only 3-5 options, and no per-option depth.
- **`brianharms/skill-propose`** is the closest in *contract shape* (4-part per-option: Approach/How-Works/Tradeoffs/Effort → ranked → "want me to go with one or combine?") and is already pi-compatible SKILL.md format — but it hard-locks 3 fixed philosophies (technique-locked), auto-crawls the codebase, and outputs exactly 3 options.
- **`ysskrishna/creative-thinking`** is the closest in *permissive spirit* + format (Agent Skills standard, "no fixed count," divergent triggers as a menu, blue-sky) — but it runs a fixed 4-phase procedure, converges to 3 top picks + parking lot (the spec keeps 8-10 ranked *open*), and has no reasoning/rejection layer.

Adapting any of these to the spec means rewriting its structure and adding two missing layers — at which point it is a new skill. The spec's combination of (a) principles-not-procedures, (b) in-chat no-auto-crawl, (c) the 4-layer contract, (d) 8-10 kept-open ranked, (e) illustrative-moves-never-forced exists in **no** single candidate. The research strongly *validates* the spec (several candidates independently re-derive parts of it) but does not *satisfy* it.

**Silver lining:** the research yielded a set of borrowable, evidence-backed ideas to fold into the build (§5).

---

## 1. The rubric (measured against the locked spec)

Each candidate was scored against the grill's load-bearing decisions. Criteria:

| Code | Criterion | Source |
|------|-----------|--------|
| **P1** | Principles, not procedures | Design philosophy |
| **P2** | Recommend-don't-direct (permissive tone) | Design philosophy |
| **P3** | Separate stable intent from volatile technique (not technique-locked) | Design philosophy |
| **P4** | Reasoning/transparency layer (gets *more* valuable as models improve) | Design philosophy |
| **P5** | Bounds, not counts | Design philosophy |
| **G** | In-chat, no auto-crawl grounding | Grounding default |
| **C1** | Framing layer (restate goal + shape being optimized for) | Output contract L1 |
| **C2** | Reasoning layer (varied / rejected+why / trade-off each optimizes) | Output contract L2 |
| **C3** | Ranked options, 8-10 kept open, per-option name/concept/why/strengths/stretches, defended ranking | Output contract L3 + Quantity + Qualities |
| **C4** | Next-move layer (invite user to pick a direction to deepen) | Output contract L4 |
| **Q** | Illustrative moves available, never forced | Illustrative moves |
| **F** | pi-compatible SKILL.md format (<100 lines, triggered description) | `write-a-skill` conventions |

Legend: ✓ clear pass · ⚠️ partial / mixed · ✗ clear miss · N/A not applicable.

---

## 2. Coverage (what was searched)

Searches run via `web_search_exa` (8 queries across the spectrum the handoff named):

1. Claude Code agent skill / slash command for creative brainstorming with ranked ideas + reasoning
2. Cursor AI rules / agent prompt for divergent ideation
3. GitHub open-source agent-skill prompt library for brainstorming
4. *LLM prompt template for ranked creative options with tradeoffs* — rate-limited, retried in batch 2
5. TRIZ inventive-principles prompt for AI agents — rate-limited (TRIZ surfaced via creativity-lite & creative-director-skill instead; covered)
6. SCAMPER / lateral-thinking prompt for AI ideation
7. Design-thinking ideation prompt for AI
8. Copilot agent instructions for brainstorming — rate-limited (Copilot ecosystem duplicates Claude Code/Cursor findings; low marginal value, skipped)

Deep-reads via `web_fetch_exa` (full SKILL.md / prompt text) for the candidates that mattered most: `neurofoo/scamper`, `ysskrishna/creative-thinking`, `ysskrishna/lateral-thinking`, `brianharms/skill-propose`. (`scdenney/diverge-skills` file paths 404'd; its README was captured in full by the search result, which is sufficient.)

**Coverage is sufficient to support the recommendation.** Two rate-limited queries were either retried successfully or covered via cross-pollination. The candidate space converged fast: after ~15 finds, new results were variants of already-seen patterns (technique-locked, rigid-procedure, multi-agent-heavy, or prompt-not-skill).

---

## 3. The closest candidates — head-to-head

| Criterion | `diverge-skills` | `skill-propose` | `creative-thinking` | Creative Concept Gen¹ | `adhd-claude` | `creativity-lite` |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| **P1** principles-not-procedure | ⚠️ | ✗ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **P2** recommend-don't-direct | ✓ | ⚠️ | ✓ | ⚠️ | ⚠️ | ⚠️ |
| **P3** not technique-locked | ✓ | ✗ | ⚠️ | ✗ | ⚠️ | ✗ |
| **P4** reasoning layer | ✗ | ⚠️ | ⚠️ | ⚠️ | ✓✓ | ⚠️ |
| **P5** bounds not counts | ⚠️ | ✗ | ✓ | ⚠️ | ⚠️ | ⚠️ |
| **G** in-chat no-crawl | ✓ | ✗ | ✓ | ✓ | ⚠️ | ✗ |
| **C1** framing | ✗ | ✗ | ⚠️ | ✓ | ✗ | ⚠️ |
| **C2** reasoning (rejected+why) | ✗ | ✗ | ✗ | ⚠️ | ✓ | ⚠️ |
| **C3** ranked 8-10 open + per-option | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| **C4** next-move | ⚠️ | ✓ | ✓ | ✓ | ⚠️ | ⚠️ |
| **Q** moves never forced | N/A | ✗ | ⚠️ | ✗ | ⚠️ | ✗ |
| **F** pi SKILL.md format | ⚠️ | ✓ | ✓ | ✗ | ✗ | ⚠️ |

¹ *Creative Concept Generator* (`aj-geddes/useful-ai-prompts`) — a prompt template, not a skill.

**No column clears the row.** Every closest candidate fails ≥3 load-bearing criteria. The failures cluster on exactly the decisions the grill locked: technique-locking (P3), missing reasoning layer (P4/C2), auto-crawl (G), and converging-to-3 instead of keeping 8-10 open (C3).

---

## 4. Candidate inventory (all finds, grouped by rejection reason)

### 4a. Real agent skills — closest format, partial fit

- **`scdenney/diverge-skills`** — *Closest in philosophy.* Research-grounded (Creative Preference Optimization, EMNLP 2025): "approaches differ in underlying mechanism, not just vocabulary"; "≥1 surprising, ≥1 novel"; diverge-before-select; labels `[Novel]/[Surprising]/[Diverse]/[Conventional]`. Claude Code + Codex. **Miss:** 3-5 options, hold-for-selection (not ranked), no framing/reasoning layers, no per-option strengths/stretches, code-implementation-oriented.
- **`brianharms/skill-propose`** — *Closest in contract shape + format.* 3 parallel subagents → 4-part per-option (Approach/How-Works/**Tradeoffs**/Effort) → ranked → winner-or-hybrid note → "Want me to go with one or combine?". Self-contained pi-compatible SKILL.md. **Miss:** 3 fixed philosophies (technique-locked), "read the actual codebase" (auto-crawl), exactly 3 options, no framing/reasoning layers.
- **`ysskrishna/creative-thinking`** — *Closest in permissive spirit.* Agent Skills standard; rich triggered description incl. "Skip when…"; "no fixed count unless user asks"; divergent triggers as a *menu* (analogy/constraint-flip/user-fantasy/time-shift/scale-shift); F/N/W tags; Harvest = top-3 + next-step + parking-lot. **Miss:** fixed 4-phase procedure (Prime→Diverge→Connect→Harvest); converges to 3 (spec keeps 8-10 open); no reasoning/rejection layer; no per-option strengths/stretches.
- **`ysskrishna/lateral-thinking`** — *Different scope.* de Bono provocations / concept fan for breaking a sticky pattern, not general divergent ideation. Output `Candidates` tagged near-term/stretch/experimental. **Use:** a *complement* to creative-brainstorm, not a replacement. Not scored above.
- **`neurofoo/scamper`** — *Technique-locked.* Clean Agent-Skills-standard SKILL.md, but the entire method IS SCAMPER's 7 prompts in fixed order. Violates P3 directly. Output is a flat per-lens table + "Idea Harvest" with feasibility/impact + wild card — no framing, no ranking defense, no reasoning layer. **Silver lining:** SCAMPER's 7 lenses are an excellent *illustrative-moves* resource (§5).
- **`johnlindquist/claude` brainstorm** — A grab-bag of `gemini` CLI invocations (generate-10, expand, six-hats, reverse, evaluate, combine). Tool-specific (`gemini` shell-outs), technique-grab-bag, not principles. Reject.

### 4b. Heavy multi-agent / orchestration — wrong weight class

These are strong on reasoning but architecturally incompatible with a lightweight in-chat skill (parallel subagents, Agent SDK, web research, file journals). All violate the in-chat grounding default and "principles not procedures."

- **`bhtru/adhd-claude`** — *Strongest reasoning/transparency.* Tree-of-thought w/ pruning via parallel Agent SDK branches under cognitive frames; scores novelty/viability/fit; **clusters by angle not surface keywords**; **trap-list with a mechanistic reason each**; flags non-obvious-but-viable; deepens top-K with load-bearing-risk + first-concrete-step. **Miss:** heavy (npm lib + CLI + Agent SDK, parallel `query()` calls), code/agent-loop oriented, not lightweight in-chat.
- **`Luigigreco/creativity` (Creativity Lite)** — *Strongest diversity-quality.* Research-backed (10 papers); fixation detection + constraint diversification (TRIZ vs Design-by-Analogy) + incubation reset; diversity metric triggers a defixation round. **Miss:** technique-locked (TRIZ/Analogy fixed), web-research auto-crawl, 2 parallel agents.
- **OrchestKit `brainstorm`** — 7-phase, parallel agents, modes, 0-10 scoring across 7 weighted dims, devil's advocate, trade-off table, **"Considered but excluded" section**, writes to experiment journal. **Miss:** very rigid/heavy, auto-crawls codebase+memory graph+journal, writes files.
- **`bladnman/ideation_team_skill`** — Multi-agent team (Arbiter/Free-Thinker/Grounder/Writer/Explorer/Image/Presentation/Archivist), depth tiers, vision docs + PDFs + PPTX. Massively over-engineered for an option-generation skill. Reject.
- **`Qnurye/diverge`** — 6-phase state machine, 7 agents, emits launcher scripts per approach + worktrees. Divergent *planning* ending in implementation, not ideation. Wrong scope.
- **`accaxx123/relay-brainstorm`** — 6 fixed expert roles incl. devil's advocate → synthesized recommendation + alternatives + risks + next steps. Multi-perspective is a *technique* (P3 violation). Has a SKILL.md + prompt files.
- **`create-genia-os` facilitate-brainstorming-session** — Multi-agent rounds, categorize, score, top 5-10 + rationale + next steps. Over-orchestrated. Reject.
- **`LingJueYa/Commons_Plan_Prompt`** — Parliamentary-style: clarify → 6-8 diverse → red/blue adversarial debate → MCDA scoring → ADR doc. **Strong** on reasoning ("why each was eliminated/retained", "transparent rationale for every score"). **Miss:** code/development-focused, heavy (red/blue teams + MCDA + ADR), converges to one recommendation.

### 4c. Rigid procedure + fixed counts + files

- **`lyndonkl/claude` `brainstorm-diverge-converge`** — Diverge 20-50 → Cluster 4-8 → Converge top 3-5 + "document tradeoffs (why chosen, what deprioritized)" + runner-up ideas; writes `.md`, validates against a JSON rubric (Score ≥ 3.5). **Miss:** rigid 3-phase, fixed counts, writes file. (The "deprioritized + runner-up" idea validates the spec's reasoning layer.)
- **`Intense-Visions/harness-engineering` `ideate`** — "Type: rigid"; grounded in STRATEGY.md (auto-crawl); fixed `(impact × confidence) ÷ effort` 1/2/3 scoring with bounded tiebreaker; per-idea fields (premise/persona/complexity/key_risk/impact/confidence/effort); strongest-objection critique; writes `docs/ideation/<slug>-date.md`. **Miss:** rigid + fixed formula (violates P1+P5), auto-crawl + writes files (G). Strong on ranking+objection, wrong philosophy + grounding + harness.

### 4d. Prompt templates (not skills)

- **`aj-geddes` Creative Concept Generator** — *Closest prompt to the contract + qualities.* Reframe → 5-8 concept territories → develop 2-3 → evaluate (strengths/risks/fitness) → recommend + next step. Quality criteria explicitly require "genuine divergence… avoid variations on the same idea with different names" and "honest about trade-offs, not universally positive." **Miss:** a prompt not a skill; role prescribes techniques (lateral/SCAMPER/analogy); converges to 2-3 developed; advertising-leaning.
- **Tree-of-Thought Prompting (Lewis C. Lin)** — Role → Divergent (prescribed: reverse-assumptions/borrow-domains/extreme-scenarios/combine) → Analysis (strengths/weaknesses/effort/roadblocks/scenarios/probability/metrics) → Selection (rank + justify + refine + next-steps + KPIs). **Closest contract *shape*** but a single mega-prompt that prescribes techniques; 3 solutions; no framing/rejection layers.
- **`CorpusIQ/hermes` creative.md** — "[N] ideas across safe/differentiator/moonshot, each with one-line + why-it-might-work + biggest-risk + effort, then recommend 3." Per-option field shape ≈ spec's. Prescribes the 3-tier technique; converges.
- **`promptblackmagic` Personal Decision Engine** — Decision-making on existing options (weighted matrix + pre-mortem + regret-min + 10/10/10 + hidden-options + final call). Not ideation. Wrong scope.
- **SCAMPER prompts** (`aiflowchat`, `juuzt.ai`, `termo`, `AIPRM`, Cambridge AI EDAM) — All hard-code SCAMPER. Technique-locked. (The Cambridge paper confirms GenAI + SCAMPER produces average-but-not-excellent creativity and struggles with technical feasibility — supports the spec's preference for *principles* over a fixed technique.)

### 4e. Domain-specific

- **`smixs/creative-director-skill`** — Advertising-creative (Cannes/D&AD), 20+ methodologies (SIT/TRIZ/SCAMPER/Bisociation), 571-campaign library, 6 weighted criteria, recursive refinement, Kill-Your-Darlings, Pre-Mortem. Domain-locked to advertising. (Kill-Your-Darlings + Pre-Mortem are borrowable reasoning concepts.)

---

## 5. Borrowable ideas for the build (the value-add)

The research didn't find a fit, but it found **evidence-backed building blocks** to fold into the new skill. These reinforce — not replace — the locked spec.

**For the "Qualities" the output must clear:**
- *Diversity across independent dimensions* — `diverge-skills` phrases it sharpest: **"differ in underlying mechanism, not just vocabulary."** `adhd-claude` operationalizes it: **"cluster by angle, not surface keywords."** Both validate the spec's "options shouldn't be variants of one idea." The spec could name this quality in those terms.
- *Novelty over safe variants* — `diverge-skills` requires **"≥1 [Surprising], ≥1 [Novel]"**; `adhd-claude` flags a **`nonObviousPick`** explicitly. Validates the spec's novelty preference; the build could require ≥1 option that "violates the obvious assumption."
- *Light reality-check* — `skill-propose`'s per-option **Tradeoffs** field and `Commons_Plan`'s **"fatal flaw identification"** are clean models for the spec's "stretches/risks" per option.

**For the "Reasoning" layer (L2):**
- *Rejected options + why* — `adhd-claude`'s **trap-list "each trap with the reason it's a trap"** and `Commons_Plan`'s **"why each was eliminated/retained"** and `OrchestKit`'s **"Considered but excluded"** section all independently re-derive the spec's reasoning layer. Strong evidence this layer is the differentiator that gets more valuable as models improve (matches P4).
- *Defended ranking* — `skill-propose`'s "brief note if one is clearly best or a hybrid would be ideal" and `creative-director-skill`'s **Kill-Your-Darlings** ("argue against your own favorite") are lightweight ways to defend a ranking without a rigid scoring formula.

**For "Illustrative moves" (never forced):**
- *SCAMPER's 7 lenses* (substitute/combine/adapt/modify/put-to-other-use/eliminate/reverse) map almost 1:1 onto the spec's illustrative-move kinds (import-a-mechanism, invert-the-goal, remove-a-constraint, vary-a-dimension). They're an excellent ready-made *menu* for the "available resource, opportunistic" layer — explicitly never forced.
- *`creative-thinking`'s divergent triggers* (analogy/constraint-flip/user-fantasy/time-shift/scale-shift) are a second clean menu, complementary to SCAMPER.
- The build can present these as "kinds of moves that satisfy the qualities" and let the model decide per-run whether to draw on them — exactly the spec's intent.

**For the per-option shape (L3):**
- `skill-propose`'s 4-part **Approach / How-It-Works / Tradeoffs / Effort** confirms the spec's **name / 1-2-sentence concept / why-it-fits / strengths / stretches-risks** shape is a well-trodden, readable contract.

**For the "Next move" layer (L4):**
- `skill-propose`'s closing question **"Want me to go with one of these, or combine ideas?"** is a clean, low-prescription model for the spec's "invite the user to pick a direction to deepen." Directly borrowable phrasing.

**For grounding the philosophy in research (optional, for the SKILL.md prose):**
- `diverge-skills` cites **Ismayzada et al., "Creative Preference Optimization," EMNLP 2025** — the "brainstorm-then-select" baseline shows meaningful gains from prompt engineering alone. The spec's "principles, not procedures" + "diverge-before-converge" stance is aligned with this line of work. Citing it would give the skill's philosophy a research anchor (as `karpathy-guidelines` anchors to Karpathy's observations).

---

## 6. Reconfirmation & caveats

- **Grounding default — confirmed.** The handoff flagged the in-chat-no-auto-crawl default as an unconfirmed assumption. The user approved the research plan (which used it as a measurement criterion) and said to proceed; I treated this as confirmation. It was a decisive measurement axis: most candidates **fail** it (they auto-crawl codebase/STRATEGY/graph/journal or write files), which is a primary reason none fits. If the user later wants the skill to *optionally* ground in the working directory, that's a build-time toggle, not a research input.
- **Rate-limit caveats.** 4 of 8 initial searches hit Exa's free-tier rate limit; 2 were retried successfully in a second batch (the two most likely to matter: Claude-Code-specific and ranked-output-template). The other 2 (TRIZ, Copilot) were not retried because TRIZ surfaced naturally via `creativity-lite` and `creative-director-skill` (both technique-lock TRIZ, confirming the pattern), and the Copilot ecosystem duplicates Claude Code/Cursor findings. Coverage is sufficient; further searches would return variants of already-seen patterns.
- **`scdenney/diverge-skills` SKILL.md not deep-read.** Raw file URLs 404'd (repo structure differs from guessed paths). The search captured its README in full — sufficient to score it. If the user wants the exact prose of the closest-in-philosophy candidate before building, a manual fetch of the repo tree would retrieve it; it is not necessary for the recommendation.
- **Pi-harness specificity.** Several candidates are Claude Code `~/.claude/skills/` drops (pi-compatible format) but a few rely on host-specific machinery (parallel Agent subagents, Agent SDK, MCP, AskUserQuestion). The spec's in-chat default means the build should depend on **no** host-specific machinery — a constraint that further narrows the adoptable field to zero.

---

## 7. Recommendation & next step

**Recommendation: build new via `write-a-skill`.** The locked spec is novel in *combination*; no existing skill shares all five of its load-bearing stances. Adapting the closest candidate (`diverge-skills` or `skill-propose` or `creative-thinking`) means rewriting its structure and adding two missing layers — which is building new with inspiration, not adoption. The research validates the spec's design (multiple candidates independently re-derive its qualities and reasoning layer) and supplies borrowable, evidence-backed building blocks (§5).

**Next session's first move (build phase):**

1. Invoke **`write-a-skill`** and follow it exactly (SKILL.md < 100 lines, triggered description ≤1024 chars, progressive disclosure, review checklist).
2. Model the new skill's DNA on **`karpathy-guidelines`** (principles-not-procedures, permissive tone, stable-intent/volatile-technique).
3. Draft against the locked 4-layer contract, folding in §5's borrowable ideas where they sharpen a quality or layer without forcing a technique.
4. **Resolve the handoff's write-time loose ends** against the spec (these are build decisions, not research inputs):
   - **Interaction model** — the L4 "next move" layer implies iterative rounds; confirm one-shot-with-invite vs. explicit round structure.
   - **Persistence** — conversational default (matches G) vs. optional file dump on request.
   - **Skill name** — working name `creative-brainstorm`; confirm.
   - **Done-state / handoff boundary** — how the "next move" hands off to `create-planning-docs` (the spec places creative-brainstorm upstream of the planning skills).
5. **Optional:** stress-test the draft against research findings via `grill-me` or `grill-with-docs` before finalizing — the handoff flagged this as available if needed.
6. Keep this research note and the grill handoff as the two source artifacts; the new skill's prose may cite Ismayilzada et al. EMNLP 2025 (per §5) as a research anchor, paralleling `karpathy-guidelines`' Karpathy anchor.

---

## 8. Source index (URLs)

**Closest candidates:**
- `scdenney/diverge-skills` — https://github.com/scdenney/diverge-skills
- `brianharms/skill-propose` — https://github.com/brianharms/skill-propose (SKILL.md deep-read)
- `ysskrishna/ai-agent-skills` creative-thinking — https://github.com/ysskrishna/ai-agent-skills (SKILL.md deep-read); overview — https://www.ysskrishna.space/blog/thinking-skills-for-ai-agents-cursor-claude-code
- `aj-geddes` Creative Concept Generator — https://aj-geddes.github.io/useful-ai-prompts/prompts/creative-concept-generator/
- `bhtru/adhd-claude` — https://github.com/bhtru/adhd-claude
- `Luigigreco/creativity` — http://github.com/Luigigreco/creativity

**Other inventory:**
- `neurofoo/agent-skills` scamper — https://raw.githubusercontent.com/neurofoo/agent-skills/HEAD/scamper/SKILL.md (deep-read)
- `ysskrishna` lateral-thinking — https://github.com/ysskrishna/ai-agent-skills (deep-read)
- OrchestKit brainstorm — https://orchestkit.vercel.app/docs/reference/skills/brainstorm
- `bladnman/ideation_team_skill` — https://github.com/bladnman/ideation_team_skill
- `Qnurye/diverge` — https://github.com/Qnurye/diverge
- `accaxx123/relay-brainstorm` — https://github.com/accaxx123/relay-brainstorm
- `create-genia-os` facilitate-brainstorming — https://cdn.jsdelivr.net/npm/create-genia-os@3.0.2/template/.aiox-core/development/tasks/facilitate-brainstorming-session.md
- `LingJueYa/Commons_Plan_Prompt` — https://github.com/LingJueYa/Commons_Plan_Prompt
- `lyndonkl/claude` brainstorm-diverge-converge — https://playbooks.com/skills/lyndonkl/claude/brainstorm-diverge-converge
- `Intense-Visions/harness-engineering` ideate — https://github.com/Intense-Visions/harness-engineering/blob/main/.cursor-plugin/commands/ideate.md
- Tree-of-Thought (Lewis C. Lin) — https://www.lewis-lin.com/posts/tree-of-thought-prompting
- `CorpusIQ/hermes` creative.md — https://github.com/CorpusIQ/corpusiq-docs/blob/main/hermes/prompts/creative.md
- `smixs/creative-director-skill` — https://github.com/smixs/creative-director-skill
- `vanderleisilva/ai-agent-prompts` — https://github.com/vanderleisilva/ai-agent-prompts
- `hamzaamjad/cursor-rules` — https://github.com/hamzaamjad/cursor-rules
- `johnlindquist/claude` brainstorm — https://github.com/johnlindquist/claude/blob/main/skills/brainstorm/SKILL.md
- Ismayilzada et al., Creative Preference Optimization (EMNLP 2025) — https://arxiv.org/abs/2505.14442
