# Handoff — Viral Short-Video Research Mission (Phase 3 deep-dives, Waves 3–4 + Phase 4)

**Date:** 2026-08-13 12:16
**Session slug:** `viral-shorts-wave3-resume`
**Continuity:** active project — prior sessions completed Phases 1–2 + Waves 1–2 of Phase 3. This handoff lets a fresh agent resume at **Wave 3** and finish through Phase 4.

---

## 1. What this project is

A multi-phase research mission to find short-video content creators who have **deeply documented, in public, the step-by-step workflows they use to make viral videos consistently (100k–1m+ views per video)** — then write one deep case study per creator plus synthesized docs (comparison matrix, recurring-patterns, source library, README) under `b0ttsagent/research/viral-shortvideo-frameworks/`.

The full, authoritative mission spec (173 lines) lives at:

**`C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md`**

The next agent MUST read it in full. It contains: hard requirements (verification bar, recency cuts, dominance formula, consistency test), the measurement protocol (yt-dlp, not UI), the orchestration plan (Phase 1 → 1.5 → 2 → 3 → 4), the extraction schema every deep-dive case study must fill, output structure, non-negotiables, quantified-parallels rules, and the acceptance checklist.

---

## 2. What's been done across all sessions

**Phase 1 (Discovery) — COMPLETE** (prior session). Three parallel `b0tts-researcher` sub-agents partitioned by EVIDENCE TYPE → 22 raw candidates.

**Phase 1.5 (Dedup + cull + authoritative yt-dlp pulls) — COMPLETE** (prior session). Dedup merged multi-surfaced candidates. Hard cuts rejected 12. Authoritative `yt-dlp --flat-playlist` pulls on each survivor computed ground-truth hit_rate, hit_magnitude, dominance. Three yt-dlp cuts caught agent over-estimates (Gary Vaynerchuk, Alex Hormozi, Peter McKinnon).

**Phase 2 (Selection gate — sign-off) — COMPLETE** (prior session). Shortlist written; **user approved the 10-creator roster** (Mino Lee dropped per user direction — PARTIAL verification + MONETIZED docs).

**Phase 3 (Deep-dives) — Waves 1 & 2 COMPLETE (6 of 10 case studies); Waves 3 & 4 NOT STARTED.** This session ran Waves 1–2.

### Approved 10-creator deep-dive roster (in waves) — UNCHANGED

| Wave | Creators | Caveats | Status |
|------|----------|---------|--------|
| Wave 1 | Zach King, MrBeast, Dhar Mann | MrBeast carries long-form-first caveat | ✅ DONE |
| Wave 2 | Keith Lee, Airrack, Steven He | Airrack carries long-form-first caveat | ✅ DONE |
| Wave 3 | Caleb Simpson, Nick DiGiovanni, Sam Sulek | Sam Sulek carries hybrid caveat + lightest docs (only 2 first-party sources) | ⬜ NOT STARTED |
| Wave 4 | Jenny Hoyos | Channel-underperformance flag (median ~190k vs 12.3M subs); dominance = 0.757 | ⬜ NOT STARTED |

Cadence (user-approved): **3 per wave, stream straight through to synthesis, no per-wave user checkpoints.** Only Phase 2 + final Phase 4 sign-off require user input.

---

## 3. Current state — exactly where to resume

**Wave 3 (Caleb Simpson, Nick DiGiovanni, Sam Sulek) — NOT STARTED. Fresh agent resumes here.**

**Wave 4 (Jenny Hoyos, solo) — NOT STARTED. After Wave 3.**

**Phase 4 (Synthesis) — NOT STARTED. After all 10 case studies pass quality gate.** Per user decision in this session (explicitly confirmed): **Phase 4 should be written by a fresh session** — synthesis is a different cognitive task that needs to hold all 10 finished case studies' schema fields in working memory, best done from a clean context loaded with just the 10 case studies + the schema. So: finish Wave 3 + Wave 4 here (or in a continuation), then hand off to ANOTHER fresh session for Phase 4 only.

### Per-creator starting-source pointers for Wave 3 & 4

(Each deep-dive agent must be seeded from the full per-creator block in the shortlist file — see Key files.)

- **Caleb Simpson** — Trading Secrets #209 (2024-11-18). Podcast IS on YouTube — find via `ytsearch` as done for prior waves (search "Caleb Simpson Trading Secrets episode 209" or "Trading Secrets Jason Tartick Caleb Simpson"). Transcribe the full episode via the youtube-transcript skill pipeline FIRST.
- **Nick DiGiovanni** — Colin & Samir "How Nick DiGiovanni Cracked the YouTube Algorithm" (2025-07).
- **Sam Sulek** — Modern Wisdom #994 (2025-09-15). Podcast IS on YouTube (Chris Williamson's channel). Transcribe via the skill pipeline. NOTE: lightest documentation in the shortlist — only 2 first-party sources (Modern Wisdom + Cutler Cast). Expect a thinner case study; downgraded-evidence-tier is acceptable per the shallow-output protocol — NEVER pad.
- **Jenny Hoyos** — My First Million #580 (2024-05-03). Podcast may be YouTube-hosted (search) or audio-only (→ web-research show notes/summaries like Dhar Mann's HIBT). **CRITICAL:** the channel-underperformance flag (median ~190k on 12.3M subs = 1.5% view-to-follower; dominance 0.757, the lowest in the shortlist) must be incorporated into her case study as a **VERIFIED FINDING, not waved away**. Her framework documentation is rich (Creator Science + My First Million cover hook construction, foreshadowing, retention graphs, but/so storytelling, Peak-End theory, 4 idea criteria, power words, first-frame) — capture it fully despite the performance flag.

---

## 4. Completed case studies (on disk — quality-gated, no re-spawns needed)

| Creator | Category dir | File | Lines | Bytes | QC verdict |
|---------|-------------|------|-------|-------|------------|
| Zach King | `vfx-illusion/` | `zach-king.md` | 162 | 27,184 | PASS — 11 first-party sources; gaps are genuine (first-frame timing inferred, posting cadence 2023-era) |
| MrBeast | `mega-creator/` | `mrbeast.md` | 157 | 34,580 | PASS — 8 first-party; long-form-first caveat reflected in platform_specific_mechanics; shorts repurposing marked THIN-SOURCE ZONE honestly |
| Dhar Mann | `scripted-microdrama/` | `dhar-mann.md` | 175 | 41,217 | PASS — 4 first-party incl. bonus BigDeal/Codie Sanchez transcript; captured 4-P framework, $10 FB pre-tests, 10:1 green-lighting funnel, 21-day pipeline; 2021-24 decline + FB recovery arc as verified finding |
| Keith Lee | `food/` | `keith-lee.md` | 156 | 29,536 | PASS — 5 first-party (BC transcript + Club Shay Shay + SXSW + Blavity + Eater); car-review format, integrity protocol, mass-request funnel, city-tour scaling |
| Airrack | `pranks-challenges/` | `airrack.md` | 127 | 28,839 | PASS — 3 first-party; "format system," A-plot, intro A/B, clipping-distribution layer; long-form-first caveat reflected; central thin spot (no first-party shorts-native framework) honestly flagged |
| Steven He | `comedy-skit/` | `steven-he.md` | 184 | 41,629 | PASS — 8 first-party incl. full Driven transcript; study-first algorithm mastery, joke-density sketches, Failure Management loop, 80% channel-crash recovery, CTR-target contradiction flagged |

All six passed the depth-gauge (every workflow step ≥1 first-party source; every claim linked; verified-vs-claimed + caveats + contradictions explicit; thin spots stated not padded). **No re-spawns were needed for any of Waves 1–2.**

---

## 5. Critical environment/workflow gotcha — the youtube-transcript skill's bundled script DOES NOT run here

The `youtube-transcript` skill's `SKILL.md` says to run `bash scripts/transcript.sh "<URL>"`. **This environment's `bash` is Linux 5.2.21 (`/usr/bin/bash`, `x86_64-pc-linux-gnu`), NOT Git Bash** — it cannot resolve `C:\` or `/c/` Windows paths, so the bundled `transcript.sh` fails with "No such file or directory." Do NOT waste time debugging that.

The skill's actual substance is reproducible directly in PowerShell + `node` + `yt-dlp` (all confirmed on PATH: `yt-dlp` 2026.07.04, `node` v24.18.0). The helper scripts (`slugify.js`, `flatten-json3.js`) DO work when called via `node`. The working replication of the skill's exact protocol (manual `en` preferred over auto `en-orig`, json3 flattening, save to `b0ttsagent/temp/youtube-transcripts/`, bot-flag handling) is:

```powershell
# === yt-dlp caption pipeline (replaces transcript.sh on this machine) ===
$SCRIPTS="C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\youtube-transcript\scripts"
$OUT="C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\youtube-transcripts"
$URL="<YOUTUBE_URL>"

# Filename via skill's slugify.js — IMPORTANT: use --no-warnings + 2>$null on metadata
# (benign ffmpeg warnings leak into stdout and pollute the filename otherwise)
$META=$(& yt-dlp --no-warnings --js-runtimes node --no-playlist --print "%(channel,uploader,uploader_id)s|%(title)s" --skip-download $URL 2>$null)
$NAME=$(& node "$SCRIPTS\slugify.js" "$META")

# Download both manual (en) and auto (en-orig) captions as json3
$(& yt-dlp --no-warnings --js-runtimes node --skip-download --write-subs --write-auto-subs --sub-langs "en,en-orig" --sub-format json3 -o "$OUT\$NAME.%(ext)s" $URL) 2>&1 | Out-Null

# Prefer manual en > auto en-orig > anything written; flatten to .txt via skill's flatten-json3.js
$j="$OUT\$NAME.en.json3"; if(-not(Test-Path -LiteralPath $j)){ $j="$OUT\$NAME.en-orig.json3" }
if(-not(Test-Path -LiteralPath $j)){ $g=Get-ChildItem -LiteralPath $OUT -Filter "$NAME.*.json3" | Select-Object -First 1; if($g){ $j=$g.FullName } else { $j=$null } }
if($j){ $(& node "$SCRIPTS\flatten-json3.js" "$j" "$OUT\$NAME.txt") } else { Write-Output "NO JSON3 WRITTEN" }
```

All `2>&1 | Out-Null` and `2>$null` redirections are MANDATORY — without them yt-dlp's benign ffmpeg/impersonation/n-challenge warnings leak into stdout and (a) halt the script under `$ErrorActionPreference='Stop'`, or (b) get slugified into the filename (a real bug that happened: a transcript got named `WARNING_ffmpeg_not_found_...`).

### Finding a podcast's YouTube watch URL (when the shortlist gives only an Apple/Spotify link)

```powershell
yt-dlp --no-warnings --js-runtimes node --flat-playlist --playlist-end 12 --print "%(id)s | %(duration)s | %(title).65s" "ytsearch12:<show name> <guest> full interview"
```

Pick the result matching the expected ~duration + title. This is how this session found the MrBeast DOAC video (`FjrJ2DJN_pA`) and the Steven He Driven Podcast video (`ZbT3vAqD_4U`). Do the same for Wave 3's Trading Secrets, Colin & Samir, Modern Wisdom episodes.

### Audio-only podcasts (no YouTube version)

When a starting source has no YouTube caption track (e.g., How I Built This, My First Million may be audio-only), the youtube-transcript approach does NOT apply. The deep-dive agent should instead webfetch show notes / episode pages / reputable transcript summaries (iHeart and other podcast hosts often publish inline transcripts — the Keith Lee Breakfast Club episode had a usable excerpt on iHeart). Mark any repackaged analyst summary as SECOND-HAND; only the creator's own words count as FIRST-PARTY.

---

## 6. Transcripts already on disk (read first — don't re-download)

Located in `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\youtube-transcripts\`:

| Transcript .txt | Creator | Wave | Source |
|-----------------|---------|------|--------|
| `Movie_Magic_How_I_Keep_Making_Viral_Videos.txt` | Zach King | 1 | Own channel / "Movie Magic" 2025-04 |
| `The_Diary_Of_A_CEO_MrBeast_If_You_Want_To_Be_Liked_Dont_Help_People_I_Lost_Tens_Of_Millions_On_Beast.txt` | MrBeast | 1 | DOAC 2025-02 (`FjrJ2DJN_pA`) |
| `Jon_Youshaei_How_Airrack_Made_YouTubes_Greatest_Comeback_Interview.txt` | Airrack | 2 | Youshaei 2025-10 (`wtMudMODlWU`) |
| `Driven_Podcast_How_Steven_He_Built_YouTube_Success_Through_220_Failures_and_Emotional.txt` | Steven He | 2 | Driven 2025-12 (`ZbT3vAqD_4U`) |

(Dhar Mann and Keith Lee used audio-only podcasts → no transcript; their agents web-researched instead. Wave 3–4 agents will create new transcripts for their starting sources.)

The skill's protocol says **sample most-recent-first** — the transcript above IS each creator's newest strategy/breakdown capture, which is why it was transcribed first. For Wave 3–4, transcribe the newest available first-party source the same way before chasing older corroborating sources.

---

## 7. Deep-dive sub-agent prompt template (reuse for Waves 3–4)

Each spawned `b0tts-researcher` gets a fresh context with NO discovery memory. Seed each with:

1. **Mission rules** (the 6 bullets from the spec: every claim linked, every schema field cited, ≥2 first-party sources or thin-sources caveat, depth-gauge definition, recency 2021–2026, provenance FIRST-PARTY/SECOND-HAND + MONETIZED/INDEPENDENT).
2. **The Extraction Schema** (closed vocabularies — the ~15 fields from the spec; out-of-vocab mechanism → `## New Terms` section, never silent stuffing).
3. **One creator's full shortlist block** (links, dominance math, sources, best starting source) — copy verbatim from `phase2-shortlist-for-signoff.md`.
4. **The pre-downloaded transcript path** to read FIRST (if you transcribed one); otherwise the instruction to web-research the audio podcast show notes.
5. **The category dir + output filename** (`case-studies/<category>/<creator-slug>.md`).
6. **Caveat instructions** if the creator carries a flag (long-form-first, hybrid, channel-underperformance).
7. **Return-format instruction**: concise report only (NOT the full case study — it's on disk) with (a) path, (b) depth-gauge self-check, (c) gaps/thin spots, (d) dominance-score dispute, (e) one-line framework summary, (f) caveat-reflection confirm if applicable. Plus "verify by re-reading the file before reporting back."

The exact prompts used for Waves 1–2 are captured in this session's task-launch tool calls (visible in the conversation log) — mirror their structure. Category dirs for Wave 3–4: `man-on-street/` (Caleb Simpson — ALREADY CREATED), `food/` (Nick DiGiovanni — ALREADY EXISTS), `fitness/` (Sam Sulek — ALREADY CREATED); `lifestyle-storytelling/` (Jenny Hoyos) **NOT YET CREATED** — create it before launching Wave 4.

Quality-gate each returned case study before declaring the wave done: verify the file landed on disk (line count + byte size via `Get-ChildItem`), confirm the agent reported the depth-gauge PASS, and re-spawn only if shallow-from-shallow-research (genuine source-availability limits are NOT grounds for re-spawn — downgrade evidence tier / write the gap explicitly instead, per the shallow-output protocol).

---

## 8. What the next agent must produce (Wave 3 → Wave 4 → Phase 4)

### Wave 3 — Caleb Simpson, Nick DiGiovanni, Sam Sulek (3 parallel `b0tts-researcher` sub-agents)
1. Create any missing category dirs (Wave 3's are all created: `man-on-street/`, `food/`, `fitness/`).
2. Find YouTube watch URLs for the three starting sources via `ytsearch` (Trading Secrets #209 Caleb Simpson; Colin & Samir Nick DiGiovanni "Cracked the YouTube Algorithm"; Modern Wisdom #994 Sam Sulek). Transcribe each via the PowerShell pipeline in §5.
3. Launch 3 parallel deep-dive sub-agents (one per creator) seeded per the template in §7.
4. Quality-gate each.

### Wave 4 — Jenny Hoyos (solo)
1. Create `case-studies/lifestyle-storytelling/` dir.
2. Transcribe My First Million #580 (if on YouTube) or web-research show notes (if audio-only).
3. Launch ONE deep-dive sub-agent. **Incorporate the channel-underperformance flag as a VERIFIED FINDING** — her median ~190k on 12.3M subs (1.5% view-to-follower; dominance 0.757) is real data, not a reason to dismiss her. Her framework documentation is rich; capture it fully. The agent prompt should state the flag explicitly and instruct the agent to treat it as verified, not caveated-away.
4. Quality-gate.

### Phase 4 — Synthesis (DO IN A FRESH SESSION — per user direction)
After all 10 case studies pass quality gate, write the four synthesis docs to `b0ttsagent/research/viral-shortvideo-frameworks/`, mirroring `vocal-mixing-frameworks/`:
- `README.md` — topic overview, methodology INCL. survivorship-bias caveat (REQUIRED top of methodology — verbatim text in handoff §9 below), dominance-ranked creator list. "Read this first if you only read three things" pattern. Lets a new reader pick a framework in 5 min.
- `01-comparison-matrix.md` — every creator vs. the extraction-schema axes, **with a platform axis** (TikTok / Shorts / Reels / multi) and platform-agnostic-vs-specific tags. Compressed rows; open linked case study for full chain.
- `02-recurring-patterns.md` — quantified: a **claim-frequency table** `tactic → number of case studies that cite it → list of creator-slugs`. Every parallel entry references **≥2 case studies by slug + a specific source from each**. Tag every parallel `platform-agnostic` or `platform-specific`.
- `03-source-library.md` — all links organized per creator. Per-source metadata (title, URL, source date, source type, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag).

### Acceptance checklist (definition of "done and good") — verify before signing off Phase 4

All must be true (from the spec, unchanged):
- [ ] Every claim in every doc linked to a source
- [ ] ≥2 primary (first-party) sources per case study, or explicit "thin sources" caveat
- [ ] Dominance ranking reproducible from the listed stats (show the numbers)
- [ ] All schema fields populated per case study (or marked N/A + reason)
- [ ] Every populated schema field carries its own source citation
- [ ] Source library entries carry full metadata (date, type, provenance, monetization bias, staleness flag)
- [ ] Quantified parallels table completed; every parallel refs ≥2 slugs + sources
- [ ] Platform axis populated in matrix; parallels tagged agnostic/specific
- [ ] Staleness tags (`still-current as of 2026?`) present on every citation
- [ ] README includes survivorship-bias caveat and lets a new reader pick a framework in 5 min

---

## 9. Survivorship-bias reminder (re-state in README methodology verbatim — non-negotiable)

These are **winners'** workflows — documented by creators who already broke out. Frameworks correlate with virality; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and an audience the reader doesn't have yet.

---

## 10. Key files (open these to resume)

| Path | Contents | Why the next agent needs it |
|------|----------|-----------------------------|
| `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md` | The full 173-line mission spec | Authoritative instructions — follow strictly |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\viral-shortvideo-research\phase2-shortlist-for-signoff.md` | Approved 10-creator shortlist; full per-creator evidence packets with links, dominance math, best starting source | **Seed every Wave 3–4 deep-dive sub-agent with one block from this file** (just the 10 — skip Mino Lee block #11, dropped) |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\viral-shortvideo-research\phase1-merged-and-cuts.md` | Phase 1 raw pool + cuts log + yt-dlp batch results | Audit trail — only needed if a deep-dive agent surfaces a candidate question |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\README.md` | Pattern to mirror for the new README | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\01-comparison-matrix.md` | Pattern to mirror for the new matrix | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\06-source-library.md` | Pattern to mirror for source-library structure | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\youtube-transcript\SKILL.md` | Skill instructions | **READ but its transcript.sh won't run here — use the PowerShell pipeline in handoff §5 instead** |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\youtube-transcript\scripts\flatten-json3.js` | Flattener (works via node) | Called by the PowerShell pipeline |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\youtube-transcript\scripts\slugify.js` | Filename slugifier (works via node) | Called by the PowerShell pipeline |
| `C:\Users\intel\DevelopmentProjectTemplate\AGENTS.md` | Project-wide agent rules | Don't violate — esp. "always invoke skills first" rule |

### Completed case studies (load for Phase 4 synthesis — the next agent reads ALL 10)

- `…\case-studies\vfx-illusion\zach-king.md` ✅
- `…\case-studies\mega-creator\mrbeast.md` ✅
- `…\case-studies\scripted-microdrama\dhar-mann.md` ✅
- `…\case-studies\food\keith-lee.md` ✅
- `…\case-studies\pranks-challenges\airrack.md` ✅
- `…\case-studies\comedy-skit\steven-he.md` ✅

(Wave 3 adds: `man-on-street\caleb-simpson.md`, `food\nick-digiovanni.md`, `fitness\sam-sulek.md`. Wave 4 adds: `lifestyle-storytelling\jenny-hoyos.md`. All 10 must exist before Phase 4.)

### Output base dir (exists — case-studies subdir also exists with category subdirs created through Wave 2)

`C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\`

Category subdirs already created: `vfx-illusion/`, `mega-creator/`, `scripted-microdrama/`, `food/`, `pranks-challenges/`, `comedy-skit/`, `man-on-street/`, `fitness/`. Still to create before Wave 4: `lifestyle-storytelling/`.

### Transcripts location (append-only)

`C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\youtube-transcripts\` — Wave 3–4 transcripts land here alongside the 4 existing ones (listed in §6).

---

## 11. Commands the next agent will run

### Verify the environment (one-time at session start)

```powershell
yt-dlp --version   # expected: 2026.07.04 or later; on PATH
node --version     # expected: v24.18.0 or later; on PATH
Test-Path -LiteralPath "C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks"
```

### Transcribe a YouTube starting source (use the PowerShell pipeline — §5 above, NOT transcript.sh)

See §5 — the full parameterized snippet. The `2>$null` / `Out-Null` redirections and `--no-warnings` flag are MANDATORY.

### Find a podcast's YouTube URL when the shortlist gives only an Apple/Spotify link

```powershell
yt-dlp --no-warnings --js-runtimes node --flat-playlist --playlist-end 12 --print "%(id)s | %(duration)s | %(title).65s" "ytsearch12:<show> <guest> full interview"
```

### Verify a case study landed on disk (quality-gate step)

```powershell
$base="C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\case-studies"
Get-ChildItem -LiteralPath "$base\<category>" -File | ForEach-Object { "{0,6} lines  {1,7} bytes  {2}" -f (Get-Content -LiteralPath $_.FullName | Measure-Object).Count, (Get-Item -LiteralPath $_.FullName).Length, $_.Name }
```

### Known extraction issue (do not chase — carried from prior handoff, unchanged)

TikTok bot-flag persists on this Windows machine (yt-dlp upstream issue #10927, Windows-only DPAPI cookie-decrypt failure). The approved 10 creators all already passed yt-dlp verification, so this should NOT recur in Phase 3. If a NEW candidate surfaces, use the approved fallback: aggregate-tracker citing SECOND-HAND flagged.

---

## 12. Open decisions (none pending until Phase 4 sign-off)

All decisions are approved and carried forward unchanged from the prior handoff:
- ✅ Mirror `vocal-mixing-frameworks/` structure
- ✅ TikTok-fail fallback = aggregate-tracker citing SECOND-HAND flagged
- ✅ Phase 3 cadence = 3 per wave, stream straight to synthesis (no per-wave checkpoints; only Phase 2 + final Phase 4 sign-off)
- ✅ Pure dominance ranking (no soft cap / no niche diversification)
- ✅ Final roster = 10 creators (Mino Lee dropped)
- ✅ **NEW this session:** Phase 4 synthesis written by a fresh session (not the same session that runs the deep-dive waves) — confirmed by user 2026-08-13

No further user decisions pending until Phase 4 synthesis sign-off.

---

## 13. Suggested skills for the next session

The user requires skills to be invoked when applicable (per `AGENTS.md`).

**For Wave 3–4 execution (this resume):**
- `youtube-transcript` — LOAD the skill to read its protocol, but use the PowerShell pipeline in handoff §5 (the bundled `transcript.sh` won't run — Linux bash, not Git Bash). Transcribe each Wave 3–4 creator's best starting source FIRST (most-recent-first), then have the deep-dive agent web-research the remaining sources.
- `create-nav-guide` — **NOT** needed (this is research, not a NavGuide-eligible configured system).
- `markdown-doc-designs` — **defer to Phase 4** session (the synthesis docs are where psychological-efficiency/scanability matters most).

**For Phase 4 synthesis session (separate fresh session):**
- `markdown-doc-designs` — silently enforce Markdown quality on the README + matrix + parallels + source-library.
- `mermaid-diagrams` — IF synthesizing any DAGs (e.g., a workflow-step dependency graph across creators). Optional.
- Do NOT invoke: `create-planning-docs` / `create-execution-plan` (this is research, not project planning — the mission spec IS the plan), `agents-md` (already exists), anything GSD-related.

---

## 14. First actions for the next agent

1. Read `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md` end-to-end (skim — most rules carry forward; the schema + non-negotiables + acceptance checklist are the binding parts).
2. Read this handoff §5 (the PowerShell transcript pipeline) — print it; you'll reuse it.
3. Read `phase2-shortlist-for-signoff.md` — extract the Caleb Simpson, Nick DiGiovanni, Sam Sulek blocks for Wave 3 (and Jenny Hoyos for Wave 4).
4. Load the `youtube-transcript` skill (for protocol context only — do NOT run its `transcript.sh`).
5. Find YouTube watch URLs for the three Wave 3 starting sources via `ytsearch`. Transcribe each via the §5 pipeline.
6. Launch **Wave 3** (3 parallel `b0tts-researcher` sub-agents): Caleb Simpson (`man-on-street/`), Nick DiGiovanni (`food/`), Sam Sulek (`fitness/`). Seed each per the template in §7. **Sam Sulek carries the lightest docs (2 first-party) — expect a thinner case study; that's acceptable, do not pad.**
7. Quality-gate each Wave 3 case study; re-spawn only if shallow-from-shallow-research (genuine source limits are NOT grounds for re-spawn).
8. Create `case-studies/lifestyle-storytelling/` dir. Launch **Wave 4** (Jenny Hoyos solo). **Incorporate the channel-underperformance flag as a verified finding, not a caveat-away.**
9. Quality-gate Wave 4.
10. At this point all 10 case studies are done. **STOP and hand off to a fresh session for Phase 4** (per user decision — synthesis is best written from a clean context with all 10 case studies + schema loaded). The Phase 4 handoff should be a short pointer doc: "all 10 case studies at `case-studies/<category>/<slug>.md`, the spec at `<path>`, the mirror structure at `vocal-mixing-frameworks/`, write the 4 synthesis docs + run the acceptance checklist." Do NOT attempt Phase 4 in the same session as the deep-dive waves — the user explicitly split them.
11. (Phase 4 session only) Write README, 01-comparison-matrix, 02-recurring-patterns, 03-source-library. Run the 10-point acceptance checklist (handoff §8). Get user final sign-off. Then — and only then — the work is "done and good."

---

## 15. Redacted / sensitive info

None to redact. All evidence is public web content. No API keys, passwords, or PII were used or generated.

---

**End of handoff.**