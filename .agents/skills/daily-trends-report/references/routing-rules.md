# Routing rules — daily-trends-report skill (reference)

Authoritative reference for the deterministic routing layer. The scripts in `../scripts/` are the executable truth — if this doc and a script disagree, the script wins and this doc is wrong.

> **Contract of record.** This doc describes the verified behavior of the audited scripts: `build-inventory.py`, `route-and-verify.py` (subcommands `route` / `verify`), with shared helpers in `_lib.py`. S1 audit: 44 rules walked, 3 fixes. S2 fixtures: 8 scenarios, all PASS. Nothing here is aspirational.

## TOC

- [Purpose and authority](#purpose-and-authority)
- [Run order](#run-order)
- [Locked constants](#locked-constants)
- [Item identity](#item-identity)
- [The inventory and its history window](#the-inventory-and-its-history-window)
- [The gates](#the-gates)
- [The update test](#the-update-test)
- [The routing table](#the-routing-table)
- [Still circulating](#still-circulating)
- [Domain preference](#domain-preference)
- [Exclusion list and prior identities](#exclusion-list-and-prior-identities)
- [What verify enforces](#what-verify-enforces)
- [Who enforces what](#who-enforces-what)

## Purpose and authority

Who reads this: the orchestrator running the skill, and the writer drafting `report.md`. It answers one question — where does each candidate item go, and why — with the rules exactly as the scripts implement them. The report's shape and wording rules live in `report-contract.md`; wave mechanics live in `wave-spec.md`.

- Rules enforced by a script are the norm here; rules the lead QA or writer enforce are marked **writer/QA** and listed in [Who enforces what](#who-enforces-what).
- Each section cites its implementing locus (`_lib.py`, `build-inventory.py`, `route-and-verify.py`) so drift between doc and code is visible.
- `_lib.py` is an import library, not an entry point. The deterministic layer is exactly two entry-point scripts, as CONTEXT-v2 mandates.

## Run order

Two entry points, run in this order. Both are stdlib-only and both accept `--today YYYY-MM-DD`, which defaults to the canonical UTC−10 today:

```text
python scripts/build-inventory.py --base "<reports root>" [--today YYYY-MM-DD] [--out PATH]
python scripts/route-and-verify.py route   --folder "<day folder>" [--today YYYY-MM-DD]
python scripts/route-and-verify.py verify  --folder "<day folder>" [--today YYYY-MM-DD]
```

`build-inventory` writes `inventory.json` (default output: `<reports root>/<YYYY-MM>/<today>/inventory.json`). `route` reads `inventory.json` plus the three leaf files (`ai.json`, `swe.json`, `productivity.json`) and writes `routed.json` into the day folder — after which `routed.json` is frozen; the writer only words from it. `verify` checks the written `report.md` against both files. `route` exits 1 if `inventory.json` is absent, telling the orchestrator to run `build-inventory.py` first.

## Locked constants

All live in `_lib.py`. Changing any of them means updating this doc and re-running `eval-fixtures.md`.

| Constant | Value | Meaning |
|---|---|---|
| `REPORT_TZ` | UTC−10, fixed offset (HST, no DST) | Canonical "today" and the base of the 7-day window. Fixed offset because this machine's zoneinfo has no IANA database; the offset is exact, not approximate. |
| `RECENCY_DAYS` | 7 | Only items published within 7 days may appear anywhere in the report. |
| `MAX_STILL_CIRCULATING` | 10 | Still circulating cap. |
| `MAX_MAIN_ITEMS` | 5 | A main section never exceeds 5 items. |
| `MAIN_SECTIONS` | AI trends · SWE trends · Productivity | The three main sections, in this order. |
| `STILL_SECTION` | Still circulating | The residue section heading. |
| `TRACKING_PARAMS` | 25 query-param names | Stripped from URL identity keys (list in [Item identity](#item-identity)). |

## Item identity

Identity is how two findings are recognized as the same story. Every gate and every verify check uses identity keys, never raw strings. Locus: `_lib.py` (`normalize_url`, `normalize_headline`, `identity_key`, `find_streak`).

**URL key (primary).** `normalize_url` produces the key, or `None` when the input is not an http(s) URL. Normalization steps, in order:

1. Lowercase the scheme and host.
2. Strip a leading `www.`, `m.`, or `mobile.` host prefix.
3. Drop the fragment.
4. Drop tracking query params (the `TRACKING_PARAMS` set); keep every other query param.
5. Strip the trailing slash from the path.

`TRACKING_PARAMS` (25 names): `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`, `utm_id`, `fbclid`, `gclid`, `gclsrc`, `dclid`, `msclkid`, `twclid`, `ref`, `ref_src`, `referrer`, `source`, `cmpid`, `mc_cid`, `mc_eid`, `igshid`, `srsltid`, `vero_id`, `yclid`, `_hsenc`, `_hsmi`.

**Headline key (fallback).** `normalize_headline`: lowercase, every run of non-alphanumeric characters becomes a single space, whitespace collapsed. Used only when URLs differ but name the same story.

**Key precedence.** `identity_key` is the URL key when present, else `headline:<headline key>`. `find_streak` looks the candidate up in the inventory's `streak_hits` map (URL keys) first; only on a miss does it try `streak_headline_hits` (headline keys). Consequences: same URL → streak-hit even under a rewritten headline; different URL + same normalized headline → streak-hit.

**Leaf field names.** The route script reads `published_date` (alias `date`), `url` (alias `link`), `delta_or_null` (alias `delta`), plus `headline`, `why`, `domain`, `source_type`. The canonical names are the wave-spec leaf schema — see `wave-spec.md`.

## The inventory and its history window

`build-inventory.py` rebuilds `inventory.json` from scratch every run. It is a throwaway parse, never a state database, never hand-edited. Locus: `find_prior_reports` and the streak maps at the end of `main()`.

**Window = last 2 report files, not calendar days.** The script globs `<base>/*/*/report.md` (the A1 month/day layout), sorts by folder names, drops today's day folder, and keeps the last 2. Missed calendar days invent nothing:

- 0 priors → no streak-hits anywhere.
- 1 prior → that file's main-section identities are the streak-hits.
- 2 priors → the union of both files' main-section identities.

**Only main sections feed history.** Records come from `## AI trends`, `## SWE trends`, and `## Productivity` only. An identity that appeared only in `## Still circulating` contributes nothing to the streak maps — this is what bounds the "once demoted" memory (below).

**Edge cases:**

| Case | Behavior |
|---|---|
| Today's day folder | Excluded by folder name, so a same-day rerun never treats its own report as history. |
| Corrupt prior (undecodable or unparseable) | Warning "…(treated as missing)", scan continues, exit 0 — never abort (F1). If all priors are corrupt, the run proceeds like a fresh run. |
| Prior row missing date/URL/headline | Skipped for inventory purposes; the warning is forwarded into `inventory.json`. |
| Future-dated prior folder name | Selection is purely lexical on folder names; a folder like `2026-09/2026-09-01/report.md` sorts after today and can displace real history (O1). Not validated — candidates are the only date-checked input. |

Each streak record carries `last_file` — the most recent prior file the identity appeared in — which verify quotes in its collision error.

> **"Once demoted" is window semantics, not permanent memory (O2).** An identity returns to a main section only via the update test — while a main-section appearance of it remains inside the last-2-file window. Because the inventory tracks main-section appearances only, an identity that stays out of the main sections for 2 consecutive prior files (Still circulating only, or absent) falls out of the inventory, and a later re-proposal reads as fresh again. Permanent memory would require a state database, which is a non-goal: the report files are the source of truth, and the inventory is a windowed view of them.

## The gates

Two gates, applied by the route script to every candidate on every run. Locus: `route_candidate`.

**Streak gate.** If the candidate's identity matches a main-section identity of either of the last 2 report files (via the inventory's streak maps), the candidate is a streak-hit and is demoted unless the update test passes.

**7-day recency gate.** A candidate's published date must fall inside `[today − 7, today]` — both endpoints inclusive (`_lib.in_window`). Consequences, in the script's check order:

- Undated candidate → **dropped**: "no verifiable YYYY-MM-DD published date".
- Future-dated candidate → **dropped**: "published date is in the future".
- Candidate with neither URL nor headline → **dropped**: "no usable URL or headline".
- Out-of-window candidate → **excluded**. Because the window check precedes the update test, the update's own date must itself be ≤7 days: a streak-hit carrying a delta but an out-of-window date is excluded anyway, even if the original story is much older.

## The update test

Re-entry to a main section for a streak-hit identity requires passing the update test. Locus: `route_candidate`.

- **Part (a), mechanical — scripted.** Passes if either: a **new URL** — the candidate's URL key differs from the URL key recorded for the prior occurrence (both present); or a **newer date** — the candidate's published date is strictly later than the Date recorded in the prior report row.
- **Part (b), delta concreteness — proxied by the script, enforced by lead QA + writer.** The script requires a non-empty `delta_or_null` string; it cannot judge whether the delta is concrete. Concreteness — a version, number, decision, CVE id, ship date — is the lead QA's and the writer's job. "Still being discussed" is not a delta, and the script will not catch it if it is written into the delta field.

Both parts must hold. The script passes the update test only when (a) holds **and** the delta is non-empty; a streak-hit, in-window candidate that fails either part lands in Still circulating ("streak-hit, re-proposed, no passing update"). An update-passed candidate routes to main with `update: true` and its `delta` carried in `routed.json`; the writer frames the item as an update citing that delta.

## The routing table

`route_candidate` checks, in order: date parseable → not future → has URL or headline → in window → prior lookup → update test. Destinations and the exact reason strings written into `routed.json`:

| Condition (checked in order) | Destination | Reason in routed.json |
|---|---|---|
| No verifiable YYYY-MM-DD date | dropped | "no verifiable YYYY-MM-DD published date" |
| Date in the future | dropped | "published date is in the future" |
| No URL and no headline | dropped | "no usable URL or headline" |
| Outside the 7-day window | excluded | "older than 7 days" — or "older than 7 days and streak-hit" |
| In window, no prior match | main (fresh) | "fresh" |
| Streak-hit, in window, update test passed | main, flagged update | "update test passed" |
| Streak-hit, in window, re-proposed, update test failed | Still circulating | "streak-hit, re-proposed, no passing update" |

Worth stating plainly:

- A streak-hit older than 7 days is excluded even with a delta — the window check runs before the update test.
- A non-streak item older than 7 days is also excluded ("older than 7 days").
- Once demoted, the only path back to a main section is the update test — within the history window (see the O2 note in [The inventory and its history window](#the-inventory-and-its-history-window)).

## Still circulating

Residue list, not a second digest. Only candidates the route script sent there can appear — the writer cannot add rows.

- **Membership:** streak-hit + published ≤7 days + re-proposed this run + failed the update test. Items that were not re-proposed this run cannot appear.
- **Sort:** newest published date first. The route script sorts `published_date` descending; the writer copies that order into `report.md`. Verify does not re-check the written order (O4).
- **Cap:** 10. Overflow is cut oldest-first, and the route output warns: "N still-circulating item(s) over the cap of 10 were cut (oldest first)".
- **Rows:** one line — headline · date · link, no why-it-matters. When empty, the whole section (heading included) is omitted; verify warns on an empty section with its heading present.

## Domain preference

Max 2 items per domain per section is a preference, not a gate. After routing, the script counts main-section items per domain per section and prints a NOTE for any domain over 2: "…: N items in domain 'D' — writer should keep at most 2 unless better items exist". It never drops an item and never fails verification. The writer applies the preference while picking the 3–5 survivors; if honoring it would drop a better item or empty a thin section, keep the better item and note the cluster. A blank domain counts as "(no domain)".

## Exclusion list and prior identities

`routed.json` carries two lists the orchestrator hands to the gap-fill wave:

- `exclusions` — every identity surfaced this run, accepted or rejected (main, Still circulating, excluded, dropped), with URL and headline, deduped. The wave is told: do not re-propose these identities unless a dated delta exists.
- `prior_identities` — every streak identity from the inventory (the last-2-file main-section history), each with its `last_file`.

`routed.json` also carries `survivor_counts` per section — the orchestrator triggers the single gap-fill wave when a section has 0–2 survivors. Gap-fill mechanics (target exactly 3, one wave max) are orchestration — see `wave-spec.md`.

## What verify enforces

`verify` reads `report.md` against `inventory.json` + `routed.json`. Gate violations are errors (exit 1); format nudges are warnings (exit 0). The full list, so the writer knows the exact bar:

**Errors — any of these fails verify:**

| Check | Error text (abridged) |
|---|---|
| report.md, inventory.json, routed.json present and readable | "FAIL: … not found" / "cannot read" |
| Each main heading present | "missing heading '## …'" |
| Every table row has Headline, YYYY-MM-DD date, URL — parser warnings become errors | "table row without Headline skipped" (F3) |
| Main section ≤5 items | "… (max 5)" |
| No duplicate identity across main sections | "one story, one section …" |
| Main items only from routed.json main for their section | "the writer cannot rescue rejects" |
| Streak collision exempt only when the update test passed | "streak collision … update test did not pass" |
| Every main item date inside the 7-day window | "date is missing or outside the 7-day window" |
| Every main item has non-empty why-it-matters | "is missing why-it-matters" |
| Still circulating ≤10 rows | "… (max 10)" |
| SC rows only from routed SC — update-passed items buried in SC fail too | "only streak-hit items that were re-proposed and failed the update test belong here" (F2) |
| SC row dates inside the 7-day window | "date is missing or outside the 7-day window" |

**Warnings — never fail the run:**

- Glance label `*Today at a glance*` not found.
- Bullet-line count in the file not exactly 3 (the glance must be the file's only list).
- Word budget outside ~400–700, excluding the Still circulating section (the token count of everything before the `## Still circulating` heading).
- `## Still circulating` heading present but the section is empty.

**Deliberately not checked** (contract-consistent gaps, not holes to exploit):

- Unknown extra `##` headings are ignored by the parser — the contract still forbids them; that part is writer discipline.
- Empty main sections and fewer items than routed pass — thin days are valid, the writer picks survivors, and there is no minimum count.
- The written Still circulating order is not re-verified — the writer copies routed.json's newest-first order (O4).

## Who enforces what

| Rule | Enforced by |
|---|---|
| Identity normalization, streak detection, 7-day window, routing, SC sort/cap, exclusion lists | Scripts (`build-inventory`, `route`, `verify`) |
| Update test part (a) — new URL or newer date | Script |
| Update test part (b) — non-empty delta | Script (proxy) |
| Update test part (b) — delta concreteness | Lead QA + writer |
| Domain spread ≤2 per domain per section | Script notes; writer applies |
| report.md skeleton, item wording, SC no-why, no outro | Writer (field-level gates by verify) |
| Update framing citing the delta | Writer |
| Per-leaf caps: 8 searches / 5 page-reads (A3) | Wave-lead QA — not scripted |
| Anchors fetch (HN front page + GitHub Trending) | Orchestrator via harness web tools — not scripted |
| index.md upsert; chat pointer | Orchestrator — not scripted |
