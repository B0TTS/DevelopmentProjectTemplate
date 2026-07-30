# Handoff: Mermaid Diagram Skill — Grill Decisions + Research Complete

**Date:** 07-18-2026
**Next session goal:** Write the mermaid skill (name TBD, e.g. `mermaid-diagrams`) into `.agents/skills/`.

---

## What was accomplished

User wants a skill for creating mermaid diagrams inside markdown docs, DAG-focused. Two phases completed:

1. **Grill session (partial)** — root decisions locked, some questions deliberately deferred until after research. One deferred question remains unanswered (see Open Decisions).
2. **Deep research** — full synthesis below. This is the crown jewel; it lives only in this handoff. Do NOT re-research unless something feels stale.

---

## Locked decisions

- **Trigger scope: Hybrid.** Fires on explicit diagram requests AND proactively when the agent is writing markdown docs (nav guides, planning docs, ADRs) and judges a diagram would help. Skill must include a "when to diagram / when not to" judgment section with explicit restraint guidance so it doesn't spam diagrams into every doc.
- **Primary use case: DAGs.** Dependency graphs, execution waves, system maps for the user's parallel-agent game-dev planning docs.
- **Coverage lineup (evidence-based, confirmed by user):**
  - **Deep dive:** `flowchart` (the DAG engine; research confirms it's the flexible default for ~90% of dev docs)
  - **Core:** `sequenceDiagram`, `stateDiagram-v2`, `gantt`, `gitGraph`, `mindmap`
  - **Lazy reference (one REFERENCE.md, condensed syntax):** class, ER, timeline, journey, quadrant, pie, C4, architecture, block, kanban, sankey, xychart, radar, treemap, packet
  - ER/class were hard cuts — matter in game dev but structurally simple, few gotchas, reference file suffices.

## Open decisions (ask user first next session, with recommendations)

1. **Hard rules vs judgment guidelines** — My rec: **rules with escape hatch**. Hard defaults ("max 15 nodes, always quote labels, subgraphs when >6 nodes") followed as checklist; agent may deviate only by stating why in a `%%` comment above the diagram. Matches AGENTS.md anti-rationalization pattern.
2. **Validation tooling** — Include a script wrapping `mmdlint` (headless, no browser, explicitly "ideal for agent usage": https://github.com/sysid/mmdlint)? `mermaid-cli` (mmdc) needs Puppeteer — too heavy. Alternative: document the parse-error feedback loop (GenAIScript pattern: `mermaid.parse()` → feed error back → regenerate) as agent behavior without tooling. My rec: document the feedback loop; add mmdlint script only if user wants deterministic validation.
3. **Target renderer confirmation** — assume GitHub + VS Code 1.121+ preview (user's docs live in markdown, viewed on GitHub/editor). Confirm; this justifies the "GitHub-safe dialect" default.
4. **Examples source** — mine examples from user's real docs (nav guides/plans) vs. synthetic examples. My rec: synthetic but shaped like his use cases (wave DAGs, gitGraph worktrees, game state machine).

---

## Research synthesis

### Renderer landscape (drives the "GitHub-safe dialect" rule)

| Surface | Mermaid version | ELK layout | Notes |
|---|---|---|---|
| GitHub (README/issues/PRs/wiki) | 11.4.1 | ❌ No | Forces its own theme |
| Obsidian | 11.4.1 | ❌ No | |
| VS Code 1.121+ preview/notebooks/chat | built-in | varies | Renders natively now |
| Notion | 11.3.0 | ❌ No | |

→ Default to dagre layout only; no ELK directives (silently no-op on GitHub); note `click` links work on GitHub.

### Complexity budgets (sources converge)

- ≤12 nodes for reliable LLM generation (prompt-engineering guides)
- 15–20 nodes = readability ceiling (multiple best-practices sources)
- 50 nodes = "complex" (mermaid-sonar analyzer)
- ~100 edges = O(n²) layout blowup (Mermaid Chart's own engineering blog)
- **Candidate rule: ≤15 nodes hard default; past that, split into overview + zoomed detail diagrams.**

### Top LLM failure modes (highest-value skill content)

1. Nested quotes in labels → parse error ("Expecting SQE, got STR")
2. Backticks in node labels → **silent** failure on GitHub, renders nothing (documented: qodo-ai/pr-agent #2211)
3. Unquoted special chars `()&:` in labels → parse error → **rule: always quote labels**
4. Lowercase `end` as node ID → breaks flowchart (capitalize: `End`/`END`)
5. `A---oB` / `A---xB` → accidentally creates circle/cross edge (space or capitalize)
6. Quotes in edge labels (`-->|"text"|`) → parse errors; keep edge labels plain
7. Styling subgraphs by display name → parse error; use `subgraph ID["Display Name"]` + reference ID in style
8. `<br/>` labels with decimals/special chars → wrap entire label in double quotes
9. Error recovery: feed parser error message back to the LLM — models self-correct well with specific errors

### Layout control for DAGs (dagre-only, works everywhere)

- **Edge declaration order drives layout** — reorder edges to untangle crossings
- Invisible links `A ~~~ B` force alignment/proximity
- Invisible subgraphs cluster nodes without visible boxes (`classDef invisible fill:#0000,stroke:#0000`, blank title `[" "]`)
- Extra dashes force rank spacing: `---->` spans more ranks (dotted: `-..->`, thick: `===>`)
- **Subgraph `direction` is IGNORED if any node links outside the subgraph** (huge gotcha, officially documented limitation)
- Intermediate "router" nodes fix width blowup from fan-out (A→Router→B,C,D,E)
- `maxWidth` flowchart config forces reflow for narrow contexts
- Direction choice: TD for hierarchies/decision trees, LR for sequential pipelines; wide+shallow → TD, deep+narrow → LR

### Styling as information

- `classDef` + `class` — reusable styles; **inheritance works**: `class D storage,degraded` merges, later classes win
- `:::className` shorthand on node declaration
- `linkStyle 0,2,4 stroke:#2563eb,stroke-width:2.5px` — 0-indexed by edge declaration order (brittle but the only way pre-v11.10); use for happy-path vs error-path visual hierarchy
- `style <id> ...` for one-off emphasis node only — exception styling loses meaning if overused
- v11.10+: edge IDs `e1@-->` allow named per-edge styling/curves (prefer over linkStyle when available)
- `theme: base` is REQUIRED before `themeVariables` take effect (otherwise silently no-op)
- YAML frontmatter config (`---\nconfig:\n  theme: forest\n---`) has replaced `%%{init}%%` in v11
- Palette discipline: 3–4 colors max, each with assigned meaning (green=success, red=error/critical, blue=info, gray=inactive)
- Escape commas in style values as `\,` (e.g. stroke-dasharray)

### v11 features worth covering

- 30+ new node shapes: `A@{ shape: cyl, label: "DB" }` (aliases: `db`, `decision`/`diam`, `stadium`/`pill`, `docs`, `st-rect`, etc.)
- `look: handDrawn` config
- Markdown strings `` "`text`" `` with auto-wrap (but see backtick silent-failure risk on older renderers — GitHub 11.4.1 supports, test first)
- New diagram types: kanban, architecture, radar, treemap, packet, sankey, xychart, block

### Existing skill reference (differentiate from this)

`mermaid-gen` in github.com/mattnigh/skills_collection — heavy on error catalog + templates + quality-gate checklists. Good structural reference. We differentiate on: DAG/layout-control depth, renderer-aware rules (GitHub-safe dialect), and the when-to-diagram judgment section.

### Key sources

- Official flowchart syntax: https://mermaid.js.org/syntax/flowchart.html
- 10 Mermaid Tricks (classDef inheritance, linkStyle, zones): https://www.beauty-diagram.com/blog/10-mermaid-tricks
- Korny's Mermaid revisited (invisible elements, frontmatter, renderer table): https://blog.korny.info/2025/03/14/mermaid-js-revisited
- Layout/sizing best practices: https://www.mermaidcreator.com/blog/mermaid-flowchart-sizing-layout-best-practices
- General best practices: https://simplemermaid.com/guides/best-practices.html
- LLM prompt engineering for mermaid: https://mermaid2img.com/blog/mermaid-prompt-engineering-for-llms
- Mermaid as agent output format (surface-gating, failure modes): https://agentpatterns.ai/instructions/mermaid-as-agent-output-format/
- mmdlint (headless validator): https://github.com/sysid/mmdlint
- mermaid.parse() API: https://www.mintlify.com/mermaid-js/mermaid/api/methods/parse

---

## Suggested skills for next session

1. **`grill-me`** (briefly) — resolve the 4 open decisions above first
2. **`write-a-skill`** — main workflow for authoring the skill files

## Key paths

- Skills go in: `C:\Users\Jonah\DevelopmentTemplate\.agents\skills\<skill-name>\SKILL.md`
- Skill authoring conventions: `C:\Users\Jonah\DevelopmentTemplate\.agents\skills\write-a-skill\SKILL.md`
  - SKILL.md under ~100 lines, description with "Use when..." triggers, split REFERENCE.md/EXAMPLES.md when content is large, scripts/ only for deterministic ops
- Proposed structure: `SKILL.md` (router + judgment + rules checklist) + `REFERENCE.md` (lazy diagram types) + `EXAMPLES.md` (templates per core type) + optional `scripts/validate` if user approves mmdlint
