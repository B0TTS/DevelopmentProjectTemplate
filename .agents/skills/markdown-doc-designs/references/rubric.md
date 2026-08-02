# Markdown Doc Design Rubric

The condensed, research-backed rubric for evaluating Markdown documents. Load this for manual review, or in auto mode when the doc is substantial or research-derived. Sources are summarized from the research findings artifact (`b0ttsagent/handoffs/08-01-2026/markdown-document-writing-research-findings.md`).

## Table of contents

1. Evidence tiers
2. Reader-task taxonomy
3. Lifespan model
4. Reading depths
5. Review principles (the core rubric)
6. Visual element semantics
7. Evidence-layering rules
8. What earns its place
9. Source index

---

## 1. Evidence tiers

Used to weight findings. Stronger tiers govern core rules; weaker tiers are optional and never override stronger evidence.

- **Tier 1** — systematic reviews, meta-analyses, broad evidence reviews, established cognitive theory.
- **Tier 2** — individual peer-reviewed studies, PubMed/publisher records.
- **Tier 3** — applied usability research, information-architecture practice, mature tool documentation, public workflow/skill implementations.
- **Tier 4** — community conventions, popular Markdown patterns without direct evidence of reader benefit.

---

## 2. Reader-task taxonomy

Identify the document's primary task before evaluating. The same subject may need a different document depending on the task.

| Task | What the reader needs | Structure bias |
|---|---|---|
| Learn | understanding + later retrieval | allow active-recall features; explain then test |
| Decide | a recommendation + tradeoffs | conclusion first, then options and limitations |
| Do | a clear next step or procedure | action first, then explanation |
| Remember | durable retrieval anchors | stable headings, searchable terms, concise aids |
| Find | fast lookup | strong heading map, indexes, scannable terms |
| Capture | speed | minimal ceremony, no metadata burden |
| Explain | shared understanding | reasoning in prose, nuance preserved |

A finding should reference the task it serves: "this section buries the action the reader needs to **do**."

---

## 3. Lifespan model

Ceremony scales with lifespan. Do not impose reference-grade structure on an ephemeral note.

| Lifespan | Optimize for | Avoid |
|---|---|---|
| Ephemeral | capture speed, immediate use | metadata, sources, navigation, decoration |
| Working | status, open questions, decisions, next actions; easy revision | elaborate formatting, locked structure |
| Reference | stable headings, searchable terms, examples, links, concise retrieval aids | throwaway phrasing, unstable terms |
| Evergreen | maintenance signals, source traceability, related links, clear scope, restrained visual structure | fragile renderer-specific features, time-sensitive facts |

---

## 4. Reading depths

A strong document supports all five. A finding may name which depth fails.

| Reading depth | Reader need |
|---|---|
| Glance | Identify purpose and main answer |
| Scan | Find headings, keywords, and actions |
| Normal read | Understand the explanation |
| Deep read | Inspect rationale, sources, and limitations |
| Action | Follow a clear next step or procedure |

---

## 5. Review principles (the core rubric)

Each principle: the rule, its evidence tier, how to check it, and the common failure.

### 5.1 Start with the reader's task
- **Evidence:** Tier 3 (applied IA/usability).
- **Check:** Can the reader tell within the first screen whether this doc helps them learn, decide, do, remember, find, capture, or explain?
- **Failure:** A guide that tries to be both a reference and a tutorial and does neither well.

### 5.2 Match structure to lifespan
- **Evidence:** Tier 3.
- **Check:** Does the ceremony (metadata, sources, navigation, decoration) match the lifespan? Ephemeral docs should not carry reference-grade scaffolding.
- **Failure:** A temp note with a source index and TOC; or an evergreen guide with no maintenance signals.

### 5.3 Put practical value near the top
- **Evidence:** Tier 3 (Nielsen scanning research).
- **Check:** Does the doc expose purpose, intended reader/use, recommendation or main answer, first action, and most important limitation before sustained reading?
- **Failure:** The bottom line is buried in the third paragraph of the third section.

### 5.4 Use headings as a map
- **Evidence:** Tier 3 (F-pattern / layer-cake scanning).
- **Check:** Of every heading — if I saw only this heading in VS Code's Outline or a search result, would I know what I would find there? Do the first words carry the information-bearing phrase?
- **Failure:** "Thoughts", "More information", "Important", "Miscellaneous".

### 5.5 One meaningful question per section
- **Evidence:** Tier 3.
- **Check:** Does the section answer one question (What is this? Why does it matter? How do I use it? When should I use it? When should I avoid it? What are the tradeoffs? What's next?)?
- **Failure:** A section that mixes rationale, steps, and caveats under one vague heading.

### 5.6 Separate action from explanation
- **Evidence:** Tier 3.
- **Check:** When the reader needs to act, is the action given before the explanation of why it works?
- **Failure:** A procedure buried inside theory.

### 5.7 Treat evidence and interpretation as different layers
- **Evidence:** Tier 1/2 (cognitive-load review; note-taking study).
- **Check:** In research-derived docs, are source finding, interpretation, personal recommendation, personal adaptation, uncertainty, and open questions kept visibly distinct?
- **Failure:** A research claim stated as a confident personal recommendation with no separation of what is known from what is being advised.

### 5.8 Remove information that does not earn its place
- **Evidence:** Tier 1/2 (coherence / redundancy principle).
- **Check:** Of each section or visual — does it improve understanding, retrieval, trust, decision-making, or action? Cut research residue, repetition that serves no retrieval purpose, and decoration.
- **Failure:** A diagram that fills space; a callout that repeats the heading; a "Background" section no one reads.

### 5.9 Use visual elements semantically
- **Evidence:** Tier 1 (signaling meta-analysis) + Tier 1/2 (cognitive-load review).
- **Check:** Is each visual matched to its job — table for comparison, diagram for relationships/sequence/dependencies/branching, callout for warnings/definitions/decisions/shortcuts/limitations, list for discrete items or steps, prose for reasoning and nuance? Is no single medium used for all jobs?
- **Failure:** A table used for prose; a Mermaid diagram added to look advanced; callouts used as decoration.

### 5.10 Design for multiple reading depths
- **Evidence:** Tier 3.
- **Check:** Can a reader glance (get purpose), scan (find headings/actions), read normally (understand), deep-read (inspect sources/limitations), and act (follow a clear step)?
- **Failure:** A doc that only works if read end to end.

### 5.11 Use active-recall features only for learning docs
- **Evidence:** Tier 1/2 (Dunlosky et al. learning-techniques review).
- **Check:** Are retrieval prompts / self-test sections present only when retention is a goal? Do not add quizzes to a lookup reference.
- **Failure:** A reference note with a "Retrieval prompts" section the reader will never use.

### 5.12 Transform, don't transcribe
- **Evidence:** Tier 2 (Mueller & Oppenheimer note-taking study).
- **Check:** Does a research-derived guide move through source findings → interpretation → personal relevance → recommended action → usable document, rather than verbatim transcription?
- **Failure:** A guide that copies source material with no personal adaptation or prioritization.

### 5.13 Signal with restraint
- **Evidence:** Tier 1 (signaling meta-analysis).
- **Check:** Is emphasis selective? If every sentence is bold, highlighted, boxed, or decorated, signals lose contrast. Signaling works through selective emphasis.
- **Failure:** A doc where half the text is bold or every other paragraph is a callout.

### 5.14 Pretty means usable, not decorative
- **Evidence:** Tier 3 (aesthetic-usability effect).
- **Check:** Does visual polish strengthen hierarchy, approachability, and retrieval — without hiding defects or adding maintenance-heavy, renderer-fragile decoration?
- **Failure:** Custom CSS or callout styling that masks missing steps or unclear recommendations.

---

## 6. Visual element semantics

| Element | Use for | Do not use for |
|---|---|---|
| Table | comparisons, structured fields | prose, narrative |
| Diagram (Mermaid) | relationships, sequence, dependencies, branching, feedback loops | decoration, simple lists |
| Callout | warnings, definitions, decisions, shortcuts, limitations | emphasis that bold could carry |
| List | discrete items, ordered steps | prose with transitions |
| Prose | reasoning, nuance, explanation | discrete facts that belong in a list/table |
| Bold | anchoring scan to key terms | whole sentences or paragraphs |

A useful visual answers one of: sequence? dependency? comparison? decision branch? parts of a system? concept relationship? A visual that answers none of these is decorative — flag it.

---

## 7. Evidence-layering rules

For research-derived documents only. Keep these layers visibly distinct:

1. **Source finding** — what the research observed, attributed.
2. **Interpretation** — what it means in general.
3. **Personal recommendation** — what the reader should do.
4. **Personal adaptation** — how it fits this reader's context.
5. **Uncertainty** — where the evidence is weak or contested.
6. **Open question** — what remains unresolved.

Mixing layer 1 with layer 3 (presenting a research finding as a confident personal recommendation) is a Blocker.

---

## 8. What earns its place

Before flagging "add X", ask whether X improves one of: understanding, retrieval, trust, decision-making, or action. Before flagging "remove X", ask the same. The rubric is not additive — more elements is not better. The goal is the minimum structure that lets the reader do the task at their needed reading depth.

Redundancy check specifically: do not repeat the same message in the title, intro, callout, summary, and conclusion unless each repetition serves a different retrieval or action purpose.

---

## 9. Source index

Key citations behind the rubric. Full links are in the research findings artifact.

**Psychology, learning, cognition**
- Dunlosky et al. — *Improving Students' Learning With Effective Learning Techniques* (Tier 1/2). Practice testing and distributed practice rated high utility; rereading and highlighting low.
- Castro-Alonso et al. — *Five Strategies for Optimizing Instructional Materials* (Tier 1/2). Multimedia, split-attention, redundancy/coherence, signaling, segmenting.
- Alpizar, Adesope & Wong — *Meta-Analysis of Signaling Principle in Multimedia Learning* (Tier 1). Signaling helps; effect depends on selective use.
- Mueller & Oppenheimer — *The Pen Is Mightier Than the Keyboard* (Tier 2). Processing beats transcription.
- Kurosu & Kashimura — *Apparent Usability vs. Inherent Usability* (Tier 3). Aesthetic-usability effect.

**Applied reading and usability**
- Nielsen Norman Group — *How Users Read on the Web* (Tier 3). Users scan; concise + scannable + objective wins.
- Nielsen Norman Group — *F-Shaped Pattern of Reading on the Web* (Tier 3). Headings as scanning cues; information-bearing first words.
- Nielsen Norman Group — *The Aesthetic-Usability Effect* (Tier 3). Attractive things are perceived as more usable — but aesthetics can mask defects.

**Tooling and standards (for boundary, not for this skill to invoke)**
- VS Code Markdown docs — CommonMark target, not GFM; preview-specific behavior exists.
- markdownlint — structural/syntax correctness only; cannot judge meaning, beauty, or reader value.
- Agent Skills specification (agentskills.io) — progressive-disclosure model.
