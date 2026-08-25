# WAVE REPORT — Prompt-writing / prompt-refinement agent skills research

**Wave lead:** b0tts-lead-researcher | **Date:** 2026-08-18 | **Researchers:** A (Anthropic first-party), B (community marketplaces), C (cross-platform)

## Per-researcher status

| Researcher | Status | Output | QA |
|---|---|---|---|
| A — Anthropic / Claude Code | done | `researcher-a.md` (162 lines) | PASS — all 8 fields per candidate, honest "no official skill" verdict |
| B — community marketplaces | done | `researcher-b.md` (223 lines, 39 URLs) | PASS — tiers, all fields, sources read |
| C — cross-platform | done | `researcher-c.md` (269 lines, 16 candidates) | PASS — all fields, UNKNOWNs flagged, no invented claims |

No retries needed. No FAIL-UNKNOWN.

## Reconciliation of overlaps

- `severity1/claude-code-prompt-improver`: found by A (lead) + C (full candidate) — merged.
- `christabone/claude-prompt-improvement`: found by A (lead) + C (candidate) — merged.
- `prompt-engineer` name collision: B's is Sourabhj00 (interactive); C's is Jeffallan (11k★, NON-interactive). Kept as two rows.
- `prompt-optimizer` name collision: B's github/awesome-copilot (NON-interactive) vs C's affaan-m/ECC (PARTIAL). Kept as two rows.
- `boost-prompt`: B only (via skillmd.com). C did not duplicate.
- `refine-prompt` (mcpmarket) / `refine-prompts` (skills.rest): leads noted by A and C but never fetched → UNVERIFIED, excluded from ranking.

## Ranked comparison table (interactive Q&A is criterion #1)

| Rank | Name | Platform | Interactive Q&A? | Install | Pros | Cons |
|---|---|---|---|---|---|---|
| 1 | `boost-prompt` (github/awesome-copilot) | VS Code (Claude Code via Joyride) | **YES** — iterative interrogation via `joyride_request_human_input` | Install Joyride VS Code extension + drop-in skill | Exact target workflow; copies final markdown prompt to **clipboard** | Requires Joyride/VS Code; thin skill body |
| 2 | `prompt-architect` (ckelsoe) | Claude Code, Codex, Gemini CLI, Cursor, ChatGPT | **YES** — 3–5-question batches, iterative; FATA interview framework | `npx prompt-architect` (MIT, 277★) | Most complete/portable; 31 frameworks, 5-dimension scoring | Install on opencode specifically UNKNOWN |
| 3 | `clarify` (owainlewis/agent-skills) | Claude Code (AskUserQuestion) | **YES** — one question at a time with recommended answers | `npx skills add owainlewis/agent-skills --skill clarify` (42★, active) | Closest structural match; emits self-contained `Final prompt:` block | Chat-only output; Claude Code-specific Q&A tool |
| 4 | `prompt-improver` (ndpvt-web) | Claude Code | **YES** — unbounded AskUserQuestion loop | Claude Code skill (85★) | Genuine interview loop; Aristotelian output polish | Chat-only output |
| 5 | `prompt-engineer` (Sourabhj00) | Claude Code | **YES** — mandatory "Context Gap Questions" step, blocks until answered | Claude Code skill | 6-step process → XML Master Prompt + per-change reasoning | 1★, unproven |
| 6 | `promptify` (ravnhq/ai-toolkit) | Claude Code | **YES** — AskUserQuestion + save-to-file option | Claude Code skill | Only candidate with file-save output | Repo **archived** |
| 7 | `prompt-improver` (severity1) | Claude Code (hook) | YES — 1–6 research-grounded questions | Claude Code skill | Auto-triggers on vague prompts; well-engineered | **Executes the task** instead of returning a polished prompt — wrong deliverable |
| 8 | `prompt-optimizer` (affaan-m/ECC) | Claude Code | PARTIAL — ≤3 conditional questions | Claude Code skill | Solid prompting theory | Star count (240k) flagged unreliable |
| 9 | `prompt-refinement` (v1truv1us) | Claude Code | PARTIAL — ≤1 blocking question | Claude Code skill | Minimal friction | Too little questioning for the use case |
| 10 | Various: `prompt-optimizer` (awesome-copilot), `prompt-refiner` (Notysoty), `prompt-improvement` (christabone/melodic), `prompt-engineer` (Jeffallan 11k★) | Claude Code / Codex | **NO** | per-repo | Solid one-shot rewriters | No interview — rank lower by definition |

**First-party (Anthropic):** NO official skill matches. Closest interactive patterns: `skill-creator` (interviews, but authors SKILL.md), `doc-coauthoring` (Q&A, but for docs). Console "prompt improver" refines prompts but has NO Q&A and isn't an activatable skill.

**Notable adjacent (not prompt refinement):** `interview-me`, `first-ask`, `grill`, `ask-questions-if-underspecified`, obra/superpowers `brainstorming` — interactive interviews, wrong output. Standalone workflows (non-skill): Interrogatory LLM (Martin Fowler / Harper Reed) — the canonical "one question at a time" technique.

## Recommendation (top 3 fits for "refine an existing prompt via Q&A")

1. **`prompt-architect` (ckelsoe)** — best overall: interactive, mature (277★, MIT), cross-platform, and the most complete framework coverage. Recommend first.
2. **`boost-prompt`** — best match for the exact workflow *including clipboard output*, if the user is OK with a VS Code + Joyride environment.
3. **`clarify` (owainlewis)** — cleanest minimal interview loop (one question at a time with recommendations); best if the user wants a simple, readable skill to adapt for their own harness.

**Key gap:** output delivery is chat-only in nearly all candidates (clipboard: boost-prompt only; file: promptify only). If the user needs clipboard/file output outside VS Code, expect to wrap the chosen skill with a small output handler.

## Anomalies / open items

- mcpmarket `refine-prompt` + skills.rest `refine-prompts` remain UNVERIFIED (leads noted, never fetched).
- No opencode-native interactive candidate exists; opencode has no official skills registry (issue anomalyco/opencode#8386).
- awesomeskill.ai + chat2anyllm per-skill crawls were not exhaustive (index quality varies).
- Researcher A notes anthropics/skills is actively maintained (pushed 2026-08-18); its skill list is current.
