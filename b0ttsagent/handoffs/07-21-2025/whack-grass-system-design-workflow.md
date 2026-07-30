# Whack Grass — System Design Workflow

**Date:** 07-21-2025  
**Project:** Whack Grass (Roblox simulator)  
**Context:** Grilling session to design a workflow for filling out Game Design Docs for all Project Systems

---

## What was accomplished

### Discovery
- Explored `C:/Development/GameProjects/Whack Grass/Rojo/Game Design Docs/Main/` — **~70 markdown docs** across 4 categories:
  - **Project Systems** (~25) — actual game systems. These are the target.
  - **Project Library** (~10) — content/data entries (boosts, enchants, grass colors). NOT systems.
  - **Project Strategies** (~7) — marketing/retention/launch plans. NOT systems.
  - **Development Framework** (~20) — planning process docs. NOT systems.
- **16 docs are completely empty**, ~50 are 1–7 line stubs, ~10 have real content. Most "systems" are currently near-empty.

### Decisions locked in

1. **Scope:** Only **Project Systems** (~25 docs) get the full treatment. Library/Strategy/Framework are excluded.
2. **Output per system doc:** 4 sections prepended:
   - Dependencies (map with execution waves)
   - Interface (exposes/consumes)
   - User Story (3+ sentence narrative)
   - Risks & Edge Cases (min 2, each with severity)
3. **Original notes:** Pushed to bottom of each doc under `## Original Notes` — exact treatment (leave untouched vs. clean up) is **deferred**.
4. **Master architecture doc:** Session 0 produces `Project Systems/Systems Architecture.md` with 3 sections:
   - Canonical system index (name, one-liner, status)
   - Dependency DAG → execution waves
   - Rough interface cross-reference table (who exposes what, who consumes it)
5. **Per-system loop (v2):**
   ```
   1. Agent loads Systems Architecture.md
   2. Agent asks 2–4 targeted questions based on DAG context
   3. You answer
   4. Agent proposes full 4-section draft
   5. You give feedback / request changes
   6. Agent asks clarifying Qs about your feedback
   7. Agent revises draft
   8. Repeat 5–7 until done
   9. Agent updates Systems Architecture.md (new systems, refined deps, interface changes)
   ```
6. **Completion gate:** Completeness checklist (specific checklist items **not yet defined**, deferred from Q11).
7. **Skill decision:** Prototype the loop on 2–3 systems first, then decide whether to turn it into a skill.
8. **Sub-docs / folders:** User will simply point agent to whichever doc/folder they want to discuss — no special rules needed.

---

## Open decisions (for next session)

| # | Question | Status |
|---|---|---|
| Q7 | Section format — exact markdown template for the 4 sections | **Deferred** |
| Q9 | Original notes — leave untouched vs. agent cleans them up for readability | **Deferred** |
| Q11 | How should Session 0 run? Same Q→Draft→Feedback loop, or a different approach? | **Was about to be answered** when handoff triggered |
| — | Completeness checklist — what specific items gate "done"? | **Deferred** from Q11 |
| — | Prototype order — which 2–3 systems to prototype the loop on? | **Not yet discussed** |
| — | Skill vs. ad-hoc — final decision after prototyping | **Deferred** |

---

## Key files and paths

| Path | Description |
|---|---|
| `C:/Development/GameProjects/Whack Grass/Rojo/Game Design Docs/Main/Project Systems/` | All ~25 system docs (stubs, empty, and filled) |
| `C:/Development/GameProjects/Whack Grass/Rojo/Game Design Docs/Main/Project Systems/Systems Architecture.md` | Master architecture doc — **to be created in Session 0** |
| `C:/Development/GameProjects/Whack Grass/Rojo/Game Design Docs/` | Root of the Obsidian vault |

### Notable existing docs by completeness

- **Has real content:** Build Steps (Dev Log) — 33 lines, Planning Step 2 Documentation — 60 lines, Index Machine — 18 lines, Launch Strategy — 51 lines, Notifications — 9 lines, Incubator — 6 lines
- **Stubs (1–3 lines):** Quests, Trading, Areas, Leaderboard + Rewards, Teleporting, Weapon Investor, Group Rewards Chest, various Inventory sub-docs
- **Empty (0 bytes):** Weapon Enchanting, Weapon Unboxing, Trading Plaza, Inventory.md, Grass Spawning, Achievements, Eggs.md, Boost Items.md, Potions.md, Infinity Pack, Elite Limited Crates, and several others

---

## Suggested skills for next session

- **grill-me** — to continue the grilling where it left off (Q11: how Session 0 runs, plus remaining open questions)
- **create-context-doc** or **create-planning-docs** — if user wants to formalize the workflow into a CONTEXT.md / PLAN.md before executing
- **write-a-skill** — once the prototype is validated, to capture the loop as a reusable skill

---

## Next session focus

Per user's stated intent: pick up the grilling where it left off. The immediate next question is **how Session 0 (producing Systems Architecture.md) should run** — same per-system Q→Draft→Feedback loop or a different top-down approach. After that, resolve the remaining deferred items (section format, original notes treatment, completeness checklist, prototype order).
