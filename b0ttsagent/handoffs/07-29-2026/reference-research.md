# Reference: Research Foundation for the Daily Roblox Genre-Rotation Schedule

**Companion to:** [`daily-roblox-genre-rotation-schedule.md`](./daily-roblox-genre-rotation-schedule.md)
**Purpose:** Deep dive on the psychological research cited in the schedule design — full findings, caveats, primary-source citations, and an explicit mapping of each finding to the schedule decision it drove.
**Scope note:** Nine findings across mere exposure, the 85% rule / inverted-U arousal, information-gap theory, affective forecasting, variety-seeking cost, novelty-dopamine exploration, interleaving/spacing, and optimal-foraging patch-leaving (MVT).

---

## Honest analogical caveat (read this first)

Every study cited here comes from a different domain than Roblox gaming:
- Perceptual/motor classification (Wilson 2019 — the 85% rule)
- Consumer choice (Ratner/Kahn/Kahneman 1999 — variety-seeking cost)
- Memory & motor learning (Rohrer & Taylor 2007/2020 — interleaving)
- Optimal foraging in animals + human analog tasks (Charnov 1976; Constantino & Daw)
- Curiosity & information demand (Loewenstein 1994)
- Affect & exposure (Zajonc 1968; Kunst-Wilson & Zajonc 1980)
- Dopamine & novelty exploration (PLOS Comp Bio 2024; TICS 2024 curiosity review)

**None of these studies measured Roblox players across genres.** The mapping here is by *mechanism-analogy*: the underlying brain mechanisms (prediction error, mere exposure, avoidance of unbridgeable uncertainty, marginal learning rate, novelty-subsidy on dopamine) are conserved, well-replicated, and domain-general. The *magnitude* of effect in the specific context of a solo player rotating Roblox genres is plausible-but-unmeasured. Treat implications as **directionally correct, magnitude unknown** — not "proven on gamers."

This is why the schedule presents as *principles with rules derived from them* rather than as calibrated dosages.

---

## Finding 1 — Mere exposure builds liking without awareness

**Primary source:** Zajonc, R. B. (1968). *Attitudinal effects of mere exposure.* Journal of Personality and Social Psychology, 9(2, Pt.2), 1–27. https://doi.org/10.1037/h0025848
Full text: https://web.mit.edu/curhan/www/docs/Articles/biases/9_J_Personality_Social_Psychology_1_(Zajonc).pdf

**Supporting / extension:** Kunst-Wilson & Zajonc (1980). *Affective Discrimination of Stimuli That Cannot Be Recognized.* Science, 208(4444), 857–859. https://www.science.org/doi/10.1126/science.7352271
— Demonstrated that the exposure→preference effect occurs even when stimuli are so degraded the subject cannot consciously recognize them. The affective tag is laid down independently of recognition memory.

**Bornstein extension (the crucial caveat):** Bornstein (1989) *Exposure and affect in the laboratory* — the mere-repeated-exposure effect is robust for *neutral or mildly positive* stimuli, but **can reverse ("boomerang effect") for stimuli the subject initially encodes as negative.** Repeated exposure to a disliked stimulus amplifies dislike rather than warming it up.

### What it says
Repeated passive exposure to a novel stimulus — even without conscious recognition — increases liking of that stimulus. The effect is one of the most replicated in social psychology, demonstrated across cultures, species, and stimulus domains.

### Caveats
- Neutral-to-mild stimuli only; **backfires on negatively-encoded stimuli** (Bornstein).
- Effect size is modest — it shifts liking, it doesn't convert revulsion into enthusiasm.
- There is an inverted-U in exposure frequency itself: liking peaks at a moderate exposure count and can decline with excessive repetition (satiation).

### How it drove the schedule design
- **Multi-session-per-genre is the unit, not one-shot.** A single exposure deposits only a small liking increment. The Genre-of-the-Week (A) structure commits 2–3 sessions to one stretch genre in a week *precisely because* the second and third exposures are where mere-exposure compounds. A pure "try every genre once" grid under-exploits this.
- **Actively-disliked genres get skipped on purpose**, not ground through. Schedule rule: *"Skip actively-disliked genres — mere-exposure backfires on negatively-encoded stimuli. If solo horror encodes strongly negative, skip it or route via a comfort-adjacent co-op variant."* This is a direct Bornstein-driven decision, not a mood.
- **Halo-of-the-week beats one-and-done sampling** as the breadth mechanism. If you're going to spend the finite liking-depositing exposures, spend them clustered so the genre's distinct pattern crystallizes alongside the affect warming.

---

## Finding 2 — The 85% Rule / inverted-U of optimal difficulty

**Primary source:** Wilson, R. C., Bonawitz, E., Costa, V. D., & Ebitz, R. B. (2019). *The Eighty-Five Percent Rule for optimal learning.* Nature Communications, 10, 4646. https://www.nature.com/articles/s41467-019-12552-4
— Adaptive agent learns the 85%-difficulty point fastest; humansCapacity-tracking & subjective-engagement peaks at *moderate* uncertainty (neither too easy nor too hard).

**Historical root:** Berlyne, D. E. (1960ff). *Conflict, Arousal, and Curiosity* + collative-variables work. Hedonic tone as an inverted-U function of "arousal potential" (novelty × complexity × surprisingness × incongruity × ambiguity). Too little arousal → boredom/under-engagement; too much → overwhelm/avoidance; peak positive affect at moderate arousal.

**Curiosity-dynamics modern synthesis:** Twomey & West (2024). *Curiosity and the dynamics of optimal exploration.* Trends in Cognitive Sciences. https://www.sciencedirect.com/science/article/pii/S1364661324000287
- Curiosity engagement is *highest* when learning structure is *possible but not complete* (moderate uncertainty). It drops off on both ends — already-mastered (boring) or unlearnable (avoidance).

### What it says
Across perceptual classification, motor learning, and curiosity dynamics, the fastest learning and highest engagement occur at *moderate* difficulty/surprise/novelty — roughly the 85%-accuracy point. Both too-easy and too-hard suppress engagement and learning.

### Caveats
- Wilson 2019 measured a *perceptual classification task* in the lab — not games or taste. The 85% number is a fit to that task; the *principle* is what generalizes, not the percentage.
- We are extrapolating "novelty/difficulty" as a proxy for "psychological distance from comfort zone" — a reasonable but not formally-validated mapping.
- The curve is real and well-replicated but its width (how sharp the peak is) varies by individual and domain.

### How it drove the schedule design
- **The Spiral (C) over pure random lottery (F).** Random draws don't respect the inverted-U; a scary-far draw lands the user in the overwhelm/avoidance zone and they bail. The spiral **grades exposure by psych distance**: start adjacent to comfort (tower defense, tycoon), move to mid, only then to far (social RP, solo horror). This keeps the user on the moderate-arousal slope of Berlyne's curve rather than dropping them off the novelty cliff.
- **The adjacent/mid/far pool sort** is literally a Berlyne-arousal-distance ranking. It's the most direct finding→structure mapping in the whole schedule.
- **Re-rank justification:** in the psychology re-rank, Spiral (C) jumped to #1 from #3 specifically because it's the *only* candidate that operates on the inverted-U directly. Random lottery (F) and quota (B) were demoted for the same reason: neither respects the 85% zone.

---

## Finding 3 — Information-gap theory & information avoidance

**Primary source:** Loewenstein, G. (1994). *The Psychology of Curiosity: A Review and Reinterpretation.* Psychological Bulletin, 116(1), 75–98.
https://www.cmu.edu/dietrich/sds/docs/loewenstein/PsychofCuriosity.pdf

**Extension:** Golman, R. & Loewenstein, G. (2016). *Information Gaps: A Theory of Preferences Regarding the Availability of Information.* Evolution of Human Behavior.
https://www.cmu.edu/dietrich/sds/docs/golman/Information-Gap%20Theory%202016.pdf
- Identifies three motives for information demand (curiosity gap, savoring/avoiding emotionally-charged info, info as decision input) and *information avoidance* ("ostrich effect") when the gap is too wide or the information is threatening.

### What it says
Curiosity is the desire to fill a *specific, recognized, bridgable information gap*. When the gap is too wide (unbridgeable) or emotionally threatening, people **avoid** the information rather than seek it. The feeling of curiosity is itself aversive in a mild way — it drives reduction by gap-closing.

### Caveats
- The theory is descriptive of motivation; it doesn't specify optimal scheduling.
- "Information gap" is a metaphor when applied to "understanding a genre's core loop" — the mapping holds at the mechanism level (recognizing what you don't yet grasp, and whether it's graspable).
- The avoidance endpoint is well-evidenced but varies heavily by individual tolerance and by framing of the gap.

### How it drove the schedule design
- **The user's resistance to OOC games is reframed as a real mechanism, not a flaw to override.** Schedule rule: *"Your resistance isn't laziness — it's a real mechanism. The fix is shrinking the gap, not forcing scary-far rotations and white-knuckling."* This reframe directly justifies the graded-distance pool over the "just try everything" approaches (B, F, J-as-headline).
- **Far-tier gating.** Social RP / solo horror / narrative are gated until the adjacent tier is cleared — *because* jumping to far genres opens an unbridgeable information gap (you don't know the conventions, the jargon, the loop, the affordances) and the user avoidance-quits the schedule.
- **Grading exposure = gap shrinking.** Each adjacent genre cleared closes gaps that make the *next* genre's gap smaller. This is why the spiral works at all.

---

## Finding 4 — Affective forecasting error

**Primary sources (canonical):**
- Gilbert, D. T., Pinel, E. C., Wilson, T. D., Blumberg, S. J., & Wheatley, T. P. (1998). *Immune neglect: A source of durability bias in affective forecasting.* JPSP, 75(3), 617–638.
- Kahneman & Snell (1992); Wilson & Gilbert (2003, 2005) — broader affective-forecasting literature.

### What it says
People systematically overestimate how unpleasant a novel experience will be ("impact bias") and underestimate their ability to cope ("immune neglect"). The *anticipated* negative affect is consistently larger than the *experienced* negative affect. This applies most strongly to ambiguous novel situations where the brain has little data to forecast from.

### Caveats
- The bias is real and large on average but varies by person and by stimulus class — some people forecast well for some things.
- "Novel experience" here usually means outcomes with a clear hedonic tone; mapping to "trying a new Roblox genre" is a reasonable extension (the novel genre is hedically-ambiguous ex ante).
- This is one of the most robust findings in social-cognitive psychology, with all the standard caveats about WEIRD-sample replication.

### How it drove the schedule design
- **The 10m Sampler (H) exploits this directly.** Resistance to start is generated by the *forecast* of unpleasantness, not the actual experience. A tiny pre-commitment (just 10 minutes) collapses the forecast-vs-reality gap because reality arrives in minute ~2, and reality is almost always less bad than forecast. Schedule rule: *committed sampler = forecasting-bias bypass.*
- **The "push through momentary cost" instruction** in the operating checklist is anchored here, coupled with Finding 5: the in-moment cost is real but smaller than predicted, and the retrospective evaluation flips positive anyway.

---

## Finding 5 — Variety-seeking costs now, rewards in retrospect

**Primary source:** Ratner, R. K., Kahn, B. E., & Kahneman, D. (1999). *Choosing Less-Preferred Experiences for the Sake of Variety.* Journal of Consumer Research, 26(1), 1–15.
https://doi.org/10.1086/209547
- Three studies show people choose to switch to less-preferred options for variety, even though they enjoy each one *less* than they would have enjoyed repeating a preferred option. **Crucially, retrospective global evaluations of a *varied* sequence are higher than of a repeated sequence** — even though each moment was worse.

**Supporting:** Ratner, R. K., & Hamilton, R. W. (2015). *Inherently loyal or easily bored? Nonconscious activation of consistency versus variety-seeking behavior.* J Consumer Psychology.
https://doi.org/10.1016/j.jcps.2010.09.006
- Variety-seeking vs. consistency-seeking is *nonconsciously primed* by framing (positive frames like "loyalty" → consistency; negative frames like "boredom" → variety). Suggests the drive is malleable, not fixed.

**Public-vs-private:** Ariely & Levav (2000); Ratner, Kahn & Kahneman (above) — people seek more variety in *public* consumption than *private*. Solo consumption drifts toward consistency.

### What it says
Variety has a paradoxical temporal signature: each varied moment is *less enjoyable* than repeating a favorite would have been, but the retrospective memory of a varied sequence is *more positive* than the memory of a monotonous one. In private (solo) consumption — like a single player on a couch — people quietly *drift toward consistency* and under-seek variety relative to what their future self will retrospectively value.

### Caveats
- Retrospective-better-than-momentary is a robust finding but the gap's size depends on whether the varied options are *notable* or merely *different* — trivial variation doesn't deliver the retrospective bonus.
- The private-drift-to-consistency finding is the load-bearing one for this user (they're solo); it's well-replicated in consumer choice but not measured in gaming-rotation contexts.

### How it drove the schedule design
- **A loose quota (B-style) was explicitly rejected as insufficient** *because* solo players nonconsciously drift to consistency. Without a *structural* commitment device, the user will narrate "I tried tower defense this week" while quietly having played 5 PvP sessions and 1 TD session. The structured Genre-of-the-Week (A) is the structural override.
- **Comfort spine is always one decision away.** Because each varied moment *is* less fun, a schedule that doesn't make comfort one decision away dies in ~3 weeks (the whole schedule collapses, not just the breadth part). The "never two stretch days back-to-back, never both lanes stretch on same day" rule is a variety-cost management rule.
- **The motivational reframe the user must internalize:** the in-the-moment "this is worse than just playing PvP" feeling is *not a signal the schedule is broken* — it's the mechanism working as the research predicts. The retrospective evaluation will invert. This is the single most important psychological instruction in the operating checklist.
- **Private-consumption flag** is in the handoff explicitly under "user traits to respect."

---

## Finding 6 — Novelty is dopamine-subsidized; novelty is also ephemeral

**Primary sources:**
- PLOS Computational Biology (2024). *Dopamine encoding of novelty facilitates efficient uncertainty-driven exploration.*
https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1011516
- Twomey & West (2024) [same as Finding 2's curiosity-dynamics cite]. Trends in Cognitive Sciences.
https://www.sciencedirect.com/science/article/pii/S1364661324000287
- Nature Neuroscience (2024). *Explaining dopamine through prediction errors and beyond.*
https://www.nature.com/articles/s41593-024-01705-4 — on the limits of pure RPE framing.

### What it says
Dopamine encodes novelty (not just reward prediction error), which *subsidizes attention* toward novel stimuli — the first encounter with anything new gets an attention/engagement boost. But within-stimulus novelty fades fast (the dopamine response habituates), and engagement collapses on two endpoints: when structure is "already learned" (boredom) or "unlearnable" (overwhelm). Optimal engagement is in between (ties back to Finding 2).

### Caveats
- Dopamine's exact role is contested; the classic RPE framework is "considered too simple" (the Nature Neurosci 2024 review). What's *not* contested is that novelty drives initial engagement and that it habituates.
- The "first 20 minutes are subsidized" framing is a reasonable ord-magnitude statement, not a calibrated timer.

### How it drove the schedule design
- **First-session impressions of any new genre are systematically overinflated by novelty dopamine.** Schedule warning: *don't judge a genre by session 1.* The Return-Ticket (I) exists to produce a session 2 *after* the novelty subsidy has faded — that's the real read on whether the genre's pattern is graspable to this user.
- **The Return-Ticket (I) is promoted from optional-modifier to core component** specifically because of this finding. Intuition doesn't crystallize in the novelty-subsidized first session; it crystallizes in the second touch where the dopamine floor dropped out and the underlying genre pattern has to do the engagement work. The schedule rule *explicitly* forces this second touch.
- **The drop rule (MVT, Finding 8) is partially counterweighted here.** "I'm bored at minute 15" might be novelty-subsidy depletion on a deep genre, not genuine marginal-return flattening. Schedule rule distinguishes boredom-on-shallow-genres (legitimate drop) from boredom-on-deep-genres (schedule another session).

---

## Finding 7 — Interleaving beats blocking (with a spacing confound)

**Primary sources:**
- Rohrer, D., & Taylor, K. (2007). *A shuffling of mathematics problems improves learning.* Instructional Science, 35, 591–603.
http://uweb.cas.usf.edu/~drohrer/pdfs/Rohrer%26Taylor2007IS.pdf
- Rohrer, D., Dedrick, R. F., & Burgess, K. (2014). *The benefit of interleaved mathematics practice is not limited to superficially similar kinds of problems.* Psychonomic Bulletin & Review.
http://uweb.cas.usf.edu/%7Edrohrer/pdfs/Rohrer_et_al_2014PB&R.pdf
- Rohrer, D., Dedrick, R. F., Hartmann, N. M., & Cheong, C. S. (2020). *A randomized controlled trial of interleaved mathematics practice.* Journal of Educational Psychology. (Preregistered cluster RCT in real classrooms.)
http://uweb.cas.usf.edu/%7Edrohrer/pdfs/Rohrer_et_al_2020JEdPsych.pdf

**On the spacing confound:**
- Taylor, K., & Rohrer, D. (2010). *The effects of interleaved practice.* Applied Cognitive Psychology.
http://uweb.cas.usf.edu/~drohrer/pdfs/Taylor&Rohrer2010ACP.pdf
- Notes that interleaving *inherently* introduces spacing (because practice on the same skill is distributed across time), so the observed benefits of interleaving may be *partly* driven by spacing rather than interleaving per se.

### What it says
Mixed practice (interleaving — a-b-c-b-c-a-c-a-b) produces stronger *transfer* and *discrimination* than grouped practice (blocked — a-a-a, b-b-b, c-c-c), even though learners *prefer* blocked and *feel* they're learning more from it (a metacognitive illusion). The mechanism is the requirement to *choose the appropriate strategy per instance* rather than being told it in advance by block order. The benefits show up in preregistered classroom RCTs, not just labs.

The spacing confound: part of interleaving's benefit may come from the *spacing* interleaving necessarily entails, not from the interleaving itself.

### Caveats
- All high-quality evidence is in *mathematics* learning. Transfer to gameplay pattern-recognition is by analogy (the discrimination mechanism is domain-general).
- The "learners prefer blocked" metacognitive illusion is a problem *for self-regulated scheduling* — the user, if left to choose, would block all sessions into one genre for a stretch and feel they're learning more, while actually doing worse.

### How it drove the schedule design
- **Weekly genre focus (A's granularity) is the correct interleaving unit.** Massing within the week builds an initial schema (you see the pattern forming across 2–3 sessions); interleaving *between* weeks builds transfer across genres. The schedule explicitly avoids both "same genre every day for 30 days" (pure blocking) and "new genre every single session" (pure interleaving with no schema per genre).
- **Spacing within the week is a rule, not a preference.** Schedule: *"2–3 sessions per lane per week, spaced ~2 days apart (not blocked into one day)."* This is direct application of the spacing confound finding — even if the interleaving benefit were entirely a spacing artifact, spacing the sessions still captures it.
- **The "never two stretch days back-to-back in the same lane" rule** is partly the variety-cost management rule (Finding 5) and partly spacing enforcement (Finding 7). One rule, two findings behind it.
- **Anti-recommendation carried in the design doc:** pure random-per-session rotation (F-style) was demoted partly because it interleaves with zero within-genre schema formation — defeating the discrimination mechanism that makes interleaving work.

---

## Finding 8 — Marginal Value Theorem / optimal patch-leaving

**Primary source:**
- Charnov, E. L. (1976). *Optimal foraging: the marginal value theorem.* Theoretical Population Biology, 9(2), 129–136.
https://digitalrepository.unm.edu/cgi/viewcontent.cgi?article=1008&context=biol_fsp

**Human-behavior extensions:**
- Constantino & Daw (human opportunity-cost learning in patch foraging). PMC.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4624618/
- Wolfe / Humans in visual-search foraging. PMC.
https://pmc.ncbi.nlm.nih.gov/articles/PMC4521330/
- MVT and normative adaptive exploration. eScholarship.
https://escholarship.org/uc/item/5339f64z

### What it says
MVT predicts an optimal forager leaves a depleting patch when the *marginal* return rate (reward per unit time, diminishing) drops to the *average* return rate of the environment (the opportunity cost of time spent). Stay too long and you waste time on diminishing returns; leave too soon and you forgo recoverable returns.

### Caveats
- Original MVT is animal foraging. Human analogs (visual search, patch foraging tasks) show MVT *partially* predicts behavior — humans use heuristics, not strict optimality, and often deviate in systematic ways (over-stay or under-stay biases).
- Game genre-learning is a *non-depleting* patch in the strict MVT sense — the genre doesn't literally run out of reward. The mapping is by analogy: the "patch" is "current rate of new pattern-learning from this genre/game," and it flattens as the genre's pattern saturates for this user.

### How it drove the schedule design
- **The drop rule is explicitly MVT-framed.** *"Drop when the rate of new pattern-learning has flattened to the environmental average — not when you're bored."* Confusion on a deep genre is *not* a flattening marginal return (it's an unstarted one); schedule another session.
- **The crucial intersection with genre depth (both MVT and Finding 6).** Different genres have differently-shaped marginal-return curves:
  - **Shallow-hook genres** (obby, rhythm, incremental clicker, arena shooter) — fast-ramp marginal return, fast plateau. Boredom at minute ~15–20 *is* a legitimate flattening signal → drop is correct.
  - **Deep-ramp genres** (tower defense, tycoon, PvE shooter, survival-system, strategy, narrative, social RP, sim-management) — slow-ramp marginal return, plateau much later. Minute-15 boredom is *not* flattening — the structure unlock is in minute ~20–30, often later. Drop-at-15 here is systematically wrong.
- **This finding alone produced the H-gated-by-depth rule.** A flat sampler applied everywhere would systematically under-sample deep genres (the user would bail at minute 10 on a genre whose payoff is at minute 25). The depth-class tagging in the genre pool, and the "shallow → sampler / deep → mandatory full 30m" gating, is the direct structural response to this curve asymmetry.
- **The "fast-dropper" user trait is reframed:** it's correct for shallow genres and *wrong* for deep ones — the schedule recognizes this and overrides the trait only where the trait misfires, not globally.

### Finding 9 — Spacing effect (compounding on Finding 7)

This is referenced alongside Finding 7's spacing-confound discussion (Taylor & Rohrer 2010). Distributed practice produces stronger retention than massed practice. The Cepeda et al. (2006) meta-analysis is the canonical summary; it's referenced conceptually here rather than cited separately because Finding 7 already covers the operative mechanism.

The schedule's "spaced ~2 days apart, not blocked into one day" rule is jointly justified by Findings 7 and 9.

---

## Finding→Schedule-decision cross-reference (the load-bearing map)

| Finding | Primary decision it drove |
|---|---|
| 1. Mere exposure (Zajonc, Bornstein caveat) | Multi-session-per-genre is the unit; actively-disliked genres get skipped, not grinded |
| 2. 85% rule / inverted-U (Wilson, Berlyne) | Spiral (C) over random lottery (F) — graded psych distance in pool sort; Spiral promoted to #1 in re-rank |
| 3. Information-gap & avoidance (Loewenstein) | Far-tier gating; resistance reframed as real mechanism to grade around, not override |
| 4. Affective forecasting error (Gilbert) | 10m Sampler (H) as forecasting-bias bypass mechanism |
| 5. Variety-cost & private drift (Ratner/Kahn/Kahneman) | Loose quota (B) rejected; comfort-spine-always-available; "in-the-moment cost is the mechanism working" reframe |
| 6. Novelty dopamine & ephemerality (PLOS 2024) | Return-Ticket (I) promoted to core; "don't judge genre by session 1" warning |
| 7. Interleaving & spacing confound (Rohrer/Taylor) | Weekly granularity (not daily, not monthly); spacing-within-week rule; back-to-back-stretch prohibition |
| 8. Marginal Value Theorem (Charnov) | Drop rule = marginal-learning-flattened (not boredom); H-gated-by-depth rule; fast-drop trait reframed as correct-for-shallow/wrong-for-deep |
| 9. Spacing effect (compounding) | Same rule as 7 — distributed, not massed |

---

## What this research explicitly does NOT justify (intellectual honesty)

To prevent overreach in a future resuming session, here is what the science does *not* license:

1. **A specific "optimal number of genres per month."** No cited study measures this for gaming contexts. Any number is heuristic, not evidence-derived.
2. **A specific "12 genres in a quarter" throughput promise.** That figure in the original brainstorm was a coverage estimate, not a research finding. The research licenses the *structure*, not the throughput.
3. **That the user will enjoy this schedule.** Finding 5 specifically predicts they will enjoy it less in-moment than comfort gaming, while valuing it more retrospectively. "The user likes it" is the wrong success metric; "the user sticks with it and retrospectively rates the breadth months higher" is.
4. **That this schedule is superior to ad-lib gaming for intuition/pattern-recognition in a *causal* sense.** The findings are mechanistic and from other domains; the schedule is a principled design from those mechanisms, not a tested intervention.
5. **That the graded-distance pool sort is correct for this specific user.** The adjacent/mid/far sort is a *hypothesis* from the user's self-reported comfort zone. A resuming agent should ask the user to re-rank any genre whose felt psych distance differs after a session or two.

## Full source list (numbered in order of first appearance)

1. Zajonc, R. B. (1968). *Attitudinal effects of mere exposure.* JPSP 9(2, Pt.2), 1–27. https://doi.org/10.1037/h0025848 — pdf: https://web.mit.edu/curhan/www/docs/Articles/biases/9_J_Personality_Social_Psychology_1_(Zajonc).pdf
2. Kunst-Wilson & Zajonc (1980). *Affective Discrimination of Stimuli That Cannot Be Recognized.* Science 208(4444), 857–859. https://www.science.org/doi/10.1126/science.7352271
3. Bornstein (1989). *Exposure and affect in the laboratory and the field.* (mere-exposure boomerang caveat.)
4. Wilson, R. C., Bonawitz, E., Costa, V. D., & Ebitz, R. B. (2019). *The Eighty-Five Percent Rule for optimal learning.* Nature Communications 10, 4646. https://www.nature.com/articles/s41467-019-12552-4
5. Berlyne, D. E. (1960ff). *Conflict, Arousal, and Curiosity.* (collative variables / arousal potential.)
6. Twomey & West (2024). *Curiosity and the dynamics of optimal exploration.* Trends in Cognitive Sciences. https://www.sciencedirect.com/science/article/pii/S1364661324000287
7. Loewenstein, G. (1994). *The Psychology of Curiosity.* Psychological Bulletin 116(1), 75–98. https://www.cmu.edu/dietrich/sds/docs/loewenstein/PsychofCuriosity.pdf
8. Golman, R. & Loewenstein, G. (2016). *Information Gaps: A Theory of Preferences Regarding the Availability of Information.* https://www.cmu.edu/dietrich/sds/docs/golman/Information-Gap%20Theory%202016.pdf
9. Gilbert, D. T., Pinel, E. C., Wilson, T. D., Blumberg, S. J., & Wheatley, T. P. (1998). *Immune neglect: A source of durability bias in affective forecasting.* JPSP 75(3), 617–638. (affective forecasting literature, inferred from standard source.)
10. Ratner, R. K., Kahn, B. E., & Kahneman, D. (1999). *Choosing Less-Preferred Experiences for the Sake of Variety.* JCR 26(1), 1–15. https://doi.org/10.1086/209547
11. Ratner, R. K. & Hamilton, R. W. (2015). *Inherently loyal or easily bored? Nonconscious activation of consistency versus variety-seeking behavior.* J Consumer Psychology. https://doi.org/10.1016/j.jcps.2010.09.006
12. Ariely, D. & Levav, J. (2000). *Sequential choice in group settings: Taking the road less traveled and less enjoyed.* JCR 27(3). (private-vs-public variety, cited per literature.)
13. PLOS Computational Biology (2024). *Dopamine encoding of novelty facilitates efficient uncertainty-driven exploration.* https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1011516
14. Nature Neuroscience (2024). *Explaining dopamine through prediction errors and beyond.* https://www.nature.com/articles/s41593-024-01705-4
15. Rohrer, D. & Taylor, K. (2007). *A shuffling of mathematics problems improves learning.* Instructional Science 35, 591–603. http://uweb.cas.usf.edu/~drohrer/pdfs/Rohrer%26Taylor2007IS.pdf
16. Rohrer, D., Dedrick, R. F., & Burgess, K. (2014). *The benefit of interleaved mathematics practice is not limited to superficially similar kinds of problems.* Psychonomic Bulletin & Review. http://uweb.cas.usf.edu/%7Edrohrer/pdfs/Rohrer_et_al_2014PB&R.pdf
17. Rohrer, D., Dedrick, R. F., Hartmann, N. M., & Cheong, C. S. (2020). *A randomized controlled trial of interleaved mathematics practice.* Journal of Educational Psychology. http://uweb.cas.usf.edu/%7Edrohrer/pdfs/Rohrer_et_al_2020JEdPsych.pdf
18. Taylor, K. & Rohrer, D. (2010). *The effects of interleaved practice.* Applied Cognitive Psychology. http://uweb.cas.usf.edu/%7Edrohrer/pdfs/Taylor&Rohrer2010ACP.pdf
19. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed practice in verbal memory: A quantitative review.* Psychological Bulletin. (spacing meta-analysis, cited by Finding 9.)
20. Charnov, E. L. (1976). *Optimal foraging: the marginal value theorem.* Theoretical Population Biology 9(2), 129–136. https://digitalrepository.unm.edu/cgi/viewcontent.cgi?article=1008&context=biol_fsp
21. Constantino & Daw — human opportunity-cost learning in patch-foraging. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC4624618/
22. Wolfe / humans in visual-search foraging. PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC4521330/
23. MVT and normative adaptive exploration. eScholarship. https://escholarship.org/uc/item/5339f64z

---

## Closing note for the resuming agent

The rules in the schedule are not arbitrary preferences. Each one is pinned to a specific finding above. If you wish to change a rule, locate its finding in the cross-reference table above, re-read the caveats for that finding, and confirm the change doesn't violate the mechanism the rule is protecting. The schedule will degrade gracefully to "generic rotation advice" if the findings are ignored; it delivers its design value only while the mechanisms are respected.