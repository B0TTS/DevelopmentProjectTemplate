# Script review — daily-trends-report skill (S1)

**Purpose:** S1 audit log — every gate/routing rule/verify check in CONTEXT-v2 §Key Terms, §Item Identity & Routing, §Report Contract, §What Success Looks Like (PLAN §0 amendments A1–A4 applied) walked against the 3 scripts. Result: 3 surgical fixes, zero open items.
**Lifespan:** ephemeral working log (S2's input). Probes live beside it in this temp dir.
**Verdicts:** ✓ implemented · FIXED (violation repaired) · BY-DESIGN (out of script scope by contract, documented) · OBSERVED (no action — not contract-covered).

## Rule check

| # | Contract rule | Script locus | Verdict | Evidence |
|---|---|---|---|---|
| 1 | A1: day folders `<YYYY-MM>/<YYYY-MM-DD>/`, index.md at parent | `build-inventory.find_prior_reports` glob `*/*/report.md`; out path `<base>/<YYYY-MM>/<today>/inventory.json` | ✓ | probe1: scanned `2026-08/2026-08-16…17`; root index.md not globbed |
| 2 | A2: canonical today = fixed UTC−10 | `_lib.REPORT_TZ`, `today_iso()` | ✓ | constant + docstring; no IANA tz on this machine (RESEARCH §4) |
| 3 | A3: per-leaf caps 8 searches / 5 reads | — | BY-DESIGN | wave-spec concern (S4), not a script rule |
| 4 | A4: "Still circulating" wording | `_lib.STILL_SECTION` | ✓ | grep: no "Redundant" string in any script |
| 5 | Identity: normalized URL primary (strip tracking query, trailing slash, `www.`/mobile hosts) | `_lib.normalize_url` | ✓ | probe1: `…/a?utm_source=x` → key `https://example.com/a`; `www.example.com/b/` → `https://example.com/b` |
| 6 | Identity: normalized headline fallback (only when URLs differ) | `_lib.normalize_headline`, `identity_key`, `find_streak` | ✓ | probe2: Story H matched via headline key on a new URL |
| 7 | Streak-hit = main-section identity in either of last 2 report files | build-inventory: records from `MAIN_SECTIONS` only | ✓ | code + probe1 streak maps |
| 8 | 0 priors → no streak-hits; 1 prior → its main identities are streak-hits | same (maps per scanned file) | ✓ | code path; no min-scan special-casing |
| 9 | Last 2 report *files*, not calendar days; missed days invent no streak | `find_prior_reports` sorted + `prior[-2:]` | ✓ | probe1 run2 |
| 10 | Today's day folder never treated as history | `p.parent.name != today` | ✓ | probe1: `2026-08-18` excluded |
| 11 | Corrupt/unreadable prior → treated as missing, logged, never abort | build-inventory prior read | FIXED (F1) | pre-fix: UnicodeDecodeError traceback, exit 1; post-fix: WARN + continue, exit 0 |
| 12 | Same-day rerun: inventory ignores today's folder; scripts overwrite outputs | exclusion + `write_text` overwrite | ✓ | probe1 |
| 13 | Streak gate applied every run | `route_candidate` via `find_streak` | ✓ | probe2 |
| 14 | 7-day recency gate; undated items dropped | `parse_date` + `in_window` | ✓ | probe2: undated dropped; `2026-08-10` excluded |
| 15 | Future-dated candidates dropped | `d > today` → dropped | ✓ | probe2 "Future story" |
| 16 | Fresh identity + dated ≤7d → main | `route_candidate` | ✓ | probe2 |
| 17 | Streak-hit + ≤7d + re-proposed + update failed → Still circulating | `route_candidate` | ✓ | probe2 Story A (no delta) |
| 18 | Streak-hit + published >7d → excluded | window check precedes update test | ✓ | probe2 |
| 19 | Update passed → main, flagged as update | (a) pass + non-empty delta → main with `update: true` | ✓ | probe2 Story A v2, Story H CVE |
| 20 | Update test (a) mechanical: new URL or newer published date | `a_new_url` / `a_newer_date` | ✓ | probe2 exercised both branches |
| 21 | Update test (b) concrete delta | non-empty `delta` string as proxy | BY-DESIGN (proxy) | documented: route-and-verify docstrings + RESEARCH §2 — concreteness enforced by lead QA + writer |
| 22 | Update's own date ≤7d even if story older | `in_window` on candidate published date | ✓ | probe2 |
| 23 | No verifiable published date → dropped | `route_candidate` | ✓ | probe2 |
| 24 | Published >7d, no passing update → excluded | `route_candidate` | ✓ | probe2 |
| 25 | Once demoted, returns to main only via update test | streak maps over the 2-file window | ✓ within window | beyond window: O2 |
| 26 | Still circulating cap 10, newest published first | sort desc + cap + cut warning | ✓ | probe2: 14 → 10, newest `2026-08-16` first, "4 over the cap" |
| 27 | Still circulating holds only re-proposed items | only candidates enter SC bucket | ✓ | probe2 |
| 28 | Domain preference max 2/domain — advisory, never drops | `domain_preference_notes` | ✓ | probe2 note: "AI company news" ×3 |
| 29 | Exclusion list for gap-fill wave | `routed.exclusions` + `prior_identities` | ✓ | probe2: 15 exclusions, 14 prior ids |
| 30 | Writer can't rescue rejects or add sources/dates | verify membership + parse-warnings-as-errors | ✓ | probe3 V-rescue, V-sc-in-main → errors |
| 31 | Verify: no main identity collides with last-2 reports unless update passed (criterion 7) | streak collision vs `routed_update_ids` | ✓ | probe3 V-sc-in-main collision error |
| 32 | Verify: update-passed items belong in main, never Still circulating | `allowed_still` set | FIXED (F2) | pre-fix probe3 V-update-in-sc: PASS; post-fix: ERROR |
| 33 | Item fields: headline + why + link + date on every item | parser + verify | FIXED (F3) | headline hole; why/date/url already enforced |
| 34 | Headings: 3 main required, `## Still circulating` optional | verify heading checks | ✓ | probe3 |
| 35 | Main sections: target 3–5, 1–2 valid thin day, max 5 hard, no minimum | verify cap only | ✓ | probe3 V-thin (1 item) PASS; V-cap (6) ERROR |
| 36 | Glance exactly 3 bullets | verify warning (soft) | BY-DESIGN soft | probe3 V-glance2: WARN, exit 0 — RESEARCH §2 |
| 37 | Word budget ~400–700 excluding SC | verify warning (soft) | BY-DESIGN soft | probe3 |
| 38 | One story, one section | verify duplicate identity across main sections | ✓ | code; probe3 |
| 39 | index.md upsert (create if missing; rerun updates the row) | not scripted | BY-DESIGN | RESEARCH §2 — manual SKILL.md instruction; deterministic layer = 2 scripts |
| 40 | Anchors fetch (HN front page + GitHub Trending) | not scripted | BY-DESIGN | RESEARCH §2 — orchestrator via harness web tools |
| 41 | Chat pointer (path + 3 bullets + demote count) | not scripted | BY-DESIGN | RESEARCH §2 — manual step |
| 42 | Exactly 2 entry-point scripts (`route` + `verify` subcommands; `_lib` an import library) | plan structure | ✓ BY-DESIGN | PLAN Complexity Tracking |
| 43 | Stdlib-only | imports: argparse/json/re/sys/datetime/pathlib/`_lib` | ✓ | grep; py_compile clean |
| 44 | Criterion 10 script parts: rerun overwrites, inventory ignores today | exclusion + overwrite | ✓ | probe1 |

## PLAN S1 known review points

| Point | Verdict |
|---|---|
| (1) build-inventory glob `*/*/report.md` matches A1 layout | ✓ — rule 1 |
| (2) update-test (b) non-empty-delta proxy documented as proxy | ✓ BY-DESIGN — rule 21 |
| (3) verify max-item caps but no minimum (thin day valid) | ✓ — rule 35 |
| (4) future-dated candidates dropped | ✓ — rule 15 |
| (5) today's day folder excluded from inventory | ✓ — rule 10 |
| (6) corrupt prior → warning, never abort | FIXED — rule 11 |

## Observed items (no action — not contract-covered)

- **O1** Future-dated prior folder displaces history: probe1 run3 — `2026-09/2026-09-01/report.md` entered the last-2 scan and pushed `2026-08-16` out. Contract drops future-dated *candidates* (rule 15) but defines priors only as "last 2 report files" with today's folder excluded. No action.
- **O2** "Once demoted" memory bound: enforced while a main-section appearance is inside the 2-file window. If a story appears only in Still circulating (or is absent) for 2 consecutive prior files, a later re-proposal reads as fresh again. Permanent memory would require a state database (Non-Goal). No action; S3 routing-rules wording should reflect window semantics.
- **O3** Verify does not flag: unknown extra `##` headings, empty main sections, or a writer dropping routed survivors (no minimum count). Thin day is valid and the writer picks survivors (DoF Medium) — a count check would contradict the contract. A title-as-H2 is also a legitimate H2, making a heading whitelist risky. No action.
- **O4** Verify does not check the written Still-circulating table's newest-first order; order is enforced upstream by routed.json's sort, which the writer copies. No action.
- **O5** Reason strings: a candidate with no URL/headline and no date reports "no verifiable YYYY-MM-DD published date" (date check runs first). Destination is correct; message slightly misleading. Cosmetic. No action.
- **O6** Verify's read of today's report.md catches OSError but not UnicodeError — an undecodable report.md exits 1 via traceback instead of a clean FAIL line. Fail semantics (exit 1) are preserved; cosmetic. No action.

## Fixes applied

### F1 — corrupt prior aborted the whole inventory build

- Rule: "Corrupt/unreadable prior → treat as missing, log it, do not abort" (CONTEXT-v2 History window; PLAN S1 point 6).
- Locus: `build-inventory.py` main(), prior-file read.
- Before: `except OSError as e:` — a prior `report.md` with invalid UTF-8 raised `UnicodeDecodeError` (a ValueError, not OSError) → unhandled traceback, exit 1, run aborted.
- After: `except (OSError, UnicodeError) as e:` — decode failure lands in the existing warning path ("cannot read … (treated as missing)"), scan continues, exit 0.
- Justification: probe1 run1 pre-fix crashed exactly on a corrupt prior in the last-2; post-fix warns and continues. One-token change; the never-abort rule is also stated in the script's own docstring.

### F2 — verify allowed update-passed items in Still circulating

- Rule: "Update test passed (delta dated ≤7d) → Main section"; SC membership = re-proposed AND failed the update test (routing table + Report Contract Still circulating).
- Locus: `route-and-verify.py` cmd_verify, `allowed_still = routed_still_ids | routed_update_ids`.
- Before: the union let a writer bury an update-passed item in the Still circulating table and verify passed.
- After: `allowed_still = routed_still_ids` — such an item now fails with the error text the script itself prints ("…only streak-hit items that were re-proposed and failed the update test belong here").
- Justification: probe3 V-update-in-sc pre-fix exit 0 / post-fix exit 1. The union contradicted both the routing table and the script's own error message for that check. The main-section collision exemption via `routed_update_ids` is unaffected (probe3 V-pass still passes).

### F3 — parser silently skipped table rows with no headline

- Rule: item fields "Headline · why · link · date" + criterion 1 (every item carries a headline).
- Locus: `_lib.py` `parse_report_md`, empty-headline branch.
- Before: `if not headline: continue` — a row with a date and link but an empty Headline cell was silently dropped; verify passed with zero warnings.
- After: `warnings.append(f"line {lineno}: table row without Headline skipped"); continue` — mirrors the documented date/URL convention in the parser's docstring; verify turns it into an ERROR.
- Justification: probe3 V-empty-headline pre-fix exit 0 / post-fix exit 1. Headline is a required field like date and URL; the silent skip made the verify gate report PASS on a contract-violating report.

## Probe evidence (throwaway, this temp dir)

- probe1 (build-inventory): last-2 file selection ✓, today excluded ✓, older folders dropped ✓, streak maps + URL normalization ✓, corrupt prior crash → fixed ✓, future-folder displacement O1.
- probe2 (route): all 6 routing rows ✓, update test both branches ✓, SC cap/sort ✓, domain notes ✓, missing leaf files warn-not-abort ✓, exclusion list ✓.
- probe3 (verify): baseline PASS (soft word-budget warning only) ✓, rescue-reject ERROR ✓, update-in-SC hole → fixed ✓, empty-headline hole → fixed ✓, SC-in-main ERROR ✓, 7-day ERROR ✓, thin-day PASS ✓, glance-2 WARN ✓, 6-item cap ERROR ✓.

## Final verdict

3 scripts audited against 44 rules: 39 ✓ (incl. 5 documented BY-DESIGN), 3 FIXED, 2 OBSERVED-no-action. **Zero OPEN items.** `python -m py_compile` clean on all 3 scripts; stdlib-only confirmed; no comments added to scripts (F3 adds a warning string, mirroring existing warnings). Scripts remain un-executed against real data; S2 fixture suite proceeds on this baseline.
