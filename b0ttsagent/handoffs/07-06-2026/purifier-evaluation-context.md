# Purifier Evaluation Context (Handoff)

**Purpose:** Give a fresh AI agent the context needed to evaluate whether a specific air purifier is a good fit for the user. The user will paste a purifier's specs/link alongside this doc and ask, "Is this good for me?"

**How to use this doc:** When the user sends a purifier (link/specs), run the checklist in the [Purifier evaluation criteria](#purifier-evaluation-criteria-run-this-checklist-against-any-purifier) section against its specs. Give a clear verdict (Good fit / Borderline / Bad fit) with a one-line reason per failed criterion, and suggest a better pick from [Reference picks](#reference-picks-what-good-looks-like-at-this-budget) if it's borderline or bad.

---

## User context

**Location & climate:** Central Oahu, Hawaii, ~1,366 ft elevation. Tropical, very humid.
- Average RH ~76% year-round (range 73-79%)
- **Nighttime RH rises to 80-90%+** (temp drops, moisture stays) — this is the danger window for mold
- Dew point 63-69°F; "muggy" May-Nov; September is the worst month
- 52" rain/year, 239 rainy days
- Hawaii electricity ~$0.33-0.40/kWh (highest in US) — matters most for the dehumidifier, less so for purifiers (low wattage, ~35-77W)

**Room:** ~100-200 sq ft bedroom. Sealed-room problem: poor airflow with door+window closed; excellent airflow when both open. Carpet had black mold (deep, surface-treated with baking soda/vinegar/detergent — likely still alive in the padding). Lots of blankets/comforters in closet (dust + moisture reservoirs). Room gets stinky/humid/hot after a day closed up.

**Health context:** Chronic mold exposure (black mold + all-day exposure as a software engineer working from the room) → symptoms: deep fatigue, depression, brain fog, cognitive impairment. Environment remediation is expected to resolve symptoms over weeks-to-months. If symptoms persist after RH is consistently <50% and the mold is removed, consider a CIRS (Chronic Inflammatory Response Syndrome) workup with a doctor.

## Ventilation / AC situation
- **Day:** AC on, windows closed, working. AC dehumidifies partially but often can't hit <50% RH alone.
- **Night:** AC off → no dehumidification, ambient RH 80-90%+. This is when the dehumidifier and purifier matter most.
- **Bad mode:** windows + door closed, fan only → humidity spikes, spores spike, worst exposure.
- **No longer smoking in the room** (smokes outside/bathroom now). So heavy carbon for smoke is NOT required — light carbon for musty odor is enough.

## Decisions already locked (do not relitigate)
- **Dehumidifier:** Midea Cube 20-pint (MAD20S1QWT), ~$200 — being purchased by grandparents as a Christmas-present trade. This is the root-cause fix (stops mold growth by holding RH <50%).
- **Hygrometer:** $10, to measure actual RH and set the dehumidifier target to ~48%.
- **Source control:** clean carpet mold (bleach/Concrobium; possibly replace the carpet section), hot-wash blankets, declutter.
- **Ventilation:** crack window + cheap box fan for fresh air exchange in sealed mode (addresses CO2/stuffiness separately from mold).
- **Air purifier = the "polish" layer.** Deferred, but the user may have $50-90 to spend on one during/after a trip.

---

## Purifier evaluation criteria (run this checklist against any purifier)

A purifier is a **Good fit** if it meets ALL of these:

| # | Criterion | Why it matters | Pass threshold |
|---|---|---|---|
| 1 | **True HEPA** (says "True HEPA", 99.97% @ 0.3μ) | Captures mold spores (3-12μ) | Must say "True HEPA" — not "HEPA-type"/"HEPA-style" |
| 2 | **CADR >= 100 CFM** (dust) | Gives 4-5 air changes/hr in 200 sq ft | >=100 good; 135+ great; <100 too weak |
| 3 | **Room rating >= 200 sq ft** | Must cover his room | >=200 sq ft (ideally 300+ for headroom) |
| 4 | **Carbon layer present** | Helps with musty mold odor | Light carbon fine (no smoking in room, so heavy carbon not needed) |
| 5 | **Replacement filter <= ~$25** | User is broke; ongoing cost matters | Check filter price on the product page before recommending |
| 6 | **Price $50-90** (up to ~$100 if clearly better) | User's budget | $50-90 ideal; up to $100 OK if specs justify |
| 7 | **Noise: irrelevant** | User explicitly doesn't care | Don't penalize for loudness; don't pay extra for quiet |

**Red flags → automatic Bad fit:**
- Ozone generator / ionizer-only (no True HEPA)
- "HEPA-type" / "HEPA-style" without "True HEPA"
- No CADR published
- Desktop / mini unit rated <150 sq ft
- No-name brand with no replacement filters available for purchase

**Verdict format:** Good fit / Borderline / Bad fit — with a one-line reason per criterion that fails, and a better pick from the reference list if borderline or bad.

---

## Reference picks (what "good" looks like at this budget)

| Model | ~Price | CADR | Room rating | Notes |
|---|---|---|---|---|
| **Levoit Core 200S** | ~$70-80 | ~109 CFM | 200 sq ft | Top budget pick; True HEPA + carbon; smart/app; filters ~$15 |
| **Levoit Core 300** (on sale) | ~$89-99 | 135 CFM | 300 sq ft | Gold-standard budget; AHAM Verified; filters ~$15-20 |
| **GermGuardian AC4825** | ~$70-90 | ~100 CFM | 150-200 sq ft | Backup; UV-C is meh; filters pricier (~$30) |
| (if budget expands) **Coway AP-1512HH Mighty** | ~$230 | 246 CFM | 361 sq ft | Best long-term; cheap filters; legendary reliability |
| (NOT needed now) Winix 5500-2 | ~$240 | 232 CFM | 360 sq ft | Only if smoking returns to the room (washable carbon) |

---

## Key facts to keep in mind
- **Mold stops growing/sporulating at RH <50%.** The dehumidifier is the root-cause fix. The purifier only cleans up spores already airborne — it's a complement, not a replacement for the dehumidifier.
- **HEPA captures spores easily** — spores are 3-12 microns, HEPA traps 99.97% at 0.3μ. Any genuine True HEPA will handle spores; the differentiator between purifiers is CADR / coverage / filter cost, not "better HEPA."
- **Fresh air exchange matters too** — a sealed occupied room builds CO2 + pollutants (a separate cognition factor from mold). The purifier recirculates/cleans air but does NOT add fresh air. He's addressing this with a cracked window + box fan.
- **Run strategy:** purifier 24/7 on medium, especially at night while sleeping. The dehumidifier is the priority device; the purifier is the polish.

---

## Suggested next-session skills
- `tutorial` — if the user wants a step-by-step walkthrough for setting up the dehumidifier + measuring RH when he gets home.
- `create-context-doc` or `create-planning-docs` — if the user wants to formalize the full remediation plan into a doc.
- (No coding skills apply — this is a lifestyle/health/appliance task, not a codebase task.)

## Key paths
- This file: `b0ttsagent/handoffs/07-06-2026/purifier-evaluation-context.md`
- AGENTS.md: `AGENTS.md` (repo guidance)
- No codebase files are involved in this task.

## Open decisions / follow-ups
- Whether the user will have $50-90 available for a purifier after the trip (TBD).
- Whether carpet mold is truly dead or needs section replacement (to assess when he's home).
- Whether symptoms clear after remediation (reassess at 4-6 weeks post-fix; if not, consider a CIRS workup).
