# Wave 02 Report — Phase 1 Verification (re-run)

Date: 2026-08-29. Wave goal: strict verification bar + consistency test + dominance score on 4 anchor candidates; one evidence JSON per candidate. Worker type: `b0tts-general-agent` (shell access) — replaces prior `b0tts-researcher` run that produced estimate-grade counts.

## Per-worker status

| Candidate | Verdict | JSON path | One-line reason |
|---|---|---|---|
| MrBeast (@MrBeast) | PASS | `working/evidence/mrbeast-2026-08-29.json` | 12/12 eligible >100k (hit_rate 1.0, median 111,467,670), newest 2026-08-22, dominance 1.0, 3 docs (2 first-party), 10m+ anchor. |
| Mark Rober (@MarkRober) | PASS | `working/evidence/mark-rober-2026-08-29.json` | 12/12 >100k (hit_rate 1.0, median 28,199,830), newest 2026-06-20, dominance 0.9, 3× first-party docs, 10m+ anchor. |
| MKBHD (@MKBHD) | PASS | `working/evidence/mkbhd-2026-08-29.json` | 12/12 >100k (hit_rate 1.0, median 3,071,970), newest 2026-08-24, dominance 0.654, 4 first-party docs (Skillshare flagged platform-hosted MONETIZED). |
| Johnny Harris (@johnnyharris) | PASS | `working/evidence/johnny-harris-2026-08-29.json` | 12/12 >100k (hit_rate 1.0, median 3,475,773), newest 2026-08-13, dominance 0.67, first-party 2021 Join The Team + 2025 How I Write, 1m+ tier. |

All 4 verdicts PASS. Run-wide PASS count: 4 (target ≥12 across run — more waves needed).

## Lead QA checklist

- [x] all 4 `working/evidence/*.json` exist
- [x] every PASS JSON contains hit_rate, median_views, and dominance inputs + arithmetic
- [x] every REJECT JSON contains rejection_reason + dead_ends_searched (N/A — all PASS; dead_ends_searched present in all)
- [x] PASS count in report (4) matches PASS JSONs on disk (4)
- [x] FAIL-UNKNOWN researchers retried once before recording FAIL-UNKNOWN

### yt-dlp exact-count verification (critical)
Lead independently re-ran `python -m yt_dlp --flat-playlist --playlist-end 12` for all 4 handles. Every per_video count in the JSONs is an exact (non-rounded) yt-dlp pull — no aggregator estimates. Medians reconcile exactly with lead's spot-checks:
- MrBeast: 103,391,655 / 119,543,685 → median 111,467,670 ✓
- Mark Rober: 27,053,725 / 29,345,934 → median 28,199,830 ✓
- MKBHD: 2,725,051 / 3,418,890 → median 3,071,970 ✓
- Johnny Harris: 3,167,515 / 3,784,031 → median 3,475,773 ✓

Eligibility filtering confirmed: each worker excluded <14-day uploads and podcast/Short-style videos (e.g., Johnny Harris excluded the Max Fisher interview; MKBHD excluded 2 newest; MrBeast excluded newest) and pulled the next eligible video — consistent with protocol. Dominance arithmetic verified for all 4 (0.3×hit_rate + 0.5×hit_magnitude + 0.2×activity).

## Anomalies

1. **Johnny Harris worker failed on first spawn** — provider error (`invalid_api_key` / Console Go upstream failure), not a research failure. Retried once with identical spec; succeeded on retry. No FAIL-UNKNOWN recorded.
2. **MKBHD doc URL is Skillshare-hosted** — flagged platform-hosted MONETIZED (first-party MKBHD course content, third-party platform). Noted in JSON; does not block PASS.
3. **MrBeast sub count** — worker cites 500M (Official Blog 2026-06-12) vs 515M (yt-dlp); both recorded as career evidence. No impact on verdict.

## Next actions

- Wave 3+ to reach run-wide target of ≥12 PASS (currently 4). Remaining strong candidates from candidates.md: Ali Abdaal, Thomas Frank, Matt D'Avella, Dan Koe, Colin and Samir, Ryan Trahan, Tom Scott, Kurtis Conner, Drew Gooden, Veritasium, Wendover, Solar Sands.
- Continue using `b0tts-general-agent` workers (shell access) for all view-count measurement.
- Watch MKBHD/Johnny Harris as 1m+ tier (not 10m+ anchors) when ranking shortlist; MrBeast and Mark Rober are the 10m+ anchors.