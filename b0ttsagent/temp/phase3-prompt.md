# Phase 3 Session Prompt — Viral Lyric Workflow Research (Session 8, final phase)

You are resuming the viral-lyric-workflow research project at its final phase. Phases 0–2 are complete. Your entire job this session is **Phase 3 — Compilation & QA**, main agent only, no sub-agents, no new research. Run to the exit gate, then stop.

## Read first (in full)

1. `b0ttsagent/planning/viral-lyric-workflows/PLAN.md` — session model + Phase 3 spec (3.1–3.4) + all wave QA notes (verification-strength signals live here)
2. `b0ttsagent/planning/viral-lyric-workflows/CONTEXT.md` — mission, OUTPUT spec, VERIFICATION PROCEDURES
3. `b0ttsagent/research/viral-lyric-workflows/SYNTHESIS.md` — Phase 2 output incl. weighting caveats for INDEX
4. All 14 files in `b0ttsagent/research/viral-lyric-workflows/creators/` — your raw material for 3.1 and 3.4
5. `b0ttsagent/research/viral-lyric-workflows/REJECTED.md` — current state: Porter Robinson (W5) logged with reason + numbers
6. `b0ttsagent/temp/lyric-pool.md` — pool/shortlist history (Deferred table, backfill candidates) for REJECTED.md final pass context

## State at session start

- 28 pool → 24 shortlist → 15 dispatched → **14 verified** (tier 1 artists only; no tier 2/3 in verified set), 1 rejected (Porter Robinson). Target was ≥10 — **met, no shortfall statement needed in INDEX**.
- Existing outputs: `creators/*.md` (14, 6-section skeleton), `SYNTHESIS.md`, `REJECTED.md` (partial). Missing: `INDEX.md`, `SOURCES.md`.

## Tasks (PLAN 3.1–3.4)

### 3.1 INDEX.md — write it

All 14 verified creators, ranked by **(1) verification strength, then (2) depth of process documentation**. Per creator: verification status, platform, 1–2 line summary.

Verification-strength inputs (derive ordering from creator docs' Section 1 + these signals, don't just eyeball):

- **Clean strong passes with margin:** Russ (30/30 in-window ≥100k), Charlie Puth (7 releases + 9 visualizers, 123M audience), Lizzo (17 releases, 17.5M audience), J. Cole (album era, 21M+ Port Antonio), Laufey (30+ uploads ≥100k incl. 42.8M Lover Girl), Olivia Dean (107M Man I Need), Raye (146M WIMH), AJR, Jack Harlow, Denzel Curry, Logic, Gracie Abrams.
- **Weak/boundary passes — rank lower:** Billie Eilish (boundary case: only 2 clean NEW commercial releases in-window; pass rests on 12 in-window official uploads incl. Isolated Vocals), Tessa Violet (thinnest margin: 3 releases just above 100k — 182.9k/146.9k/122.8k; her own quote "I haven't had a success like that since 'Crush'").
- **Monthly-audience gaps (recorded, not blocking):** Denzel Curry, Laufey, Olivia Dean, Russ (consent wall), Logic. Extractable for: Puth 123M, Billie 366M, Harlow 28.7M, AJR 99M, Lizzo 17.5M, Gracie 91M, Raye 66.4M, Tessa 1.93M, J. Cole gap.
- **Doc-depth signals:** who has anchor sources (Song Exploder episodes: Billie, Denzel, Lizzo, Laufey, Gracie, Raye, Harlow; Genius Verified: Puth, Logic, Denzel; full documentaries: Logic, J. Cole; own course: Puth, Lizzo-MWTM) vs thinner docs (no Song Exploder for Tessa, Olivia, AJR, Russ, Logic, J. Cole — noted gaps in their docs).
- PLAN W5 QA note says Phase 3 INDEX weighting should reflect Tessa's weaker verification strength.

### 3.2 SOURCES.md — write it

Every link used, per creator, with access dates. Consolidate from each creator doc's Section 6 + Section 1 links. Access date: **2026-08-13** (every doc states it). Include per-doc local scratch-JSON references where docs cite them (`b0ttsagent/temp/lyricscreen/*`). Keep grouped by creator, mirroring the docs' source lists — do not drop links the docs cite.

### 3.3 REJECTED.md — final pass

Current file already has the Porter Robinson entry (correct, keep it). Final pass duties:

- Verify the one rejection is complete with reason + observed numbers (it is — check against PLAN W5 QA note).
- Decide how to represent Phase-0 deferred (7: Lorde, Dua Lipa, Sabrina Carpenter, Lady Gaga, Jason Blume, Ed Bell, Cole Mize) and backfill-never-dispached candidates (shortlist 16–24 + pool remainder: Shinoda, Bellion, Maggie Rogers, Toby Gad, Ross Golan, ADORA, Nicolle Galyon, Ryan S. Jhun, Brent Baxter, mgk, Hanumankind, San Holo, HALIENE). These were cut, NOT failed verification. Recommendation: add a clearly-labeled "Deferred at Phase 0 — never verified" section so failure vs not-attempted stays honest; do NOT fold them into the failed list (CONTEXT forbids padding).
- Update the header status line to reflect Phase 3 final state.

### 3.4 Traceability sweep — run it, fix what fails

Every claim in every output must trace to a cited source link. Procedure:

1. Walk all 14 creator docs: each claim in Sections 1–5 must trace to a link in Section 6 (or an inline link). Flag claims lacking a trace.
2. Walk SYNTHESIS.md: every matrix cell and ranked-list/diverge claim must resolve to at least one creator doc (which itself carries the link). If a SYNTHESIS claim can't be matched to a doc, fix or cut it.
3. INDEX.md and SOURCES.md are compilations — verify they don't introduce new claims beyond the docs.
4. Fix flagged issues by editing the offending doc (trim the claim or add the citation from that doc's own evidence). If a fix would require NEW external research, don't research — cut the claim and note the cut in the doc.
5. Verification commands are only for re-checking an existing number whose evidence looks broken; use CONTEXT VERIFICATION PROCEDURES exactly (hand-verified commands, `1> file.json 2> file_err.txt`). Do not verify anything new.

### Exit gate — all of:

- [ ] `INDEX.md` exists: 14 creators ranked by verification strength then doc depth, each with status/platform/1–2 line summary
- [ ] `SOURCES.md` exists: every link per creator, access dates
- [ ] `REJECTED.md` final: 1 failure logged with reason+numbers; deferred section clearly separated
- [ ] Sweep pass: every claim traces to a cited link; no guesses
- [ ] `creators/` (14), `SYNTHESIS.md`, `INDEX.md`, `SOURCES.md`, `REJECTED.md` — all 5 outputs present
- [ ] Update `PLAN.md` Phase 3 checkboxes + sequencing table (this is the last phase — mark project complete after the gate)

## Session rules

- Main agent only. No sub-agent dispatch. No new creator research.
- Skill: `markdown-doc-designs` applies silently (auto mode) while writing INDEX.md/SOURCES.md.
- No web research needed this session — everything is on disk. If you must re-verify a number, shell commands per CONTEXT VERIFICATION PROCEDURES only.
- Stop at the exit gate. Report completion + the final verified count. Do not start anything beyond Phase 3.
