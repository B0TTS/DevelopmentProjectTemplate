"""s8 rerun determinism check: compare run1 vs run2 outputs.

Checks:
1. routed.json byte-identical across runs (rerun produces identical routing).
2. inventory.json identical modulo the generated_at timestamp.
3. inventory scanned only the prior folder (today's folder ignored, even
   though today's report.md exists with identity s8-today).
4. streak_hits contains the prior identity but NOT today's.
"""
import json
import sys

fx = r"C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\daily-trends-report-fixtures"
logs = fx + r"\logs"
r1 = open(logs + r"\s8-run1-routed.json", "rb").read()
r2 = open(logs + r"\s8-run2-routed.json", "rb").read()
print("routed.json byte-identical:", r1 == r2)

i1 = json.load(open(logs + r"\s8-run1-inventory.json", encoding="utf-8"))
i2 = json.load(open(logs + r"\s8-run2-inventory.json", encoding="utf-8"))
g1, g2 = i1.pop("generated_at"), i2.pop("generated_at")
print("inventory identical modulo generated_at:", i1 == i2)
print("generated_at run1:", g1)
print("generated_at run2:", g2)

print("reports_scanned:", i1["reports_scanned"])
print("streak_hits keys:", sorted(i1["streak_hits"].keys()))
print("today's identity in streak_hits (must be False):",
      "https://example.com/s8-today" in i1["streak_hits"])
print("prior identity in streak_hits (must be True):",
      "https://example.com/s8-prior" in i1["streak_hits"])
