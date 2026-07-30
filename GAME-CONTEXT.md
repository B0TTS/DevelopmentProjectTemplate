# GAME-CONTEXT.md — Whack Grass

Reference doc for the Roblox game **Whack Grass**. Captures the game's design facts so future sessions can run retention/game-design brainstorming (e.g., the `roblox-retention-brainstorm-V2` skill) without re-eliciting the basics from the user. Project-wide agent rules live in `AGENTS.md` (cite by path, not duplicated here).

---

## Game Overview

- **Title:** Whack Grass *(working)*
- **Platform:** Roblox
- **Genre:** Simulator, Pet Simulator 99 (PS99) style
- **Status:** In planning — systems are tentative and flexible unless marked otherwise
- **Target audience:** Young, PS99-style (~8–12 years old)

## Core Loop

Equip weapons → **cut (whack) grass** → sell grass for money → unbox better weapons → cut more/better grass → repeat. The minute-to-minute verb is *cutting grass with weapons*. Progression comes from better weapons unlocking access to higher-value grass in higher-tier zones.

## Key Mechanics

- **Multi-weapon equip:** Up to ~20 weapons equipped simultaneously; multi-weapon grass cutting is the signature mechanic. This is a primary axis for exclusivity in retention ideas.
- **Weapon unboxing:** Weapons come from unboxing crates bought with money (the loop's spend step).
- **Grass:** Has **tiers** (by zone — higher zones = higher-tier grass), **rarities**, and **colors/types**. Color-typing gives weapons matchup bonuses against specific grass colors, making the up-to-20-weapon equip a strategic *diversification* decision (equip across colors, not just stack power). Resolved during a mid-term retention brainstorm.
- **Zones/areas:** Progression-gated areas to explore; each zone has its own grass tier/ecosystem. Zones are gated by **cash + quest** (PS99-style: pay a cash threshold and complete a quest objective to unlock the next zone).
- **Failure state:** **None.** The core loop is pure chill cutting — no damage, health, or ejection. Retention ideas must work without stakes; push-your-luck / survival / gauntlet systems are ruled out.
- **Pets (functional):** Pets boost cutting and sell value (PS99-style), not cosmetic-only. **Eggs** are the acquisition loop (obtained → incubated → hatched → pet).
- **Rebirth (PS99-style, maybe):** Reset zone progress while keeping weapons/inventory; gain permanent bonuses (more equip slots, luck, damage). Whether rebirth ships is **undecided** — but designing the economy with rebirth in mind now avoids painful retrofits later.

## Planned Systems

Tentative feature list (not final — each may be cut or reshaped during planning):

- Achievements
- Quests (PS99-style)
- Items
- Boost items
- Potions
- Clans
- Trading
- Competitive leaderboards
- Egg incubator (eggs/pets) — primary *daily retention* system

## Monetization

Aggressive, PS99-style (Robux-heavy). Confirmed revenue vectors:

- **Gamepasses** (permanent perks)
- **Limited crates** (time-limited weapon crates)
- **Items** (purchasable in-game items)
- **Infinity packs** (recurring-purchase bundles)

For retention-idea purposes: every idea's Monetization field should lean into this stance honestly. If monetizing a given idea would hurt the mechanic, say "better left free" rather than forcing it.

## Target Session Length

**60 minutes** is the design target for a typical session. Use this to calibrate scope boundaries in retention brainstorming (e.g., mid-term = 10–60 min aligns with the core session arc; long-term = 1h+ spans multiple sessions).

## Key Terms

- **Whack** = cut (the core verb).
- **Weapon slots** = the up-to-20 equippable weapons a player holds at once.
- **Grass tiers** = zone-based grass progression (low → high).
- **Grass rarities** = rarity axis within grass (common → rare/legendary).
- **Eggs/pets** = egg incubation loop produces functional pets that boost output.
- **Rebirth** = PS99-style prestige reset (zone reset, keep weapons, permanent bonuses).
- **Infinity packs** = recurring-purchase Robux bundles.
- **PS99** = Pet Simulator 99; the genre/mechanic reference point.

## Assumptions

Decided-by-default choices — treated as decided, override if wrong:

- Grass has tiers (by zone) + rarities + colors/types (resolved — color-typing with weapon matchups is in).
- Pets are functional (boost cutting & sell value), not cosmetic.
- Infinity packs are recurring-purchase bundles (not one-time).
- Rebirth is being designed around even if it doesn't ship at launch.
- Monetization is aggressive across all systems (not a single cautious vector).

## Open Questions

Must resolve before or during deeper design. Flagged so future sessions know what to probe rather than assume:

- `[RESOLVED]` **Grass color/types** — **YES.** Grass has colors/types; weapons have matchup bonuses. Decided during a mid-term retention brainstorm. Now a primary exclusivity lever (especially for loadout-crafting ideas).
- `[NEEDS CLARIFICATION]` **Rebirth** — confirmed in or out? PS99-style if in. Currently "might add, only PS99-style."
- `[NEEDS CLARIFICATION]` **Pet equip count** — how many pets active at once? (Affects multi-pet synergy ideas.)
- `[PARTIALLY RESOLVED]` **Zone count / structure** — gating type decided: **cash + quest** (pay cash + complete a quest objective). A DPS-check “Zone Guardian” boss was proposed during brainstorming but rejected (keeps the gate chill, no failure state). Zone *count* and specifics of each gate quest remain TBD.
- `[RESOLVED]` **Combat / damage mechanic** — **No failure state.** Pure chill cutting, no damage, no death, no ejection. Retention ideas must work without stakes; push-your-luck / survival / gauntlet systems are ruled out.
- `[NEEDS CLARIFICATION]` **Egg incubation timers & slot count** — specific durations and max concurrent incubators.
- `[NEEDS CLARIFICATION]` **Clan features** — clan-specific retention systems (clan goals, clan wars, clan leaderboards) — depth TBD.
- `[NEEDS CLARIFICATION]` **Quest structure** — daily-only, or story/event chains too? PS99-style specifics TBD.

## Tooling Pointer

- **Retention brainstorming:** use the `roblox-retention-brainstorm-V2` skill at `.agents/skills/roblox-retention-brainstorm-V2/SKILL.md`. It reads game context from this doc and prior conversation; probe only the Open Questions relevant to the chosen scope.
- **Project-wide agent rules:** see `AGENTS.md` in the project root (skill invocation, nav guides, handoffs, temp files, anti-rationalization).

---

*Living document — if an assumption is proven wrong or an Open Question resolves during work, update this file before continuing. Stale context is actively harmful.*
