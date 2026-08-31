# Wave 04 Report — Phase 1 Verification (wave 3 of N)

Date: 2026-08-29. Wave goal: verify 4 candidates (Thomas Frank, Matt D'Avella, Colin and Samir, Kurtis Conner) with the strict wave-02 protocol. All 4 workers were `b0tts-general-agent` (shell access for yt-dlp), spawned in parallel in one message.

## Per-worker status

| Candidate | Verdict | JSON path | One-line reason |
|---|---|---|---|
| Thomas Frank (@Thomasfrank) | PASS | `working/evidence/thomas-frank-2026-08-29.json` | 10/12 last eligible >100k (83.3%, median 215,433) via exact yt-dlp; FIRST-PARTY docs Creator's Companion (2026-07-31, MONETIZED) + Ultimate Guide (2023-07-19, INDEPENDENT); verified 3.01M subs/186M views; dominance 0.261 (activity 0 — newest 2024-03-22, dormant). |
| Matt D'Avella (@mattdavella) | PASS | `working/evidence/matt-davella-2026-08-29.json` | 12/12 eligible >100k (100%, median 556k) via exact yt-dlp; Emmy-nominated Netflix director, 4.04M subs; FIRST-PARTY Master YouTube 5-stage workflow (2022–2026, MONETIZED); dominance 0.428. |
| Colin and Samir (@ColinandSamir) | PASS | `working/evidence/colin-and-samir-2026-08-29.json` | 10/12 >100k (83.3%, median 197,541) via exact yt-dlp; 1.63M subs; FIRST-PARTY monetized Growth Playbook (2024–2025, 3 Rules workflow) + 2 companion videos; dominance 0.460 (activity 1.0). |
| Kurtis Conner (@kurtisConner) | PASS | `working/evidence/kurtis-conner-2026-08-29.json` | 12/12 >100k (100%, median 4,103,208) via exact yt-dlp; 5.68M subs, long career 2013–present; FIRST-PARTY docs Colin & Samir (2023-11-08) + Anthony Padilla (2023-03-31); dominance 0.705, 1m+ tier. |

## Lead QA checklist

- [x] all 4 `working/evidence/*.json` exist
- [x] every PASS JSON contains hit_rate, median_views, dominance inputs + arithmetic (verified independently)
- [x] counts came from `python -m yt_dlp` pulls, not aggregator estimates (per_video = 12 exact counts each; dead_ends_searched documents yt-dlp usage + per-video date/duration verification; no estimate-grade counts)
- [x] every REJECT JSON contains rejection_reason and dead_ends_searched — N/A (no REJECTs this wave)
- [x] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN — N/A (no failures)

## Dominance scores (PASSes)

- Kurtis Conner: 0.705 (hit_rate 1.0, magnitude 0.4103, activity 1.0)
- Colin and Samir: 0.460 (hit_rate 0.833, magnitude 0.0198, activity 1.0)
- Matt D'Avella: 0.428 (hit_rate 1.0, magnitude 0.0556, activity 0.5)
- Thomas Frank: 0.261 (hit_rate 0.833, magnitude 0.0215, activity 0.0)

## Anomalies

- Thomas Frank is dormant (newest upload 2024-03-22, 890 days) → activity 0.0, lowest dominance of the wave. Passes gates (hits within 2021–2026, 83.3% hit-rate) but flagged as sub-1M median, not top-anchor tier.
- Matt D'Avella's Wikipedia verification lead is a 404 (no English Wikipedia page); worker fell back to Variety Emmy nomination + Leaders.com + Wikipedia "Less Is Now" credit. Career evidence still solid.
- Colin and Samir's playbook page has no explicit publish date; worker used copyright footer + Passionfruit/Arcmira coverage as dating proxies (2024-01-24). Acceptable within window.
- Kurtis Conner's doc date was previously "not clearly listed"; worker located explicit 2023-11-08 header date. Resolved.

## Next actions

- Run-wide PASS count now 11 (7 prior + 4 this wave). Target ≥12 (prefer 15) → 1 more PASS needed to hit floor; 4 more to hit preferred target.
- Recommend Wave 05 verify remaining strong candidates (e.g., Dan Koe, Sean Cannell, Ryan Trahan already banked, Casey Neistat, Drew Gooden, Safiya Nygaard, Peter McKinnon, Dan Mace, Wendover, Solar Sands, Mina Le, Veritasium already banked) to reach 15.
- No re-runs required this wave.