# Wave 01 Report — Phase 0: Candidate Discovery

- Wave: 01 · Phase: 0 (candidate discovery) · Date: 2026-08-17
- Goal: ≥20 unique, schema-complete candidates in `working/candidates.md`
- Status: **COMPLETE** — 44 unique candidates (goal ≥20)

## Per-researcher status

| Lane | Researcher | Status | Rows written | Verdict |
|------|-----------|--------|--------------|---------|
| A — consumer/B2B SaaS/marketing | b0tts-researcher (ses_fee230f54ffeH4g1wvkXA2Oulw) | done | 17 | PASS |
| B — dev tools/open source | b0tts-researcher (ses_fee2307b2ffeO3kzs5CPVjP9iY) | done | 14 | PASS |
| C — mobile/games/niche | b0tts-researcher (ses_fee22ffdaffeNrYS6LrBVu0Psl) | done | 14 | PASS |

No retries required. All three researchers completed on first attempt.

## QA checklist results

- [x] All 3 lane files exist with ≥7 rows each — A: 17, B: 14, C: 14 (counted lines starting `- **`)
- [x] Every row has name + ≥1 scale lead URL + ≥1 first-party doc URL — 0 rows missing either URL across all 3 files
- [x] Dedup by name done — 45 raw rows → 44 unique; **Steve Schoger** appeared in lanes A and B, merged into one row (kept in Lane A section, `[merged from lanes A+B]` noted). No same-name/different-person collisions found.
- [x] Lane balance in merged file — A: 17, B: 13, C: 14 (all ≥4)
- [x] Weak rows flagged `?` in notes — present throughout (see anomalies)
- [x] `report-01.md` written with per-researcher status + merged count + anomalies

## Merged output

- File: `working/candidates.md` — 44 unique rows (17 + 13 + 14)
- Row schema: `- **Name** — products: … — route: … — scale lead: <url> — first-party doc: <url> — notes: …` (fixed, all rows conform)

## Anomalies

1. **SearXNG flakiness (all lanes)** — `searxng_searxng_web_search` intermittently returned empty mid-run for all three researchers; each fell back to `websearch` (Exa) per skill routing. No data loss; expected behavior.
2. **Lane B — engineer-creator rows** — 5 rows (Zeno Rocha, Nicolas Gallagher, Andrey Sitnik, Matt Perry, Paul Henschel) are individually-credited tool creators who are engineers rather than visual designers; included under the lane's "designers/creators" reading and flagged in notes. Sindre Sorhus flagged `?` for thin written process content. Downstream should decide whether strict visual-design credit is required.
3. **Lane C — award corrections** — Researcher C corrected false leads against the Wikipedia ADA winners list: Storyteller, Dicey Dungeons, and Thermo are NOT ADA winners (rows flagged `?` accordingly). Daniel Benmergui's personal site is down (GDC talk/interview used as first-party doc). Marc Edwards flagged as Mac-niche, not mobile.
4. **Lane A — unverified scale figures** — several revenue/audience figures are self-disclosed or third-party (Meng To 35k readers, Ran Segall $250k/yr, Chris Do $4.9M, Mike Kus award list, Dann Petty award wins) — all flagged `?`. Karri Saarinen, Julie Zhuo, Brad Frost, Ethan Marcotte, Frank Chimero, Erika Hall, Tobias Ahlin Bjerrome are the strongest un-flagged rows.
5. **No verification performed** — per wave spec, this wave is discovery-only. Verification window 2021-08-17 → 2026-08-17 is context for later waves.

## Next actions

1. **Wave 2 (verification)** — verify scale leads for the strongest candidates: MAU/revenue figures (Lane A), GitHub stars/npm downloads (Lane B), ADA/award claims + sales figures (Lane C). Focus on un-flagged rows first.
2. **Lane B triage decision** — decide whether engineer-creator rows (5 flagged) stay in the candidate pool or move to a secondary list.
3. **Subset selection** — 44 candidates far exceeds the ≥20 goal; downstream waves can select a balanced subset (e.g., top ~8 per lane) for deep verification.
4. **Re-check dead links** — danielbenmergui.com (down), gregwohlwend.com (thin) — may need alternate first-party docs during verification.