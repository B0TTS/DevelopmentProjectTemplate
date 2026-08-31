# Wave 05 Report — Phase 1 Verification (wave 4 of N)

**Date:** 2026-08-29
**Wave goal:** verify 4 candidates (Drew Gooden, Wendover Productions, Solar Sands, Dan Mace) with the strict protocol from wave-02.md.
**Run-wide PASS bank:** 11 prior + 3 this wave = **14 PASS** (target ≥12, prefer 15). One REJECT this wave.

## Per-worker status

| Candidate | Verdict | JSON path | One-line reason |
|---|---|---|---|
| Drew Gooden (@drewgooden) | **PASS** | `working/evidence/drew-gooden-2026-08-29.json` | 12/12 eligible >100k, median 4,697,784, hit_rate 1.0, activity 1.0, dominance 0.735; verified 4.87M; 2024-03-08 Anthony Padilla first-party workflow doc in window. |
| Wendover Productions (Sam Denby) | **PASS** | `working/evidence/wendover-productions-2026-08-29.json` | Verified 4.91M/831M; 12/12 >100k, median 859,858, dominance 0.543; docs 2021-11-17 Nebula FIRST-PARTY + 2026-05-12 Oxford Union in window. Sub-1M median, not top anchor. |
| Solar Sands (@solarsands) | **REJECT** | `working/evidence/solar-sands-2026-08-29.json` | Documentation gate fails: row's doc URL is The Nth Company (23.1k), not Solar Sands; exhaustive search (181 titles + web + Patreon) found no 2021–2026 public first-party workflow doc. Consistency 8/12 (66.7%, median 601k, dominance 0.33) would pass, but borderline is REJECT. |
| Dan Mace (@DanMace) | **PASS** | `working/evidence/dan-mace-2026-08-29.json` | Verified channel + 10yr Cannes/Beast Philanthropy career; 2024-04-14 first-party doc in window; 10/12 >100k (83.3%, median 391,782), dominance 0.269; dormancy 274d = activity 0 but 1.5M/2.5M hits keep recency PASS. |

## Lead QA checklist

- [x] all 4 `working/evidence/*.json` exist
- [x] every PASS JSON contains hit_rate, median_views, dominance inputs + arithmetic (verified arithmetic for all 3 PASS files)
- [x] counts came from `python -m yt_dlp` pulls, not aggregator estimates — per_video counts are exact integers (e.g. drew-gooden 2,454,281…7,430,720; wendover 853,979…1,438,503; dan-mace 44,381…2,536,471; solar-sands 28,566…1,226,780), all 12 eligible rows each
- [x] every REJECT JSON contains rejection_reason and dead_ends_searched (solar-sands has both)
- [x] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN — none occurred; all 4 workers completed on first attempt

## Anomalies

1. **Handle mismatch (Drew Gooden):** candidates.md lists `@drewgooden`, which resolves to an unrelated NBA channel (167 followers). Worker correctly identified the comedy creator's actual handle `@drewisgooden` (UCTSRIY3GLFYIpkR2QwyeklA) and used it for all yt-dlp counts. **Recommend updating candidates.md handle to `@drewisgooden`.**
2. **Bad doc URL (Solar Sands):** candidates.md row's first-party doc URL `https://www.youtube.com/watch?v=-n-cDjfHp1c` is The Nth Company (23.1k subs), not Solar Sands. This was the primary documentation evidence and its invalidation drove the REJECT. **Recommend correcting/removing this URL in candidates.md.**
3. **Dan Mace dormancy:** newest upload 2025-11-28 (274 days) → activity 0.0, but 2024–2025 hits (1.5M/2.5M) keep recency PASS. Flag as lower-activity PASS.

## Next actions

- Update candidates.md: fix Drew Gooden handle → `@drewisgooden`; correct/remove Solar Sands doc URL.
- Run-wide PASS now 14 (target ≥12, prefer 15). One more PASS would hit the preferred 15 — consider one more verification wave if roster remains.
- Solar Sands REJECT is documentation-only; if a valid 2021–2026 first-party workflow doc surfaces later, candidate could be re-verified.