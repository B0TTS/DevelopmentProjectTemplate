# The Universal Vocal Chain (Distilled From the Research)

**What this is:** one starter chain synthesized from every documented workflow in this research set, in the order the jobs appear across all of them — translated into free tools so you can run it today. It is a *starting routing*, not a preset: the legends share the order and the job of each stage; the settings are yours to dial per song (see `02-recurring-patterns.md`, pattern 14).

**The chain, in one line:**
`clean recording → tune → subtractive EQ → de-ess → level (clip gain) → gentle comp → tone EQ → fast comp → saturation → sends (ducked delay, short verb) → throws`

---

## Step 0 — Move off Audacity for the chain work

Audacity teaches editing and comping fine, but its real-time chain workflow is the weakest of any free option, and every framework in this research assumes a channel strip you can reorder live.

| Free/cheap DAW | Why |
|---|---|
| **Reaper** ($60, unlimited full-featured trial) | The practical choice: full routing, sends, sidechains, free stock suite (ReaEQ, ReaComp, ReaXcomp). Closest to how pros think |
| **Waveform Free** | Fully free, unlimited tracks, real sends |
| **GarageBand** (Mac only) | What Yeat sketches on; fine to start |

Your MP3-instrumental workflow stays identical in all of them: beat on track 1, vocals above it.

## Step 1 — Record it right (the stage that does 50% of the work)

- Peaks around **−6 dBFS**, no clipping, 24-bit (the documented SoS standard — `cs/04-tracking/gain-staging-and-session-workflow.md`)
- Quiet, soft room (closet clothes / blankets behind and above you), pop filter or sock, mic slightly off-axis to reduce sibilance
- **Monitor an exciting vocal in your headphones while recording** (pattern 13): at minimum your tuning + a little reverb/delay in the cue, even if you record dry
- Details: `04-home-recording-playbook.md`

## Step 2 — Tune first (choose your doctrine)

| Goal | Free tool | Setting guidance (from `cs/04-tracking/tuning-workflows.md`) |
|---|---|---|
| Audible rap/rage effect (Uzi/Carti/Yeat lane) | **MAutoPitch** (free) or Graillon Free | Retune/speed fast — near-instant for hard-tune; Uzi's documented range is Retune 12 down to 5 |
| Invisible fix | **Melodyne trial** or manual pitch in your DAW | Slow retune (20–80 ms) + humanize; fix only what's off |

Set the **key of the beat first** — a wrong key setting tunes you to wrong notes. Put tuning before everything else (Antares' documented guidance; pattern 1).

## Step 3 — Subtractive EQ (cleanup)

Free: **TDR Nova** (dynamic EQ), stock EQ, or **ReaEQ**.

1. High-pass ~80–100 Hz (Kesha: 96 Hz; Teezio HPFs at 80 while tracking)
2. Sweep-solo to find and notch harshness/resonances (Bainz does this with clip effects; you do it with a narrow bell)
3. Cut mud zone **200–500 Hz** a few dB if boxy (Kesha dips 200 + 500; Ali dips ~300)

## Step 4 — De-ess

Free: **TDR Nova** (band mode on the ess region) or Spitfish.

- Start searching **4–8 kHz**; documented anchors: Kesha 4230 Hz, Kinelski 6557 Hz
- If you boost air later and the esses come back, add a *second* light de-esser after the boost (Kinelski does exactly this)

## Step 5 — Level with clip gain, before any compressor

Turn loud words down and quiet words up *on the clip* (Tumay's leveling doctrine; Bainz clip-gains badly tracked vocals; Cervini's step 1). Target: a compressor that follows sees an already-mostly-even performance. This is the cheapest professional-sounding move in the entire document.

## Step 6 — Gentle compression (evening stage)

Free: **ReaComp**, **TDR Kotelnikov**, or stock compressor.

- Ratio ~2:1–3:1, slow-ish attack, medium release, **1–3 dB of gain reduction** (Cervini's opto stage: 1–2 dB)
- Job: smooth the performance, nothing more (Kinelski's PuigChild "doesn't hit it very hard")

## Step 7 — Tone EQ (the "sound" stage)

Now that the vocal is clean and even:

- **Air:** +2–4 dB shelf/bell at **8–12 kHz** (Ali's +8k bell; CLA's +9 @ 8k; Kesha's +6.5k; Kirkpatrick's +12k). Free: **Fresh Air** (Slate, free) was built for exactly this and is in Jaycen Joshua's current chain
- Optional body: small boost 150–250 Hz if the vocal is thin
- Rule from CLA: EQ *into* the fast compressor (next step), so the comp tames any harshness the air boost wakes up

## Step 8 — Fast compression (character/pin stage)

Free: ReaComp (fast attack/release), **Klanghelm DC1A** (free 1176-ish).

- 1176-style behavior: ratio 4:1, fast attack, fast release, 2–5 dB GR (Teezio/Cervini territory)
- Rock/aggressive lane: push to 8–15 dB GR (CLA/Lancaster). Rage lane: push until it survives your beat
- Net result of steps 6+8: staged compression — the single most repeated comp pattern in the research

## Step 9 — Saturation (subtle)

Free: **Softube Saturation Knob**, **Klanghelm IVGI**, or a second instance of anything driven slightly.

- A few % of harmonic grit helps the vocal cut small speakers (Bainz: True Iron + Neutron Exciter; Hawkins: Decapitator "nothing crazy"; Manny/Ali: tape + Decapitator on "The Box")
- If you can hear the distortion on solo, it's probably too much — judge it against the beat

## Step 10 — Space via sends (never inserts on the lead)

Free: **Valhalla Supermassive**, stock delay, any free plate.

1. **Send A — tempo delay:** ¼-note or ½-note (Kesha uses half-notes), low-pass the return, and if your DAW allows, **duck it with a compressor keyed by the lead** (Bainz/Cervini pattern) so it only blooms in gaps
2. **Send B — short plate/room:** small, dark, barely audible (Scheps' "bone dry but isn't" recipe)
3. Keep the lead itself dry; rap vocals die under big reverb (Jaycen's rule)

## Step 11 — Throws and ear candy (last, like Bainz)

When the static mix is done: duplicate single words onto a new track, pitch them down / add huge reverb / chop them, tuck them low. 2–5 moments per song, not 50. ("One of the last things I do in the entire process" — Bainz.)

## Final — level against the beat

Turn the **beat down 1–2 dB** from where it feels safe (Kesha). Check the hook in mono at low volume (Ali's Auratone doctrine). Bounce, listen on phone speaker + earbuds, adjust vocal level once more. Done — don't open it again tomorrow (Leslie/Mike Dean speed doctrine; Yeat: "I never touch anything after it's done").

---

## The 10 mistakes this research says you're probably making

1. **Boosting EQ on a raw, uncleared vocal** — cleanup first (pattern 4)
2. **One compressor doing 10 dB** — split it into two stages (pattern 5)
3. **Tuning after EQ/compression** — pitch tracking degrades; tune first (pattern 1)
4. **Big reverb on rap vocals** — delays, ducked (pattern 7)
5. **No clip gain** — the compressor is doing your editing job (step 5)
6. **Recording too hot or too quiet** — peaks ~−6 dBFS (step 1)
7. **No de-esser, or one after a big air boost only** — budget for two (pattern 6)
8. **Mixing the vocal quieter than the beat** — pattern 8
9. **One chain for verse and hook when your delivery changes** — split per section (pattern 9)
10. **Mixing for 3 days** — time-box it; speed is a documented feature (pattern 12)

## Practice protocol (how to actually internalize this)

1. **Week 1 — capture:** record the same 8 bars 5 times, changing only mic distance/room. Keep the best; learn what "recorded right" sounds like raw.
2. **Week 2 — the chain:** run steps 2–8 on that take. Bypass-toggle each stage and name out loud what changed. If you can't hear a stage, it's doing too little or too much.
3. **Week 3 — space + throws:** steps 10–11. A/B against a reference song you love at matched loudness.
4. **Week 4 — speed runs:** full song, 60-minute cap, three sessions on three different songs (Leslie's 3-hour rap mix, compressed). Compare your week-4 mixes to week 2.
5. **Ongoing:** every new song, change exactly one variable. The engineers in this research got their sound from repetition of a fixed framework, not from exploring plugins.
