import sys, re
sys.stdout.reconfigure(encoding='utf-8')

README = open('README.md', encoding='utf-8').read()
MAT = open('01-comparison-matrix.md', encoding='utf-8').read()
PAT = open('02-recurring-patterns.md', encoding='utf-8').read()
SRC = open('03-source-library.md', encoding='utf-8').read()

caveat = "These are winners' workflows \u2014 documented by creators who already broke out. Frameworks correlate with virality; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and an audience the reader doesn't have yet."

checks = {
 '1. README has survivorship caveat verbatim (handoff \u00a79)' : caveat in README,
 '2. README dominance math shown for Jenny (0.759)' : "0.5(1.0) + 0.3(0.198) + 0.2(1.0) = 0.5 + 0.0594 + 0.2 = 0.759" in README,
 '3. README has \u201cPick a framework in 5 min\u201d' : "Pick a framework in 5 min" in README,
 '4. README has Acceptance checklist section' : "Acceptance checklist" in README,
 '5. Matrix has platform axis + agnostic/specific tags' : "Platform axis" in MAT and "platform-agnostic" in MAT and "platform-specific" in MAT,
 '6. Matrix covers all 7 closed-vocab retention mechanisms' : all(t in MAT for t in ['curiosity gap','escalating stakes','stakes reset','payoff density','reaction bait','visual resets','open-question stack']),
 '7. Patterns doc has claim-frequency table' : "Claim-frequency table" in PAT,
 '8. Patterns doc has >=15 parallels with Tag: line' : PAT.count("Tag: ") >= 15,
 '9. Source library has full per-source metadata' : all(t in SRC for t in ['FIRST-PARTY','SECOND-HAND','MONETIZED','INDEPENDENT','still-current','2026']),
 '10. Mermaid block present in patterns doc' : "flowchart TD" in PAT,
 '11. All 10 creators in matrix' : all(s in MAT for s in ['Zach King','MrBeast','Dhar Mann','Keith Lee','Airrack','Steven He','Caleb Simpson','Nick DiGiovanni','Sam Sulek','Jenny Hoyos']),
 '12. Matrix has Provenance staleness table (per-creator)' : "Provenance staleness" in MAT,
 '13. Patterns doc has Tactics (single-slug section)' : "single-slug" in PAT.lower() or "saw in 1" in PAT,
 '14. Patterns doc has Diverges section (verified disagreements)' : "Where the dataset diverges" in PAT,
 '15. Source library has Primary Wells + per-creator tables' : "Primary wells" in SRC and "Sources cited in each case study" in SRC,
 '16. No doubled-double-quotes left anywhere' : all('""' not in d for d in [README,MAT,PAT,SRC]),
 '17. No leaked non-English typos' : all(p not in d for p in ['\u4ed8\u8d39','\u8bbf\u8c08','\u56e0\u4e3a','l\u1ee3i','Casey study','Colylie','Behav-Beast','Spectra reflected'] for d in [README,MAT,PAT,SRC]),
}

print("Final acceptance self-audit:")
ok = True
for k,v in checks.items():
    mark = "  [x]" if v else "  [ ] -- FAIL"
    print(f"{mark}  {k}")
    ok = ok and v
print()
print("ALL CHECKS PASS:", ok)