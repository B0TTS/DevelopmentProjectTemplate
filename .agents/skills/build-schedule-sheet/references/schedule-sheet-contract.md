# Weekly Schedule Sheet Contract

The output of `build-schedule-sheet`. A Weekly Schedule Sheet is a single Markdown file with exactly 10 sections in this order. The contract is semantic and stable; the sheet is generated dynamically from the Schedule Spec (no hardcoded task lists, no runtime dependency on any external example).

## Output filename

`weekly-schedule-sheet-v<content_version>.md` (lowercase, preserves the source `content_version`). Written **beside the selected Schedule Spec by default**; an explicit destination overrides this. Existing outputs are never overwritten silently — a collision requires an explicit choice (new destination, replace, or cancel).

## Duration notation

Internally all durations are **integer minutes**. In the sheet, every duration, total, and flex value renders as `Xh Ym` with these rules:

| Minutes | Renders | Example |
|---|---|---|
| `n ≥ 60` and minutes leftover | `Xh Ym` | 90 → `1h 30m` |
| `n ≥ 60` and no leftover | `Xh` | 480 → `8h` |
| `n < 60` | `Ym` | 30 → `30m` |
| `0` | `0m` | — |

**No decimal-hour notation** anywhere (no `1.5h`, no `3.33h`). A category column with no task time shows `–`.

## Section list (fixed order)

1. **Provenance metadata** — blockquote with source spec filename, content version, format version, builder (`build-schedule-sheet`), free-day accounting mode, and the inferred free day.
2. **Legend and accounting rules** — table defining every tag/marker (POW, POF, Sleep, NR, Flex, Conditional, Freeday exception) and the active accounting rule (free-day excluded by default, Mon–Sat totals, 24h/day, etc.).
3. **Master weekly time summary** — one row per **non-free day** (Mon–Sat by default), columns `Day | POW | POF | Sleep | Total`. Bottom rows: `Weekly Total` and `Avg/day` over the non-free days. The free day is **not** a row here (it has its own daily table in section 4 and reference columns in sections 5–7).
4. **Ordered daily schedule tables (all 7 days)** — one table per calendar day in `calendar.days` order. Columns: `| # | Task | POF | POW | Sleep |`. Rows: every task scheduled that day, in ascending `order`. Each task's minutes go in its category column; others are `–`. Markers in the Task cell: `(flex)` for flex tasks, `(conditional)` for conditional, `(NR)` for NR. A totals row sums each column.
5. **POW breakdown** — task rows × day columns (non-free days + a `Sun (ref)` / free-day reference column), plus a `Wk Total` over non-free days. Includes a `Fixed subtotal` row, the flex row(s), and a `Total` row. Free-day column shown for reference, never summed into the weekly total.
6. **POF breakdown** — same structure as POW.
7. **Sleep breakdown** — same structure as Sleep.
8. **Task-to-day matrix** — top-level tasks only (source order) × all 7 day columns. Marks: `✔` scheduled · `opt` conditional · `NR` not required · `–` off. Subtasks do not get matrix rows (they live in section 10).
9. **Ranked weekly task hours** — ranked by total non-free-day minutes descending (ties share a rank). Columns: `# | Task | Category | Wk Hours | % of Week`. `% of Week` = weekly minutes ÷ (`non-free days × 1440`) × 100. **Conditional and NR tasks are excluded** (they carry 0 counted minutes). **Flex tasks are included** (their computed weekly hours are real). Daily table totals are not ranked.
10. **Task details / execution notes** — for each task that has `notes` or `subtasks`, a subsection with the task's `order`, `name`, category, scheduled days (h/m), the note, and its subtasks (name, optional advisory `duration_minutes`, optional `days`, optional notes). This is where long instructions live instead of bloating the daily tables.

### Sections explicitly NOT generated

- **Insight Highlights** — removed by design.
- **Clarifying Q&A** — removed by design.

## Daily table layout

```
### <Day> [— Freeday]

| # | Task | POF | POW | Sleep |
|---|---|---:|---:|---:|
| <order> | <name> <marker> | <m or –> | <m or –> | <m or –> |
| …
| | **Totals** | **POF** | **POW** | **Sleep** |
```

- `#` = source task `order` (the identity/step number).
- Each task occupies exactly one category column.
- Preserve source `order` ascending within each day.
- Mark `Flex`, `Conditional`, and `NR` in the Task cell — never by putting minutes in the wrong column.

## Breakdown layout (POW/POF/Sleep)

```
| Task | Mon | … | Sat | Sun (ref) | Wk Total (non-free) |
```

- One row per task of that category that appears on any non-free day, plus each flex task.
- `Fixed subtotal` row = Σ plain-task minutes per day.
- Flex row(s) = computed remainder per day.
- `Total` row = subtotal + flex.
- Free-day column is a reference only and is **never** added to `Wk Total`. A note under the table states this.

## Master summary (with free-day accounting excluded, default)

```
| Day | POW | POF | Sleep | Total |
|---|---|---|---|---|
| Monday | 8h | 8h | 8h | 24h |
| …
| Saturday | 8h | 8h | 8h | 24h |
| **Weekly Total (Mon–Sat)** | **48h** | **48h** | **48h** | **144h** |
| **Avg/day (Mon–Sat)** | **8h** | **8h** | **8h** | **24h** |
```

## Provenance block

```
> **Source Spec:** `Schedule Spec V4.1.md`
> **Spec Version:** 4.1
> **Format Version:** 1
> **Built By:** build-schedule-sheet
> **Free-Day Accounting:** Excluded by default
> **Free Day:** sun
```

When free-day accounting is included, the legend and provenance state `Included (explicitly requested)`, weekly totals add the free day, and percentage denominators use `7 × 24h = 168h`.

## Stability

The section set, section order, daily-table columns, and duration notation are stable across schedule content. Structural changes (different categories, different day count, different budget model) **block** generation rather than being guessed.