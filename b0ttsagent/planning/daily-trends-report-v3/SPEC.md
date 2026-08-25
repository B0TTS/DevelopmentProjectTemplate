# Spec — daily-trends-report v3: orchestrator context efficiency

## Problem Statement

The orchestrator — the agent the user spawns with the `daily-trends-report` skill loaded — accumulates too much context over a single run because it is the one *doing* the phase-level work, not just coordinating it. Today it personally fetches the Hacker News and GitHub Trending anchors into its own context, reads the research-wave reference to author the wave spec and later the gap-fill spec, drags the frozen routing output back into context to build the gap-fill prompt, and reads the report to assemble the index and chat pointer. Over a run the heavy, disposable artifacts (anchor page content, inventory, routing decisions) all transit the long-lived orchestrator context. The user wants the orchestrator to stay thin — a conductor that spawns phase leads, receives compact summaries, and keeps most of the work (and therefore most of the context) inside disposable subagent contexts.

## Solution

Restructure the run from "orchestrator executes most steps directly" into "orchestrator sequences a chain of lead-owned phases, each with a self-contained prompt that returns only a compact summary." The deterministic layer (the two scripts that own identity, routing, and verification) is left completely untouched, and the on-disk day-folder contract is unchanged — so a reader sees the exact same report as before. The change is purely in *who runs which phase and whose context absorbs which artifact*:

- A new **Explorer** agent owns the setup (inventory + wave-spec authoring).
- A **lead-researcher + two researcher leaves** own the anchors fetch (HN + GitHub Trending), stitched into a single `anchors` file.
- The **smart general agent** owns routing + gap-fill.
- The **writer** (smart general agent) is unchanged — wording only from the frozen routing output.
- The **orchestrator** keeps only the final ship phase (verify, index, chat pointer) and the act of sequencing phases.

Each phase's instructions live in a self-contained prompt or spec the phase agent reads itself, so the orchestrator only ever loads the top-level runbook to coordinate.

## User Stories

1. As the orchestrator, I want to spawn a dedicated Explorer agent for setup rather than do it myself, so that the inventory results and wave-spec authoring stay out of my context window.
2. As the orchestrator, I want the Explorer agent to run the inventory build and report back only a count and any edge-case warnings, so that I never read the inventory contents.
3. As the orchestrator, I want the Explorer agent to author the wave spec by path-reference only, so that the spec lands on disk without the anchors or inventory contents ever entering my context.
4. As the orchestrator, I want the anchors fetch to be handled by a lead-researcher I spawn directly, so that the Hacker News and GitHub Trending page content lives and dies inside leaf contexts and never reaches me.
5. As the orchestrator, I want the anchors wave to fan out two researcher leaves (one per source), so that each heavy fetch is isolated in its own disposable context.
6. As the anchors lead-researcher, I want each leaf to write its raw source list to its own file and return only a count, so that I can quality-check existence and non-emptiness without reading page content.
7. As the anchors lead-researcher, I want to stitch the two leaf outputs into a single anchors file, so that every downstream contract that references one anchors filename keeps working unchanged.
8. As the orchestrator, I want the Explore phase and the anchors wave to run as parallel siblings with a single join before research, so that setup completes faster without either depending on the other's contents.
9. As the orchestrator, I want to hand routing and gap-fill to the smart general agent, so that reading the frozen routing output (exclusions, prior identities, survivor counts) happens in a disposable context, not mine.
10. As the routing agent, I want to run the route command and read survivors-per-section from its output, so that I can decide the single gap-fill wave mechanically rather than by judgment.
11. As the routing agent, I want to build the gap-fill spec from the frozen routing output's exclusions, prior identities, and empty domain hints, so that the gap-fill wave targets exactly the thin sections without re-proposing already-surfaced identities.
12. As the routing agent, I want to enforce "exactly one gap-fill wave, then stop," so that a thin day ships short rather than looping.
13. As the routing agent, I want to declare the routing output frozen at the end of my phase, so that the writer's input is unambiguous and instrumental.
14. As the orchestrator, I want the writer phase to remain unchanged (spawn the smart general agent with the frozen routing output and the report contract), so that wording stays a pure, isolated step.
15. As the writer, I want the frozen routing output and the report contract to be the only things I read, so that I word from decisions already made and never re-research or re-route.
16. As the orchestrator, I want to keep only the ship phase for myself (run verify, one rewrite at most, upsert the index, post the chat pointer), so that I remain the run's closing voice with minimal context.
17. As the report reader, I want the finished daily digest to be byte-for-byte equivalent in shape to today's (same sections, same fields, same glance block, same word budget), so that the refactor is invisible to me.
18. As the user, I want the deterministic routing rules (identity, streak gate, 7-day window, update test, Still circulating) to be enforced by the same scripts as before, so that the refactor changes orchestration only and never changes report semantics.
19. As the user, I want the existing fixture scenarios to still pass against the unchanged scripts, so that there is hard proof the behavioral layer was not disturbed.
20. As a phase agent, I want my task prompt to be fully self-contained, so that I can complete my phase without inheriting the skill's entire reference library into my context.
21. As the orchestrator, I want the top-level runbook to be the only thing I load at runtime, so that the reference docs become phase-owned rather than orchestrator-owned.
22. As a phase agent, I want a precise "who may write what" boundary, so that I only touch my assigned paths and never a frozen or script-written file.
23. As the user, I want a new dedicated Explorer agent definition rather than a generic agent wearing an explorer hat, so that the setup phase has a tuned prompt sized to its job and is cheap to spawn every run.
24. As the user, I want the existing lead-researcher, researcher, and general-agent definitions to be reused unchanged where they fit, so that only the genuinely new role adds a definition.
25. As the orchestrator, I want each phase to return a bounded summary (a few lines or a capped word count), so that coordination cost stays small even with more phases.
26. As a phase agent encountering a failed leaf or missing output, I want to retry exactly once then record the gap, so that no phase ever fabricates work to fill a hole.
27. As the user, I want same-day reruns, thin days, and gap-fill caps to behave identically to today, so that the refactor does not regress any edge case the existing fixtures cover.
28. As the user, I want the refuse list and manual-invocation behavior to stay exactly as they are, so that the skill's trigger boundaries are unaffected by an orchestration change.

## Implementation Decisions

- **The orchestrator becomes a thin conductor.** It spawns phases in sequence and keeps for itself only the ship phase (verify, one rewrite, index upsert, chat pointer). It never reads anchors, inventory, or the frozen routing output; heavy artifacts live only inside phase-agent contexts.
- **A new Explorer agent is introduced** as a dedicated setup agent (not a generic agent wearing an explorer hat). Its job is confined to: run the inventory build command, then author the wave spec from the template using path-references only (no runtime reads of anchors or inventory contents). This lifts the v2 "no new agent definitions" freeze — deliberately, once, because the role is spawned every run and earns a tuned prompt.
- **Setup is split into two parallel siblings joined before research.** (a) the Explorer phase producing the inventory and the wave spec; (b) the anchors wave producing the anchors file. Neither depends on the other's contents, but both must exist before the research phase's leaves run.
- **Anchors become a lead-coordinated wave of two researcher leaves.** The lead-researcher spawns one leaf for the Hacker News front page and one for GitHub Trending; each leaf fetches raw title/link (or repo/link) lists into its own file and returns only a count. The lead quality-checks the files and stitches them into a single anchors file, preserving the existing single-filename contract.
- **Routing + gap-fill move to the smart general agent.** This phase runs the route command, reads survivors-per-section, and if any section has too few survivors author the single gap-fill spec from the frozen routing output's exclusions, prior identities, and empty domain hints — then re-spawn the research lead for the thin section, re-route, and stop. No third wave.
- **The writer phase is unchanged.** The smart general agent receives the frozen routing output plus the report contract and performs wording only.
- **Ship stays with the orchestrator** because it is the run's user-facing close: run verify, allow at most one writer rewrite on a hard failure (then ship with a "verify failed" note), upsert the index, post the path plus exactly three glance bullets and the demoted count when non-empty.
- **The deterministic layer is untouched.** Identity normalization, the streak gate, the 7-day window, the update test, routing destinations, the Still circulating cap and sort, the domain preference notes, and the verify errors/warnings all remain owned by the existing two scripts. No routing or report-semantics change is in scope.
- **Phase prompts are self-contained.** Each phase agent receives, in its spawn message or a spec it reads, everything it needs (commands, template, schema, output paths, caps, QA checklist, return format). This is what lets the orchestrator load only the top-level runbook at runtime.
- **The on-disk day-folder contract is unchanged.** The same artifacts, same writers-of-record, same frozen-file rules, and the same "scripts are the executable truth, never hand-edited" discipline carry forward verbatim.
- **Write boundaries carry forward.** Leaves and leads write only their assigned paths inside the day folder; only the writer writes the report; only the scripts write the inventory and routing files.

## Testing Decisions

**What makes a good test here:** test external behavior, not orchestration internals. A refactor of *who runs which phase* succeeds or fails by the on-disk outcome — a complete run produces a valid day folder whose report passes verification — not by how many spawns occurred. Context-efficiency claims are validated by instruction-and-doc checks (bounded summaries, self-contained prompts), not by fixture runs.

**The single highest seam:** the verification gate plus the day-folder layout. Because the deterministic scripts and the report contract are unchanged, the acceptance boundary is unchanged: a full run (regardless of how phases are sequenced) must yield an `inventory`, `anchors`, three leaf outputs, a frozen routing output, a `report`, and an upserted index, and the verify command must exit 0 (or exit 1 → exactly one rewrite → ship with a note).

**Existing seams reused (zero new deterministic seams):** the two scripts remain the executable truth; the existing fixture scenarios (first run, streak collision, older-than-window, undated, update-test, same-day rerun, thin day, and the routing/verify checks) must still pass with no script edits. Running them against the untouched scripts is the proof that the behavioral layer was not disturbed.

**Modules under test:**
- The two deterministic scripts — regression only, via the existing fixture set; expect zero changes and zero new fixtures needed at this layer.
- The new phase orchestration — validated by a fresh end-to-end run through the new runbook that produces verify-passing output; plus a doc-level pass that each phase's prompt is self-contained and each phase returns a bounded summary.
- The new Explorer agent definition — validated as a loaded, spawnable subagent whose prompt matches the setup phase's job.

**Prior art:** the existing fixture scenarios and the script-review/fixture-build flow defined in the v2 plan are the model; the writer's already-self-contained prompt (frozen routing output + report contract in the spawn message) is the template for making the Explorer and routing prompts self-contained.

## Out of Scope

- Any change to the deterministic routing rules, identity normalization, gates, update test, or verification checks.
- Any change to the report skeleton, item fields, glance block, word budget, or Still circulating rules.
- Any change to the three main sections or the coverage-domain hint lists.
- Any change to the 7-day window, the canonical timezone, or the per-leaf search/read caps.
- Scheduling, cron, or automatic invocation — the skill remains manual-only.
- Personalization, tracker publishing, weekly recaps, or any refuse-list change.
- Introducing a state database or moving off the "report files are the source of truth" principle.
- Any dual-harness path; the runtime stays opencode.
- Rewriting the scripts "for clarity" — they stay as-is unless a fixture run proves a defect.

## Further Notes

- The v2 planning docs (context, plan, and their amendments) are frozen; this spec is the v3 change on top and lives alongside them, not as a rewrite.
- The coordination-overhead tradeoff is accepted deliberately: more phases means more spawn handoffs, but subagent contexts are disposable, so total *orchestrator* context drops sharply even if the sum across all phase contexts is mildly higher.
- The two open confirmations from the design discussion are resolved here as decisions, pending user acceptance: (1) the Explorer is a new dedicated agent definition, and (2) the anchors wave writes two leaf files that the lead stitches into the single anchors file.
- Because the scripts and report contract are untouched, the expected regression surface is near-zero; the risk the fixtures guard against is accidental drift in the runbook or in a phase prompt that changes where an artifact lands or which agent writes it.