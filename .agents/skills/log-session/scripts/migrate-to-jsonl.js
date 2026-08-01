#!/usr/bin/env node
// One-time migration: parse b0ttsagent/sessionlogs/AI Sesssions.md into sessions.jsonl.
//
// Usage:
//   node migrate-to-jsonl.js [inputMd] [outputJsonl] [--force]
//
// Defaults:
//   inputMd      = b0ttsagent/sessionlogs/AI Sesssions.md
//   outputJsonl  = b0ttsagent/sessionlogs/sessions.jsonl
//
// Refuses to overwrite an existing output file unless --force (prevents clobbering
// a live log that has already been seeded and appended to).

const fs = require('fs');
const path = require('path');

const positional = process.argv.slice(2).filter(a => !a.startsWith('--'));
const force = process.argv.includes('--force');

const inputMd = path.resolve(process.cwd(), positional[0] || 'b0ttsagent/sessionlogs/AI Sesssions.md');
const outputJsonl = path.resolve(process.cwd(), positional[1] || 'b0ttsagent/sessionlogs/sessions.jsonl');

if (!fs.existsSync(inputMd)) {
  console.error(`Error: input markdown not found: ${inputMd}`);
  process.exit(1);
}
if (fs.existsSync(outputJsonl) && !force) {
  console.error(
    `Error: output already exists: ${outputJsonl}\n` +
    `Refusing to overwrite (would risk clobbering a live log).\n` +
    `Re-run with --force to overwrite.`
  );
  process.exit(1);
}

const md = fs.readFileSync(inputMd, 'utf8');

// Split on lines that are exactly '---'. The first chunk is the file preamble.
const lines = md.split(/\r?\n/);
const chunks = [];
let cur = [];
for (const line of lines) {
  if (line.trim() === '---') {
    chunks.push(cur);
    cur = [];
  } else {
    cur.push(line);
  }
}
chunks.push(cur);

const entries = [];
let id = 0;

for (const chunk of chunks) {
  const titleLine = chunk.find(l => /^##\s+/.test(l));
  if (!titleLine) continue; // preamble or empty chunk — skip

  id += 1;
  const entry = {
    id,
    title: titleLine.replace(/^##\s+/, '').trim(),
    date: null,
    resumeCommand: null,
    agentHarness: null,
    device: null,
    description: '',
  };

  // Header fields (#### Date: / #### Resume Command: / #### Agent Harness: / #### Device:)
  for (const line of chunk) {
    const m = line.match(/^####\s+(Date|Resume Command|Agent Harness|Device):\s*(.*)$/);
    if (!m) continue;
    let val = m[2].trim();
    const key = m[1];
    if (key === 'Resume Command') val = val.replace(/^`|`$/g, ''); // strip wrapping backticks
    switch (key) {
      case 'Date':          entry.date = val || null; break;
      case 'Resume Command': entry.resumeCommand = val || null; break;
      case 'Agent Harness': entry.agentHarness = val || null; break;
      case 'Device':        entry.device = val || null; break;
    }
  }

  // Description: collect the '- ' lines that follow '#### Description:'
  const descIdx = chunk.findIndex(l => /^####\s+Description:\s*$/.test(l));
  if (descIdx !== -1) {
    const descLines = [];
    for (let i = descIdx + 1; i < chunk.length; i++) {
      const l = chunk[i];
      if (/^####\s+/.test(l)) break;
      if (l.trim() === '') continue;
      const dm = l.match(/^\s*-\s+(.*)$/);
      descLines.push(dm ? dm[1].trim() : l.trim());
    }
    entry.description = descLines.join('\n');
  }

  entries.push(entry);
}

const out = entries.map(e => JSON.stringify(e)).join('\n') + '\n';
fs.writeFileSync(outputJsonl, out, 'utf8');

console.log(`Migrated ${entries.length} entries -> ${outputJsonl}`);
console.log(`ids 1..${entries.length} (file order preserved, duplicates kept with distinct ids)`);