# Handoff — Viral Short-Video Research Mission (Phase 3 deep-dives)

**Date:** 2026-08-13 11:39
**Session slug:** `viral-shorts-research-phase3`
**Continuity:** active project — prior agent's context was full; this handoff lets a fresh agent resume at Phase 3.

---

## 1. What this project is

A multi-phase research mission to find short-video content creators who have **deeply documented, in public, the step-by-step workflows they use to make viral videos consistently (100k–1m+ views per video)** — and then write one deep case study per creator plus a synthesized comparison matrix, recurring-patterns doc, source library, and README under `b0ttsagent/research/viral-shortvideo-frameworks/`.

The full, authoritative mission spec (173 lines) lives at:

**`C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md`**

The next agent should read it in full. It contains: hard requirements (verification bar, recency cuts, dominance formula, consistency test), the measurement protocol (yt-dlp, not UI eyeballing), the orchestration plan (Phase 1 → 1.5 → 2 → 3 → 4), the extraction schema every deep-dive case study must fill, output structure, non-negotiables, quantified-parallels rules, and the acceptance checklist.

---

## 2. What's been done in this session

**Phase 1 (Discovery) — COMPLETE.** Three parallel `b0tts-researcher` sub-agents ran, partitioned by evidence TYPE (not platform):
- Agent A — course/blog authors — returned 7 candidates
- Agent B — podcast/interview regulars — returned 10 candidates
- Agent C — own-channel strategy video creators — returned 5 candidates
- Total raw pool: 22 (with overlaps)

**Phase 1.5 (Dedup + cull + authoritative yt-dlp pulls) — COMPLETE.**
- Dedup merged two multi-surfaced candidates (Zach King on B+C; Jenny Hoyos on A+B).
- Hard cuts (12 candidates rejected) — listed with one-line reasons in the shortlist file.
- Authoritative `yt-dlp --flat-playlist --playlist-end 22 --print "%(view_count)s | %(title).55s"` pulls on each survivor on its primary platform. Computed ground-truth hit_rate, hit_magnitude, and dominance via the fixed formula `dominance = 0.5 × hit_rate + 0.3 × hit_magnitude + 0.2 × activity`. Excluded ≥7-day-old videos on TikTok (via `upload_date`) and the first 1–2 rows on YouTube Shorts (per spec rule).
- Three yt-dlp cuts caught candidates the agents had rated highly:
  - Gary Vaynerchuk — true hit_rate ~0.05 (15.2M followers, ~15k median video on TikTok) — chronic underperformance
  - Alex Hormozi — true hit_rate 0.10 on YouTube Shorts (17k median on 4.4M subs) — volume-distribution; mostly flops individually
  - Peter McKinnon — true hit_rate 0.40 on Shorts (98k median on 8M subs) — below 0.6 floor

**Phase 2 (Selection gate — sign-off) — COMPLETE.**
- Shortlist evidence packet written and **user approved the shortlist** on 2026-08-13.
- **User decision: drop Mino Lee from the shortlist** (he carried `verification: PARTIAL` because TikTok bot-flag + Windows DPAPI cookie bug prevented yt-dlp verification; his documentation was also heavily MONETIZED).
- Final deep-dive roster = **10 creators** (all dominance 1.000; one caveat-flag — MrBeast, Airrack, Sam Sulek are long-form-first/hybrid).

---

## 3. Current state — exactly where to resume

**Phase 3 (Deep-dives) — NOT STARTED.** Fresh agent resumes here.

Per user's earlier sign-off, **3 per wave, stream straight through to synthesis with no per-wave checkpoints.** 10 creators → 4 waves total (Wave 1: 3, Wave 2: 3, Wave 3: 3, Wave 4: 1).

### Approved 10-creator deep-dive roster (in waves)

| Wave | Creators | Caveats |
|------|----------|---------|
| Wave 1 | Zach King, MrBeast, Dhar Mann | MrBeast carries long-form-first caveat |
| Wave 2 | Keith Lee, Airrack, Steven He | Airrack carries long-form-first caveat |
| Wave 3 | Caleb Simpson, Nick DiGiovanni, Sam Sulek | Sam Sulek carries hybrid-caveat + lightest docs (only 2 first-party sources) |
| Wave 4 | Jenny Hoyos | Carries channel-underperformance flag (median ~190k vs 12.3M subs); dominance = 0.757 |

### Per-creator starting-source pointers

(Included in full in the shortlist file; the deep-dive agents should be seeded from there — see files section below.)

- **Zach King** — https://www.youtube.com/watch?v=riyKST4L_3c — own "Movie Magic" BTS channel, 2025-04. Transcribe this first.
- **MrBeast** — Diary of a CEO 2025-02 podcast (link in shortlist).
- **Dhar Mann** — How I Built This with Guy Raz (2024-04-29).
- **Keith Lee** — The Breakfast Club (2023-12-15).
- **Airrack** — Jon Youshaei "How Airrack Made YouTube's Greatest Comeback" (2025-10).
- **Steven He** — Driven Podcast (2025-12-11).
- **Caleb Simpson** — Trading Secrets #209 (2024-11-18).
- **Nick DiGiovanni** — Colin & Samir "Cracked the YouTube Algorithm" (2025-07).
- **Sam Sulek** — Modern Wisdom #994 (2025-09-15).
- **Jenny Hoyos** — My First Million #580 (2024-05-03).

---

## 4. What the next agent must produce (Phase 3 → 4)

### Phase 3 — one fresh `b0tts-researcher` sub-agent per creator, parallel within waves

Each spawned agent gets THIS prompt shell (fresh context — they have no discovery memory):

- The full mission spec from the path above (or paste relevant chunks: extraction schema, non-negotiables, shallow-output protocol).
- One creator's entry from the shortlist file (links, sources, dominance math, best starting source).
- The shared **Extraction Schema** fields from the spec — every case study fills the same closed-vocabulary fields so the matrix is mechanical. Every populated field carries its own inline source citation.
- Instruction: produce an **exhaustive** case study at `case-studies/<category>/<creator-slug>.md` (depth-gauge met when every workflow step has ≥1 first-party source, every claim linked, verified-vs-claimed + caveats + contradictions explicit). Do NOT pad to hit a length; if sources run thin, say so and stop.
- Instruction: transcribe the best starting source via the `youtube-transcript` skill first, sample most-recent-first for any other strategy videos on the creator's own channel. Transcripts go to `b0ttsagent/temp/youtube-transcripts/`.
- Quality-gate: if shallow on re-read, re-spawn that creator's agent with a different angle prompt. If still thin, downgrade evidence tier rather than inflate.

### Phase 3.5 — case study folder taxonomy

Mirror `b0ttsagent/research/vocal-mixing-frameworks/case-studies/` pattern — sub-dirs by category. Suggested categorizations (the next agent should decide and apply consistently):
- `case-studies/vfx-illusion/` — Zach King
- `case-studies/mega-creator/` — MrBeast
- `case-studies/scripted-microdrama/` — Dhar Mann
- `case-studies/food/` — Keith Lee, Nick DiGiovanni
- `case-studies/pranks-challenges/` — Airrack
- `case-studies/comedy-skit/` — Steven He
- `case-studies/man-on-street/` — Caleb Simpson
- `case-studies/fitness/` — Sam Sulek
- `case-studies/lifestyle-storytelling/` — Jenny Hoyos

(Or coarser — agent's call, but document the choice in the README once.)

### Phase 4 — synthesis docs (write LAST, after all 10 case studies pass quality gate)

Output to `b0ttsagent/research/viral-shortvideo-frameworks/`, mirroring `vocal-mixing-frameworks/`:
- `README.md` — topic overview, methodology incl. survivorship-bias caveat (REQUIRED top of methodology), dominance-ranked creator list. "Read this first if you only read three things" pattern. Lets a new reader pick a framework in 5 min.
- `01-comparison-matrix.md` — every creator vs. the extraction-schema axes, **with a platform axis** (TikTok / Shorts / Reels / multi) and platform-agnostic-vs-specific tags. Compressed rows; open linked case study for full chain.
- `02-recurring-patterns.md` — quantified (per spec): a **claim-frequency table** `tactic → number of case studies that cite it → list of creator-slugs`. Every parallel entry references **≥2 case studies by slug + a specific source from each**. Tag every parallel `platform-agnostic` or `platform-specific`.
- `03-source-library.md` — all links organized per creator. Per-source metadata (title, URL, source date, source type, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag).

### Acceptance checklist (definition of "done and good") — verify before signing off Phase 4

All must be true:
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

The state of these checkboxes is currently `INCOMPLETE` — they get verified during Phase 4 sign-off.

---

## 5. Key files (open these to resume — they hold the work product)

| Path | Contents | Why the next agent needs it |
|------|----------|-----------------------------|
| `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md` | The full 173-line mission spec | Authoritative instructions for ALL phases — do not improvise; follow it strictly |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\viral-shortvideo-research\phase2-shortlist-for-signoff.md` | The approved 11-creator shortlist; full per-creator evidence packets with links, dominance math, best starting source. **NEXT AGENT DROPS MINO LEE (#11)** and deep-dives the other 10 | Seed every Phase 3 deep-dive sub-agent with one block from this file |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\viral-shortvideo-research\phase1-merged-and-cuts.md` | Phase 1 raw pool (22) + Phase 1.5 cuts log + yt-dlp batch results | Audit trail — only needed if a deep-dive agent surfaces a candidate question |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\README.md` | Pattern to mirror for the new README structure (file map, evidence tiers, corrections, limitations, suggested reading order) | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\01-comparison-matrix.md` | Pattern to mirror for the new matrix (Tables A/B/C with compressed rows; evidence-tier key) | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\vocal-mixing-frameworks\06-source-library.md` | Pattern to mirror for source-library structure (primary wells, verification protocol, current-monitoring) | Synthesis format reference |
| `C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\youtube-transcript\SKILL.md` | Skill instructions for transcribing YouTube strategy videos via yt-dlp | Each deep-dive agent transcribes the creator's best starting source first (sample most-recent-first; older vids are fill-in only) |
| `C:\Users\intel\DevelopmentProjectTemplate\AGENTS.md` | Project-wide agent rules (skill invocation mandate, no-SSH-VPS rule, directory map) | Don't violate — especially the "always invoke skills first" rule |

### Output locations (don't exist yet — will be created by deep-dive agents)

- `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\` — top-level output dir (already created)
- `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks\case-studies\` — case-study parent dir (already created); per-category subdirs to be created
- `C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\youtube-transcripts\` — yt-dlp transcripts land here (created on first use by the transcript skill)

---

## 6. Commands the next agent will run

### Verify the environment (one-time at session start)

```powershell
yt-dlp --version   # expected: 2026.07.04 or later; on PATH
bash --version     # expected: 5.2+ — needed by youtube-transcript skill
Test-Path -LiteralPath "C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\research\viral-shortvideo-frameworks"
```

### Verify a deep-dive candidate's views (only if a deep-dive agent disputes the dominance score)

```powershell
# YouTube Shorts (flat mode — no upload dates; exclude first 1–2 rows per spec)
yt-dlp --flat-playlist --playlist-end 22 --print "%(view_count)s | %(title).55s" --no-warnings "https://www.youtube.com/@HANDLE/shorts"

# TikTok (use upload_date to apply ≥7-day exclusion)
yt-dlp --flat-playlist --playlist-end 25 --print "%(view_count)s | %(upload_date)s | %(title).45s" --no-warnings "https://www.tiktok.com/@HANDLE"

# Verify one video's metadata (e.g., to check newest-upload date for activity score)
yt-dlp --print "%(upload_date)s | %(title).60s | %(view_count)s" --no-warnings --no-playlist "https://www.youtube.com/watch?v=VIDEOID"
```

### Known extraction issue (do not chase)

TikTok bot-flag persists on this Windows machine even with browser cookies — Chrome and Edge both fail with `Failed to decrypt with DPAPI` (yt-dlp upstream issue #10927, Windows-only). Per user's approved Phase 1 rule, the fallback for TikTok-blocked candidates was **aggregate-tracker citing SECOND-HAND flagged** — but the approved 10 have all already passed yt-dlp verification, so this issue should not recur. If a NEW Post-Phase-2 candidate surfaces, follow the same fallback.

### youtube-transcript skill invocation

Load the skill via the `skill` tool with name `youtube-transcript` BEFORE running any transcript download — the skill provides the orchestrator script and bot-flag handling protocol. Transcripts save to `b0ttsagent/temp/youtube-transcripts/` with filename `Channel_Title.txt`.

---

## 7. Open decisions (none pending — all already approved)

- ✅ Mirror `vocal-mixing-frameworks/` structure (NOT the typo'd `viral-mixing-frameworks` name from the original prompt — that folder doesn't exist)
- ✅ TikTok-fail fallback = aggregate-tracker citing SECOND-HAND flagged
- ✅ Phase 3 cadence = 3 per wave, stream straight to synthesis (no per-wave user checkpoints; only Phase 2 + final Phase 4 sign-off)
- ✅ Pure dominance ranking (no soft cap / no niche diversification)
- ✅ Final roster = 10 creators (Mino Lee dropped per user direction in this handoff message)

No further user decisions pending until Phase 4 synthesis sign-off.

---

## 8. Suggested skills for the next session

The user requires skills to be invoked when applicable (per `AGENTS.md`).

**Definitely needed:**
- `youtube-transcript` (`.agents/skills/youtube-transcript/SKILL.md`) — transcribe each creator's best starting source FIRST (their newest strategy/breakdown video) before either primary sources. Recency is the binding constraint per the spec's "Sample most-recent-first" rule. Read the SKILL.md before invoking.

**Likely needed:**
- `write-a-skill-v2` — only if you decide to extract the case-study production process as its own reusable skill (out of scope unless the user asks). Do NOT auto-invoke.
- `markdown-doc-designs` — for the final synthesis docs. The spec mandates a quality bar; this skill silently enforces psychological efficiency / scanability on Markdown. Consider invoking when writing the README and matrix.
- `mermaid-diagrams` — if synthesize any DAGs (e.g., a workflow-step dependency graph across creators). Optional.

**Do NOT invoke:**
- `create-planning-docs` / `create-execution-plan` — this is research, not project planning. The mission spec IS the plan.
- `agents-md` — already exists and is fine.
- Anything GSD-related — wrong tool family.

---

## 9. Survivorship-bias reminder (re-state in the README methodology verbatim)

These are **winners'** workflows — documented by creators who already broke out. Frameworks correlate with virality; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and an audience the reader doesn't have yet.

(Copy this text directly into `README.md` methodology per the spec's non-negotiable.)

---

## 10. First actions for the next agent

1. Read `C:\Obsidian\Repos\Main\Personal\Personal\Development\Prompts\Workspace\2026\Short Content Research V4.md` end-to-end.
2. Read `b0ttsagent/temp/viral-shortvideo-research/phase2-shortlist-for-signoff.md` — extract per-creator blocks for the deep-dive agents.
3. Load the `youtube-transcript` skill.
4. Launch **Wave 1** (3 parallel `b0tts-researcher` sub-agents): Zach King, MrBeast, Dhar Mann. Seed each with one block from the shortlist + the extraction schema from the spec + the inappropriate-terms rules.
5. When Wave 1 returns, quality-gate each case study; if any is thin, re-spawn that creator's agent with a different angle. If still thin after one re-spawn, downgrade evidence tier (write the gap explicitly, never pad).
6. Launch **Wave 2** (Keith Lee, Airrack, Steven He) — same protocol.
7. Launch **Wave 3** (Caleb Simpson, Nick DiGiovanni, Sam Sulek).
8. Launch **Wave 4** (Jenny Hoyos — solo; the channel-underperformance flag should be incorporated into the case study as a verified finding, not waved away).
9. After all 10 case studies pass quality gate, write the four synthesis docs (README, comparison-matrix, recurring-patterns, source-library) and run the acceptance checklist.

---

## 11. Redacted / sensitive info

None to redact. All evidence is public web content. No API keys, passwords, or PII were used or generated.

---

**End of handoff.**