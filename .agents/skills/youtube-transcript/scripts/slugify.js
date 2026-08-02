#!/usr/bin/env node
// Slugify "Channel|Title" into a Windows-safe filename:
//   whitespace / | -> "_"
//   keep Unicode letters, digits, combining marks, and _ . -
//   strip Windows-illegal chars (<>:"/\|?*) and control chars
//   collapse underscore runs, trim leading/trailing . and _, cap at 100 chars
// Usage: node slugify.js "Channel|Title"
// Prints the slug (empty string if nothing survives — caller falls back to video ID).

const input = process.argv[2] || "";
const out = input
  .replace(/[\s|]+/g, "_")
  .replace(/[<>:"/\\|?*\x00-\x1f]/g, "")
  .replace(/[^\p{L}\p{M}\p{N}_.-]/gu, "")
  .replace(/_+/g, "_")
  .replace(/^[._]+|[._]+$/g, "")
  .slice(0, 100);
console.log(out);
