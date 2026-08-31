# Wave 08 — Phase 2 Deep-dive

**Wave goal:** deep-dive for the roster; every shortlisted creator gets `case-studies/<slug>.md` that passes the depth gate (every workflow step ≥1 first-party source link; every claim linked; verified-vs-claimed + caveats + contradictions explicit). Exit: each doc is DEPTH-PASS or THIN-with-explicit-gap per the Shallow-output protocol.

**Phase:** 2. Inputs: `working/shortlist.md` entries + `working/MANIFEST.md`. Phase 2 does NOT re-verify — verification is settled in Phase 1.

**Roster (one worker per creator, parallel):**
1. veritasium — Derek Muller — shortlist rank #4
2. drew-gooden — Drew Gooden — shortlist rank #5
3. kurtis-conner — Kurtis Conner — shortlist rank #6
4. johnny-harris — Johnny Harris — shortlist rank #7

**WORKER TYPE:** `b0tts-general-agent` (has shell; `b0tts-researcher` lacks shell — do not use it)

**Per-worker task prompt (verbatim for every worker, fill in NAME + slug):**

> You are a Phase 2 deep-dive researcher (b0tts-general-agent — you HAVE shell). Your creator: **NAME — slug**. First read their entry in `working/shortlist.md` (it lists documentation sources and the best starting source). Read their first-party documentation end to end: strategy videos via the `youtube-transcript` skill (load the skill, read its SKILL.md first; transcripts go to `b0ttsagent/temp/youtube-transcripts/`; sample most-recent-first, older videos only after the recent record is captured; if bare `yt-dlp` fails use `python -m yt_dlp`), blogs, podcasts, interviews, course summaries. Paid content: only publicly readable summaries — never fabricate from marketing copy, never ask anyone to pay. Write `case-studies/<slug>.md` in the creator's own terms — no imposed schema; cover what THEY document (open/hook, structure, pacing, retention, editing rhythm, cadence, replication without burnout) and skip what they don't. Every workflow step ≥1 first-party source link; every claim linked; verified-vs-claimed + caveats + contradictions explicit. Sources thin → say so explicitly and stop; never pad. Final message ≤250 words: DEPTH-PASS or THIN + path + one-line reason. Never paste doc content into your final message.

**Completion criteria:** one `case-studies/<slug>.md` per roster entry, each verdict DEPTH-PASS or THIN-with-explicit-gap

**Lead QA checklist (each wave):**
- [ ] every expected `case-studies/<slug>.md` exists
- [ ] every workflow step carries a source link (spot-grep the file for link density per section; a step with no link → flag for re-run)
- [ ] THIN verdicts carry explicit gap statements, not padded prose
- [ ] doc count in report matches files on disk
- [ ] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN

**Lead output:** `working/waves/report-08.md` — per-worker status (done / fail / retried), verdicts, anomalies, next actions. Lead final message ≤500 words: status, file paths, verdicts, next actions. Never paste file contents.

**Context budget:** workers → disk only, ≤250-word finals. Lead reads only this spec + worker summaries. Never read full case studies or evidence JSONs into context.
