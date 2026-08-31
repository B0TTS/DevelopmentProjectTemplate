# Wave 02 — Phase 1 Verification (wave 1 of N)

**Wave goal:** run the strict verification bar + consistency test + dominance score on 4 anchor candidates; write one evidence JSON per candidate. Target run-wide: ≥12 PASS (prefer 15) before stopping.

**Phase:** 1 (Verification). Input: `working/candidates.md` + `working/MANIFEST.md`.

**Roster (one worker per candidate, parallel):**
1. MrBeast — https://www.youtube.com/@MrBeast — slug `mrbeast`
2. Mark Rober — https://www.youtube.com/@MarkRober — slug `mark-rober`
3. MKBHD (Marques Brownlee) — https://www.youtube.com/@MKBHD — slug `mkbhd`
4. Johnny Harris — https://www.youtube.com/@johnnyharris — slug `johnny-harris`

Each worker gets their candidate's full row from `working/candidates.md`.

**WORKER TYPE: `b0tts-general-agent`** — NOT `b0tts-researcher`. A prior run with b0tts-researcher workers failed: they have no shell tool and could not run the yt-dlp measurement protocol (fell back to estimate-grade aggregators). b0tts-general-agent workers have shell access. The lead (b0tts-lead-researcher) is still the one who spawns them, in ONE message, parallel.

**Per-worker task prompt** (give verbatim, with the candidate name + row filled in):

> You are a Phase 1 verification researcher (worker type: b0tts-general-agent — you HAVE shell access; the previous researcher type lacked it). Read `working/waves/wave-02.md` sections "Verification checks" and "Measurement protocol" before starting. Your candidate: **[NAME — handle]** — row from candidates.md: <paste row>. Run the 6 checks in order: verification bar → recency → consistency test → dominance score → documentation requirement → magnitude note. Use `python -m yt_dlp` in your shell for ALL view counts (bare `yt-dlp` is not on PATH). Use `websearch` for career evidence and doc-source dating; read a page before citing it. Write the full record to `working/evidence/<slug>-2026-08-29.json` per the schema below, OVERWRITING any existing file at that path (an earlier estimate-grade version exists). Verdict: PASS or REJECT (a REJECT needs a reason + dead-ends searched). Do NOT lower any gate — borderline is REJECT. Final message ≤250 words: verdict, JSON path, one-line reason. Never paste JSON content into your final message.

**Verification checks (researchers read this):**
1. **Verification bar** — creator verified (checkmark) OR long public career; PLUS consistent evidence of 100k+ views per video; PLUS verifiable career evidence (sub counts, documented earnings/brand deals, media coverage, platform stats). Borderline → REJECT.
2. **Recency** — hits within 2021–2026 (flat mode returns no dates: pull dates for the newest few videos individually); documentation sources must be 2021–2026 (use each doc's published date). Every citation carries a `still-current as of 2026?` flag: YES / NO / UNCLEAR + one-line reason. Hits or documentation frozen pre-2021 → REJECT.
3. **Consistency test** — ≥60% of the creator's last 12 eligible videos exceed 100k views, evidenced by per-video counts (never channel-level claims). Report median views. Exclude videos <14 days old (flat mode has no dates → exclude the first 1–2 rows). Exclude Shorts/livestreams/podcasts by title; pull durations individually if ambiguous.
4. **Dominance score** — `dominance = 0.3 × hit_rate + 0.5 × hit_magnitude + 0.2 × activity`. hit_rate (0–1) = share of last 12 eligible >100k. hit_magnitude = median views ÷ 10,000,000, capped 1.0. activity: newest upload ≤30 days = 1.0, ≤90 days = 0.5, older = 0. Report all three inputs + the arithmetic.
5. **Documentation requirement** — creator must have publicly explained their workflow. Flag each source: FIRST-PARTY vs SECOND-HAND; MONETIZED vs INDEPENDENT. English documentation only.
6. **Magnitude note** — tier: 1m+ median prioritized; 10m+/video anchors the top of the shortlist.

**Measurement protocol:**
```bash
python -m yt_dlp --flat-playlist --playlist-end 12 --print "%(view_count)s | %(title).50s" "https://www.youtube.com/@HANDLE/videos"
python -m yt_dlp --flat-playlist --playlist-end 12 --print "%(id)s | %(title).40s" "https://www.youtube.com/@HANDLE/videos"
# per newest few videos individually (dates + exact counts):
python -m yt_dlp --print "%(upload_date)s | %(view_count)s | %(duration)s | %(title).40s" "https://www.youtube.com/watch?v=<ID>"
# optional channel sub count:
python -m yt_dlp --flat-playlist --playlist-end 1 --print "%(channel_follower_count)s | %(uploader)s" "https://www.youtube.com/@HANDLE/videos"
```

**Evidence JSON schema** (`working/evidence/<slug>-2026-08-29.json`):
```json
{
  "name": "", "handle": "", "platform": "YouTube", "niche_format": "",
  "verification": { "status": "PASS|REJECT", "career_evidence": [{"claim": "", "link": "", "still_current_2026": "YES|NO|UNCLEAR + reason"}] },
  "recency": { "newest_upload_dates": [""], "doc_sources": [{"title": "", "url": "", "date": "", "still_current_2026": ""}] },
  "consistency": { "hit_rate": 0.0, "median_views": 0, "per_video": [{"title": "", "views": 0, "eligible": true}], "excluded_new_uploads": 0 },
  "dominance": { "score": 0.0, "hit_rate_input": 0.0, "hit_magnitude_input": 0.0, "activity_input": 0, "arithmetic": "" },
  "documentation": [{"title": "", "url": "", "date": "", "provenance": "FIRST-PARTY|SECOND-HAND", "monetized": "MONETIZED|INDEPENDENT"}],
  "magnitude_note": "", "verdict": "PASS|REJECT", "rejection_reason": "", "dead_ends_searched": []
}
```

**Completion criteria:** 4 evidence JSONs on disk with EXACT yt-dlp view counts (not aggregator estimates); every PASS backed by hit-rate figure + dominance arithmetic inside the JSON (PASS with no numbers = flag + re-run); every REJECT has a reason + dead-ends.

**Lead QA checklist:**
- [ ] all 4 `working/evidence/*.json` exist
- [ ] every PASS JSON contains hit_rate, median_views, and dominance inputs + arithmetic
- [ ] every REJECT JSON contains rejection_reason and dead_ends_searched
- [ ] PASS count in report matches PASS JSONs on disk
- [ ] FAIL-UNKNOWN researchers retried once before recording FAIL-UNKNOWN

**Lead output:** `working/waves/report-02.md` — per-researcher status (candidate, verdict, path, one-line reason), anomalies, next actions. Lead final message ≤500 words.

**Context budget:** researchers → disk only, ≤250-word finals. Lead reads only this spec + researcher summaries. Never read full evidence JSONs into context.
