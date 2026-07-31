#!/usr/bin/env node
// parse-spec.js — Stage 1: extract + parse + normalize a Schedule Spec.
//
// Reads a Schedule Spec Markdown file, pulls out the authoritative
// `schedule-spec` fenced JSON block, parses it, and emits a normalized
// intermediate model (JSON) for validate-spec.js to consume.
//
// Usage:
//   node parse-spec.js <spec.md> [--out <model.json>]
//
// Exit codes: 0 ok | 1 no/invalid fenced block | 2 malformed JSON | 3 usage
//
// This script does light structural normalization only. Correctness/budget
// validation, flex math, and ranking live in validate-spec.js.

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const inputPath = args.find(a => !a.startsWith('--'));
const outPath = flag('--out');

if (!inputPath) {
  console.error('Usage: node parse-spec.js <spec.md> [--out <model.json>]');
  process.exit(3);
}

const absPath = path.resolve(process.cwd(), inputPath);
let markdown;
try {
  markdown = fs.readFileSync(absPath, 'utf8');
} catch (e) {
  console.error(`Error: cannot read input file: ${absPath}: ${e.message}`);
  process.exit(1);
}

// Extract the first fenced block whose info string is `schedule-spec`.
// Supports ``` and ~~~ fences; info string matched case-insensitively.
const fenceRe = /(^|\n)(`{3,}|~{3,})schedule-spec[ \t]*\r?\n([\s\S]*?)\r?\n\2(?=`|\n|$)/i;
const m = markdown.match(fenceRe);
if (!m) {
  console.error('Error: no `schedule-spec` fenced JSON block found in the input.');
  process.exit(1);
}
const jsonText = m[3];

let spec;
try {
  spec = JSON.parse(jsonText);
} catch (e) {
  console.error(`Error: the schedule-spec block is not valid JSON: ${e.message}`);
  process.exit(2);
}

const srcDir = path.dirname(absPath);
const filename = path.basename(absPath);

// Extract a version token from the filename, e.g. "V4.1" / "v4.1" -> "4.1".
// null when absent (no cross-check; not a blocker).
let filenameVersion = null;
const vMatch = filename.match(/v(\d+(?:\.\d+)*)/i);
if (vMatch) filenameVersion = vMatch[1];

// Normalize each task to a stable shape. Defer heavy validation to validate-spec.
const rawTasks = Array.isArray(spec.tasks) ? spec.tasks : [];
const tasks = rawTasks.map((t, idx) => {
  const id = t.id;
  const name = t.name;
  const order = t.order;
  const category = t.category;
  const days = Array.isArray(t.days) ? t.days.slice() : undefined;
  const is_flex = t.flex === true;
  const is_conditional = t && typeof t.conditional === 'object' && t.conditional !== null;
  const is_nr = t.nr === true;
  const conditional_max = is_conditional ? t.conditional.max_minutes : null;

  let duration_minutes = null;
  if (is_flex) {
    // FLEX sentinel preserved for validate-spec to fill per day.
    duration_minutes = 'FLEX';
  } else if (is_conditional) {
    duration_minutes = null;
  } else if (t && Object.prototype.hasOwnProperty.call(t, 'duration_minutes')) {
    duration_minutes = t.duration_minutes;
  }

  const subtasks = Array.isArray(t.subtasks) ? t.subtasks.map(s => ({
    name: s.name,
    duration_minutes: s.duration_minutes,
    days: Array.isArray(s.days) ? s.days.slice() : undefined,
    notes: s.notes,
    subtasks: Array.isArray(s.subtasks) ? s.subtasks : undefined,
  })) : undefined;

  return {
    id, name, order, category, days,
    duration_minutes,
    is_flex, is_conditional, is_nr, conditional_max,
    notes: t.notes,
    subtasks,
  };
});

const model = {
  source: {
    filename,
    path: absPath,
    dir: srcDir,
    content_version: spec.content_version,
    filename_version: filenameVersion,
  },
  format_version: spec.format_version,
  content_version: spec.content_version,
  calendar: spec.calendar,
  budgets: spec.budgets,
  tasks,
};

const json = JSON.stringify(model, null, 2);
if (outPath) {
  fs.writeFileSync(path.resolve(process.cwd(), outPath), json + '\n', 'utf8');
  console.error(`Parsed -> ${path.resolve(process.cwd(), outPath)}`);
} else {
  process.stdout.write(json + '\n');
}