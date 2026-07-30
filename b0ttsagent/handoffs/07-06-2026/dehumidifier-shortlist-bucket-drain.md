# Dehumidifier Shortlist + Bucket-Drain Plan (Handoff)

**Purpose:** Give a fresh AI agent the context to (a) continue helping the user shop for a dehumidifier within ~$200, and (b) authorize candidate units the user brings in against a shopping checklist. Supersedes `purifier-evaluation-context.md` (which had locked the Midea Cube 20-pint as a "do not relitigate" decision — that decision is now reopened; this doc replaces it).

**Status:** Dehumidifier research complete. User is now actively shopping and will send candidate units for a go/no-go check. Air purifier purchase is deferred (criteria preserved at bottom for later use).

---

## User context (condensed — read this first)

- **Location & climate:** Central Oahu, Hawaii, ~1,366 ft elevation. Tropical, very humid. Avg RH ~76% (range 73-79%); **nighttime RH rises to 80-90%+** (danger window for mold). Dew point 63-69°F; September is the worst month. 52" rain/yr, 239 rainy days.
- **Electricity:** ~$0.33-0.40/kWh (highest in US) — the dehumidifier is the highest-wattage device in the remediation plan, so wattage matters a lot.
- **Room:** ~100-200 sq ft bedroom, sealed-room problem (poor airflow with door+window closed; excellent when both open). Carpet has black mold (deep, surface-treated; padding likely still a wet reservoir). Lots of blankets/comforters (dust + moisture reservoirs).
- **Health:** Chronic mold exposure → fatigue, depression, brain fog, cognitive impairment. Environment remediation expected to resolve symptoms over weeks-to-months. If symptoms persist after RH is sustained <50% and mold removed, consider a CIRS workup with a doctor.
- **Ventilation/AC:** AC on during day (dehumidifies partially); AC off at night → no dehumidification, ambient RH 80-90%+. The dehumidifier earns its keep overnight. No longer smoking in the room (smokes outside/bathroom now).
- **Decisions locked (root-cause fixes):** Hygrometer $10 (target RH 48%, 2% buffer below mold's 50% growth threshold). Source control: clean carpet mold (bleach/Concrobium; possibly replace the section), hot-wash blankets, declutter. Ventilation: crack window + cheap box fan for fresh air exchange — full schedule in `b0ttsagent/temp/room-airing-schedule.md` (reference, not duplicated here).
- **The dehumidifier is the root-cause fix** (stops mold growth by holding RH <50%). The purifier is only the "polish" layer (cleans up airborne spores) and is deferred.

---

## The key research insight (this shapes everything)

**For manual draining, tank size beats pint rating.** User initially assumed "high-pint = fewer empties." That's true for a drain-hose setup but **backwards for manual draining**: pint rating = how much water it *pulls*; tank size = how often you *empty*. Standard dehumidifiers (most 30- and 50-pint units) assume a drain hose, so they ship with tiny 0.4-1.6-gal tanks → a 50-pint into a 1.6-gal tank = ~4 empties/day at the user's humidity, failing the user's 2x/day limit. The **cube design** (Midea Cube / Comfort-Aire BCD series) is the only form factor pairing a real compressor with a 3-4 gallon tank.

**Then the user pivoted to a hose+bucket setup** (gravity drain into a bucket, emptied daily), which unlocks every standard dehumidifier by making the small-tank problem disappear. This is now the active plan — see Bucket plan below.

---

## Researched shortlist (all within budget)

**Tier 1 — cube design (big internal tank, also have a gravity-drain port for bucket hybrid):**

| Model | Pints/day | Tank | Watts | Noise | ES | Price | Notes |
|---|---|---|---|---|---|---|---|
| **Comfort-Aire BCD-35A** *(top rec)* | 35 | 4.2 gal | 345 | 42.5-45 dB | Yes | $199.99-224.99 | 35-pint cube clone of Midea 35; quieter + cheaper than Midea; recovers fast after airing/cleaning; likely same OEM platform |
| Midea Cube 35 (MAD35S1QWT) | 35 | 4.2-4.4 gal | ~345 (IEF 2.01) | ~50 dB | Yes | $229.99 | Walmart/Sylvane; better app (Midea Air), 3 fan speeds; user doesn't care about smart/app |
| Midea Cube 20 (MAD20S1QWT) — original pick, now restocked | 20 | 3.2 gal | **262** (lowest) | 39-44 dB | Yes | $179-189 | Right-sized on paper for sq footage but slower recovery in extreme humidity + wet carpet; lowest power draw |
| Comfort-Aire BCD-20A | 20 | 3.0 gal | **230** (lowest) | 42 dB | Yes | $190-200 | 20-pint cube clone |

**Tier 2 — now viable thanks to bucket plan (hose+bucket, ~30-pint focus for power/noise):**
Reopened by the pivot. Binding constraints become wattage + noise + price instead of tank. Favors 30-pint units (~$150-180, ~250-300W ~$35/mo vs ~$75/mo for a 50-pint, ~45 dB). A 5-gal bucket gives >1 day of headroom at 30 pints. **50-pints ruled out on HI power cost** (~580W, ~$75/mo running 12hr/day) unless user specifically wants fastest recovery during carpet-drying weeks.

**Ruled out regardless:**
- 30-pint "bedroom" units (Kesnos CTH30B, Waykar, etc.): 0.4-0.6-gal tanks → 6+ empties/day *without* a bucket. (Viable *with* bucket, though.)
- Standard 20-25 pint (Haier QDHR20LZ, GE 25): ~1-gal tank → 2.5+ empties/day at 80-90% RH without bucket.
- Desiccant/mini/thermoelectric (TABYIK, Pro Breeze): not real compressor units, can't hold <50% RH here.

---

## The bucket plan (active strategy)

User will run the dehumidifier's **gravity-drain hose into a bucket**, emptied once daily. ~$15-30 of bucket gear turns "manual draining" from a constraint into a non-issue.

**Risks ranked (user asked, this is the answer to give if revisited):**
1. **Overflow onto carpet — the serious one, and it IS a mold risk.** Gravity-drain port bypasses the internal tank → the unit's "tank full → auto-shutoff" is defeated. A puddle re-hydrates the moldy carpet padding, undoing weeks of drying. Mitigations: bucket sized bigger than a day's extraction + empty religiously daily; bucket in a shallow plastic tray as secondary catch; **$10 water-leak alarm** on the floor beside the bucket (critical overnight).
2. **Mosquitoes — Hawaii-specific.** Standing water = Aedes (dengue/zika vector) breeding. Egg→adult ~7-10 days, so daily emptying breaks the cycle. **A lidded bucket** (drill a hose-sized hole) blocks adults from laying eggs.
3. **Evaporation recycling.** Open bucket returns moisture to room air. **Lid fixes this too** (does double duty with mosquitoes).
4. **Carrying spill.** 5 gal ~40 lb; two hands, don't set on carpet en route.
5. **Bucket biofilm (the user's original worry — actually the smallest risk).** Condensate is near-distilled, low organic content, so mold growth is slow. Weekly rinse, splash of vinegar if slimy. Not potable (coils aren't sterile) but user isn't drinking it.

**Ideal bucket setup:** 5-gal bucket + sealing lid (or Gamma Seal lid ~$20), drill hose-sized hole; hose from gravity-drain port; **leave internal tank in** as a backup shutoff if the port clogs; bucket in a shallow plastic storage bin/tray; leak alarm on floor beside; empty daily, rinse weekly.

**Cube + bucket hybrid option (most bulletproof for remediation phase):** Cube designs also have a gravity-drain port → 4-gal internal tank + 5-gal bucket = ~9 gal = 2-3 days unattended, with internal tank as fail-safe. Probably overkill but the safest option while carpet dries.

---

## Shopping checklist — run this against any candidate the user brings in

If a unit passes ALL greenlight gates and trips no red flag, do a final authorization check (cross-reference wattage claim, sanity-check the pint rating against Energy Star's database, flag reliability red flags on that specific model) and give go/no-go.

### ✅ GREENLIGHT GATES — must pass ALL

| # | Gate | What to look for | Why |
|---|---|---|---|
| 1 | Compressor-based | Says "compressor," "refrigerant" (R410a/R32/R290), or lists CFM/IEF (L/kWh) | Only compressor units hold <50% RH at 80-90%+ nights. Desiccant/thermoelectric tops ~60% |
| 2 | Gravity/continuous drain port | "Continuous drainage," "drain hose connection," "gravity drain," OR hose included | The whole bucket plan. Non-negotiable |
| 3 | 20-35 pints/day (sweet spot 30-35) | Use the DOE/AHAM number — see pint gotcha below | <20 too slow to recover; >35 power cost in HI gets painful for little gain |
| 4 | Energy Star certified | ES logo or "Energy Star" in specs; "Most Efficient 2025" bonus | ~20% less power; real money monthly at $0.36/kWh on a 24/7 device |
| 5 | Watts ≤ ~350 (30-pint) or ≤ ~400 (35-pint) | "Watts"/"Power" in specs; if only amps, × 115 = watts | 580W 50-pint ~$75/mo @ 12hr/day; 300W 30-pint ~$39/mo |
| 6 | Price ≤ $225 incl. HI shipping | Ideally ≤$200 so the ~$20 bucket kit fits the $200 total | User budget |
| 7 | Ships to Hawaii or local pickup | Verify on retailer checkout | User constraint |
| 8 | Noise ≤ ~55 dB | "noise level" dB/dBA | User's AC is 40-60 dB; anything ≤55 sleeps fine |
| 9 | Brand is findable | Real manufacturer name, warranty page, replacement parts/filters available | No-name = no support |

### 🚩 RED FLAGS — any one = skip, don't authorize

- "Peltier," "thermoelectric," "desiccant," "semiconductor," "ultrasonic" — can't hit <50% RH here
- "Mini," "closet," "desktop," "bathroom," "RV" + rated <150 sq ft / <10 pints — too weak
- No drain port at all (manual-tank-only) — defeats the bucket plan
- No wattage/amps published anywhere — can't vet power cost
- Not Energy Star — wastes HI power
- "Up to 50 pints at 90°F/90% RH" with no DOE rating — see gotcha
- Ozone generator / ionizer-only marketing (junk brands)
- Suspiciously cheap ("50-pint for $79") — almost always a rebadged 10-pint thermoelectric
- No warranty info / no replacement filters

### ⚠️ Pint-rating gotcha (trips up shoppers)

Since 2019 the DOE tests dehumidifiers at **65°F / 60% RH** (was 80°F/60%). Manufacturers cite two numbers:
- **Real number = DOE/AHAM rated pints** (65°F/60% RH). Energy Star uses this. **Trust it.**
- **Fantasy number = "up to X pints/day at 90°F/90% RH"** — can be 2-3× the real number. A "50-pint (90°F/90%)" might be a real ~20-pint DOE unit.

**Rule:** if the page only shows a "max conditions" number and no DOE/AHAM/IEF number, treat as suspect — find the DOE rating (Energy Star product finder or spec sheet PDF) or skip. Gates #3 and #5 use the DOE number.

### Nice-to-haves (NOT gates)
Auto-defrost; auto-restart after power outage; adjustable humidistat (35-85% range) with target setpoint; washable filter (no recurring cost); 2+ fan speeds; internal tank still present as backup shutoff if hose clogs; timer.

### The copy-paste block the user sends in
```
Brand + model:
DOE-rated pints/day:
Watts (or amps):
Tank size (gal) — even though using bucket, tells if backup shutoff exists:
Gravity/continuous drain port? (Y/N, hose included?):
Noise dB:
Energy Star? (Y/N, Most Efficient?):
Price (incl. HI shipping):
Retailer link:
```

---

## Open decisions / follow-ups

- **User is actively shopping** and will send candidate units for go/no-go authorization against the checklist above.
- **Cube (Tier 1) vs hose+bucket 30-pint (Tier 2):** user hasn't picked a lane. Cube = simpler (no bucket needed), big internal tank, but ~$200-225 and slightly more power. 30-pint + bucket = cheaper unit (~$150-180), less power, but adds bucket-maintenance overhead. Both viable; user's call.
- **Bucket-kit purchase** (~$15-30) needs to happen if going Tier 2 or cube+bucket hybrid: 5-gal bucket + sealing/Gamma lid + shallow tray + leak alarm.
- **Carpet mold:** whether truly dead or needs section replacement — assess when user is home.
- **Symptoms:** reassess 4-6 weeks post-fix; if not improving, consider a CIRS workup with a doctor.
- **Air purifier:** deferred, may have $50-90 later. Criteria preserved below for that future purchase.

---

## Air purifier evaluation criteria (preserved for later — deferred purchase)

When the user has $50-90 to spend on the "polish layer" purifier, run this checklist against any unit. The purifier only cleans up spores already airborne — it complements, not replaces, the dehumidifier. HEPA captures spores easily (spores are 3-12μ, HEPA traps 99.97% @ 0.3μ); differentiator is CADR / coverage / filter cost, not "better HEPA."

**Good fit = meets ALL of these:**

| # | Criterion | Why | Pass threshold |
|---|---|---|---|
| 1 | True HEPA (says "True HEPA," 99.97% @ 0.3μ) | Captures mold spores | Must say "True HEPA" — not "HEPA-type"/"HEPA-style" |
| 2 | CADR ≥ 100 CFM (dust) | 4-5 air changes/hr in 200 sq ft | ≥100 good; 135+ great; <100 too weak |
| 3 | Room rating ≥ 200 sq ft | Must cover the room | ≥200 (ideally 300+ for headroom) |
| 4 | Carbon layer present | Helps with musty mold odor | Light carbon fine (no smoking in room now, so heavy carbon not needed) |
| 5 | Replacement filter ≤ ~$25 | User is broke; ongoing cost matters | Check filter price on the product page |
| 6 | Price $50-90 (up to ~$100 if clearly better) | Budget | $50-90 ideal; up to $100 OK if justified |
| 7 | Noise: irrelevant | User doesn't care | Don't penalize for loudness; don't pay extra for quiet |

**Red flags → automatic Bad fit:** ozone generator / ionizer-only (no True HEPA); "HEPA-type"/"HEPA-style" without "True HEPA"; no CADR published; desktop/mini unit rated <150 sq ft; no-name brand with no replacement filters available.

**Verdict format:** Good fit / Borderline / Bad fit — one-line reason per failed criterion, and a better pick from the reference list if borderline/bad.

**Reference picks at this budget:**
- Levoit Core 200S ~$70-80, ~109 CFM, 200 sq ft, filters ~$15 — top budget pick
- Levoit Core 300 (on sale) ~$89-99, 135 CFM, 300 sq ft, AHAM Verified, filters ~$15-20 — gold-standard budget
- GermGuardian AC4825 ~$70-90, ~100 CFM, 150-200 sq ft, filters pricier (~$30) — backup
- (if budget expands) Coway AP-1512HH Mighty ~$230, 246 CFM, 361 sq ft — best long-term
- (NOT needed now) Winix 5500-2 ~$240, 232 CFM, 360 sq ft — only if smoking returns to the room

**Run strategy:** purifier 24/7 on medium, especially at night. Dehumidifier is the priority device; purifier is the polish.

---

## Suggested next-session skills

- `tutorial` — if user wants a step-by-step walkthrough for setting up the dehumidifier + bucket kit + measuring RH when they get home.
- `create-nav-guide` — if user wants to save this shopping checklist as a reusable NavGuide for future appliance shopping (the checklist generalizes beyond dehumidifiers with minor edits).
- (No coding skills apply — this is a lifestyle/health/appliance task.)

## Key paths
- This file: `b0ttsagent/handoffs/07-06-2026/dehumidifier-shortlist-bucket-drain.md`
- Room airing schedule (reference, not duplicated): `b0ttsagent/temp/room-airing-schedule.md`
- Superseded/deleted: `b0ttsagent/handoffs/07-06-2026/purifier-evaluation-context.md` (purifier criteria folded into this doc)
- AGENTS.md: `AGENTS.md` (repo guidance)
- No codebase files are involved in this task.
