---
name: agent-builder
description: Create in-depth custom agents and corresponding skills for OpenCode with extensive research phases, parallel subagents, dynamic Q&A with research configuration, and persistent research storage for future evolution.
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: enhanced-agent-creation
  domain: opencode
  research_extent: configurable  # quick|standard|deep|expert
---

## What I Do

- Guide interactive agent creation through structured Q&A with 14 questions (Q9-Q14 for research)
- Execute parallel research subagents based on user-defined extent and topics
- **Research troubleshooting knowledge**: Common issues, bugs, error messages, and documented workarounds
- **Research version/changelog history**: Breaking changes, deprecations, migration guides, version evolution
- Generate research-backed agent files with detailed narrative analysis
- Create associated skills when complex instructions are needed
- Validate agent configuration against quality standards (90% threshold)
- Support both OpenCode-only and Claude-compliant output formats
- Store comprehensive research findings in agent `research/` subfolder
- Provide update instructions for future agent evolution in `research/INSTRUCTIONS.md`

## When to Use Me

Use when:
1. Creating a new agent for OpenCode with complex requirements
2. Building specialized subagents for workflows
3. Creating agents requiring extensive research on technologies, frameworks, or domains
4. Migrating agents from other systems (Cursor, Claude Code)
5. Defining orchestrator agents with delegation patterns
6. Creating agents that will evolve over time with update procedures

## Non-Interactive Mode (Fast-Path)

When calling agent-builder programmatically (via task tool) with a complete specification:

- Agent purpose/domain clearly stated
- Target platforms or technologies listed
- Quality expectations mentioned

**Example non-interactive invocation:**
```
Create a Kotlin Pro agent expert in Kotlin Multiplatform (Android, iOS, Desktop, Web), 
with extensive knowledge on architecture patterns, deployment, app store publishing, 
native APIs, Kotlin web, debugging, and standards. Integrate UX behavioral design 
principles. Create as global skill matching opencode-knowledge quality (280-350 line 
agent, 18+ knowledge files of 200+ lines each).
```

**Defaults Applied (unless specified):**
- `scope`: `global` — Agent applies workspace-wide
- `claude_compliant`: `0` — OpenCode-only format
- `research_extent`: `deep` — For comprehensive requests
- `quality_threshold`: `0.90` — 90% quality score required
- `max_iterations`: `3` — Maximum fix iterations

The agent-builder will:
1. Detect complete specification
2. Skip 14-question Q&A
3. Use sensible defaults (deep research_extent for comprehensive requests)
4. Proceed directly to research and generation



## Configuration

### Scope (Default: Global)

```yaml
scope: global | project
```

| Scope | Agent Directory | Research Directory | Skill Directory |
|-------|-----------------|-------------------|-----------------|
| `global` | `~/.config/opencode/agents/` | `~/.config/opencode/agents/{name}/research/` | `~/.config/opencode/skills/` |
| `project` | `.opencode/agents/` | `.opencode/agents/{name}/research/` | `.opencode/skills/` |

### Claude Compliance (Default: 0)

```yaml
claude_compliant: 0 | 1
```

| Value | Behavior |
|-------|----------|
| `0` | OpenCode-only: Use `AGENTS.md`, record-style tools, OpenCode-specific fields |
| `1` | Claude-compliant: Use `CLAUDE.md`, avoid OpenCode-specific fields, use `.claude/` directories |

### Quality Threshold (Default: 0.90)

```yaml
quality_threshold: 0.90
```

Minimum score (out of 100) for agent to pass quality validation.

### Max Iterations (Default: 3)

```yaml
max_iterations: 3
```

### Research Configuration (Q9-Q14)

#### Research Extent (Q9)

| Level | Subagents | Depth | Time Estimate | Use When |
|-------|-----------|-------|---------------|----------|
| `quick` | 1-2 | Surface scan, key docs only | 5-10 min | Simple agents, well-understood domain |
| `standard` | 3-5 | Multiple sources, moderate depth | 15-30 min | Most agents, new domain for user |
| `deep` | 5-8 | Comprehensive, all relevant sources | 30-60 min | Complex agents, novel domain |
| `expert` | 8+ | Exhaustive, novel research required | 1-2+ hours | Critical agents, cutting-edge domain |

**Default**: `standard`

#### Research Topics (Q10)

Accepts comma-separated list with dynamic subquestions:

```
User: "security, performance"
System:
  - For 'security', what specific areas? (e.g., authentication, input validation, secrets management)
  - For 'performance', what specific areas? (e.g., caching, lazy loading, bundle size)
```

#### Source Prioritization (Q11)

| Source Type | Best For |
|-------------|----------|
| `Official Docs` | Version-specific features, APIs |
| `GitHub Examples` | Implementation patterns, edge cases |
| `Community Discussions` | Common pitfalls, solutions |
| `Academic Papers` | Novel algorithms, cutting-edge techniques |
| `Internal Codebase` | Consistency, integration points |

**Default**: `Official Docs, GitHub Examples`

#### Technology/Framework Focus (Q12)

Accepts comma-separated list with dynamic subquestions for versions and aspects.

#### Platform Integration (Q13)

| Level | Description |
|-------|-------------|
| `standalone` | Self-contained, no platform dependencies |
| `loose` | Optional platform integration, graceful degradation |
| `tight` | Platform-aware, uses platform capabilities |
| `core` | Deep platform integration, extends platform |

**Default**: `loose`

#### Failure Modes (Q14)

Accepts comma-separated list with dynamic subquestions for handling strategies.

### Troubleshooting & Version History Research (Automatic)

For all agents, agent-builder **automatically** researches when applicable:

| Research Area | Sources | Output Location |
|---------------|---------|-----------------|
| **Common Issues** | GitHub Issues, Stack Overflow, Discord/Slack | `research/findings/troubleshooting-001.md` |
| **Known Bugs** | Issue trackers, release notes, PR references | `research/findings/known-bugs-001.md` |
| **Workarounds** | Community solutions, Gists, discussions | `research/findings/workarounds-001.md` |
| **Breaking Changes** | CHANGELOG.md, release notes, migration guides | `research/findings/changelog-001.md` |
| **Version Evolution** | Version history, deprecation notices | `research/findings/version-history-001.md` |

**Research Priority**: Troubleshooting research runs in parallel with topic research, weighted by `research_extent`:
- `quick`: Scan top 5 issues/docs only
- `standard`: Scan top 20 issues + recent changelogs
- `deep`: Comprehensive issue scan + full changelog + community solutions
- `expert`: Exhaustive historical analysis + edge case documentation

### Quality Threshold (Default: 0.90)

```yaml
quality_threshold: 0.90
max_iterations: 3
```

### Research Storage Structure

```
~/.config/opencode/agents/{agent-name}/
├── {agent-name}.md              # The generated agent file
└── research/
    ├── research-spec.md         # Research specification from Q9-Q14
    ├── research-execution.md    # Execution log with timestamps
    ├── research-synthesis.md    # Synthesized findings
    ├── findings/
    │   ├── opencode-formats-001.md
    │   ├── existing-agents-001.md
    │   ├── {topic}-001.md           # Topic-specific research
    │   ├── troubleshooting-001.md   # Common issues & error messages
    │   ├── known-bugs-001.md        # Documented bugs & edge cases
    │   ├── workarounds-001.md       # Community solutions & workarounds
    │   ├── changelog-001.md         # Breaking changes & deprecations
    │   └── version-history-001.md   # Version evolution & migration guides
    ├── sources/
    │   └── {source}-001.md          # Downloaded documentation
    └── INSTRUCTIONS.md             # Update instructions for future evolution
```

## Agent Templates

### Research Agent Template

For agents that gather and synthesize information.

```markdown
---
name: {name}
description: {description}
mode: subagent
tools:
  read: true
  glob: true
  grep: true
  webfetch: true
  websearch: true
  write: false
  edit: false
  bash: false
  task: false
model: default
temperature: 0.3
category: research
---

{agent-body}
```

### Code Review Agent Template

For agents that analyze code without modifying it.

```markdown
---
name: {name}
description: {description}
mode: subagent
tools:
  read: true
  glob: true
  grep: true
  write: false
  edit: false
  bash: false
model: default
temperature: 0.1
category: quality
---

{agent-body}
```

### Orchestrator Agent Template

For agents that coordinate other agents.

```markdown
---
name: {name}
description: {description}
mode: primary
tools:
  read: true
  write: true
  edit: true
  glob: true
  grep: true
  task: true
permission:
  task:
    "*": "allow"
model: default
temperature: 0.2
category: orchestration
---

{agent-body}
```

### Documentation Agent Template

For agents that create and maintain documentation.

```markdown
---
name: {name}
description: {description}
mode: subagent
tools:
  read: true
  write: true
  edit: true
  glob: true
  grep: true
  webfetch: true
  bash: false
model: default
temperature: 0.5
category: documentation
---

{agent-body}
```

### Development Agent Template

For agents that write and modify code.

```markdown
---
name: {name}
description: {description}
mode: subagent
tools:
  read: true
  write: true
  edit: true
  glob: true
  grep: true
  bash: true
  webfetch: true
model: default
temperature: 0.3
category: development
---

{agent-body}
```

## Tool Selection Guide

| Tool | Enable When |
|------|-------------|
| `read` | Always (default) |
| `glob` | File discovery needed |
| `grep` | Content search needed |
| `write` | Creates new files |
| `edit` | Modifies existing files |
| `bash` | Shell commands required |
| `task` | Delegates to subagents |
| `webfetch` | Fetches web content |
| `websearch` | Web search required |
| `lsp` | LSP operations needed |

## Quality Checklist

### Required Fields

- [ ] `name` - kebab-case, 1-64 chars, matches `[a-z0-9]+(-[a-z0-9]+)*`
- [ ] `description` - 1-1024 chars, clear purpose
- [ ] `mode` - `primary`, `subagent`, or `all`

### Recommended Fields

- [ ] `tools` - record-style mapping (NOT comma-separated string)
- [ ] `temperature` - appropriate for agent type
- [ ] `category` - logical grouping
- [ ] `tags` - searchable keywords

### Content Requirements

- [ ] Agent description is 3+ sentences
- [ ] Capabilities list has 1+ items
- [ ] Intended use cases is 2+ sentences
- [ ] Input format specified
- [ ] Output format specified
- [ ] Limitations documented

### Troubleshooting Content (If Applicable)

- [ ] Common issues section with error patterns
- [ ] Known bugs with version-specific context
- [ ] Workarounds with source citations
- [ ] Breaking changes noted with migration guidance
- [ ] Version constraints documented (min version, deprecated features)

## Output Paths

### OpenCode-Only (claude_compliant: 0)

| Type | Global | Project |
|------|--------|---------|
| Agent | `~/.config/opencode/agents/{name}.md` | `.opencode/agents/{name}.md` |
| Skill | `~/.config/opencode/skills/{name}/SKILL.md` | `.opencode/skills/{name}/SKILL.md` |

### Claude-Compliant (claude_compliant: 1)

| Type | Global | Project |
|------|--------|---------|
| Agent | `~/.claude/agents/{name}.md` | `.claude/agents/{name}.md` |
| Skill | `~/.claude/skills/{name}/SKILL.md` | `.claude/skills/{name}/SKILL.md` |

## Related Skills

- opencode-knowledge - Reference for OpenCode formats and best practices
- documentation - For creating agent documentation

## Sources

- OpenCode Agents.md - Agent format specification
- OpenCode Skills.md - Skill format specification
- OpenCode Rules.md - AGENTS.md and CLAUDE.md formats
