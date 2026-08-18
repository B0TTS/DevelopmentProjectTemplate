# Wave 01 — Phase 0: Candidate Discovery

- Phase: 0 (Candidate discovery)
- Goal: ≥20 unique, schema-complete candidates in `working/candidates.md`
- Roster: 3 discovery researchers in parallel fanout — lanes A/B/C
- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17 (context only; no verification this wave)

## Shared tooling (all researchers)

- Follow routing from `.agents/skills/opencode-web-research/SKILL.md`: try `searxng_searxng_web_search` ONCE; on error/empty use `websearch` (Exa). `web_search` (metasearch2) is last resort only.
- Search snippets are discovery, not evidence — skim each first-party doc URL you list to confirm it contains actual process content.
- Write full work product to disk only. Final message ≤250 words (row count, file path, 3 strongest names).

## Row schema (fixed — every row, exact format)

`- **Name** — products: … — route: … — scale lead: <url> — first-party doc: <url> — notes: …`

## Researcher A — consumer / B2B SaaS / marketing sites

- Output file: `working/candidates-lane-A.md`
- Task prompt (send verbatim):
  > Lane A — consumer/B2B SaaS/marketing sites. Find ≥7 named designers individually credited on shipped products AND with first-party process content (own blog, YouTube, course, book, X threads). Use the row schema from the wave spec. Route guesses: MAU, revenue, or individually-credited craft awards (Awwwards/FWA Site of the Month/Year, CSSDA, Communication Arts, Webby, Apple Design Award). Prefer candidates whose scale evidence looks findable. Do NOT verify — flag uncertainty honestly (role unconfirmed, doc looks like a listicle). Write rows to `working/candidates-lane-A.md`. Final message ≤250 words: row count, path, 3 strongest names.

## Researcher B — dev tools / open source

- Output file: `working/candidates-lane-B.md`
- Task prompt (send verbatim):
  > Lane B — dev tools/open source. Find ≥7 named designers/creators of shipped developer tools (CLIs, TUIs, SDKs, dev apps) with individual design credit and first-party process content. Scale route will be the usage-stat proxy (npm ≥1M weekly downloads OR GitHub ≥20k stars) — record the tool's npm package name or GitHub repo as the scale lead. Skip team design systems (Material, Polaris, Carbon) — individual credit only. Do NOT verify. Write rows to `working/candidates-lane-B.md`. Final message ≤250 words: row count, path, 3 strongest names.

## Researcher C — mobile / games / niche genres

- Output file: `working/candidates-lane-C.md`
- Task prompt (send verbatim):
  > Lane C — mobile/games/niche genres. Find ≥7 named designers individually credited on shipped mobile apps, games, or niche products with first-party process content. Apple Design Award individually-credited designers are a strong lead; also indie apps with a documented design process. Scale routes: MAU, revenue, or award. Do NOT verify — flag uncertainty. Write rows to `working/candidates-lane-C.md`. Final message ≤250 words: row count, path, 3 strongest names.

## Completion criteria

- 3 lane files exist, each ≥7 schema-complete rows
- `working/candidates.md` merged + deduped, ≥20 unique rows, weak rows flagged with `?`
- `working/waves/report-01.md` written

## QA checklist (lead)

- [ ] All 3 lane files exist with ≥7 rows each (count lines starting `- **`)
- [ ] Every row has: name + ≥1 scale lead URL + ≥1 first-party doc URL
- [ ] Dedup by name done (same-name designers disambiguated by product)
- [ ] Lane balance: no lane <4 rows in final merged file
- [ ] Weak rows flagged `?` in notes
- [ ] `report-01.md` has per-researcher status + merged count + anomalies
