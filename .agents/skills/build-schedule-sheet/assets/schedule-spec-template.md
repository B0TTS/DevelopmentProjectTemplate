# Schedule Spec V<version>

Supporting prose goes here. Prose is context only — the JSON block below is authoritative. Do not let prose override structured values.

```schedule-spec
{
  "format_version": 1,
  "content_version": "0.1",
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
      "id": "sleep",
      "name": "Sleep",
      "order": 1,
      "category": "Sleep",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
      "duration_minutes": 480
    },
    {
      "id": "work",
      "name": "Work",
      "order": 2,
      "category": "POW",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat"],
      "flex": true,
      "duration_minutes": "FLEX"
    },
    {
      "id": "free-freetime",
      "name": "Free Freetime",
      "order": 3,
      "category": "POF",
      "days": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"],
      "flex": true,
      "duration_minutes": "FLEX"
    }
  ]
}
```

## How to fill this in

- `content_version` — your schedule version (e.g. `4.1`); drives the output filename `weekly-schedule-sheet-v<content_version>.md`.
- `calendar.free_day` — the one free day; excluded from weekly aggregates by default.
- `budgets` — target minutes per category per day-type. Flex fills `budget − fixed`. Edit freely; the skill owns no constants.
- `tasks[]` — each task needs a unique stable `id`, a human `name`, an integer `order`, a single `category` (`POW`/`POF`/`Sleep`), and a `days` array. Use one of four shapes:
  - **plain** — `days` + integer `duration_minutes`.
  - **flex** — add `flex: true` and `"duration_minutes": "FLEX"` (one flex task per category per day owns the remainder).
  - **conditional** — add `conditional: { "max_minutes": 60 }` (visible, not counted by default).
  - **nr** — add `nr: true` (recommendation, 0 scheduled minutes, never counted).
- `subtasks[]` are execution detail inside a parent — name + optional `duration_minutes` (advisory) + optional `days` (subset of parent days) + optional `notes`. They are never independently counted.

Full rules: see `references/schedule-spec-contract.md`. A complete worked example: see `references/schedule-spec-example.md`.