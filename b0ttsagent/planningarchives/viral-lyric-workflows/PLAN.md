# PLAN — Viral Lyric Workflow Research

What/why: `b0ttsagent/planning/viral-lyric-workflows/CONTEXT.md` (mission, eligibility gates, verification procedures, output spec). This doc is the how only.

## Session Model

- One phase per session; **Phase 1 spans 5 sessions — one wave per session.** Run each session to its wave exit gate, then **stop**. No session logging, no handoff docs, no resume scaffolding.
- A new session begins by reading this PLAN + CONTEXT.md + prior outputs on disk (`creators/*.md`, `REJECTED.md`).

## Technical Context

| Item | Value |
|---|---|
| Environment | Windows PowerShell 5.1; yt-dlp 2026.07.04 on PATH; curl.exe 8.21.0; Discogs token in CONTEXT.md |
| Web research | opencode-web-research skill (SearXNG-first), per CONTEXT ORCHESTRATION |
| Sub-agents | b0tts-researcher (web discovery/reading), general (multi-step deep dives); shell access confirmed — sub-agents own verification (0.2 probe) |
| Verification | CONTEXT.md VERIFICATION PROCEDURES — hand-verified commands, `1> file.json 2> file_err.txt` only |
| Output | `b0ttsagent/research/viral-lyric-workflows/` (INDEX.md, creators/, SYNTHESIS.md, SOURCES.md, REJECTED.md) |
| Scale | 28 pool → 24 shortlist → 15 targeted (ranks 1–15) → ≥10 verified creators |
| Constraints | Public sources only; every claim cited; never pad with unverified names |
| Clarified (0.1) | Primary genres Pop + Hip-Hop/Rap (others secondary); target 10 verified; ~20–30 min per candidate |
| Phase 0 carry-overs | flat-playlist `timestamp` EMPTY on yt-dlp 2026.07.04 → 24-month cadence via `yt-dlp -J --playlist-items 1-30 "<channel>/videos"`; corrected channels: Lizzo = UCXVMHu5xDH1oOfUGvaLyjGg, J. Cole = UCnc6db-y3IU7CkT_yeVXdVg (@JCole; W1 QA disproved pool's UCnzJFckvQBA5nn9lMu08LWQ = JColeVEVO, inactive since 2019, and @JColeNC = renamed fan channel); Tier-2 eligibility via credits (Discogs/ASCAP/Genius), not own listener numbers |

## Phase 0 — Discovery & Screening (Session 1) — COMPLETE

Exit gate passed 2026-08-13. See `b0ttsagent/temp/lyric-pool.md`: 28 pool, 24 shortlisted, probe verdict (sub-agents own verification: YES), 0.1 answers. Raw cheap-screening JSON in `b0ttsagent/temp/lyricscreen/`.

## Phase 1 — Verification & Deep Dives (Sessions 2–6: 5 waves × 3 creators)

Target: shortlist ranks 1–15, one wave per session, 3 parallel sub-agents per wave.

- [ ] **1.0 Prompt template (Session 2, before W1)** — per-creator sub-agent prompt: verify numbers/credits FIRST (sub-agents own verification — CONTEXT VERIFICATION PROCEDURES), then workflow research via opencode-web-research skill (SearXNG-first) across YouTube transcripts/blogs/podcasts/courses. Output `creators/<name>.md` on the 6-section skeleton (CONTEXT OUTPUT spec). Tier-2 creators: verify via credits, not own listener numbers. Cadence dates: dated listing command only — flat-playlist timestamps are empty on this build.
- [ ] **1.0b Orchestrator duty (every wave)** — every sub-agent brief MUST instruct the sub-agent to load/activate the `opencode-web-research` skill.
- [ ] **1.1 Wave dispatch `[P]`** — 3 parallel deep-dive sub-agents per session, one creator per agent, shortlist rank order:

| Wave | Session | Creators (shortlist rank) |
|---|---|---|
| W1 | 2 | Russ (1), Logic (2), J. Cole (3) |
| W2 | 3 | Charlie Puth (4), Billie Eilish (5), Jack Harlow (6) |
| W3 | 4 | AJR (7), Denzel Curry (8), Lizzo (9) |
| W4 | 5 | Laufey (10), Gracie Abrams (11), Raye (12) |
| W5 | 6 | Tessa Violet (13), Olivia Dean (14), Porter Robinson (15) |

- [ ] **1.2 Reap & QA (end of every wave)** — main agent spot-checks each returned doc's numbers (re-run key commands where evidence looks thin), files passing docs, logs failures with reasons to `REJECTED.md`. Next wave's briefs incorporate prior waves' rejection learnings.
- [ ] **1.3 Backfill policy** — after each wave, if (verified so far + remaining planned) < 10, promote backfill candidates into free slots of remaining waves. Order: shortlist ranks 16–24 (Shinoda, Bellion, Maggie Rogers, Toby Gad, Ross Golan, ADORA, Nicolle Galyon, Ryan S. Jhun, Brent Baxter), then pool remainder (mgk, Hanumankind, San Holo, HALIENE). No extra wave beyond W5.
- [ ] **1.4 Shortfall path** — if <10 after W5, stop and state the shortfall (CONTEXT failure path).

**Exit gate (stop after W5):** ≥10 verified creators with complete 6-section docs in `creators/`; every failed candidate logged in `REJECTED.md` with reason. If <10 after shortlist exhausted, stop anyway and state the shortfall.

### Phase 1 Wave Tracking

Check Dispatch + Reap & QA + Backfill check off per wave as you go. Running verified count: **14/10** (W1: Russ, Logic, J. Cole; W2: Charlie Puth, Billie Eilish, Jack Harlow; W3: AJR, Denzel Curry, Lizzo; W4: Laufey, Gracie Abrams, Raye; W5: Tessa Violet, Olivia Dean — all passed; W5 rejection: Porter Robinson, cadence gate failed, logged in REJECTED.md. QA re-ran dated listings + single-video channel checks + monthly-audience extraction + citation HEAD checks, all matched).

| Wave | Creators | Dispatch | Reap & QA | Backfill check |
|---|---|---|---|---|
| W1 | Russ, Logic, J. Cole | [x] | [x] | [x] |
| W2 | Charlie Puth, Billie Eilish, Jack Harlow | [x] | [x] | [x] |
| W3 | AJR, Denzel Curry, Lizzo | [x] | [x] | [x] |
| W4 | Laufey, Gracie Abrams, Raye | [x] | [x] | [x] |
| W5 | Tessa Violet, Olivia Dean, Porter Robinson | [x] | [x] | [x] |

**W1 backfill check:** 3 verified + 12 remaining planned = 15 ≥ 10 — no backfill promotion needed yet. (If a later wave fails ≥4 creators, promote: shortlist 16–24 → Shinoda, Bellion, Maggie Rogers, Toby Gad, Ross Golan, ADORA, Nicolle Galyon, Ryan S. Jhun, Brent Baxter; then pool remainder → mgk, Hanumankind, San Holo, HALIENE.)

**W2 backfill check:** 6 verified + 9 remaining planned (W3–W5) = 15 ≥ 10 — no backfill promotion needed. (Failure threshold unchanged: promote only if a later wave drops ≥4 total.)

**W3 backfill check:** 9 verified + 6 remaining planned (W4–W5) = 15 ≥ 10 — no backfill promotion needed. Only 1 more verified creator is required to hit the 10 target. The edge case is binary: W4 and W5 are the last two waves, so backfill promotion is impossible anyway (1.3 promotes into free wave slots only). If both waves somehow produced zero verified creators, the count would sit at 9 and the 1.4 shortfall statement would cover it — no promotion action is available or warranted now. Backfill candidates (shortlist 16–24, then pool remainder) stay untouched unless the user reopens a wave.

**W4 backfill check:** 12 verified + 3 remaining planned (W5) = 15 ≥ 10 — target already exceeded, no backfill promotion needed. W5 (Tessa Violet, Olivia Dean, Porter Robinson) runs as planned; shortlist ranks 16–24 (Shinoda, Bellion, Maggie Rogers, Toby Gad, Ross Golan, ADORA, Nicolle Galyon, Ryan S. Jhun, Brent Baxter) and pool remainder (mgk, Hanumankind, San Holo, HALIENE) stay untouched. The 1.3 backfill policy is now moot — 1.4 shortfall path can only trigger if W5 drops all 3 AND the 12 current docs were somehow revoked.

**W5 backfill check:** 14 verified (W5 added Tessa Violet, Olivia Dean; Porter Robinson rejected) ≥ 10 target — **target exceeded by 4; no backfill promotion needed; 1.3 policy moot; 1.4 shortfall path cannot trigger** (14 verified, only 1 rejection). Shortlist ranks 16–24 and pool remainder stay untouched. Phase 1 complete — all 5 waves dispatched, reaped, and QA'd.

**W5 QA note (first rejection of the phase, recorded):** Porter Robinson failed the Consistency Test — only 1 official in-window release ≥100k on his own channel (Year of the Cup, 2024-08-22, 590,901; Hollowheart 2024-08-12 is 1 day outside the window; SMILE! :D era MVs/audios all Mar–Jul 2024, pre-window; zero uploads since 2024-08-22; VEVO channel stale since 2015; no official SoundCloud; WannaCry 2026 collab sits on Ninajirachi's channel). Pool hypothesis mis-dated the Smile :D singles as in-window — lesson: verify era dates against the dated listing before assuming cadence. Other W5 learnings: (1) Olivia Dean's pool-doc channel id (UCT3cEUoL1X0_BxN6q7LVH1w) was WRONG — third pool-handle failure after J. Cole and Lizzo; verified channel is UCYKlku5Zg5FnAc3bgY7kQnA, caught because the sub-agent checked video-level channel_id; (2) pool hypothesis details were also wrong for Olivia (The Art of Loving = 2025-09-26 not 2026; Man I Need peaked Hot 100 #2 not "top-5"; Grammy = Best New Artist, 68th Grammys 2026-02-01); (3) her pool doc lead was a 47s And The Writer Is… shorts clip — the deep source is the full Ep. 226 (Ross Golan, 2025-10-27, auto-captions); (4) Tessa Violet passed with the thinnest margin of the phase — all 3 qualifying releases sit just above 100k (182.9k / 146.9k / 122.8k) and she states "I haven't had a success like that since the release of 'Crush'" — Phase 3 INDEX weighting should reflect weaker verification strength; her 1.93M monthly audience WAS extractable (re-verified in QA from escaped ytInitialData JSON); (5) both W5 sub-agents reported SearXNG general engines returning empty and fell back to built-in websearch per skill routing — noted, no action; (6) W5 zero-song-exploder gap for both passing creators (no episodes exist); (7) no caption gap issues beyond notes — both docs cited auto-captions where used.

**Phase 1 exit gate: PASSED (2026-08-13).** 14 verified creators ≥ 10 target with complete 6-section docs in `creators/`; the single failed candidate (Porter Robinson) logged in REJECTED.md with reason and numbers. Phase 2 (Synthesis, Session 7) is a separate session — do not start it here.

**W4 QA note (dual-channel catch, recorded):** Gracie Abrams' artist-channel hub listing mixed TWO official channels — @gracieabrams (UCwXDwwxNVRXPcPk7ABkakdA) and the official GracieAbramsVEVO distributor channel (UCVFRVXH1hRoWkmpKCRmLMiQ, confirmed via channel-page title). MVs and lyric videos live on VEVO; live/process content (Apple Music Live, Story of My Song) on the artist channel. Accepted under the W3 Denzel Curry precedent (VEVO is an official licensed distributor channel, not fan/compilation/Topic). Doc updated with per-release channel attribution; pass also holds on the artist channel alone (Apple Music Live 13.8M + Story of My Song 527k + 3 live uploads ≥1M). W4 learnings for W5: (1) Gracie's monthly audience WAS extractable (91M — music.youtube.com HTML worked again); (2) Laufey's was NOT (HTTP 200 but no monthlyListenerCount in ytInitialData — third confirmed unextractable case, policy unchanged: record gap, never block); (3) Raye's pool-doc channel lead was CORRECT this time (UCw5z_dopYnvEL6Rc8KNKsnw), but a legacy channel UC1aQVIVnCGa4hDJtvNxf11g hosts her pre-2025 hits incl. Escapism 277M — check which channel hosts the flagship hits, the current one isn't always where the back-catalog numbers are; (4) Song Exploder transcripts remain the anchor sources (all three W4 docs used them); (5) Raye's Vevo Footnotes making-of videos have no captions — cited via secondary recaps + gap noted; (6) Music Week was registration-walled for Raye (snippet quotes only, flagged in doc); (7) W4 had zero rejections, REJECTED.md unchanged.

**W2 QA note (boundary case, recorded):** Billie Eilish passed on the inclusive reading — 12 official own-channel song uploads in-window (BOAF MV 913M, INTRO visualizer, 10 Isolated Vocals, all ≥100k; zero fan/Topic uploads used), but only 2 are clean NEW commercial releases in-window (her May-2024 album + between-album quiet period sits just outside). Accepted because the gate's disqualification clause names only fan re-uploads/compilations/Topic uploads, and her in-window viral output (913M-view MV) plainly satisfies the gate's intent. Phase 3 INDEX ranking should weight her verification strength accordingly. W2 learnings for later waves: monthly audience was extractable for all three (123M / 366M / 28.7M — try music.youtube.com HTML first, the consent-wall failure is not universal); Song Exploder transcript PDFs on songexploder.net are anchor sources with live links.

**W3 QA note (channel-attribution catch, recorded):** Denzel Curry's dated listing from the artist-channel hub (@DENZELCURRYPH) returned videos from TWO official channels — 11 of 12 in-window releases verified at video level on the artist channel (UCiKxNvM...), and "GOT ME GEEKED" lives on the official VEVO channel (@denzelcurryvevo4743, UCfgaO8E...). Accepted: VEVO is an official licensed distributor channel (not fan/compilation/Topic, which the gate's disqualification clause names), and the pass holds with 11 artist-channel releases alone. W3 learnings for later waves: (1) artist-channel hub listings can mix channels — spot-check video-level channel_id when a dated dump's channel attribution matters; (2) his monthly audience was NOT extractable (client-rendered music.youtube.com, tab API 400) — recorded as gap per policy, never blocked; (3) Lizzo's pool doc lead was wrong — Song Exploder ep. 291 breaks down "Still Bad", NOT "Truth Hurts" (her story is in Billboard's How It Went Down instead) — pool leads stayed leads, agents re-derived process sources; (4) no Genius Verified episodes exist for Lizzo (gap recorded); (5) AJR's official "Making of Bang!" is production-side only — lyric content came from the How I Write / David Perell episode instead.

## Phase 2 — Synthesis (Session 7) — COMPLETE

- [x] **2.1 Element extraction** — from each `creators/*.md`, extract named workflow elements. → 12 elements (E1–E12).
- [x] **2.2 Matrix** — creators × elements table. → 14×12 matrix in SYNTHESIS.md (a).
- [x] **2.3 Ranked parallels** — shared elements ranked by creator count, weighted by verification strength (tier 1 > tier 2 > tier 3). → All 14 verified are tier 1; within-tier weighting applied (Billie Eilish + Tessa Violet = weak-verification contributors, per W2/W5 QA notes). Ranked list in SYNTHESIS.md (b).
- [x] **2.4 Divergences** — notable conflicts/exceptions between frameworks. → 9 divergences in SYNTHESIS.md (c).

**Exit gate: PASSED (2026-08-13).** `SYNTHESIS.md` written with (a) matrix, (b) ranked list, (c) divergences. Phase 3 (Compilation & QA, Session 8) is a separate session — do not start it here.

**Phase 2 top-line findings (for Phase 3 INDEX weighting):** truth-from-life material = 14/14 creators (the only universal); capture bank 11/14; structured quality gates 10/14; long gestation 9/14; sound-first drafting 8/14; co-write partnership 8/14; constraints 7/14 (0 weak contributors — strongest-weighted); concept-first 7/14. Entry-point elements (chorus-first 4, first-line-first 5, title-first 5) are the least shared and the biggest divergence source. Daily-discipline cluster (5) is the most weakly weighted (2/5 weak-verification contributors).

## Phase 3 — Compilation & QA (Session 8)

- [ ] **3.1 INDEX.md** — all verified creators ranked by (1) verification strength, (2) process-documentation depth; shortfall stated if <10.
- [ ] **3.2 SOURCES.md** — every link used, per creator, with access dates.
- [ ] **3.3 REJECTED.md final pass** — complete with every failed candidate + reason.
- [ ] **3.4 Traceability sweep** — every claim in every output traces to a cited link; no guesses.

**Exit gate (stop here):** all 5 outputs exist and pass the sweep.

## Sequencing Summary

| Phase | Session | Agent(s) | Parallelism | Exit gate |
|---|---|---|---|---|
| 0 Discovery & Screening | 1 | Main + 3 researchers (single burst) + 1 probe | 3 parallel | DONE — pool 28, shortlist 24 |
| 1 Deep Dives | 2–6 | 3 sub-agents per wave | 5 waves × 3 | ≥10 verified creators |
| 2 Synthesis | 7 | Main only | — | DONE — SYNTHESIS.md (matrix + ranked list + divergences) |
| 3 Compilation & QA | 8 | Main only | — | 5 outputs + sweep pass |

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| Over-collection buffer (28 → 24 → 15 → 10) | Verification attrition expected; CONTEXT mandates discovery-first | Smaller pool risks landing under 10 with no backfill available |
| Capability probe step (0.2) | Sub-agent shell access was unconfirmable from config | RESOLVED — probe passed; sub-agents own verification |
| Wave-based dispatch, 5 waves × 3 | User-chosen (5 waves of 3 targeting top 15); one wave per session bounds session size and lets rejection learnings brief the next wave | Full parallel (15 agents) risks a wave of unverified numbers and one unwieldy QA pass |
| Backfill promotion (1.3) | Shortfall-driven promotion avoids a fixed 15-slot ceiling that risks landing under 10 | Fixed waves would strand 13 backfill candidates while under target |
| Single-burst discovery (no waves) | Pool-building has no verification attrition, so reaping between waves adds nothing | Discovery waves would serialize source-domain returns for no benefit |
| Pool file in `b0ttsagent/temp/` not research/ | Pool is scratch work, not verified output | Writing unverified candidates into research/ blurs the output spec's "verified only" intent |
