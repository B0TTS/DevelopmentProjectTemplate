"""Route leaf candidates through the identity gates, or verify a written report.

Run, don't read.

    route   python scripts/route-and-verify.py route   --folder <day-folder> [--today YYYY-MM-DD]
    verify  python scripts/route-and-verify.py verify  --folder <day-folder> [--today YYYY-MM-DD]

route: reads <day-folder>/inventory.json + ai.json + swe.json + productivity.json,
applies the streak gate, 7-day window, and update test (mechanical part (a)
plus non-empty delta as the (b) proxy), and writes routed.json. The routed
file is then FROZEN — the writer only words from it.

verify: reads <day-folder>/report.md against inventory.json + routed.json.
Gate violations are errors (exit 1); format nudges (glance bullet count,
word budget) are warnings (exit 0). One rewrite, then ship with a note.

Both commands are stdlib-only. The writer does not apply gates; the writer
does not rescue rejects. See references/routing-rules.md for the rules
behind every check here.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _lib

LEAF_FILES = {
    "AI trends": "ai.json",
    "SWE trends": "swe.json",
    "Productivity": "productivity.json",
}


def load_candidates(folder):
    """Read the three leaf files. Missing/unreadable files are warnings with
    zero candidates — never an abort."""
    candidates = []
    warnings = []
    for section, fname in LEAF_FILES.items():
        p = folder / fname
        if not p.exists():
            warnings.append(f"{fname} missing — treated as zero candidates")
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            warnings.append(f"{fname} unreadable: {e} — treated as zero candidates")
            continue
        items = data.get("items", data) if isinstance(data, dict) else data
        for it in items if isinstance(items, list) else []:
            if isinstance(it, dict):
                c = dict(it)
                c["section"] = section
                candidates.append(c)
    return candidates, warnings


def route_candidate(c, inv, today):
    """Return (destination, reason, url_key, head_key) for one candidate.

    Destinations: main | still_circulating | excluded | dropped.
    The update test's mechanical part (a) — new URL or newer published date —
    runs here. Part (b), the concreteness of the delta, is proxied by a
    non-empty delta string; the wave-lead QA and writer enforce concreteness
    (version, number, decision, CVE id, ship date)."""
    d = _lib.parse_date(c.get("published_date") or c.get("date"))
    if not d:
        return "dropped", "no verifiable YYYY-MM-DD published date", None, None
    if d > today:
        return "dropped", "published date is in the future", None, None
    url_key, head_key = _lib.item_keys(c.get("url") or c.get("link"), c.get("headline"))
    if not url_key and not head_key:
        return "dropped", "no usable URL or headline", None, None

    prior = _lib.find_streak(inv, url_key, head_key)
    if not _lib.in_window(d, today):
        reason = "older than 7 days" if not prior else "older than 7 days and streak-hit"
        return "excluded", reason, url_key, head_key
    if not prior:
        return "main", "fresh", url_key, head_key

    # Streak-hit and within 7 days: only the update test can return it to main.
    a_new_url = bool(url_key and prior.get("url_key") and url_key != prior["url_key"])
    prior_date = _lib.parse_date(prior.get("date"))
    a_newer_date = bool(prior_date and d > prior_date)
    delta = str(c.get("delta_or_null") or c.get("delta") or "").strip()
    if (a_new_url or a_newer_date) and delta:
        return "main", "update test passed", url_key, head_key
    return "still_circulating", "streak-hit, re-proposed, no passing update", url_key, head_key


def make_item(c, url_key, head_key, update=False, reason=None):
    item = {
        "headline": c.get("headline", ""),
        "why": c.get("why", ""),
        "url": c.get("url") or c.get("link") or "",
        "published_date": c.get("published_date") or c.get("date") or "",
        "domain": c.get("domain", ""),
        "source_type": c.get("source_type", ""),
        "delta": c.get("delta_or_null") or c.get("delta") or "",
        "url_key": url_key,
        "head_key": head_key,
        "identity": _lib.identity_key(url_key, head_key),
        "update": update,
    }
    if reason:
        item["reason"] = reason
    return item


def cmd_route(args):
    folder = Path(args.folder)
    inv_p = folder / "inventory.json"
    if not inv_p.exists():
        print(f"error: {inv_p} not found — run scripts/build-inventory.py first")
        return 1
    try:
        inv = json.loads(inv_p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"error: cannot read inventory.json: {e}")
        return 1
    try:
        today = date.fromisoformat(args.today)
    except ValueError:
        print(f"error: --today must be YYYY-MM-DD, got '{args.today}'")
        return 2

    candidates, warnings = load_candidates(folder)
    routed = {
        "today": args.today,
        "tz": "UTC-10 (fixed offset, no DST)",
        "folder": str(folder),
        "main": {sec: [] for sec in _lib.MAIN_SECTIONS},
        "still_circulating": [],
        "excluded": [],
        "dropped": [],
        "candidate_counts": {sec: 0 for sec in _lib.MAIN_SECTIONS},
        "survivor_counts": {},
        "domain_counts": {sec: {} for sec in _lib.MAIN_SECTIONS},
        "domain_preference_notes": [],
        "exclusions": [],
        "prior_identities": [],
        "warnings": warnings,
    }

    for c in candidates:
        routed["candidate_counts"][c["section"]] += 1
        dest, reason, url_key, head_key = route_candidate(c, inv, today)
        if dest == "main":
            item = make_item(c, url_key, head_key, update=(reason == "update test passed"))
            routed["main"][c["section"]].append(item)
        elif dest == "still_circulating":
            routed["still_circulating"].append(
                make_item(c, url_key, head_key, reason=reason)
            )
        elif dest == "excluded":
            routed["excluded"].append(make_item(c, url_key, head_key, reason=reason))
        else:
            routed["dropped"].append(make_item(c, url_key, head_key, reason=reason))

    # Still circulating: newest published first, cap 10.
    routed["still_circulating"].sort(
        key=lambda it: it["published_date"], reverse=True
    )
    overflow = len(routed["still_circulating"]) - _lib.MAX_STILL_CIRCULATING
    if overflow > 0:
        warnings.append(
            f"{overflow} still-circulating item(s) over the cap of "
            f"{_lib.MAX_STILL_CIRCULATING} were cut (oldest first)"
        )
        routed["still_circulating"] = routed["still_circulating"][:_lib.MAX_STILL_CIRCULATING]

    # Domain spread: max 2 per domain per section is a writer preference.
    # The script notes clusters; it never drops a better item on its own.
    for sec in _lib.MAIN_SECTIONS:
        routed["survivor_counts"][sec] = len(routed["main"][sec])
        counts = {}
        for it in routed["main"][sec]:
            d = it["domain"] or "(no domain)"
            counts[d] = counts.get(d, 0) + 1
        routed["domain_counts"][sec] = counts
        for d, n in counts.items():
            if n > 2:
                routed["domain_preference_notes"].append(
                    f"{sec}: {n} items in domain '{d}' — writer should keep at most "
                    "2 unless better items exist"
                )

    # Exclusion list for the gap-fill wave: everything already surfaced this
    # run (accepted or rejected), plus prior-report streak identities.
    seen = set()
    buckets = (
        [routed["main"][sec] for sec in _lib.MAIN_SECTIONS]
        + [routed["still_circulating"], routed["excluded"], routed["dropped"]]
    )
    for bucket in buckets:
        for it in bucket:
            ident = it["identity"]
            if ident and ident not in seen:
                seen.add(ident)
                routed["exclusions"].append(
                    {"identity": ident, "url": it["url"], "headline": it["headline"]}
                )
    for rec in (inv.get("streak_hits") or {}).values():
        routed["prior_identities"].append(
            {"identity": _lib.identity_key(rec.get("url_key"), rec.get("head_key")),
             "url": rec.get("url"), "headline": rec.get("headline"),
             "last_file": rec.get("last_file")}
        )

    try:
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "routed.json").write_text(
            json.dumps(routed, indent=2) + "\n", encoding="utf-8"
        )
    except OSError as e:
        print(f"error: cannot write routed.json: {e}")
        return 1

    mains = ", ".join(f"{sec} {len(routed['main'][sec])}" for sec in _lib.MAIN_SECTIONS)
    print(
        f"routed -> {folder}/routed.json | main: {mains} | "
        f"still_circulating: {len(routed['still_circulating'])} | "
        f"excluded: {len(routed['excluded'])} | dropped: {len(routed['dropped'])}"
    )
    for w in warnings:
        print("  WARN:", w)
    for n in routed["domain_preference_notes"]:
        print("  NOTE:", n)
    return 0


def cmd_verify(args):
    folder = Path(args.folder)
    errors = []
    warnings = []

    rp = folder / "report.md"
    if not rp.exists():
        print(f"FAIL: {rp} not found")
        return 1
    try:
        text = rp.read_text(encoding="utf-8")
    except OSError as e:
        print(f"FAIL: cannot read report.md: {e}")
        return 1
    try:
        today = date.fromisoformat(args.today)
    except ValueError:
        print(f"error: --today must be YYYY-MM-DD, got '{args.today}'")
        return 2

    sections, parse_warns = _lib.parse_report_md(text)
    # A malformed row in today's report is a contract violation, not a warning.
    for w in parse_warns:
        errors.append(w)
    inv_p, routed_p = folder / "inventory.json", folder / "routed.json"
    if not inv_p.exists() or not routed_p.exists():
        print("FAIL: inventory.json and routed.json must both exist in the folder")
        return 1
    try:
        inv = json.loads(inv_p.read_text(encoding="utf-8"))
        routed = json.loads(routed_p.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"FAIL: cannot read inventory/routed: {e}")
        return 1

    routed_main_ids = {}
    routed_update_ids = set()
    for sec in _lib.MAIN_SECTIONS:
        routed_main_ids[sec] = set()
        for it in routed.get("main", {}).get(sec, []):
            ident = it.get("identity")
            if ident:
                routed_main_ids[sec].add(ident)
            if it.get("update"):
                routed_update_ids.add(ident)
    routed_still_ids = {it.get("identity") for it in routed.get("still_circulating", [])}

    # Main sections: headings, item fields, routing membership, gates.
    for sec in _lib.MAIN_SECTIONS:
        if f"## {sec}" not in text:
            errors.append(f"missing heading '## {sec}'")
    seen_ids = set()
    for sec in _lib.MAIN_SECTIONS:
        items = sections.get(sec, [])
        if len(items) > _lib.MAX_MAIN_ITEMS:
            errors.append(f"{sec}: {len(items)} items (max {_lib.MAX_MAIN_ITEMS})")
        for it in items:
            ident = _lib.identity_key(it["url_key"], it["head_key"])
            if ident in seen_ids:
                errors.append(f"one story, one section — '{it['headline']}' duplicates another main-section identity")
            seen_ids.add(ident)
            if ident not in routed_main_ids[sec]:
                errors.append(
                    f"{sec}: '{it['headline']}' is not in routed.json main for this "
                    "section — the writer cannot rescue rejects"
                )
            prior = _lib.find_streak(inv, it["url_key"], it["head_key"])
            if prior and ident not in routed_update_ids:
                errors.append(
                    f"{sec}: streak collision — '{it['headline']}' appeared in "
                    f"{prior.get('last_file')} and the update test did not pass"
                )
            d = _lib.parse_date(it["date"])
            if not d or not _lib.in_window(d, today):
                errors.append(f"{sec}: '{it['headline']}' date is missing or outside the 7-day window")
            if not it["why"].strip():
                errors.append(f"{sec}: '{it['headline']}' is missing why-it-matters")

    # Still circulating: only routed-for items, in window, capped.
    sc = sections.get(_lib.STILL_SECTION, [])
    if len(sc) > _lib.MAX_STILL_CIRCULATING:
        errors.append(
            f"{_lib.STILL_SECTION}: {len(sc)} rows (max {_lib.MAX_STILL_CIRCULATING})"
        )
    allowed_still = routed_still_ids
    for it in sc:
        ident = _lib.identity_key(it["url_key"], it["head_key"])
        if ident not in allowed_still:
            errors.append(
                f"{_lib.STILL_SECTION}: '{it['headline']}' was not routed for "
                "still-circulating — only streak-hit items that were re-proposed "
                "and failed the update test belong here"
            )
        d = _lib.parse_date(it["date"])
        if not d or not _lib.in_window(d, today):
            errors.append(
                f"{_lib.STILL_SECTION}: '{it['headline']}' date is missing or outside the 7-day window"
            )
    if not sc and f"## {_lib.STILL_SECTION}" in text:
        warnings.append("Still circulating section is empty — omit the heading entirely")

    # Format nudges (soft): glance block and word budget.
    if re.search(r"[*_]{1,2}Today at a glance[*_]{1,2}", text) is None:
        warnings.append("glance label '*Today at a glance*' not found")
    bullet_lines = [
        l for l in text.splitlines()
        if l.strip().startswith("- ") or l.strip().startswith("* ")
    ]
    if len(bullet_lines) != 3:
        warnings.append(f"glance has {len(bullet_lines)} bullet(s), expected exactly 3")
    body_words = len(re.findall(r"\S+", text.split(f"## {_lib.STILL_SECTION}")[0]))
    if not (400 <= body_words <= 700):
        warnings.append(f"word budget {body_words} outside ~400-700 (excluding Still circulating)")

    for e in errors:
        print("  ERROR:", e)
    for w in warnings:
        print("  WARN:", w)
    if errors:
        print(f"FAIL: {len(errors)} gate violation(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: gates clean, {len(warnings)} warning(s)")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("route", help="route leaf candidates -> routed.json")
    r.add_argument("--folder", required=True, help="today's day folder")
    r.add_argument("--today", default=_lib.today_iso())
    r.set_defaults(fn=cmd_route)
    v = sub.add_parser("verify", help="verify report.md against inventory + routed")
    v.add_argument("--folder", required=True, help="today's day folder")
    v.add_argument("--today", default=_lib.today_iso())
    v.set_defaults(fn=cmd_verify)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
