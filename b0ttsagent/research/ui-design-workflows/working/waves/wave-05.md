# Wave 05 — Phase 1: Verification (wave 4 of N)

- Phase: 1 (Verification)
- Goal: 1 targeted re-check (Ahlin MAU) + 3 fresh candidates — running pool: 11 PASS (1 flagged), target >=12
- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Roster: 4 researchers, parallel fanout (R1 = re-check, R2–R4 = fresh)
- Input: `working/candidates.md` + existing evidence JSON (R1 only)

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

## Researcher 1 — RE-CHECK: Tobias Ahlin Bjerrome (MAU confirmation)

- Output file: `working/evidence/tobias-ahlin-bjerrome-2026-08-17.json` (EDIT the existing file — do not rewrite from scratch; keep its dead_ends and add to them)
- Task prompt (send verbatim):
  > RE-CHECK candidate Tobias Ahlin Bjerrome — GitHub Copilot. The existing evidence JSON at `b0ttsagent/research/ui-design-workflows/working/evidence/tobias-ahlin-bjerrome-2026-08-17.json` cites Copilot figures of "50M users (cumulative)" — but the verification route requires MAU (monthly active users), not cumulative users. Your job: (1) find a public in-window statement of GitHub Copilot MAU — check Microsoft FY2026 Q1 earnings (Oct 2025, Nadella reportedly said "20 million monthly active users") via Microsoft investor page, transcripts, or reputable press (TechCrunch/The Verge); (2) confirm individual design credit: public evidence naming Ahlin Bjerrome specifically for Copilot's UI design (his own blog posts about designing Copilot, GitHub blog bylines, press). Then EDIT the existing JSON: update scale_evidence to the MAU figure with source URL + tier + date; if no credible MAU figure exists, set verdict to REJECT with reason "scale-not-met: cumulative users only, no public MAU" and keep everything else. If MAU found but individual credit fails, REJECT team-credit. Append new dead ends. Final message <=250 words: new verdict + what changed.

## Researcher 2 — Jared Palmer

- Output file: `working/evidence/jared-palmer-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Jared Palmer — Formik / Turborepo (dev-tools lane). Discovery row: scale lead https://github.com/jaredpalmer/formik (~34k stars, ~1M+ npm/wk claimed); first-party doc https://jaredpalmer.com/blog/formik-taming-forms-in-react. Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution: Palmer publicly credited as Formik's creator; establish his designer credentials (freelance designer background, design work pre-Formik) — individual credit, not team. Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/formik and https://api.github.com/repos/jaredpalmer/formik; record fetch date 2026-08-17. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/jared-palmer-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 3 — Mike Kus

- Output file: `working/evidence/mike-kus-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Mike Kus — marketing/brand sites for startups and global brands (agency lane; freelance/designer). Discovery row: scale lead https://www.awwwards.com/sites/mike-kus-1 (self-listed: Awwwards Site of the Day x6, Site of the Month x1, Designer of the Year finalist x2); first-party doc https://mikekus.com/. Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Route: award — find an Awwwards **Site of the Month** (or higher: Site of the Year, FWA of the Month/Year, CSSDA WOTY) that is (a) dated in-window (2021-08-17 → 2026-08-17), (b) on the official Awwwards/FWA site, (c) individually credited to Mike Kus (not an agency). Site of the Day does NOT count. His self-listed profile is not evidence — verify on the award platform itself. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/mike-kus-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Researcher 4 — Matt Perry

- Output file: `working/evidence/matt-perry-2026-08-17.json`
- Task prompt (send verbatim):
  > Verify candidate Matt Perry — Motion (Framer Motion) / Popmotion / CSS Studio (dev-tools lane). Discovery row: scale lead https://github.com/motiondivision/motion (~33k stars, ~4.5M npm/wk claimed); first-party doc https://motion.dev/magazine. Run the 4 checks IN ORDER, stop at first failure, per the verification standard in the wave spec. Attribution judgment: discovery flagged him "engineer, not visual designer" — investigate: is Perry publicly credited as a designer on shipped design tools (ex-Framer design work, CSS Studio, Motion's visual design)? If the credit is purely engineering, REJECT on attribution even if scale is huge. Scale: usage-stat — fetch live https://api.npmjs.org/downloads/point/last-week/framer-motion and https://api.github.com/repos/motiondivision/motion; record fetch date 2026-08-17. Record doc-currency. Write evidence JSON per schema to `b0ttsagent/research/ui-design-workflows/working/evidence/matt-perry-2026-08-17.json`. Final message <=250 words: verdict + path + one-line reason.

## Completion criteria

- 4 evidence JSONs exist with exact schema keys (R1 = updated existing)
- Each PASS has a dated figure + source URL + tier inside the JSON
- Each REJECT has a reason + dead-ends searched
- `working/waves/report-05.md` written

## QA checklist (lead)

- [ ] All 4 JSONs exist, parse as JSON, all schema keys present
- [ ] Every PASS backed by dated figure + tier (no figure → flag for re-run)
- [ ] Every REJECT carries reason + dead ends
- [ ] R1's update: MAU figure corrected OR verdict flipped to REJECT with reason — one of the two
- [ ] Verdicts in report match JSONs on disk
- [ ] `report-05.md` has per-researcher status + PASS/REJECT counts + anomalies
