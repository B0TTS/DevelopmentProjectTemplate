# Schedule Spec Contract (format_version: 1)

The authoritative input format for `build-schedule-sheet`. A Schedule Spec is a Markdown file whose source of truth is a single fenced JSON block with the info string `schedule-spec`. Surrounding Markdown prose is supporting context only and **must not** override structured values.

Example envelope:

````md
# Schedule Spec V4.1

Optional human-readable notes. Prose is context only.

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
  "tasks": []
}
```
````

All durations are **integer minutes**. The skill owns no budget constants — budgets live in the spec (see *Rationale* below).

## Top-level fields

| Field | Required | Type | Notes |
|---|---|---|---|
| `format_version` | yes | integer | Schema version. Currently `1`. Unknown value = blocker (no silent reinterpretation). |
| `content_version` | yes | string | Schedule/spec version, e.g. `"4.1"`. Drives the output filename `weekly-schedule-sheet-v<content_version>.md`. Must agree with any version present in the source filename (e.g. `Schedule Spec V4.1.md`). Disagreement / missing value = blocker. |
| `calendar` | yes | object | `days[]` (7 lowercase weekday codes, any order) + `free_day` (one code from `days`). Missing/invalid/free_day not in days = blocker. |
| `budgets` | yes | object | `work_day` and `free_day`, each `{ "POW": int, "POF": int, "Sleep": int }` minutes. A day uses the `free_day` budget iff its code === `calendar.free_day`. Used to compute flex. |
| `tasks` | yes | array | One or more task objects (see below). Empty array = blocker. |

Weekday codes: `mon tue wed thu fri sat sun` (lowercase only).

## Task object

| Field | Required | Type | Notes |
|---|---|---|---|
| `id` | yes | string | Stable unique machine id. Distinct from `name` and `order`. Duplicate id = blocker. |
| `name` | yes | string | Human-readable display name. |
| `order` | yes | integer | Display/step order. Drives the `#` column and source-order preservation. Duplicates allowed across tasks but discouraged. |
| `category` | yes | string | One of `POW`, `POF`, `Sleep`. Unknown value = blocker. A task belongs to exactly one category. |
| `days` | yes | array[string] | Day codes this task runs on. Must be a subset of `calendar.days`. Unknown code = blocker. Explicit day assignments are authoritative; recurrence (frequency) is derived from this array. |
| `duration_minutes` | conditional | integer \| `"FLEX"` | Required for plain, flex, and NR tasks. Integer minutes, or the literal `"FLEX"` for flex tasks. Conditional tasks omit this (their max comes from `conditional`). |
| `notes` | no | string | Execution note shown in the details section. |
| `subtasks` | no | array | Execution detail within the parent (see below). Never independently counted. |
| `flex` | no | boolean | `true` marks this task as the remainder/flex allocation for its category on its days. See *Flex rules*. |
| `conditional` | no | object | `{ "max_minutes": int }`. Visible in the sheet but **not counted** by default. Draws down a flex/remainder task when taken. |
| `nr` | no | boolean | `true` = Not Required: a recommendation only. Visible with **0 scheduled minutes**; excluded from totals, rankings, flex, and percentages. `duration_minutes` (if present) is advisory text for the details section only. |

A task uses exactly one scheduling shape:

- **Plain** — `days` + integer `duration_minutes`. Counts toward its category fixed subtotal on each listed day.
- **Flex** — `days` + `duration_minutes: "FLEX"` + `flex: true`. Duration for a day = `budgets[day_type][category] − Σ fixed durations` of that category on that day.
- **Conditional** — `days` + `conditional: { max_minutes }` (no `duration_minutes`). Visible; not counted unless the user explicitly requests conditional time be counted.
- **NR** — `days` + optional integer `duration_minutes` (advisory) + `nr: true`. Visible as a recommendation; 0 scheduled minutes; never counted.

## Subtasks

Subtasks are **execution detail within a parent** — they are never independently scheduled and never counted in addition to the parent.

| Field | Required | Type | Notes |
|---|---|---|---|
| `name` | yes | string | Subtask name. |
| `duration_minutes` | no | integer | Advisory only. Shown in the details section. Never added to any total. |
| `days` | no | array[string] | When this subtask applies within the parent. If present, must be a subset of the parent's `days` (otherwise blocker — that's an independently-scheduled subtask mislabeled, give it its own top-level id). |
| `notes` | no | string | Execution note for the subtask. |

### Parent/subtask duration-conflict rule (v1 scope)

If a task's subtasks are **uniform** (none has `days`) and **all** carry `duration_minutes`, their sum must equal the parent's `duration_minutes`; otherwise blocker.

If **any** subtask has `days` (per-day variance, e.g. a morning ritual whose components change by day), the sum cannot be validated safely, so the conflict check is **skipped** and a non-blocking note is emitted. This is a deliberate v1 scope choice: a naive sum would false-positive on legitimate per-day variance. If you need strict per-day allocation accounting, model those components as top-level tasks with their own stable ids.

## Flex rules (enforced by the validator)

For every (day, category) where `budgets[day_type][category] > 0`:

1. Compute `fixed = Σ duration_minutes` of plain tasks of that category scheduled that day (flex / conditional / NR excluded).
2. If `fixed > budget` → **blocker** (over budget). On a free day this also catches work tasks scheduled on a 0-POW-budget day.
3. If `fixed == budget` → no flex needed. A flex task of that category scheduled that day gets 0 minutes (non-blocking note).
4. If `fixed < budget` → exactly **one** flex task of that category must be scheduled that day to own the remainder:
   - zero flex tasks → **blocker** (unallocated time, ambiguous ownership)
   - more than one → **blocker** (ambiguous flex ownership)
   - the single flex task's duration that day = `budget − fixed`.

Conditional and NR tasks never enter `fixed` or the flex remainder. Flex is not inferred from task names — the `flex: true` flag is required.

## Free-day accounting

The free day is inferred from `calendar.free_day` and shown in the sheet (its own daily table + a reference column in breakdowns). **By default free-day accounting is excluded** from weekly totals, averages, percentages, rankings, and flex sums. The user must explicitly request inclusion (`--free-day-accounting included`) to add it; the skill never infers that request from a free-day budget in the spec. The active mode is stated in the provenance block.

When excluded (default): weekly totals sum the non-free days only; the free-day daily table and breakdown columns are shown for reference but never summed. When included: the free day joins the weekly totals and its percentages are computed against `7 × 24h = 168h` instead of `(non-free days) × 24h`.

## Rationale: budgets in the spec

Budgets (the 8/8/8 work-day and 0/16/8 free-day targets) are part of a schedule's identity, not universal constants. Declaring them in the spec:

- removes magic constants from the skill (the skill owns no `480`/`960` numbers),
- lets budgets evolve across schedule versions without skill churn,
- keeps the flex formula honest: `flex = budget − fixed`.

The skill still **blocks** on budget shapes it cannot model (e.g. extra categories, missing category entries, negative minutes), so diverging from the standard model is never silently reinterpreted.

## v1 scope boundaries (deliberate, documented)

- **No per-day `assignments[]`** in v1. Each task has one `duration_minutes` applied to every day in its `days`. A task that needs different durations by day, or multiple occurrences on one day, must be modeled as multiple top-level tasks with distinct ids until assignment records are added. The handoff names explicit assignment records as a future contract feature; they are deferred here to avoid speculative schema/code (no current spec needs them).
- **No multi-occurrence-per-day** modeling. A task either runs once on each of its days or is a flex/conditional/NR marker.
- **No decimal-hour notation** in the generated sheet. All durations render as `Xh Ym` (e.g. `1h 30m`, `30m`, `8h`); internals are integer minutes.

Anything not described here is a blocker unless explicitly listed as non-blocking in the validator's warning set.