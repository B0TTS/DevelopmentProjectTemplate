# MANIFEST — ui-design-workflows research run

- Research date: 2026-08-17
- Verification window: 2021-08-17 → 2026-08-17
- Target: 12 verified PASS + 12 full depth docs (floor 10; user decision 2026-08-17, supersedes earlier stop-at-8)
- Depth docs: all verified, in ranking order; spares from verified pool on DEPTH-REJECT
- Orchestrator: main agent · Phase leads: `b0tts-general-agent` (never spawns) · Wave leads: `b0tts-lead-researcher` (only spawner) · Researchers: `b0tts-researcher` · Misc non-lead: `explore`
- Tooling: SearXNG first (try once, may be empty from subagent context) → `websearch` (Exa) → `web_search` (metasearch2, last resort)
- Pauses: none — run to end

## Waves

| # | Phase | Result | Counts | Next action |
|---|-------|--------|--------|-------------|
| 01 | 0 (Discovery) | PASS | 44 unique candidates (A17/B13/C14), 22 weak-flagged, phase gate 4/4 | Wave 02: verify 4 strongest in-window candidates |
| 02 | 1 (Verification) | PASS | 4/4 PASS (Wathan usage-stat, shadcn usage-stat, Otto usage-stat, Herbert award ADA-2022), pool=4 | Wave 03: Saarinen, McLeod, Bostock, Schoger |
| 03 | 1 (Verification) | PASS | 3 PASS (McLeod award ADA-2024, Bostock usage-stat, Schoger usage-stat) / 1 REJECT (Saarinen tier3-only), pool=7 | Wave 04: Verou, Stoiber, Ahlin Bjerrome, Prangley |
| 04 | 1 (Verification) | PASS | 4 PASS (Verou usage-stat, Stoiber usage-stat, Ahlin MAU-flagged, Prangley revenue-weak), pool=11, 2 anomalies adjudicated by orchestrator | Wave 05: Ahlin MAU re-check + Palmer, Kus, Perry |
| 05 | 1 (Verification) | PASS | 1 PASS (Palmer usage-stat) / 3 REJECT (Ahlin no-public-MAU, Kus no-SOTM, Perry engineering-credit), pool=11 | Wave 06: Sorhus, Gage, Flarup, Stollenmayer |
| 06 | 1 (Verification) | PASS | 1 PASS (Stollenmayer award ADA-2025) / 2 REJECT (Gage no-award, Flarup tier3-only) / 1 FAIL-UNKNOWN (Sorhus — not needed), pool=12 TARGET MET | Phase 1 close: gate + ranking; then Phase 2 waves |
| P1 | 1 close | PASS | 12 PASS / 6 REJECT / 1 FAIL-UNKNOWN; ranked 1-12 for depth docs | Wave 07: depth docs Wathan, Otto, Bostock, shadcn |
| 07 | 2 (Depth docs) | PASS | 3 DEPTH-PASS (Wathan, Otto, Bostock) / 1 DEPTH-REJECT (shadcn principles-only), docs=3 | Wave 08: depth docs Verou, Schoger, Stollenmayer, Herbert |
| 08 | 2 (Depth docs) | PASS | 4/4 DEPTH-PASS (Verou, Schoger, Stollenmayer, Herbert), docs=7 | Wave 09: depth docs McLeod, Stoiber, Palmer, Prangley |
