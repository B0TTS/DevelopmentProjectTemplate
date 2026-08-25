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

