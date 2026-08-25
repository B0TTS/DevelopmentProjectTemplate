# Wave spec — 2026-08-18

Goal: fill the day folder with routed leaf candidates for today's report
Day folder: C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18
Inventory: C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\inventory.json
Anchors: C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\anchors.md

## Roster
3 leaves of `b0tts-researcher` (AI / SWE / Productivity), fanned out in ONE message.
Wave report: append a `## Wave 1 report` section to this file when done.

## Per-leaf task prompt
Give each leaf the following verbatim, with {{SECTION}}, {{HINTS}}, {{OUT}} substituted:

---
Research the {{SECTION}} section of today's daily trends report.

Output file: {{OUT}}
Anchors (discovery seeds only, never report items): C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\anchors.md
Inventory (prior identities): C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\inventory.json

Budget: at most 8 web searches and 5 full page-reads. When the budget is
spent, stop and write what you have.

Rules:
- Every item needs a dated primary source: published/updated YYYY-MM-DD, or
  HN submission time only when the cited item is that post. No date → drop
  the item.
- Read a page before citing it. Never invent dates, numbers, or links.
- Coverage domains for {{SECTION}}: {{HINTS}}. Hints, not a quota.
- An HN thread or GitHub trending row is never a report item.
- Do not re-propose any identity in inventory.json unless you have a
  concrete dated delta (version, number, decision, CVE id, ship date). With
  a delta: set delta_or_null. Without one: skip the item.
- Item schema: headline, why, url, published_date, domain, source_type,
  delta_or_null.

Write your complete findings to {{OUT}} as {"items": [...]} (an empty items
list is valid). Return ≤250 words: status, path, item count, anomalies.
---

## Output paths
- AI trends    → C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\ai.json
- SWE trends   → C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\swe.json
- Productivity → C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\reports\daily-reports\AI-Development Trends\2026-08\2026-08-18\productivity.json

## QA checklist
The lead QA checklist in references/wave-spec.md, applied to the disk outputs.

## Completion criteria
- All 3 files exist and pass QA (or the gaps are recorded in the wave report).
- Wave report appended to this file.
