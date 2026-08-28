---
name: creative-brainstorm
description: Generate multiple creative candidate options for a stated goal, ranked with transparent reasoning. Use when the user wants to brainstorm, ideate, explore options, generate alternatives, or find creative directions for any goal, problem, or design — before committing to a plan.
disable-model-invocation: true
---

# Creative Brainstorm

Given a stated goal, generate multiple creative candidate options — ranked, with explanations and transparent reasoning. Domain-agnostic: game systems, UI, product, anything. This skill diverges; convergence is the next skill's job.

Anchored to Ismayilzada et al., *Creative Preference Optimization* (2025) — creativity is multifaceted (novelty, diversity, surprise, quality); locking to one technique or one dimension underserves it.

**Tradeoff:** This skill biases toward breadth and transparency over picking a winner. If the user wants a single recommendation, let them say so.

## Philosophy

- **Principles, not procedures.** State qualities and intent; don't prescribe a fixed method. Techniques are the model's to choose per-run, so the skill stays useful as models improve.
- **Recommend, don't direct.** Permissive tone ("consider…", "you might…"), not imperative. Prescription ages out; reasoning ages well.
- **Separate stable intent from volatile technique.** Intent (diverse, novel, well-reasoned, ranked, transparent) is fixed; the *how* is not. Resist technique-locking — a fixed framework, fixed roles, or a mandated lens set. It's the field's default failure mode; don't drift into it.
- **Lean on requirements that get more valuable as models improve** — especially the reasoning layer.
- **Bounds, not counts** — ceilings and qualities, not quotas.

## Grounding

In-chat by default. Work from what the user states in the conversation. **Do not auto-crawl files or the codebase.** If the user pastes project context, factor it in; otherwise blue-sky.

## Output (four layers, in order)

1. **Framing** (2–3 lines) — restate the goal and name the shape you're optimizing for.
2. **Reasoning** — surface honestly: what you deliberately varied across options, what you considered and rejected (and why each was a trap or weaker fit), and what trade-off each surviving option optimizes. No required vocabulary. This layer is the differentiator — don't let it become a polite afterthought.
3. **Ranked options** — best-fit first. Each option: a name, a 1–2-sentence concept, why it fits, its strengths, and its stretches/risks (light reality-check). Defend the ranking — note if one is clearly best or a hybrid would be ideal; argue briefly against your own favorite when warranted.
4. **Next move** (one line) — invite the user to pick a direction to deepen, or combine ideas.

## Qualities the output must clear

- **Diversity across independent dimensions** — options should differ in underlying mechanism, not just vocabulary. Cluster by angle, not surface keywords. Aim for at least one option that violates the obvious assumption.
- **Novelty preferred over safe variants.**
- **Defended ranking.**
- **Light reality-check** on each option.
- **Reasoning surfaced** — rejected options + why.

Aim for ~8–10 options; hard max 12 unless the user asks for more. Keep them ranked and *open* — do not narrow to a winner. Convergence is downstream (`create-planning-docs`).

## Illustrative moves (available, never forced)

Kinds of moves that satisfy the qualities — draw on them when they help, skip them when they don't; the model decides per-run: vary a dimension deliberately · import a mechanism from another domain · invert the goal · remove a constraint then pull back · recombine parts of options.

For a richer menu (SCAMPER's seven lenses; lateral-thinking triggers), see [REFERENCE.md](REFERENCE.md).

## Interaction

One-shot per run. If the user takes the "next move" invite, run again, deepening that direction. Output stays in chat; write a file only if the user explicitly asks.
