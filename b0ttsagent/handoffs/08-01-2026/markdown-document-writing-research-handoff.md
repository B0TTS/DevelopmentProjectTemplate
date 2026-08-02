# Handoff: Markdown Document-Writing Research

## Next-session purpose

Conduct a research session that will provide the foundation for a future Agent Skill that generates effective personal Markdown notes and practical guides.

The future skill is intended for documents such as:

- Research-derived personal guides—for example, turning research about making good videos into a step-by-step guide for the user's own videos.
- Personal notes.
- Quick temporary documents.

No research or skill implementation was performed during the grilling session.

## Locked direction

- **Primary capability:** generate new personal Markdown notes and guides.
- **Existing-document review:** out of scope for version one, apart from any lightweight self-check performed on a document the skill just generated.
- **Reader:** primarily the user as a human reader.
- **Core quality goal:** documents should be psychologically efficient and distinctly pretty—not merely technically valid Markdown.
- **Evidence priority:** evidence-based findings govern the core rules. Popular practices may be included as optional patterns, but should not override stronger evidence without a clear usability reason.
- **Primary rendering environment:** VS Code Markdown Preview.
- **Deferred:** the precise boundary between portable Markdown and VS Code-specific presentation features.
- **Deferred:** output ceremony, filename conventions, destination selection, and whether substantial documents require draft approval before writing. Decide these after research rather than guessing now.

## Research scope

Evaluate all four categories of existing skills, tools, and reusable patterns:

1. **Research-to-guide skills** — turn findings, sources, formulas, or frameworks into actionable personal guides.
2. **Markdown quality and presentation skills** — improve hierarchy, scanability, visual polish, and reader comprehension.
3. **Knowledge-management skills** — create notes, indexes, quick references, summaries, or linked personal documentation.
4. **Markdown tooling skills** — validate, lint, render, convert, or enhance Markdown documents.

Filter candidates through the user's actual use cases: personal notes, practical guides, research-derived frameworks, and quick temporary documents.

## Baseline research deliverable

The next session should aim to produce a four-part research package:

1. **Evidence base** — findings about comprehension, memory, information retrieval, visual hierarchy, aesthetics, and cognitive load, with source quality clearly separated.
2. **Practical design principles** — concise rules for creating psychologically efficient and pretty Markdown notes and guides.
3. **Worked examples** — before/after transformations or model document patterns, ideally using a research-derived video guide as a realistic example.
4. **Adoption candidates** — existing skills and tools from all four categories, with rationale, overlap analysis, and adopt/adapt/reject recommendations.

This is a baseline, not a rigid schema. Extend it only when the evidence reveals a necessary additional section.

## Candidate evaluation hypothesis

Start with this adoption rubric, but refine, replace, or simplify it after examining real candidates:

- Reader value: comprehension, memory, retrieval, scanning, or visual appeal.
- Fit: usefulness for personal notes, practical guides, research synthesis, or temporary documents.
- Evidence quality: credible research or demonstrated practice.
- Distinct value: whether it fills a gap in the current stack.
- Operational cost: ceremony, maintenance, dependencies, and context burden.
- Adoption path: ease of installation, adaptation, or integration.

## Important design questions for research

The research should answer—not assume—questions such as:

- Which document structures improve comprehension and retrieval for personal reference material?
- Which visual-design choices make Markdown prettier while supporting, rather than harming, cognition?
- Which VS Code Markdown Preview features are useful and stable enough to adopt?
- Which elements should be portable Markdown, and which should be optional VS Code-specific polish?
- When should a generated document be written directly versus shown for approval first?
- How should quick temporary documents differ from substantial research-backed guides?
- Which existing skills overlap with the planned skill, and which add genuinely distinct value?

## Relevant project files

- **Session log with the complete transcript and approved summary:** `b0ttsagent/handoffs/08-01-2026/grill-session-md-document-writing-skills-research.json`
- **Skill-authoring guidance:** `.agents/skills/write-a-skill-v2/SKILL.md`
- **Behavioral guidelines requested for authoring:** `.agents/skills/karpathy-guidelines/SKILL.md`
- **Existing Markdown/nav-guide creator:** `.agents/skills/create-nav-guide/SKILL.md`
- **Existing context-document creator:** `.agents/skills/create-context-doc/SKILL.md`
- **Existing planning-document skills:** `.agents/skills/create-planning-docs/SKILL.md` and `.agents/skills/create-execution-plan/SKILL.md`
- **Existing diagram skill, relevant when evaluating Markdown presentation patterns:** `.agents/skills/mermaid-diagrams/SKILL.md`
- **Project rules:** `AGENTS.md`

## Suggested next-session workflow

1. Read the session log and the relevant existing skills above.
2. Define the research questions and source-quality standards before searching.
3. Research the psychology and evidence behind effective human-readable documents.
4. Research current Markdown/document-creation skills and tools across all four categories.
5. Compare findings against the existing stack to identify overlap and gaps.
6. Produce the four-part research package, including concrete examples and adoption recommendations.
7. Use the findings to design the future skill; do not implement it until the research and design decisions are complete.
