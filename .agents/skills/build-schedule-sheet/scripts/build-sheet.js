#!/usr/bin/env node
// build-sheet.js — Stage 3: render the Weekly Schedule Sheet draft + preflight.
//
// Reads a validated+computed model (from validate-spec.js). Renders the
// 10-section Weekly Schedule Sheet Markdown and writes it as a DRAFT under
// b0ttsagent/temp/. Prints a preflight JSON to stdout (source, versions,
// draft path, proposed output path, sections, blockers, warnings).
//
// This script NEVER writes the final output. The agent writes the final sheet
// to `output_path` only after explicit approval and a collision recheck.
//
// Usage:
//   node build-sheet.js <validated.json> [--output <final-path>] [--draft-dir <dir>]
//
// Exit codes: 0 ok | 1 blockers present (refuses to render) | 3 usage

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const inputPath = args.find(a => !a.startsWith('--'));
const outputOverride = flag('--output');
const draftDir = flag('--draft-dir') || path.join('b0ttsagent', 'temp');

if (!inputPath) {
  console.error('Usage: node build-sheet.js <validated.json> [--output <final-path>] [--draft-dir <dir>]');
  process.exit(3);
}

const inPath = path.resolve(process.cwd(), inputPath);
let result;
try { result = JSON.parse(fs.readFileSync(inPath, 'utf8')); }
catch (e) { console.error(`Error: cannot read validated model: ${e.message}`); process.exit(1); }

const CATEGORIES = ['POW', 'POF', 'Sleep'];
const DAYNAME = { mon: 'Monday', tue: 'Tuesday', wed: 'Wednesday', thu: 'Thursday', fri: 'Friday', sat: 'Saturday', sun: 'Sunday' };
const COLS = ['POF', 'POW', 'Sleep']; // daily-table column order per contract

// --- Preflight assembly (computed before rendering so blockers short-circuit) ---
const c = result.computed || {};
const sourceName = (result.source && result.source.filename) || 'unknown';
const contentVersion = result.content_version || 'unknown';
const outputDir = (result.source && result.source.dir) || process.cwd();
const outputPath = outputOverride
  ? path.resolve(process.cwd(), outputOverride)
  : path.join(outputDir, `weekly-schedule-sheet-v${contentVersion}.md`);

const SECTIONS = [
  'Provenance metadata', 'Legend and accounting rules', 'Master weekly summary',
  'Daily schedule tables', 'POW breakdown', 'POF breakdown', 'Sleep breakdown',
  'Task-to-day matrix', 'Ranked weekly task hours', 'Task details / execution notes',
];

// Refuse to render if blockers.
if (!result.ok) {
  const preflight = {
    ok: false,
    blockers: result.blockers,
    warnings: result.warnings,
    source: sourceName,
    content_version: contentVersion,
    output_path: outputPath,
    sections: [],
    message: 'Blockers present; refusing to render. Resolve blockers and re-run validate-spec.js.',
  };
  process.stdout.write(JSON.stringify(preflight, null, 2) + '\n');
  console.error(`\nRefusing to render: ${result.blockers.length} blocker(s).`);
  for (const b of result.blockers) console.error(`  - [${b.code}] ${b.message}`);
  process.exit(1);
}

// --- Helpers ---
function fmt(min) {
  if (min == null) return '–';
  if (min === 0) return '0m';
  const h = Math.floor(min / 60), m = min % 60;
  if (h && m) return `${h}h ${m}m`;
  if (h) return `${h}h`;
  return `${m}m`;
}
function fmtRange(max) { // conditional 0..max
  return `0–${fmt(max)}`;
}
const WEEK_ORDER = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'];
function dayRangeLabel(days) {
  // "Mon–Sat" when the counted days are a contiguous run in week order
  // (incl. wrap-around); else a comma list so split weeks stay honest.
  const ord = WEEK_ORDER;
  const idxs = days.map(d => ord.indexOf(d)).sort((a, b) => a - b);
  let contiguous = idxs.length > 1;
  for (let i = 1; i < idxs.length; i++) {
    const expected = idxs[i - 1] + 1;
    const wrap = idxs[i - 1] === 5 && idxs[i] === 6; // sat->sun fine
    if (idxs[i] !== expected && !wrap) { contiguous = false; break; }
  }
  const named = [...days].sort((a, b) => ord.indexOf(a) - ord.indexOf(b));
  if (contiguous) return `${DAYNAME[named[0]].slice(0, 3)}–${DAYNAME[named[named.length - 1]].slice(0, 3)}`;
  return named.map(d => DAYNAME[d].slice(0, 3)).join(', ');
}
const fdaLabel = result.free_day_accounting === 'included'
  ? 'Included (explicitly requested)'
  : 'Excluded by default';
const sumDays = result.summed_days || c.non_free_days;
const freeDay = c.free_day;
const countedDays = sumDays; // days entering weekly totals
const refFreeDay = result.free_day_accounting === 'included' ? null : freeDay;
const allDays = c.all_days;

// task lookup by id
const taskById = {};
for (const t of c.tasks) taskById[t.id] = t;

// --- Render ---
const lines = [];
const L = (s) => lines.push(s);

L(`# Weekly Schedule Sheet — v${contentVersion}`);
L('');
L(`> **Source Spec:** \`${sourceName}\``);
L(`> **Spec Version:** ${contentVersion}`);
L(`> **Format Version:** ${result.format_version}`);
L(`> **Built By:** build-schedule-sheet`);
L(`> **Free-Day Accounting:** ${fdaLabel}`);
L(`> **Free Day:** ${freeDay}`);
L('');

// 2. Legend
L('## Legend and Accounting Rules');
L('');
L('| Tag | Meaning |');
L('|---|---|');
L('| **POW** | Part of Work — counts toward the daily work total |');
L('| **POF** | Part of Freetime — counts toward the daily free total |');
L('| **Sleep** | Separate category — sleep baseline |');
L('| **NR** | Not Required — a recommendation only; 0 scheduled minutes; never enters any total |');
L('| **Freeday exception** | Runs on the non-free days; skipped on the free day |');
L('| **Flex** | Filled block — expands to hit the category budget (budget − fixed) |');
L('| **Conditional** | Optional block — visible but not counted by default; draws down a flex block when taken |');
L('');
L(`Accounting: the free day (${freeDay}) is shown for reference and **${result.free_day_accounting === 'included' ? 'included' : 'excluded'}** from weekly totals, averages, percentages, and rankings. Counted days: ${sumDays.map(d => DAYNAME[d]).join(', ')}. Daily targets apply per the spec budgets.`);
L('');

// 3. Master weekly summary
L('## Master Weekly Summary');
L('');
L(`| Day | POW | POF | Sleep | Total |`);
L(`|---|---|---|---|---|`);
const orderedCounted = allDays.filter(d => sumDays.includes(d));
for (const d of orderedCounted) {
  const p = c.per_day[d];
  L(`| ${DAYNAME[d]} | ${fmt(p.POW.total)} | ${fmt(p.POF.total)} | ${fmt(p.Sleep.total)} | ${fmt(p.total)} |`);
}
L(`| **Weekly Total (${dayRangeLabel(sumDays)})** | **${fmt(result.computed.weekly.POW.total)}** | **${fmt(result.computed.weekly.POF.total)}** | **${fmt(result.computed.weekly.Sleep.total)}** | **${fmt(result.computed.weekly.total)}** |`);
L(`| **Avg/day (${dayRangeLabel(sumDays)})** | **${fmt(result.computed.avg_per_day.POW)}** | **${fmt(result.computed.avg_per_day.POF)}** | **${fmt(result.computed.avg_per_day.Sleep)}** | **${fmt(result.computed.avg_per_day.total)}** |`);
L('');

// 4. Daily schedule tables (all 7 days)
L('## Daily Schedules');
L('');
L('> `#` = source task order. Each task fills exactly one category column. Conditional tasks are visible but not counted; NR tasks are listed in a note and shown in the matrix, not as daily rows.');
L('');
for (const d of allDays) {
  const isFree = d === freeDay;
  L(`### ${DAYNAME[d]}${isFree ? ' — Freeday' : ''}`);
  L('');
  L('| # | Task | POF | POW | Sleep |');
  L('|---|---|---:|---:|---:|');
  const dayTasks = c.tasks
    .filter(t => (t.days || []).includes(d) && t.shape !== 'nr')
    .sort((a, b) => a.order - b.order);
  for (const t of dayTasks) {
    const marker = t.shape === 'flex' ? ' *(flex)*' : (t.shape === 'conditional' ? ' *(conditional)*' : '');
    const vals = {};
    for (const col of COLS) vals[col] = '–';
    if (t.shape === 'conditional') {
      vals[t.category] = fmtRange(t.conditional_max);
    } else {
      vals[t.category] = fmt(t.per_day[d]);
    }
    L(`| ${t.order} | ${t.name}${marker} | ${vals.POF} | ${vals.POW} | ${vals.Sleep} |`);
  }
  // totals row (fixed + flex only)
  const p = c.per_day[d];
  L(`| | **Totals** | **${fmt(p.POF.total)}** | **${fmt(p.POW.total)}** | **${fmt(p.Sleep.total)}** |`);
  L('');
  // NR note for this day
  const nrToday = c.tasks.filter(t => (t.days || []).includes(d) && t.shape === 'nr');
  if (nrToday.length) {
    L(`> **NR (visible, 0 scheduled minutes, not counted):** ${nrToday.map(t => `${t.order}. ${t.name}`).join(' · ')}`);
    L('');
  }
}

// 5-7. Breakdowns
function renderBreakdown(cat, titleDayCols) {
  L(`## ${cat} Breakdown by Day`);
  L('');
  const header = ['Task', ...titleDayCols.map(d => d === freeDay && refFreeDay ? `${DAYNAME[d]} (ref)` : DAYNAME[d]), `Wk Total (${dayRangeLabel(sumDays)})`];
  L('| ' + header.join(' | ') + ' |');
  L('|' + header.map(() => '---').join('|') + '|');
  const catTasks = c.tasks.filter(t => t.category === cat && t.shape !== 'conditional' && t.shape !== 'nr' && (t.shape === 'flex' || (t.days || []).some(d => sumDays.includes(d) || d === freeDay)));
  catTasks.sort((a, b) => a.order - b.order);
  // split plain vs flex for subtotal/flex layout
  const plain = catTasks.filter(t => t.shape === 'plain');
  const flex = catTasks.filter(t => t.shape === 'flex');
  const dayCols = titleDayCols;
  for (const t of plain) {
    const row = [t.name, ...dayCols.map(d => fmt(t.per_day[d]))];
    let wk = 0; for (const d of sumDays) if (typeof t.per_day[d] === 'number') wk += t.per_day[d];
    row.push(fmt(wk));
    L('| ' + row.join(' | ') + ' |');
  }
  // fixed subtotal
  const subRow = ['**Fixed subtotal**', ...dayCols.map(d => fmt(c.per_day[d][cat].fixed))];
  subRow.push(fmt(sumDays.reduce((a, d) => a + c.per_day[d][cat].fixed, 0)));
  L('| ' + subRow.join(' | ') + ' |');
  for (const t of flex) {
    const row = [`${t.name} *(flex)*`, ...dayCols.map(d => fmt(t.per_day[d]))];
    let wk = 0; for (const d of sumDays) if (typeof t.per_day[d] === 'number') wk += t.per_day[d];
    row.push(fmt(wk));
    L('| ' + row.join(' | ') + ' |');
  }
  // total
  const totRow = ['**Total**', ...dayCols.map(d => fmt(c.per_day[d][cat].total))];
  totRow.push(fmt(sumDays.reduce((a, d) => a + c.per_day[d][cat].total, 0)));
  L('| ' + totRow.join(' | ') + ' |');
  L('');
  // conditional + NR notes for this category
  const cond = c.tasks.filter(t => t.category === cat && t.shape === 'conditional');
  const nr = c.tasks.filter(t => t.category === cat && t.shape === 'nr');
  if (cond.length) L(`> **Conditional (not counted):** ${cond.map(t => `${t.name} (0–${fmt(t.conditional_max)}, days: ${(t.days||[]).join(', ')})`).join(' · ')}`);
  if (nr.length) L(`> **NR (0 scheduled minutes, not counted):** ${nr.map(t => `${t.name} (days: ${(t.days||[]).join(', ')})`).join(' · ')}`);
  if (cond.length || nr.length) L('');
}

const breakdownCols = result.free_day_accounting === 'included' ? allDays : [...sumDays, freeDay];
renderBreakdown('POW', breakdownCols);
renderBreakdown('POF', breakdownCols);
renderBreakdown('Sleep', breakdownCols);

// 8. Task-to-day matrix
L('## Task-to-Day Matrix');
L('');
L(`✔ = scheduled · opt = conditional · NR = Not Required (0 scheduled minutes) · – = off. Rows in source order.`);
L('');
const mheader = ['Step', 'Task', ...allDays.map(d => DAYNAME[d].slice(0, 3))];
L('| ' + mheader.join(' | ') + ' |');
L('|' + mheader.map(() => '---').join('|') + '|');
const matrixTasks = c.tasks.slice().sort((a, b) => a.order - b.order);
for (const t of matrixTasks) {
  const row = [String(t.order), t.name, ...allDays.map(d => {
    if (!(t.days || []).includes(d)) return '–';
    if (t.shape === 'conditional') return 'opt';
    if (t.shape === 'nr') return 'NR';
    return '✔';
  })];
  L('| ' + row.join(' | ') + ' |');
}
L('');

// 9. Ranked weekly task hours
L('## Ranked Weekly Task Hours');
L('');
const denom = sumDays.length * 1440;
L(`> Sunday excluded — percentages are of the ${fmt(denom)} (${sumDays.length}×24h) counted week. Conditional and NR tasks carry 0 counted minutes and are not ranked.`);
L('');
L('| # | Task | Category | Wk Hours | % of Week |');
L('|---|---|---|---|---|');
for (const r of c.ranking) {
  L(`| ${r.rank} | ${r.name} | ${r.category} | ${fmt(r.weekly_minutes)} | ${r.percent.toFixed(1)}% |`);
}
L('');

// 10. Task details / execution notes
L('## Task Details / Execution Notes');
L('');
const detailTasks = c.tasks.slice().sort((a, b) => a.order - b.order).filter(t => t.notes || (Array.isArray(t.subtasks) && t.subtasks.length));
for (const t of detailTasks) {
  const shape = t.shape === 'flex' ? 'flex' : t.shape === 'conditional' ? `conditional (0–${fmt(t.conditional_max)})` : t.shape === 'nr' ? 'NR' : fmt(t.duration_minutes);
  L(`### ${t.order}. ${t.name} *(${t.category}, ${shape})*`);
  L('');
  L(`**Days:** ${(t.days || []).map(d => DAYNAME[d]).join(', ')}`);
  L('');
  if (t.notes) { L(t.notes); L(''); }
  if (Array.isArray(t.subtasks) && t.subtasks.length) {
    L('**Subtasks:**');
    L('');
    for (const s of t.subtasks) {
      let line = `- ${s.name}`;
      if (typeof s.duration_minutes === 'number') line += ` — ${fmt(s.duration_minutes)}`;
      if (Array.isArray(s.days) && s.days.length) line += ` — days: ${s.days.map(d => DAYNAME[d]).join(', ')}`;
      L(line);
      if (s.notes) { L(`  - ${s.notes}`); }
      if (Array.isArray(s.subtasks) && s.subtasks.length) {
        for (const ss of s.subtasks) L(`  - ${ss.name}${typeof ss.duration_minutes === 'number' ? ` — ${fmt(ss.duration_minutes)}` : ''}`);
      }
    }
    L('');
  }
}

const md = lines.join('\n');

// Write draft to temp.
if (!fs.existsSync(draftDir)) fs.mkdirSync(draftDir, { recursive: true });
const ts = new Date().toISOString().replace(/[:.]/g, '-');
const draftPath = path.join(draftDir, `build-schedule-sheet-${ts}-draft.md`);
fs.writeFileSync(draftPath, md, 'utf8');

const preflight = {
  ok: true,
  draft_path: draftPath,
  output_path: outputPath,
  source: sourceName,
  content_version: contentVersion,
  format_version: result.format_version,
  free_day_accounting: result.free_day_accounting,
  sections: SECTIONS,
  blockers: result.blockers,
  warnings: result.warnings,
  totals: {
    POW: fmt(result.computed.weekly.POW.total),
    POF: fmt(result.computed.weekly.POF.total),
    Sleep: fmt(result.computed.weekly.Sleep.total),
    total: fmt(result.computed.weekly.total),
    counted_days: sumDays,
  },
  message: 'Draft rendered. Review draft_path; on approval, write to output_path after rechecking collision.',
};
process.stdout.write(JSON.stringify(preflight, null, 2) + '\n');