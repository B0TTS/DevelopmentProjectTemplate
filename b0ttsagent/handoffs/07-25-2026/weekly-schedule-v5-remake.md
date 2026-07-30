# Handoff: Weekly Schedule V5 Remake

## Summary

Ran a grill-me session to resolve every branch of the new weekly schedule before building. The user wants to remake `weekly-scheduleV4.md` using the new source data in `Schedule Architecture V4.1.md`. Every structural decision was walked down and resolved — the full spec is now locked and ready to build.

## What was accomplished

- Loaded and diffed both `weekly-scheduleV4.md` (current) and `Schedule Architecture V4.1.md` (new source)
- Resolved all ambiguities in V4.1 through one-at-a-time grilling (10 questions)
- Reached shared understanding on every task, frequency, duration, category, and structural rule
- Produced a complete task inventory ready for document construction

## Resolved decisions (what changed from V4 → V5)

| Decision | Resolution |
|---|---|
| **Sunday structure** | Fully unstructured, same as V4 (0 POW / 16 POF / 8 Sleep). Lightweight anchors stay (Breakfast, Moral Code Review, Skate). "Completely free day" means free of work obligations. |
| **Morning Ritual** | 6x Mon–Sat, 1.5hr capped container. Sub-tasks: 30m meditation (daily), 30m manifestations (Mon/Wed/Sat only), 15m clear air, remainder for brush teeth/etc. On non-manifestation days (Tue/Thu/Fri), brush teeth gets 45m; on manifestation days, 15m. |
| **Clear out air** | Sub-task of Morning Ritual Mon–Sat. On Sunday: no-stress whenever, just a recommendation — not modeled in the schedule. |
| **Sunlight** | Now conditional/optional (Option C). Listed as 0–1hr POF, Mon–Sat. Skip if enough sunlight was gotten during the morning ritual meditation at 8am. Not hard-coded into the hour totals — Extra Freetime absorbs whatever isn't used. |
| **POF target** | Stays rigid 8/8/8 model (8h POW / 8h POF / 8h Sleep). The V4.1 "3–4hr floor" note is just a floor, not structural. |
| **Mobile Gaming (NEW)** | POW, 6x Mon–Sat, 30m. Task #16 in architecture doc ordering. |
| **PC Gaming (NEW)** | POW, 6x Mon–Sat, 30m. Task #17 in architecture doc ordering. |
| **Gaming placement** | Follow natural architecture doc flow — both come after End of Day Ritual in the task order. |
| **Skill Study** | 3x Tue/Thu/Fri, 1.5hr (the requirements-section line saying "Wed/Sat/Sun" was stale — user removed it). |
| **Gym** | 3x Tue/Thu/Fri, 2hr (unchanged from V4). |
| **Streaming Development** | 3x Mon/Wed/Fri, 3hr (unchanged). |
| **Streaming MC Hardcore** | 2x Wed/Sat, 3hr (unchanged). |
| **All other tasks** | Unchanged from V4 frequencies/durations. |

## Complete task inventory for V5 build

### POF tasks
| Task | Freq | Duration | Notes |
|---|---|---|---|
| Morning Ritual (container) | 6x Mon–Sat | 1.5hr | Sub: meditation 30m, manifestations 30m (Mon/Wed/Sat only), clear air 15m, brush teeth/etc remainder |
| Sunlight | 6x Mon–Sat | 0–1hr | Conditional — skip if enough during morning ritual; not hard-coded |
| Make & Eat Breakfast | 7x daily | 1hr | Moveable |
| Moral Code Review | 1x Sun | 15m (0.25hr) | |
| Cleaning (quick) | 6x Mon–Sat | 10m (~0.17hr) | |
| Clean Dehumidifier | 1x Sat | 10m (~0.17hr) | Spray, sit 10-15m, wash, dry |
| Go Gym | 3x Tue/Thu/Fri | 2hr | |
| Skate | 1x Sun | 1hr | Travel time not included |
| Streaming MC Hardcore | 2x Wed/Sat | 3hr | 1hr prep + 2hr stream |
| Extra Personal Freetime | flex | fills to 8hr POF | |

### POW tasks
| Task | Freq | Duration | Notes |
|---|---|---|---|
| Planning | 6x Mon–Sat | 30m (0.5hr) | |
| Game Ideation | 6x Mon–Sat | 30m (0.5hr) | |
| Skill Study | 3x Tue/Thu/Fri | 1.5hr | |
| Streaming Development | 3x Mon/Wed/Fri | 3hr | 1hr planning/study + 2hr streaming |
| Weekly Review + Goals | 1x Sat | 1hr | 30m review + 30m goals/plans |
| End of Day Ritual | 6x Mon–Sat | 1hr | 15m dev forum + 15m AI reports + 30m work review |
| Mobile Gaming | 6x Mon–Sat | 30m (0.5hr) | NEW — play at least 1 new game/week |
| PC Gaming | 6x Mon–Sat | 30m (0.5hr) | NEW — play at least 1 new game/week |
| Work (flex) | flex | fills to 8hr POW | |

### Sleep
| Task | Freq | Duration |
|---|---|---|
| Sleep | 7x daily | 8hr |

## Task ordering (from architecture doc)

1. Morning Ritual (POF)
2. Sunlight (POF, conditional)
3. Moral Code Review (POF, Sun only)
4. Make & Eat Breakfast (POF)
5. Weekly Review + Goals (POW, Sat only)
6. Planning (POW)
7. Game Ideation (POW)
8. Cleaning (POF)
9. Clean Dehumidifier (POF, Sat only)
10. Go Gym (POF)
11. Skate (POF, Sun only)
12. Skill Study (POW)
13. Work (POW, flex)
14. Streaming Development (POW)
15. End of Day Ritual (POW)
16. Mobile Gaming (POW) ← NEW
17. PC Gaming (POW) ← NEW
18. Streaming MC Hardcore (POF)
19. Extra Personal Freetime (POF, flex)
20. Sleep

## Open considerations for the builder

- **Friday is very tight.** Fixed POW with the two new gaming tasks = 7.5hr, leaving only 0.5hr flex Work. The user said they want to see the full document first, then adjust. Don't try to fix it — just surface it prominently in the insights.
- **Morning Ritual changed from 1hr to 1.5hr.** This adds 0.5hr of POF every day, squeezing Extra Freetime by the same amount. The daily POF math shifts.
- **Sunlight as conditional (0–1hr).** Model it in the tables but note it as optional. Don't hard-code it into the POF totals since Extra Freetime absorbs the variance.
- **Manifestations sub-task is Mon/Wed/Sat only.** This affects the Morning Ritual's internal allocation on those days vs Tue/Thu/Fri. The user confirmed the 1.5hr is a capped container — the internal distribution adjusts but the container duration doesn't change.
- **Mobile Gaming and PC Gaming are POW.** The user was firm on this. They count as work time.

## Key files

| File | Role |
|---|---|
| `b0ttsagent/Notes/Schedule Architecture V4.1.md` | **Source of truth** — the new architecture spec |
| `b0ttsagent/Notes/weekly-scheduleV4.md` | **Template to follow** — same structure (legend, master summary, per-day tables, breakdown tables, task matrix, weekly ranking, insights) but with V5 data |
| `b0ttsagent/Notes/weekly-scheduleV5.md` | **Output** — the new schedule to create |

## What to build

Rebuild the weekly schedule document using the same table/structure format as `weekly-scheduleV4.md` (legend, master summary, per-day ordered schedules, POW breakdown, POF breakdown, Sleep breakdown, task-to-day matrix, weekly hours ranked, insight highlights) but with all the V5 changes above.

The user wants to see the full document before making further adjustments.

## Suggested skills for next session

- **create-nav-guide** — the user might want to doc the final schedule as a reference
- **mermaid-diagrams** — if any visual dependency/timeline diagrams would help
