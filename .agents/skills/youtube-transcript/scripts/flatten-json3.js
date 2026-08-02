#!/usr/bin/env node
// Flatten a yt-dlp json3 caption file into a clean single-line .txt.
// Usage: node flatten-json3.js <file.json3> [out.txt]
// Default output: same directory + basename as the source, .txt extension.
// Prints the output path on success.

const fs = require("fs");
const path = require("path");

// json3 "utf8" text occasionally carries HTML entities (e.g. &amp;, &#39;, &quot;).
const named = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " " };
function unescape(text) {
  return text
    .replace(/&#(\d+);/g, (_, d) => String.fromCodePoint(Number(d)))
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&([a-z]+);/gi, (m, n) => named[n.toLowerCase()] ?? m);
}

const src = process.argv[2];
if (!src) {
  console.error("usage: node flatten-json3.js <file.json3> [out.txt]");
  process.exit(2);
}

const data = JSON.parse(fs.readFileSync(src, "utf8"));
const lines = (data.events || [])
  .map((e) => (e.segs || []).map((s) => s.utf8 || "").join(""))
  .filter((l) => l.trim().length > 0);
const text = unescape(lines.join(" ")).replace(/\s+/g, " ").trim();

const out =
  process.argv[3] ||
  path.join(path.dirname(src), path.basename(src, path.extname(src)) + ".txt");
fs.writeFileSync(out, text + "\n", "utf8");
console.log(out);
