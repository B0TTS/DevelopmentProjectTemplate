# Glossary — Terms Used Across the Research

**Purpose:** lookup while reading the case studies. Grouped by stage of the workflow; one line per term, defined the way engineers in this research use it.

## Recording

- **Gain staging** — setting each level in the path so nothing clips and nothing is buried; at recording, peaks ~−6 dBFS
- **Headroom** — the gap between your signal's peaks and 0 dBFS (digital maximum); leaving it = safety + room for processing
- **dBFS** — decibels relative to digital full scale; 0 is the ceiling, everything lives below it
- **Clipping** — exceeding 0 dBFS (digital distortion). Bad on your vocal input; *deliberately* used on rage beats (F1lthy)
- **Proximity effect** — directional mics boost low frequencies when you get close; warmth or mud, your choice
- **Plosive** — the air blast from P/B consonants hitting the capsule; pop filters exist for this
- **Sibilance** — harsh S/T/SH energy, lives roughly 4–8 kHz
- **Punch-in** — re-recording a small section mid-take instead of doing another full pass
- **Print (commit)** — recording/rendering an effect permanently into the audio, e.g. Teezio prints Auto-Tune
- **Clip gain** — turning a clip itself up/down before any plugin; editing with gain instead of compression
- **2-track** — a beat as a single stereo file (your MP3 instrumentals are 2-tracks)

## Pitch

- **Retune Speed** — Auto-Tune's core knob: how fast notes snap to target. ~0–5 ms = robotic (T-Pain/rage); Uzi sits 5–12; 20–80 ms = natural
- **Humanize** — lets sustained notes drift naturally while fast notes still snap; lowers the "robot" artifact at slow retune speeds
- **Formant** — the "throat size" character of a voice; shifting it down = bigger/darker (Little AlterBoy's trick) without changing pitch
- **Graph mode / manual tuning** — note-by-note surgical pitch editing (Melodyne's style), vs. real-time automatic

## Dynamics

- **Ratio / attack / release** — how hard / how fast in / how fast out a compressor works. 1176-style = fast everything
- **Gain reduction (GR)** — how many dB the compressor is pulling down; "1–3 dB GR" = gentle, "15–20 dB" = CLA's pummel
- **Opto vs FET vs VCA** — compressor flavors: opto (LA-2A/CL-1B) = smooth/slow, FET (1176) = fast/aggressive, VCA (SSL bus) = clean glue
- **Staged/serial compression** — 2+ compressors in a row each doing a little (Teezio's signature)
- **Parallel compression** — blending a crushed copy under the untouched signal (Scheps' Rear Bus; Ali's VOG trick on 808s)
- **Multiband compression** — compressing only chosen frequency bands (Waves C6: tames 100–500 Hz buildup only when it happens)
- **De-esser** — a compressor that only hears the sibilance band
- **Sidechain ducking** — plugin B turns down whenever signal A plays; Bainz's delay only blooms when the vocal stops

## EQ

- **HPF / low-cut** — high-pass filter: removes everything below a frequency (vocals: 70–100 Hz)
- **Shelf vs bell** — shelf tilts everything above/below a point; bell boosts/cuts a zone
- **Mud zone** — ~200–500 Hz, where boxiness lives (Kesha dips 200 + 500; Ali dips 300)
- **Harsh zone** — ~2–5 kHz, where aggression/ear-fatigue lives (Manny cuts 3k on the 2-bus)
- **Air** — 8–16 kHz+; the expensive-sounding sheen (Ali's +8k bell, Kirkpatrick's +12k)
- **Dynamic EQ / Soothe-style** — EQ cuts that only engage when the frequency gets loud; the modern cleanup tool
- **Sweep-solo** — boosting a narrow band and sweeping to *find* a problem frequency before cutting it

## Space & FX

- **Insert** — effect directly on the channel (the whole signal passes through)
- **Send / aux** — a copy of the signal routed to a shared effect; the lead stays dry, the wet return blends in
- **Plate / hall / room** — reverb flavors: plate = smooth bright metal plate emulation; hall = big space; room = small space
- **Slap** — a single short delay repeat (~80–110 ms); depth without wash (Scheps, Manny)
- **Predelay** — gap between the dry vocal and reverb onset; keeps words clear inside reverb
- **Throw** — a one-off effect on a single word/phrase, printed on its own track (Bainz's Vox Throws)
- **Ping-pong delay** — repeats alternating left/right

## Workflow

- **Comp** — the best-of edit assembled from multiple takes; also the verb
- **Double** — a second full performance layered with the lead (not a copy — a new take)
- **Stack** — the full vocal arrangement: lead + doubles + harmonies + ad-libs
- **Ad-lib** — the reactive background vocals ("yeah," "what," echoes of line endings)
- **Rough mix** — the artist/producer's working balance; pros treat it as the contract
- **Stem** — a rendered group (vocal stem, beat stem) for handoff
- **Vocal rider / clip automation** — automatic or manual micro-fader moves keeping every word audible
- **Mix bus / 2-bus** — the stereo channel everything sums into
- **Mono check** — listening summed to mono (Ali's Auratone) to test if the vocal survives phones/clubs
