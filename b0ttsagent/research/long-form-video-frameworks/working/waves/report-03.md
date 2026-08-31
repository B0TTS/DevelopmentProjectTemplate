# Wave 03 Report — Phase 1 Verification (wave 2 of N)

Date: 2026-08-29. Wave goal: verify 4 more candidates (Veritasium, Ryan Trahan, Ali Abdaal, Tom Scott) with the strict wave-02 protocol. Worker type: `b0tts-general-agent` (shell access for yt-dlp). Run-wide PASS target ≥12 (prefer 15).

## Per-worker status

| Candidate | Verdict | JSON path | One-line reason |
|---|---|---|---|
| Veritasium (@veritasium) | PASS | `working/evidence/veritasium-2026-08-29.json` | 12/12 eligible >100k (hit_rate 1.0, median 6,817,628), newest 2026-08-17, dominance 0.841, first-party docs (The Future of Veritasium 2025-12-24 + Fireside 2026-02-27), 1m+ tier. |
| Ryan Trahan (@RyanTrahan) | PASS | `working/evidence/ryan-trahan-2026-08-29.json` | 12/12 >100k (hit_rate 1.0, median 2,323,887), newest 2026-07-18, dominance 0.516, 3 workflow docs 2022–2025 (YouTube Blog, Colin & Samir 2025-07-13, Editing Podcast), 1m+ tier. |
| Ali Abdaal (@aliabdaal) | REJECT | `working/evidence/ali-abdaal-2026-08-29.json` | Consistency 6/12 = 50% >100k (median 101,841) < 60% gate; even generous newest-exclusions (50% / 58.3%) stay <60%. Strong docs + 6.68M subs but recent long-form window fails. Dominance 0.355. |
| Tom Scott (@TomScottGo) | PASS | `working/evidence/tom-scott-2026-08-29.json` | 12/12 >100k (hit_rate 1.0, median 864,985), newest 2026-08-24, dominance 0.543, 3 English docs 2021–2026 (Waveform 2022-06-03, Waveform Clips 2022-06-08, WIRED Tech Support 2026-06-02). Magnitude just below 1m+ tier but perfect consistency sustains PASS. |

Verdicts: 3 PASS, 1 REJECT. Run-wide PASS count now **7** (wave-02: 4 + wave-03: 3). Target ≥12 — more waves needed.

## Lead QA checklist

- [x] all 4 `working/evidence/*.json` exist (veritasium, ryan-trahan, ali-abdaal, tom-scott)
- [x] every PASS JSON contains hit_rate, median_views, and dominance inputs + arithmetic (verified all 3: 0.841 / 0.516 / 0.543 reconcile exactly)
- [x] counts came from `python -m yt_dlp` pulls, not aggregator estimates — all per_video counts are exact non-rounded values; dead_ends_searched confirms per-watch-page verification (e.g., Ali Abdaal IDs fEMHMd7fovM…CFBEih785-I; Ryan Trahan resolved handle 404 via channel ID UCnmGIkw-KdI0W5siakKPKog)
- [x] REJECT JSON (ali-abdaal) contains rejection_reason + dead_ends_searched
- [x] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN — N/A, all 4 completed on first spawn

### yt-dlp exact-count verification (critical)
Lead spot-checked per_video arrays via targeted grep. All counts are exact (non-rounded) yt-dlp pulls — no aggregator estimates. Medians reconcile with the reported hit_rate/magnitude arithmetic for all 3 PASSes and the 1 REJECT.

## Anomalies

1. **Ryan Trahan handle 404** — `@RyanTrahan/videos` flat-playlist returned 404; worker resolved via channel ID `UCnmGIkw-KdI0W5siakKPKog` (verified via websearch + YouTube Blog channel link). Counts unaffected; recorded in dead_ends_searched.
2. **Ali Abdaal borderline REJECT** — strong documentation (2023/2025 first-party guides) and 6.68M-sub career, but recent 12-video long-form window is 50% >100k with median ~102k. Per protocol, borderline = REJECT; gate not lowered. This is a documentation-rich candidate that fails only on current view consistency — worth noting for any future "workflow-doc quality" sub-analysis, but not a shortlist PASS.
3. **Tom Scott magnitude** — median 864,985 sits just below the 1m+ prioritized tier; PASS sustained by perfect 12/12 consistency + strong 2021–2026 docs. Flag for ranking (not a 1m+ tier anchor).

## Next actions

- Wave 4+ to reach run-wide target ≥12 PASS (currently 7). Remaining strong candidates from candidates.md: Thomas Frank, Matt D'Avella, Dan Koe, Colin and Samir, Kurtis Conner, Drew Gooden, Wendover, Solar Sands, Dan Mace, Linus Tech Tips.
- Continue `b0tts-general-agent` workers (shell access) for all view-count measurement.
- Watch Tom Scott as sub-1m-tier (not a 1m+ anchor) when ranking shortlist; Veritasium and Ryan Trahan are the 1m+ tier additions this wave. MrBeast and Mark Rober remain the 10m+ anchors.