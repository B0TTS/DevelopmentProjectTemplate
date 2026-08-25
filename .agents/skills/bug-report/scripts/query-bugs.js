#!/usr/bin/env node
// Query b0ttsagent/bugs/bugs.jsonl — the bug registry index.
//
// The registry is append-only, latest-wins: a bug id may appear on multiple
// lines (creation, cause updates, mark-fixed); the LAST line per id is
// authoritative. This script collapses to the latest line per id BEFORE
// filtering, so results always reflect current state.
//
// Keeps query context cost O(matches) instead of O(history): the agent (and
// the owner) never have to read the whole registry into context to find a bug.
// Used by the bug-report skill for the dedupe check (Step 1) and for ad-hoc
// owner queries.
//
// Usage:
//   node query-bugs.js [filters]
//
// Filters (all optional, combinable):
//   --state <s>      open | in progress | closed            (case-insensitive)
//   --severity <s>   low | medium | high | critical | unknown (case-insensitive)
//   --search <text>  case-insensitive substring on title + description + causes
//   --id <id>        exact id match (e.g. 2025-08-18-login-crash)
//   --latest <N>     show only the N most-recently-updated matches (after other filters)
//   --file <path>    path to the jsonl (default: b0ttsagent/bugs/bugs.jsonl)
//   --json           emit raw JSONL (one object per match) instead of the markdown view
//
// With no filters, prints the 10 most-recently-updated bugs.

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const file = path.resolve(process.cwd(), flag('--file') || 'b0ttsagent/bugs/bugs.jsonl');
const state = flag('--state');
const severity = flag('--severity');
const search = flag('--search');
const idFilter = flag('--id');
const latestRaw = flag('--latest');
const latest = latestRaw != null ? parseInt(latestRaw, 10) : null;
const asJson = args.includes('--json');

if (!fs.existsSync(file)) {
  console.error(`Error: registry not found: ${file}`);
  process.exit(1);
}

// Read all lines; keep the LAST occurrence per id (latest-wins). Unparseable
// lines are skipped, not fatal — a hand-edited bad line shouldn't crash queries.
const byId = new Map();
const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(l => l.trim());
for (const line of lines) {
  let obj;
  try { obj = JSON.parse(line); } catch { continue; }
  if (obj == null || obj.id == null) continue;
  byId.set(obj.id, obj); // later set overwrites earlier → last line per id wins
}
let entries = Array.from(byId.values());

if (state) {
  const s = state.toLowerCase();
  entries = entries.filter(e => (e.state || '').toLowerCase() === s);
}
if (severity) {
  const s = severity.toLowerCase();
  entries = entries.filter(e => (e.severity || '').toLowerCase() === s);
}
if (search) {
  const s = search.toLowerCase();
  entries = entries.filter(e =>
    `${e.title || ''} ${e.description || ''} ${(e.causes || []).join(' ')}`
      .toLowerCase().includes(s)
  );
}
if (idFilter) {
  entries = entries.filter(e => e.id === idFilter);
}

// Most recently updated first (lexicographic on YYYY-MM-DD; fall back to created_at).
entries.sort((a, b) => {
  const da = a.updated_at || a.created_at || '';
  const db = b.updated_at || b.created_at || '';
  return db.localeCompare(da);
});

const noFilters = !state && !severity && !search && !idFilter;
const limit = (latest != null && !Number.isNaN(latest)) ? latest : (noFilters ? 10 : entries.length);
const shown = (limit != null) ? entries.slice(0, limit) : entries;

if (asJson) {
  shown.forEach(e => console.log(JSON.stringify(e)));
} else {
  if (!shown.length) { console.log('No bugs match.'); process.exit(0); }
  for (const e of shown) {
    const causes = (e.causes && e.causes.length)
      ? e.causes.map(c => `  - ${c}`).join('\n')
      : '  - (none yet — investigation pending or inconclusive)';
    const related = (e.related && e.related.length) ? e.related.join(', ') : '(none)';
    console.log(`## ${e.title || '(untitled)'}`);
    console.log(`- ID: ${e.id}`);
    console.log(`- State: ${e.state || 'unknown'}`);
    console.log(`- Severity: ${e.severity || 'unknown'}`);
    console.log(`- File: ${e.filepath || '(missing)'}`);
    console.log(`- Created: ${e.created_at || 'unknown'}  |  Updated: ${e.updated_at || 'unknown'}`);
    console.log(`- Description: ${e.description || ''}`);
    console.log(`- Suspected causes:`);
    console.log(causes);
    console.log(`- Related: ${related}`);
    console.log(`\n---\n`);
  }
}
console.error(`${shown.length} bug(s).`);
