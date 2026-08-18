# Wave 06 — Phase 1: Verification (wave 5 of N)

- Phase: 1 (Verification)
- Goal: verdict for 4 candidates — running pool: 11 PASS, target >=12
- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, one candidate each, parallel fanout
- Input: `working/candidates.md` (their rows)

## Verification standard (send with every researcher — the 4 checks, in order, stop at first failure)

1. **Individual attribution** — name publicly tied to a shipped product (portfolio / LinkedIn / credits / press "designed by"). Team or design-system credit alone → REJECT `team-credit`.
2. **In-window** — the scale/award evidence is dated within 2021-08-17 → 2026-08-17. For usage-stat: fetch LIVE numbers today and record the fetch date (live data is in-window by definition). Out-of-window with nothing recent → REJECT `out-of-window`.
3. **Scale evidence** — exactly one of: MAU ≥1M (credible public source) / revenue thousands-per-month (credible source) / dev-tool usage-stat (npm ≥1M downloads/week OR GitHub ≥20k stars, dated official-API data) / individually-credited in-window top-tier award (Awwwards SOTY/SOTM, FWA of Month/Year, CSSDA WOTY, Communication Arts, Webby, Apple Design Award). Excluded: lifetime honors, agency wins, FWA of the Day, Behance/Dribbble popularity, IGF/BAFTA.
4. **Source tier** — Tier 1 (official APIs/platforms, regulatory/audited filings, reputable press) counts alone; Tier 2 (product's own blog) counts with corroboration; Tier 3 (self-disclosed) requires ≥1 Tier 1/2 reporting the same figure; estimate trackers (LATKA, SitePrice, SimilarWeb, ppc.land) corroborate only. Tier-3-only → REJECT `tier3-only`. Fetch official sources directly — search snippets are discovery, not evidence.

Also record **doc-currency**: one line — is the first-party workflow doc still referenced as current in recent content?

## Evidence JSON schema (exact keys)

```json
{
  "name": "...",
  "products": ["..."],
  "route": "MAU | revenue | usage-stat | award",
  "scale_evidence": {"figure": "...", "date": "...", "source_url": "...", "tier": "T1|T2|T3"},
  "window_5yr": "in-window | out-of-window",
  "doc_currency": "...",
  "verdict": "PASS | REJECT",
  "rejection_reason": "... or null",
  "dead_ends_searched": ["..."]
}
```

## Shared tooling (all researchers)

- Follow `.agents/skills/opencode-web-research/SKILL.md`: try `searxng_searxng_web_search` ONCE; on error/empty use `websearch` (Exa). `web_search` (metasearch2) is last resort only.
- Read a page before citing it. Never invent a number, date, or quote. REJECT is a valid outcome — log the dead ends.
- Write the JSON to the exact output path. Final message <=250 words: verdict + path + one-line reason.
- Efficiency: if any search/read tool hangs or returns nothing twice in a row, switch tools and move on. Budget ~40 minutes of tool work; if you cannot complete a check, record UNKNOWN in the JSON and finish writing — never stall without writing your output file.

## Researcher 1 — Sindre Sorhus

- Output file: `working/evidence/sindre-sorhus-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Sindre Sorhus — chalk / open-source tools (dev-tools lane). Discovery row: scale lead https://github.com/chalk/chalk (~10M+ weekly downloads claimed); first-party doc https://sindresorhus.com/ (newsletter/talks; design-process content flagged thin `?`). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: Sorhus publicly credited as chalk's creator; establish his designer credentials — he is "designer by training" (Westerdals Oslo School of Arts); find public evidence of his design identity (interviews, bio) — is he credibly "the designer" of his tools? Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/chalk and https://api.github.com/repos/chalk/chalk; record fetch date 2026-08-17. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/sindre-sorhus-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 2 — Zach Gage

- Output file: `working/evidence/zach-gage-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Zach Gage — Knotwords, Good Sudoku, Puzzmo (mobile/games lane). Discovery row: scale lead https://developer.apple.com/news/?id=ti9czxni (Knotwords ADA 2023 FINALIST); first-party doc http://www.stfj.net/The30YearGame/ (talks/writing). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Route: award — Knotwords was an Apple Design Award FINALIST (finalist ≠ winner, does not count); search for an in-window WIN individually credited to Gage: ADA winner lists (2021-2026), Webby wins for Good Sudoku/Knotwords/Puzzmo (2021-2026), FWA/Awwwards n/a. If none → REJECT (reason: no qualifying in-window award). Backup: MAU/revenue for Puzzmo or Good Sudoku from Tier 1/2 sources only. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/zach-gage-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 3 — Michael Flarup

- Output file: `working/evidence/michael-flarup-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Michael Flarup — Thermo / Weather Up / Thermodo (mobile lane). Discovery row: scale lead https://medium.com/@MakerHunt/today-we-have-michael-flurap-who-is-an-awesome-designer-and-helped-design-be-my-eyes-e2596addb8f2 (Thermo 5M+ users self-disclosed); first-party doc https://medium.com/@flarup/what-everyone-should-know-about-the-process-of-designing-apps-7fbc81f6e1d8. Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Route: MAU — "Thermo 5M+ users" is self-disclosed (Tier 3); find independent Tier 1/2 corroboration (press, app store statements) of Thermo's user base >=1M in-window, OR a qualifying in-window award individually credited to Flarup (ADA/Webby 2021-2026). If only Tier 3 → REJECT tier3-only. Record doc-currency (are his process articles still referenced as current?). Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/michael-flarup-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 4 — Philipp Stollenmayer

- Output file: `working/evidence/philipp-stollenmayer-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Philipp Stollenmayer (Kamibox) — Song of Bloom, o k a y? (mobile/games lane). Discovery row: scale lead https://en.wikipedia.org/wiki/Apple_Design_Awards (Song of Bloom ADA 2020, individually credited); first-party doc https://kamibox.de/songofbloom-files (design docs). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Song of Bloom's ADA is 2020-06 — BEFORE the window start (2021-08-17) → out-of-window. Search for an in-window qualifying win: Webby wins (Song of Bloom won a Webby in 2021? — verify date: 25th Webbys announced May 2021 — if May 2021, it is still out-of-window), ADA 2021-2026 for any Kamibox title, Communication Arts. If none → REJECT out-of-window. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/philipp-stollenmayer-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Completion criteria

- 4 evidence JSONs exist with exact schema keys
- Each PASS has a dated figure + source URL + tier inside the JSON
- Each REJECT has a reason + dead-ends searched
- `working/waves/report-06.md` written

## QA checklist (lead)

- [ ] All 4 JSONs exist, parse as JSON, all schema keys present
- [ ] Every PASS backed by dated figure + tier (no figure → flag for re-run)
- [ ] Every REJECT carries reason + dead ends
- [ ] Verdicts in report match JSONs on disk
- [ ] `report-06.md` has per-researcher status + PASS/REJECT counts + anomalies
