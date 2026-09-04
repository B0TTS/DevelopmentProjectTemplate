# Wave 1 — Industries that Survived and/or Profited in the Great Depression

**Wave goal:** produce one evidence-backed research file per scope identifying which industries and named companies survived and/or profited during the Great Depression (1929–1939, US-focused), with every material claim linked to a source. Exit: each file is DEPTH-PASS or THIN-with-explicit-gap.

**Definitions (apply to all workers):**
- **Survived** = industry did not collapse en masse and/or leading firms held share, paid dividends, or stayed solvent through 1929–1939.
- **Profited** = grew revenue/profit, gained market share, or rewarded shareholders (dividends/stock appreciation) during 1929–1939.
- Both categories count; label each example as survived or profited (or both).

**Roster (one worker per scope, parallel):**

1. **R1 — Consumer staples & household necessities.** Food manufacturing (Kellogg, General Foods), tobacco (American Tobacco, R.J. Reynolds), soap/household goods (Procter & Gamble, Colgate). Why demand held up; advertising/marketing strategy during the Depression.
2. **R2 — Entertainment & escapism.** Hollywood studios (MGM, Warner Bros., Paramount), radio networks (NBC, CBS), cheap amusements, cosmetics ("lipstick effect" — Coty, Max Factor), candy (Hershey, Mars). Evidence for counter-cyclical demand.
3. **R3 — Budget retail, catalogs & the repair/secondhand economy.** Woolworth five-and-dime, A&P grocery chain, Sears/Montgomery Ward catalogs, repair shops, secondhand goods. Why value-focused distribution thrived.
4. **R4 — Utilities, energy, gold & defense.** Electric utilities, oil companies, gold-mining boom (Homestake Mining), DuPont and early defense work, alcohol post-1933 repeal (distillers/brewers).
5. **R5 — Cash-rich survivors & distressed-asset strategies.** How cash-rich firms gained share or bought distressed assets/competitors cheaply (DuPont/General Motors, GM vs. Ford, bank consolidation), plus notable Depression-era investors; brief note on international exceptions (e.g., USSR, Japan) if sources allow.

**WORKER TYPE:** `b0tts-researcher` (web research; no shell needed).

**Per-worker task prompt (verbatim for every worker, fill in SCOPE + FILE):**

> You are a deep single-scope web researcher working a Great Depression research wave. Your scope: **SCOPE**. Search the web, read primary and credible secondary sources, verify claims against them. Write complete findings to `b0ttsagent/research/great-depression-industries/FILE`.
> Required sections in the file: (1) Scope summary; (2) Industries/companies with evidence — a table where possible (industry / company / what happened 1929–1939 / survived-or-profited / source link); (3) Why it survived/profited — the mechanisms; (4) Counterintuitive or disputed findings; (5) Sources — numbered URLs with access date; (6) Confidence & gaps.
> Quality bar: every material claim carries an inline source link; at least 6 distinct source URLs; explicitly separate verified (corroborated by primary/secondary sources) from claimed or disputed; no unsourced assertions. If sources are thin, say so explicitly and stop — never pad, never fabricate.
> Final message ≤250 words: verdict DEPTH-PASS or THIN + file path + one-line reason. Never paste doc content into your final message.

**Completion criteria:** 5 files exist (`R1-consumer-staples.md` … `R5-cash-rich-survivors.md`), each DEPTH-PASS or THIN-with-explicit-gap.

**Lead QA checklist:**
- [ ] all 5 expected files exist
- [ ] each has the 6 required sections
- [ ] each has ≥6 distinct source URLs; spot-grep for claims lacking links
- [ ] THIN verdicts carry explicit gap statements, not padded prose
- [ ] file count in report matches files on disk
- [ ] FAIL-UNKNOWN workers retried once before recording FAIL-UNKNOWN

**Lead output:** `b0ttsagent/research/great-depression-industries/WAVE-REPORT.md` — per-worker status (done / fail / retried), verdicts, anomalies, a reconciled cross-cutting section (top industries/companies that survived or profited, one-line evidence each, grouped survived vs profited), next actions. Lead final message ≤500 words: status, file paths, verdicts, next actions. Never paste file contents.

**Context budget:** workers → disk only, ≤250-word finals. Lead reads only this spec + worker summaries. Never read full worker files into context.
