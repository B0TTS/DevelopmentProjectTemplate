#!/usr/bin/env node
"use strict";
// grill-me-v3 transcript helper.
//
// Keeps the read-modify-write of the growing qAndA array OUT of the agent's
// context. User questions are logged before they are displayed, so the agent
// never has to reconstruct a question after receiving the answer. Node-only,
// no jq required.
//
//   GRILL_QUESTION="..." node append.js ask <session.json>
//   GRILL_ANSWER="..." node append.js answer <session.json>
//   GRILL_QUESTION="..." node append.js decision <session.json>
//   node append.js close  <session.json> --summary "approved summary text"
//   node append.js remove <session.json> --entry N [--yes]
//   node append.js state  <session.json>

const { readFile, writeFile } = require("node:fs/promises");

const [action, targetPath] = process.argv.slice(2);

function usage() {
  process.stderr.write(
    `grill-me-v3 transcript helper
usage:
  GRILL_QUESTION="..." node append.js ask <session.json>
  GRILL_ANSWER="..." node append.js answer <session.json>
  GRILL_QUESTION="..." node append.js decision <session.json>
  node append.js close  <session.json> --summary "approved summary text"
  node append.js remove <session.json> --entry N [--yes]
  node append.js state  <session.json>
`
  );
  process.exit(1);
}

function die(msg) {
  process.stderr.write(`grill-append error: ${msg}\n`);
  process.exit(1);
}

const nowIso = () => new Date().toISOString();

async function load(p) {
  let text;
  try {
    text = await readFile(p, "utf8");
  } catch (e) {
    die(`Could not read session file: ${p} (${e.message})`);
  }
  try {
    return JSON.parse(text);
  } catch (e) {
    die(`Session file is not valid JSON: ${p} (${e.message})`);
  }
}

async function save(p, data) {
  await writeFile(p, JSON.stringify(data, null, 2) + "\n", "utf8");
}

if (!action || !targetPath) usage();

function requireActive(data, operation) {
  if (data.status !== "active") {
    die(
      `Refusing to ${operation}: session status is "${data.status}", not "active". ` +
        `Reopen or start a new session.`
    );
  }
}

function ensureEntries(data) {
  if (!Array.isArray(data.qAndA)) data.qAndA = [];
  return data.qAndA;
}

(async () => {
  if (action === "ask") {
    const question = process.env.GRILL_QUESTION;
    if (question == null || question.length === 0) {
      die("Set GRILL_QUESTION to the complete question before running ask.");
    }
    const data = await load(targetPath);
    requireActive(data, "log a question");
    const entries = ensureEntries(data);
    const pending = entries.findIndex((entry) => entry.answer === null);
    if (pending !== -1) {
      die(`Refusing to log a question: entry #${pending + 1} is still awaiting an answer.`);
    }
    entries.push({ question, answer: null, timestamp: nowIso() });
    await save(targetPath, data);
    process.stdout.write(
      `Logged question #${entries.length} to ${targetPath}. Ask the user using the exact GRILL_QUESTION text; do not paraphrase it.\n`
    );
  } else if (action === "answer") {
    const answer = process.env.GRILL_ANSWER;
    if (answer == null) {
      die("Set GRILL_ANSWER to the user's complete, verbatim response before running answer.");
    }
    const data = await load(targetPath);
    requireActive(data, "record an answer");
    const entries = ensureEntries(data);
    const pending = entries
      .map((entry, index) => (entry.answer === null ? index : -1))
      .filter((index) => index !== -1);
    if (pending.length === 0) {
      die("Refusing to record an answer: no question is awaiting an answer.");
    }
    if (pending.length > 1) {
      die(`Refusing to record an answer: ${pending.length} questions are awaiting answers.`);
    }
    const index = pending[0];
    entries[index].answer = answer;
    entries[index].answeredAt = nowIso();
    await save(targetPath, data);
    process.stdout.write(`Recorded answer for question #${index + 1} in ${targetPath}.\n`);
  } else if (action === "decision" || action === "append") {
    const question = process.env.GRILL_QUESTION;
    const answer =
      action === "decision"
        ? "(self-resolved — user may veto)"
        : process.env.GRILL_ANSWER;
    if (question == null || answer !== "(self-resolved — user may veto)") {
      die(
        `${action} is only for self-resolved decisions. ` +
          `Use ask before a user question, then answer after the user responds.`
      );
    }
    const data = await load(targetPath);
    requireActive(data, "record a decision");
    const entries = ensureEntries(data);
    const pending = entries.findIndex((entry) => entry.answer === null);
    if (pending !== -1) {
      die(`Refusing to record a decision: entry #${pending + 1} is still awaiting an answer.`);
    }
    entries.push({ question, answer, timestamp: nowIso() });
    await save(targetPath, data);
    process.stdout.write(`Recorded self-resolved decision #${entries.length} in ${targetPath}.\n`);
  } else if (action === "close") {
    const i = process.argv.indexOf("--summary");
    if (i === -1 || !process.argv[i + 1]) {
      die('close requires: --summary "approved summary text"');
    }
    const summary = process.argv[i + 1];
    const data = await load(targetPath);
    if (data.status === "complete") die("Session is already complete.");
    const pending = ensureEntries(data).findIndex((entry) => entry.answer === null);
    if (pending !== -1) {
      die(`Refusing to close: entry #${pending + 1} is still awaiting an answer.`);
    }
    data.status = "complete";
    data.summary = summary;
    await save(targetPath, data);
    process.stdout.write(
      `Closed session ${targetPath}: summary set, status=complete.\n`
    );
  } else if (action === "state") {
    const data = await load(targetPath);
    process.stdout.write(
      JSON.stringify(
        {
          topic: data.topic,
          startedAt: data.startedAt,
          status: data.status,
          entries: Array.isArray(data.qAndA) ? data.qAndA.length : 0,
          summary: data.summary ?? null,
        },
        null,
        2
      ) + "\n"
    );
  } else if (action === "remove") {
    const i = process.argv.indexOf("--entry");
    if (i === -1 || !process.argv[i + 1])
      die('remove requires: --entry N (1-based index, as shown by append).');
    const raw = process.argv[i + 1];
    const n = Number(raw);
    if (!Number.isInteger(n) || n < 1)
      die(`remove: --entry must be a positive 1-based integer (got "${raw}").`);
    const yes = process.argv.includes("--yes");
    const data = await load(targetPath);
    const count = Array.isArray(data.qAndA) ? data.qAndA.length : 0;
    if (count === 0) die("Nothing to remove: qAndA is empty or missing.");
    if (n > count) die(`Entry #${n} does not exist. Valid range is 1..${count}.`);
    const entry = data.qAndA[n - 1];
    const preview =
      `Entry #${n}:\n` +
      `  question:   ${entry.question}\n` +
      `  answer:     ${entry.answer}\n` +
      `  timestamp:  ${entry.timestamp}\n`;
    const doRemove = async () => {
      data.qAndA.splice(n - 1, 1);
      await save(targetPath, data);
      const remaining = data.qAndA.length;
      process.stdout.write(
        `Removed entry #${n} from ${targetPath}.\n` +
        `${remaining} entr${remaining === 1 ? "y" : "ies"} remain.\n`
      );
    };
    if (yes) {
      await doRemove();
    } else if (process.stdin.isTTY) {
      process.stdout.write(preview + "\nDelete this entry? [y/N] ");
      const readline = require("node:readline");
      const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
      const answered = await new Promise((res) => rl.question("", res));
      rl.close();
      if (/^(y|yes)$/i.test(String(answered).trim())) await doRemove();
      else process.stdout.write("Aborted: entry not removed.\n");
    } else {
      process.stdout.write(
        preview +
        `\nReview this entry with the user, then re-run with --yes to delete it:\n` +
        `  node ${process.argv[1]} remove "${targetPath}" --entry ${n} --yes\n`
      );
    }
  } else {
    usage();
  }
})().catch((e) => die(e && e.message ? e.message : String(e)));