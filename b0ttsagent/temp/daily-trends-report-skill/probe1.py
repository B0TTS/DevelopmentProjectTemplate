"""Probe 1: build-inventory behavior. Throwaway S1 probe, not the S2 fixture suite."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TMP = Path(__file__).resolve().parent
BUILD = ROOT / ".agents/skills/daily-trends-report/scripts/build-inventory.py"
BASE = TMP / "probe1" / "AI-Development Trends"


def report(title_day, rows_ai=(), rows_swe=(), rows_prod=()):
    def table(rows):
        lines = ["| Domain | Headline | Why it matters | Date | Link |",
                 "|---|---|---|---|---|"]
        for domain, headline, why, date, url in rows:
            lines.append(f"| {domain} | {headline} | {why} | {date} | {url} |")
        return "\n".join(lines)

    return f"""# AI-Development Trends — {title_day}

*Today at a glance*
- bullet one
- bullet two
- bullet three

## AI trends

{table(rows_ai)}

## SWE trends

{table(rows_swe)}

## Productivity

{table(rows_prod)}
"""


def run_build(extra_label, out):
    r = subprocess.run(
        [sys.executable, str(BUILD), "--base", str(BASE), "--today", "2026-08-18", "--out", str(out)],
        capture_output=True, text=True, cwd=str(ROOT),
    )
    print(f"--- {extra_label} ---")
    print("exit:", r.returncode)
    print("stdout:", r.stdout.strip())
    if r.stderr.strip():
        print("stderr:", r.stderr.strip()[:2000])
    if out.exists():
        inv = json.loads(out.read_text(encoding="utf-8"))
        print("scanned:", inv["reports_scanned"])
        print("streak url keys:", sorted(inv["streak_hits"].keys()))
        print("streak headline keys:", sorted(inv["streak_headline_hits"].keys()))
        if inv["streak_hits"]:
            k = sorted(inv["streak_hits"].keys())[0]
            print("sample streak rec:", inv["streak_hits"][k])
        print("warnings:", inv["warnings"])
    print()


def setup_run1():
    # priors: 07-30, 08-15 (good), 08-16 (good), 08-17 CORRUPT, 08-18 = today
    (BASE / "2026-07" / "2026-07-30").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-07" / "2026-07-30" / "report.md").write_text(
        report("2026-07-30", [("AI company news", "Old story", "Old.", "2026-07-29", "https://example.com/old")]),
        encoding="utf-8")
    (BASE / "2026-08" / "2026-08-15").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-08" / "2026-08-15" / "report.md").write_text(
        report("2026-08-15", [("AI policy/regulation", "Mid story", "Mid.", "2026-08-14", "https://example.com/mid")]),
        encoding="utf-8")
    (BASE / "2026-08" / "2026-08-16").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-08" / "2026-08-16" / "report.md").write_text(
        report("2026-08-16", [
            ("AI company news", "Story A", "Something happened.", "2026-08-15", "https://example.com/a?utm_source=x"),
            ("AI research papers", "Story B", "Paper dropped.", "2026-08-16", "https://www.example.com/b/"),
        ]), encoding="utf-8")
    (BASE / "2026-08" / "2026-08-17").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-08" / "2026-08-17" / "report.md").write_bytes(b"\xff\xfe\x00corrupt not utf-8 \x9c\xff")
    (BASE / "2026-08" / "2026-08-18").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-08" / "2026-08-18" / "report.md").write_text(
        report("2026-08-18", [("AI infra/hardware", "Today story", "Today.", "2026-08-18", "https://example.com/today")]),
        encoding="utf-8")


def main():
    setup_run1()
    run_build("run1: corrupt prior in last-2 (never abort, warning)", TMP / "probe1" / "out1.json")

    # run2: clean last-2, both scanned, streak on A with newest occurrence
    (BASE / "2026-08" / "2026-08-17" / "report.md").write_text(
        report("2026-08-17", [
            ("AI company news", "Story A", "Still developing.", "2026-08-15", "https://example.com/a?utm_source=x"),
            ("open-source AI", "Story C", "New repo.", "2026-08-17", "https://example.com/c"),
        ]), encoding="utf-8")
    run_build("run2: clean last-2 (08-16, 08-17)", TMP / "probe1" / "out2.json")

    # run3: add a future-dated month folder -> observe inclusion in last-2
    (BASE / "2026-09" / "2026-09-01").mkdir(parents=True, exist_ok=True)
    (BASE / "2026-09" / "2026-09-01" / "report.md").write_text(
        report("2026-09-01", [("AI company news", "Future story", "Future.", "2026-09-01", "https://example.com/future")]),
        encoding="utf-8")
    run_build("run3: future-dated prior folder present", TMP / "probe1" / "out3.json")


if __name__ == "__main__":
    main()
