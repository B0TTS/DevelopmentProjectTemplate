import Evtx.Evtx as evtx
import re
from collections import Counter, defaultdict

path = r"C:\Users\Jonah\DevelopmentTemplate\Events.evtx"
counts = Counter()
samples = defaultdict(list)
times = []

with evtx.Evtx(path) as log:
    for rec in log.records():
        try:
            xml = rec.xml()
        except Exception:
            continue
        m_prov = re.search(r'<Provider Name="([^"]+)"', xml)
        m_id = re.search(r'<EventID[^>]*>(\d+)</EventID>', xml)
        m_time = re.search(r'<TimeCreated SystemTime="([^"]+)"', xml)
        m_lvl = re.search(r'<Level>(\d+)</Level>', xml)
        prov = m_prov.group(1) if m_prov else "?"
        eid = m_id.group(1) if m_id else "?"
        lvl = m_lvl.group(1) if m_lvl else "?"
        t = m_time.group(1) if m_time else "?"
        counts[(prov, eid, lvl)] += 1
        if len(samples[(prov, eid)]) < 2:
            samples[(prov, eid)].append((t, xml))
        times.append(t)

print("Total:", sum(counts.values()), "Range:", min(times), "->", max(times))
print("\n=== Top (provider, id, level) ===")
for (p,e,l),c in counts.most_common(30):
    print(f"{c:6}  L{l}  {p} ID={e}")

print("\n=== WHEA breakdown ===")
whea_rows = [(p,e,l,c) for (p,e,l),c in counts.items() if "WHEA" in p]
for p,e,l,c in sorted(whea_rows, key=lambda r:-r[3]):
    print(f"{c:6}  L{l}  {e}")

print("\n=== Kernel-Power / Kernel-Boot / EventLog / volmgr ===")
for key in counts:
    p,e,l = key
    if p in ("Microsoft-Windows-Kernel-Power","Microsoft-Windows-Kernel-Boot","EventLog","volmgr","Microsoft-Windows-Kernel-General") and counts[key]>=2:
        print(f"{counts[key]:6}  L{l}  {p} ID={e}")