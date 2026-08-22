# Which prompt-improvement skill to use: prompt-architect vs improve-prompt

> Default to **prompt-architect** for chat-based prompt improvement across any model; reach for **improve-prompt** when the prompt lives inside a source file and you want Claude-orthodox, deliberately non-bloated output.

**Task:** decide
**When to use:** Any time you're about to improve a prompt in this project and need to pick between the two installed skills (`prompt-architect` and `improve-prompt`). Both live in `.agents/skills/` and trigger on the same keywords ("improve this prompt"), so the choice is a real fork, not automatic.

## What each skill is for

| | **prompt-architect** | **improve-prompt** |
|---|---|---|
| Doctrine | 31 research-backed frameworks across 7 intent categories | The 10 techniques from Anthropic's official prompt-engineering docs |
| Model fit | Model-agnostic (frameworks are universal) | Claude-specific (prefill, extended thinking, XML idioms) |
| Output | Structured prompt produced in chat, with before/after **1–10 scores** on 5 dimensions | **In-place file edit** of your source prompt + narrative summary (no files) |
| Selection aid | Decision tree + progressive clarifying Q&A, can switch frameworks mid-flow | Fixed 10-item checklist evaluated every time |
| Special coverage | Rare techniques: RPEF (recover a prompt from output), Pre-Mortem, Devil's Advocate, Reverse-Role/FATA, RCoT | Only what Anthropic documents |
| Restraint | Weaker — framework machinery can over-structure | Strong — ships examples teaching "no changes needed" and "don't over-engineer" |
| Currency | Manually versioned | Self-syncing doc-fetcher against live Anthropic docs |

## When does prompt-architect win?

- **You're on a non-Claude model** (e.g. pi). improve-prompt leans on Claude-API features (prefill `{`, extended thinking, role in the `system` parameter); its advice is translatable effort on other models. prompt-architect is designed to be model-agnostic.
- **The prompt is a pasted-in-chat intention.** Its progressive Q&A interviews you, picks a framework, returns a clean structured prompt — zero friction. improve-prompt's automated scripts want a *file path* and force a temp-file detour for chat pastes.
- **The task is unusual.** Only prompt-architect can reach for Reverse Prompt Engineering, Pre-Mortem, or Devil's Advocate. Improve-prompt has nothing for jobs outside Anthropic's doc set.
- **You want measurable proof.** The 5-dimension 1–10 score gives a tangible before/after. improve-prompt gives reasoning + confidence — more honest, but not quantifiable.

## When does improve-prompt win?

- **The prompt lives in a codebase.** If system prompts, templates, or LLM calls live in `prompts/`, YAML, or Python strings, improve-prompt reads the file and writes the edit back in place, preserving quoting and escaping. That beats copying prompt-architect's chat output into the file yourself. Its home turf: "improve the prompt in `prompts/system.txt`."
- **You're shipping to Claude specifically.** Its checklist rules (prefill to force JSON, 3-level CoT with mandated output-reasoning, 20K-token document placement) come straight from current Anthropic docs and are kept current by its fetcher.
- **You want the agent to NOT inflate the prompt.** Its "already good → no changes" and "over-engineering warning" examples are an actual quality bar. For one-line tasks ("translate this to Spanish") prompt-architect's machinery can produce a monster; improve-prompt's constraints keep it a one-liner.

## Where the evidence is weak

- **The scores are vibes, not benchmarks.** prompt-architect's 8.8/10 is self-assessed, not a measured result. Trust it as a narrative device, not a measurement.
- **"Claude-optimized" cuts both ways.** Neither skill is validated on pi/mixed models; the frameworks are universal in principle, but the *defaults* (XML structure, phrasing) favor Claude's style. Expect to translate output on other models.
- **Not evaluated empirically against each other here.** These win/lose rules come from reading both SKILL.md files + the tool landscape (christabone, Agensi), not from A/B tests on real prompts.

## Next-step decision

1. Prompt is a chat paste or unknown model → **prompt-architect**.
2. Prompt is embedded in a file in this repo → **improve-prompt** (regardless of model).
3. Prompt will ship to a Claude API/system prompt → **improve-prompt** aggress.
4. Prompt needs an unusual technique (recover/reverse/stress-test) → **prompt-architect**.
5. Prompt is trivial and you're worried about bloat → **improve-prompt** restrains better.
6. Neither fits (you're building production LLM apps needing JSON schemas, injection defense, RAG) → that's a different job class; Agensi's `prompt-engineer` type skill, not these two.

## Sources

- ckelsoe/prompt-architect README + installed `SKILL.md` (v3.5.1)
- christabone/claude-prompt-improvement SKILL.md, CHECKLIST.md, scripts (read in-session, 2026-08-18)
- Agentskills / skills.sh / mcpmarket listings for adjacent prompt skills (2026-08-18)

---
**Source:** session 2026-08-18 (prompt-skill comparison)
**Last reviewed:** 2026-08-18
**Related:** none
