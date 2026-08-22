# Eval fixtures — daily-trends-report

Runnable scenario suite for the skill's deterministic layer (the two scripts). Every scenario is reproducible from this doc alone: one self-contained fixture generator, two tiny helper scripts, and the commands quoted per scenario. Together they prove success criteria 1–7 and 10 of the skill's contract; criteria 8–9 are instruction checks (see the split at the end). Routing explanations behind each expected output live in [routing-rules.md](routing-rules.md).

## Contents

- [Conventions](#conventions)
- [Mandated minimums](#mandated-minimums)
- [Fixture generator](#fixture-generator)
- [Scenario 1: first-ever run, MANDATED](#scenario-1-first-ever-run-mandated)
- [Scenario 2: identity in both priors, no delta, MANDATED](#scenario-2-identity-in-both-priors-no-delta-mandated)
- [Scenario 3: streak-hit older than 7 days](#scenario-3-streak-hit-older-than-7-days)
- [Scenario 4: streak-hit with dated delta returns to main](#scenario-4-streak-hit-with-dated-delta-returns-to-main)
- [Scenario 5: over-7-day item, no delta, MANDATED](#scenario-5-over-7-day-item-no-delta-mandated)
- [Scenario 6: undated finding, MANDATED](#scenario-6-undated-finding-mandated)
- [Scenario 7: main-section collision, MANDATED](#scenario-7-main-section-collision-mandated)
- [Scenario 8: same-day rerun, criterion 10](#scenario-8-same-day-rerun-criterion-10)
- [Criteria 8–10: script-checkable vs instruction checks](#criteria-810-script-checkable-vs-instruction-checks)
- [Reproduction log](#reproduction-log)

## Conventions

- **Fixture root** `<fx>` = `b0ttsagent/temp/daily-trends-report-eval/` — a throwaway root inside the repo's temp dumping ground. Delete it at any time. It is synthetic and never touches the real reports tree (`b0ttsagent/reports/`).
- **Determinism.** Every command passes `--today 2026-08-18`; the 7-day window is therefore 2026-08-11..2026-08-18. The scripts' canonical clock is the fixed UTC−10 offset; the explicit `--today` makes the fixtures independent of the wall clock.
- **Shell.** Commands are shown for PowerShell (the repo shell). On bash, the same quoted `"$fx/..."` forms work; the variable assignment is `fx="b0ttsagent/temp/daily-trends-report-eval"`. Check each exit code with `$LASTEXITCODE` (PowerShell) / `$?` (bash).
- **Exit codes.** 0 = success for all three commands except where a scenario expects a verify FAIL (exit 1). A malformed `--today` exits 2. Warnings never affect the exit code.
- **Expected WARN lines.** Every fixture report is intentionally compact, so every verify emits exactly one warning: `WARN: word budget <n> outside ~400-700 (excluding Still circulating)`. This is a nudge, not a gate. The glance label + exactly-3-bullets check is satisfied in every fixture, so no glance warning appears.
- **The three commands** every scenario runs (substitute the scenario number for `<N>`; `$fx` as defined above):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s<N>/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s<N>/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s<N>/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

In expected outputs below, `...` stands for the fixture-root path prefix printed by each command (its exact form depends on your working directory; the counts and verdict lines are the contract).

## Mandated minimums

Five fixtures are the contract-mandated minimums (the skill's context, authoring order): a run must prove these five behaviors before shipping. They map to scenarios 1, 2, 5, 6, 7 — marked **MANDATED** in their headings and bold in the table. Scenarios 3, 4, and 8 are extra coverage (routing-table rows and the rerun criterion).

| Mandated fixture | Scenario |
|---|---|
| First-ever run (empty folder) → day folder + `report.md`, 3 sections, required fields | [Scenario 1](#scenario-1-first-ever-run-mandated) |
| Same identity in last 2 reports, no dated delta → no main section | [Scenario 2](#scenario-2-identity-in-both-priors-no-delta-mandated) |
| >7-day item, no delta → absent everywhere | [Scenario 5](#scenario-5-over-7-day-item-no-delta-mandated) |
| Undated finding → absent | [Scenario 6](#scenario-6-undated-finding-mandated) |
| Main-section identity collision with a last-2 report → verify fails | [Scenario 7](#scenario-7-main-section-collision-mandated) |

## Fixture generator

Save the following block as `<fx>/make-fixtures.py` (the file is stdlib-only; it deliberately does not import the skill's `_lib` — the scripts under test compute identity keys themselves), then run it from the repo root:

```powershell
python b0ttsagent/temp/daily-trends-report-eval/make-fixtures.py
```

It is idempotent: re-running regenerates all eight scenario bases. It writes prior-day `report.md` files, today's leaf JSONs, and today's `report.md` (standing in for the writer's output) per scenario.

```python
"""Eval fixture builder for the daily-trends-report skill. Stdlib only.

Writes, under b0ttsagent/temp/daily-trends-report-eval/:

    s<N>/AI-Development Trends/
        2026-08/<prior-day>/report.md      (history, per scenario)
        2026-08/2026-08-18/                (today: leaf JSONs + report.md)

today = 2026-08-18 in every scenario (every run passes --today 2026-08-18);
7-day window = 2026-08-11..2026-08-18. Idempotent. Never touches the real
reports tree. Run from the repo root:  python make-fixtures.py
"""

import json
from pathlib import Path

ROOT = Path("b0ttsagent/temp/daily-trends-report-eval")
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
            "| Headline | Date | Link |",
            "|---|---|---|",
        ]
        for it in sc:
            lines.append(
                f"| {it['headline']} | {it['date']} | [{it['headline']}]({it['url']}) |"
            )
        lines += [""]
    return "\n".join(lines)


def write_report(n, d, *args, **kwargs):
    path = day_dir(n, d) / "report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report_md(d, *args, **kwargs), encoding="utf-8")


def write_leaf(n, fname, items):
    path = day_dir(n, TODAY) / fname
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

# Shared streak identity X.
X = item(
    "Model X hits milestone",
    "https://example.com/model-x",
    "2026-08-14",
    "AI research papers",
    why="Model X passes a training milestone, beating prior baselines.",
)

# ---- s1: first-ever run (empty base) ----
write_leaf(1, "ai.json", [
    leaf("Frontier lab ships open-weights model", "https://example.com/frontier-v3",
         "2026-08-17", "frontier model releases", "blog post",
         why="A new open-weights frontier model lands with permissive licensing, resetting the cost floor for self-hosting."),
])
write_leaf(1, "swe.json", [
    leaf("Critical RCE patched in popular build tool", "https://example.com/buildtool-cve",
         "2026-08-16", "security & CVEs", "advisory",
         why="A remote code execution bug in a widely used build tool is fixed; upgrade paths are published."),
])
write_leaf(1, "productivity.json", [
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

# ---- s2: identity in BOTH priors, re-proposed, no delta -> Still circulating ----
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

# ---- s3: streak-hit + published >7 days -> excluded ----
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

# ---- s4: streak-hit with dated concrete delta -> main, update:true ----
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

# ---- s5: published >7 days, no delta -> absent everywhere ----
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

# ---- s6: undated finding -> dropped/absent ----
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

# ---- s7: main-section collision, update NOT passed -> verify exits 1 ----
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

# ---- s8: same-day rerun ----
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
```

## Scenario 1: first-ever run, MANDATED

Proves criterion 1: an empty base → today's day folder with a `report.md` that has 3 main sections and every item carrying headline, why-it-matters, link, and date; padding is never forced.

**Setup.** `make-fixtures.py` already wrote it: s1 has no prior days; today's folder holds one candidate per leaf and a writer-written `report.md` with 3 main sections.

**Run** (substitute `s1` for `<N>` in the three commands above):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s1/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s1/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s1/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `wrote ...inventory.json: scanned 0 prior report(s), 0 url-key streak hits, 0 headline-key hits, 0 warning(s)`
- route, exit 0: `routed -> .../routed.json | main: AI trends 1, SWE trends 1, Productivity 1 | still_circulating: 0 | excluded: 0 | dropped: 0`
- verify, exit 0: `WARN: word budget 192 outside ~400-700 (excluding Still circulating)` then `PASS: gates clean, 1 warning(s)`

**Criterion check.** The day folder exists with `report.md` + `inventory.json` + `routed.json`; verify's PASS proves the 3 main headings, the glance block, and required item fields all hold, and route's `main: 1/1/1` proves every fresh candidate landed in its section.

## Scenario 2: identity in both priors, no delta, MANDATED

Proves criteria 2 and 3: an identity in both of the last 2 reports, re-proposed with no dated delta, appears in no main section — it lands in Still circulating only because it is re-proposed and ≤7 days old.

**Setup.** s2's priors `2026-08-16` and `2026-08-17` both carry X ("Model X hits milestone", `https://example.com/model-x`); the 08-17 copy is written with `?utm_source=hn` to exercise URL normalization end-to-end. Today's `ai.json` re-proposes X (published 2026-08-14, `delta_or_null: null`) plus one fresh item. Today's `report.md` holds the fresh item in main and X in Still circulating.

**Run** (substitute `s2`):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s2/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s2/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s2/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `wrote ...inventory.json: scanned 2 prior report(s), 3 url-key streak hits, 3 headline-key hits, 0 warning(s)`
- route, exit 0: `routed -> .../routed.json | main: AI trends 1, SWE trends 0, Productivity 0 | still_circulating: 1 | excluded: 0 | dropped: 0`
- verify, exit 0: `WARN: word budget 104 outside ~400-700 (excluding Still circulating)` then `PASS: gates clean, 1 warning(s)`

**Criterion check.** In `routed.json`, `still_circulating` contains the item with identity `https://example.com/model-x` (reason `streak-hit, re-proposed, no passing update`) and `main["AI trends"]` contains only the fresh item. `inventory.json`'s `streak_hits` key for the 08-17 prior is the normalized `https://example.com/model-x` — the tracking param was stripped.

## Scenario 3: streak-hit older than 7 days

Proves the routing-table row "Streak-hit + published >7d → Excluded": the streak alone does not demote to Still circulating when the item is also too old.

**Setup.** s3's priors carry X dated 2026-08-06 (outside the window). Today re-proposes X with the same old date and no delta, plus one fresh item.

**Run** (substitute `s3`):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s3/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s3/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s3/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `scanned 2 prior report(s), 3 url-key streak hits, 3 headline-key hits, 0 warning(s)`
- route, exit 0: `main: AI trends 1, SWE trends 0, Productivity 0 | still_circulating: 0 | excluded: 1 | dropped: 0`
- verify, exit 0: `PASS: gates clean, 1 warning(s)` (word budget 104)

**Criterion check.** `routed.json`'s `excluded` contains X with reason `older than 7 days and streak-hit`; X is absent from `main` and `still_circulating`; today's `report.md` contains no X, which verify confirms by passing.

## Scenario 4: streak-hit with dated delta returns to main

Proves criterion 4: a streak-hit identity with a dated, concrete delta returns to a main section flagged as an update, via both update-test branches (newer date on the same URL, and new URL on the same headline).

**Setup.** s4's priors carry X dated 2026-08-13. Today's `ai.json` proposes two updates: X on the same URL with `published_date` 2026-08-17 and a concrete delta, and X's headline on a new URL (`model-x-v2-details`) with the same newer date and delta (exercising the headline-identity fallback).

**Run** (substitute `s4`):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s4/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s4/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s4/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `scanned 2 prior report(s), 3 url-key streak hits, 3 headline-key hits, 0 warning(s)`
- route, exit 0: `main: AI trends 2, SWE trends 0, Productivity 0 | still_circulating: 0 | excluded: 0 | dropped: 0`
- verify, exit 0: `PASS: gates clean, 1 warning(s)` (word budget 146)

**Criterion check.** Both `main["AI trends"]` items in `routed.json` carry `"update": true` (reason `update test passed`); verify passes despite the streak because the collision check exempts `routed_update_ids`. This is the positive control for Scenario 7's failure.

## Scenario 5: over-7-day item, no delta, MANDATED

Proves criterion 5: an item published >7 days ago with no passing update appears nowhere in the report.

**Setup.** s5 has an empty base (no streak involved). Today's `ai.json`: "Legacy feature announcement" published 2026-08-05, no delta, plus one fresh item.

**Run** (substitute `s5`):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s5/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s5/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s5/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `scanned 0 prior report(s), 0 url-key streak hits, 0 headline-key hits, 0 warning(s)`
- route, exit 0: `main: AI trends 1, SWE trends 0, Productivity 0 | still_circulating: 0 | excluded: 1 | dropped: 0`
- verify, exit 0: `PASS: gates clean, 1 warning(s)` (word budget 105)

**Criterion check.** `routed.json`'s `excluded` holds the legacy item with reason `older than 7 days`; today's `report.md` has no legacy item, and verify's PASS proves it appears nowhere (main and Still circulating are both checked against `routed.json`).

## Scenario 6: undated finding, MANDATED

Proves criterion 6: a finding without a verifiable published date is dropped and absent from the report.

**Setup.** s6 has an empty base. Today's `ai.json`: "Mystery finding with no date" with `published_date: ""`, plus one fresh item.

**Run** (substitute `s6`):

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s6/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s6/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s6/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

**Expected:**

- inventory, exit 0: `scanned 0 prior report(s), 0 url-key streak hits, 0 headline-key hits, 0 warning(s)`
- route, exit 0: `main: AI trends 1, SWE trends 0, Productivity 0 | still_circulating: 0 | excluded: 0 | dropped: 1`
- verify, exit 0: `PASS: gates clean, 1 warning(s)` (word budget 103)

**Criterion check.** `routed.json`'s `dropped` holds the mystery item with reason `no verifiable YYYY-MM-DD published date`; the item is absent from `main`, `still_circulating`, and the written report, and verify passes.

## Scenario 7: main-section collision, MANDATED

Proves criterion 7: when a report places a streak-hit identity in a main section without a passing update test, verify exits 1 and names the prior file.

**Setup.** s7's prior `2026-08-17` carries X dated 2026-08-13. Today's `ai.json` re-proposes X with no delta. Today's `report.md` is the writer-error fixture: X sits in `## AI trends` dated 2026-08-13 (in window, so the collision is the only gate violation).

**Run.** Save the following block as `<fx>/inject-s7.py`, then run the four commands:

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s7/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s7/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python b0ttsagent/temp/daily-trends-report-eval/inject-s7.py "$fx/s7/AI-Development Trends/2026-08/2026-08-18/routed.json"
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s7/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
```

```python
"""s7 failure-mode injection: move the streak-hit X from still_circulating into
main["AI trends"] with update=false — a routed.json that claims a streak-hit
for main without a passing update test (stale or hand-edited routed file).
This is the state verify's collision gate must catch."""
import json
import sys

p = sys.argv[1]
r = json.load(open(p, encoding="utf-8"))
target = "https://example.com/model-x"
moved = [it for it in r["still_circulating"] if it.get("identity") == target]
assert moved, "X not found in still_circulating"
for it in moved:
    it2 = dict(it)
    it2.pop("reason", None)
    it2["update"] = False
    r["main"]["AI trends"].append(it2)
r["still_circulating"] = [it for it in r["still_circulating"] if it.get("identity") != target]
open(p, "w", encoding="utf-8").write(json.dumps(r, indent=2) + "\n")
print("injected", len(moved), "item(s) into main[AI trends] with update=false")
```

**Expected:**

- inventory, exit 0: `wrote ...inventory.json: scanned 1 prior report(s), 2 url-key streak hits, 2 headline-key hits, 0 warning(s)`
- route, exit 0 (honest routing): `main: AI trends 0, SWE trends 0, Productivity 0 | still_circulating: 1 | excluded: 0 | dropped: 0`
- inject, exit 0: `injected 1 item(s) into main[AI trends] with update=false`
- verify, **exit 1**:
  ```
  ERROR: AI trends: streak collision — 'Model X hits milestone' appeared in 2026-08/2026-08-17/report.md and the update test did not pass
  WARN: word budget 101 outside ~400-700 (excluding Still circulating)
  FAIL: 1 gate violation(s), 1 warning(s)
  ```

**Criterion check.** Verify exits 1 with a collision error naming the prior file `2026-08/2026-08-17/report.md` — the deterministic gate that a streak-hit without a passing update never sits in a main section. Positive control: Scenario 4's verify passes with the same streak identity because `update: true` exempts it.

## Scenario 8: same-day rerun, criterion 10

Proves the script half of criterion 10: a same-day rerun overwrites today's outputs in place, the inventory ignores today's folder, and the second run routes identically.

**Setup.** s8's prior `2026-08-17` carries "Recurring story from yesterday" (`https://example.com/s8-prior`). Today's folder already holds a first-run `report.md` with fresh item T (`https://example.com/s8-today`, dated 2026-08-18) and `ai.json` = [T].

**Run.** Run the three commands (substitute `s8`), snapshot the outputs, run the three commands again, then compare. Save the check block as `<fx>/check-s8.py` first:

```powershell
python .agents/skills/daily-trends-report/scripts/build-inventory.py --base "$fx/s8/AI-Development Trends" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py route --folder "$fx/s8/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
python .agents/skills/daily-trends-report/scripts/route-and-verify.py verify --folder "$fx/s8/AI-Development Trends/2026-08/2026-08-18" --today 2026-08-18
Copy-Item "$fx/s8/AI-Development Trends/2026-08/2026-08-18/routed.json" "$fx/s8-routed-run1.json"
Copy-Item "$fx/s8/AI-Development Trends/2026-08/2026-08-18/inventory.json" "$fx/s8-inventory-run1.json"
# ... run the same three commands again ...
python b0ttsagent/temp/daily-trends-report-eval/check-s8.py "$fx/s8/AI-Development Trends/2026-08/2026-08-18" "$fx/s8-routed-run1.json" "$fx/s8-inventory-run1.json"
```

```python
"""s8 rerun determinism check: compare run-1 snapshots against the live
run-2 outputs in the day folder."""
import json
import sys

day, routed_snap, inv_snap = sys.argv[1], sys.argv[2], sys.argv[3]

r1 = open(routed_snap, "rb").read()
r2 = open(day + "/routed.json", "rb").read()
print("routed.json byte-identical:", r1 == r2)

i1 = json.load(open(inv_snap, encoding="utf-8"))
i2 = json.load(open(day + "/inventory.json", encoding="utf-8"))
g1, g2 = i1.pop("generated_at"), i2.pop("generated_at")
print("inventory identical modulo generated_at:", i1 == i2)

print("reports_scanned:", i2["reports_scanned"])
print("streak_hits keys:", sorted(i2["streak_hits"].keys()))
print("today's identity in streak_hits (must be False):",
      "https://example.com/s8-today" in i2["streak_hits"])
print("prior identity in streak_hits (must be True):",
      "https://example.com/s8-prior" in i2["streak_hits"])
```

**Expected.** Both runs, all three commands exit 0:

- inventory: `wrote ...inventory.json: scanned 1 prior report(s), 1 url-key streak hits, 1 headline-key hits, 0 warning(s)`
- route: `main: AI trends 1, SWE trends 0, Productivity 0 | still_circulating: 0 | excluded: 0 | dropped: 0`
- verify: `PASS: gates clean, 1 warning(s)` (word budget 95)

The check prints:

```
routed.json byte-identical: True
inventory identical modulo generated_at: True
reports_scanned: ['2026-08/2026-08-17/report.md']
streak_hits keys: ['https://example.com/s8-prior']
today's identity in streak_hits (must be False): False
prior identity in streak_hits (must be True): True
```

**Criterion check.** The second run's live files are identical to the run-1 snapshots (overwrite in place, no drift); `reports_scanned` names only the 08-17 prior (today's folder ignored even though today's `report.md` exists with its own identity); today's identity never entered history. The "index.md still has one row for the day" half is an instruction check — see the split table below.

## Criteria 8–10: script-checkable vs instruction checks

| Criterion | Script-checkable (fixture evidence) | SKILL.md instruction check (manual) |
|---|---|---|
| 8 — index.md row + chat pointer | none scripted — index upsert and the chat pointer are orchestrator steps; the deterministic layer is the two scripts | index.md created-if-missing with the newest row on top; same-day rerun upserts the row, never appends a duplicate; chat = path + the 3 glance bullets + "N items demoted" when Still circulating is non-empty |
| 9 — glance readable <1 min, file in 15 min | partial — the glance label + exactly-3-bullets check and the word budget are verify **warnings** (exit 0); satisfied in every fixture above | reading-time checks are human; the markdown-doc-designs quality bar applies to the writer's output |
| 10 — same-day rerun | fully script-checkable: Scenario 8 (overwrite + today's-folder exclusion + identical routing) | the "index.md still has one row for the day" half rides on the criterion-8 instruction |

## Reproduction log

2026-08-18 (S4): this doc was written, then its three fenced Python blocks (generator + `inject-s7.py` + `check-s8.py`) were extracted programmatically from this page and saved to `<fx>/`, and **all 8 scenarios were re-run end-to-end from the commands quoted above** to prove the doc alone suffices — no session memory, no S2 artifacts. Recorded results:

- Scenarios 1–6, 8: every inventory/route/verify command exited 0 and printed exactly the expected lines above (same counts, same word-budget warnings — 192 / 104 / 104 / 146 / 105 / 103 / 95).
- Scenario 7: inventory 0, route 0, inject 0, verify **1** — the collision ERROR named `2026-08/2026-08-17/report.md` exactly as quoted.
- Scenario 8: both runs all exit 0; `check-s8.py` printed all five expected lines with `True`/`False` as quoted.

No discrepancies between this doc's expected outputs and the scripts' actual behavior.
