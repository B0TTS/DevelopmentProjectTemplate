#!/usr/bin/env node
// Query sessions.jsonl — the session resume index.
//
// Keeps resume-time context cost O(matches) instead of O(history): the agent
// never has to read the whole log back into context to find an entry.
//
// Usage:
//   node query-sessions.js [filters]
//
// Filters (all optional, combinable):
//   --latest <N>        show only the last N matches (after other filters)
//   --search <text>    case-insensitive substring match on title + description
//   --harness <name>   exact (case-insensitive) agentHarness match
//   --device <name>    exact (case-insensitive) device match
//   --file <path>      path to the jsonl (default: b0ttsagent/sessionlogs/sessions.jsonl)
//   --json             emit raw JSONL instead of the markdown view
//
// With no filters, prints the latest 10 sessions.

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const file = path.resolve(process.cwd(), flag('--file') || 'b0ttsagent/sessionlogs/sessions.jsonl');
const latestRaw = flag('--latest');
const latest = latestRaw != null ? parseInt(latestRaw, 10) : null;
const search = flag('--search');
const harness = flag('--harness');
const device = flag('--device');
const asJson = args.includes('--json');

if (!fs.existsSync(file)) {
  console.error(`Error: not found: ${file}`);
  process.exit(1);
}

let entries = fs.readFileSync(file, 'utf8')
  .split(/\r?\n/)
  .filter(l => l.trim())
  .map(l => {
    try { return JSON.parse(l); }
    catch { return null; }
  })
  .filter(Boolean);

if (search) {
  const s = search.toLowerCase();
  entries = entries.filter(e => `${e.title || ''} ${e.description || ''}`.toLowerCase().includes(s));
}
if (harness) {
  const h = harness.toLowerCase();
  entries = entries.filter(e => (e.agentHarness || '').toLowerCase() === h);
}
if (device) {
  const d = device.toLowerCase();
  entries = entries.filter(e => (e.device || '').toLowerCase() === d);
}

const limit = (latest != null && !Number.isNaN(latest)) ? latest : (args.length === 0 ? 10 : entries.length);
const shown = (limit != null) ? entries.slice(-limit) : entries;

if (asJson) {
  shown.forEach(e => console.log(JSON.stringify(e)));
} else {
  if (!shown.length) { console.log('No sessions match.'); process.exit(0); }
  for (const e of shown) {
    const desc = (e.description || '')
      .split(/\r?\n/)
      .map(l => `- ${l}`)
      .join('\n');
    console.log(`## ${e.title || '(untitled)'}`);
    console.log(`#### ID: ${e.id}`);
    console.log(`#### Date: ${e.date || 'Unknown'}`);
    console.log(`#### Resume Command: \`${e.resumeCommand || ''}\``);
    console.log(`#### Agent Harness: ${e.agentHarness || 'Unknown'}`);
    console.log(`#### Device: ${e.device || 'Unknown'}`);
    console.log(`#### Description:`);
    console.log(desc);
    console.log(`\n---\n`);
  }
}
console.error(`${shown.length} session(s).`);