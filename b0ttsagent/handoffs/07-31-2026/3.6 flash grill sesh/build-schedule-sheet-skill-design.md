# Handoff: Build Schedule Sheet Skill Design

## Overview & Goal
Designed the specification for a new Agent Skill (`build-schedule-sheet`) to automate creating and updating 13-table **Schedule Sheets** (weekly schedule breakdowns) from **Schedule Specs** (architecture documents).

## Artifact Reference
All decisions, user answers, and internal decision-tree resolutions are recorded in the structured JSON session artifact:
* **Grill Session Log:** `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\handoffs\07-31-2026\3.6 flash grill sesh\grill-session-weekly-schedule-skill-2.json`

---

## Accomplished & Key Decisions

1. **Terminology & Concepts**
   * **Input:** **Schedule Specs** (architecture/source documents, e.g., `b0ttsagent/Notes/Schedule Architecture V4.1.md`).
   * **Output:** **Schedule Sheets** (the 13-table canonical breakdown, e.g., `b0ttsagent/Notes/weekly-scheduleV5.md`).

2. **File Paths & Versioning**
   * **Naming Pattern:** Output Sheets directly match the input Spec version (e.g., `Schedule Spec V4.1` → `weekly-schedule-sheet-V4.1.md`).
   * **Location:** Saved alongside notes/specs in `b0ttsagent/Notes/`.

3. **Output Format (13 Canonical Tables)**
   Enforces the exact structure established in `weekly-scheduleV5.md`:
   * Table 1: Master Summary (Hours per Day, Mon–Sat)
   * Tables 2–8: Per-Day Ordered Schedules (Mon through Sun) with Spec step `#` numbers
   * Table 9: Work (POW) Breakdown by Day + Weekly Total
   * Table 10: Free (POF) Breakdown by Day + Weekly Total
   * Table 11: Sleep Breakdown by Day
   * Table 12: Task-to-Day Matrix
   * Table 13: Weekly Hours by Task (Ranked, Mon–Sat)
   * Insight Highlights
   * Clarifying Q&A Log

4. **Mathematical & Re-balancing Rules**
   * **Mon–Sat Target:** 8.0h POW + 8.0h POF + 8.0h Sleep = 24.0h daily total (144.0h Mon–Sat week total).
   * **Sunday Target (Freeday):** 0.0h POW + 16.0h POF + 8.0h Sleep = 24.0h. Excluded from Mon–Sat weekly totals.
   * **Flex Blocks:** `Work (flex)` and `Extra Personal Freetime (flex)` fill remaining daily hours to hit exact targets.
   * **NR Tasks:** Carry `0.0h` scheduled hours.

5. **Execution Workflow**
   * **Interactive Clarification First:** Surfacing any spec ambiguities or math gaps to the user before writing the Sheet, recording answers in a `## ❓ Clarifying Q&A` section.
   * **Math Verification Loop:** Pre-output pass checking all row and column sums against raw input.

---

## Relevant Files & Paths
* **Reference Spec:** `b0ttsagent/Notes/Schedule Architecture V4.1.md`
* **Reference Output Sheet:** `b0ttsagent/Notes/weekly-scheduleV5.md`
* **Target Skill Location (When Ready to Build):** `.agents/skills/build-schedule-sheet/SKILL.md`

---

## Suggested Next Steps & Skills for Next Session

When ready to author and implement the skill file:
1. **`write-a-skill-v2`** — Use to scaffold `.agents/skills/build-schedule-sheet/SKILL.md` per `agentskills.io` standards (trigger router, progressive disclosure, copy-in checklist).
2. **`karpathy-guidelines`** — Apply guidelines for surgical, verifiable math logic and minimal over-engineering.
