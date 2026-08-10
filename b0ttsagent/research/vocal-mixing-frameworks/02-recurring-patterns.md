# Patterns That Recur Across Legends

**The meta-finding:** across 30+ verified engineers/artists spanning polished pop, chart rap, rage, and rock, the vocal workflows converge on the same skeleton. They disagree about *amounts* and *taste* — they almost never disagree about *order and job of each stage*. The formula is a sequence of jobs: **capture it right → tune (first, if it's an effect) → clean up → level → compress in stages → tone → place in space → excite**. Everything else is personality.

**How to read this doc:** each pattern states what recurs, who does it (with the strongest source), and what it means for you. Case-study paths are abbreviated — `cs/01/…` = `case-studies/01-modern-rap-mix/…` etc.

---

## The patterns

### 1. Tuning goes first — and there are exactly two doctrines

Every documented workflow puts pitch correction at or near the front of the chain (Antares' own guidance: pitch correction on the raw vocal, before reverb/compression, because processing degrades pitch tracking — `cs/04-tracking/tuning-workflows.md`). The split is *intent*:

| Doctrine | Who | Practice |
|---|---|---|
| **Auto-Tune as the instrument** (live, audible, often printed) | Teezio (Retune 11–13, printed — "no one will ever hear Chris's vocal raw"), Kesha Lee (insert #1 always, Uzi performs through it; Retune 12→5), Bainz (on every record track), Mike Dean (invented the 808s "Heartbreak" sound), Bladee ("it's how we found our sound"), Yeat/T-Pain lineage | Fast retune, monitored in headphones while recording, committed to tape |
| **Melodyne as invisible fix** | Kuk Harrell, Josh Gudwin (Tek O'Ryan tunes), Louis Bell (Melodyne → light Auto-Tune lock), Ian Kirkpatrick (comp first, then Melodyne), Mike Dean (minimal), Jaycen Joshua ("Auto-Tune is an effect, not a tuner") | Slow/manual correction after comping; the listener never knows |

There is no third option. Pick your doctrine per song; don't drift between them mid-record.

### 2. The recording chain is nearly identical everywhere

Bright, in-your-face LDC mic (Sony C-800G is the modern rap/pop standard — Kuk Harrell: "vocals are very bright and in-your-face today"; Dr. Dre's engineer ran it into a Neve 1073) → Neve-style preamp → one opto compressor (Tube-Tech CL-1B or LA-2A) touching lightly. Documented for Thug, Drake, Kanye, Chris Brown, Post Malone, Kendrick, twenty one pilots. Details: `cs/04-tracking/mic-selection-and-mic-chains.md`.

**Why it matters:** the mic is chosen as the *first EQ move* — a mic whose top end already cuts means less boosting later, which means less sibilance and harshness to fix.

### 3. Compress at capture, not just after

Bainz, Mike Dean, Tumay ("compress until it sounds right with nothing on Pro Tools"), Teezio, Avron ("hit the vocal pretty hard," 4:1–8:1), Hawkins (overdriven UA 610 → 1176). The performance arrives at the mix already leveled and colored. Counterpoint exists (Louis Bell records clean through an Apollo pre so he can change color later) — but even he compresses in the box immediately after.

### 4. Cleanup comes before tone — always

Every deeply documented chain opens with subtraction, not enhancement:

- Bainz: RX + clip-effect notches, then Pro-Q3/DeEdger/Soothe2/Spiff *before* any tone plugin; "clean-up stuff on audio tracks, tone shaping on the bus" (`cs/01/bainz.md`)
- Leslie Brathwaite: "I take what's called a subtractive approach… tedious cleanup work that some engineers don't do" (`cs/01/leslie-brathwaite.md`)
- Cervini: clip gain → tune → **subtractive EQ** → then compression (`cs/05/zakk-cervini.md`)
- Kinelski: chain *starts* with a low cut; Kirkpatrick: chain starts with a 30 Hz cleansweep; Kesha: de-esser is insert #2

The modern toolchain for this stage: Soothe2, TDR DeEdger, Pro-DS, RX. Job: remove mud, harshness, plosives, room, and sibilance *so the compressor reacts to the voice, not the problems*.

### 5. Compression happens in stages, each doing a little

Teezio: "Instead of completely smashing things with one compressor, I will compress lightly in stages" (EQP-1A → 1176 → Pro-MB → RComp). Cervini: opto 1–2 dB, *then* 1176 to "pin" it. Marroquin: fast 32264 *then* smooth CL-1B — "two compressors because I was looking for a speed of attack the CL-1B doesn't have." Gudwin: LA-2A on tracks, 1176 on the bus.

**The division of labor:** one compressor evens the performance (slow/opto), another catches peaks and adds character (fast/FET). The rock lane is the loud exception — CLA's 15–20 dB GR "pummel" and Lancaster's "spank" — but note both still add a *second* stage (limiter, bus comp) after.

### 6. De-essing is non-negotiable, and often happens twice

Kinelski's standard: Waves De-Esser at 6557 Hz, plus Pro-DS at the end for tricky vocals. Kesha de-esses per-track *and* on the bus at 4230 Hz. Bainz runs de-essers in the cleanup stage *and* Pro-DS on the vocal bus. Marroquin built his famous SSL sidechain de-esser because stock ones "retain less personality." CLA's rule explains *why* everyone is careful: "EQ after the compressor leads to sibilance issues" — boost into compression, and the comp tames the harshness the boost creates.

### 7. Rap vocals live on delays, not reverb

Jaycen Joshua: "Reverb is the kiss of death on rap vocals… reverb and rap don't mix" — his "RapVerb" is a delay. Kesha's vocal space is a half-note delay into a highs-cut hall, widened. Avron keeps the lead dry and uses 16th-note delays on stacks. Scheps' vocals sound "bone dry" but carry slap ~110 ms + short plate + pitch-shifted stereo delay.

**The modern refinement — ducking:** Bainz sidechains the ¼-note delay's compressor to the vocal so echo only blooms in gaps; Cervini ducks reverb/delay buses under the lead; Kirkpatrick's Saturn sidechain "erases the delay" when the vocal returns. Space that never fights the word.

Exceptions are deliberate and artist-specific: Post Malone wants anthemic reverb (Bell), Manny Marroquin contrasts dry verse / washy hook to "control the listener's mind."

### 8. The vocal is louder than you think

Kesha Lee turns the **beat down 1–2 dB** so Uzi sits on top. CLA: "vocals are the star." Cervini: "the vocal is king… it sits right on top of everything." Hawkins: drums and vocals are the two pillars. This is also the entire rage-mix consequence: F1lthy's beats are clipped walls, so the vocal must ride *above* a near-clipping instrumental.

### 9. One chain per section, not one chain per song

Lancaster chops the lead across tracks with different processing per section. Jaycen: "When he changes his tone, the EQ has to change." Avron keeps separate verse/chorus EQs (verse gets +8.4k to match the chorus register). Manny: dry verse, washy hook. If your delivery changes between verse and hook, your chain should too.

### 10. FX throws are a separate craft — and they're the last step

Bainz's Vox Throw folder: ~15 pre-built 100%-wet effect tracks ("monster voice," "wide chorused double," "short room burst"); for one special word he duplicates the audio onto a throw track — "this is one of the last things I do in the entire process." Gudwin prints delays to audio and hand-nudges them to the feel. Hawkins automates tape-echo feedback/pan live on the hook. Finneas chops vocals with zero-smoothness tremolo. The pattern: **the static mix is finished first; ear candy is placed surgically after.**

### 11. The rough mix is the contract

Jaycen demands the rough 3 days early and studies it. Leslie imports the rough *into the session* and locks onto what the client loves. Marroquin builds from faders-at-zero while checking the rough. Mike Dean: "I stay very true to the demo." For a self-recording artist the translation is: **your monitor-while-recording sound is your rough — get it exciting in the headphones first** (see pattern 13).

### 12. Speed is a feature, not a compromise

Leslie: "The songs I spend the least amount of time on sound the best" (3-hour rap mixes). Mike Dean mixes fast, revises in 30-minute passes. Kuk Harrell comps a Rihanna lead in ~90 minutes. Jaycen averages a record a day. Yeat records songs the day the beat arrives. Time-boxed decisions keep taste ahead of second-guessing.

### 13. The artist hears the finished vocal *while performing*

Uzi hears Auto-Tune in his headphones. Teezio tracks with HPF + VintageVerb + H-Delay in the cue. Chris Brown's Auto-Tune is printed because the performance is shaped *through* it. Louis Bell: a vocalist who feels "immortal and untouchable" in their headphones performs more openly. Your monitor chain *is* part of the vocal sound — it changes the takes you get.

### 14. Restraint is the endgame

Mike Dean: "Stop overmixing" — beats arrive already EQ'd/compressed; leave them. Serban Ghenea: "I really have no bag of tricks… the song dictates what you need to do." Kinelski: "Sometimes mixing involves literally doing nothing." Finneas: "The less stuff you have, the easier it is to make music." Every Bainz plugin is "doing very minor things." The chains look long; the *moves* are small.

---

## Where the legends disagree (so you can choose deliberately)

| Question | Camp A | Camp B | Your decision rule |
|---|---|---|---|
| Tuning | Printed, audible Auto-Tune (Teezio, Kesha, Dean, rage scene) | Invisible Melodyne (Kuk, Gudwin, Kirkpatrick) | Melodic/rage → A. Natural/emotional rap → B. Both tune *early* |
| Compression total | Barely-there stages (Kinelski, Bell) | 15–20 dB pummel (CLA, Lancaster) | Polished → A. Aggressive/rock-tinged → B |
| Templates | Fixed routing + palette, settings per song (Kesha, Teezio, CLA, Hawkins) | Anti-template (Dean: "I start with the session as it comes"; Serban) | Build a fixed *routing* template; never save *settings* as gospel |
| Analog vs ITB | Analog capture + desk (Ali, Marroquin, Dean) | 100% in the box hits (Serban, Teezio, Scheps, Gudwin) | Irrelevant to you: every ITB camp has Grammys. Capture-side discipline is what transfers |
| Reverb on rap | Never (Jaycen) | Sometimes, as contrast (Manny, Bell) | Default no; use as a *section* effect |

## Patterns specific to your lane (rage/plugg/underground, 2021–2026)

Verified behavior from `cs/02-new-wave-rap/`, with honesty labels intact:

1. **Self-recording is the norm, not the exception** — Yeat records/engineers/mixes himself; wifiskeleton built a catalog on BandLab then FL Studio; Lucki finishes albums alone. The pros in lane 01 are *references*, not gatekeepers. (A-tier: FADER, Guardian)
2. **Auto-Tune is the instrument, monitored live** — the one fully documented underground chain (Kesha/Uzi) confirms it. (A-tier: SoS)
3. **The vocal sits *above* a damaged beat** — F1lthy's documented method is soft-clipping the whole instrumental bus; the vocal convention that survives on top is loud, dry, tuned, and doubled. (A/B-tier for the beat; C-tier for exact vocal numbers)
4. **Volume of output is part of the sound** — 24-hour beat-to-song turnaround (BNYX/Yeat), two-week albums (Bladee's *Cold Visions*). Iteration speed replaces polish. (A-tier)
5. **Closed-loop sessions** — Carti/Lucki record with only the engineer hearing; the playback is a controlled reveal. Solo translation: finish the song before you A/B it to death. (B-tier)
