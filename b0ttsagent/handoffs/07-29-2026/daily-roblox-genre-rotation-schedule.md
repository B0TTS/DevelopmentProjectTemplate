# Handoff: Daily Roblox Genre-Rotation Schedule

**Session date:** 07-29-2026
**Topic:** Designing a psychologically-grounded daily Roblox play schedule for cross-genre intuition/pattern-recognition building, with explicit emphasis on playing *outside* the user's comfort zone.
**Companion research doc:** [`reference-research.md`](./reference-research.md) — full citations, per-finding caveats, and the finding→decision mapping. **Read this alongside the handoff.**

---

## 1. Summary of what was accomplished

The user wanted a daily gaming structure (~30m mobile + 30m PC, natural-fit genres each lane) for building cross-genre intuition and pattern recognition — with the explicit goal of forcing themselves outside a narrow comfort zone (PvP, FPS, incremental, Minecraft). The user drops games fast and tends to avoid genres outside comfort.

The session went through three phases:

1. **Clarifying Q&A** — locked 5 constraints: (a) comfort zone = PvP/FPS/incremental/Minecraft, (b) goal = intuition + pattern recognition (not analytical deconstruction), (c) natural-fit device↔genre mapping (no forced cross-training), (d) 30m/device is a *max* (freetime extension allowed), (e) user drops games fast when not hooked.

2. **Creative brainstorm (~10 ranked candidate schedules)** — generated options A–J spanning breadth mechanisms (rotation, block-day, quota, lottery, chart) and stretch intensities. Ranked with reasoning and trade-offs. Key output: Genre-of-the-Week (A), Spiral (C), Return-Ticket (I), 10m Sampler (H), Alternate-Day (E).

3. **Psychology-domain re-analysis with web research** — ran real studies through the schedule options. Nine findings mapped to decisions (see reference.md). Result: a re-rank and a **locked hybrid: A + C + I + H-gated-by-depth**. Delivered a concrete 2-week starter schedule using adjacent-tier genres only.

## 2. The locked design (the deliverable)

**Hybrid schedule = Engine A + Stretch-genre selection C + Continuity I + Intra-session H-gated**

- **A — Genre-of-the-Week:** one stretch genre per lane per week; 2–3 sessions/lane/week, **spaced ~2 days apart** (not blocked — spacing compounds the schema). Comfort fills non-stretch sessions.
- **C — Spiral / graded distance:** stretch genres drawn from a pool sorted by psychological distance from comfort (adjacent → mid → far). Far genres are **gated** until the adjacent tier is cleared. The pool lives in the schedule doc.
- **I — Return-Ticket:** any stretch session that hooks earns a guaranteed follow-up slot — either a *different game in the same genre* (builds genre-schema, not game-loyalty) *or* a deeper session in the hooked game. **This second touch is where intuition actually compounds** — it outlasts the novelty-dopamine subsidy that inflates session-1 impressions.
- **H — 10m Sampler, gated by genre depth:**
  - **Shallow-hook genres** (obby, rhythm, incremental clicker, arena shooter) → sampler: game A 10m → if flat, game B 10m → invest rest in whichever hooked. Uses the user's fast-drop as a *feature*; bypasses affective-forecasting resistance.
  - **Deep-ramp genres** (tower defense, tycoon, PvE shooter, survival-system, strategy, narrative, social RP, simulation-management) → **mandatory full 30m, no sampler.** Don't bail at minute 12; structure unlocks at minute ~20–30 and the fast-drop trait is *wrong* here.

### Auxiliary rules
- **Comfort spine always one decision away.** Never two stretch days back-to-back in the same lane; never both lanes stretch on the same day. Protects long-term adoption past week 3 (variety-cost finding — stretch sessions hurt in the moment).
- **Drop rule = MVT, not boredom.** Drop when *rate of new pattern-learning has flattened* (marginal return ≈ environmental average). Confusion on a deep genre ≠ drop signal — it's a "schedule another full-30m" signal.
- **Skip actively-disliked genres on purpose.** Mere-exposure backfires on negatively-encoded stimuli. If solo horror encodes strongly negative, skip it or route via a comfort-adjacent co-op variant.

## 3. Current state / what's delivered

- Full 2-week starter schedule written in-chat (Week 1 = Tower Defense × Tycoon; Week 2 = Co-op PvE shooter × Obby), using adjacent-tier genres only.
- Graded-distance genre pool drafted (comfort / adjacent / mid / far), with depth-class tags per genre to drive the H-gating.
- Per-session operating checklist delivered (before / during / at-minute-25 / after).
- Two honest gotchas surfaced explicitly: (a) Week 1 will *feel* worse than a PvP month in-the-moment (variety-cost) but retrospectively rate higher — hold that line; (b) Week 1 session-1 impressions are novelty-inflated — the return-ticket session-2 is the real read.

## 4. Open decisions / next steps for a resuming agent

1. **Run the 2-week starter as-is**, then the user reports back what hooked vs. actively disliked. Next agent should:
   - Promote any cleared-adjacent genre off the pool (mark it "cleared → comfort-tier-2").
   - Draft **Week 3–4 into the mid tier** using the same A+C+I+H-gated structure. Mid-tier genres from the pool: Obby/platformer, Racing, Rhythm (mobile); Battle Royale, Horror-lite co-op, MOBA-lite/arena (PC).
   - Tune the sampler-vs-full-30m gating **if any deep genre felt mislabeled** (e.g., user reports a TD didn't unlock until minute 35 → confirm deep; reports a tycoon hooked in 8m → consider sampler-OK-after-first-session).
2. **Genre-pool maintenance.** The adjacent/mid/far sort is a *hypothesis* of psych distance from *this user's* comfort zone. A resuming agent should ask the user to re-rank any genre whose lived psych distance differs from the draft sort after a session or two.
3. **Reflection artifact (open question).** The user's stated goal (intuition + pattern recognition) *might* benefit from a one-line-per-session log to crystallize the pattern — but the brainstorm explicitly *rejected* the "analyze-and-annotate every session" option as homework-overkill. If the user wants more reinforcement, propose a **low-friction variant**: a 6-word max "genre loop = ___" line per stretch session, no more. Do not push the heavy version.
4. **File persistence (open).** The schedule currently lives only in chat history. User was offered a planning-doc export and did not request one. Offer once more if they want it to survive outside this handoff, but don't force.

## 5. Suggested skills for the next session

- **`create-context-doc`** — if the user wants to promote this into a persistent CONTEXT.md (the "what & why") before building out weeks 3–8. Pure harvest, no new decisions.
- **`create-execution-plan`** — if a CONTEXT.md exists and they want a PLAN.md carrying the full multi-week rollout (adjacent → mid → far arcs) as executable phases. Needs CONTEXT.md first.
- **`creative-brainstorm`** — if mid-tier weeks reveal a constraint the current hybrid doesn't handle (e.g., a genre that needs 2 sessions to even parse the loop, breaking the "spaced ~2 days" cadence). Re-run to generate schedule *variants* for that edge, don't patch ad hoc.
- **`explain-it-v2`** — if the user wants to deeply understand *why* the H-gating-by-depth rule matters (the MVT vs novelty-subsidy tradeoff), this is the Socratic-walkthrough skill.
- **Not recommended:** `grill-me` / `grill-with-docs` unless the user wants to stress-test the schedule against their own lived experience *after* running 2 weeks — premature before there's data.

## 6. Key context for continuing (non-file)

- **User traits to respect:** fast-dropper, resists OOC games, plays Minecraft constantly, solo player (private consumption → consistency-drift risk per Ratner/Kahn — this is *why* a loose quota alone was rejected as insufficient).
- **Device mapping:** mobile = obby/sims/rhythm/incremental; PC = FPS/build/tactical/strategic/Minecraft. Natural fit only (no cross-training) — explicit user decision.
- **The single most load-bearing finding:** the **second touch** (Return-Ticket) is where intuition is built, because session-1 of any new genre is novelty-dopamine-inflated and the underlying genre pattern only crystallizes once that subsidy fades. Protect this slot.
- **The most counterintuitive rule the user needs to internalize:** variety *costs* in the moment but rewards in retrospect — so feeling "this is worse than just playing FPS" mid-session is *not* a signal the schedule is broken; it's the mechanism working.

## 7. Research foundation

All nine findings, their caveats, the honest analogical caveat (none of these studies measured Roblox players — mechanism-analogy, not proven-on-gamers), and the explicit finding→decision mapping live in **[`reference-research.md`](./reference-research.md)** in this same folder. Read it before materially changing the schedule — the rules are not arbitrary, they're each pinned to a specific finding.