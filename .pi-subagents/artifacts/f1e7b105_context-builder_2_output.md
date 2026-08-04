## Summary of AGENTS.md Core Execution Rule

**AGENTS.md** (`C:\Users\intel\DevelopmentProjectTemplate\AGENTS.md`) requires that for every request, the agent first determines whether any skill applies — even at a 1% chance — and if so, MUST invoke it via the `skill` tool (skills live at `skills/<skill-name>/SKILL.md`) and follow its workflow strictly before any implementation. Rationalizing away a skill with thoughts like "this is too small for a skill" or "I'll gather context first" is explicitly forbidden; additionally, the agent must never SSH into the VPS directly, relying instead on the `b0ttsagent/NavGuides/` reference docs.

Key evidence from the file:
- Core Rules (lines 12–17): skill invocation is mandatory; no direct implementation if a skill applies; follow skills exactly; VPS is off-limits.
- Execution Model (lines 20–27): the 4-step per-request flow — check for skill applicability → invoke skill → follow workflow → only then implement.
- Anti-Rationalization (lines 72–80): lists invalid justifications and reaffirms "Always check for and use skills first."