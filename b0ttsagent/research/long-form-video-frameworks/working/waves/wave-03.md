# Wave 03 — Phase 1 Verification (wave 2 of N)

**Wave goal:** verify 4 more candidates with the same strict protocol as wave-02. Run-wide: 4/12 PASS banked; target ≥12 PASS (prefer 15).

**Phase:** 1 (Verification). Inputs: `working/candidates.md` + `working/MANIFEST.md` + `working/waves/wave-02.md` (protocol reference).

**Roster (one worker per candidate, parallel):**
1. Veritasium (Derek Muller) — https://www.youtube.com/@veritasium — slug `veritasium`
2. Ryan Trahan — https://www.youtube.com/@RyanTrahan — slug `ryan-trahan`
3. Ali Abdaal — https://www.youtube.com/@aliabdaal — slug `ali-abdaal`
4. Tom Scott — https://www.youtube.com/@TomScottGo — slug `tom-scott`

Each worker gets their candidate's full row from `working/candidates.md`.

**WORKER TYPE: `b0tts-general-agent`** (they have shell for yt-dlp — b0tts-researcher lacks shell; do not use it for verification). Lead spawns all workers in ONE message, parallel.

**Per-worker task prompt** (give verbatim, with the candidate name + row filled in):

> You are a Phase 1 verification researcher (worker type: b0tts-general-agent — you HAVE shell access). Read `working/waves/wave-02.md` sections "Verification checks" and "Measurement protocol" before starting — they define the 6 checks and the exact yt-dlp commands. Your candidate: **[NAME — handle]** — row from candidates.md: <paste row>. Run the 6 checks in order: verification bar → recency → consistency test → dominance score → documentation requirement → magnitude note. Use `python -m yt_dlp` in your shell for ALL view counts (bare `yt-dlp` is not on PATH). Use `websearch` for career evidence and doc-source dating; read a page before citing it. Write the full record to `working/evidence/<slug>-2026-08-29.json` per the schema in wave-02.md. Verdict: PASS or REJECT (a REJECT needs a reason + dead-ends searched). Do NOT lower any gate — borderline is REJECT. Final message ≤250 words: verdict, JSON path, one-line reason. Never paste JSON content into your final message.

**Completion criteria:** 4 evidence JSONs on disk with exact yt-dlp counts; every PASS backed by hit-rate figure + dominance arithmetic; every REJECT has a reason + dead-ends.

**Lead QA checklist:**
- [ ] all 4 `working/evidence/*.json` exist
- [ ] every PASS JSON contains hit_rate, median_views, dominance inputs + arithmetic
- [ ] counts came from `python -m yt_dlp` pulls, not aggregator estimates (check per_video counts + dead_ends_searched)
- [ ] every REJECT JSON contains rejection_reason and dead_ends_searched
- [ ] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN

**Lead output:** `working/waves/report-03.md` — per-worker status, anomalies, next actions. Lead final message ≤500 words.

**Context budget:** workers → disk only, ≤250-word finals. Lead reads only this spec + wave-02 protocol + worker summaries. Never read full evidence JSONs into context.
