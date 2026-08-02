# Handoff: Markdown Document-Writing Skill Creation

## Next-session purpose

Create the future Skill v2 for generating psychologically efficient, attractive personal Markdown notes and practical guides, using the completed research artifact as its evidence and design input.

The next session should focus on skill creation and validation. Do not repeat the full research unless a specific unresolved claim needs verification.

## Completed in this session

- Read the prior Markdown document-writing research handoff.
- Read the prior grilling-session JSON artifact.
- Activated and followed the Karpathy guidelines.
- Loaded the Skill v2 authoring guidance.
- Clarified that this session would be research-only.
- Conducted research across:
  - Psychology and cognitive science
  - Reading and scanning behavior
  - Cognitive load and signaling
  - Retrieval practice and active processing
  - Digital note-taking
  - Aesthetic usability
  - Public Agent Skills and writing workflows
  - VS Code Markdown features
  - Markdown linting and formatting
  - Knowledge-management systems
  - Publishing systems
- Created the detailed research document:

`b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-findings.md`

That document contains the detailed findings, source links, limitations, public-resource evaluations, adoption matrix, and open design questions. Use it as the primary research reference rather than duplicating its contents here.

## Intended future skill capability

The future skill should generate new personal Markdown notes and practical guides, especially:

- Research-derived guides, such as turning research about making good videos into a step-by-step guide for the user’s own videos
- Personal reference notes
- Quick temporary documents

Secondary cases worth supporting or testing:

- Learning and study notes
- Decision-support documents
- Reusable procedures and checklists

The primary reader is the user as a human. The quality target is not merely valid Markdown. Documents should be psychologically efficient, easy to scan and retrieve, and distinctly pretty without visual decoration harming comprehension or maintainability.

## Research conclusions to carry forward

The research strongly suggests that the future skill should:

1. Identify the document’s task: learn, decide, do, remember, find, capture, or explain.
2. Treat document lifespan as a major variable:
   - Ephemeral
   - Working
   - Reference
   - Evergreen
3. Put purpose and practical value near the top.
4. Use headings as a retrieval map.
5. Keep one meaningful question or job per section.
6. Separate action from explanation.
7. Remove redundant or nonessential information.
8. Use visual elements semantically:
   - Tables for comparisons
   - Diagrams for relationships and processes
   - Callouts for warnings, definitions, decisions, shortcuts, and limitations
9. Preserve distinctions between evidence, interpretation, recommendation, personal adaptation, and uncertainty.
10. Support multiple reading depths: glance, scan, normal reading, deep reading, and action.
11. Use active-recall features only for learning-oriented documents, not every note.
12. Transform research into personal actions instead of transcribing source material.
13. Run structural and surface-quality checks, while recognizing that linting cannot judge reader usefulness or beauty.
14. Use portable Markdown as the semantic baseline and VS Code-specific presentation selectively.

## Public resources identified

Provisional research recommendations:

- **Adopt as baseline:** VS Code built-in Markdown Preview
- **Adopt:** markdownlint
- **Adopt optionally:** Code Spell Checker
- **Adopt optionally:** Markdown All in One
- **Use selectively:** built-in Mermaid support
- **Reject:** deprecated Markdown Preview Mermaid extension
- **Adapt:** Anthropic’s document co-authoring workflow
- **Adapt:** Superpowers writing-skill and fresh-agent testing patterns
- **Evaluate separately:** Foam
- **Use as pattern reference or separate tool:** Obsidian
- **Use for publishing-heavy cases:** Quarto
- **Do not use as the core approach:** visual-art/design skills intended for canvas artifacts

Detailed source links and rationale are in:

`b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-findings.md`

## Open design decisions for the next session

These were intentionally deferred until after research.

### 1. Skill scope and mode behavior

Decide whether one skill should use internal modes for:

- Ephemeral notes
- Working documents
- Reference guides
- Evergreen guides
- Learning notes
- Procedures

Or whether the capability should eventually split into narrower skills.

The research indicates that purpose and lifespan matter, but does not require multiple separate skills.

### 2. Output ceremony

Decide when the agent should:

- Write directly
- Show a draft first
- Ask for approval
- Use an adaptive rule based on lifespan, complexity, and research depth

### 3. Evidence visibility

Decide how research-derived documents should expose sources:

- Minimal source visibility
- Full claim-level traceability
- Layered sources: practical main content plus detailed sources/appendix

### 4. Portable versus VS Code-specific Markdown

Decide which features belong in:

- The portable semantic core
- An optional VS Code polish layer

Potential candidates include custom CSS, callout syntax, Mermaid, math, and renderer-specific extensions.

### 5. Connected knowledge base

Standalone readability should remain the baseline. Decide when to add:

- Related-note links
- Indexes
- Backlinks
- Tags
- Knowledge-base metadata

### 6. Validation workflow

Decide how the skill’s self-check should combine:

- Purpose and audience check
- Scanability check
- Redundancy check
- Actionability check
- Evidence/uncertainty check
- Visual restraint check
- Optional markdownlint or other external tooling

## Suggested next-session workflow

1. Read the research artifact in full:
   `b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-findings.md`
2. Read the Skill v2 authoring guidance:
   `.agents/skills/write-a-skill-v2/SKILL.md`
3. Read the Karpathy guidelines:
   `.agents/skills/karpathy-guidelines/SKILL.md`
4. Inspect relevant existing local skills only as implementation context, especially:
   - `.agents/skills/create-nav-guide/SKILL.md`
   - `.agents/skills/create-context-doc/SKILL.md`
   - `.agents/skills/create-planning-docs/SKILL.md`
   - `.agents/skills/create-execution-plan/SKILL.md`
   - `.agents/skills/mermaid-diagrams/SKILL.md`
5. Design the trigger surface and negative boundaries.
6. Decide whether the skill needs references, examples, scripts, or only a concise `SKILL.md`.
7. Author the skill using progressive disclosure and a deliberately narrow job.
8. Add at least three evaluations based on the primary use cases.
9. Validate the skill structure, frontmatter, description, paths, and line count.
10. Test the skill in fresh contexts if the harness supports it.

## Research limitations

- Search-provider API limitations prevented a fully exhaustive public Agent Skills landscape review.
- Several findings came from applied web usability research rather than direct personal-Markdown experiments.
- Public tool status and marketplace capabilities can change; re-check current status before making installation or dependency decisions.
- The research does not itself lock the future skill architecture.

## Relevant files

- Research artifact:
  `b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-findings.md`
- This handoff:
  `b0ttsagent/handoffs/08-01-2026/markdown-document-writing-skill-creation-handoff.md`
- Prior research-session handoff:
  `b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-handoff.md`
- Prior grill-session transcript artifact:
  `b0ttsagent/handoffs/08-01-2026/grill-session-md-document-writing-skills-research.json`
- Skill-authoring guidance:
  `.agents/skills/write-a-skill-v2/SKILL.md`
- Behavioral guidelines:
  `.agents/skills/karpathy-guidelines/SKILL.md`
- Project rules:
  `AGENTS.md`

## Explicit next-session boundary

The next session is for **skill creation**, not another broad research session. Use the research artifact as the source of truth for the initial design, then validate and refine the skill against the user’s actual document use cases.
