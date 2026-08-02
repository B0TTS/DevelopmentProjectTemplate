# Markdown Document-Writing Research Findings

## Research status

This document records the research completed for a future Agent Skill that generates effective personal Markdown notes and practical guides. It is a research artifact, not a final skill specification.

No skill was implemented or modified during this session.

## Research scope

The research covered two co-equal tracks:

1. **Human-reader research** — comprehension, scanning, memory, retrieval, cognitive load, visual signaling, and aesthetic usability.
2. **Public ecosystem research** — public Agent Skills, writing workflows, Markdown tooling, VS Code features, knowledge-management systems, and publishing tools.

The intended use cases were:

- Research-derived practical guides
- Personal reference notes
- Quick temporary documents

Secondary cases considered:

- Learning and study notes
- Decision-support documents
- Reusable procedures and checklists

Document lifespan was treated as a major dimension:

- Ephemeral
- Working
- Reference
- Evergreen

The primary rendering environment is VS Code Markdown Preview. Public resources were considered whether free, open source, commercial, active, or inactive, with their status and limitations distinguished.

## Important research limitation

Several configured web-search providers were unavailable because API keys were not configured. The research therefore relied heavily on directly fetched official documentation, public repositories, publisher metadata, PubMed records, Crossref records, and accessible applied-research sources. The public Agent Skills search was narrower than originally intended; the findings below should not be read as proof that no other relevant public skills exist.

---

# 1. Evidence model

The evidence was interpreted using four tiers.

## Tier 1 — Strong evidence

- Systematic reviews
- Meta-analyses
- Broad evidence reviews
- Well-designed experimental studies
- Established cognitive theories where relevant

## Tier 2 — Supporting evidence

- Individual peer-reviewed studies
- Reputable academic or institutional sources
- Publisher or PubMed abstracts

## Tier 3 — Applied practice

- Usability research
- Technical-writing guidance
- Information-architecture practice
- Mature tool documentation
- Public workflow and skill implementations

## Tier 4 — Popular practice

- Community conventions
- Frequently used Markdown patterns
- Tool-specific habits without direct evidence of reader benefit

The future skill should not treat all four tiers as equally authoritative. Stronger evidence should govern core principles; lower-tier practices may still be adopted when they offer clear usability value and do not introduce unnecessary ceremony or visual clutter.

---

# 2. Human-reader findings

## 2.1 Readers scan before they commit to deep reading

### Evidence tier

Tier 3: applied empirical usability research.

Nielsen Norman Group reports that users commonly scan new web pages rather than reading every word. Their research and guidance emphasize:

- Meaningful subheadings
- Highlighted keywords
- Bulleted lists
- One primary idea per paragraph
- An inverted-pyramid structure
- Concise wording
- Objective language

Their comparison of alternative versions of the same content reported better measured usability for concise and scannable presentations than for promotional prose. Their combined concise, scannable, and objective version performed best in the reported task measures.

Sources:

- [How Users Read on the Web — Nielsen Norman Group](https://www.nngroup.com/articles/how-users-read-on-the-web/)
- [F-Shaped Pattern of Reading on the Web — Nielsen Norman Group](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)

### What this means for personal Markdown

A document should reveal its purpose and practical value before requiring sustained reading. This is relevant to guides, reference notes, decision documents, and procedures.

A useful opening pattern is:

```markdown
# Clear document title

> One-sentence purpose or bottom line.

## What to do

Immediate recommendation or first action.

## Key points

- Most important point
- Second important point
- Important limitation

## Details

Explanations, examples, and supporting material.
```

This is not a universal template. A temporary scratchpad may need only a title and a short list. The finding is that important information should not be hidden behind a wall of prose when the reader is likely looking for a quick answer.

### Limitations

The cited research concerns web pages and information-seeking behavior, not personal Markdown files specifically. The transfer is reasonable because both involve visual scanning and retrieval, but the evidence should not be overstated as a direct Markdown experiment.

---

## 2.2 Headings are retrieval aids, not decoration

### Evidence tier

Tier 3: applied eye-tracking and information-architecture research.

The F-pattern article describes several scanning patterns, including:

- **F-shaped scanning** — attention concentrated near the top and left side
- **Layer-cake scanning** — attention moving across headings and subheadings
- **Spotted scanning** — searching for distinctive words, numbers, or links
- **Commitment scanning** — reading nearly everything when motivation is high

The article argues that strong formatting and information cues can reduce arbitrary scanning and direct readers toward meaningful content.

### Practical implications

Headings should communicate what a section contains.

Prefer:

```markdown
## Choose the recording format
## When this framework fails
## Three steps for the opening
## Recommended default
```

Over vague headings such as:

```markdown
## Thoughts
## More information
## Important
## Miscellaneous
```

The first words of a heading matter because readers may see only a small portion of it while scanning. Headings should therefore begin with the information-bearing phrase.

### Operational rule suggested by the evidence

Ask of every heading:

> If I saw only this heading in an outline or search result, would I know what I would find there?

VS Code makes this particularly relevant because its Outline view and heading navigation expose the heading hierarchy directly.

Source:

- [F-Shaped Pattern of Reading on the Web — Nielsen Norman Group](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)

---

## 2.3 Concision and objectivity reduce reader work

### Evidence tier

Tier 3: applied usability research.

The Nielsen Norman Group report describes better performance for concise, scannable, and objective content than for promotional language. It proposes that exaggerated language imposes an additional filtering burden: readers must separate factual content from claims they do not trust or need.

### Practical implications

For personal documents:

- State the conclusion before the background when the reader needs a decision.
- Remove throat-clearing introductions.
- Avoid inflated claims such as “the ultimate,” “revolutionary,” or “the perfect system” unless the language is intentionally personal and clearly framed as opinion.
- Use precise verbs and concrete nouns.
- Put caveats next to the claim they qualify.

This is especially important in research-derived guides. The guide should not turn research into confident-sounding slogans that exceed the evidence.

Source:

- [How Users Read on the Web — Nielsen Norman Group](https://www.nngroup.com/articles/how-users-read-on-the-web/)

---

## 2.4 Cognitive-load research supports removing unnecessary processing

### Evidence tier

Tier 1/2: review of cognitive-load and multimedia-learning research.

Castro-Alonso and colleagues review strategies for optimizing instructional materials. The review discusses:

- The multimedia principle
- The split-attention effect and spatial contiguity
- The redundancy/coherence principle
- The signaling principle
- The transient-information and segmenting principles

The authors also discuss how learners can sometimes manage these strategies themselves, while noting that effects can depend on expertise.

Source:

- [Castro-Alonso et al., “Five Strategies for Optimizing Instructional Materials” — PubMed](https://pubmed.ncbi.nlm.nih.gov/33716467/)
- [Full-text record — PMC](https://pmc.ncbi.nlm.nih.gov/articles/pmid/33716467/)

### Practical Markdown implications

#### Remove redundancy

Do not repeat the same message in the title, introductory paragraph, callout, summary, and conclusion unless each repetition serves a different retrieval or action purpose.

#### Keep related material together

If a diagram explains a process, place it close to the explanation. If a table compares options, place the interpretation near the table rather than forcing the reader to search elsewhere.

#### Signal importance

Use a restrained set of signals:

- Informative headings
- Bold terms
- Short lead sentences
- Numbered steps
- Purposeful callouts
- Consistent labels

#### Segment complexity

Break a long process into stages. For example:

```markdown
## Stage 1 — Decide the goal

## Stage 2 — Prepare the material

## Stage 3 — Execute the workflow

## Stage 4 — Review the result
```

### Important limitation

Most of this evidence comes from instructional multimedia, not ordinary personal notes. The principles should be used as design guidance, not as rigid laws. A simple text note does not need to become a multimedia lesson merely because visuals can sometimes help learning.

---

## 2.5 Signaling helps readers identify important information

### Evidence tier

Tier 1: meta-analysis of signaling in multimedia learning.

Alpizar, Adesope, and Wong conducted a meta-analysis of the signaling principle in multimedia learning environments. The surrounding research base includes cueing, attention guidance, eye-tracking, and signaling relationships between text and visual information.

Source:

- [A Meta-Analysis of Signaling Principle in Multimedia Learning Environments](https://doi.org/10.1007/s11423-020-09748-7)
- [Crossref metadata and abstract record](https://api.crossref.org/works/10.1007/s11423-020-09748-7)

### Practical implications

Signaling in Markdown can include:

- Headings that name the question answered by a section
- Bolded terms that anchor scanning
- A concise “Bottom line” block
- A warning callout before a risky step
- A short label before an example
- A diagram that emphasizes flow or dependency

### Restraint requirement

If every sentence is bold, highlighted, boxed, or decorated, the signals lose contrast. Signaling works through selective emphasis, not maximum emphasis.

---

## 2.6 Active processing is more defensible than passive rereading

### Evidence tier

Tier 1/2: broad review in cognitive and educational psychology.

Dunlosky and colleagues evaluated ten learning techniques, including:

- Elaborative interrogation
- Self-explanation
- Summarization
- Highlighting
- Keyword mnemonics
- Imagery
- Rereading
- Practice testing
- Distributed practice
- Interleaved practice

Their review gave high utility ratings to practice testing and distributed practice. Elaborative interrogation, self-explanation, and interleaving received moderate ratings. Rereading, highlighting, and some forms of summarization received lower ratings because their benefits were less consistent or depended heavily on conditions.

Source:

- [Improving Students’ Learning With Effective Learning Techniques — PubMed](https://pubmed.ncbi.nlm.nih.gov/26173288/)
- [Publisher link](https://journals.sagepub.com/doi/10.1177/1529100612453266)

### Implications for document types

A document intended to help the user learn may include optional retrieval prompts:

```markdown
## Retrieval prompts

1. What is the central idea?
2. When should I use it?
3. What would make it fail?
4. Can I explain the process without looking?
```

A normal reference note should not automatically contain quizzes. The cost of active-recall features is justified when retention is a goal, not when the document is merely a lookup reference.

### Design distinction

The future skill should distinguish:

- **Reference documents** — optimized for finding and applying information
- **Learning documents** — optimized for understanding and later retrieval

These may share a visual language but should not be forced into the same structure.

---

## 2.7 Digital note-taking research favors processing over transcription

### Evidence tier

Tier 2: peer-reviewed experimental study.

Mueller and Oppenheimer’s paper, *The Pen Is Mightier Than the Keyboard*, reports three studies in which students who took notes on laptops performed worse on conceptual questions than students who took notes longhand. The authors argue that laptop users were more likely to transcribe lectures verbatim, while longhand note-takers processed and reframed information.

Source:

- [The Pen Is Mightier Than the Keyboard — DOI](https://doi.org/10.1177/0956797614524581)
- [Crossref record with abstract](https://api.crossref.org/works/10.1177/0956797614524581)

### Relevance to generated Markdown

This is evidence about the note-creation process, not proof that Markdown is inherently inferior to handwritten notes. The transferable lesson is:

> A useful document should transform information rather than merely transcribe it.

A research-to-guide workflow should therefore move through:

```text
Source findings
→ interpretation
→ personal relevance
→ recommended action
→ usable document
```

### Limitations

The study concerned students taking lecture notes. It does not establish that a carefully designed digital reference guide is inferior to handwritten notes. It supports caution against verbatim copying and unprocessed source accumulation.

---

## 2.8 Visuals can help, but decorative detail can distract

### Evidence tier

Tier 1/2: cognitive-load and multimedia-learning research.

The cognitive-load review supports using visualizations when they complement text, while also supporting the removal of nonessential information. The research base includes work on the coherence principle, redundancy, signaling, spatial contiguity, and split attention.

### Practical distinction

A useful visual answers one of these questions:

- What is the sequence?
- What depends on what?
- How do options compare?
- Where does a decision branch?
- What are the parts of this system?
- What is the relationship between concepts?

A decorative visual merely fills space or creates atmosphere.

### Suggested rule

Use a table for comparison, a diagram for relationships or flow, and prose for explanation. Do not use one medium for all three jobs.

---

## 2.9 Aesthetic appeal influences perceived usability

### Evidence tier

Tier 3: applied HCI research summary.

Nielsen Norman Group describes the aesthetic-usability effect: people tend to perceive attractive interfaces as more usable and may tolerate minor usability problems longer. The article traces the effect to Kurosu and Kashimura’s 1995 study of ATM interfaces.

Sources:

- [The Aesthetic-Usability Effect — Nielsen Norman Group](https://www.nngroup.com/articles/aesthetic-usability-effect/)
- [Kurosu & Kashimura, “Apparent Usability vs. Inherent Usability”](https://doi.org/10.1145/223355.223730)

### Practical implications

Pretty documents may be:

- Easier to approach
- Perceived as more orderly
- More inviting to revisit
- More likely to receive patient attention

But aesthetics can also mask problems. A visually attractive guide may still have poor navigation, missing steps, or unclear recommendations.

### Design conclusion

Pretty Markdown should mean:

> Visual polish that strengthens hierarchy, approachability, and retrieval without hiding defects or adding maintenance-heavy decoration.

---

# 3. Synthesis into practical design principles

The following principles are the strongest synthesis of the research. They are still research conclusions rather than final instructions for the future skill.

## 3.1 Start with the reader’s task

Identify whether the document is primarily for:

- Learning
- Deciding
- Doing
- Remembering
- Finding
- Capturing
- Explaining

The same subject may need a different document depending on the task.

## 3.2 Match structure to lifespan

### Ephemeral

Optimize for capture speed and immediate use. Avoid elaborate metadata, sources, navigation, and decoration unless they are directly useful.

### Working

Show status, open questions, decisions, and next actions. Make revision easy.

### Reference

Use stable headings, searchable terms, examples, links, and concise retrieval aids.

### Evergreen

Add maintenance signals, source traceability, related links, clear scope, and carefully chosen visual structure.

## 3.3 Put practical value near the top

A substantial guide should normally expose:

- Its purpose
- Its intended reader or use
- Its recommendation or main answer
- Its first action
- Its most important limitation

## 3.4 Use headings as a map

Headings should be meaningful in isolation. A reader viewing VS Code’s Outline should be able to understand the document’s structure without opening every section.

## 3.5 Make one section answer one meaningful question

Useful section questions include:

- What is this?
- Why does it matter?
- How do I use it?
- When should I use it?
- When should I avoid it?
- What are the tradeoffs?
- What should I do next?

## 3.6 Separate action from explanation

Do not bury a procedure inside theory. Present the action first when the user needs to act, then explain why it works.

## 3.7 Treat evidence and interpretation as different layers

A research-derived guide should distinguish:

- Source finding
- Interpretation
- Personal recommendation
- Personal adaptation
- Uncertainty
- Open question

This is both an epistemic and a usability benefit: the reader can understand what is known and what is being recommended.

## 3.8 Remove information that does not earn its place

Ask of each section or visual:

> Does this improve understanding, retrieval, trust, decision-making, or action?

If not, it may be research residue, repetition, or decoration.

## 3.9 Use visual elements semantically

- Tables: comparisons and structured fields
- Diagrams: relationships, sequence, dependencies, branching
- Callouts: warnings, definitions, decisions, shortcuts, limitations
- Lists: discrete items or steps
- Prose: reasoning and nuance

## 3.10 Design for multiple reading depths

A strong document should support:

| Reading depth | Reader need |
|---|---|
| Glance | Identify purpose and main answer |
| Scan | Find headings, keywords, and actions |
| Normal read | Understand the explanation |
| Deep read | Inspect rationale, sources, and limitations |
| Action | Follow a clear next step or procedure |

---

# 4. Public ecosystem findings

## 4.1 Anthropic public Agent Skills

Repository:

- [anthropics/skills](https://github.com/anthropics/skills)

Relevant example:

- [doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)

### Reusable patterns

The document co-authoring workflow emphasizes:

1. Context gathering
2. Refinement and structure
3. Reader testing

It asks about document type, audience, desired impact, format, and constraints before drafting. It also proposes testing a completed document with a fresh model to identify ambiguity, missing context, contradictions, and reader questions.

### Evaluation

**Adapt, do not directly adopt as the default workflow.**

It is useful for substantial research-heavy guides but too ceremonious for quick temporary notes.

Repository status observed during research:

- Public
- Active
- Large public adoption and visibility
- Repository describes its skills as examples and production-related references

Source:

- [Anthropic Skills README](https://github.com/anthropics/skills)

---

## 4.2 Superpowers writing-skill patterns

Repository:

- [obra/superpowers](https://github.com/obra/superpowers)

Relevant resources:

- [Writing Skills](https://github.com/obra/superpowers/tree/main/skills/writing-skills)
- [Skill-authoring best practices](https://github.com/obra/superpowers/blob/main/skills/writing-skills/anthropic-best-practices.md)
- [Testing Skills With Subagents](https://github.com/obra/superpowers/blob/main/skills/writing-skills/testing-skills-with-subagents.md)

### Reusable patterns

- Write a precise trigger description.
- Use concrete examples to communicate quality.
- Test with fresh agents rather than trusting the authoring context.
- Separate authoring from evaluation.
- Treat verification as behavior-focused rather than document-length-focused.

### Evaluation

**Adapt for future skill development and testing.**

These patterns are more relevant to creating the future skill than to the content of the generated Markdown documents.

---

## 4.3 Agent Skills Directory and specification

Sources:

- [Agent Skills Directory](https://skills.sh/)
- [Agent Skills specification](https://agentskills.io/specification)
- [agentskills/agentskills](https://github.com/agentskills/agentskills)

The ecosystem uses directory-based skills with a required `SKILL.md` and optional scripts, references, and assets. The progressive-disclosure model makes the description especially important for discovery and allows deeper resources to be loaded only when needed.

### Evaluation

This is the relevant portability model for a future skill. The future skill should remain narrow enough to trigger reliably and should move long evidence notes or examples into references rather than making the main skill body unnecessarily large.

---

## 4.4 VS Code built-in Markdown support

Source:

- [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)

VS Code provides:

- Markdown Preview
- Side-by-side preview
- Heading-based Outline view
- Jump-to-heading navigation
- Workspace heading search
- Path completion for links and images
- Local link validation when enabled
- Header and link reference navigation
- Mermaid diagram rendering
- KaTeX math rendering
- Custom preview CSS through `markdown.styles`
- Preview security controls

### Important compatibility finding

VS Code targets CommonMark and does not simply equal GitHub Flavored Markdown. A VS Code-first document can therefore use features that do not render identically elsewhere.

This suggests a two-tier design model for future skill research:

```text
Core document layer
→ portable Markdown and stable semantic structure

Optional presentation layer
→ VS Code-specific preview behavior, CSS, or extensions
```

The exact boundary remains open for the future skill-creation session.

---

## 4.5 markdownlint

Sources:

- [markdownlint repository](https://github.com/DavidAnson/markdownlint)
- [markdownlint VS Code extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)

markdownlint provides structural and style rules for Markdown/CommonMark documents, including:

- Heading increments
- Duplicate headings
- Blank lines
- List consistency
- Link fragments
- Alt text
- Code-fence languages
- Table shape
- Descriptive link text
- Consistent emphasis style

It can report issues in VS Code and support automatic fixes for many rules.

### Evaluation

**Strong adoption candidate.**

It is low-cost and useful for technical correctness and consistency.

### Boundary

It cannot determine whether a document is:

- Clear
- Psychologically efficient
- Beautiful
- Properly scoped
- Evidence-based
- Useful to the user

It should remain a validation layer, not be mistaken for a writing-quality system.

Observed public repository metadata during research:

- Repository: `DavidAnson/markdownlint`
- License: MIT
- Public and not archived
- Actively updated at time of research
- Established public adoption

---

## 4.6 Markdown All in One

Sources:

- [Markdown All in One — VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [GitHub repository](https://github.com/yzhang-gh/vscode-markdown)

Capabilities include:

- Table-of-contents generation and updating
- List editing
- Section numbering
- Table formatting
- Task-list support
- Math support
- Link and image completion
- Markdown-to-HTML printing

### Evaluation

**Useful optional adoption candidate.**

It is most useful for substantial reference documents, working notes with many headings, and documents that need HTML export. It is less necessary for short-lived notes.

Observed public repository metadata during research:

- Repository: `yzhang-gh/vscode-markdown`
- Public and not archived
- Actively maintained at time of research
- Established VS Code extension with substantial public usage

---

## 4.7 Mermaid

VS Code’s built-in Markdown Preview supports Mermaid diagrams.

Source:

- [VS Code Markdown documentation — Mermaid](https://code.visualstudio.com/docs/languages/markdown)

The previously common extension:

- [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

is marked deprecated because Mermaid support was merged into VS Code.

### Evaluation

**Use built-in Mermaid; do not add the deprecated extension.**

Mermaid is appropriate for:

- Processes
- Decision trees
- Dependencies
- Feedback loops
- Conceptual relationships

It should not be added merely to make a document appear more advanced.

---

## 4.8 Code Spell Checker

Source:

- [Code Spell Checker — VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

Capabilities include:

- Local spelling checks
- Markdown support
- Custom dictionaries
- Technical dictionaries
- Inline suggestions
- Section-level disable/enable comments
- Custom ignored words

### Evaluation

**Low-cost optional adoption candidate.**

It improves surface quality while keeping checking local. It must be configured carefully around technical terms, names, and intentional personal vocabulary.

The extension documentation explicitly notes that it can have missing words and dictionary errors, so its suggestions require judgment.

---

## 4.9 Foam

Sources:

- [Foam repository](https://github.com/foambubble/foam)
- [Foam documentation](https://foambubble.github.io/foam/)

Foam is a personal knowledge-management and sharing system built around VS Code and GitHub. It provides:

- Wikilinks
- Backlinks
- Graph visualization
- Link completion
- Rename synchronization
- Section references
- Note embeds
- Templates
- Daily notes
- Orphan and placeholder detection
- Publishing recipes

Foam’s documentation also promotes atomic notes and connected knowledge.

### Evaluation

**Strong pattern reference; possible larger adoption.**

Foam is relevant if the workflow expands from standalone documents into a connected personal knowledge base. Its cost includes workspace conventions, extension dependency, wikilink syntax, and ongoing maintenance.

Foam’s own documentation describes the software as work in progress and asks users to tolerate alpha-grade behavior. This makes it less suitable as an invisible dependency of a simple document-writing skill.

---

## 4.10 Obsidian

Source:

- [Obsidian Help](https://help.obsidian.md/)

Relevant capabilities:

- Markdown notes
- Internal links
- Community plugins
- Themes and CSS snippets
- Web clipping
- CLI access
- Publishing
- Sync

### Evaluation

**Pattern reference or separate tool, not a direct VS Code-first dependency.**

Obsidian demonstrates mature patterns for connected notes, backlinks, customization, and publishing. It also introduces a separate application ecosystem and a large choice surface.

---

## 4.11 Quarto

Sources:

- [Quarto Markdown basics](https://quarto.org/docs/authoring/markdown-basics.html)
- [Quarto cross-references](https://quarto.org/docs/authoring/cross-references.html)
- [Quarto CLI repository](https://github.com/quarto-dev/quarto-cli)

Quarto provides extended Markdown authoring for scientific and technical publishing, including:

- Cross-references
- Citations
- Figures and tables
- Math
- Multiple output formats
- HTML/PDF and other publishing workflows

### Evaluation

**Use selectively for publication-heavy documents.**

Quarto is powerful for research reports and reproducible publishing, but excessive for quick personal notes and ordinary personal guides.

---

# 5. Adoption matrix

| Resource or pattern | Provisional recommendation | Main value | Main limitation |
|---|---|---|---|
| VS Code built-in Markdown Preview | Adopt as baseline | Preview, outline, navigation, Mermaid, math, links | Renderer-specific behavior and CommonMark/GFM differences |
| markdownlint | Adopt | Structural consistency and Markdown correctness | Cannot judge meaning, beauty, or reader value |
| Code Spell Checker | Adopt optionally | Surface polish and local spelling checks | False positives and technical vocabulary issues |
| Markdown All in One | Adopt optionally | TOCs, lists, tables, numbering, HTML export | Unnecessary ceremony for small notes |
| Built-in Mermaid | Adopt selectively | Semantic diagrams for flow and relationships | Poor diagrams add clutter; large diagrams can be hard to scan |
| Mermaid preview extension | Reject | No longer necessary | Deprecated because VS Code includes support |
| Anthropic doc-coauthoring | Adapt | Context gathering, refinement, reader testing | Too heavy for quick notes |
| Superpowers writing-skill patterns | Adapt | Examples, testing, skill-quality discipline | Primarily aimed at skill development and coding workflows |
| Foam | Evaluate separately | Connected notes, backlinks, graph, templates | Higher maintenance and alpha-grade warning |
| Obsidian | Pattern reference or separate adoption | Mature linked-note and publishing patterns | Separate app ecosystem and dependency surface |
| Quarto | Use for publishing-heavy cases | Citations, cross-references, multiple outputs | Excessive for ordinary personal Markdown |
| Canvas/design-oriented skills | Reject for core workflow | Strong visual artifact creation | Optimized for art/design artifacts, not readable personal Markdown |

---

# 6. What existing resources do not solve

The public ecosystem already has strong solutions for:

- Markdown syntax support
- Heading navigation
- Link validation
- Spelling
- Table-of-contents generation
- Diagrams
- Connected notes
- Publishing
- Generic document collaboration
- Skill authoring and testing

The least-covered problem is the reasoning layer between research and a useful personal document:

```text
Research findings
→ personal relevance
→ prioritization
→ recommended action
→ retrieval-friendly structure
→ attractive but restrained presentation
```

A future skill could add distinct value by deciding:

- What information belongs in the main document
- What belongs in supporting notes
- What the user should do with the information
- What structure matches the document’s purpose and lifespan
- Which visual elements clarify rather than decorate
- How much evidence visibility is appropriate
- When a quick note should avoid ceremony

---

# 7. Open questions for the future skill-creation session

These were intentionally left unresolved for the next session.

## 7.1 Output workflow

When should the agent:

- Write directly
- Show a draft first
- Ask for approval
- Use an adaptive rule based on document lifespan and research depth

## 7.2 Evidence visibility

Possible approaches include:

- Minimal source visibility
- Full claim-level traceability
- Layered sources with a practical main body and detailed appendix

The research supports preserving traceability, but the exact presentation should be chosen based on document type and reader burden.

## 7.3 Portable versus VS Code-specific presentation

The likely model is:

- Portable semantic Markdown as the core
- Optional VS Code-specific polish when it adds meaningful value

The precise feature boundary needs practical rendering tests.

## 7.4 Unified skill versus modes

The skill might use a unified workflow with internal modes for:

- Ephemeral notes
- Working documents
- Reference guides
- Evergreen guides
- Learning notes
- Procedures

Or it might eventually split into narrower skills. The research suggests that lifespan and reader task matter enough to justify mode-aware behavior, but not necessarily separate skills.

## 7.5 Standalone versus connected documents

Standalone readability should remain the baseline. Links, indexes, backlinks, tags, and knowledge-base features should be added when the document has long-term reuse value.

## 7.6 Validation scope

Technical validation can be delegated to tools such as markdownlint, but psychological and visual validation likely requires a document-specific self-check or reader-oriented review.

---

# 8. Provisional overall conclusion

The future capability should not be understood as a generic “make Markdown prettier” skill.

A more useful description is:

> A purpose- and lifespan-aware personal document generator that transforms information into an actionable, scannable, visually coherent Markdown document.

The research-supported conceptual layers are:

```text
1. Identify the document’s task
2. Estimate lifespan and maintenance needs
3. Extract and prioritize useful information
4. Convert information into actions, decisions, or retrieval aids
5. Build a clear heading and section hierarchy
6. Add restrained visual signaling
7. Preserve evidence, uncertainty, and personal adaptation
8. Run structural and surface-quality checks
```

The primary opportunity for a future Skill v2 is the transformation step—not basic Markdown syntax. VS Code and existing extensions already cover much of the technical layer.

---

# 9. Source index

## Psychology, learning, and cognition

1. Dunlosky et al. — [Improving Students’ Learning With Effective Learning Techniques](https://pubmed.ncbi.nlm.nih.gov/26173288/)
2. Castro-Alonso et al. — [Five Strategies for Optimizing Instructional Materials](https://pubmed.ncbi.nlm.nih.gov/33716467/)
3. Alpizar, Adesope, & Wong — [A Meta-Analysis of Signaling Principle in Multimedia Learning Environments](https://doi.org/10.1007/s11423-020-09748-7)
4. Mueller & Oppenheimer — [The Pen Is Mightier Than the Keyboard](https://doi.org/10.1177/0956797614524581)
5. Kurosu & Kashimura — [Apparent Usability vs. Inherent Usability](https://doi.org/10.1145/223355.223730)

## Applied reading and usability research

6. Nielsen Norman Group — [How Users Read on the Web](https://www.nngroup.com/articles/how-users-read-on-the-web/)
7. Nielsen Norman Group — [F-Shaped Pattern of Reading on the Web](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
8. Nielsen Norman Group — [The Aesthetic-Usability Effect](https://www.nngroup.com/articles/aesthetic-usability-effect/)

## VS Code and Markdown tooling

9. [Markdown and Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)
10. [DavidAnson/markdownlint](https://github.com/DavidAnson/markdownlint)
11. [markdownlint VS Code extension](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
12. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
13. [Markdown All in One repository](https://github.com/yzhang-gh/vscode-markdown)
14. [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
15. [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

## Agent Skills and workflows

16. [Anthropic public skills](https://github.com/anthropics/skills)
17. [Anthropic document co-authoring skill](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring)
18. [obra/superpowers](https://github.com/obra/superpowers)
19. [Superpowers writing skills](https://github.com/obra/superpowers/tree/main/skills/writing-skills)
20. [Agent Skills Directory](https://skills.sh/)
21. [Agent Skills specification](https://agentskills.io/specification)
22. [agentskills/agentskills](https://github.com/agentskills/agentskills)

## Knowledge management and publishing

23. [Foam](https://github.com/foambubble/foam)
24. [Foam documentation](https://foambubble.github.io/foam/)
25. [Obsidian Help](https://help.obsidian.md/)
26. [Quarto Markdown basics](https://quarto.org/docs/authoring/markdown-basics.html)
27. [Quarto cross-references](https://quarto.org/docs/authoring/cross-references.html)
28. [Quarto CLI](https://github.com/quarto-dev/quarto-cli)
