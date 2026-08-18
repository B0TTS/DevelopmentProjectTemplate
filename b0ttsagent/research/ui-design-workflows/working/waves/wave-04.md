# Wave 04 — Phase 1: Verification (wave 3 of N)

- Phase: 1 (Verification)
- Goal: verdict (PASS/REJECT) for 4 candidates — running pool: 7 PASS, target >=12
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
- Efficiency: if any search/read tool hangs or returns nothing twice in a row, switch tools and move on. Budget ~40 minutes of tool work; if you cannot complete a check, record UNKNOWN in the JSON and finish writing — never stall without writing your output file.

## Researcher 1 — Lea Verou

- Output file: `working/evidence/lea-verou-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Lea Verou — Prism.js / Color.js / Mavo (dev-tools lane). Discovery row: scale lead https://github.com/PrismJS/prism (~8M weekly downloads claimed); first-party doc https://lea.verou.me/ (blog + design/API process content). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution judgment: Verou is publicly credited as Prism's creator; establish her designer credentials (graphic design background, web standards design work, CSS Secrets author) — is she credibly "the designer" of the shipped tool? Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/prismjs and https://api.github.com/repos/PrismJS/prism; record fetch date 2026-08-17. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/lea-verou-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 2 — Max Stoiber

- Output file: `working/evidence/max-stoiber-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Max Stoiber — styled-components / Spectrum (dev-tools lane). Discovery row: scale lead https://github.com/styled-components/styled-components (~40k stars, ~1.5M npm/wk claimed); first-party doc https://mxstbr.com/thoughts/css-in-js (design rationale content). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: Stoiber publicly credited as creator of styled-components; establish his designer credentials (designer/engineer at Thinkmill, Moxy Studio design work) — individual design credit, not team. Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/styled-components and https://api.github.com/repos/styled-components/styled-components; record fetch date 2026-08-17. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/max-stoiber-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 3 — Tobias Ahlin Bjerrome

- Output file: `working/evidence/tobias-ahlin-bjerrome-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Tobias Ahlin Bjerrome — Spotify (consumer), GitHub Copilot. Discovery row: scale lead https://open.spotify.com/ (Spotify MAU); first-party doc https://tobiasahlin.com/blog/ (process posts on Spotify/Minecraft/GitHub design work). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: find public evidence crediting Bjerrome INDIVIDUALLY for a shipped product's design (Spotify UI work or GitHub Copilot design — press/interviews/credits naming him, not just team). Scale: try (a) MAU — Spotify MAU >=1M from Tier 1 source (Spotify investor releases / reputable press, in-window); or (b) GitHub Copilot MAU >=1M (reputable press reported 30M+ in 2025). The scale must attach to a product he is individually credited on — if attribution fails, REJECT team-credit regardless of scale. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/tobias-ahlin-bjerrome-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 4 — Charli Marie Prangley

- Output file: `working/evidence/charli-marie-prangley-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Charli Marie Prangley — Kit (ConvertKit, B2B SaaS). Discovery row: scale lead https://convertkit.com/; first-party doc https://charlimarie.com/blog (process content; also YouTube CharliMarieTV + Inside Marketing Design podcast). Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: publicly credited individually for Kit's design/marketing site work (her title, press, interviews). Scale: revenue route — Kit ARR/revenue figure from Tier 1 press or Tier 2 (Kit's own blog) with corroboration; Kit's founder discloses revenue publicly but that is Tier 3 self-disclosure — it needs an independent Tier 1/2 source reporting the same figure to count. If only Tier 3 → REJECT tier3-only (log dead ends; no estimate trackers as anchor). Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/charli-marie-prangley-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Completion criteria

- 4 evidence JSONs exist with exact schema keys
- Each PASS has a dated figure + source URL + tier inside the JSON
- Each REJECT has a reason + dead-ends searched
- `working/waves/report-04.md` written

## QA checklist (lead)

- [ ] All 4 JSONs exist, parse as JSON, all schema keys present
- [ ] Every PASS backed by dated figure + tier (no figure → flag for re-run)
- [ ] Every REJECT carries reason + dead ends
- [ ] Verdicts in report match JSONs on disk
- [ ] `report-04.md` has per-researcher status + PASS/REJECT counts + anomalies
