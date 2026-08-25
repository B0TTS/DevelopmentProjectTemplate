# Wave 02 — Phase 1: Verification (wave 1 of N)

- Phase: 1 (Verification)
- Goal: verdict (PASS/REJECT) for 4 candidates — first wave toward >=12 PASS
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

## Researcher 1 — Adam Wathan

- Output file: `working/evidence/adam-wathan-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Adam Wathan — Tailwind CSS / Tailwind UI / Headless UI (dev-tools lane). Discovery row: scale lead https://github.com/tailwindlabs/tailwindcss; first-party docs https://adamwathan.me/ and https://tailwindcss.com/blog (design posts e.g. "Designing Tailwind UI Ecommerce"). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Likely route: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/tailwindcss and https://api.github.com/repos/tailwindlabs/tailwindcss, record fetch date 2026-08-17. Attribution: is Wathan publicly credited as creator/designer of these tools (not team credit)? Also record doc-currency for his workflow content. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/adam-wathan-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 2 — shadcn

- Output file: `working/evidence/shadcn-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate shadcn — shadcn/ui + shadcn CLI (dev-tools lane). Discovery row: scale lead https://github.com/shadcn-ui/ui (~114k stars claimed); first-party doc https://ui.shadcn.com/docs (design principles: Beautiful Defaults, Open Code, Composition). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Likely route: usage-stat — fetch live https://api.github.com/repos/shadcn-ui/ui and, if relevant, npm data; record fetch date 2026-08-17. Attribution: shadcn publicly credited as the creator/designer of shadcn/ui (he's a designer at Vercel — confirm individual credit). Also record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/shadcn-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 3 — Mark Otto

- Output file: `working/evidence/mark-otto-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Mark Otto — Bootstrap + Bootstrap Icons (dev-tools lane). Discovery row: scale lead https://github.com/twbs/bootstrap (~160k stars claimed); first-party doc https://markdotto.com/ (design deep-dives). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Likely route: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/bootstrap and https://api.github.com/repos/twbs/bootstrap; record fetch date 2026-08-17. Attribution: is Otto individually credited as creator/designer of Bootstrap (not just team credit)? Also record doc-currency (is his process blog still referenced as current?). Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/mark-otto-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 4 — Curtis Herbert

- Output file: `working/evidence/curtis-herbert-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Curtis Herbert — Slopes (mobile lane, Breakpoint Studio, solo creator). Discovery row: scale lead https://www.revenuecat.com/blog/growth/slopes-from-indie-side-hustle-to-1m-in-arr-and-an-apple-design-award; first-party doc https://blog.curtisherbert.com/slopes-diaries-9-for-the-good-of-the-business/. Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Routes to try: (a) award — Slopes Apple Design Award 2022 (Interaction) — confirm via Apple newsroom or Wikipedia Apple Design Awards list, check it's individually credited to Herbert, in-window; (b) revenue — $1M ARR claim: find Tier 1/2 corroboration (press or Slopes' own blog), NOT RevenueCat blog alone. Record doc-currency for Slopes Diaries. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/curtis-herbert-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Completion criteria

- 4 evidence JSONs exist with exact schema keys
- Each PASS has a dated figure + source URL + tier inside the JSON
- Each REJECT has a reason + dead-ends searched
- `working/waves/report-02.md` written

## QA checklist (lead)

- [ ] All 4 JSONs exist, parse as JSON, all schema keys present
- [ ] Every PASS backed by dated figure + tier (no figure → flag for re-run)
- [ ] Every REJECT carries reason + dead ends
- [ ] Verdicts in report match JSONs on disk
- [ ] `report-02.md` has per-researcher status + PASS/REJECT counts + anomalies
