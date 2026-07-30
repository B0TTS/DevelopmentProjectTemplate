# Reference: Scope Definitions, Output Specs, and Rules

## The 6 retention scopes

Present this menu when the user hasn't named a scope. Each scope is anchored on **duration**; the examples are illustrative flavor, not definitional.

| Scope | Duration | Flavor / intent |
|---|---|---|
| **Micro** | seconds–few min | Hold attention *right now*. Core-loop juice + quick layered systems (auto-earning pets, mining a block, click crits, early-game rebirths). Ideas read like core-loop design, not "come back later." |
| **Short-term** | 1–10 min | A single satisfying play arc — complete a quest, pop an early achievement, do a rebirth cycle. Resolves within one short sitting. |
| **Mid-term** | 10–60 min | A meatier goal you work toward within a session — unlock a new area, earn a new pickaxe, chase a cluster of achievements. The "one good session" horizon. |
| **Long-term** | 1 hr+ (often multi-session) | The grind that keeps veterans engaged — mastery systems, end-game achievements, final area unlocks, clan competition. The thing competitive players chase for complete mastery. |
| **Daily** | per-day (24 hr cycle) | "Come back tomorrow." Login hooks, daily quests, timer-based deposit-and-wait, rotating markets/weather. The daily ritual. |
| **Weekly** | per-week (7-day cycle) | Predominantly a *strategy/cadence* layer — limited-time updates, rotating shops, seasonal arcs — but still generate genuine weekly *systems* where they fit (7-day tournaments, weekly boss raids). Be honest about the scope's nature. |

A system's **primary scope** is determined by its typical duration in the user's game (not by an example label). Systems that span scopes are **hybrid-tagged** (see below).

## Probing rules

- **Adaptive and minimal.** Extract what's already known from the user's request and prior context. Ask only to fill genuine gaps.
- **One question at a time.** Each with your recommended answer (so the user can accept fast or correct).
- **Always summarize back first** — state your read of their game before probing, so misreads surface early.
- **Floor:** always confirm the core loop + theme. You cannot generate exclusive ideas without knowing what the game actually is.
- **Ceiling:** stop probing when the next question's answer wouldn't change any idea you'd generate. Don't interrogate beyond what matters.
- Typical things that affect ideas and may warrant a question: audience age, existing systems (clans, trading, leaderboards, prestige/rebirth), resource types and tiers, monetization stance, session-length expectations. Ask only those relevant to the chosen scope and not already known.

## Output format

Every run produces three parts, in order:

1. **Ranking rationale** — one line arguing briefly for the ordering (most thematically-exclusive first; generic-but-effective lower and honestly tagged).
2. **Overview table** — one row per idea, covering *all* ideas at a glance:

   | # | Name | Concept (1 line) | Excl. |

   - `#` = rank, best-fit-first.
   - `Name` = short, evocative.
   - `Concept` = one sentence, what it is.
   - `Excl.` = exclusivity tag: `exclusive` / `semi` / `generic`.

3. **Per-idea tables** — one per idea, immediately after the overview. The idea Name is the heading (e.g., `### 1. Weather System`), followed by a 2-column table whose left column is the field and right column is the content. Use these rows, in order:

   | Field | Content |
   |---|---|
   | Concept | 1 sentence — what the system is. |
   | Scope fit | Why it fits this scope's duration/intent. |
   | Why exclusive | Exclusivity tag + why. If `exclusive`, name the specific game mechanic that makes it possible. If `semi`, the framing is exclusive, the shape is portable. If `generic`, the mechanic is portable — say so honestly. |
   | Strengths | Key upsides. |
   | Risks | Key downsides / cons. |
   | Hybrid | Other scopes touched (e.g., "long, short"), or **omit this entire row** when there are none. |
   | Monetization | Specific Robux/speed-up/gamepass angles. If forcing monetization would hurt the mechanic, write "better left free" + why. |

### Brevity rule (firm)

- **~1 line per row (~15 words).** No multi-sentence prose anywhere — not in Concept, not in Strengths, nowhere.
- **Sole exception:** the **Why exclusive** row may run **2 lines, but only when the idea is tagged `exclusive`** — that reasoning is the skill's differentiator and one line can't always carry it. For `semi` and `generic` ideas, Why-exclusive stays 1 line.
- This rule is the mechanism that kills verbosity. Enforce it; don't let rows drift back to prose paragraphs.

### Uniformity

Every idea gets the same per-idea table. No prose blocks, no top-N cutoff, no special-casing. Rank still orders everything (best-fit-first).

## Exclusivity — intent and moves

**Intent (firm):** every idea should be exclusive to the user's game — only possible because of its specific mechanics — and that exclusivity legible in the output. Generic-but-effective ideas are allowed but must be honestly tagged.

**Illustrative moves (available, never forced)** — draw on those that help, skip the rest; the model chooses per-idea:
- Build from a unique game element (not theme-on-generic).
- Test against the nearest clone and name the difference.
- Fuse theme + mechanic until inseparable.
- Exploit a specific unique mechanic as the load-bearing part of the idea.

No gate, no mandatory pipeline. An idea clears the intent if it's genuinely exclusive *or* honestly tagged generic.

## Hybrid tagging

- **Primary scope** = the scope being brainstormed, by duration.
- **Hybrid tags** = secondary scopes the idea also touches, shown only when real. If none, **omit the Hybrid row** from that idea's table.
- This skill does **not** do cross-scope gap analysis ("you're lacking in mid-term"). It only tags ideas. The user eyeballs tags to spot thin categories themselves.
- If an idea is "spread thin" across many scopes (weak in all), note that — it's a signal the user may want a dedicated system for a given scope.

## Quantity

- **No hard cap.** Don't truncate great ideas to stay under a number.
- **Soft target:** aim for ~15–20. That's calibration, not a limit.
- **Go higher when rich:** 20–30+ is welcome when a scope is rich — generate as many as you see fit.
- **Stop when padding starts.** Adding another idea that doesn't strengthen the set is worse than stopping. This is the only real ceiling — not a quota, not a number.

## Reference-game grounding

- Light, on-demand. Mention real Roblox sim games (Pet Sim 99, Bee Swarm Simulator, Mining Simulator, Clicker Simulator, etc.) only when a comparison genuinely illuminates an idea.
- Never mandatory. The exclusivity benchmark is "could any comparable incremental/sim game do this unchanged?" — not "could PS99 do it?"
- Don't anchor creativity toward a specific game's patterns.
