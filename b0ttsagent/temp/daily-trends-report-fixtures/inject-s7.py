"""s7 failure-mode injection: move the streak-hit X from still_circulating into
main[AI trends] with update=false, simulating a routed.json that claims a
streak-hit for main without a passing update test (stale/hand-edited routed
file). This is the state verify's collision gate must catch."""
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
