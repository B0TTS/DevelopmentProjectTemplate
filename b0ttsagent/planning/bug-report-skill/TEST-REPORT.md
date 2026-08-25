# Bug-Report Skill — Test Report

Date: 2026-08-21
Method: per `write-a-skill-v2`, tests were run as **fresh runner sessions**
(orchestrated b0tts-general-agent subagents, each simulating a fresh session
loading the `bug-report` skill via the `skill` tool), then verified on disk.

Spec under test: `SPEC.md` (this directory). Evaluations reference:
`.agents/skills/bug-report/references/evaluations.md`.

---

## Result summary

| Seam | Scenario | Result |
|------|----------|--------|
| 1a | Report a bug end-to-end (most details missing) | **PASS** |
| 1b | Feature request phrased like a bug (negative boundary) | **PASS** |
| 2  | Registry contract (invariant) | **PASS** (1 note) |
| 3  | "I fixed X, mark it fixed" (mark-fixed path) | **PASS** |

All seams passed. One real defect surfaced and was repaired (see Finding 1).

---

## Seam 1a — Skill invocation (end-to-end report)

**Runner A** reported: "There's a bug. The template dev installer keeps crashing
when I run it. I think it's broken." (most intake fields missing).

Verified:
- Skill loaded via `skill` tool; fired on natural-language bug phrasing and
  routed to Mode A.
- **Dedupe first** — ran `query-bugs.js --search` (registry-missing error handled
  gracefully on first run) and scanned bug docs. No duplicates found.
- **Intake** — exactly **4 questions**, batched into **one numbered list**
  (repro → expected/actual → environment → impact), extraction-first, no
  re-asking of stated facts.
- **Title + severity** — 3 title candidates proposed; user picked first
  ("Template dev installer crashes on startup in PowerShell 7"). Severity
  inferred from impact → `high`.
- **Read-back** — full summary (id, title, severity, description, repro,
  expected/actual, environment, impact, target filepath) presented **before
  any disk write**; confirmed.
- **Record** — doc at
  `b0ttsagent/bugs/open/2026-08-21-template-dev-installer-crash.md` with
  correct front matter (`id`, `title`, `severity`, `state: open`, `created_at`)
  and all prose sections; Suspected Causes / Ruled Out left as placeholders.
  Registry line 1 appended: `state: open`, `causes: []`,
  `created_at = updated_at = 2026-08-21`.
- **Investigation (read-only)** — entry points derived from the repro
  (installer package). No source files modified, no git history used. Three
  suspected causes appended under `### Investigation — 2026-08-21`, each with
  confidence + `file:line` evidence + "what would confirm this". Ruled-out and
  open questions recorded under `### As of 2026-08-21`.
- Registry line 2 appended: same id, `state: open` (unchanged), `causes[]`
  populated, `updated_at` refreshed.
- **Refused to fix** — runner explicitly recorded that fix temptation was
  stopped by the skill's refusal rules.

---

## Seam 1b — Negative boundary (feature request phrased like a bug)

**Runner B** reported: "It'd be cool if the template dev installer could also
scaffold a Rust project template — right now there's no way to do that. Kind of
feels like a bug that it doesn't support it."

Verified:
- Skill loaded; classified as **feature request**, not a bug (nothing broken;
  no repro/symptom/impact; "expected vs actual" inapplicable).
- Refused cleanly per the skill's "NOT for feature requests … say so and stop —
  do not partly comply".
- **Zero writes** — no doc created, no registry line appended, no investigation
  run, no state transitions. `bugs.jsonl` line count unchanged.

---

## Seam 3 — Mark-fixed path

**Runner C** reported: "I fixed the template dev installer crash, mark it fixed."

Verified:
- Routed to **Mode B** (not Mode A) — no new bug filed, no new investigation.
- Located the bug via `query-bugs.js --search` (collapsed to
  `2026-08-21-template-dev-installer-crash`).
- **Confirmed** the bug (id + filepath) with the user **before** any change.
- Document moved `b0ttsagent/bugs/open/` → `b0ttsagent/bugs/fixed/` (same
  filename).
- Front matter `state` → `closed`; `id`, `title`, `severity`, `created_at`
  unchanged; body sections intact (targeted front-matter edit, not rewrite).
- Registry line 3 appended: same `id`, `state: closed`, `filepath` under
  `fixed/`, `updated_at` refreshed, all other fields carried forward.

---

## Seam 2 — Registry contract (invariant)

Checked after all runs (3 lines in `b0ttsagent/bugs/bugs.jsonl`):
- Every line parses as JSON. **PASS**
- All 10 schema keys present per line (`id`, `state`, `title`, `description`,
  `causes`, `filepath`, `severity`, `created_at`, `updated_at`, `related`). **PASS**
- `state` ∈ {open, in progress, closed}. **PASS**
- `severity` ∈ {low, medium, high, critical, unknown}. **PASS**
- Date fields match `YYYY-MM-DD`. **PASS**
- **Latest-wins** holds — `query-bugs.js --id` returns the last line per id
  (the `closed` line). **PASS**
- Query filters work: `--state closed`, `--severity high`, `--search`,
  `--id`, `--json`, default list. **PASS**
- Strict UTF-8 decode of the whole file. **PASS** (after repair, see Finding 1)

**Note:** historical registry lines (1–2) reference the pre-move `open/`
path, which no longer resolves after the bug moved to `fixed/`. This is
inherent to append-only latest-wins: only the **latest line per id** is
authoritative, so the "filepath resolves" check should be evaluated on the
latest line per id, not on every line.

---

## Findings to feed back into the skill

1. **HIGH — JSONL encoding hazard (real corruption).** The skill says to append
   a registry line "by hand" but never mandates encoding. Runner A appended via
   PowerShell `Add-Content` (default ANSI) → em-dashes in `causes[]` became
   mojibake, producing **invalid UTF-8** in `bugs.jsonl`. Repaired by rewriting
   the registry as clean UTF-8 with ASCII-safe separators (semantics unchanged).
   Runner C only avoided the issue by using an explicit .NET UTF-8 (no-BOM)
   append. Recommendation: add one line to SKILL.md — append registry lines as
   valid UTF-8 (no BOM) and/or keep registry strings ASCII-safe.

2. **MED — `rg` not on PATH.** Step 1's dedupe command
   (`rg -l -i "<keywords>" b0ttsagent/bugs/open b0ttsagent/bugs/fixed`) failed
   in this harness; the runner improvised with the grep/glob tools. Add a
   fallback instruction (grep tool / `Select-String`).

3. **LOW — first-run bootstrap unspecified.** The skill never says to create
   `b0ttsagent/bugs/{open,fixed}/` when absent; runners guessed it. One line
   would remove ambiguity.

4. **LOW — slug derivation ambiguity.** The stopword list omits prepositions
   like "on", and the ~5-word/~40-char cap is loose. Runner A's confirmed title
   produced a longer token slug; the runner trimmed to the read-back-confirmed
   id. Recommend clarifying that the read-back-confirmed id is authoritative.

5. **LOW — Mode B mechanics unspecified.** "Move the document" and "update
   front matter" don't say how: use the filesystem move (not `git mv`), and a
   targeted front-matter-only edit (a full rewrite would violate
   body-preservation).

6. **NOTE — sub-agent availability.** b0tts-general-agent subagents have no
   `task` tool, so the skill's "in a harness without sub-agents, run the
   focused read-only passes yourself" fallback fired. Already documented in the
   skill — worked as intended.

7. **NOTE — negative boundary placement.** The feature-request boundary lives
   only in the trigger description and the "What this skill refuses" paragraph,
   not restated in the Mode A/B routing section. Runners found it, but it could
   be surfaced in routing.

---

## Current on-disk state (post-test)

- `b0ttsagent/bugs/open/` — empty.
- `b0ttsagent/bugs/fixed/2026-08-21-template-dev-installer-crash.md` — kept as
  a real bug record (state: closed).
- `b0ttsagent/bugs/bugs.jsonl` — 3 lines (open → causes → closed) for one id,
  valid UTF-8.

Per owner decision: skill files (`SKILL.md`, `references/evaluations.md`) were
**not** modified — findings reported here only.
