# Phase 2 Master Plan — Deep-dive waves (executed by the Phase 2 orchestrator, a b0tts-general-agent)

**Phase goal:** every shortlisted creator gets `case-studies/<slug>.md` that passes the depth gate. Exit: 15 case studies on disk, each DEPTH-PASS or logged-thin per the Shallow-output protocol.

**Inputs:** `working/shortlist.md` (15 ranked entries; each carries the best starting source) + `working/MANIFEST.md`. Phase 2 does NOT re-verify — verification is settled in Phase 1.

**Wave roster (execute in this order, strictly sequential):**

| Wave | Creators (slug — name) |
|---|---|
| 07 | mrbeast — MrBeast · mark-rober — Mark Rober · airrack — Airrack/Eric Decker |
| 08 | veritasium — Derek Muller · drew-gooden — Drew Gooden · kurtis-conner — Kurtis Conner · johnny-harris — Johnny Harris |
| 09 | mkbhd — Marques Brownlee · linus-tech-tips — Linus Sebastian · wendover-productions — Sam Denby · tom-scott — Tom Scott |
| 10 | mina-le — Mina Le · ryan-trahan — Ryan Trahan · colin-and-samir — Colin and Samir · matt-davella — Matt D'Avella |

**Orchestration rules (for you, the Phase 2 orchestrator):**

1. One wave at a time, strictly in order. For each wave: write `working/waves/wave-0N.md` (from the template below, roster filled in), then spawn ONE `b0tts-lead-researcher` for that wave. Block until it returns. Only then start the next wave.
2. Lead prompt (adapt roster + wave number): "You are Wave N lead. Read `working/waves/wave-0N.md` and execute it exactly. Spawn all deep-dive workers in ONE message (parallel fanout), worker type `b0tts-general-agent`. Wait for all workers. Read each worker's final message only. Run the Lead QA checklist. Write `working/waves/report-0N.md`. Final message ≤500 words."
3. After each wave returns: QA-gate on disk (every expected `case-studies/<slug>.md` exists; DEPTH-PASS/THIN verdicts match the report), then append one MANIFEST line: `Wave NN | Phase 2 Deep-dive | OK/<issues> | per-creator verdicts | next: wave NN+1`.
4. Shallow-output protocol (if a worker returns THIN): have that wave's lead re-spawn that creator's worker ONCE with a different angle prompt (new source trail, different framing). If still THIN, accept the doc only if it states the gap explicitly (downgraded evidence tier or "documentation insufficient") — never padded prose, never invented steps.
5. Failure handling: lead dies mid-wave → re-spawn fresh with "resume from working/MANIFEST.md". Worker FAIL-UNKNOWN → retry once with same spec; second failure → record FAIL-UNKNOWN and move on.
6. YOUR context budget: never read case studies or evidence JSONs into your context. QA via file-existence checks + grep (e.g., check each case study contains `http` links; count files). Work from lead summaries only.
7. If you die mid-phase, the orchestrator re-spawns you with "resume from working/MANIFEST.md".

**Wave spec template (what each wave-0N.md contains):**
- Wave goal (deep-dive for the roster; depth gate definition)
- Phase: 2. Inputs: `working/shortlist.md` entries + `working/MANIFEST.md`.
- Roster: slug — name — shortlist rank, one per worker
- WORKER TYPE: `b0tts-general-agent` (has shell; b0tts-researcher lacks shell)
- Per-worker task prompt (verbatim, below)
- Completion criteria: one `case-studies/<slug>.md` per roster entry, each verdict DEPTH-PASS or THIN-with-explicit-gap
- Lead QA checklist + Lead output `working/waves/report-0N.md`

**Per-worker task prompt (verbatim for every worker, fill in NAME + slug):**

> You are a Phase 2 deep-dive researcher (b0tts-general-agent — you HAVE shell). Your creator: **NAME — slug**. First read their entry in `working/shortlist.md` (it lists documentation sources and the best starting source). Read their first-party documentation end to end: strategy videos via the `youtube-transcript` skill (load the skill, read its SKILL.md first; transcripts go to `b0ttsagent/temp/youtube-transcripts/`; sample most-recent-first, older videos only after the recent record is captured; if bare `yt-dlp` fails use `python -m yt_dlp`), blogs, podcasts, interviews, course summaries. Paid content: only publicly readable summaries — never fabricate from marketing copy, never ask anyone to pay. Write `case-studies/<slug>.md` in the creator's own terms — no imposed schema; cover what THEY document (open/hook, structure, pacing, retention, editing rhythm, cadence, replication without burnout) and skip what they don't. Every workflow step ≥1 first-party source link; every claim linked; verified-vs-claimed + caveats + contradictions explicit. Sources thin → say so explicitly and stop; never pad. Final message ≤250 words: DEPTH-PASS or THIN + path + one-line reason. Never paste doc content into your final message.

**Lead QA checklist (each wave):**
- [ ] every expected `case-studies/<slug>.md` exists
- [ ] every workflow step carries a source link (spot-grep the file for link density per section; a step with no link → flag for re-run)
- [ ] THIN verdicts carry explicit gap statements, not padded prose
- [ ] doc count in report matches files on disk
- [ ] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN

**Phase-level QA (you, before reporting back):** 15 case studies exist; each has ≥2 first-party source links (or explicit thin-sources caveat); MANIFEST has one line per wave (07–10).

**Final report to the orchestrator:** ≤800 words — per wave: lead verdicts, DEPTH-PASS/THIN per creator, anomalies; total counts; MANIFEST status. Never paste doc content.
