# Report contract — daily-trends-report skill (reference)

The shape of the daily deliverable the user reads: file layout, the `report.md` skeleton, item field rules, glance/word-budget/Still-circulating rules, `index.md`, and the chat pointer. Routing decisions are not here — see `routing-rules.md`. Wave mechanics are in `wave-spec.md`.

> **Authority.** Scripts first, then this doc. The `verify` subcommand machine-checks most rules below; where a rule is writer discipline rather than a hard check, this doc says so.

## TOC

- [Purpose](#purpose)
- [File layout](#file-layout)
- [The report.md skeleton](#the-reportmd-skeleton)
- [Main-section item fields](#main-section-item-fields)
- [The glance block](#the-glance-block)
- [Word budget](#word-budget)
- [Still circulating section](#still-circulating-section)
- [index.md](#indexmd)
- [Chat pointer](#chat-pointer)
- [Examples](#examples)
- [What verify checks on report.md](#what-verify-checks-on-reportmd)

## Purpose

Who reads this: the writer drafting `report.md`, and the orchestrator assembling the day folder and posting the chat pointer. It answers one question per section: what must the file contain, and what does a good versus broken item look like. The report is a quick-scan digest sized for a 15-minute read — every rule below serves that budget.

## File layout

A1 layout — one day folder per run inside a month folder; a single `index.md` at the reports root:

```text
b0ttsagent/reports/daily-reports/AI-Development Trends/
  index.md                 <- one row per report, newest on top
  2026-08/
    2026-08-18/
      report.md            <- the digest (only the writer writes it)
      anchors.md           <- HN front page + GitHub Trending snapshot (orchestrator)
      inventory.json       <- last-2-files parse (build-inventory.py)
      ai.json              <- AI leaf output
      swe.json             <- SWE leaf output
      productivity.json    <- Productivity leaf output
      routed.json          <- frozen routing decisions (route-and-verify.py route)
      wave-1.md            <- this run's wave spec (orchestrator)
```

The scripts write exactly `inventory.json` and `routed.json`; nothing else writes them. The three leaf files and `wave-1.md` are wave mechanics — see `wave-spec.md`.

## The report.md skeleton

Exactly this structure, nothing else — no outro, no methodology, no "sources consulted":

```markdown
# Daily AI & SWE trends — 2026-08-18

*Today at a glance*

- <the day's AI headline, one line>
- <the day's SWE headline, one line>
- <the day's Productivity headline, one line>

## AI trends

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| <domain> | <headline> | <1-2 sentences> | <YYYY-MM-DD> | [<source>](<url>) |

## SWE trends

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|

## Productivity

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|

## Still circulating        <- omit this whole section when empty

| Headline | Date | Link |
|---|---|---|---|
| <headline> | <YYYY-MM-DD> | [<source>](<url>) |
```

Rules around the skeleton:

- **Title:** writer-chosen wording, but it must carry the run date. Verify does not inspect the title.
- **Headings** are exactly and only `## AI trends`, `## SWE trends`, `## Productivity`, `## Still circulating`. Stable, no witty titles, no emoji.
- **Section order** is fixed: AI, SWE, Productivity, then Still circulating.
- **Nothing else anywhere** — verify counts bullet lines in the whole file and warns when the count is not exactly 3, so the glance must be the only list in the report.

## Main-section item fields

One item = one table row. Columns exactly: `Domain · Headline · Why it matters · Date · Link`.

| Field | Rule | Enforced by |
|---|---|---|
| Headline | Required, non-empty. The story in one line; no dates in headlines — dates live in the Date column. | verify (parser error on empty) |
| Why it matters | Required; ≤2 sentences / ~40 words. | Non-empty: verify error. Length: writer discipline. |
| Link | Required; source URL as a markdown link (`[text](url)`) or bare URL. Primary source, not an aggregator page. | verify (parser error on missing) |
| Date | Required; published (or updated) date as YYYY-MM-DD, inside the 7-day window inclusive. No guessed dates. | route drops undated; verify errors on missing/out-of-window |
| Domain | From routed.json; one of the section's domain hints. | Writer; verify does not check non-empty |

Counts: target 3–5 per section; 1–2 is a valid thin day; 5 is a hard cap (verify errors above 5); there is no minimum. Never pad — a thin day beats a padded day.

Order: the writer orders by "worth a click", not recency.

Cross-section: one story, one section. If an item fits both AI and SWE, pick one; verify errors on duplicate identities across main sections.

Updates: an item flagged `update: true` in routed.json is framed as an update citing the delta carried in routed.json — no re-research, no new sources.

## The glance block

Label `*Today at a glance*` (italic), then exactly 3 bullets — one per section, in section order — each the day's single most click-worthy item from that section. Every section gets a bullet even on a thin day. Verify warns when the label is missing or the file's bullet count is not exactly 3, which is why the glance must be the file's only list. A reader names the day's 3 headlines from this block in under a minute.

## Word budget

The whole `report.md` runs ~400–700 words, excluding the Still circulating section. Verify's count is the non-space-token count of everything before the `## Still circulating` heading — title, glance, and table text included (when the section is absent, the whole file counts). Soft warning only: a run outside the budget still passes verify — fix it, but never by padding.

## Still circulating section

- **Who appears:** identities the route script sent there — streak-hit, ≤7 days, re-proposed this run, update test failed. Nothing else, ever.
- **Rows:** one line — headline · date · link. No why-it-matters column, no commentary.
- **Order:** newest published date first — copy the order straight from routed.json.
- **Cap:** 10 rows.
- **Empty:** omit the section and its heading entirely (verify warns on an empty section with the heading present).

## index.md

Lives at the reports root (`AI-Development Trends/index.md`). The orchestrator maintains it — it is not scripted.

- Create it if missing.
- Columns: `Date · File · Item count · One-line glance`.
- Newest row on top.
- Same-day rerun updates the existing row for that date — never appends a duplicate.

```markdown
| Date | File | Item count | One-line glance |
|---|---|---|---|
| 2026-08-18 | [2026-08/2026-08-18/report.md](2026-08/2026-08-18/report.md) | 9 | <the glance, condensed to one line> |
| 2026-08-17 | [2026-08/2026-08-17/report.md](2026-08/2026-08-17/report.md) | 11 | <the glance, condensed to one line> |
```

## Chat pointer

After the run completes, post exactly this and nothing else — no second report, no extra analysis:

```text
b0ttsagent/reports/daily-reports/AI-Development Trends/2026-08/2026-08-18/report.md
- <glance bullet 1>
- <glance bullet 2>
- <glance bullet 3>
N items demoted        <- only when Still circulating is non-empty; N = its row count
```

## Examples

Dates below are illustrative; a real item's Date must sit inside the 7-day window of its run. Each rejected example states the contract violation it breaks.

**Good — AI trends.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| AI company news | Anthropic ships Claude Opus 4.5 with a 1M-token context window | Doubles the previous flagship's context ceiling, making whole-codebase analysis practical in a single prompt. | 2026-08-18 | [Announcement](https://www.anthropic.com/news/claude-opus-4-5) |

Why it is good: one story, one concrete why in 2 sentences (~20 words), a dated primary source as a markdown link, and a domain from the AI section's hint list.

**Rejected — AI trends.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| AI company news | Anthropic ships Claude Opus 4.5 | The new model doubles the context ceiling, so whole-codebase prompts become practical. Beyond that, this move reshapes the competitive landscape. Context has become the main axis frontier labs compete on. Developers will feel it downstream in pricing and tooling over the coming quarters. | 2026-08-18 | [Announcement](https://www.anthropic.com/news/claude-opus-4-5) |

Rejected because: the why-it-matters runs ~45 words across 4 sentences. The contract allows ≤2 sentences / ~40 words. Verify only checks non-empty, so length is writer discipline — but the 15-minute read budget is the point of the rule.

**Good — SWE trends.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| Security & CVEs | CVE-2026-8821: authenticated RCE in a widely deployed router firmware | Fixed firmware is shipping, but millions of devices update slowly; the exposure window is the story. | 2026-08-17 | [Vendor advisory](https://vendor.example/security/2026-8821) |

Why it is good: a concrete CVE id, a 2-sentence why naming the actual risk, a dated vendor advisory as the source, and one story in one section.

**Rejected — SWE trends.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| Security & CVEs | New vuln class hits default CI setups | Affects default installs of a tool used by most pipelines. |  | [Advisory](https://vendor.example/advisories/2026-08) |

Rejected because: no published date. The route script drops undated candidates with reason "no verifiable YYYY-MM-DD published date", so this row never reaches report.md; smuggled in, it would fail verify. No guessed dates — the Date cell must hold a real YYYY-MM-DD.

**Good — Productivity.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| AI-assisted dev workflows | JetBrains ships an AI code-review agent inside its IDEs | Puts automated review into the toolchain millions of developers already use daily, with a documented early-access dataset. | 2026-08-18 | [Blog post](https://blog.jetbrains.com/idea/2026/08/ai-code-review/) |

Why it is good: a shipped tool with a dated primary source — the Productivity constraint bans roundups and evergreen advice — and a why that says what changed rather than re-describing the feature.

**Rejected — Productivity.**

| Domain | Headline | Why it matters | Date | Link |
|---|---|---|---|---|
| AI-assisted dev workflows | New terminal agent ships |  | 2026-08-18 | [Release notes](https://terminal-agent.example/releases/1.0) |

Rejected because: empty why-it-matters. Verify errors on it ("is missing why-it-matters"). The why is the point of the digest — what changed and why it matters, not merely that a thing exists.

**Good — Still circulating.**

| Headline | Date | Link |
|---|---|---|
| Model X hits milestone | 2026-08-14 | [example.com/model-x](https://example.com/model-x) |

Why it is good: one line — headline · date · link, no why column; newest published first (it sits above any older row); it appears only because the route script sent it here (streak-hit, ≤7 days, re-proposed, update test failed).

**Rejected — Still circulating.**

| Headline | Date | Why it matters | Link |
|---|---|---|---|
| Model X hits milestone | 2026-08-14 | Still widely discussed; worth keeping an eye on. | [example.com/model-x](https://example.com/model-x) |

Rejected because: Still circulating rows carry no why-it-matters. These are residue, not fresh signal — commentary would quietly turn the section into a second digest and break the quick-scan budget. Verify does not reject the extra column, so this one is writer discipline.

## What verify checks on report.md

Hard errors (exit 1): the three main headings present; every row complete (Headline, YYYY-MM-DD date, URL); why-it-matters non-empty; dates inside the 7-day window; ≤5 items per main section; one story one section; every item from routed.json (no rescued rejects); streak collisions allowed only for update-passed items; Still circulating rows only routed-SC, ≤10, in window.

Soft warnings (exit 0): glance label + exactly 3 bullets, word budget ~400–700 excluding Still circulating, empty SC section with its heading present.

Not checked: the title, extra headings (contract forbids them — writer discipline), thin/empty sections, and the written SC order. Verbatim messages and the routing side: `routing-rules.md` → "What verify enforces".
