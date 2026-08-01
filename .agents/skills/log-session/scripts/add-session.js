#!/usr/bin/env node
// Append one session entry (a single JSON object on stdin) to sessions.jsonl.
//
// The caller supplies: title, date, resumeCommand, agentHarness, description,
// and optionally device. This script assigns id = max(existing ids) + 1 and
// appends one JSONL line. Creates the file if it does not yet exist.
//
// Usage:
//   echo '{"title":"...","date":"2026-08-01","resumeCommand":"pi --session ...","agentHarness":"Pi","description":"..."}' \
//     | node add-session.js [--file <path>]
//
// Required: title, date, resumeCommand, agentHarness, description
// Optional: device (defaults to null if omitted)
// Forbidden: id (assigned automatically — including it is an error)

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const file = path.resolve(process.cwd(), flag('--file') || 'b0ttsagent/sessionlogs/sessions.jsonl');

const REQUIRED = ['title', 'date', 'resumeCommand', 'agentHarness', 'description'];

let stdin = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', d => { stdin += d; });
process.stdin.on('end', () => {
  let entry;
  try { entry = JSON.parse(stdin); }
  catch (e) { console.error('Error: stdin is not valid JSON:', e.message); process.exit(1); }

  if (entry == null || typeof entry !== 'object' || Array.isArray(entry)) {
    console.error('Error: stdin must be a single JSON object.');
    process.exit(1);
  }
  for (const k of REQUIRED) {
    if (entry[k] == null || entry[k] === '') {
      console.error(`Error: missing required field "${k}"`);
      process.exit(1);
    }
  }
  if ('id' in entry) {
    console.error('Error: do not include "id" — it is assigned automatically.');
    process.exit(1);
  }
  if (!('device' in entry)) entry.device = null;

  // Compute next id from existing file.
  let nextId = 1;
  if (fs.existsSync(file)) {
    const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(l => l.trim());
    if (lines.length) {
      const ids = lines.map(l => { try { return JSON.parse(l).id; } catch { return 0; } });
      nextId = Math.max(...ids, 0) + 1;
    }
  }

  const record = { id: nextId, ...entry };
  fs.appendFileSync(file, JSON.stringify(record) + '\n', 'utf8');
  console.log(`Appended session #${nextId} -> ${file}`);
  console.log(JSON.stringify(record, null, 2));
});