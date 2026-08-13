# AGENTS.md Research Report

**Scope:** General research on repository-level `AGENTS.md` files, with the current repository's root `AGENTS.md` as the practical target. This report is research only; it does not propose or apply edits to `AGENTS.md`.

**Research date:** 2026-08-02

## Executive summary

`AGENTS.md` is an open, plain-Markdown convention for giving coding agents durable, repository-specific context and operating instructions. It is best understood as an agent-facing project map and safety/workflow contract—not as a replacement for `README.md`, full architecture documentation, or reusable task workflows.

The highest-confidence guidance from official sources converges on a few areas:

- State the exact commands an agent needs to install, build, test, lint, format, type-check, and run the project.
- Record project-specific facts that are not reliably inferable from source code: non-obvious conventions, directory boundaries, required sequencing, generated files, unusual tooling, operational constraints, and security rules.
- Use concise, concrete, verifiable instructions. Prefer named commands, paths, examples, and explicit approval boundaries over taste words such as “clean” or “best practice.”
- Keep the root file focused and maintained. Link to deeper docs rather than duplicating them.
- Treat nested instruction files as scoped layers for materially different subprojects, not as copies of the root file.
- Keep tool interoperability in mind: `AGENTS.md` is increasingly cross-tool, but discovery and precedence behavior are not identical across Codex, Copilot, Cursor, Claude Code, Gemini CLI, and other tools.
- Treat the file as a living configuration artifact. Update it when recurring corrections, commands, or constraints change.

The research evidence is mixed and should temper simplistic claims that “more instructions are always better.” One controlled Codex study reported lower runtime and output-token use with a root `AGENTS.md`; a broader context-file benchmark found generated files slightly reduced success and increased cost, while developer-written files provided only modest gains; another two-agent ablation found no measurable correctness effect within its statistical power. The safest synthesis is: repository instructions can change agent behavior and may improve efficiency or process alignment, but their value depends heavily on specificity, freshness, non-redundancy, scope, and evaluation.

---

## 1. What `AGENTS.md` is

### 1.1 Open format, not a rigid schema

The official `agents.md` site describes `AGENTS.md` as a simple, open format and an “README for agents.” It says the file is standard Markdown, has no required fields, and may use any headings. The file exists to provide context and instructions that a coding agent needs while working in a repository.

Typical subject matter named by the official site includes:

- project overview;
- build and test commands;
- code style guidelines;
- testing instructions;
- security considerations;
- commit or pull-request conventions;
- deployment steps;
- large datasets and other repository-specific gotchas.

The format is intentionally lower-level than a full agent framework. It does not by itself define executable skills, tool permissions, hooks, subagents, or a universal machine-readable schema.

### 1.2 What it is not

A useful boundary from the sources is:

- `README.md` primarily serves humans evaluating, using, or contributing to the project.
- `AGENTS.md` serves agents that are about to inspect or modify the repository.
- `CONTRIBUTING.md` can remain the human contribution process document.
- A skill packages a reusable task-specific workflow and resources.
- Architecture docs, ADRs, runbooks, and API references should remain the source of truth for their domains.

`AGENTS.md` can link to these documents and identify when the agent should read them. It should not become a second copy of the entire repository documentation set.

### 1.3 Governance and adoption

The official site states that the format emerged from collaboration across OpenAI Codex, Amp, Google Jules, Cursor, and Factory, and is now stewarded by the Agentic AI Foundation under the Linux Foundation. The site also reports use by more than 60,000 open-source projects. These adoption figures are useful ecosystem context, but they are site-reported counts rather than an independently audited measure of effective use.

---

## 2. What belongs in a strong repository file

### 2.1 Project orientation

The agent needs a short factual orientation before it acts:

- what the repository contains;
- the primary languages and frameworks;
- the major runtime or package manager;
- the important top-level areas;
- where the relevant architecture, design, or operational docs live.

The orientation should help the agent choose where to look, not enumerate every file. A pointer such as “read `docs/auth-architecture.md` before changing authentication” is usually more durable than embedding the full architecture explanation.

### 2.2 Exact commands

This is the most consistently repeated practical recommendation in official and high-quality applied sources. Commands should be copy-pasteable and include the working directory, flags, environment setup, or service prerequisites when those matter.

Useful command categories:

| Category | What to record |
|---|---|
| Install/bootstrap | Package manager, lockfile-aware install, required tool versions, local services |
| Development | Start commands, ports, profiles, seed/setup steps |
| Build | Exact build command and output expectations |
| Fast tests | Targeted test command for the area being changed |
| Full tests | CI-equivalent or complete test command; note cost or prerequisites |
| Lint/format | Check and autofix commands, if distinct |
| Type-check | Exact command and relevant scope |
| Validation | Code generation, schema checks, docs builds, smoke tests |
| Deployment/release | Only if relevant, with approval requirements and environment boundaries |

The file should distinguish “run this for a normal change” from “run this only for a full release or expensive validation.” It should not imply that every command must run for every change if that is not true.

### 2.3 Non-obvious conventions

Record conventions an agent is likely to get wrong even after reading nearby code. Examples include:

- an unusual naming or capitalization rule;
- a required error-handling or API pattern;
- a package manager that must be used instead of a tempting alternative;
- a generated directory that must be regenerated rather than hand-edited;
- a test fixture or snapshot workflow;
- a required changelog entry or commit format;
- a subsystem that intentionally violates a general repository convention;
- a required order of operations after changing schemas, routes, clients, or generated code.

The strongest guidance is concrete and verifiable. “Use the project’s normal style” is weak. “Run `pnpm lint --filter api` from the repository root; tests live next to source as `*.test.ts`” is actionable.

### 2.4 Boundaries, approvals, and security

The file should name high-blast-radius actions that require care. Common categories include:

- secrets, API keys, credentials, and private data;
- generated or vendored files;
- production configuration;
- deployment and release commands;
- database migrations or destructive data operations;
- CI/CD and permissions changes;
- public API changes;
- dependency additions or lockfile changes;
- infrastructure or remote-system changes;
- local-only paths or credentials that must never be committed.

Use explicit categories such as:

- **Always:** actions expected for ordinary work;
- **Ask first:** actions requiring user approval;
- **Never:** actions that are prohibited in the agent’s normal operating scope.

The exact categories should reflect the repository. Rules should state the safe alternative where one exists, for example “do not edit `src/generated/`; run `pnpm codegen` from the package root.”

A key distinction: prose instructions are guidance, not an absolute security enforcement mechanism. Claude Code’s official documentation says its persistent Markdown files are context and not enforced configuration; it recommends hooks when an action must be blocked regardless of model judgment. This generalizes: use CI, permissions, sandboxing, hooks, pre-commit checks, and branch protections for hard controls.

### 2.5 Definition of done and reporting

A useful file can state what “complete” means for a normal change:

- targeted checks run and passing;
- broader checks run when relevant;
- tests added or updated for behavior changes;
- generated artifacts refreshed when required;
- no secrets or unrelated changes introduced;
- final response includes changed files, validation performed, and known limitations.

This is especially useful when the repository has repeated handoff or review expectations.

### 2.6 References and routing

A root file can function as a table of contents:

- link to architecture docs;
- link to service-specific runbooks;
- point to test guidance;
- identify navigation guides or design docs;
- say which document to read before changing a sensitive subsystem.

Do not assume a link alone is enough for a critical rule: commands and non-negotiable safety constraints should remain inline because tools differ in how and when they follow references.

---

## 3. Scope, hierarchy, and interoperability

### 3.1 Root and nested files

The official convention supports a root `AGENTS.md` and nested files for subprojects. A nested file is appropriate when a subtree has materially different:

- runtime or language;
- build/test workflow;
- package manager;
- architecture or conventions;
- security boundary;
- deployment process.

The root should contain repository-wide guidance. A nested file should contain only the differences or local rules; duplicating the root creates drift and increases context load.

### 3.2 Codex behavior

OpenAI’s current Codex documentation provides the clearest detailed loading model:

- global instructions come from the Codex home directory;
- project instructions are collected from the project root down to the current directory;
- at each directory, `AGENTS.override.md` is preferred over `AGENTS.md`;
- files are concatenated from general to specific, so deeper instructions appear later;
- the assembled project instructions have a configurable byte limit, with the documented default reported as 32 KiB in the current guide;
- empty files are skipped;
- Codex can be configured with fallback filenames, but arbitrary filenames are not automatically discovered.

Because tooling versions and configurations can vary, verify active instructions in the actual agent. Codex’s documentation suggests commands and logs for checking the source files loaded.

### 3.3 GitHub Copilot behavior

GitHub’s official documentation distinguishes several customization mechanisms:

- `.github/copilot-instructions.md` for repository-wide Copilot instructions;
- `.github/instructions/**/*.instructions.md` for path-scoped instructions with `applyTo` glob frontmatter;
- `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` as agent instruction files for supported Copilot surfaces.

GitHub documents nearest-`AGENTS.md` precedence for Copilot agent work. Support differs by product surface: GitHub.com cloud agent, code review, VS Code, JetBrains, Eclipse, Xcode, and Copilot CLI do not all support the same instruction types. The official support matrix should be consulted before assuming a particular file is active.

### 3.4 Claude Code behavior

Anthropic’s official documentation says Claude Code reads `CLAUDE.md`, not `AGENTS.md`, by default. The documented portability approach is to create a `CLAUDE.md` that imports `AGENTS.md` with `@AGENTS.md`, or to use a symlink when appropriate. On Windows, Anthropic specifically notes that an import avoids the elevated permissions or Developer Mode commonly required for symlinks.

Claude’s own hierarchy includes project, user, managed, local, and path-scoped rule mechanisms. The important general lesson is not to assume that “AGENTS.md is universal” means every tool discovers it identically.

### 3.5 Gemini CLI behavior

Google’s Gemini CLI uses `GEMINI.md` by default and loads hierarchical context files, including just-in-time context when tools access files. The official documentation allows changing `context.fileName` to a filename or list such as `AGENTS.md`, `CONTEXT.md`, and `GEMINI.md`. Therefore, AGENTS interoperability is possible through configuration, but default discovery should be checked for the actual environment.

### 3.6 General interoperability rule

Keep shared guidance tool-agnostic:

- repository facts;
- commands;
- conventions;
- safety boundaries;
- links to project docs.

Keep tool-specific behavior in native adapter files or configuration when needed:

- hooks;
- permission syntax;
- path glob frontmatter;
- custom agent definitions;
- slash commands;
- MCP configuration;
- subagent or model settings.

Avoid multiple conflicting “sources of truth.” If multiple files are necessary, use imports or explicit adapters and periodically audit their relationship.

---

## 4. Relationship to Agent Skills and other mechanisms

The Agent Skills open specification describes a skill as a directory containing a required `SKILL.md` plus optional `scripts/`, `references/`, and `assets/`. The required frontmatter is `name` and `description`; the description should explain both what the skill does and when it should activate.

The key distinction is:

| Mechanism | Best for |
|---|---|
| `AGENTS.md` | Durable repository context, commands, conventions, constraints, routing, and safety expectations that apply broadly |
| Nested `AGENTS.md` | Subtree-specific differences |
| Skill | A reusable task-specific procedure, expertise, examples, scripts, templates, and validation loop |
| Rule file | A topic- or path-specific rule set supported by a tool |
| Subagent/custom agent | A specialized role with its own context, tools, or model behavior |
| Hook/CI/permissions | Enforceable controls and automated checks |
| MCP/tool integration | External data or service access |

Agent Skills use progressive disclosure:

1. metadata is discovered first;
2. the main instructions load when the skill is activated;
3. references, scripts, and assets load only when needed.

This is a strong architecture for keeping `AGENTS.md` from becoming an encyclopedia. Put always-on repository rules in the root file and move multi-step, task-specific workflows into skills or linked documents.

The Agent Skills documentation also recommends extracting skills from real tasks, real corrections, existing project artifacts, code review feedback, and failure cases. This is relevant to `AGENTS.md` maintenance: recurring corrections are evidence for a durable repository rule, while one-off task instructions should generally remain in the task or a skill.

---

## 5. What empirical research currently says

The studies below are preprints or exploratory analyses, not settled standards. They are useful for forming hypotheses and avoiding overconfident advice.

### 5.1 Agent READMEs: An Empirical Study of Context Files for Agentic Coding

**Source:** Chatlatanagulchai et al., 2025, arXiv:2511.12884.

**Design:** Analysis of 2,303 context files from 1,925 repositories across Claude Code, OpenAI Codex, and GitHub Copilot ecosystems.

**Findings:**

- context files were generally long and difficult to read;
- they often used a shallow hierarchy with one H1 and H2/H3 sections;
- they were actively maintained, behaving more like evolving configuration than write-once documentation;
- common content categories included implementation details (69.9%), architecture (67.7%), and build/run guidance (62.3%);
- security (14.5%) and performance (14.5%) appeared much less often;
- automated classification worked better for concrete functional topics than abstract or nuanced categories.

**Implications:** Teams commonly encode functional execution guidance but under-specify non-functional quality and safety constraints. An `AGENTS.md` review should not only ask “can the agent run the project?” but also “what security, performance, privacy, and operational constraints could it get wrong?”

**Limitations:** Category presence was binary, so the study measured whether a topic appeared, not the quality or depth of the guidance. The sample covered three tool ecosystems and may not represent all projects.

### 5.2 On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents

**Source:** Lulla et al., 2026, arXiv:2601.20404.

**Design:** Paired comparison of Codex executions with and without a root `AGENTS.md`, using 10 repositories and 124 pull requests. Measures focused on wall-clock time and token usage.

**Reported findings:**

- median runtime was lower with `AGENTS.md` by approximately 28.64%;
- median output tokens were lower by approximately 16.58%;
- task completion behavior was described as comparable.

**Limitations:**

- one agent family/model configuration;
- a small repository and PR sample;
- focus on efficiency rather than correctness, maintainability, or alignment;
- the authors explicitly call for more repositories, task types, agents, and models.

**Implication:** A good file may reduce repeated discovery and process overhead, but this study does not prove that adding more prose improves patch correctness.

### 5.3 Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

**Source:** Gloaguen et al., 2026, arXiv:2602.11988.

**Design:** Evaluated coding agents on SWE-bench Lite and a new AGENTbench collection of 138 tasks from 12 repositories with developer-written context files. Compared no context, LLM-generated context, and developer-written context across multiple agent/model combinations.

**Reported findings:**

- LLM-generated context files slightly reduced success rates on average;
- developer-written files provided only a modest average improvement;
- context files increased steps and inference costs by more than 20% in the reported settings;
- agents generally followed specific instructions, including repository-specific tool choices;
- context files caused more repository exploration and testing but did not reliably improve task success;
- architectural overviews did not clearly reduce time to find the files relevant to a task;
- generated context performed better when existing documentation was removed, suggesting that redundancy is an important failure mode.

**Implication:** Do not automatically dump a generated repository summary into `AGENTS.md`. High-value content is likely to be specific, non-obvious, and not already available elsewhere. Avoid adding instructions that cause unnecessary exploration or universal full-suite work.

**Limitations:** The benchmark is Python-focused and the findings are task-, agent-, and model-dependent. The authors describe the work as evidence against unnecessary context, not proof that all repository instructions are harmful.

### 5.4 Toward Instructions-as-Code

**Source:** Arabat and Sayagh, MSR 2026 / arXiv:2606.13449.

**Design:** Analysis of 15,549 agentic PRs across 148 projects, comparing project metrics before and after instruction-file creation.

**Reported findings:**

- 27.7% of projects increased merge rate by at least 20%;
- 26.35% decreased it;
- projects with increased merge rate had longer files and more structured headings in an exploratory comparison;
- the authors argue that instruction files should be treated as software-engineering artifacts and evaluated for quality.

**Implication:** Adding an instruction file is not automatically beneficial. Structure and content quality matter, and instruction maintenance deserves version control, review, and evaluation.

**Limitations:** Before/after observational comparisons cannot establish that the instruction file caused the change. Projects may change tools, agents, maintainers, tasks, or development practices at the same time.

### 5.5 Configuring Agentic AI Coding Tools: An Exploratory Study

**Source:** Mohsenimofidi et al., 2026, arXiv:2602.14690.

**Design:** Systematic analysis of eight configuration mechanisms across Claude Code, GitHub Copilot, Cursor, Gemini, and Codex, plus an analysis of 2,923 GitHub repositories.

**Reported findings:**

- context files dominate repository configuration and are often the only mechanism used;
- `AGENTS.md` shows signs of convergence as an interoperable baseline;
- most repositories use only one or two skills or subagents;
- 85.5% of observed skills lacked additional resources, suggesting skills are often used as static text rather than executable workflow bundles;
- tool-specific configuration cultures differ.

**Implication:** Start with a focused `AGENTS.md`; use skills, rules, subagents, hooks, and MCP when they solve a distinct repeated problem rather than adding every mechanism at once.

**Limitations:** The paper is a point-in-time snapshot of a rapidly changing ecosystem and reports adoption patterns, not causal performance effects.

---

## 6. Synthesis: what appears most important

Across official documentation, strong repository examples, and the mixed research evidence, the following principles are the most defensible.

### Principle 1: Optimize for information the agent cannot safely infer

High-value entries answer questions such as:

- Which exact command is correct here?
- Which package manager or environment is mandatory?
- Which generated or remote-controlled files are off-limits?
- Which workflow must happen after a change?
- Which security or operational action requires approval?
- Which design document or runbook must be read before changing this subsystem?

Low-value entries repeat generic software advice or describe obvious directory names without changing agent behavior.

### Principle 2: Make rules concrete and verifiable

Prefer:

- exact commands;
- exact paths;
- named tools;
- explicit conditions;
- small examples;
- safe alternatives;
- validation commands;
- expected output or completion criteria.

Avoid vague language such as “use best practices,” “keep it clean,” or “follow the architecture” without saying where the architecture is documented or how to verify compliance.

### Principle 3: Put high-risk and high-frequency guidance where it is easy to retrieve

The root file should make commands, non-negotiable safety rules, and important routing visible early. A deeply buried rule is easier to miss, especially when instructions are combined from multiple scopes or tools.

### Principle 4: Use scope instead of condition-heavy prose

If a subsystem has a genuinely different workflow, use a nested instruction file or a path-scoped native rule when supported. This is usually clearer than a root file containing many “if you are working in X…” branches.

### Principle 5: Separate guidance from enforcement

`AGENTS.md` can tell the agent not to run a destructive command, but it cannot guarantee compliance. Use permissions, hooks, CI, protected branches, sandboxing, and review gates for actions that must be blocked.

### Principle 6: Maintain it from observed failures

A durable rule should usually originate from one of these signals:

- the agent made the same mistake more than once;
- a reviewer repeatedly requested the same correction;
- a command or package manager changed;
- a new generated-file or deployment boundary appeared;
- a production incident exposed a non-obvious constraint;
- a task repeatedly requires the same routing or validation step.

Do not add every possible rule preemptively. The research suggests instruction files can increase activity and cost when they add redundant or unnecessary requirements.

### Principle 7: Treat it as code-like configuration

Review it in version control, keep it synchronized with scripts and CI, test the commands, and remove stale instructions. A wrong instruction is not harmless documentation debt: an agent may follow it confidently.

---

## 7. Practical reading list

### Highest-priority official sources

1. **AGENTS.md official site** — https://agents.md/
   - Open format definition, purpose, common sections, nested-file concept, FAQ, and configuration examples for Aider and Gemini.

2. **OpenAI Codex: Custom instructions with AGENTS.md** — https://developers.openai.com/codex/guides/agents-md
   - Most detailed official explanation of global/project/nested discovery, override behavior, precedence, size limits, fallback names, and troubleshooting.

3. **OpenAI Codex: Customization** — https://developers.openai.com/codex/concepts/customization
   - Explains how AGENTS.md relates to skills, MCP, and subagents, and recommends keeping durable project guidance small.

4. **GitHub Copilot: support matrix for custom instructions** — https://docs.github.com/en/copilot/reference/custom-instructions-support
   - Important because support varies by Copilot surface.

5. **GitHub Copilot: repository instructions** — https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
   - Documents repository-wide, path-specific, and agent instruction mechanisms.

6. **Claude Code memory and instructions** — https://code.claude.com/docs/en/memory
   - Critical interoperability caveat: Claude Code uses `CLAUDE.md` by default and documents importing `AGENTS.md`.

7. **Gemini CLI context files** — https://geminicli.com/docs/cli/gemini-md/
   - Documents hierarchy, just-in-time context, `/memory`, imports, and configuring `AGENTS.md` as a context filename.

8. **Sentry AGENTS.md template** — https://develop.sentry.dev/sdk/getting-started/templates/agents-md/
   - High-quality practical template emphasizing non-obvious information, exact commands, concise rules, automation, and iterative maintenance.

### Research and empirical sources

9. **Agent READMEs: An Empirical Study of Context Files for Agentic Coding** — https://arxiv.org/html/2511.12884
   - Large-scale characterization of structure, maintenance, and content categories.

10. **On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents** — https://arxiv.org/html/2601.20404
    - Paired Codex efficiency study reporting lower runtime and output-token use with `AGENTS.md`.

11. **Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?** — https://arxiv.org/abs/2602.11988
    - Multi-agent benchmark suggesting generated context can hurt slightly and raise cost; useful counterweight to vendor recommendations.

12. **Toward Instructions-as-Code** — https://arxiv.org/html/2606.13449
    - Large observational PR-level study; argues instruction files should be maintained and evaluated like software artifacts.

13. **Configuring Agentic AI Coding Tools: An Exploratory Study** — https://arxiv.org/html/2602.14690v2
    - Cross-tool ecosystem study covering context files, skills, subagents, rules, hooks, commands, settings, and MCP.

### Skills and reusable resources

14. **Agent Skills specification** — https://agentskills.io/specification
    - Canonical open format for `SKILL.md`, optional scripts/references/assets, and progressive disclosure.

15. **Agent Skills authoring best practices** — https://agentskills.io/skill-creation/best-practices
    - Strong guidance on extracting real expertise, focusing on non-obvious information, using validation loops, and controlling context load.

16. **Anthropic: Introducing Agent Skills** — https://www.anthropic.com/news/skills
    - Official overview and ecosystem rationale.

17. **Anthropic Skills repository** — https://github.com/anthropics/skills
    - Reputable examples of reusable skills and supporting resources.

18. **Sentry skills and AGENTS.md material** — https://github.com/getsentry/skills
    - Practical organization-specific skills, including an AGENTS.md-oriented skill referenced by Sentry’s documentation.

### Evaluation tools and less authoritative but useful resources

19. **Agent Skills reference validator (`skills-ref`)** — https://github.com/agentskills/agentskills/tree/main/skills-ref
    - Validates skill format; it is for `SKILL.md`, not a universal `AGENTS.md` linter.

20. **AGENTS.md evaluation skill** — https://github.com/vltansky/agents-md-evals
    - Experimental A/B-testing resource for discovering which instruction rules actually change behavior. Treat as a research/prototyping tool, not an established standard.

21. **OpenAI Codex repository `AGENTS.md`** — https://github.com/openai/codex/blob/main/AGENTS.md
    - Real-world example of detailed repository and language-specific instructions.

22. **OpenAI Agents Python `AGENTS.md`** — https://github.com/openai/openai-agents-python/blob/main/AGENTS.md
    - Real-world example emphasizing repository structure, `uv`, testing, docs, and contribution checks.

23. **Sentry SDK examples** — linked from https://develop.sentry.dev/sdk/getting-started/templates/agents-md/
    - `sentry-cocoa`, `sentry-javascript`, `sentry-dotnet`, `sentry-react-native`, `sentry-cli`, and `sentry-python` show different repository shapes and command tables.

---

## 8. Questions for a later repository-specific review

This report intentionally does not modify the current root `AGENTS.md`. If the project later wants an audit or redesign, useful questions include:

1. Which instructions in the current file prevent mistakes that agents have actually made?
2. Which commands are currently exact, tested, and still valid?
3. Which rules are specific to this repository versus general agent behavior?
4. Which material belongs in a skill, nav guide, runbook, or architecture document instead?
5. Which actions should be enforced with tooling rather than prose?
6. Are any rules duplicated or potentially conflicting with `.agents/skills/`, tool-native files, or nested instructions?
7. Which security, privacy, deployment, and remote-system constraints are not currently represented?
8. Would a small representative A/B evaluation reveal that any high-cost rules are redundant or counterproductive?

---

## Source-quality notes

- Official vendor and standard sources were prioritized for file semantics and tool behavior.
- Peer-reviewed/preprint empirical studies were used for evidence about effectiveness, with study design and limitations recorded.
- Community guides and experimental tools were included as leads and examples, not treated as authoritative standards.
- Tool support changes quickly. Compatibility claims should be rechecked against current official documentation before operationalizing them.
- Reported adoption counts and claims from `agents.md` are ecosystem-reported and should not be interpreted as proof of quality or efficacy.

---

## References

- AGENTS.md. https://agents.md/
- OpenAI Developers. Custom instructions with AGENTS.md. https://developers.openai.com/codex/guides/agents-md
- OpenAI Developers. Customization. https://developers.openai.com/codex/concepts/customization
- GitHub Docs. Support for different types of custom instructions. https://docs.github.com/en/copilot/reference/custom-instructions-support
- GitHub Docs. Adding repository custom instructions. https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- Anthropic. How Claude remembers your project. https://code.claude.com/docs/en/memory
- Gemini CLI Docs. Provide context with GEMINI.md files. https://geminicli.com/docs/cli/gemini-md/
- Sentry Developer Docs. AGENTS.md template. https://develop.sentry.dev/sdk/getting-started/templates/agents-md/
- GitHub Blog. How to write a great agents.md. https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- Agent Skills. Specification. https://agentskills.io/specification
- Agent Skills. Best practices for skill creators. https://agentskills.io/skill-creation/best-practices
- Anthropic. Introducing Agent Skills. https://www.anthropic.com/news/skills
- Chatlatanagulchai et al. Agent READMEs. https://arxiv.org/html/2511.12884
- Lulla et al. On the Impact of AGENTS.md Files. https://arxiv.org/html/2601.20404
- Gloaguen et al. Evaluating AGENTS.md. https://arxiv.org/abs/2602.11988
- Arabat and Sayagh. Toward Instructions-as-Code. https://arxiv.org/html/2606.13449
- Mohsenimofidi et al. Configuring Agentic AI Coding Tools. https://arxiv.org/html/2602.14690v2
- OpenAI Codex repository. https://github.com/openai/codex/blob/main/AGENTS.md
- OpenAI Agents Python repository. https://github.com/openai/openai-agents-python/blob/main/AGENTS.md
- Vltansky. agents-md-evals. https://github.com/vltansky/agents-md-evals
