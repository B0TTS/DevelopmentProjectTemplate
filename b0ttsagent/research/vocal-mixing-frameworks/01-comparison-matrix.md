# Cross-Artist Comparison Matrix

**Purpose:** fast lookup — compare any two documented workflows element by element. Every row is compressed; open the linked case study for the full chain with settings and source URLs.

**Reading key:** Evidence = strongest tier backing that row (A = primary technical interview, B = reputable secondary, C = community reconstruction). `→` = signal order.

---

## Table A — Documented recording chains (what the vocal passes through while being recorded)

| Artist / Engineer | Mic | Preamp | Compression at tracking | Tuning at tracking | Evidence |
|---|---|---|---|---|---|
| Young Thug — Bainz | Sony C-800G | Neve 1073 | Tube-Tech CL-1B | Auto-Tune on the record insert, always | A |
| Chris Brown — Teezio | Telefunken ELA M 251 | Neve 1073 | Tube-Tech CL-1B | Auto-Tune **printed**, Retune 11–13 | A |
| Drake — 40 / Cadastre | Sony C-800G (or U87; SM57 in control room) | Neve 1073/1081 | Teletronix LA-2A, "very lightly" | Auto-Tune early in the ITB chain | A (C for the "Cadastre chain" specifics) |
| Kanye — Mike Dean | C-800G / SM7B / U67 | Neve 1073 (or BAE) | CL-1B, "that's it" | Minimal Melodyne; Auto-Tune only as effect | A |
| Post Malone — Louis Bell | Sony C-800G | Apollo Twin built-in pre (no outboard) | UAD 1176 ITB | Melodyne, then very light Auto-Tune | A |
| Bieber — Josh Gudwin | (studio condenser) | — | UAD SSL E-Channel → LA-2A → Waves C6, kept into the mix | Melodyne by Chris "Tek" O'Ryan | A |
| Billie Eilish — Finneas | AT2020 ($80) → later TLM 103 | Apollo | Logic stock compressor | None as fix; Auto-Tune only as obvious effect | A |
| twenty one pilots — Hawkins | Sony C-800G | UA 610, **overdriven** | Blue-stripe 1176 | — | A |
| Fall Out Boy — Neal Avron | Neumann U47 tube | — | Neve 33264 / Distressor / 1176, 4:1–8:1, "hit pretty hard" | — | A |
| Kendrick — MixedByAli (TPAB era) | Modded Telefunken U47 (U67 on "Alright") | Neve 1073 | CL-1B | — | A |
| Lil Uzi Vert — Kesha Lee | — | — | — | **Auto-Tune is insert #1 on every vocal track, no exceptions**; Uzi hears it in headphones; Retune 12→5 | A |

**Shared pattern:** one great bright mic → Neve-style preamp → one opto compressor (CL-1B/LA-2A) touching lightly → tuning live if it's an effect, after if it's a fix. Details: `case-studies/04-tracking/rap-vocal-recording-chains.md`.

## Table B — Documented mix vocal chains (what the mixer actually does)

| Engineer (acts) | Chain, compressed | Comp philosophy | EQ philosophy | Space/FX | Signature | Evidence |
|---|---|---|---|---|---|---|
| Bainz (Thug/Gunna) | Pro-Q3 → Auto-Tune → DeEdger ×2 → Soothe2 → Spiff → Pro-Q3 → C6 → de-esser → CL-1B; printed aux: True Iron → MC404 → Ruby 2 → Ultra Marine 4 → Neutron Exciter; bus: Pro-DS → Royal Mu → Gullfoss ≤20% | Late, gentle, after cleanup | Cleanup cuts on tracks; tone (Ruby tube EQ) on bus | 9 sends; ¼-note delay **sidechain-ducked**; Bricasti plate | **Vox Throws** — 15 100%-wet FX tracks, dropped on single words as the last step | A |
| Kesha Lee (Uzi) | Per track: Auto-Tune → DeEsser → EQ3 → C1 gate. Bus: de-ess @4230 Hz → EQ3 (HPF 96 Hz, −200/500, +6.5k) → RComp → SSL E → CLA-3A → Detailer → MCL-2269 limiter | Serial color comps on the bus | Cut mud, add 6.5k "Firkins" air | Half-note delay + highs-cut hall + S1 width | **Beat turned down 1–2 dB** — vocal louder than the beat | A |
| Teezio (Chris Brown) | Pro-Q2 → EQP-1A → 1176 → Pro-MB → RComp → De-Esser | **Staged light comp** ×3–4, never one hard | Pultec tone early | Printed hand-edited H-Delay ¼/8th; Valhalla on sends only | Printed Auto-Tune on the way in (Retune 11–13) | A |
| Josh Gudwin (Bieber) | Per track: SSL E → LA-2A → C6. Bus: 1176, Pro-DS, Manley Massive Passive (cuts 330/560/3k) | Smooth leveling + bus glue | Light surgical cuts on bus | Hall + plate + ¼ + ping-pong + Dimension D sends | The fixed "trio" template; vocal is the mix | A |
| Rob Kinelski (Billie) | Pro-Q2 low-cut → PuigChild 670 → De-Esser 6557 Hz → Pro-Q2 (mids 200–2k) → 1073 color → Vocal Rider 1.5 dB → manual rides | One gentle color comp | Low-cut + mid scoop only | Nearly none — dry intimacy | Same chain on all 4 vocal groups, whole album | A |
| Ian Kirkpatrick (Dua Lipa) | Cleansweep 30 Hz → Vulf → LA-3A → Soothe → Pultec (+12k into de-esser) → Pro-DS → Pro-Q2 → LFO Tool ducking | Two soft comps doing "almost nothing" each | Subtractive body control (Soothe) | VintageVerb + OTT + 1176 on the return | **3-pass comping**; comp → tune → final comp | A |
| MixedByAli (Kendrick) | RComp (thresh −18) → SSL filters → S1 width → Distressor grit; modern: SSL 4000E **+8k bell / −300 Hz** | RComp for mid control + Distressor presence | Desk EQ; 8k bell / 300 Hz dip | EMT 250; FX as narrative emotion | **Mono Auratone for ~80% of the mix** | A |
| Manny Marroquin (Kanye) | HPF 160/200 → 32264 3:1 fast → CL-1B 4:1 med → Avalon 2055 (+25k, −220) → dbx 902 | **Dual comp**: fast + smooth | Sizzle high, cut low-mid | Echo Farm 577 ms throws; PCM42 80 ms slap | **SSL sidechain de-esser** (boost +12 dB @6–7k in the key) | A |
| Jaycen Joshua (current rap/pop) | El Rey → Pro-Q3 → MC404 → Fresh Air → de-esser → CLA Vocals → MV2 | MV2 leveling last | Fresh Air for presence | **No reverb on rap** — delays only ("RapVerb" is a delay) | Parallel 160x→Pultec on kick/808; chain-on-flat-then-dial | A |
| Louis Bell (Post Malone) | 1176 → CLA Vocals → 1073/550A; RVerb; Inflator | 1176 for attack/roundness | Minimal — capture right | Lots of reverb by artist taste ("anthemic") | Melodyne → light Auto-Tune lock; ad-lib chorus separation | A |
| Chris Lord-Alge (rock/pop) | Bus: SSL E (+9 dB @8k, HPF ~70) → CLA-76 (4:1, slow attack/fast release) → CLA Vocals → L1; Devil-Loc lightly per track | **Pummel**: 15–20 dB GR; drive more level in for more comp | **Broad, additive only** — EQ feeds comp | Tempo delays; hall for anthemic sections only | Limiter-as-attitude; automation is the real mix | A |
| Adam Hawkins (TØP/MGK) | Decapitator → Pro-Q2 HPF → Scheps Omni → RenDeEsser → dbx 160 → J37 slap | Omni high-ratio + 160 "sheen" | 300 Hz taming | Little Plate, EchoBoy ×3, MicroShift | Distortion as texture; album-wide template reuse | A |
| Zakk Cervini (modern alt) | Clip gain → tune → subtractive Pro-Q3 → opto 1–2 dB → Pultec air/body → 1176 fast/fast → ducked FX sends | Gentle opto then FET "pin" | Surgical first, Pultec color after | Valhalla + EchoBoy, **sidechain-ducked** | Five "small moves" chain; FX duck under the vocal | A (via his NTM teaching) |
| Andrew Scheps (Hozier etc.) | No insert chain — slap ~110 ms + short plate/room + pitch-shifted stereo delay; everything into **parallel buses / Rear Bus** | Parallel density instead of insert comp | "EQ for placement, not volume" | Sounds bone-dry but isn't | Rear Bus: one compressor the whole mix feeds | A |
| Dan Lancaster (BMTH) | SSL E + CLA-76 per section-track; PuigTec +16k verse air; MM Drive as distortion-EQ | **"Spank" first** — heavy comp before anything | Per-layer surgical notches | Insert reverbs on featured harmonies | Section-split vocal tracks (same singer, 6 chains) | A |
| Neal Avron (FOB/TØP) | Verse/chorus Filterbank EQs (verse +8.4k) → C4 taming harsh registers | Hard at tracking, little at mix | Section-differentiated | Dry lead; 16th-note delays on stacks | Compression as attitude, not level | A |
| Mike Dean (Kanye/Travis) | Minimal ITB: Nectar 3 / RVox / Pro-Q3 / bx_2098; D-Verb, H-Delay, Valhalla | One opto at tracking; often nothing after | **Don't EQ what's already right** | Stock-ish, simple | "Stop overmixing"; stay true to the demo | A |

## Table C — Self-mixed / underground artists (your taste lane: what's verified vs reconstructed)

| Artist | Verified fact (A/B tier) | Community reconstruction (C tier — unverified) |
|---|---|---|
| Yeat | Records, engineers, and mixes his own vocals (FADER); up to ~90 vocal tracks; ad-libs as sound design; bedside MacBook immediacy | "Retune 0–10 ms, heavy saturation, dry loud vocal" — preset-blog guesswork |
| Playboi Carti | Fritz Owens recorded + mixed all of *MUSIC*; closed-loop sessions (only engineer hears takes); Mike Dean mixed one track | Rage-chain specifics — fan reverse-engineering only |
| Lil Uzi Vert | Kesha Lee's full documented chain (Table B) | — |
| wifiskeleton | FL Studio + Soyuz 1973 + UA Volt 476 (own photos); early catalog made on **BandLab**; taught his own style on YouTube | Bitcrush/pitch-stack "sigilkore chain" tutorials — by ear |
| Drain Gang / whitearmor | Auto-Tune as the founding instrument (Bladee, Guardian); fully self-produced/self-mixed; albums made in cottages/bedrooms in weeks | Everything else — no technical docs exist |
| Lucki / Yung Icey | Finishes most of each album alone, then final sessions with Icey; FL Studio pipeline | Vocal chain never documented |
| Opium (Ken Carson/Lone) | Ben Lidsky records/mixes bulk; Roark Bailey mixes flagships; Colin Leonard masters all | "Opium vocal preset" numbers — marketing, not sources |

## What actually differs by genre (the short version)

| Decision | Polished rap/pop (Ali, Bainz, Gudwin, Bell) | Rock/alt (CLA, Hawkins, Cervini, Lancaster) | Rage/underground (reconstructed) |
|---|---|---|---|
| Compression total | Staged, 2–4 light touches | Heavy: 15–20 dB GR is the sound | Heavy + clipping tolerated |
| EQ instinct | Subtractive cleanup, then tone | Broad additive boosts into comp | Whatever survives the beat |
| Reverb | Minimal; delays instead | Short, purposeful | Dry and loud on top |
| Tuning | Doctrine-split (see patterns doc) | Transparent/none | Maximal, audible, instant |
| Vocal level | Loud | Loud | **Louder than the beat** |
