# Bug-Report Skill — Spec

## Problem Statement

Bugs in this repository currently get described in passing during chat sessions and then disappear with the conversation. There is no durable record of what broke, how to reproduce it, how severe it is, or what the suspected cause was. When the owner finally gets around to a bug, the context (reproduction steps, environment details, the reasoning behind a suspected cause) has to be rebuilt from scratch or is simply lost. The result is repeated investigation work, duplicates of already-known bugs, and no way to triage or search the bug backlog.

## Solution

A `bug-report` agent skill that turns a spoken bug report into a structured, searchable bug record and a codebase investigation — all without the user doing paperwork.

When the user reports a bug, the skill runs a short intake Q&A (at most ~4 questions, asking only what the user hasn't already said) to reach shared understanding: reproduction steps, expected vs actual behavior, environment, and impact. It then writes the bug as an in-depth Markdown document under the bug-document root and appends a concise machine-readable entry to a JSONL registry. After the record is written, the skill investigates the codebase — orchestrating read-only explorer sub-agents to probe suspect areas — and appends suspected causes (multiple allowed, each with confidence and evidence) to the same Markdown document and registry entry.

The skill also has a second, small mode: when the user says they've fixed a bug, the skill moves the document to the fixed-bugs folder and appends the registry update.

Everything the skill produces is human-readable today and machine-queryable later (the registry is deliberately shaped so a future web app could consume it with no migration).

## User Stories

1. As a repo owner, I want to describe a bug in my own words and have the agent ask only for the details I didn't provide, so that I never repeat myself.
2. As a repo owner, I want the intake Q&A capped at ~4 questions, so that reporting a bug stays fast and doesn't feel like an interrogation.
3. As a repo owner, I want to be able to answer "unknown" to any intake question, so that a missing detail never blocks the report.
4. As a repo owner, I want the agent to check whether a similar bug is already recorded before questioning me, so that I don't create duplicates.
5. As a repo owner, I want to review a short read-back summary before anything is written to disk, so that the record reflects what I actually meant.
6. As a repo owner, I want each bug saved as a human-readable Markdown document, so that I can open and read any bug standalone.
7. As a repo owner, I want bug documents named by date and slug, so that a folder listing is automatically chronological.
8. As a repo owner, I want open bugs and fixed bugs in separate folders, so that I can see at a glance what still needs attention.
9. As a repo owner, I want a single JSONL registry of all bugs, so that I can list and search the backlog without opening any documents.
10. As a repo owner, I want each registry entry to carry state, title, description, causes, filepath, id, timestamps, severity, and related-bug links, so that the registry is self-sufficiently queryable.
11. As a repo owner, I want registry updates appended as new lines with the latest line per bug winning, so that manual edits stay safe and the append history is preserved.
12. As a repo owner, I want registry filepath links relative to the project root, so that the registry stays portable if the project moves.
13. As a repo owner, I want to fix a bug and then just say so — "I fixed X, mark it fixed" — so that the document moves to the fixed folder and the registry updates in one step.
14. As a repo owner, I want to be able to update the registry by hand myself, so that bookkeeping works even without an agent session.
15. As a repo owner, I want each bug assigned a severity (low/medium/high/critical), so that I can triage what to work on first.
16. As a repo owner, I want the agent to investigate the codebase after recording the bug, so that a suspected cause is waiting for me without my asking.
17. As a repo owner, I want the investigation to derive its entry points from my reproduction steps, so that it looks where the bug actually manifests.
18. As a repo owner, I want the investigation orchestrated as read-only explorer sub-agents, so that several suspect areas are probed efficiently and the code is never modified.
19. As a repo owner, I want multiple suspected causes documented, so that less-obvious causes aren't discarded.
20. As a repo owner, I want each suspected cause to carry a confidence level and a "what would confirm this" note, so that I know how much to trust it and how to verify it.
21. As a repo owner, I want cause claims to cite file and line, so that hypotheses are evidence-backed rather than speculative.
22. As a repo owner, I want the investigation to stop at hypotheses, so that the skill never wanders into fixing the bug.
23. As a repo owner, I want inconclusive investigations to record what was ruled out and what remains open, so that future sessions don't redo the work.
24. As a repo owner, I want later investigations to append new sections without rewriting earlier ones, so that each document remains a trail of reasoning over time.
25. As a repo owner, I want a query script that lists and searches the registry by state, severity, and keyword, so that I can find bugs without loading the whole registry into an agent's context.
26. As a repo owner, I want the skill to refuse feature requests and bug-fixing work, so that it stays single-purpose and never blurs into other flows.
27. As a repo owner, I want the bug-document template stored as a reference file inside the skill, so that formatting stays consistent across sessions without extra scripts.
28. As a future tool author, I want the registry to be a clean, append-only JSONL, so that building a web app over it later needs no migration.

## Implementation Decisions

### Skill identity and placement

- Skill name `bug-report`, living at `.agents/skills/bug-report/` (name matches directory, per the Agent Skills standard).
- Skill authoring itself follows the `write-a-skill-v2` skill — the build session invokes it and applies its guidelines (progressive disclosure, trigger-description rules, two-instance testing). This spec does not duplicate those guidelines; it only records design decisions.
- The skill has **two entry modes**: (a) the bug-report flow (four steps below), and (b) the mark-fixed flow ("I fixed X, mark it fixed"). The trigger description must route both phrasings and carry a negative boundary: NOT feature requests, NOT fixing the bug.

### Step 1 — Intake Q&A

- **Extraction-first:** harvest everything the user's report already contains; ask only for gaps. Never re-ask what was stated.
- **Ordering:** reproduction steps → expected vs actual → environment → impact.
- **Hybrid batching:** routine fields are asked in one numbered batch; ambiguous or contradictory answers are probed individually.
- **Skip rules:** any field may be answered "unknown" without blocking the flow.
- **Question cap:** at most ~4 questions total. Once minimal reproduction and impact are captured, stop.
- **Dedupe first:** before any questions, check existing bugs (via the query script and a keyword scan of the bug documents) for a possible duplicate or related bug; if found, surface it and let the user decide whether to link instead of filing new.
- **Read-back:** a short summary of everything to be written is presented and confirmed by the user before anything touches disk.
- **Explicitly out:** context auto-fill (environment/OS guessed from the project) is not used; the user answers the environment question.

### Step 2 — Record (storage architecture: hybrid)

Two folders, one registry, human-readable docs + machine-readable index:

- `b0ttsagent/bugs/open/` — active bugs (state `open` or `in progress`).
- `b0ttsagent/bugs/fixed/` — closed bugs (state `closed`).
- One registry: `b0ttsagent/bugs/bugs.jsonl`, covering both folders.
- Markdown documents named `YYYY-MM-DD-slug.md`; the slug derives from the title.
- The registry's `filepath` is project-root-relative (e.g. `b0ttsagent/bugs/open/2025-08-18-login-crash.md`).

Registry entry schema (one JSON object per line, camelCase, matching the `sessions.jsonl` precedent):

```json
{
  "id": "stable unique identifier",
  "state": "open | in progress | closed",
  "title": "short title",
  "description": "1-3 sentence summary",
  "causes": ["one short string per suspected cause"],
  "filepath": "project-root-relative path to the markdown doc",
  "severity": "low | medium | high | critical",
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD",
  "related": ["ids of duplicates/related bugs"]
}
```

- **Append-only, latest-wins:** registry changes are written as a new line; the most recent line for an `id` is authoritative. Existing lines are never edited or rewritten.
- The agent appends the initial registry line in the same step as writing the markdown doc. State is written as `open` and the agent never changes it afterwards.
- **No scaffold or validate scripts:** the agent writes the document by hand, following a template stored in the skill's `references/`.

### Markdown document structure

- **Minimal YAML front matter:** `id`, `title`, `severity`, `state`, `created_at` — so any document is self-explanatory standalone.
- **Prose sections:** Description; Expected vs Actual; Reproduction Steps; Environment; Impact; Suspected Causes; Ruled Out & Open Questions (the last two filled when applicable).
- **Append-only history:** each investigation appends a new Suspected Causes section; earlier sections are never rewritten.

### State semantics (personal tracking, not agent workflow)

- The agent writes `state: "open"` at creation and never changes state on its own.
- State transitions belong to the owner: `in progress` = the owner is personally working on the fix (unrelated to the agent's investigation); `closed` = fixed and moved to `fixed/`.
- Closing happens either manually or via the skill's mark-fixed mode.

### Step 3 — Investigation

- **Entry points** are derived from the reproduction steps — the repro steps are the map of where to look.
- **Explorer sub-agents:** read-only sub-agents probe the codebase; count is left to agent judgment, dispatched one per suspect area. They never modify files.
- **Multiple causes:** all suspected causes are documented, not just the top one.
- **Bounded effort:** investigate to hypotheses, not to a fix. Stop at well-supported hypotheses or record the investigation as inconclusive.
- **Per cause:** confidence (`low`/`medium`/`high`), evidence citing file and line, and a "what would confirm this" note.
- **Explicitly out:** git history (blame / recently-changed files) is not used as a suspect generator.

### Step 4 — Append suspected causes

- Suspected causes are appended to the same Markdown document (new section per investigation run) and mirrored as short strings in the registry's `causes` array via a new appended registry line (with `updated_at` refreshed).

### Mark-fixed mode

- Triggered by phrasing like "I fixed X, mark it fixed": move the document from `open/` to `fixed/`, update its front matter `state` to `closed`, and append a new registry line with `state: "closed"` and the updated `filepath`.
- The owner may also do any of this manually; append-only latest-wins means both paths are safe.

### Query script (only script in the skill)

- One script in the skill's `scripts/`, modeled on `log-session`'s `query-sessions.js`: list and search the registry by state, severity, and keyword, without loading the whole file into an agent's context window. Used for the dedupe check and for owner queries.

## Testing Decisions

### What makes a good test

Only external behavior is tested, never implementation details: (1) the observable conversation (question count, extraction-first behavior, read-back) and (2) the on-disk artifacts (document placement, front matter, sections; registry line validity, schema conformance, latest-wins). Tests are run as fresh-session evaluations, not by inspecting the skill's internals.

### Test seams

- **Seam 1 — the skill invocation (primary, end-to-end):** a fresh agent session runs the skill with a realistic bug report. Verify the intake behavior and that the document appears in `b0ttsagent/bugs/open/` with correct front matter and sections, and one valid line is appended to `b0ttsagent/bugs/bugs.jsonl`.
- **Seam 2 — the registry contract (invariant):** after any run, every line parses as JSON with the agreed schema; `state` is one of the three allowed values; `filepath` resolves to an existing file; latest-wins holds per `id`. Checked with the query script plus a trivial parse check.
- **Seam 3 — the mark-fixed path:** a fresh session runs "I fixed bug X, mark it fixed"; verify the document moves to `fixed/`, front matter updates, and a new registry line with `state: "closed"` and updated `filepath` is appended.

### Prior art

- `write-a-skill-v2`'s two-instance loop: author in one session, observe a fresh runner session, feed observations back.
- `log-session`'s query-script pattern and its append-only `sessions.jsonl` ownership model.
- `agent-builder`'s parallel-subagent orchestration precedent for the explorer sub-agents.
- Three evaluation scenarios that would fail without the skill, run at Seams 1 and 3 in fresh sessions.

## Out of Scope

- Building the skill itself (SKILL.md, references, scripts) — that is a future session executing this spec.
- Fixing bugs: the skill ends at suspected causes.
- Git-based suspect generation (blame, recent changes).
- Context auto-fill of environment details.
- Scaffold and validate scripts (the doc template is a reference file; writing is by hand).
- Cross-linking bug records to session logs or planning documents.
- A web app over the registry (the registry is only shaped so one is possible later, with no migration).
- Any research under `b0ttsagent/research/bug-report-skills/` — skipped entirely.
- Feature requests and non-bug reports.

## Further Notes

- The append-only, latest-wins registry follows the established `sessions.jsonl` convention in this repo, and the query script follows `log-session`'s pattern of keeping the index out of the agent's context window.
- The registry is deliberately kept to concise fields so it stays cheap to read in full if ever needed, and trivially consumable by a future web app.
- Testing is evaluation-driven per `write-a-skill-v2`: run realistic bug reports in fresh sessions and watch what a runner actually does, including whether the skill fires at all on natural-language bug reports.
- Open micro-decisions, to be confirmed with the owner at build time (explicitly not assumed here): who drafts the bug title (agent-proposed options vs owner-provided), and how severity is proposed during intake (e.g., agent proposes from the impact answer and the read-back confirms it).
