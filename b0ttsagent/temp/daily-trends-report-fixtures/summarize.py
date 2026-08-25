"""Print a compact summary of a routed.json (or inventory.json) for results.md."""
import json
import sys

p = sys.argv[1]
kind = sys.argv[2] if len(sys.argv) > 2 else "routed"
data = json.load(open(p, encoding="utf-8"))

if kind == "routed":
    print("main:")
    for sec, items in data["main"].items():
        for it in items:
            print(f"  {sec}: {it['headline']!r} update={it.get('update')} reason={it.get('reason')}")
    print("still_circulating:", [it["headline"] for it in data["still_circulating"]])
    print("excluded:", [(it["headline"], it.get("reason")) for it in data["excluded"]])
    print("dropped:", [(it["headline"], it.get("reason")) for it in data["dropped"]])
    print("warnings:", data["warnings"])
    print("domain_preference_notes:", data["domain_preference_notes"])
else:  # inventory
    print("reports_scanned:", data["reports_scanned"])
    print("streak_hits url keys:", sorted(data["streak_hits"].keys()))
    print("streak_headline_hits keys:", sorted(data["streak_headline_hits"].keys()))
    print("warnings:", data["warnings"])
