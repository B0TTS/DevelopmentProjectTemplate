# Streaming Schedule Redesign — V4.2

## Summary

The current streaming setup (Streaming Dev POW on Mon/Wed/Fri + MC Hardcore POF on Wed/Sat) is being scrapped entirely. The new design replaces it with two stream types, both classified as **POF** (Part of Freetime — competes with Gym, relaxation, etc.).

A grill session was in progress when the handoff was requested. The grill walked through POW vs POF classification, duration, prep time, and began exploring day placement. The day-placement decision is the main open item remaining.

## Reference Docs

- `b0ttsagent/Notes/Schedule Architecture V4.1.md` — the master schedule architecture doc; all existing tasks, requirements, and design philosophy live here
- `b0ttsagent/Notes/weekly-schedule.md` — the full per-day breakdown with POW/POF/Sleep tables, flex calculations, and day-by-day task matrices

## Decisions Locked In

| Decision | Answer |
|---|---|
| **Old streams** | Scrap both Streaming Dev (POW) and MC Hardcore (POF) entirely |
| **Classification** | Both Normal and Chill = **POF** |
| **Normal streams** | 2x/week guaranteed, 30min prep + 1.5h stream = **2h total each** |
| **Chill streams** | 2x/week, 30min prep + 1.5h stream = **2h total each** |
| **Channels** | Separate channels — Normal on one, Chill on another (fried/chill vibe would hurt brand identity on main) |
| **Gap rule** | ≥1 day between same-type streams (Normal→Normal, Chill→Chill). Different types CAN be back-to-back (Normal Mon + Chill Tue = valid) |
| **Chill day restriction** | Chill can only go on **Mon, Wed, Fri, Sat** |
| **Normal day restriction** | No restriction — any day Mon–Sat |
| **Total weekly streaming** | 8h POF (was 6h POF for MC Hardcore — net +2h POF) |
| **Sunday** | No streams on Freeday (0h POW, 16h POF, unstructured) |

## Open Decision: Day Placement

This is the main thing the next session needs to resolve. The constraints are:

1. **2 Normal days** from Mon–Sat, with ≥1 gap day between them
2. **2 Chill days** from {Mon, Wed, Fri, Sat}, with ≥1 gap day between them
3. Same-day double-stacking (Normal + Chill same day = 4h POF) is allowed but tight
4. **Minimize impact on already-tight gym days**

### The POF landscape (after removing old streams)

| Day | Fixed POF | +1 Stream (2h) | Flex POF remaining | Notes |
|---|---|---|---|---|
| **Mon** | 3.17h | 5.17h | **2.83h** | Roomiest day |
| **Tue** | 5.17h | 7.17h | **0.83h** ⚠️ | Gym day |
| **Wed** | 3.17h | 5.17h | **2.83h** | Roomiest day |
| **Thu** | 5.17h | 7.17h | **0.83h** ⚠️ | Gym day |
| **Fri** | 5.17h | 7.17h | **0.83h** ⚠️ | Gym + Skill Study + already tightest POW day (only 1.5h flex Work) |
| **Sat** | 3.33h | 5.33h | **2.67h** | Weekly Review + Goals, dehumidifier |
| **Sun** | 2.25h | — | — | Freeday — no streams |

### Option A: Normal = Mon + Thu, Chill = Wed + Sat

- Normal gap: Mon→Thu (3 days ✓), Thu→Mon (4 days ✓)
- Chill gap: Wed→Sat (3 days ✓), Sat→Wed (4 days ✓)
- No same-day stacking
- POF remaining after streams: Mon 2.83, **Thu 0.83**, Wed 2.83, Sat 2.67
- **Tradeoff**: Thursday is tight (50min flex). Only one tight day.

### Option B: Normal = Mon + Sat, Chill = Wed + Fri

- Normal gap: Mon→Sat (5 days ✓), Sat→Mon (2 days ✓)
- Chill gap: Wed→Fri (2 days ✓), Fri→Wed (2 days ✓)
- No same-day stacking
- POF remaining: Mon 2.83, Sat 2.67, Wed 2.83, **Fri 0.83**
- **Tradeoff**: Friday is tight (50min flex). Friday is already the tightest POW day (only 1.5h flex Work). Tight on both fronts.

### Option C: Normal = Tue + Fri, Chill = Mon + Wed

- Normal gap: Tue→Fri (3 days ✓), Fri→Tue (4 days ✓)
- Chill gap: Mon→Wed (2 days ✓), Wed→Mon (2 days ✓)
- No same-day stacking
- POF remaining: **Tue 0.83**, **Fri 0.83**, Mon 2.83, Wed 2.83
- **Tradeoff**: Two tight days (Tue + Fri). Both are gym days.

### Option D: Normal = Mon + Thu, Chill = Fri + Sat

- Normal gap: Mon→Thu (3 days ✓)
- Chill gap: Fri→Sat (1 day ✓️ — different type from Normal so no back-to-back concern with Thu→Fri)
- Wait — Chill Fri→Sat IS back-to-back Chill. **Violates gap rule.** Invalid.

### Option E: Normal = Wed + Sat, Chill = Mon + Fri

- Normal gap: Wed→Sat (3 days ✓), Sat→Wed (4 days ✓)
- Chill gap: Mon→Fri (4 days ✓), Fri→Mon (3 days ✓)
- No same-day stacking
- POF remaining: Wed 2.83, Sat 2.67, Mon 2.83, **Fri 0.83**
- **Tradeoff**: Friday tight again. But only one tight day.

### The core tension

A Chill stream must go on Fri or not at all if we want to avoid tight Fridays. But Chill is restricted to {Mon, Wed, Fri, Sat} — so we could do Chill = Mon + Wed, but then Normal's 2 slots need ≥1 day apart and avoiding Friday tightness pushes Normal to something like Tue + Thu or Tue + Sat, both of which put streams on gym days.

**Key question for next session**: Which is worse — a tight Friday (already a heavy day) or putting streams on two gym days?

## Suggested Skills for Next Session

- **`grill-me`** — the grill was mid-flight; resume from day-placement decision and continue through any remaining branches (prep time blocking, what content goes on which stream type, etc.)
- **`create-planning-docs`** — once day placement and all decisions are locked, write CONTEXT.md + PLAN.md for the V4.2 schedule update
- **`close`** or **`closev2`** — once everything is decided, wrap the session

## Next Session Focus (if argument provided)

- Resolve the 4 day slots for Normal/Chill
- Decide whether prep time (30min) is bundled adjacent to stream time or placed elsewhere
- Clarify what content goes on Normal vs Chill streams (dev? gaming? variety?)
- Rebuild the weekly per-day tables to reflect the new streaming layout
- Verify the 8h POF / 8h POW / 8h Sleep balance still holds on every day
