# Handoff — Creative-Brainstorm Skill Design (Grill Session)

**Date:** 2026-07-12
**Session type:** Grill (via `grill-me` skill) → locked design spec
**Next phase:** Research — **pending user go-ahead (not started)**

## TL;DR

Grilled the design of a new **"creative-brainstorm"** skill — a domain-agnostic creative ideation skill: given a stated goal, generate multiple creative candidate options, ranked, with explanations and transparent reasoning. The full design spec is now locked. The next step is the **research phase** the user flagged at the start of the session: search for existing open-source "creative ideation / brainstorm" agent skills, measure each against the locked spec, and build new (via `write-a-skill`) only if nothing fits.

> **No research was conducted this session** — the user explicitly gated it: *"please stop before conducting deep research… refrain from researching once we have reached a shared understanding and you consider this session complete."* Do not begin research until the user says go.

## Motivating use case (the concrete test case)

Game progression systems — a short-term retention loop with long-term scalability, quest-like but more creative options. This drove the grill but is **not** the skill's scope. The skill itself must be **domain-agnostic and universally adoptable** (game systems, UI design, product design, anything).

## What was accomplished

- Ran a `grill-me` session to stress-test the skill's design intent *before* researching existing options (per the user's flow: grill → research → build).
- Resolved every load-bearing design branch one at a time. The locked spec below is the artifact of that session — it exists nowhere else on disk yet.

## Locked design spec

### Purpose & scope
- Hybrid: divergent solution ideation + product/feature direction. Given a stated goal, generate multiple creative candidate options.
- Domain-agnostic and universally adoptable (game systems, UI, product, anything).
- Sits upstream of the planning skills in this repo: `creative-brainstorm` → user picks → `create-planning-docs` → `grill-me` / `grill-with-docs` → `create-execution-plan`.

### Design philosophy (load-bearing)
- **Principles, not procedures** — model on `karpathy-guidelines`' DNA; state qualities/intent, don't prescribe a fixed method. The "how" is left to the model of the day so the skill scales as AI intelligence improves.
- **Recommend, don't direct** — permissive tone ("consider…", "you might…"), not imperative ("you must…", "never…").
- **Separate stable intent from volatile technique** — intent (diverse, novel, well-reasoned, ranked, transparent) is stable; techniques are the model's to choose.
- **Lean on requirements that get *more* valuable as models get smarter** — especially the reasoning/transparency layer.
- **Bounds, not counts** — ceilings and qualities, not fixed steps or quotas.

### Grounding
- **In-chat by default; no auto-crawl of codebase/files.** ⚠️ *Surfaced as an assumption during the grill; user did not explicitly confirm it — reconfirm at the start of the next session.*
- User supplies project context if they want it factored in; otherwise blue-sky.

### Output contract (4 layers, in order)
1. **Framing** (2-3 lines) — restate goal + the shape being optimized for.
2. **Reasoning** — surface honestly: what was deliberately varied, what was considered and rejected and why, what trade-off each option optimizes. **No required vocabulary.**
3. **Ranked options** — best-fit first; each with name, 1-2-sentence concept, why it fits, strengths, stretches/risks (light reality-check). Defend the ranking.
4. **Next move** (1 line) — invite the user to pick a direction to deepen, setting up iterative rounds.

### Quantity
- Quality over quantity; aim ~8-10, hard max 12; exceed 12 only if the user asks. Stated as a maximum, not a mandate.

### Qualities the output must clear
- Genuine diversity across independent dimensions (options shouldn't be variants of one idea).
- Novelty preferred over safe variants.
- Defended ranking.
- Light reality-check.
- Reasoning surfaced (rejected options + why).

### Illustrative moves (available resource, opportunistic — never forced)
- Non-exhaustive list of *kinds of moves* that satisfy the qualities: vary a dimension deliberately · import a mechanism from another domain · invert the goal · remove a constraint then pull back · etc.
- The model decides per-run whether to draw on them. **Never forced** (user's final refinement: "Sometimes it's unnecessary. Let the model decide when to include illustrative moves and when not to.")

## Open decisions

**Write-time loose ends (decide when building, not research inputs):**
- Interaction model: one-shot vs iterative rounds (the "next move" layer implies iterative — confirm at build time).
- Persistence: conversational default vs optional file dump.
- Skill name (working name: `creative-brainstorm`).
- Done-state / handoff boundary to the planning skills.

**To reconfirm at start of next session:**
- The **in-chat-no-auto-crawl grounding default** (flagged above).

## Suggested skills for the next session

- **`write-a-skill`** — use to build the skill if research finds nothing fitting. Its SKILL.md defines the structure/conventions (SKILL.md < 100 lines, description requirements, when to split files, review checklist). Follow it exactly if building.
- **`grill-me`** or **`grill-with-docs`** — available if the spec needs re-stress-testing against research findings before building.
- **`create-planning-docs`** — only if the user decides to formalize the spec into CONTEXT/PLAN docs before building (not currently requested; the flow is research → build).

*Note: the research phase itself uses the `web_search_exa` / `web_fetch_exa` tools, not a skill.*

## Key files & paths

- Skills root: `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\`
- `write-a-skill` (build conventions): `.agents/skills/write-a-skill/SKILL.md`
- `karpathy-guidelines` (the DNA to model the new skill on): `.agents/skills/karpathy-guidelines/SKILL.md`
- `grill-me` (used this session): `.agents/skills/grill-me/SKILL.md`
- Existing behavioral skills to differentiate the new one from: `grill-me`, `grill-with-docs`, `explain-it-v2`, `karpathy-guidelines`, `create-planning-docs`, `create-context-doc`, `create-execution-plan`.
- Prior similar handoff (skill-design-via-grill precedent): `b0ttsagent/handoffs/06-19-2026/docs-mcp-skill-design-grill.md` — useful to see how a comparable skill-design effort concluded.
- AGENTS.md (project rules — skill-first execution, no SSH to VPS): `AGENTS.md`

## Next session's first move

1. Reconfirm the **in-chat-no-auto-crawl grounding** assumption with the user.
2. On user go-ahead, run the **research phase**: `web_search_exa` for existing open-source "creative ideation / brainstorm" agent skills (look for Claude Code / Cursor / Copilot agent skills, prompt libraries, and general ideation frameworks); `web_fetch_exa` to read the promising ones.
3. Measure each find against the locked spec above. Recommend: adopt an existing one if it fits the philosophy + contract, else build new via `write-a-skill`.
4. If building: resolve the write-time loose ends (interaction model, persistence, name, done-state) against the spec.
