"""Build inventory.json from the last 2 report files (excluding today's folder).

Run, don't read:

    python scripts/build-inventory.py --base "b0ttsagent/reports/daily-reports/AI-Development Trends" [--today YYYY-MM-DD] [--out PATH]

Defaults: --today is the canonical today (UTC-10); --out is
<base>/<YYYY-MM>/<YYYY-MM-DD>/inventory.json (created if missing).

Exit 0 on success, 1 if the output cannot be written. Warnings never abort —
a corrupt prior report is treated as missing and logged.

The inventory is a throwaway parse of the report files (the source of
truth), rebuilt every run. Never hand-edit it.
"""

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _lib


def find_prior_reports(base, today):
    """Ascending (oldest-first) list of the last 2 report files, excluding
    today's day folder. Day folders sort because they are YYYY-MM-DD; month
    folders sort because they are YYYY-MM. The streak-map builder relies on
    oldest-first order (later records overwrite earlier ones)."""
    reports = sorted(
        base.glob("*/*/report.md"),
        key=lambda p: (p.parent.parent.name, p.parent.name),
    )
    prior = [p for p in reports if p.parent.name != today]
    return prior[-2:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True, help="reports root, e.g. the 'AI-Development Trends' folder")
    ap.add_argument("--today", default=_lib.today_iso(), help="YYYY-MM-DD, defaults to canonical today (UTC-10)")
    ap.add_argument("--out", default=None, help="output path, defaults to <base>/<YYYY-MM>/<today>/inventory.json")
    args = ap.parse_args()

    try:
        today = date.fromisoformat(args.today)
    except ValueError:
        print(f"error: --today must be YYYY-MM-DD, got '{args.today}'")
        return 2

    base = Path(args.base)
    if args.out:
        out = Path(args.out)
    else:
        out = base / args.today[:7] / args.today / "inventory.json"

    warnings = []
    scanned_files = []
    records = []

    for rp in find_prior_reports(base, args.today):
        try:
            text = rp.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as e:
            warnings.append(f"cannot read {rp}: {e} (treated as missing)")
            continue
        try:
            sections, w = _lib.parse_report_md(text)
        except Exception as e:  # corrupt file: treat as missing, do not abort
            warnings.append(f"corrupt/unparseable {rp}: {e} (treated as missing)")
            continue
        for wmsg in w:
            warnings.append(f"{rp}: {wmsg}")
        rel_file = f"{rp.parent.parent.name}/{rp.parent.name}/report.md"
        scanned_files.append(rel_file)
        for sec in _lib.MAIN_SECTIONS:
            for it in sections.get(sec, []):
                records.append({
                    "file": rel_file,
                    "day": rp.parent.name,
                    "section": it["section"],
                    "headline": it["headline"],
                    "url": it["url"],
                    "url_key": it["url_key"],
                    "head_key": it["head_key"],
                    "date": it["date"],
                    "domain": it["domain"],
                })

    # Streak maps: main-section identities over the scanned files.
    # Records arrive oldest-first, so overwriting keeps the newest occurrence.
    streak_hits = {}
    streak_headline_hits = {}
    for r in records:
        rec = {
            "last_file": r["file"],
            "section": r["section"],
            "headline": r["headline"],
            "url": r["url"],
            "url_key": r["url_key"],
            "head_key": r["head_key"],
            "date": r["date"],
            "domain": r["domain"],
        }
        if r["url_key"]:
            streak_hits[r["url_key"]] = rec
        if r["head_key"]:
            streak_headline_hits[r["head_key"]] = rec

    payload = {
        "generated_at": datetime.now(_lib.REPORT_TZ).isoformat(),
        "tz": "UTC-10 (fixed offset, no DST)",
        "today": args.today,
        "reports_scanned": scanned_files,
        "streak_hits": streak_hits,
        "streak_headline_hits": streak_headline_hits,
        "warnings": warnings,
    }

    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    except OSError as e:
        print(f"error: cannot write {out}: {e}")
        return 1

    print(
        f"wrote {out}: scanned {len(scanned_files)} prior report(s), "
        f"{len(streak_hits)} url-key streak hits, "
        f"{len(streak_headline_hits)} headline-key hits, "
        f"{len(warnings)} warning(s)"
    )
    for w in warnings:
        print("  WARN:", w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
