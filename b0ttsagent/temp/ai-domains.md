# AI Skill Domains — Quick Reference

The six ranked domains for training "understanding & using AI" in the 1.5h x3/week rotation. Full reasoning, weakest-domain diagnosis, and the Calibration Block live in the session; this file is just the map.

## Quick Access

1. **Verification & Calibration** — error taxonomy + seeded probes + trust from measured catch-rates. *Weakest domain; trained first.*
2. **Interpretation Prediction** — forecast misfires before running; scored by a cumulative misfire library.
3. **Decomposition** — fuzzy concept → explicit spec (goal, done-when, constraints, unknowns, edges) before opening the agent.
4. **Context Supply** — pack what the agent needs to know; fix "the missing piece" in the input, not the output.
5. **Build Systems** — your strongest domain; builds the practice instruments, not a practice slot.
6. **Learning Craft** — watch-list; unscheduled until retention failure shows up.

## Domain Table

| Rank | Domain | One-liner | Status |
|---|---|---|---|
| 1 | Verification & Calibration | Know the error classes, get labeled positives, match trust to evidence | Weakest — block focus |
| 2 | Interpretation Prediction | Falsifiable pre-run forecasts, fed by hindsight → foresight library | Biggest self-reported gap |
| 3 | Decomposition | Explicit spec before prompt; mark ambiguity spots | Core of "fuzzy concept" fix |
| 4 | Context Supply | Input-side cure for missing context (replaces "Prompt Craft") | Reframe of old #5 |
| 5 | Build Systems | Ledger, error-seeder, preflight skill — the factory | Delivery vehicle, not a slot |
| 6 | Learning Craft | Durable self-teaching (retrieval, spaced review) | Watch-list only |

**Block:** The Calibration Block, 4 wks, 40-min slice x3/wk — Session shape: 5 review / 8 spec / 5 predict / 12 run / 8 check / 2 ledger.

---

## In Depth

Each domain: what it is, why it's ranked where it is, where it shows up in your workflows, and how the block trains it.

### 1. Verification & Calibration

**What it is.** Knowing what kinds of errors agent output can contain, acquiring real evidence about whether a specific output contains them, and setting trust to match that evidence — not your doctrine. Three sub-mechanics: error taxonomy (what can go wrong), ground-truth construction (how you'd know), calibration (confidence matched to measured accuracy).

**Why it's first.** Your slice-of-cake model ("agents aren't wrong, they're missing something") deletes the fabrication class by definition — anomalies get reclassified as omissions, patched by re-prompting, never counted as caught errors. The most damaging failure mode is invisible to you by policy, not by accident. Compounding it: you learn unfamiliar domains at high volume (no internal ground truth, so "usually right" is a mood, not a measurement) and you build on what you learn (a wrong fact becomes a premise in the next script or skill). Errors compound geometrically.

**In your day.** Your test-runs already verify *interpretation* (will it get the prompt?) — never *content* (is the output true?). All your checking capacity sits on the omission class, the one class whose remedy you already know (re-prompt). Best skill, spent where it's worth least.

**Block training.** Seeded-error probes: take a finished output, fresh agent seeds subtle load-bearing errors into a copy (answer key stored separately), you hunt cold on a timer, then score. You can't calibrate a detector that never sees a confirmed positive — this is the instrument. Weekly forensic moves rotate classes: source-trace (fabrication), counter-interrogation (omission), reverse-spec (spec-gap), date/version check (drift).

### 2. Interpretation Prediction

**What it is.** Simulating in advance how the model will read your input, and producing *testable forecasts*: this term is ambiguous and it will read it as X; this instruction is buried and it will skip step 2; this constraint is implied and it will violate it. Not vibes — specific, falsifiable, located.

**Why it's second.** Your biggest self-reported problem, and the direct lever on faster offloading: every misfire foreseen before running is a test-run cycle saved. The decisive evidence is the asymmetry — you diagnose misfires well in hindsight, don't predict before running. Good post-mortem, no pre-mortem is the classic signature of a trainable skill: the pattern machinery works, the protocol that runs it pre-run is missing.

**In your day.** Today this manifests as the test-run — expensive, empirical, safe. Prediction is a cheaper probe: 5 minutes of forecasting, scored against the run itself. Every hindsight insight that currently evaporates ("oh, it always defaults to the newest API version") becomes a line in the misfire library — a cumulative checklist feeding the next spec.

**Block training.** The 5-minute prediction step with a strict rubric (names a failure mode *and* a location; strict / partial / miss) plus the misfire-library review opening each session. The ledger accumulates a hit-rate you can actually see move.

### 3. Decomposition

**What it is.** Interrogating your own half-formed concept until it becomes an explicit specification — goal, done-when, constraints, unknowns, edge cases — before the agent sees it. Discovering what you actually want by forcing it into a form that can't hide fuzziness.

**Why it's third.** Your friction splits roughly evenly between (a) concept still fuzzy in your head and (b) translation failure. Decomposition owns (a). It ranks below prediction because fuzzy concepts *cause* the misfires prediction flags — a spec with unmarked ambiguous spots is exactly where foresight fails. It's also the foundation: you can't predict misfires of an intent you never stated, or supply context for a goal you haven't decomposed.

**In your day.** Close to what you already do, but the decomposition happens implicitly on the way to the prompt — never externalized, never scored on how well it survived transfer. The 5-line spec before opening the agent moves fuzziness-resolution from "during the run, at agent cost" to "before the run, at your cost."

**Block training.** The 8-minute spec step with one twist: you must mark the two spots where ambiguity is most likely — a required self-forecast that folds prediction into decomposition. The reverse-spec forensic move audits it: a fresh agent infers your requirements from the output alone; the diff against your intended spec shows which intent failed to transfer and why.

### 4. Context Supply

**What it is.** The showing half of "knowing vs. showing": deciding what the agent needs to *know* before asking — facts, files, examples, constraints, anti-goals — and packing it into the input.

**Why it's fourth and why it replaces "Prompt Craft."** Your own metaphor is the evidence: "agents aren't wrong, they're missing something — you just look for the missing piece." You hunt the missing piece in the *output*, but a missing-context failure is caused by a missing piece in the *input*. Your fix loop runs on the wrong side of the interface — the strongest single datum in the whole profile. The prior analysis called this domain Prompt Craft, saw your 31-framework skill, and ranked you strong. Frameworks are rhetoric; they don't select context. Fluency masked the gap.

**In your day.** Every offload — script, research digest, skill definition — has a context-selection moment: which files, which constraints, which assumptions to correct in advance. Currently opportunistic. The domain makes it deliberate: when output comes back missing something, the first question is *did you fail to supply it*, before *what did the agent drop*.

**Block training.** No separate timed step — trained through the spec step (constraints and unknowns are context decisions) and the forensic moves: omission counter-interrogation and spec-gap reverse-spec produce direct supply-failure evidence. If those classes dominate the ledger, Context Supply rises to #3 in Block 2. Later drill: adversarial context-minimization — give the agent only minimum context, see what breaks, learn which context earns its tokens.

### 5. Build Systems

**What it is.** Your infrastructure skill — custom skills, MCP servers, workflows — repurposed as the factory that builds the practice instruments, not a standalone domain to train.

**Why it's structured this way.** You're already strongest here; training it directly is low-yield. But it's your highest-leverage asset because it converts private skill into enforced process: a better prompt improves one task, a built skill improves every future trigger of it — and doesn't rely on you remembering. Exactly what the weakest domain needs: you don't need to remember a forensic move if a custom skill runs it.

**In your day.** Building the block's own instruments: ledger template + query script, error-seeding protocol (fresh-session seeder with key files), preflight skill surfacing misfire-library checks before opening an agent, reverse-spec skill for the forensic moves. Time spent here is in your strongest domain; output multiplies the weakest.

**Block training.** None scheduled — it's the delivery vehicle for ranks 1–4. Once the instruments exist, it graduates from "domain to schedule" to "infrastructure you just use."

### 6. Learning Craft

**What it is.** If it ever earns a slot: making agent-assisted self-teaching produce durable, retrievable knowledge — Socratic loops, self-quizzing, spaced review — instead of fluent-feeling consumption that evaporates.

**Why it's sixth (and might be nothing).** The evidence is one fact: you self-teach at high volume. Nothing shows retention failure, application failure, or dissatisfaction with learning outcomes. The prior analyst ranked it #4 on genre convention (fluency-trap lore), not on your data. It stays only as a watch-list, because the link to Verification is real: your verification deficit matters most in the domains you learn at high volume.

**How it gets probed.** One 5-minute unprompted recall check in the Week-4 close-out on material learned through the block. No recall → it earns a Block 2 slot. Solid recall → it stays parked.

### The through-line

Read as a chain: **Decomposition** makes the intent real → **Context Supply** makes it visible to the model → **Prediction** audits the handoff before the run → **Verification** audits the output after it → **Build Systems** automates what you'll forget → **Learning Craft** decides whether the loop leaves you smarter. The block trains it worst-first, not easiest-first.