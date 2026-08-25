"""S2 fixture builder — synthetic day folders for the daily-trends-report scenarios.

Generates, per scenario s1..s8:
    b0ttsagent/temp/daily-trends-report-fixtures/s<N>/AI-Development Trends/
        <YYYY-MM>/<YYYY-MM-DD>/report.md          (prior days)
        2026-08/2026-08-18/                       (today: leaves + report.md)

Deterministic: today = 2026-08-18 (explicit --today everywhere), 7-day window
2026-08-11..2026-08-18. Identities are computed via the skill's own _lib so
fixtures match script expectations exactly.

Idempotent: re-running regenerates everything. Does not touch the real
b0ttsagent/reports/ tree.
"""

import json
import sys
from pathlib import Path

SCRIPTS = Path(r"C:\Users\intel\DevelopmentProjectTemplate\.agents\skills\daily-trends-report\scripts")
sys.path.insert(0, str(SCRIPTS))
import _lib  # noqa: E402

ROOT = Path(r"C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\daily-trends-report-fixtures")
TODAY = "2026-08-18"


def base(n):
    return ROOT / f"s{n}" / "AI-Development Trends"


def day_dir(n, d):
    return base(n) / "2026-08" / d


def report_md(run_date, glance, ai=(), swe=(), prod=(), sc=()):
    lines = [f"# Daily Trends — {run_date}", "", "*Today at a glance*", ""]
    lines += [f"- {g}" for g in glance]
    lines += [""]
    for heading, items in (
        ("## AI trends", ai),
        ("## SWE trends", swe),
        ("## Productivity", prod),
    ):
        lines += [heading, ""]
        lines += [
            "| Domain | Headline | Why it matters | Date | Link |",
            "|---|---|---|---|---|",
        ]
        for it in items:
            lines.append(
                f"| {it['domain']} | {it['headline']} | {it.get('why', '')} | "
                f"{it['date']} | [{it['headline']}]({it['url']}) |"
            )
        lines += [""]
    if sc:
        lines += ["## Still circulating", ""]
        lines += [
            "| Domain | Headline | Why it matters | Date | Link |",
            "|---|---|---|---|---|",
        ]
        for it in sc:
            lines.append(
                f"| {it['domain']} | {it['headline']} |  | "
                f"{it['date']} | [{it['headline']}]({it['url']}) |"
            )
        lines += [""]
    return "\n".join(lines)


def write_report(n, d, *args, **kwargs):
    path = day_dir(n, d) / "report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report_md(d, *args, **kwargs), encoding="utf-8")


def write_leaf(base_path, fname, items):
    if isinstance(base_path, int):
        base_path = base(base_path)
    path = base_path / "2026-08" / TODAY / fname
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"items": items}, indent=2) + "\n", encoding="utf-8")


def leaf(headline, url, published, domain, source_type, why=None, delta=None):
    return {
        "headline": headline,
        "why": why or "",
        "url": url,
        "published_date": published,
        "domain": domain,
        "source_type": source_type,
        "delta_or_null": delta,
    }


def item(headline, url, date, domain, why=""):
    return {"headline": headline, "url": url, "date": date, "domain": domain, "why": why}


QUIET = ["Quiet day."]

# Story X — the shared streak identity.
X = item(
    "Model X hits milestone",
    "https://example.com/model-x",
    "2026-08-14",
    "AI research papers",
    why="Model X passes a training milestone, beating prior baselines.",
)

# ---------------- s1: first-ever run (empty base) ----------------
write_leaf(base(1), "ai.json", [
    leaf("Frontier lab ships open-weights model", "https://example.com/frontier-v3",
         "2026-08-17", "frontier model releases", "blog post",
         why="A new open-weights frontier model lands with permissive licensing, resetting the cost floor for self-hosting."),
])
write_leaf(base(1), "swe.json", [
    leaf("Critical RCE patched in popular build tool", "https://example.com/buildtool-cve",
         "2026-08-16", "security & CVEs", "advisory",
         why="A remote code execution bug in a widely used build tool is fixed; upgrade paths are published."),
])
write_leaf(base(1), "productivity.json", [
    leaf("New terminal autocomplete ships", "https://example.com/term-auto",
         "2026-08-18", "new SWE productivity tools", "release notes",
         why="A terminal autocomplete tool ships with context-aware shell completions and a local-first cache."),
])
write_report(1, TODAY,
             ["AI trends: Frontier lab ships an open-weights model.",
              "SWE trends: A critical build-tool RCE gets patched.",
              "Productivity: A new terminal autocomplete ships."],
             ai=[item("Frontier lab ships open-weights model", "https://example.com/frontier-v3", "2026-08-17",
                      "frontier model releases", why="A new open-weights frontier model lands with permissive licensing, resetting the cost floor for self-hosting.")],
             swe=[item("Critical RCE patched in popular build tool", "https://example.com/buildtool-cve", "2026-08-16",
                       "security & CVEs", why="A remote code execution bug in a widely used build tool is fixed; upgrade paths are published.")],
             prod=[item("New terminal autocomplete ships", "https://example.com/term-auto", "2026-08-18",
                        "new SWE productivity tools", why="A terminal autocomplete tool ships with context-aware shell completions and a local-first cache.")])

# ---------------- s2: identity in BOTH priors, re-proposed, no delta -> Still circulating ----------------
P16 = item("Vector DB company launches serverless tier", "https://example.com/s2-p16", "2026-08-14", "AI company news",
           why="Serverless vector indexing drops the entry cost for small teams.")
P17 = item("Open benchmark leaderboard adds evals", "https://example.com/s2-p17", "2026-08-15", "AI research papers",
           why="New eval categories make leaderboard scores harder to game.")
write_report(2, "2026-08-16",
             ["AI trends: Model X passes a milestone.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X, P16])
write_report(2, "2026-08-17",
             ["AI trends: A new leaderboard eval set.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Model X hits milestone", "https://example.com/model-x?utm_source=hn", "2026-08-14",
                      "AI research papers", why="Model X passes a training milestone, beating prior baselines."), P17])
write_leaf(2, "ai.json", [
    leaf("Model X hits milestone", "https://example.com/model-x",
         "2026-08-14", "AI research papers", "paper", delta=None),
    leaf("New safety-eval framework released", "https://example.com/s2-fresh",
         "2026-08-17", "AI research papers", "paper",
         why="A framework for red-teaming agents ships with a public scoreboard."),
])
write_leaf(2, "swe.json", [])
write_leaf(2, "productivity.json", [])
write_report(2, TODAY,
             ["AI trends: A new safety-eval framework lands.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("New safety-eval framework released", "https://example.com/s2-fresh", "2026-08-17",
                      "AI research papers", why="A framework for red-teaming agents ships with a public scoreboard.")],
             sc=[item("Model X hits milestone", "https://example.com/model-x", "2026-08-14", "AI research papers")])

# ---------------- s3: streak-hit + published >7 days -> excluded ----------------
X_OLD = item("Model X hits milestone", "https://example.com/model-x", "2026-08-06", "AI research papers",
             why="Model X passes a training milestone, beating prior baselines.")
write_report(3, "2026-08-16",
             ["AI trends: Model X milestone.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X_OLD, item("Agent framework reaches 1.0", "https://example.com/s3-p16", "2026-08-05",
                             "dev tools & editors", why="A stable API attracts plugin authors.")])
write_report(3, "2026-08-17",
             ["AI trends: Cloud inference prices cut.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X_OLD, item("Cloud provider cuts inference prices", "https://example.com/s3-p17", "2026-08-06",
                             "cloud & pricing", why="Price cuts ripple into per-call costs for agents.")])
write_leaf(3, "ai.json", [
    leaf("Model X hits milestone", "https://example.com/model-x",
         "2026-08-06", "AI research papers", "paper", delta=None),
    leaf("Training-data licensing dispute settles", "https://example.com/s3-fresh",
         "2026-08-17", "AI policy/regulation", "news",
         why="The settlement sets a precedent for how training corpora are licensed."),
])
write_leaf(3, "swe.json", [])
write_leaf(3, "productivity.json", [])
write_report(3, TODAY,
             ["AI trends: A training-data licensing dispute settles.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Training-data licensing dispute settles", "https://example.com/s3-fresh", "2026-08-17",
                      "AI policy/regulation", why="The settlement sets a precedent for how training corpora are licensed.")])

# ---------------- s4: streak-hit with dated concrete delta -> main, update:true ----------------
X_MID = item("Model X hits milestone", "https://example.com/model-x", "2026-08-13", "AI research papers",
             why="Model X passes a training milestone, beating prior baselines.")
write_report(4, "2026-08-16",
             ["AI trends: Model X milestone.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X_MID, item("Open-source agent runtime gains contributors", "https://example.com/s4-p16", "2026-08-12",
                             "open-source AI", why="Contributor growth signals an ecosystem forming.")])
write_report(4, "2026-08-17",
             ["AI trends: AI chip dev kits ship.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X_MID, item("AI chip startup ships dev kits", "https://example.com/s4-p17", "2026-08-13",
                             "AI infra/hardware", why="Dev kits let teams benchmark locally before cloud spend.")])
write_leaf(4, "ai.json", [
    leaf("Model X hits milestone", "https://example.com/model-x",
         "2026-08-17", "AI research papers", "release notes",
         delta="v2.1 ships 2026-08-17 with 3x benchmark and new API"),
    leaf("Model X hits milestone", "https://example.com/model-x-v2-details",
         "2026-08-17", "AI research papers", "release notes",
         delta="release notes for v2.1: new API, 3x benchmark"),
])
write_leaf(4, "swe.json", [])
write_leaf(4, "productivity.json", [])
write_report(4, TODAY,
             ["AI trends: Model X v2.1 ships with a 3x benchmark.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Model X hits milestone", "https://example.com/model-x", "2026-08-17", "AI research papers",
                      why="v2.1 ships 2026-08-17 with a 3x benchmark and a new API — an update to the earlier milestone."),
                 item("Model X hits milestone", "https://example.com/model-x-v2-details", "2026-08-17", "AI research papers",
                      why="The v2.1 release notes detail the new API and the 3x benchmark run.")])

# ---------------- s5: published >7 days, no delta -> absent everywhere ----------------
write_leaf(5, "ai.json", [
    leaf("Legacy feature announcement", "https://example.com/s5-old",
         "2026-08-05", "AI company news", "news", delta=None),
    leaf("Agents benchmark suite ships", "https://example.com/s5-fresh",
         "2026-08-16", "AI research papers", "paper",
         why="A reproducible agents benchmark with public traces ships its first leaderboard."),
])
write_leaf(5, "swe.json", [])
write_leaf(5, "productivity.json", [])
write_report(5, TODAY,
             ["AI trends: An agents benchmark suite ships.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Agents benchmark suite ships", "https://example.com/s5-fresh", "2026-08-16",
                      "AI research papers", why="A reproducible agents benchmark with public traces ships its first leaderboard.")])

# ---------------- s6: undated finding -> dropped/absent ----------------
write_leaf(6, "ai.json", [
    leaf("Mystery finding with no date", "https://example.com/s6-undated",
         "", "AI research papers", "paper", delta=None),
    leaf("Open-source small model lands", "https://example.com/s6-fresh",
         "2026-08-15", "open-source AI", "blog post",
         why="A small open model with strong per-token efficiency targets laptops."),
])
write_leaf(6, "swe.json", [])
write_leaf(6, "productivity.json", [])
write_report(6, TODAY,
             ["AI trends: An open-source small model lands.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Open-source small model lands", "https://example.com/s6-fresh", "2026-08-15",
                      "open-source AI", why="A small open model with strong per-token efficiency targets laptops.")])

# ---------------- s7: main-section collision, update NOT passed -> verify exits 1 ----------------
write_report(7, "2026-08-17",
             ["AI trends: Model X milestone.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[X_MID, item("Dev conference schedules agent keynote", "https://example.com/s7-p17", "2026-08-12",
                             "AI company news", why="Agent tooling gets main-stage billing at a major dev conference.")])
write_leaf(7, "ai.json", [
    leaf("Model X hits milestone", "https://example.com/model-x",
         "2026-08-13", "AI research papers", "paper", delta=None),
])
write_leaf(7, "swe.json", [])
write_leaf(7, "productivity.json", [])
# Writer-error fixture: the writer put the streak-hit back into a main section.
write_report(7, TODAY,
             ["AI trends: Model X milestone.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Model X hits milestone", "https://example.com/model-x", "2026-08-13", "AI research papers",
                      why="Model X passes a training milestone, beating prior baselines.")])

# ---------------- s8: same-day rerun ----------------
write_report(8, "2026-08-17",
             ["AI trends: A recurring AI company story.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Recurring story from yesterday", "https://example.com/s8-prior", "2026-08-12",
                      "AI company news", why="A company story that ran yesterday.")])
write_leaf(8, "ai.json", [
    leaf("Today's fresh story", "https://example.com/s8-today",
         "2026-08-18", "AI company news", "news",
         why="A fresh story published today."),
])
write_leaf(8, "swe.json", [])
write_leaf(8, "productivity.json", [])
write_report(8, TODAY,
             ["AI trends: Today's fresh story.", "SWE trends: Quiet day.", "Productivity: Quiet day."],
             ai=[item("Today's fresh story", "https://example.com/s8-today", "2026-08-18", "AI company news",
                      why="A fresh story published today.")])

print("fixtures written under", ROOT)
for n in range(1, 9):
    print(f"  s{n}: {base(n)}")
print("today's window:", _lib.today_iso() and "explicit --today 2026-08-18 used in all runs")
