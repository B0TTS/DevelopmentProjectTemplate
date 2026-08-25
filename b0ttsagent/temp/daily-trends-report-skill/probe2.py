"""Probe 2: route subcommand — gates, update test, SC cap/sort, domain notes, exclusions."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TMP = Path(__file__).resolve().parent
ROUTE = ROOT / ".agents/skills/daily-trends-report/scripts/route-and-verify.py"
DAY = TMP / "probe2-day"

TODAY = "2026-08-18"  # window: 2026-08-11 .. 2026-08-18


def main():
    streak_hits = {}
    streak_headline_hits = {}

    def add_prior(url, headline, date, domain="AI company news"):
        url_key = url.replace("?utm_source=x", "").replace("www.", "")
        head_key = "".join(c.lower() for c in headline if c.isalnum() or c == " ").replace("  ", " ")
        rec = {"last_file": "2026-08/2026-08-17/report.md", "section": "AI trends",
               "headline": headline, "url": url, "url_key": url_key, "head_key": head_key,
               "date": date, "domain": domain}
        streak_hits[url_key] = rec
        streak_headline_hits[head_key] = rec

    add_prior("https://example.com/a?utm_source=x", "Story A", "2026-08-15")
    add_prior("https://example.com/h", "Story H", "2026-08-14")
    for n in range(1, 13):
        add_prior(f"https://example.com/s{n}", f"Story S{n}", f"2026-08-{10 + (n + 1) // 2}")

    inv = {"today": "2026-08-17", "streak_hits": streak_hits,
           "streak_headline_hits": streak_headline_hits, "warnings": []}
    DAY.mkdir(parents=True, exist_ok=True)
    (DAY / "inventory.json").write_text(json.dumps(inv), encoding="utf-8")

    ai = [
        {"headline": "Fresh in window", "why": "w", "url": "https://example.com/f1",
         "published_date": "2026-08-17", "domain": "frontier model releases", "source_type": "post"},
        {"headline": "Undated story", "why": "w", "url": "https://example.com/u1"},
        {"headline": "Future story", "why": "w", "url": "https://example.com/fut",
         "published_date": "2026-08-19", "domain": "AI company news"},
        {"headline": "Old fresh", "why": "w", "url": "https://example.com/old",
         "published_date": "2026-08-10", "domain": "AI company news"},
        {"headline": "Story A", "why": "w", "url": "https://example.com/a",
         "published_date": "2026-08-15", "domain": "AI company news"},
        {"headline": "Story A", "why": "w", "url": "https://example.com/a",
         "published_date": "2026-08-17", "delta_or_null": "v2.0 released 2026-08-17",
         "domain": "open-source AI"},
        {"headline": "Story H", "why": "w", "url": "https://news.example.com/h-new",
         "published_date": "2026-08-16", "delta_or_null": "CVE-2026-1234 patched in 1.2.3",
         "domain": "AI policy/regulation"},
        {"headline": "No identity item", "why": "w"},
        {"headline": "Story A", "why": "w", "url": "https://example.com/a",
         "published_date": "2026-08-15", "delta_or_null": "still being discussed",
         "domain": "AI company news"},
    ]
    for i in range(10, 13):
        ai.append({"headline": f"Cluster {i}", "why": "w", "url": f"https://example.com/c{i}",
                   "published_date": f"2026-08-{i + 6}", "domain": "AI company news", "source_type": "post"})
    for n in range(1, 13):
        ai.append({"headline": f"Story S{n}", "why": "w", "url": f"https://example.com/s{n}",
                   "published_date": f"2026-08-{10 + (n + 1) // 2}", "domain": "AI infra/hardware"})

    (DAY / "ai.json").write_text(json.dumps({"items": ai}), encoding="utf-8")
    # swe.json and productivity.json intentionally absent -> warning, never abort

    r = subprocess.run(
        [sys.executable, str(ROUTE), "route", "--folder", str(DAY), "--today", TODAY],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    print("exit:", r.returncode)
    print(r.stdout)
    if r.stderr.strip():
        print("stderr:", r.stderr.strip()[:1500])
    routed = json.loads((DAY / "routed.json").read_text(encoding="utf-8"))
    print("main counts:", {s: len(v) for s, v in routed["main"].items()})
    for s in ("AI trends", "SWE trends", "Productivity"):
        for it in routed["main"][s]:
            print("  MAIN", s, "|", it["headline"], "| update:", it["update"], "|", it["published_date"])
    print("still_circulating:", [(it["headline"], it["published_date"]) for it in routed["still_circulating"]])
    print("excluded:", [(it["headline"], it["reason"]) for it in routed["excluded"]])
    print("dropped:", [(it["headline"], it["reason"]) for it in routed["dropped"]])
    print("domain notes:", routed["domain_preference_notes"])
    print("n exclusions:", len(routed["exclusions"]), "| n prior_identities:", len(routed["prior_identities"]))


if __name__ == "__main__":
    main()
