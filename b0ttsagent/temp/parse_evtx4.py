import Evtx.Evtx as evtx
import re
from collections import Counter

path = r"C:\Users\Jonah\DevelopmentTemplate\Events.evtx"

kp41 = []
volmgr161 = []
whea17 = []
boot6008 = []

with evtx.Evtx(path) as log:
    for rec in log.records():
        try:
            xml = rec.xml()
        except Exception:
            continue
        m_prov = re.search(r'<Provider Name="([^"]+)"', xml)
        m_id = re.search(r'<EventID[^>]*>(\d+)</EventID>', xml)
        m_time = re.search(r'<TimeCreated SystemTime="([^"]+)"', xml)
        if not (m_prov and m_id): continue
        prov = m_prov.group(1); eid = m_id.group(1); t = m_time.group(1) if m_time else "?"
        if prov=="Microsoft-Windows-Kernel-Power" and eid=="41":
            kp41.append((t,xml))
        elif prov=="volmgr" and eid=="161":
            volmgr161.append((t,xml))
        elif prov=="Microsoft-Windows-WHEA-Logger" and eid=="17":
            whea17.append((t,xml))
        elif prov=="EventLog" and eid=="6008":
            boot6008.append((t,xml))

def strip(x): return re.sub(r'\s+',' ',x).strip()

print(f"=== Kernel-Power 41 ({len(kp41)}) ===")
for t,xml in kp41:
    bug = re.search(r'<BugcheckCode>([^<]+)</BugcheckCode>', xml)
    bc1 = re.search(r'<BugcheckParameter1[^>]*>([^<]+)</BugcheckParameter1>', xml)
    bc2 = re.search(r'<BugcheckParameter2[^>]*>([^<]+)</BugcheckParameter2>', xml)
    bc3 = re.search(r'<BugcheckParameter3[^>]*>([^<]+)</BugcheckParameter3>', xml)
    bc4 = re.search(r'<BugcheckParameter4[^>]*>([^<]+)</BugcheckParameter4>', xml)
    print(t, "| bug=",bug.group(1) if bug else "?",
          "p1=",bc1.group(1) if bc1 else "","p2=",bc2.group(1) if bc2 else "",
          "p3=",bc3.group(1) if bc3 else "","p4=",bc4.group(1) if bc4 else "")

print(f"\n=== EventLog 6008 ({len(boot6008)}) ===")
for t,xml in boot6008[:3]:
    print(t, "|", strip(xml[xml.find('<EventData'):xml.find('</EventData')])[:250])

print(f"\n=== volmgr 161 ({len(volmgr161)}) ===")
for t,xml in volmgr161[:2]:
    print(t,"|",strip(xml[xml.find('<EventData'):xml.find('</EventData')])[:200])

# WHEA-17 device signature: count distinct error type / device
print(f"\n=== WHEA-17 first/last timestamps ({len(whea17)}) ===")
print("first:", whea17[0][0] if whea17 else "-")
print("last:", whea17[-1][0] if whea17 else "-")
print("\n-- sample WHEA-17 --")
print(whea17[0][1][:1500] if whea17 else "")