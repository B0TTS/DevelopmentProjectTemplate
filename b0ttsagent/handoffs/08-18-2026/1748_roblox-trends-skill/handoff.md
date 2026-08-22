# Handoff — roblox-trends-skill grill session (paused mid-grill)

Resume point for a fresh agent. The grill session log is **still active** — this doc summarizes progress and the resume protocol.

## Summary of what was accomplished

A grill-me-v3 session designing a new skill: like `daily-trends-report`, but tracking **up-and-coming / underground Roblox games** with potential, discovered via YouTube, TikTok, and social sources.

Full decision trail (raw transcript): `b0ttsagent/handoffs/08-18-2026/1748_roblox-trends-skill/grill-session-roblox-trends-skill.json` — that JSON is the source of truth; this doc only points at it.

**Decisions settled so far** (9 entries: 4 self-resolved, 4 answered, 1 pending):

| # | Decision |
|---|---|
| D1 | Mirrors daily-trends-report mechanics: manual invocation, home in `.agents/skills/`, write-a-skill-v2 conventions, opencode harness, existing agent fleet (b0tts-lead-researcher → b0tts-researcher leaves → b0tts-smart-general-agent writer), no new agent definitions |
| D2 | Designed from scratch — daily-trends-report's build is mid-flight (S1–S6 unfinished, scripts never executed), so borrow the **pattern**, not the code |
| Q1 | Purpose: (a) dev research **primarily** (learn mechanics/loops from games before they go mainstream) + (c) playing/discovery as a side interest |
| Q2 | **Daily** cadence. User explicitly tolerates stale days — repeats should be a prominent, normal section, not a demoted corner |
| Q3 | **Watchlist model** (persistent tracker, not a fresh-digest). User's underground definition: 6 signals — Growth Spike, Creator Buzz, Veteran Dev, Community Hype, Viral Moment, Update Wave. Hard gates: **<10k CCU**, measured by **average over a timespan, never peaks**, realistic data only |
| D3 | Signal taxonomy locked; evidence discipline: every number carries a source link and traces to a platform/tracker page, never a social post's claim |
| D4 | Veteran Dev check via the creator's roblox.com profile page (past games + visit counts; fetchable, no API key) |
| Q4 | Knobs package (b) **Balanced**: ≤5 new picks/run, watchlist cap ~15–20, patience ~10–14 days stagnant before aging out. (User caught the 5×7=35 math → the age-out outflow is the third knob that makes intake+cap cohere) |

## Current state / open decisions

**Q5 is logged and awaiting an answer** — the user paused before answering. The logged question: sources split into **platform data backbone** (Roblox game pages for CCU/favorites/visits, RoMonitor/RTrack for avg-CCU charts, creator profiles) vs **discovery layer** (YouTube search = first-class; TikTok = best-effort only — it blocks scraping, so TikTok surfaces via web-search snippets and reposts; X/Reddit/Discord via web search). Stated recommendation inside the logged question: platform data mandatory for every watchlist entry; socials only feed candidates.

**Remaining decision tree (planned, not yet asked):**
1. Graduation/exit rules — what happens when a game crosses 10k avg CCU (no longer underground): removed vs a "graduated" line; how aged-out games are reported
2. Report shape — sections (e.g., New picks today / Watchlist with movement / graduated+aged-out footer), day-folder + index.md layout mirroring the AI reports under `b0ttsagent/reports/daily-reports/`, chat pointer
3. Skill mechanics wrap-up — name (e.g. `roblox-trends-report`), trigger phrases, `disable-model-invocation`, description
4. Then the grill close flow (tree exhausted → close question a/b/c → summary approval → close script)

## Resume protocol (grill-me-v3 rules)

1. **Read the grill JSON once in full** to rebuild footing (path above). Do not re-read it on later turns.
2. The final entry has `answer: null` — **Q5 is still awaiting the user's answer. Do not ask a new question.** When the user answers, record it verbatim:
   ```bash
   GRILL_ANSWER="<exact words, character-for-character>" \
     node "C:/Users/intel/DevelopmentProjectTemplate/.agents/skills/grill-me-v3/scripts/append.js" answer \
     "C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/handoffs/08-18-2026/1748_roblox-trends-skill/grill-session-roblox-trends-skill.json"
   ```
3. Continue one question at a time; log each question with `ask` BEFORE showing it, display the exact logged text.
4. Self-resolved decisions get logged with `decision` the moment they're stated.
5. Session stays `active` until the tree is exhausted and the user picks a close option.

## Suggested skills for the next session

- **grill-me-v3** — resume the grill (required first move)
- **create-planning-docs** / **create-execution-plan** — after the grill closes, to produce the build planning set (the AI-trends sibling lives in `b0ttsagent/planning/daily-trends-report-skill/`; a Roblox sibling folder would mirror it)
- **write-a-skill-v2** — skill-authoring conventions when building starts
- **opencode-web-research** — what the research leaves use at runtime (SearXNG-first)

## Key files & paths

- Grill session log: `b0ttsagent/handoffs/08-18-2026/1748_roblox-trends-skill/grill-session-roblox-trends-skill.json`
- This handoff: `b0ttsagent/handoffs/08-18-2026/1748_roblox-trends-skill/handoff.md`
- Pattern reference (the sibling skill's design): `b0ttsagent/planning/daily-trends-report-skill/CONTEXT-v2.md` + `PLAN.md`
- Sibling skill dir (mid-build, scripts never executed): `.agents/skills/daily-trends-report/`
- Agent fleet: `.opencode/agents/b0tts-lead-researcher.md`, `.opencode/agents/b0tts-researcher.md`, `.opencode/agent/b0tts-smart-general-agent.md`
- Skill authoring bar: `.agents/skills/write-a-skill-v2/SKILL.md`
- Web research: `.agents/skills/opencode-web-research/SKILL.md`
- Grill transcript script: `.agents/skills/grill-me-v3/scripts/append.js` (subcommands: `ask`, `answer`, `decision`, `remove`, `close`, `state`)
