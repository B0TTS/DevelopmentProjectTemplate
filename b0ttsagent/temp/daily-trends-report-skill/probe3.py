"""Probe 3: verify subcommand — pass baseline + contract-violation variants.

Run BEFORE and AFTER the S1 script fixes; variants V-update-in-sc and
V-empty-headline are the two suspected gate holes being demonstrated.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TMP = Path(__file__).resolve().parent
RV = ROOT / ".agents/skills/daily-trends-report/scripts/route-and-verify.py"
DAY = TMP / "probe3-day"
TODAY = "2026-08-18"

PAD = ("The significance here is that teams adopting this in production will see "
       "measurable changes in their delivery cadence and operational posture over "
       "the next quarter, and practitioners who skip it will fall behind their "
       "peers on core workflows and incident response, so it is worth a click "
       "before planning next week's work and on-call rotations.")

def base_inventory():
    return {
        "streak_hits": {
            "https://example.com/u1": {
                "last_file": "2026-08/2026-08-17/report.md", "section": "AI trends",
                "headline": "Story U1", "url": "https://example.com/u1",
                "url_key": "https://example.com/u1", "head_key": "story u1",
                "date": "2026-08-15", "domain": "AI company news"},
            "https://example.com/s1": {
                "last_file": "2026-08/2026-08-17/report.md", "section": "SWE trends",
                "headline": "Story S1", "url": "https://example.com/s1",
                "url_key": "https://example.com/s1", "head_key": "story s1",
                "date": "2026-08-14", "domain": "security & CVEs"},
        },
        "streak_headline_hits": {},
    }

def base_routed():
    return {
        "main": {
            "AI trends": [
                {"identity": "https://example.com/f1", "headline": "Fresh story",
                 "url": "https://example.com/f1", "update": False},
                {"identity": "https://example.com/u1", "headline": "Story U1",
                 "url": "https://example.com/u1", "update": True},
            ],
            "SWE trends": [
                {"identity": "https://example.com/w1", "headline": "SWE fresh",
                 "url": "https://example.com/w1", "update": False},
            ],
            "Productivity": [
                {"identity": "https://example.com/p1", "headline": "Prod fresh",
                 "url": "https://example.com/p1", "update": False},
            ],
        },
        "still_circulating": [
            {"identity": "https://example.com/s1", "headline": "Story S1",
             "url": "https://example.com/s1"},
        ],
    }

def main_table(rows):
    lines = ["| Domain | Headline | Why it matters | Date | Link |", "|---|---|---|---|---|"]
    for domain, headline, why, date, url in rows:
        lines.append(f"| {domain} | {headline} | {why} | {date} | {url} |")
    return "\n".join(lines)

def sc_table(rows):
    lines = ["| Headline | Date | Link |", "|---|---|---|"]
    for headline, date, url in rows:
        lines.append(f"| {headline} | {date} | {url} |")
    return "\n".join(lines)

def make_report(ai_rows, swe_rows, prod_rows, sc_rows, n_bullets=3):
    bullets = "\n".join(
        f"- Glance bullet {i}: {PAD[:60]}" for i in range(1, n_bullets + 1))
    sc = f"\n\n## Still circulating\n\n{sc_table(sc_rows)}" if sc_rows else ""
    return f"""# AI-Development Trends — 2026-08-18

*Today at a glance*
{bullets}

## AI trends

{main_table(ai_rows)}

## SWE trends

{main_table(swe_rows)}

## Productivity

{main_table(prod_rows)}{sc}
"""

def run_variant(name, routed, ai, swe, prod, sc, n_bullets=3):
    (DAY / "inventory.json").write_text(json.dumps(base_inventory()), encoding="utf-8")
    (DAY / "routed.json").write_text(json.dumps(routed), encoding="utf-8")
    (DAY / "report.md").write_text(make_report(ai, swe, prod, sc, n_bullets), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(RV), "verify", "--folder", str(DAY), "--today", TODAY],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    print(f"--- {name} ---")
    print("exit:", r.returncode)
    print(r.stdout.strip())
    if r.stderr.strip():
        print("stderr:", r.stderr.strip()[:1200])
    print()

def main():
    DAY.mkdir(parents=True, exist_ok=True)
    F1 = ("frontier model releases", "Fresh story", PAD, "2026-08-17", "https://example.com/f1")
    U1 = ("AI company news", "Story U1", "Now cites v2.0 which shipped on 2026-08-17. " + PAD,
          "2026-08-17", "https://example.com/u1")
    W1 = ("languages & frameworks", "SWE fresh", PAD, "2026-08-16", "https://example.com/w1")
    P1 = ("AI-assisted dev workflows", "Prod fresh", PAD, "2026-08-15", "https://example.com/p1")
    S1 = ("Story S1", "2026-08-14", "https://example.com/s1")

    r = base_routed()

    run_variant("V-pass baseline", r, [F1, U1], [W1], [P1], [S1])
    run_variant("V-rescue (non-routed item in main)", r,
                [F1, U1, ("AI infra/hardware", "Rescued reject", PAD, "2026-08-17", "https://example.com/rescue")],
                [W1], [P1], [S1])
    run_variant("V-update-in-sc (update-passed item written in Still circulating)", r,
                [F1], [W1], [P1], [S1, ("Story U1", "2026-08-17", "https://example.com/u1")])
    run_variant("V-empty-headline (row with date+link but no headline)", r,
                [F1, U1, ("AI infra/hardware", "", "Has date and link. " + PAD, "2026-08-17", "https://example.com/hl")],
                [W1], [P1], [S1])
    run_variant("V-sc-in-main (SC-routed story written in main)", r,
                [F1, U1, ("security & CVEs", "Story S1", PAD, "2026-08-14", "https://example.com/s1")],
                [W1], [P1], [])
    run_variant("V-window (main item outside 7-day window)", r,
                [F1, U1], [("languages & frameworks", "SWE fresh", PAD, "2026-08-10", "https://example.com/w1")],
                [P1], [S1])
    run_variant("V-thin (1 item per section is valid)", r,
                [F1], [W1], [P1], [S1])
    run_variant("V-glance2 (2 bullets: warning, not failure)", r,
                [F1, U1], [W1], [P1], [S1], n_bullets=2)

    # cap: 6 fresh items in AI
    cap_routed = base_routed()
    extra = []
    for i in range(4):
        extra.append({"identity": f"https://example.com/x{i}", "headline": f"Extra {i}",
                      "url": f"https://example.com/x{i}", "update": False})
    cap_routed["main"]["AI trends"] = cap_routed["main"]["AI trends"] + extra
    cap_rows = [F1, U1] + [("AI company news", f"Extra {i}", PAD, "2026-08-17", f"https://example.com/x{i}")
                           for i in range(4)]
    run_variant("V-cap (6 main items -> error)", cap_routed, cap_rows, [W1], [P1], [S1])


if __name__ == "__main__":
    main()
