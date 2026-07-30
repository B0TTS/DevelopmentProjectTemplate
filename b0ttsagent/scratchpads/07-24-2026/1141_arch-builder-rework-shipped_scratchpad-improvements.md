# Scratchpad — Branch 3: Improve skills used
**Session:** arch-builder-rework-shipped
**Date:** 07-24-2026 11:41

Skills invoked/consulted this session (close/closev2 excluded per rules): `grill-me`, `mermaid-diagrams`, `systems-architecture-builder`, `write-a-skill` (applicability check).

## Categories identified
- grill-me-pacing-friction
- skill-scope-gaps
- rule-clarifications

## Extraction

### grill-me-pacing-friction
- grill-me's fixed "ask the questions one at a time" rule caused visible pacing friction: after two rounds the user interjected "lets speed this up lets take your recc for ones you think are hard. Just leave like visual design UI/UX questions for me." Context: Q6 and Q6.1 were asked individually with recommendations; both were approved instantly ("your recc works"), showing the one-at-a-time cadence was pure overhead for this user on mechanical branches. Reason: the skill has no delegation/pacing concept — it can't auto-accept its own recommendations on user-defined categories, can't batch related sub-decisions, and can't take a mid-session throttle instruction. Adding a "delegation & pacing" clause (user may designate decision categories to auto-resolve via recommendation, and may request batching; model announces auto-locks in a compact list and reserves questions for the delegated categories) directly fixes the observed friction while preserving the relentless-interview core for decisions the user actually wants to make.

### skill-scope-gaps
- write-a-skill's description and process cover only creating NEW skills ("Create new agent skills… Use when user wants to create, write, or build a new skill"). This session's primary work was restructuring/rewriting an existing skill's bundled template and editing two existing SKILL.md files — a gray zone. The handoff even suggested "write-a-skill — if structural changes exceed inline edits," but on reading, the skill's gather-requirements interview and review-checklist are creation-shaped. Context: I read write-a-skill fully to check applicability, concluded "not governing here," and proceeded with judgment. Reason: skill-rework sessions will recur (the whole arc was a skill rework); the skill should either explicitly cover reworks (structure/conventions apply to edits of existing skills too — e.g. the ≤100-line SKILL.md guidance, progressive disclosure, description requirements) or explicitly disclaim them so future sessions don't burn a read checking.

### rule-clarifications
- mermaid-diagrams' Restraint Rule says "Maintain a strict limit of max 1 diagram per document unless explicit split is required." The systems-architecture-builder template now canonically ships 2+ diagrams per doc (overview chips + per-wave details). "Unless explicit split is required" arguably covers it, but an agent reading narrowly could flag the arch template's own pattern as a violation. Context: noticed while editing mermaid-diagrams SKILL.md checklist this session; no failure occurred, it's a latent ambiguity. Reason: one clarifying clause ("multi-diagram split patterns canonized by another skill's template count as explicit splits") removes the tension between two skills that are now formally integrated.

## Gleaning Pass

### grill-me-pacing-friction
- Re-checked the full grill arc (Q6 presentation → user confirm → evidence grep → Q6.1 presentation → user throttle message → batched final question → approval): the single pacing item is captured with its batching and delegation facets. The "explore the codebase instead of asking" rule worked well (classDef grep grounded Q6.1) — a success, not friction; nothing to add.

### skill-scope-gaps
- Re-checked every skill file read this session for other scope/coverage gaps: grill-me's scope is fine (only the pacing gap above); mermaid-diagrams' scope was extended as planned (no residual gap beyond the clarification item); systems-architecture-builder's description still accurately matches its behavior post-edit. No additional scope gaps qualify.

### rule-clarifications
- Re-checked both edited SKILL.md files and the template for other cross-skill tensions: the builder's new routing rule vs mermaid-diagrams trigger #3/#4 are aligned (active + passive); the builder's "edge-integrity check" vs the template's HTML-comment version agree (template adds "surface it to the user, don't silently draw it" — consistent); wave-table-authority appears in both consistently. Only the restraint-rule tension qualifies.

## Triple-check note
Not activated — gleaning confirmed non-empty categories with justifications.
