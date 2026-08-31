# Wave 01 Report — Phase 0 Discovery

**Wave goal:** produce `working/candidates.md` with ≥20 unique, schema-complete candidates of long-form video creators with documented workflows (2021–2026, English).
**Date:** 2026-08-29
**Status:** COMPLETE — 30 unique candidates (target ≥20 met).

## Researcher status

| Lane | Researcher | Returned | Candidates written | Unique after dedup | Verdict |
|------|-----------|----------|--------------------|--------------------|---------|
| A — Course/blog authors | b0tts-researcher | ✅ | 13 | 12 | DONE |
| B — Podcast/interview circuit | b0tts-researcher | ✅ | 12 | 10 | DONE |
| C — Channel strategy-video creators | b0tts-researcher | ✅ (initial) | 13 | 3 | RETRIED |
| C — (targeted re-run) | b0tts-researcher (resumed) | ✅ | +4 new | 8 | DONE |

All 3 initial task calls returned. Lane C required one targeted re-run (see below).

## Dedup notes

- Deduped by handle, strongest row kept on collision. 10 cross-lane collisions resolved: MKBHD, Veritasium, Ali Abdaal, Matt D'Avella, Thomas Frank, Peter McKinnon, Casey Neistat, Johnny Harris, Roberto Blake, Colin and Samir.
- Kept-row attribution: MKBHD→A (Wikipedia + Skillshare + Cortex), Veritasium→C (2026 on-channel editing-process video), Ali Abdaal→A (Wikipedia + Ultimate Guide), Matt D'Avella→A, Thomas Frank→A, Peter McKinnon→B (Forbes + 2025 FroKnowsPhoto), Casey Neistat→B (2023 Digital Spaghetti), Johnny Harris→A (public team-workflow site), Roberto Blake→A, Colin and Samir→A (written playbook).
- Final per-lane counts: **A=12, B=10, C=8** (all ≥4). Total **30 unique**.

## Anomalies

- **Lane C initial under-contribution:** first pass returned 13 rows but 10 duplicated lanes A/B, leaving only 3 unique (Dan Mace, Wendover, Linus). Failed the "≥4 per lane" QA item → re-ran Lane C once with a targeted prompt (resumed same session) to find non-duplicate channel-strategy-video creators. Added Solar Sands, Patrick Willems, Thomas Flight, Mina Le → Lane C unique = 8. No further retry needed.
- **SearXNG MCP returned empty** for all researchers (expected); all fell back to `websearch` per skill guidance.
- **Weak/flagged rows for Phase 1 scrutiny:** Peter McKinnon (SECOND-HAND-only written workflow; best doc 2017 outside window), Safiya Nygaard (SECOND-HAND-only, doc 2020 edge), Johnny Harris (Patreon locked / SECOND-HAND for open web), Wendover (Nebula creator-owned, SECOND-HAND for YouTube), Linus (forum post, factory video SECOND-HAND), Mina Le (SECOND-HAND interview framing, no on-channel workflow video), Patrick Willems & Thomas Flight (docs predate 2021 window), Paddy Galloway (role unconfirmed as primary talent), Roberto Blake (median views below 100k), Dan Koe (no Wikipedia).
- **Common-name collisions disambiguated** in rows (e.g. "Sean Cannell – Think Media", "Marques Brownlee – MKBHD", "Sam Denby — Wendover Productions", "Linus Sebastian — Linus Tech Tips").

## Lead QA checklist

- [x] Dedup done — no duplicate handles in candidates.md (verified programmatically)
- [x] Every row has verification-lead + channel + first-party doc URL (verified all 30)
- [x] No lane contributed <4 final candidates (A=12, B=10, C=8)
- [x] Weak rows flagged with `SECOND-HAND-only` / `role unconfirmed` / date flags for Phase 1
- [x] Common-name collisions disambiguated (product/channel in row)

## Next actions

1. **Phase 1 (verification):** run view-count / verification tests on the 30 candidates; prioritize the 10m+/video anchors (MrBeast, Mark Rober, MKBHD, Johnny Harris) and resolve flagged rows (Peter McKinnon, Safiya, Wendover, Linus, Mina Le, Patrick Willems, Thomas Flight).
2. Confirm 2021–2026 first-party doc freshness for edge-dated rows (Patrick Willems, Thomas Flight, Safiya).
3. Consider whether Paddy Galloway (strategist, not primary talent) and Roberto Blake (sub-100k median) survive the strict bar; may be dropped in Phase 1.