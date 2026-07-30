import Evtx.Evtx as evtx
import Evtx.Views as e_views
import re, sys
from collections import Counter, defaultdict

path = r"C:\Users\Jonah\DevelopmentTemplate\Events.evtx"

counts = Counter()
by_id = defaultdict(list)
times = []

with evtx.Evtx(path) as log:
    for rec in log.records():
        try:
            xml = rec.xml()
        except Exception:
            continue
        # extract provider + eventid + time
        m_prov = re.search(r'<Provider Name="([^"]+)"', xml)
        m_id = re.search(r'<EventID Qualifier="[^"]*">(\d+)</EventID>|<EventID>(\d+)</EventID>', xml)
        m_time = re.search(r'<TimeCreated SystemTime="([^"]+)"', xml)
        prov = m_prov.group(1) if m_prov else "?"
        eid = (m_id.group(1) or m_id.group(2)) if m_id else "?"
        t = m_time.group(1) if m_time else "?"
        counts[(prov, eid)] += 1
        by_id[(prov, eid)].append((t, xml))
        times.append(t)

print("Total records:", sum(counts.values()))
print("Time range:", min(times) if times else "-", "to", max(times) if times else "-")
print("\n=== Top providers/ids ===")
for (p,e),c in counts.most_common(20):
    print(f"{c:6}  {p}  ID={e}")

# Focus on crash-related events
focus = []
for key, items in by_id.items():
    prov, eid = key
    if any(s in prov.lower() for s in ["whea","bugcheck","kernel-power","volmgr","eventlog","kernel-boot"]) or \
       (prov.lower()=="kernel-power" and eid=="41") or eid in ("16","17","41","6008","1001","161"):
        focus.append((prov, eid, len(items)))

print("\n=== Crash-relevant ===")
for prov,eid,c in sorted(set(focus), key=lambda x:-x[2]):
    print(f"{c:6}  {prov} ID={eid}")