#!/usr/bin/env node

// ── template-dev-installer ──────────────────────────────────────────
// Interactive installer that copies selected template categories into
// the current working directory.
//
// Categories:
//   1. Skills      — AGENTS.md, README.md, .agents/, b0ttsagent/ (additive)
//   2. OpenCode    — .opencode/plugins/, opencode.json, settings.json
//   3. Pi          — .pi/agent/settings.json, extensions/, mcp.json
//   4. All         — everything above
// ────────────────────────────────────────────────────────────────────

import checkbox, { Separator } from "./reactive-checkbox.mjs";
import { confirm } from "@inquirer/prompts";
import { cpSync, existsSync, mkdirSync, readdirSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const FILES = resolve(__dirname, "..", "files");
const CWD = process.cwd();

// ── Category definitions ────────────────────────────────────────────
// Each category maps to source dirs/files relative to ./files/ and
// their destination relative to the user's CWD.

const CATEGORIES = {
  skills: {
    label: "Skills (AGENTS.md, README.md, .agents/, b0ttsagent/)",
    items: [
      { src: "AGENTS.md",              dest: "AGENTS.md",              additive: true },
      { src: "README.md",              dest: "README.md",              additive: true },
      { src: ".agents",                dest: ".agents",                additiveSkills: true },
      { src: "b0ttsagent/temp",        dest: "b0ttsagent/temp",        additive: true },
      { src: "b0ttsagent/sessionlogs", dest: "b0ttsagent/sessionlogs", additive: true },
      { src: "b0ttsagent/handoffs",    dest: "b0ttsagent/handoffs",    additive: true },
      { src: "b0ttsagent/NavGuides",   dest: "b0ttsagent/NavGuides",   additive: true },
    ],
  },
  opencode: {
    label: "OpenCode (.opencode/plugins, opencode.json, settings.json)",
    items: [
      { src: "opencode/plugins",        dest: ".opencode/plugins" },
      { src: "opencode/opencode.json",  dest: ".opencode/opencode.json" },
      { src: "opencode/settings.json",  dest: ".opencode/settings.json" },
    ],
  },
  pi: {
    label: "Pi (.pi/agent/settings.json, extensions/, mcp.json)",
    items: [
      { src: "pi/settings.json",        dest: ".pi/agent/settings.json" },
      { src: "pi/extensions",           dest: ".pi/agent/extensions" },
      { src: "pi/mcp.json",             dest: ".pi/agent/mcp.json" },
    ],
  },
};

// ── Helpers ─────────────────────────────────────────────────────────

function warnIfExists(destPath) {
  if (existsSync(destPath)) {
    console.log(`  ⚠  ${destPath} already exists — will be overwritten.`);
  }
}

function copyItem(item, skillsFilter) {
  const src = resolve(FILES, item.src);
  const dest = resolve(CWD, item.dest);
  if (!existsSync(src)) {
    console.log(`  ✘  Source not found: ${item.src}  (skipping)`);
    return;
  }
  if (item.additiveSkills) {
    copyAdditiveSkills(src, dest, skillsFilter);
    return;
  }
  if (item.additive && existsSync(dest)) {
    console.log(`  →  ${item.dest} already exists — skipping.`);
    return;
  }
  if (!item.additive) {
    warnIfExists(dest);
  }
  cpSync(src, dest, { recursive: true, force: !item.additive });
  console.log(`  ✓  ${item.dest}`);
}

function copyAdditiveSkills(srcDir, destDir, skillsFilter) {
  const skillsSrc = resolve(srcDir, "skills");
  const skillsDest = resolve(destDir, "skills");

  if (!existsSync(skillsSrc)) {
    console.log(`  ✘  Source skills not found  (skipping)`);
    return;
  }

  mkdirSync(destDir, { recursive: true });
  mkdirSync(skillsDest, { recursive: true });

  let skills = readdirSync(skillsSrc, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name);

  // If a filter is provided, only copy selected skills
  if (skillsFilter) {
    skills = skills.filter((s) => skillsFilter.includes(s));
  }

  if (skills.length === 0) {
    console.log(`  →  .agents/skills/ — no skills selected, skipping.`);
    return;
  }

  let added = 0;
  let skipped = 0;
  for (const skill of skills) {
    const dest = resolve(skillsDest, skill);
    if (existsSync(dest)) {
      skipped++;
    } else {
      cpSync(resolve(skillsSrc, skill), dest, { recursive: true });
      added++;
    }
  }

  const filterNote = skillsFilter ? ` (${skills.length} selected)` : "";
  console.log(`  ✓  .agents/skills/ — ${added} added, ${skipped} already existed${filterNote}`);
}

function installCategory(name, skillsFilter) {
  const cat = CATEGORIES[name];
  console.log(`\n── Installing ${cat.label.split(" (")[0]} ──`);
  for (const item of cat.items) {
    copyItem(item, skillsFilter);
  }
}

// ── Main ────────────────────────────────────────────────────────────

async function main() {
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
  console.log("  Development Template Installer");
  console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n");

  const chosen = await checkbox({
    message: "Select categories to install (Space to toggle, Enter to confirm):",
    choices: [
      { name: "All",         value: "all",     isAll: true },
      new Separator(),
      { name: "Skills",      value: "skills" },
      { name: "OpenCode",    value: "opencode" },
      { name: "Pi",          value: "pi" },
    ],
  });

  if (chosen.length === 0) {
    console.log("Nothing selected. Aborted.");
    process.exit(0);
  }

  // Determine what to install
  const toInstall = chosen.includes("all")
    ? Object.keys(CATEGORIES)
    : chosen;

  // ── Skill selection ────────────────────────────────────────────
  let skillsFilter = null; // null = install all skills (no filter)
  if (toInstall.includes("skills")) {
    const skillsSrc = resolve(FILES, ".agents", "skills");
    const availableSkills = readdirSync(skillsSrc, { withFileTypes: true })
      .filter((d) => d.isDirectory())
      .map((d) => d.name)
      .sort();

    console.log(""); // spacer
    const chosenSkills = await checkbox({
      message: "Select skills to install:",
      choices: [
        { name: "All", value: "all", isAll: true },
        new Separator(),
        ...availableSkills.map((s) => ({ name: s, value: s })),
      ],
    });

    if (chosenSkills.length === 0) {
      // Remove skills from install list
      toInstall.splice(toInstall.indexOf("skills"), 1);
      if (toInstall.length === 0) {
        console.log("Nothing selected. Aborted.");
        process.exit(0);
      }
    } else if (chosenSkills.includes("all")) {
      skillsFilter = null; // all skills
    } else {
      skillsFilter = chosenSkills;
    }
  }

  const labels = toInstall.map((n) => CATEGORIES[n].label.split(" (")[0]).join(", ");
  const ok = await confirm({
    message: `Install ${labels} into ${CWD}?`,
    default: true,
  });
  if (!ok) {
    console.log("Aborted.");
    process.exit(0);
  }

  for (const name of toInstall) {
    installCategory(name, skillsFilter);
  }

  console.log("\n✔  Done.\n");
}

main().catch((err) => {
  console.error("Error:", err.message);
  process.exit(1);
});
