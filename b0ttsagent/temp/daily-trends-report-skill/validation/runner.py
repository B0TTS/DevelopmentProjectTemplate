"""Runner-B style driver: run all 8 eval scenarios against the extracted fixtures
and record exit codes + key lines. Stdlib only."""
import subprocess
from pathlib import Path

FX = Path("b0ttsagent/temp/daily-trends-report-skill/validation")
SCRIPTS = Path(".agents/skills/daily-trends-report/scripts")
TODAY = "2026-08-18"
KEY = ("wrote ", "routed ->", "PASS:", "FAIL:", "ERROR:", "injected", "routed.json byte-identical",
       "inventory identical", "reports_scanned", "streak_hits keys", "today's identity", "prior identity")

def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")

def base(n): return str(FX / f"s{n}" / "AI-Development Trends")
def day(n): return str(FX / f"s{n}" / "AI-Development Trends" / "2026-08" / "2026-08-18")
def inv(n): return ["python", str(SCRIPTS / "build-inventory.py"), "--base", base(n), "--today", TODAY]
def route(n): return ["python", str(SCRIPTS / "route-and-verify.py"), "route", "--folder", day(n), "--today", TODAY]
def verify(n): return ["python", str(SCRIPTS / "route-and-verify.py"), "verify", "--folder", day(n), "--today", TODAY]

def show(tag, rc, out):
    print(f"  [{tag}] exit={rc}")
    for line in out.splitlines():
        ls = line.strip().encode("ascii", "replace").decode("ascii")
        if ls.startswith(KEY):
            print("      " + ls)

overall = True
# Scenarios 1-6
for n in range(1, 7):
    ok = True
    print(f"Scenario {n}")
    for tag, cmd, want in (("inv", inv(n), 0), ("route", route(n), 0), ("verify", verify(n), 0)):
        rc, out = run(cmd)
        show(tag, rc, out)
        ok = ok and rc == want
    print(f"  => {'PASS' if ok else 'FAIL'}")
    overall = overall and ok

# Scenario 7
print("Scenario 7")
ok = True
rc, out = run(inv(7)); show("inv", rc, out); ok &= rc == 0
rc, out = run(route(7)); show("route", rc, out); ok &= rc == 0
rc, out = run(["python", str(FX / "inject-s7.py"), str(FX / "s7" / "AI-Development Trends" / "2026-08" / "2026-08-18" / "routed.json")]); show("inject", rc, out); ok &= rc == 0
rc, out = run(verify(7)); show("verify", rc, out); ok &= rc == 1
print(f"  => {'PASS' if ok else 'FAIL'}")
overall = overall and ok

# Scenario 8 (two runs + snapshot + check)
print("Scenario 8")
ok = True
for tag in ("inv", "route", "verify"):
    cmd = {"inv": inv(8), "route": route(8), "verify": verify(8)}[tag]
    rc, out = run(cmd); show(tag + "(run1)", rc, out); ok &= rc == 0
snap_r = (FX / "s8-routed-run1.json"); snap_i = (FX / "s8-inventory-run1.json")
snap_r.write_bytes((FX / "s8" / "AI-Development Trends" / "2026-08" / "2026-08-18" / "routed.json").read_bytes())
snap_i.write_bytes((FX / "s8" / "AI-Development Trends" / "2026-08" / "2026-08-18" / "inventory.json").read_bytes())
for tag in ("inv", "route", "verify"):
    cmd = {"inv": inv(8), "route": route(8), "verify": verify(8)}[tag]
    rc, out = run(cmd); show(tag + "(run2)", rc, out); ok &= rc == 0
rc, out = run(["python", str(FX / "check-s8.py"), str(FX / "s8" / "AI-Development Trends" / "2026-08" / "2026-08-18"), str(snap_r), str(snap_i)])
show("check-s8", rc, out); ok &= rc == 0
print(f"  => {'PASS' if ok else 'FAIL'}")
overall = overall and ok

print("=" * 70)
print("OVERALL:", "ALL 8 SCENARIOS PASS" if overall else "FAILURES PRESENT")
sys_exit = 0 if overall else 1
raise SystemExit(sys_exit)
