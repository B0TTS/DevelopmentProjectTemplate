---
name: roblox-retention-brainstorm-v2
description: Generate ranked retention-system ideas for Roblox simulator games, one time-horizon scope at a time (micro, short, mid, long, daily, weekly), with each idea crafted to be exclusive to the user's specific game mechanics rather than portable to any simulator. Output is compact per-idea tables, not prose (v2 of the retention brainstormer — v1 outputs prose). Use when designing retention systems for a Roblox simulator/incremental game, when the user says "brainstorm retention", "daily retention", "weekly retention", "retention systems", "how do I keep players coming back", or wants retention ideas scoped by session length.
---

# Roblox Retention Brainstorm

Generate ranked, thematically-exclusive retention-system ideas for Roblox simulator games — one time-horizon scope at a time.

## Philosophy

This skill is a **focused brainstormer**, not an architect. It does one job: produce creative, exclusive retention ideas for a single scope. It does not do cross-scope gap analysis or assemble retention roadmaps.

The core differentiator: every idea should be **exclusive to the user's game** — only possible because of the game's specific mechanics, not portable to any simulator unchanged — and that exclusivity should be **legible** in the output. Generic-but-effective ideas are still welcome, but must be honestly tagged, not fake-exclusivity'd.

State intent, not procedure. The methods below are stable intent; the *how* is the model's to choose per-run and per-game.

## Quick start

1. **Scope.** If the user didn't name a scope, present the 6-scope menu (see [REFERENCE.md](REFERENCE.md)) and ask them to pick. If they named one, proceed.
2. **Summarize back.** State what you understand about their game (core loop, theme, audience, existing systems, monetization stance) from their request and prior context. Let them correct before you probe further.
3. **Probe adaptively.** Ask only what you need to generate exclusive ideas for the chosen scope — one question at a time, each with your recommended answer. Floor: always confirm core loop + theme. Ceiling: stop when the next question's answer wouldn't change any idea. See [REFERENCE.md](REFERENCE.md).
4. **Generate.** Produce the output in the **table format** defined in [REFERENCE.md](REFERENCE.md): a one-line ranking rationale, a lean overview table covering all ideas, then one compact per-idea table for every idea. Quantity: aim for ~15–20; go to 20–30+ when a scope is rich; generate as many as you see fit — "stop when padding starts" is the only real ceiling, not a quota. Tag hybrid ideas. Include monetization honestly.
5. **Next move.** End with one optional line inviting the user to deepen, combine, or re-run for another scope.

## What makes this skill work

- **One scope at a time.** Don't bleed into other scopes except via hybrid tags.
- **Exclusivity is the point.** Pursue it via the intent + moves in [REFERENCE.md](REFERENCE.md), not a rigid pipeline.
- **Honesty over flattery.** If an idea is generic, tag it generic. If monetization would hurt an idea, say "better left free."
- **Tables, not prose.** Output is compact tables — brief, scannable, uniform. No prose blocks. Enforce the brevity rule in [REFERENCE.md](REFERENCE.md).
- **Light reference grounding.** Mention real sim games (PS99, Bee Swarm, Mining Sim, etc.) only when a comparison genuinely illuminates — never as a mandatory step.

All specs — scope definitions, output table spec, brevity rule, exclusivity moves, hybrid rules, probing rules, quantity guidance — live in [REFERENCE.md](REFERENCE.md). Read it before generating. For a full worked example of a ranked daily-scope run in table format (with exclusivity tags, hybrid tags, and monetization), see [EXAMPLES.md](EXAMPLES.md).
