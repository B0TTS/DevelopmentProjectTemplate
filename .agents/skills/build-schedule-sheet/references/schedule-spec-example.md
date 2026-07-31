# Schedule Spec Example V4.1 (worked reference)

This is the canonical `Schedule Architecture V4.1` schedule translated into the `schedule-spec` contract (`format_version: 1`). It serves two roles:

1. A **reference** authors copy and edit from when bumping a schedule version (real specs will look like this).
2. The **validation fixture** the skill's scripts are run against as the "clean valid" scenario.

It is intentionally a *reference*, not a blank template — for a blank skeleton see `assets/schedule-spec-template.md`.

Prose here is supporting context only. The JSON block below is authoritative. Note that **Streaming MC Hardcore** is split into two guarded ids (`streaming-mc-hardcore` required Thursday + `streaming-mc-hardcore-optional` NR Sunday) because the same activity has a required instance one day and a Not-Required instance another; this reproduces the source accounting exactly.

```schedule-spec
{
  "format_version": 1,
  "content_version": "4.1",
  "calendar": {
    "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
    "free_day": "sun"
  },
  "budgets": {
    "work_day": { "POW": 480, "POF": 480, "Sleep": 480 },
    "free_day": { "POW": 0, "POF": 960, "Sleep": 480 }
  },
  "tasks": [
    {
      "id": "morning-ritual",
      "name": "Morning Ritual",
      "order": 1,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 90,
      "subtasks": [
        { "name": "Meditation", "duration_minutes": 30, "days": ["mon", "tue", "wed", "thu", "fri", "sat"], "notes": "Sit idle, no distractions. Keeps mind clear. 8am = easy sunlight." },
        { "name": "Manifestations/Affirmations", "duration_minutes": 30, "days": ["mon", "wed", "sat"] },
        { "name": "Clear out air", "duration_minutes": 15, "notes": "15m per the guide." },
        { "name": "Brush teeth / etc", "duration_minutes": 15, "days": ["mon", "wed", "sat"], "notes": "Remainder of the 1.5h container. 15m on manifestation days (Mon/Wed/Sat), 45m on Tue/Thu/Fri." }
      ],
      "notes": "1.5h capped container, Mon-Sat. Per-day variance in subtasks, so the uniform subtask-sum check is intentionally skipped (see schedule-spec-contract.md)."
    },
    {
      "id": "sunlight",
      "name": "Sunlight",
      "order": 2,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "conditional": { "max_minutes": 60 },
      "notes": "0-1h. Skip if enough sunlight was gotten during the 8am Morning Ritual. Conditional; not counted toward the 8h POF total by default; draws down Extra Personal Freetime when taken."
    },
    {
      "id": "moral-code-review",
      "name": "Moral Code Review",
      "order": 3,
      "category": "POF",
      "days": ["sun"],
      "duration_minutes": 15
    },
    {
      "id": "breakfast",
      "name": "Make and Eat Breakfast",
      "order": 4,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
      "duration_minutes": 60,
      "notes": "New schedule; feel free to move this around as you get used to it."
    },
    {
      "id": "weekly-review-goals",
      "name": "Weekly Review + Goals",
      "order": 5,
      "category": "POW",
      "days": ["sat"],
      "duration_minutes": 60,
      "subtasks": [
        { "name": "Weekly Review", "duration_minutes": 30, "notes": "Ask what worked, what didn't, what needs to change. Journal lessons, set priorities. Reduces unfinished tasks and rumination." },
        { "name": "Week Goals/Plans", "duration_minutes": 30, "notes": "Plan skill-study days and stream days for the coming week. Be sure to add missing subtasks.", "subtasks": [
          { "name": "Plan skill study days" },
          { "name": "Plan stream days and content" }
        ] }
      ]
    },
    {
      "id": "planning",
      "name": "Planning",
      "order": 6,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 30
    },
    {
      "id": "game-ideation",
      "name": "Game Ideation",
      "order": 7,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 30
    },
    {
      "id": "cleaning",
      "name": "Cleaning",
      "order": 8,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 10,
      "notes": "Make sure the room's not too dirty. Wash a dish or two."
    },
    {
      "id": "clean-dehumidifier",
      "name": "Clean Dehumidifier",
      "order": 9,
      "category": "POF",
      "days": ["sat"],
      "duration_minutes": 10,
      "subtasks": [
        { "name": "Spray down", "notes": "Options: isopropyl alcohol (70-90%), hydrogen peroxide, or white vinegar (recommended)." },
        { "name": "Let sit", "notes": "10-15m." },
        { "name": "Wash off with water" },
        { "name": "Let dry" }
      ]
    },
    {
      "id": "go-gym",
      "name": "Go Gym",
      "order": 10,
      "category": "POF",
      "days": ["tue", "fri", "sat"],
      "duration_minutes": 120,
      "notes": "Good for mental health."
    },
    {
      "id": "skate",
      "name": "Skate",
      "order": 11,
      "category": "POF",
      "days": ["sun"],
      "duration_minutes": 60,
      "notes": "1h skating; travel time not included. Just show up."
    },
    {
      "id": "skill-study",
      "name": "Skill Study",
      "order": 12,
      "category": "POW",
      "days": ["tue", "thu", "fri"],
      "duration_minutes": 90,
      "notes": "Being the best is a long-term effort investment."
    },
    {
      "id": "work",
      "name": "Work",
      "order": 13,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "flex": true,
      "duration_minutes": "FLEX",
      "notes": "Flex block: expands so daily POW hits the 8h target. Work schedule may differ depending on the day."
    },
    {
      "id": "end-of-day-ritual",
      "name": "End of Day Ritual",
      "order": 14,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 60,
      "subtasks": [
        { "name": "Dev forum checkup", "duration_minutes": 15, "notes": "Specifically the public resources." },
        { "name": "Read daily AI reports", "duration_minutes": 15, "notes": "Underground, up-and-coming, AI trends, etc." },
        { "name": "Work Review", "duration_minutes": 30, "notes": "Log wins; review finished/unfinished/delegated/backlogged tasks; find bottlenecks; extract lessons; clean up workspace/tabs and note loose thoughts for tomorrow." }
      ]
    },
    {
      "id": "mobile-gaming",
      "name": "Mobile Gaming",
      "order": 15,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 30,
      "notes": "Improve understanding of the biggest user market slice; keep up with trending Roblox games.",
      "subtasks": [
        { "name": "Play at least 1 new game every week" }
      ]
    },
    {
      "id": "pc-gaming",
      "name": "PC Gaming",
      "order": 16,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "duration_minutes": 30,
      "notes": "Keep up with trending Roblox games for inspiration.",
      "subtasks": [
        { "name": "Play at least 1 new game every week" }
      ]
    },
    {
      "id": "streaming-normal",
      "name": "Streaming Normal",
      "order": 17,
      "category": "POF",
      "days": ["mon", "wed"],
      "duration_minutes": 120,
      "subtasks": [
        { "name": "Plan/prep", "duration_minutes": 30, "notes": "Plan, study, and get ready for anything stream-related." },
        { "name": "Stream", "duration_minutes": 90, "notes": "Unmask stream: be engaging, conversate, practice 1-on-1 conversational skills." }
      ],
      "notes": "Don't start streaming until you have a monetized MVP for Whack Grass. Generate income ASAP."
    },
    {
      "id": "streaming-mc-hardcore",
      "name": "Streaming MC Hardcore",
      "order": 18,
      "category": "POF",
      "days": ["thu"],
      "duration_minutes": 120,
      "subtasks": [
        { "name": "Pre-stream prep", "duration_minutes": 30, "notes": "Study, plan, setup, smoke up." },
        { "name": "Stream", "duration_minutes": 90, "notes": "Unmask stream." }
      ],
      "notes": "Required weekly instance runs Thursday. (Sunday instance is NR — see streaming-mc-hardcore-optional.)"
    },
    {
      "id": "streaming-mc-hardcore-optional",
      "name": "Streaming MC Hardcore",
      "order": 18,
      "category": "POF",
      "days": ["sun"],
      "nr": true,
      "notes": "Optional 2nd weekly unmask stream. The arc doc recommends NOT scheduling Sundays as stream days; Thursday's instance is the required one. 0 scheduled minutes; never counted."
    },
    {
      "id": "clip-farm",
      "name": "Clip Farm",
      "order": 19,
      "category": "POF",
      "days": ["sun"],
      "nr": true,
      "duration_minutes": 150,
      "subtasks": [
        { "name": "Study content creation", "duration_minutes": 50 },
        { "name": "Content for chill streams", "duration_minutes": 50 },
        { "name": "Content for main streams", "duration_minutes": 50 }
      ],
      "notes": "NR. 2-3h max if you feel like it; split into thirds (study / chill-stream content / main-stream content). Advisory durations only — 0 scheduled minutes; comes out of Extra Personal Freetime if done. Don't take it too seriously."
    },
    {
      "id": "extra-personal-freetime",
      "name": "Extra Personal Freetime",
      "order": 20,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
      "flex": true,
      "duration_minutes": "FLEX",
      "notes": "Flex block: expands so daily POF hits the 8h target (16h on the free day). Strive for 8h total POF; at least 3-4h to yourself per day."
    },
    {
      "id": "sleep",
      "name": "Sleep",
      "order": 21,
      "category": "Sleep",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
      "duration_minutes": 480,
      "notes": "8h baseline target; may be reduced if you personally need less."
    }
  ]
}
```

### Expected weekly accounting (Mon-Sat, free-day excluded)

Used as the assertion target for the clean-valid scenario:

- Daily totals (Mon-Sat): POW 8h, POF 8h, Sleep 8h = 24h. Sunday (free day): 0 / 16h / 8h.
- Work flex: Mon 5h, Tue 3h 30m, Wed 5h, Thu 3h 30m, Fri 3h 30m, Sat 4h. Weekly = 24h 30m.
- Extra Personal Freetime flex: Mon-Fri 3h 20m, Sat 3h 10m. Weekly = 19h 50m. Sunday = 13h 45m (reference only).
- Top ranked (Mon-Sat): Sleep 48h (33.3%), Work flex 24h 30m (17.0%), Extra Freetime flex 19h 50m (13.8%), Morning Ritual 9h (6.3%), then Go Gym 6h / Breakfast 6h / End of Day 6h (4.2% each).

Conditional (Sunlight) and NR (Clip Farm, MC Hardcore Sunday) carry 0 counted minutes and are excluded from totals and ranking.