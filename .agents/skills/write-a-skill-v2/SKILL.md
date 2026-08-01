---
name: write-a-skill-v2
description: Create, rewrite, and validate Agent Skills (SKILL.md with scripts/, references/, assets/) that load optimally via progressive disclosure per the agentskills.io standard. Use when the user wants to create, write, build, scaffold, or revise an agent skill, or says 'skill', 'SKILL.md', 'meta-skill', or needs correct Agent Skills frontmatter, structure, naming, or trigger descriptions. NOT for hooks, CLAUDE.md/AGENTS.md rules, prompt templates, or pi extensions.
---

# Writing Agent Skills

Author skills that a coding agent can **discover** and **use successfully**. Grounded in the open [Agent Skills standard](https://agentskills.io/specification) and [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). This file is itself kept under 500 lines; push depth into `references/`.

## What a skill is

A skill is a directory that teaches the agent how to do a specific task well. It is **not** a system prompt or a rule file (use `CLAUDE.md`/`AGENTS.md` for permanent rules), nor a prompt template. It is a capability the agent loads on demand when a task matches.

## Progressive disclosure — the core model

The agent loads a skill in three tiers. Design for it.

| Tier | What loads | When | Budget |
|------|-----------|------|--------|
| 1. Metadata | `name` + `description` | At startup, for every skill | ~100 tokens each |
| 2. Instructions | Full `SKILL.md` body | Only when the skill is triggered | < 5000 tokens |
| 3. Resources | `scripts/`, `references/`, `assets/` | Only when actually read | effectively unlimited |

Consequence: you can install dozens of skills — only their descriptions sit in context until one fires. **The description is the most important thing you write.**

## Directory structure

```
skill-name/
├── SKILL.md          # required: frontmatter + instructions
├── scripts/          # optional: deterministic code the agent runs
│   └── validate.py
├── references/      # optional: long-form docs loaded on demand
│   └── schema.md
└── assets/           # optional: templates, data, images
    └── form-template.json
```

Only `SKILL.md` is required. Use **forward slashes** in all paths, even on Windows (backslashes break Unix agents). Reference files **one level deep** — never chain `reference.md → other.md → deeper.md`; the agent may only preview (`head -100`) the deep file and miss content.

## Authoring process

### 1. Gather the trigger surface first (it shapes everything)
Ask the user:
- One sentence: what capability this provides.
- Trigger phrases people will actually type (verbs + nouns).
- What it must **refuse** to do (negative boundary).
- Does it need scripts, or just instructions?
- Which models/agents will run it?

### 2. Write the description before the body
Draft `description` now (see "Trigger router" below). It decides whether your skill ever fires — about 90% of "my skill never loads" reports are description problems, not body problems.

### 3. Build evaluations BEFORE extensive docs
Evaluation-driven authoring (else you document imagined problems):
1. Run the task **without** a skill, with the user. Note what context you keep re-explaining.
2. Write 3 scenarios that would fail without this skill.
3. Author the **minimum** SKILL.md content that lets a fresh agent pass them.
4. Iterate against the scenarios, not against a wish list.

### 4. Two-instance loop: author (A) vs. fresh runner (B)
- **A** = the authoring session (you + the model): design and refine instructions.
- **B** = a **fresh** session with the skill loaded: run the real task and **watch what it actually does** — which files it reads, which rules it skips, whether it over- or under-explains.
- Feed observations back to A: *"B forgot to filter test accounts — should that rule be more prominent?"* Refine, re-test.
- Skills load at session start, so **test triggering in a fresh session** each time.

### 5. Review with the user
Present the draft and ask: Does this cover your use cases? Is anything over- or under-explained? Then run the checklist at the bottom.

## Frontmatter (the rules that bite)

```yaml
---
name: skill-name
description: What it does and when to use it. Be specific.
license: MIT                      # optional
compatibility: requires python3     # optional, max 500 chars
metadata:                          # optional, arbitrary key-value
  author: you
allowed-tools: bash read           # optional, experimental
---
```

**`name` rules (spec):** 1–64 chars; lowercase `a-z`, `0-9`, hyphens only; no leading/trailing hyphen; **no consecutive hyphens**; **must match the parent directory** for portability. Avoid vague names (`helper`, `utils`) and reserved words (`anthropic`, `claude`). Prefer **gerund form** — `processing-pdfs`, `testing-code` — it reads as a capability.

> Harness note (pi): pi relaxes the "name == parent dir" rule and only warns on name violations while still loading the skill. Match the dir anyway — skills are portable across Cursor, Codex, Gemini CLI, etc., and other tools enforce it.

**`description` rules:** 1–1024 chars; non-empty; **third person**; says what it does **and** when to use it. See "Trigger router."

**Harness-honored fields (pi):** only `name`, `description`, and `disable-model-invocation` change behavior. `disable-model-invocation: true` **hides the skill from the system prompt** so the agent won't auto-load it — it can still be triggered explicitly as `/skill:name`. Use it for skills that must only fire on purpose (deploy, destructive ops, or a retained previous version). The other spec fields (`license`, `compatibility`, `metadata`, `allowed-tools`) are spec-valid and useful as documentation/for other tools, but pi ignores them behaviorally. Claude-Code-only fields like `when_to_use`/`user-invocable` are **not** in the standard and pi ignores them — do not rely on them here.

## The trigger router (description = 90% of success)

The description is a router, not docs. The agent semantically matches the user's request against it to decide whether to load the skill.

```
Good:  "Extract text and tables from PDF files, fill forms, merge PDFs.
        Use when working with PDF files, forms, or document extraction."
Bad:   "Helps with documents."          ← matches everything, triggers nothing
```

Pattern that triggers reliably:
1. **First sentence:** what it does (verbs + the concrete nouns people type).
2. **Second sentence:** `Use when …` with the actual trigger phrases.
3. **Negative boundary:** `NOT for …` listing adjacent tasks it could be confused with.

Pitfalls that cause misfires:
- Too broad → loads on irrelevant tasks.
- Too narrow → never fires.
- Vague language ("helps with", "assists") → unreliable matching.
- First person ("I can…") → inconsistent discovery; always third person.

## Degrees of freedom — set specificity deliberately

Pick how much room you leave the agent. Match specificity to fragility.

| Freedom | Form | Use when | Example |
|---------|------|----------|---------|
| **High** | prose instructions | Many valid approaches; context decides | "Review the PR for clarity, correctness, and risk" |
| **Medium** | pseudocode + params | A preferred pattern exists; some variance ok | "Use the field map in `references/schema.md`; map unknown fields to `_unknown`" |
| **Low** | exact scripts | Fragile/consistent; stakes high; exact sequence required | "Run `scripts/migrate.py --plan`, validate output, then `--apply`" |

Analogy: a narrow cliff path needs guardrails (low freedom); an open field just needs a compass (high freedom).

**One job per skill.** If you find an "...and it can also..." branch, split it. Kitchen-sink skills misfire.

## Patterns to build into the skills you author

### Workflow + copy-in checklist
For multi-step tasks, give a numbered workflow and a checklist the agent copies into its reply and ticks off. This prevents skipped steps and lets you (and the agent) track progress.

### Feedback loop
`Run a validator → fix errors → repeat` until clean. The validator can be a script **or** a reference doc the agent checks against (e.g., `references/style-guide.md` as the validator for a writing skill).

### Plan-validate-execute (batch / destructive)
For batch updates or destructive changes, force a plan artifact before execution:
`analyze → write plan (e.g., changes.json) → validate plan with a script → execute → verify`.
The plan must be **machine-verifiable**; make the validator verbose ("field `x` not found; available: a, b, c") so the agent can self-correct.

### Examples pattern
When output quality depends on style, give concrete input→output pairs. Examples convey desired detail more clearly than descriptions.

### Template / conditional
Provide output templates (strict for data formats, flexible when adaptation helps). For decision points, branch with a conditional ("if X, read `references/a.md`; else read `references/b.md`") rather than offering the user a menu — don't make the agent present choices it can resolve itself.

## Scripts (when and how)

Add a utility script when the operation is **deterministic** (validation, formatting) or the **same code** would be regenerated repeatedly. Scripts save tokens, improve reliability, and ensure consistency vs. ad-hoc generated code.

- **Solve, don't defer.** Handle errors explicitly inside the script; don't raise and hand the puzzle back to the agent.
- **No voodoo constants.** Every magic number/flag must be justified and self-documenting (Ousterhout's law). If you don't know the right value, the agent won't either.
- **Run vs. read.** Most scripts should be **executed**, not read into context: say "Run `scripts/analyze.py` to extract fields." Reserve "See `scripts/analyze.py` for the algorithm" for when the agent needs the logic.
- **Declare dependencies** in SKILL.md; don't assume packages are installed.

## Progressive-disclosure mechanics

- Keep **SKILL.md under 500 lines**. Near that limit, split into `references/`.
- For a reference file **> 100 lines**, put a **table of contents** at the top so a partial read still reveals what's available.
- **One level deep**: all reference files link directly from SKILL.md, never from each other.
- **Descriptive filenames**: `references/finance.md`, not `references/doc1.md`.
- **No time-sensitive info** in the body (versions, "latest", dates) — it rots. Move historical/old-pattern notes to a clearly-labeled "old patterns" section.
- **Consistent terminology** throughout — pick one term per concept (`API endpoint`, not also `URL`/`route`/`path`).
- **MCP tool names** must be fully qualified: `BigQuery:bigquery_schema`, not `bigquery_schema`.

## Anti-patterns to avoid

- **Windows backslashes** in paths — always forward slashes.
- **Offering the user a menu** of approaches when the task lets the agent decide — pick the path or use a conditional.
- **Kitchen-sink skills** — split instead.
- **Deep reference chains** — flatten to one level.
- **Magic numbers** in scripts.
- **Time-sensitive facts** in the body.
- **First-person descriptions** ("I can…").
- **Unqualified MCP tool references**.
- **Assuming tools/packages are installed** without declaring them.
- **Over-explaining** what a smart model already knows — challenge each paragraph: "Does this justify its token cost?"

## Testing

- **Test with every model you target.** Opus wants less hand-holding; Haiku wants more; Sonnet is the balance point. One SKILL.md must work across them, so aim for the middle.
- **Test triggering in a fresh session** (skills load at start). A skill that never fires is almost always a description problem.
- **Observe how the runner navigates** — file read order, missed links, over-relied-on sections, ignored files. Iterate on structure, not assumptions.
- Include at least **three evaluations** and run real (not toy) usage before sharing.

## Final checklist

Before sharing a skill, verify:
- [ ] Description: specific, third person, includes what + `Use when…` + a `NOT for…` boundary
- [ ] `name` ≤ 64 chars, valid charset, matches parent dir, no reserved words, gerund form
- [ ] SKILL.md body under 500 lines
- [ ] References one level deep; forward-slash paths; descriptive filenames
- [ ] One job per skill (split if "and it also…")
- [ ] Degrees of freedom chosen deliberately
- [ ] No time-sensitive info; consistent terminology
- [ ] Concrete examples / input-output pairs included
- [ ] Scripts solve (don't defer), no magic constants, deps declared
- [ ] MCP tools fully qualified; no assumed-installed tools
- [ ] At least 3 evaluations; tested on each target model in fresh sessions
- [ ] If it must not auto-fire: `disable-model-invocation: true`

## Harness notes (pi-specific, in addition to the standard)

- pi loads skills from `~/.pi/agent/skills/`, `~/.agents/skills/`, project `.pi/skills/`, `.agents/skills/` (trusted), packages, settings `skills[]`, and `--skill <path>`.
- Skills register as `/skill:name` and accept args: `/skill:pdf-tools extract file.pdf`.
- `disable-model-invocation: true` ⇒ hidden from the system prompt, `/skill:name` only.
- Unknown frontmatter fields are ignored (no warning); only `name`/`description`/`disable-model-invocation` affect behavior.
- Missing description ⇒ skill not loaded. Name collisions warn and keep the first found.

---

*Authoring a skill? Pair this with the `karpathy-guidelines` skill: surgical changes, no speculative flexibility, verifiable success criteria.*