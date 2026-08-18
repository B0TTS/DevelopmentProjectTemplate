# Wave 03 — Phase 1: Verification (wave 2 of N)

- Phase: 1 (Verification)
- Goal: verdict (PASS/REJECT) for 4 candidates — running pool: 4 PASS, target >=12
- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, one candidate each, parallel fanout
- Input: `working/candidates.md` (their rows) — each researcher reads only their candidate's row

## Verification standard (send with every researcher — the 4 checks, in order, stop at first failure)

1. **Individual attribution** — name publicly tied to a shipped product (portfolio / LinkedIn / credits / press "designed by"). Team or design-system credit alone → REJECT `team-credit`.
2. **In-window** — the scale/award evidence is dated within 2021-08-17 → 2026-08-17. For usage-stat: fetch LIVE numbers today and record the fetch date (live data is in-window by definition). Out-of-window with nothing recent → REJECT `out-of-window`.
3. **Scale evidence** — exactly one of: MAU ≥1M (credible public source) / revenue thousands-per-month (credible source) / dev-tool usage-stat (npm ≥1M downloads/week OR GitHub ≥20k stars, dated official-API data) / individually-credited in-window top-tier award (Awwwards SOTY/SOTM, FWA of Month/Year, CSSDA WOTY, Communication Arts, Webby, Apple Design Award). Excluded: lifetime honors, agency wins, FWA of the Day, Behance/Dribbble popularity, IGF/BAFTA.
4. **Source tier** — Tier 1 (official APIs/platforms, regulatory/audited filings, reputable press) counts alone; Tier 2 (product's own blog) counts with corroboration; Tier 3 (self-disclosed) requires ≥1 Tier 1/2 reporting the same figure; estimate trackers (LATKA, SitePrice, SimilarWeb, ppc.land) corroborate only. Tier-3-only → REJECT `tier3-only`. Fetch official sources directly (npm API, GitHub API, award pages, Wikipedia) — search snippets are discovery, not evidence.

Also record **doc-currency**: one line — is the first-party workflow doc still referenced as current in recent content?

## Evidence JSON schema (exact keys — output path per researcher)

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

## Researcher 1 — Karri Saarinen

- Output file: `working/evidence/karri-saarinen-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Karri Saarinen — Linear (B2B SaaS issue tracker; co-founder). Discovery row: scale lead https://linear.app/; first-party docs https://karrisaarinen.com/ and Linear's blog ("How we redesigned the Linear UI"). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: co-founder publicly credited as Linear's designer (press interviews, "designed by"). Scale: look for public in-window Linear revenue/ARR figures in reputable press (TechCrunch, The Verge) or an official Linear source, OR MAU >=1M from a credible public source. If no Tier 1/2 scale figure is publicly findable → REJECT tier3-only (log dead ends; do not use estimate trackers as anchor). Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/karri-saarinen-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 2 — Ryan McLeod

- Output file: `working/evidence/ryan-mcleod-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Ryan McLeod — Blackbox (iOS puzzle, solo creator, Shapes+Stories). Discovery row: scale lead https://en.wikipedia.org/wiki/Apple_Design_Awards; first-party doc https://medium.com/@warpling (design-process posts). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Route: award — Blackbox won Apple Design Award 2017 (out of window) AND reportedly again for visionOS (2024?) — verify the in-window win via Apple newsroom and the Wikipedia Apple Design Awards list; confirm individual credit (solo creator) and exact award date in-window. Backup routes: MAU/revenue — "14M+ players" is self-disclosed; only count with Tier 1/2 corroboration. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/ryan-mcleod-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 3 — Mike Bostock

- Output file: `working/evidence/mike-bostock-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Mike Bostock — D3.js, Observable (dev-tools lane). Discovery row: scale lead https://github.com/d3/d3; first-party doc https://bost.ocks.org/mike/ (design process essays). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution judgment: Bostock is publicly credited as D3's creator; establish his design-credit credentials (NYT Graphics editor, visualization designer by trade) — is he credibly "the designer" of the shipped tool, not merely its engineer? Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/d3 and https://api.github.com/repos/d3/d3; record fetch date 2026-08-17. Record doc-currency (are his essays still referenced as current?). Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/mike-bostock-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 4 — Steve Schoger

- Output file: `working/evidence/steve-schoger-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Steve Schoger — Heroicons / Tailwind UI / Refactoring UI (dev-tools lane; visual designer, Tailwind Labs partner). Discovery row: scale lead https://github.com/tailwindlabs/heroicons (~23.7k stars claimed); first-party doc https://www.steveschoger.com/ (plus X design-tip threads). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: publicly credited as the designer of Heroicons/Tailwind UI/Refactoring UI (individual credit, not team). Scale: usage-stat — fetch live https://api.github.com/repos/tailwindlabs/heroicons (>=20k stars?) and/or npm weekly downloads for @heroicons/react (https://api.npmjs.org/downloads/point/last-week/@heroicons/react); record fetch date 2026-08-17. If neither meets threshold, check for a public revenue figure for Tailwind UI/Refactoring UI with Tier 1/2 sourcing — otherwise REJECT with reason. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/steve-schoger-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Completion criteria

- 4 evidence JSONs exist with exact schema keys
- Each PASS has a dated figure + source URL + tier inside the JSON
- Each REJECT has a reason + dead-ends searched
- `working/waves/report-03.md` written

## QA checklist (lead)

- [ ] All 4 JSONs exist, parse as JSON, all schema keys present
- [ ] Every PASS backed by dated figure + tier (no figure → flag for re-run)
- [ ] Every REJECT carries reason + dead ends
- [ ] Verdicts in report match JSONs on disk
- [ ] `report-03.md` has per-researcher status + PASS/REJECT counts + anomalies
