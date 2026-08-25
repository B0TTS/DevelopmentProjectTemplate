# Handoff — Viral Short-Video Research Mission (Wave 4 = Jenny Hoyos, then Phase 4)

**Date:** 2026-08-13 12:40
**Session slug:** `viral-shorts-wave4-resume`
**Continuity:** active project — prior sessions completed Phases 1–2 + Waves 1–2 of Phase 3 (the `1216_viral-shorts-wave3-resume` handoff). This session completed **Wave 3** (all 3 case studies QC'd) and **prepped Wave 4** (dir created, starting-source YouTube URL found). The user invoked `/handoff` to hand Wave 4 itself off to a fresh session, per the standing decision that the final deep-dive wave + Phase 4 synthesis each get a clean context.

---

## 0. READ THIS FIRST

The prior handoff is the authoritative reference for everything foundational. Do NOT re-derive what it already captures:

**`C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\handoffs\08-13-2026\1216_viral-shorts-wave3-resume\handoff.md`**

It carries, in full:
- §1 — What the project is (the multi-phase research mission + authoritative spec path)
- §5 — **Critical environment gotcha**: the `youtube-transcript` skill's bundled `transcript.sh` does NOT run here (Linux bash, not Git Bash). The full working PowerShell + node + yt-dlp replication IS in §5, including the **mandatory** `--no-warnings` / `2>$null` / `Out-Null` redirections that prevent benign ffmpeg warnings from polluting filenames. Paste and reuse that snippet verbatim.
- §5 — The `ytsearch` pattern for finding podcast YouTube watch URLs when the shortlist gives only Apple/Spotify links.
- §5 — Audio-only podcast protocol (when a podcast has no YouTube caption track, web-research show notes / episode pages; mark repackaged analyst summaries SECOND-HAND).
- §7 — Deep-dive sub-agent prompt template (the 7 seed components).
- §9 — Survivorship-bias caveat (re-state verbatim at the top of Phase 4 README methodology).
- §10 — Key files table.
- §11 — Verify-environment + transcribe + quality-gate commands.

This handoff is a **delta** — what changed this session + exactly where Wave 4 resumes. If anything here conflicts with the prior handoff, this one wins (it is newer).

---

## 1. What this session accomplished

### Wave 3 (Caleb Simpson, Nick DiGiovanni, Sam Sulek) — COMPLETE, all 3 QC'd, no re-spawns

1. Verified the environment (yt-dlp 2026.07.04, node v24.18.0, case-studies dir present — all unchanged from prior handoff).
2. Read the prior handoff, the full mission spec, and the approved shortlist (Jenny Hoyos block at section #10, lines 244–263).
3. Found the YouTube watch URLs for all 3 starting sources via `ytsearch` (Caleb Simpson's first search returned nothing — a broader query + upload-date/channel metadata match confirmed it; see §3 below for the exact IDs and gotchas).
4. Transcribed all 3 starting sources via the §5 PowerShell pipeline — all landed substantive (sizes scaling with podcast length as expected).
5. Launched 3 parallel `b0tts-researcher` deep-dive sub-agents (one per creator), each seeded per the §7 template.
6. Quality-gated each: verified the file landed on disk (line count + byte size match agent reports), confirmed the depth-gauge PASS, confirmed every schema field cited, confirmed thin spots stated explicitly (Sam correctly marked 4 fields N/A+reason — NOT padded).
7. Created the `lifestyle-storytelling/` category dir for Wave 4.
8. Found the YouTube watch URL for the Wave 4 starting source (My First Million #580, Jenny Hoyos).
9. Started transcribing it via the §5 pipeline → **USER ABORTED before the caption download completed.** No Jenny Hoyos transcript landed on disk; the deep-dive sub-agent was NOT launched.

### Wave 4 starting-source YouTube URL — CONFIRMED (this session, saves the next agent a search)

- **My First Million #580 — Jenny Hoyos** — canonical upload:
  - `https://www.youtube.com/watch?v=ZpjGGbrcC8E`
  - Channel: "My First Million" (uploader = channel = same), uploaded **2024-05-03**, duration 2689s (~45 min)
  - Title: "Her Viral Formula Breaks 100 Million Views On YouTube Shorts (ft. Jenny Hoyos)"
  - Matches the shortlist's stated source date (2024-05-03) exactly.
- **DO NOT use** the other surfaced candidate `4iZLER8U2U4` ("The Formula To Break 100 Million Views On Shorts (ft/ Jenny Hoyos)") — that is a **BlackNova Productions re-upload dated 2026-07-28** = SECOND-HAND. The canonical first-party source is `ZpjGGbrcC8E` on the My First Million channel.

---

## 2. Current state — exactly where to resume

**Phase 3 Wave 4 (Jenny Hoyos, solo) — NOT STARTED. Fresh agent resumes here.**

Three concrete steps:

1. **Transcribe `https://www.youtube.com/watch?v=ZpjGGbrcC8E`** via the §5 PowerShell pipeline from the prior handoff. No Jenny Hoyos transcript exists on disk yet (this session's transcription was aborted; nothing landed).
2. **Launch ONE `b0tts-researcher` deep-dive sub-agent** for Jenny Hoyos, seeded per the §7 template. Output file: `case-studies/lifestyle-storytelling/jenny-hoyos.md` (the dir is ALREADY created this session).
3. **Quality-gate** the result (same depth-gauge as Waves 1–3).

Then — and ONLY after Wave 4 passes — STOP and hand off to **another** fresh session for **Phase 4 synthesis** (per the user's standing decision, carried forward unchanged). Do not attempt Phase 4 in the same session as the Wave 4 deep-dive. See §5 below for the Phase 4 handoff template.

---

## 3. Wave 3 YouTube URL findings (recorded so they aren't re-derived)

All three Wave 3 transcriptions succeeded on the first try via the §5 pipeline.

- **Caleb Simpson** — Trading Secrets #209
  - `https://www.youtube.com/watch?v=VA5bvf0Yffo`
  - Channel: "Jason Tartick", uploaded **2024-11-18**, duration 2994s (~50 min)
  - Title: "Caleb Simpson: 42 million views & only making $3,300?! The candid breakdown of $ in content creation"
  - **Gotcha:** the initial `ytsearch12:Trading Secrets Jason Tartick Caleb Simpson episode 209 apartment rent` returned zero results. A broader query (`Caleb Simpson Trading Secrets podcast apartment tiktok`) surfaced `VA5bvf0Yffo`; the upload date 2024-11-18 + channel "Jason Tartick" is the conclusive match (Apple's #209 is also 2024-11-18). NOTE: this YouTube version is the **~50 min edited cut**, vs Apple's reported 1h21m — the deep-dive agent flagged this in the case study; cite the YouTube cut as the canonical first-party source.
- **Nick DiGiovanni** — Colin & Samir "Cracked the YouTube Algorithm"
  - `https://www.youtube.com/watch?v=w52xUmjIZPk`
  - Duration 5497s (~91 min), channel Colin & Samir, matched on first search.
- **Sam Sulek** — Modern Wisdom #994
  - `https://www.youtube.com/watch?v=5117cPLuqB0`
  - Channel: "Chris Williamson", duration 7820s (~130 min = 2h10m — matches shortlist's stated length), title "How to Get Better Every Single Day - Sam Sulek (4K)".

---

## 4. Completed case studies (now 9 of 10 — load all for Phase 4)

All on disk under `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\case-studies\`. Wave 3 additions this session are starred.

| Creator | Category dir | File | Lines | Bytes | QC verdict |
|---------|-------------|------|-------|-------|------------|
| Zach King | `vfx-illusion/` | `zach-king.md` | 162 | 27,184 | PASS (prior session) |
| MrBeast | `mega-creator/` | `mrbeast.md` | 157 | 34,580 | PASS (prior session) |
| Dhar Mann | `scripted-microdrama/` | `dhar-mann.md` | 175 | 41,217 | PASS (prior session) |
| Keith Lee | `food/` | `keith-lee.md` | 156 | 29,536 | PASS (prior session) |
| Airrack | `pranks-challenges/` | `airrack.md` | 127 | 28,839 | PASS (prior session) |
| Steven He | `comedy-skit/` | `steven-he.md` | 184 | 41,629 | PASS (prior session) |
| **Caleb Simpson** ⭐ | `man-on-street/` | `caleb-simpson.md` | 186 | 34,969 | PASS — PARTIAL verification captured as finding (no confirmed checkmark); 2026 cadence-slowdown flag confirmed with data (12 posts / ~12 weeks ≈ 1/week vs 4–6×/week in 2024) and interpreted as a deliberate inbound-pipeline move, not a collapse. Dominance 1.000 undisputed. |
| **Nick DiGiovanni** ⭐ | `food/` | `nick-digiovanni.md` | 186 | 28,757 | PASS — LONG-CAREER-VERIFIED (7 yr; MasterChef finalist; Forbes 30u30; surpassed Gordon Ramsay's channel Jan 2025). C&S + HIBT as the 2 first-party anchors (HIBT via PodScripts.co transcript — flagged third-party transcription service). Dominance 1.000 undisputed. |
| **Sam Sulek** ⭐ | `fitness/` | `sam-sulek.md` | 157 | 25,343 | PASS — HYBRID caveat + lightest-docs honored: 4 schema fields marked N/A+reason, NOT padded (pattern_interrupt_cadence/hook_type/first_frame_timing where applicable to long-form, plus partial N/A for clips vs long-form split). Dominance 1.000 independently re-pulled by the agent (median 3.35M to the exact figure, confirming the shortlist's note that the agent's 0.74 was an under-estimate). **Bonus correction surfaced:** the shortlist's "no course/**brand** monetization" is half-wrong — Sam has brand sponsorships (Hostile, Raw Nutrition, Gymshark-adjacent); only "no course/community" holds. Captured in Caveat #5 of the case study. |

**No re-spawns were needed across Waves 1–3.** Wave 4 (Jenny Hoyos) is the last remaining case study before synthesis.

---

## 5. What comes after Wave 4 — Phase 4 synthesis (FRESH session, per user decision)

After `jenny-hoyos.md` passes quality gate, all 10 case studies are done. **STOP.** Per the user's standing decision (explicitly confirmed 2026-08-13 and carried forward in the prior handoff §3): **Phase 4 synthesis is written by a different fresh session** — synthesis is a different cognitive task that needs to hold all 10 finished case studies' schema fields in working memory, best done from a clean context loaded with just the 10 case studies + the schema + the mirror structure.

The Phase-4 handoff from the Wave-4-finished session should be a short pointer doc, NOT a long re-derivation. State:
- All 10 case studies at `case-studies/<category>/<slug>.md` (list the 10 paths).
- The mission spec path and the acceptance checklist (10 items — see prior handoff §8).
- The mirror structure at `b0ttsagent/research/vocal-mixing-frameworks/` (README, 01-comparison-matrix, 06-source-library; for the new project use 01/02/03 numbering per spec).
- The four synthesis docs to write: `README.md`, `01-comparison-matrix.md` (with the platform axis + agnostic/specific tags), `02-recurring-patterns.md` (the quantified claim-frequency table `tactic → # case studies → list of creator-slugs`; every parallel refs ≥2 slugs + a specific source from each), `03-source-library.md` (full per-source metadata: title, URL, source date, source type, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag).
- The **survivorship-bias caveat** verbatim (prior handoff §9 — re-state at the top of README methodology; non-negotiable).
- Skills for that session: `markdown-doc-designs` (silently enforce Markdown quality on all four synthesis docs); `mermaid-diagrams` only IF a cross-creator workflow-step DAG is being synthesized. Do NOT invoke planning-doc or GSD skills.
- Then user sign-off against the 10-point acceptance checklist.

---

## 6. Jenny Hoyos deep-dive seeding — the one thing to get right

This is the most important framing point for Wave 4. The prior handoff §3 and the shortlist block both flag it; restating here because it is the single most likely thing to get wrong:

> **Jenny Hoyos carries a CHANNEL-UNDERPERFORMANCE FLAG.** Her current YouTube Shorts median is ~190k on 12.3M subs = 1.5% view-to-follower; dominance = 0.757 (the **lowest** in the shortlist — every other approved creator is 1.000). She still passes the secondary median >100k test, and she passes the 0.6 hit-rate floor (20/20 ≥ 100k). But the per-video level is ~50x lower than her 2023-24 historical peak (the agent's "10M avg per Short" was based on that peak — current output is genuinely lower).

> **THIS FLAG IS A VERIFIED FINDING, NOT A REASON TO DISMISS HER.** Her framework documentation is the RICHEST in the shortlist (Creator Science #167 covers hook construction, foreshadowing, retention-graph analysis, but/so storytelling, idea funnel 100→25→10; My First Million #580 covers the 4 idea criteria, power words, first-frame, stakes, Peak-End theory, team data tools). The sub-agent prompt MUST state the flag explicitly AND instruct the agent to treat the per-video performance as verified real data while capturing the framework mechanics in full. Do not let the agent either (a) wave the underperformance away to preserve a rosy story, or (b) dismiss her framework because the per-video numbers dropped. Both failure modes violate the spec — her system is exactly what the mission is trying to extract, AND its recent per-video decay is itself a finding worth recording (the spec calls for verified-vs-claimed honesty, and this is a claimed-vs-verified gap the agent should surface in the `## Verified vs Claimed` and `## Caveats / Contradictions` sections).

Seed the sub-agent with:
1. **Mission rules** — the 6 bullets from the spec (every claim linked, every schema field cited, ≥2 first-party or thin-sources caveat, depth-gauge definition, recency 2021–2026, provenance FIRST-PARTY/SECOND-HAND + MONETIZED/INDEPENDENT).
2. **The Extraction Schema** — the ~15 fields with closed vocabularies from the spec; out-of-vocab mechanism → `## New Terms` section, never silent stuffing.
3. **Jenny Hoyos's full shortlist block** — copy verbatim from `phase2-shortlist-for-signoff.md` section #10 (lines 244–263).
4. **The transcript path** to read FIRST — once transcribed, it will be at `b0ttsagent/temp/youtube-transcripts/My_First_Million_Her_Viral_Formula_Breaks_100_Million_Views_On_YouTube_Shorts_ft._Jenny_Hoyos.txt` (the slugify output this session printed that NAME before the abort; verify the filename on disk after transcribing in case slugify produced a slightly different string).
5. **Output path** — `case-studies/lifestyle-storytelling/jenny-hoyos.md`.
6. **The channel-underperformance flag** — stated as a verified finding to incorporate, with the exact math (`0.5×1.0 + 0.3×0.19 + 0.2×1.0 = 0.757`), and the instruction to treat the framework documentation as rich/worth capturing in full while honestly recording the per-video decay.
7. **Return-format instruction** — concise report only (NOT the full case study — it's on disk): (a) path + line count + byte size, (b) depth-gauge self-check (every workflow step ≥1 first-party source, listed), (c) gaps/thin spots written explicitly, (d) dominance-score dispute check (0.757 — confirm or dispute with stats), (e) one-line framework summary, (f) underperformance-flag-reflection confirm (captured as verified finding, NOT waived away). Plus "verify by re-reading the file before reporting back."

---

## 7. Key files (open these to resume)

Re-stating only the additions/changes from the prior handoff's §10 table — the prior table is still authoritative for everything else.

| Path | Contents | Why the next agent needs it |
|------|----------|-----------------------------|
| `b0ttsagent/handoffs/08-13-2026/1216_viral-shorts-wave3-resume/handoff.md` | Prior handoff (foundational) | **READ FIRST** — environment, PowerShell pipeline §5, audio-only protocol, §7 sub-agent template, §9 survivorship caveat, §10 key files, §11 commands |
| `b0ttsagent/temp/viral-shortvideo-research/phase2-shortlist-for-signoff.md` (lines 244–263) | Jenny Hoyos shortlist block | **Seed the Wave 4 sub-agent with this block verbatim** — links, 0.757 dominance math, first-party sources (Creator Science #167 + My First Million #580 + Jay Clouse beachside interview), best starting source |
| `b0ttsagent/research/viral-shortvideo-frameworks/case-studies/lifestyle-storytelling/` | Wave 4 output dir | **ALREADY CREATED this session** — drop `jenny-hoyos.md` here; no need to mkdir |
| `b0ttsagent/temp/youtube-transcripts/` (append-only) | Transcripts dir | The 3 new Wave 3 transcripts + the soon-to-be-created Jenny Hoyos transcript land here alongside the 4 prior ones |

### Wave 3 transcripts added this session (already on disk — read-first for Phase 4 if it touches these creators; do NOT re-download)

- `Jason_Tartick_Caleb_Simpson_42_million_views_only_making_3300_The_candid_breakdown_of_in_content_cre.txt` (Caleb Simpson, Trading Secrets #209 YouTube cut, ~50 min)
- `Colin_and_Samir_How_Nick_DiGiovanni_Cracked_the_YouTube_Algorithm.txt` (Nick DiGiovanni, ~91 min)
- `Chris_Williamson_How_to_Get_Better_Every_Single_Day_-_Sam_Sulek_4K.txt` (Sam Sulek, Modern Wisdom #994, ~130 min)

### Transcripts NOT yet on disk (next agent makes this one)

- Jenny Hoyos — My First Million #580 (`ZpjGGbrcC8E`). Transcribe FIRST via the §5 pipeline, then launch the deep-dive sub-agent.

---

## 8. Commands the next agent will run

### Verify the environment (one-time at session start)
Per prior handoff §11 — `yt-dlp --version` (expect 2026.07.04+), `node --version` (expect v24.18.0+), `Test-Path -LiteralPath "...viral-shortvideo-frameworks"`.

### Transcribe the Jenny Hoyos starting source (§5 PowerShell pipeline)
URL already found (§1 above) — no search needed. Reuse the prior handoff §5 snippet verbatim with `$URL="https://www.youtube.com/watch?v=ZpjGGbrcC8E"`. The `2>$null` / `Out-Null` redirections and `--no-warnings` flag are MANDATORY.

### Verify the Wave 4 case study landed on disk (quality-gate)
```powershell
$base="C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\case-studies"
Get-ChildItem -LiteralPath "$base\lifestyle-storytelling" -File | ForEach-Object { "{0,6} lines  {1,7} bytes  {2}" -f (Get-Content -LiteralPath $_.FullName | Measure-Object).Count, (Get-Item -LiteralPath $_.FullName).Length, $_.Name }
```
Also `read` the file to confirm all sections present (header meta, extraction schema with per-field citations, workflow breakdown each step sourced, `## Sources` with full metadata, `## Verified vs Claimed`, `## Caveats / Contradictions`, `## New Terms` if needed) and confirm the underperformance flag is captured as a verified finding.

### Confirm all 10 case studies present before handoff to Phase 4
```powershell
$base="C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\case-studies"
Get-ChildItem -LiteralPath $base -Recurse -File -Filter *.md | ForEach-Object { "{0,4} lines  {1,7} bytes  {2}" -f (Get-Content -LiteralPath $_.FullName | Measure-Object).Count, (Get-Item -LiteralPath $_.FullName).Length, $_.FullName.Substring($base.Length+1) }
```
Expect exactly 10 files across 9 category dirs (`food/` has both Keith Lee and Nick DiGiovanni). Any count ≠ 10 = stop and investigate.

---

## 9. Open decisions (none pending until Phase 4 sign-off)

All decisions remain approved and carried forward unchanged from the prior handoff §12:
- Mirror `vocal-mixing-frameworks/` structure for the synthesis docs
- TikTok-fail fallback = aggregate-tracker citing SECOND-HAND flagged (relevant only if a NEW candidate surfaces; the approved 10 already passed yt-dlp)
- Phase 3 cadence = solo wave here (Wave 4), stream straight to synthesis
- Pure dominance ranking (no soft cap / no niche diversification)
- Final roster = 10 creators (Mino Lee dropped)
- **Phase 4 synthesis written by a fresh session** — confirmed by user 2026-08-13, carried forward. Wave 4 does NOT do Phase 4. Wave 4 finishes, then hands off AGAIN.

No further user decisions pending until Phase 4 synthesis sign-off.

---

## 10. First actions for the next agent

1. Read this handoff §0 and the prior handoff (`1216_viral-shorts-wave3-resume/handoff.md`) end-to-end — the prior one carries the environment gotcha (§5 PowerShell pipeline) and the sub-agent template (§7) you will reuse.
2. Verify the environment (§8 commands) — quick one-time check.
3. Transcribe `https://www.youtube.com/watch?v=ZpjGGbrcC8E` (My First Million #580, Jenny Hoyos, 2024-05-03) via the §5 pipeline. Confirm the .txt landed with substantive size.
4. Read the Jenny Hoyos block from `phase2-shortlist-for-signoff.md` (section #10, lines 244–263) — that plus this handoff's §6 framing is the sub-agent seed.
5. Launch **ONE** `b0tts-researcher` deep-dive sub-agent for Jenny Hoyos, seeded per §7 of the prior handoff + §6 of this one. **The channel-underperformance flag is a VERIFIED FINDING — state it explicitly in the prompt and instruct the agent to capture the rich framework mechanics in full while honestly recording the per-video decay. Do not let the agent wave it away OR dismiss her system.**
6. Quality-gate: verify the file landed on disk (line count + byte size), re-read it to confirm all sections + per-field citations + verified-finding treatment of the flag, confirm the depth-gauge PASS. Re-spawn only if shallow-from-shallow-research (the flag is a genuine verified finding, NOT grounds for re-spawn).
7. Confirm all 10 case studies are on disk (§8 final command — expect 10 files).
8. **STOP and write the Phase 4 handoff** — a short pointer doc per §5 above; handoff to ANOTHER fresh session for synthesis. Do NOT attempt Phase 4 in this session. The user explicitly split them.
9. (Phase 4 session only — beyond this handoff's scope) Write README + 01-comparison-matrix + 02-recurring-patterns + 03-source-library per the spec's acceptance checklist; invoke `markdown-doc-designs` (and optionally `mermaid-diagrams`); run the 10-point checklist; get user final sign-off.

---

## 11. Suggested skills for the next session

The user requires skills invoked when applicable (per `AGENTS.md`).

**For Wave 4 execution (this resume):**
- `youtube-transcript` — LOAD the skill for protocol context, but use the §5 PowerShell pipeline from the prior handoff (the bundled `transcript.sh` does not run here — Linux bash, not Git Bash). Transcribe `ZpjGGbrcC8E` FIRST.
- `create-nav-guide` — **NOT** needed (research, not a NavGuide-eligible configured system).
- `markdown-doc-designs` — **DEFER to the Phase 4 session** (Wave 4 produces a single case study; synthesis is where psychological-efficiency/scanability matters most).
- Do NOT invoke: `create-planning-docs` / `create-execution-plan` (the mission spec IS the plan), `agents-md` (already exists), anything GSD-related.

**For the Phase 4 synthesis session (separate fresh session, after this):**
Per prior handoff §13: `markdown-doc-designs` (silently enforce on all four synthesis docs); `mermaid-diagrams` only IF synthesizing cross-creator workflow-step DAGs; do NOT invoke planning-doc or GSD skills.

---

## 12. Redacted / sensitive info

None to redact. All evidence is public web content. No API keys, passwords, or PII were used or generated.

---

**End of handoff. Resume at Wave 4 (Jenny Hoyos). The starting-source URL is already found (`ZpjGGbrcC8E`); the output dir is already created. Transcribe → launch one deep-dive sub-agent (with the underperformance flag framed per §6) → quality-gate → STOP and hand off to a fresh session for Phase 4 synthesis.**