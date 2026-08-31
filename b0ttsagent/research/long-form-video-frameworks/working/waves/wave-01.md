# Wave 01 — Phase 0 Discovery

**Wave goal:** produce `working/candidates.md` with ≥20 unique, schema-complete candidates — creators of edited long-form YouTube videos (10–30 min: video essays, deep dives, explainers, documentary-style, storytelling, edited commentary-comedy) who have **publicly documented their own workflows** (2021–2026 sources). Excluded formats: podcasts, livestreams, let's-plays/walkthroughs, raw vlogs, music videos, compilations/reactions, news. English-language documentation only.

**Roster:** 3 b0tts-researcher agents, one per discovery lane (partitioned by evidence type):
- **Lane A — Course/blog authors:** creators who published written frameworks (blogs, course summaries, Substacks, public deck breakdowns).
- **Lane B — Podcast/interview circuit regulars:** creators whose process is documented across public podcasts/interviews.
- **Lane C — Channel strategy-video creators:** creators who film their own "how I make my videos" breakdowns on their channel.

**HARD SPAWN RULE — read before anything else:** You spawn researchers by making **parallel `task` tool calls** — three Task-tool invocations with `subagent_type: "b0tts-researcher"`, all in ONE assistant message (one response block, three tool calls). Do NOT write scripts, do NOT use bash/CLI to launch agents, do NOT use any other spawning mechanism. Task tool calls only. If the Task tool is missing from your toolset, stop immediately and say so in your final message — do not improvise an alternative.

**Per-researcher task prompt** (give each verbatim, filling in their lane):

> You are a discovery researcher (Phase 0) for a study of long-form video creators with deeply documented workflows. Your lane: [LANE NAME — lane description]. Target format: edited YouTube long-form (10–30 min; video essays, deep dives, explainers, documentary-style, storytelling, edited commentary-comedy). Exclude podcasts, livestreams, let's-plays, raw vlogs, music, compilations/reactions, news. Only creators who plausibly pass a strict bar: verified or long public career, consistent 100k+ views per video (prefer 1m+ median; 10m+/video anchors ranked highest), hits within 2021–2026, and public 2021–2026 documentation of their actual workflow. English documentation only.
>
> Return up to 15 candidates — fewer if that's all that's strong; never pad. Write `working/candidates-lane-X.md` (X = A/B/C) using EXACTLY this row schema, one line per candidate:
> `- **Name (handle)** — niche/format: … — verification lead: <url> — channel: <url> — first-party doc: <url> — notes: …`
> Notes: flag uncertainty honestly (e.g. `role unconfirmed`, `doc URL looks like a listicle`, `SECOND-HAND-only`). Every row needs a verification-lead URL, a channel URL, and ≥1 first-party doc URL that looks like it contains their actual process.
>
> Tooling: use `websearch` as primary search (SearXNG MCP often returns empty — try once, move on). Load the `opencode-web-research` skill for guidance. Read a page before citing it — snippets are discovery, not evidence. Do NOT run verification or view-count tests — that is Phase 1.
>
> Final message ≤250 words: candidate count, file path, your 3 strongest names. Never paste doc content into the final message.

**Completion criteria:** after fanout completes, lead merges the three lane files into `working/candidates.md` (dedupe by handle; keep strongest row on collision), target ≥20 unique rows, ≥4 from each lane. If a lane returned <7 or rows miss fields, re-run that one lane with a targeted prompt once before declaring done.

**Lead QA checklist:**
- [ ] dedup done (no duplicate handles in candidates.md)
- [ ] every row has verification-lead URL + channel URL + first-party doc URL
- [ ] no lane contributed <4 final candidates (after retry if needed)
- [ ] weak rows flagged with `?` or `SECOND-HAND-only` for Phase 1 scrutiny
- [ ] common-name collisions disambiguated (product/channel in row)

**Lead output:** `working/waves/report-01.md` — per-researcher status (lane, count, verdict), dedup notes, anomalies, next actions. Lead final message ≤500 words.

**Context budget (enforced):** researchers write full work to disk only, final message ≤250 words. Lead reads only the wave spec + researcher summaries + the three lane files (needed for the merge — they are ≤15 rows each). Never read external docs into context.

**Mandatory researcher-spawn method (repeated because it has failed before):** the ONLY way you spawn the 3 researchers is three `task` tool calls in one assistant message, `subagent_type` = `b0tts-researcher`. Never write a script, never use bash, never launch external processes. Your final report must state that all 3 task calls returned and their verdicts.
