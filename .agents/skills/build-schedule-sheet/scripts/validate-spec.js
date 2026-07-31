#!/usr/bin/env node
// validate-spec.js — Stage 2: validate the normalized model and compute all numbers.
//
// Reads a normalized model (from parse-spec.js; file arg or stdin), validates
// it (blockers vs warnings), and — when the structure is sound enough —
// computes per-day fixed/flex/total, weekly aggregates, and the ranked task
// list. Free-day accounting is EXCLUDED by default (opt-in with
// --free-day-accounting included).
//
// IMPORTANT: this script collects ALL blockers it can before exiting, and it
// ALWAYS writes the structured result (to --out if given, else stdout) so the
// agent can read blockers in machine form even on failure. Exit 1 only when
// blockers exist.
//
// Usage:
//   node validate-spec.js <model.json> [--free-day-accounting excluded|included] [--out <validated.json>]
//
// Exit codes: 0 ok | 1 blockers present | 3 usage

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const inputPath = args.find(a => !a.startsWith('--'));
const fda = flag('--free-day-accounting') || 'excluded';
const outPath = flag('--out');

if (!inputPath || !['excluded', 'included'].includes(fda)) {
  console.error('Usage: node validate-spec.js <model.json> [--free-day-accounting excluded|included] [--out <validated.json>]');
  process.exit(3);
}

let modelText = '';
const inPath = path.resolve(process.cwd(), inputPath);
try {
  modelText = fs.readFileSync(inPath, 'utf8');
} catch (e) {
  console.error(`Error: cannot read model file: ${inPath}: ${e.message}`);
  process.exit(1);
}

let model;
try { model = JSON.parse(modelText); }
catch (e) { console.error(`Error: model is not valid JSON: ${e.message}`); process.exit(1); }

const VALID_DAYS = new Set(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']);
const CATEGORIES = ['POW', 'POF', 'Sleep'];
const KNOWN_FORMAT_VERSIONS = new Set([1]);

const blockers = [];
const warnings = [];
const pushB = (code, message) => blockers.push({ code, message });
const pushW = (code, message) => warnings.push({ code, message });

// --- Structural validation (collect all; never early-exit) ---

if (!KNOWN_FORMAT_VERSIONS.has(model.format_version)) {
  pushB('unknown_format_version', `format_version ${JSON.stringify(model.format_version)} is not supported (known: 1). The skill refuses to reinterpret an unknown schema.`);
}
if (!model.content_version || typeof model.content_version !== 'string') {
  pushB('missing_content_version', 'content_version is required (non-empty string); it drives the output filename.');
} else {
  const fv = model.source && model.source.filename_version;
  if (fv !== null && fv !== undefined && fv !== model.content_version) {
    pushB('version_conflict', `content_version "${model.content_version}" disagrees with version "${fv}" found in the source filename "${model.source.filename}".`);
  }
}

const cal = model.calendar;
let calendarValid = false, freeDayValid = false;
if (!cal || !Array.isArray(cal.days) || cal.days.length !== 7) {
  pushB('invalid_calendar', 'calendar.days must be an array of exactly 7 day codes.');
} else {
  const seen = new Set();
  let dupDay = false, badDay = false;
  for (const d of cal.days) {
    if (!VALID_DAYS.has(d)) { pushB('invalid_calendar', `calendar.days contains unknown day code "${d}".`); badDay = true; }
    if (seen.has(d)) { pushB('invalid_calendar', `calendar.days contains duplicate day "${d}".`); dupDay = true; }
    seen.add(d);
  }
  if (!badDay && !dupDay) calendarValid = true;
  if (!cal.free_day || !VALID_DAYS.has(cal.free_day) || !cal.days.includes(cal.free_day)) {
    pushB('invalid_free_day', `calendar.free_day "${cal.free_day}" is missing or not in calendar.days.`);
  } else {
    freeDayValid = true;
  }
}

const bud = model.budgets;
let budgetsValidForFlex = false;
if (!bud || typeof bud !== 'object') {
  pushB('invalid_budgets', 'budgets object is required.');
} else {
  for (const dt of ['work_day', 'free_day']) {
    const b = bud[dt];
    if (!b || typeof b !== 'object') { pushB('invalid_budgets', `budgets.${dt} is required.`); continue; }
    const extra = Object.keys(b).filter(k => !CATEGORIES.includes(k));
    if (extra.length) pushB('unsupported_budget_model', `budgets.${dt} has unsupported category keys: ${extra.join(', ')}. Only POW, POF, Sleep are supported.`);
    for (const c of CATEGORIES) {
      const v = b[c];
      if (typeof v !== 'number' || !Number.isInteger(v) || v < 0) {
        pushB('invalid_budgets', `budgets.${dt}.${c} must be a non-negative integer minute value.`);
      }
    }
  }
  budgetsValidForFlex = bud && bud.work_day && bud.free_day
    && CATEGORIES.every(c => typeof bud.work_day[c] === 'number' && Number.isInteger(bud.work_day[c]) && bud.work_day[c] >= 0
      && typeof bud.free_day[c] === 'number' && Number.isInteger(bud.free_day[c]) && bud.free_day[c] >= 0);
}

if (!Array.isArray(model.tasks) || model.tasks.length === 0) {
  pushB('missing_tasks', 'tasks must be a non-empty array.');
}

const canDoFlex = calendarValid && freeDayValid && budgetsValidForFlex;
const freeDay = (cal && cal.free_day) || null;
const dayType = (d) => (d === freeDay ? 'free_day' : 'work_day');

// --- Per-task validation (always run) ---
const ids = new Map();
const flexOwnersByCat = { POW: {}, POF: {}, Sleep: {} };

const tasks = (model.tasks || []).map((t, idx) => {
  if (!t || typeof t !== 'object') { pushB('invalid_task', `task at index ${idx} is not an object.`); return { _shape: 'invalid', _index: idx, days: [] }; }
  const id = t.id;
  if (!id || typeof id !== 'string') { pushB('missing_id', `task at index ${idx} has no valid string id.`); }
  else if (ids.has(id)) { pushB('duplicate_id', `duplicate task id "${id}".`); }
  else ids.set(id, idx);

  if (!t.name || typeof t.name !== 'string') { pushB('invalid_task', `task "${id}" has no valid name.`); }
  if (t.order === undefined || typeof t.order !== 'number' || !Number.isInteger(t.order)) {
    pushB('invalid_task', `task "${id}" has no valid integer order.`);
  }
  if (!CATEGORIES.includes(t.category)) {
    pushB('invalid_category', `task "${id}" has unknown category "${t.category}". Allowed: POW, POF, Sleep.`);
  }
  if (!Array.isArray(t.days) || t.days.length === 0) {
    pushB('invalid_days', `task "${id}" has no days array.`);
  } else {
    for (const d of t.days) {
      if (!VALID_DAYS.has(d) || !(cal && cal.days && cal.days.includes(d))) {
        pushB('invalid_days', `task "${id}" uses unknown/uncalendar day "${d}".`);
      }
    }
  }

  const is_flex = t.is_flex === true;
  const is_conditional = t.is_conditional === true;
  const is_nr = t.is_nr === true;
  const shapeFlags = [is_flex, is_conditional, is_nr].filter(Boolean);
  if (shapeFlags.length > 1) {
    pushB('ambiguous_shape', `task "${id}" mixes mutually-exclusive flags (flex/conditional/nr). Pick one.`);
  }
  let shape;
  if (is_flex) {
    shape = 'flex';
    if (t.duration_minutes !== 'FLEX') {
      pushB('invalid_flex_duration', `task "${id}" is flex but duration_minutes is not the literal "FLEX".`);
    }
  } else if (is_conditional) {
    shape = 'conditional';
    if (t.duration_minutes !== null && t.duration_minutes !== undefined) {
      pushB('invalid_conditional', `task "${id}" is conditional but also declares duration_minutes; remove it.`);
    }
    if (typeof t.conditional_max !== 'number' || !Number.isInteger(t.conditional_max) || t.conditional_max <= 0) {
      pushB('invalid_conditional', `task "${id}" conditional.max_minutes must be a positive integer.`);
    }
  } else if (is_nr) {
    shape = 'nr';
    if (t.duration_minutes !== undefined && t.duration_minutes !== null &&
        (typeof t.duration_minutes !== 'number' || !Number.isInteger(t.duration_minutes) || t.duration_minutes < 0)) {
      pushB('invalid_nr', `task "${id}" advisory duration_minutes must be a non-negative integer.`);
    }
  } else {
    shape = 'plain';
    if (typeof t.duration_minutes !== 'number' || !Number.isInteger(t.duration_minutes) || t.duration_minutes <= 0) {
      pushB('invalid_duration', `task "${id}" duration_minutes must be a positive integer (or "FLEX" for flex tasks).`);
    }
  }
  if (is_flex && canDoFlex) {
    for (const d of (t.days || [])) {
      if (calendarValid && cal.days.includes(d)) {
        flexOwnersByCat[t.category][d] = flexOwnersByCat[t.category][d] || [];
        flexOwnersByCat[t.category][d].push(idx);
      }
    }
  }

  // Subtasks.
  let subtasks = t.subtasks;
  if (Array.isArray(subtasks)) {
    subtasks = subtasks.map((s, si) => {
      if (!s || !s.name || typeof s.name !== 'string') pushB('invalid_subtask', `task "${id}" subtask ${si} has no name.`);
      if (Array.isArray(s.days)) {
        for (const d of s.days) {
          if (!(t.days || []).includes(d)) {
            pushB('subtask_day_outside_parent', `task "${id}" subtask "${s && s.name}" uses day "${d}" outside the parent's days; give it its own top-level id instead.`);
          }
        }
      }
      if (s && s.duration_minutes !== undefined && s.duration_minutes !== null &&
          (typeof s.duration_minutes !== 'number' || !Number.isInteger(s.duration_minutes) || s.duration_minutes < 0)) {
        pushB('invalid_subtask', `task "${id}" subtask "${s.name}" duration_minutes must be a non-negative integer.`);
      }
      return s;
    });
    const allHaveDur = subtasks.length > 0 && subtasks.every(s => s && typeof s.duration_minutes === 'number');
    const anyHasDays = subtasks.some(s => s && Array.isArray(s.days) && s.days.length);
    if (allHaveDur && !anyHasDays && typeof t.duration_minutes === 'number' && !is_nr) {
      const sum = subtasks.reduce((a, s) => a + (s.duration_minutes || 0), 0);
      if (sum !== t.duration_minutes) {
        pushB('subtask_duration_conflict', `task "${id}": uniform subtask durations sum to ${sum}m but parent duration is ${t.duration_minutes}m.`);
      }
    }
    if (anyHasDays) {
      pushW('subtask_variance_skipped', `task "${id}" has per-day subtask variance; parent/subtask duration-conflict check skipped (subtask durations are advisory).`);
    }
  }

  return { ...t, _shape: shape, _index: idx };
});

// --- Flex math + computation (only when structurally sound) ---
let computed = null;
let sumDays = [];
if (canDoFlex) {
  const resolved = new Map();
  for (const t of tasks) {
    const map = {};
    for (const d of (t.days || [])) map[d] = t._shape === 'plain' ? (t.duration_minutes || 0) : null;
    resolved.set(t._index, map);
  }

  const perDay = {};
  for (const d of cal.days) {
    const dt = dayType(d);
    perDay[d] = { _day_type: dt };
    for (const cat of CATEGORIES) {
      const budget = bud[dt][cat];
      let fixed = 0;
      for (const t of tasks) {
        if (t._shape === 'plain' && t.category === cat && (t.days || []).includes(d)) fixed += (t.duration_minutes || 0);
      }
      const owners = (flexOwnersByCat[cat][d]) || [];
      if (fixed > budget) pushB('over_budget', `Day "${d}" ${cat}: fixed ${fixed}m exceeds budget ${budget}m.`);
      const remainder = budget - fixed;
      if (owners.length > 1) pushB('ambiguous_flex', `Day "${d}" ${cat}: ${owners.length} flex tasks compete to own the remainder; exactly one is allowed.`);
      let flex = 0;
      if (owners.length === 1) {
        if (remainder > 0) { flex = remainder; resolved.get(owners[0])[d] = remainder; }
        else { resolved.get(owners[0])[d] = 0; pushW('flex_zero_remainder', `Day "${d}" ${cat}: flex task has 0 remainder (fixed already meets budget).`); }
      } else if (owners.length === 0 && remainder > 0 && budget > 0) {
        pushB('unallocated_time', `Day "${d}" ${cat}: ${remainder}m unallocated with no flex task to own it; budgets must be met exactly or a flex task declared.`);
      }
      perDay[d][cat] = { fixed, flex, total: fixed + flex, budget };
    }
    perDay[d].total = CATEGORIES.reduce((a, c) => a + perDay[d][c].total, 0);
  }

  const nonFreeDays = cal.days.filter(d => d !== freeDay);
  sumDays = fda === 'included' ? cal.days : nonFreeDays;
  const weekly = {};
  for (const cat of CATEGORIES) {
    weekly[cat] = {
      fixed: sumDays.reduce((a, d) => a + perDay[d][cat].fixed, 0),
      flex: sumDays.reduce((a, d) => a + perDay[d][cat].flex, 0),
    };
    weekly[cat].total = weekly[cat].fixed + weekly[cat].flex;
  }
  weekly.total = CATEGORIES.reduce((a, c) => a + weekly[c].total, 0);
  const avgPerDay = {};
  for (const cat of CATEGORIES) avgPerDay[cat] = Math.round(weekly[cat].total / sumDays.length);
  avgPerDay.total = Math.round(weekly.total / sumDays.length);

  const denomMinutes = sumDays.length * 1440;
  const ranking = tasks
    .map(t => {
      let weekly_minutes = 0;
      for (const d of sumDays) {
        const m = resolved.get(t._index)[d];
        if (typeof m === 'number') weekly_minutes += m;
      }
      return { id: t.id, name: t.name, category: t.category, order: t.order, weekly_minutes };
    })
    .filter(r => r.weekly_minutes > 0)
    .sort((a, b) => b.weekly_minutes - a.weekly_minutes || (a.order - b.order));
  let lastMin = null, lastRank = 0;
  ranking.forEach((r, i) => {
    if (lastMin === r.weekly_minutes) r.rank = lastRank;
    else { r.rank = i + 1; lastRank = i + 1; lastMin = r.weekly_minutes; }
    r.percent = (r.weekly_minutes / denomMinutes) * 100;
  });

  const condCount = tasks.filter(t => t._shape === 'conditional').length;
  const nrCount = tasks.filter(t => t._shape === 'nr').length;
  if (condCount) pushW('conditional_present', `${condCount} conditional task(s) present: visible but not counted by default. Approval required to finalize.`);
  if (nrCount) pushW('nr_present', `${nrCount} NR task(s) present: 0 scheduled minutes; excluded from totals, ranking, flex, and percentages.`);

  const computedTasks = tasks.map(t => {
    const map = resolved.get(t._index) || {};
    let weekly_minutes = 0;
    for (const d of sumDays) if (typeof map[d] === 'number') weekly_minutes += map[d];
    return {
      id: t.id, name: t.name, order: t.order, category: t.category, days: t.days,
      shape: t._shape,
      is_flex: t.is_flex === true, is_conditional: t.is_conditional === true, is_nr: t.is_nr === true,
      conditional_max: t.conditional_max || null,
      duration_minutes: (t._shape === 'plain' || (t._shape === 'nr' && typeof t.duration_minutes === 'number')) ? t.duration_minutes : null,
      per_day: map,
      weekly_minutes,
      counted: t._shape === 'plain' || t._shape === 'flex',
      notes: t.notes,
      subtasks: t.subtasks,
    };
  });

  computed = {
    free_day: freeDay,
    non_free_days: nonFreeDays,
    all_days: cal.days,
    per_day: perDay,
    weekly, avg_per_day: avgPerDay, ranking,
    tasks: computedTasks,
  };
}

const result = {
  ok: blockers.length === 0,
  blockers,
  warnings,
  free_day_accounting: fda,
  summed_days: sumDays,
  excluded_days: fda === 'included' ? [] : (freeDay ? [freeDay] : []),
  source: model.source,
  format_version: model.format_version,
  content_version: model.content_version,
  calendar: cal,
  budgets: bud,
  computed,
};

const json = JSON.stringify(result, null, 2);
if (outPath) fs.writeFileSync(path.resolve(process.cwd(), outPath), json + '\n', 'utf8');
else process.stdout.write(json + '\n');

if (blockers.length) {
  console.error(`\nBLOCKERS (${blockers.length}):`);
  for (const b of blockers) console.error(`  - [${b.code}] ${b.message}`);
  process.exit(1);
}