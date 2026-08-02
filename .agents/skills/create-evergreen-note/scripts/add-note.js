#!/usr/bin/env node
// Append one evergreen-note entry (a single JSON object on stdin) to index.jsonl.
//
// The caller supplies: title, date, file, taskType, and optionally source and
// related. This script assigns id = max(existing ids) + 1 and appends one JSONL
// line. Creates the file (and its parent directory) if they do not yet exist —
// safe on a fresh clone, since git cannot track an empty b0ttsagent/Notes/Evergreen/ dir.
//
// Usage:
//   echo '{"title":"...","date":"2026-08-01","file":"b0ttsagent/Notes/Evergreen/x.md","taskType":"learn"}' \
//     | node add-note.js [--file <path>]
//
// Required: title, date, file, taskType
// Optional: source (defaults to null), related (defaults to [])
// Forbidden: id (assigned automatically — including it is an error)
// Constrained: taskType must be one of learn | decide | do | remember
//              related, if present, must be an array of strings

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function flag(name) {
  const i = args.indexOf(name);
  return i === -1 ? undefined : args[i + 1];
}
const file = path.resolve(process.cwd(), flag('--file') || 'b0ttsagent/Notes/Evergreen/index.jsonl');

const REQUIRED = ['title', 'date', 'file', 'taskType'];
const ALLOWED_TASK_TYPES = ['learn', 'decide', 'do', 'remember'];

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
  if (!ALLOWED_TASK_TYPES.includes(entry.taskType)) {
    console.error(`Error: taskType must be one of ${ALLOWED_TASK_TYPES.join(', ')}. Received: ${JSON.stringify(entry.taskType)}`);
    process.exit(1);
  }
  if (!('source' in entry)) entry.source = null;
  if (!('related' in entry)) {
    entry.related = [];
  } else if (!Array.isArray(entry.related) || !entry.related.every(v => typeof v === 'string')) {
    console.error('Error: "related" must be an array of strings (note titles or ids).');
    process.exit(1);
  }

  // Compute next id from existing file.
  let nextId = 1;
  if (fs.existsSync(file)) {
    const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(l => l.trim());
    if (lines.length) {
      const ids = lines.map(l => { try { return JSON.parse(l).id; } catch { return 0; } });
      nextId = Math.max(...ids, 0) + 1;
    }
  }

  // Fresh clones lose the empty Evergreen dir (git cannot track empty dirs),
  // so recreate it on demand before appending.
  fs.mkdirSync(path.dirname(file), { recursive: true });

  const record = { id: nextId, ...entry };
  fs.appendFileSync(file, JSON.stringify(record) + '\n', 'utf8');
  console.log(`Appended evergreen note #${nextId} -> ${file}`);
  console.log(JSON.stringify(record, null, 2));
});
