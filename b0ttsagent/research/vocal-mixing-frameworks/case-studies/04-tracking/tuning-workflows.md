# Tuning Workflows (Auto-Tune vs Melodyne — Documented Practice: Who Tunes, When, and At What Settings)

- **Lane:** Recording / Tracking — documented pitch-correction practice: live-vs-post, retune speeds by genre, tuning order in the chain, per-artist documented approaches
- **Anchored in:** Kuk Harrell (pop vocal production), Noah "40" Shebib (Drake), Mike Dean & Anthony Kilhoffer (Kanye/Travis), T-Pain (the canonical Auto-Tune artist), Antares official documentation, Sound On Sound (Melodyne feature; Kuk feature; 'Headlines')
- **Evidence base:** A-tier: Antares official guides, SOS (Melodyne feature; Kuk Harrell; Headlines), MWTM #142 (Kanye chain). B-tier: Billboard (T-Pain/Kanye), The FADER (Mike Dean), MusicRadar (808s), Mix With The Masters. C-tier: blog "Travis Scott settings" claims (explicitly labeled).

## Why This Matters

There are two documented philosophies, and knowing which one a record used tells you how to set your own knobs:
1. **Live/creative tuning** — Auto-Tune running while the artist sings (retune fast, effect audible): T-Pain, Kanye's 808s-era sound, Travis Scott's melodic style, and Young Thug's tracking template.
2. **Post/transparent tuning** — vocal producer fixes pitch after comping with Melodyne-style tools (retune slow or manual, effect inaudible): Kuk Harrell's pop process, most mainstream pop/R&B leads.

Both are documented with exact practice below.

## The Two Tools (official documented behavior)

- **Retune Speed (ms)** is "the single most important control in any pitch correction plugin": 0 ms = instant hard-tuned correction ("the effect you know from T-Pain and Cher"); 10–50 ms = transparent; for natural results, "use a slower Retune Speed (20 to 80 ms), enable Flex Tune, and set Humanize to a moderate value." For the effect: "set Retune Speed to 0-5 ms, disable Flex Tune, and keep Humanize at zero." [Antares, https://www.antarestech.com/blog/pitch-correction-the-complete-guide-to-tuning-vocals]
- **Auto Mode vs Graph Mode:** Auto Mode = real-time, for tracking sessions/live; Graph Mode = surgical note-by-note post work. [Antares, ibid.]
- **Placement:** "always place your pitch correction early in the signal chain, on your raw, unprocessed performance" — reverb, noise, or aggressive compression degrades pitch tracking. [Antares, ibid.]
- **Key/scale first:** wrong key setting "will move notes to the wrong target pitch"; detuned beats need the plugin's transpose/detune matched to the beat's actual tuning. [Antares, ibid.]

## Documented Per-Artist Practice

### T-Pain — live, on the way in (the origin)
- T-Pain's signature is "the T-Pain effect," achieved through Auto-Tune [Berklee, https://www.berklee.edu/news/berklee-now/t-pain-effect-about-much-more-auto-tune]
- His documented criticism of Kanye proves his own method: "Kanye uses it, but he doesn't use it correctly… You don't know how it's going to come out. You can't catch your mistakes before they happen. So sometimes it gets a little wobbly." — i.e., T-Pain performs *through* Auto-Tune live (catching mistakes as they happen); Kanye adds it after the fact. [Billboard, https://www.billboard.com/music/music-news/t-pain-kanye-west-auto-tune-6296959/]
- Retune implication: for the audible effect, 0–5 ms per Antares' own docs. [Antares, https://www.antarestech.com/blog/pitch-correction-the-complete-guide-to-tuning-vocals]

### Kanye West — Auto-Tune as a sound, mandated
- On 808s & Heartbreak (2008): "Reports suggest that the majority of the tracks… make heavy use of Antares Auto-Tune"; Mike Dean confirmed Kanye "fell in love with the Auto-Tune" while working on Lil Wayne/Jeezy remixes. [MusicRadar, https://www.musicradar.com/news/tech/kanye-west-loves-auto-tune-808-sounds-and-naked-girls-177589]
- The documented "Runaway" lead-vocal chain places Auto-Tune Pro *in the tracking/processing chain* (with Waves C1 Gate, SansAmp PSA-1, McDSP E606, 6-band EQ, reverbs/delays). [MWTM #142, https://mixwiththemasters.com/videos/jeff-bhasker-anthony-kilhoffer-kanye-west-runaway]
- Mike Dean's rule for setting Auto-Tune correctly: "it does help to be able to figure out what key a song is in… so you can set your Auto-Tune right. So many songs with Auto-Tune are off or have the wrong note playing on the 808." [The FADER, https://www.thefader.com/2018/10/08/mike-dean-interview-travis-scott-and-kanye-west]

### Travis Scott — live effect, settings NOT publicly documented
- Documented: Auto-Tune-forward vocal sound; Dean mixes his vocals with wide dynamic range as the centerpiece [Lincoln blog documenting Dean's Twitter thread, https://wmlaudioproject1.blogs.lincoln.ac.uk/2017/10/20/researchmike-deantravis-scott-production/]; Ca$hpassion keeps tuning light on singers like Don Toliver ("Too much AutoTune would be bad for someone like Don. You have to keep that light.") [Billboard, https://www.billboard.com/music/rb-hip-hop/cashpassion-travis-scott-interview-9341515/]
- C-tier, unverified: blog posts claiming "Travis uses retune speed 0–5 ms / 5–15 ms / 20–40 ms" contradict each other — no primary source states his retune number. Do not cite these as fact. [e.g. https://vocalpresets.com/blog/travis-scott-vocal-chain; https://devicemag.com/which-autotune-does-travis-scott-use/]

### Young Thug / trap — Auto-Tune in the recording template
- Bainz's tracking template has Auto-Tune on the record tracks ("two record tracks, with Antares AutoTune") — correction happens live while tracking, before the comp is even made. [SOS Ski, https://www.soundonsound.com/techniques/inside-track-young-thug-gunna-ski]

### Drake — post-tracking, in the box, even on raps
- 40 (on 'Headlines'): "Nine of Drake's 12 vocal tracks, as well as Divine Brown's vocal track, had Auto-Tune on them. On this record I actually tuned the raps! Drake raps in a very melodic way… I therefore hit it with some Auto-Tune to centre the pitch a little bit. If I left it off, I'd be surprised if many people would notice. It's just a bit of pitch-correction." [SOS, https://www.soundonsound.com/techniques/noah-40-shebib-recording-drakes-headlines]
- Auto-Tune's latency was real enough that 40 hand-compensated 1380 samples per track. [SOS, ibid.]

### Kuk Harrell / pop — post-comp transparent tuning, Melodyne preferred
- Edit order: timing first, then tune; "The final version may have Melodyne, if it needs it. For me, Melodyne sounds more natural than Auto-Tune. It's not as jerky and you can dial in the bends and stretch things and make things pitch-perfect, if that is what the record calls for. I've done many records with Auto-Tune, but the way I do it, it does not have that Auto-Tune sound." [SOS, https://www.soundonsound.com/people/kuk-harrell-vocal-producer?page=2]
- Vocals arrive at the mixer already tuned: "When I send the session to the mix engineer, the vocal sound is what it is supposed to be." [SOS, ibid.]

## The Documented Post-Tuning Workflow (SOS Melodyne feature, A-tier)

1. **Dedicated tuning project** separate from the mix session (keeps resources free; keeps tuning recallable). Import vocals + "a rough instrumental mix of the song… it provides the context you need."
2. **Pitch Grid: 'No Snap'** — "sometimes moving a note ±15 cents sharp or flat of the 'perfect' pitch can make all the difference."
3. Split notes with the Note Separation tool so bends aren't flattened ("to prevent these nuances of performance from being lost").
4. Correct Pitch Centre + Drift at 100% as a starting point, then hand-tune details.
5. **Print the tuned result to audio** as insurance — "it's good to know that the vocal line you've just laboured over is saved as audio."
6. Listen in context for artifacts; subtle is the goal unless the effect is the point. [SOS, https://www.soundonsound.com/techniques/pitch-correcting-vocals-melodyne]

**Tuning before or after compression:** documented answer — before. Antares: pitch correction first in the chain on a clean signal; Kuk tunes before his rough mix; the Melodyne workflow operates on raw captured audio in a separate project. Compression comes after, in the mix chain. [Antares, https://www.antarestech.com/blog/pitch-correction-the-complete-guide-to-tuning-vocals]; [SOS Melodyne, https://www.soundonsound.com/techniques/pitch-correcting-vocals-melodyne]

## Home Setup Translation

1. **Decide which record you're making.** Melodic-rap/T-Pain/Kanye-style: Auto-Tune-type plugin live on the record track, retune 0–5 ms, key set to the song's key (free: MAutoPitch, GSnap, FL Pitcher, Logic Pitch Correction). Transparent pop: record clean, tune after comping with Melodyne-style manual editing (free DAW stock tuners; Melodyne Essential if budget allows).
2. **Set the key first — always.** Wrong key = worse than no tuning (Dean's rule, Antares' #1 mistake).
3. **Check the beat's actual pitch:** many beats are detuned; match Auto-Tune's transpose to the beat or retune the beat (Antares documented fix).
4. **Tune before any compression/reverb.** Clean signal in → tuned → then compress.
5. **Tune in a copy of the project** (Kuk's edit order + SOS's separate tuning project), then print audio.
6. **Nudge timing first, then pitch** — Kuk's fixed order; you can't tune what's rhythmically wrong.
7. **For natural results: 20–80 ms retune + Flex Tune + Humanize**; for the effect: 0–5 ms, no Flex Tune (official Antares numbers).
8. **Don't over-correct great takes** — Antares: "If you find yourself needing to over-correct, you're usually better off tracking a new take."
9. **Rap vocals get tuned too** (40 tuned Drake's raps "a little bit") — melodic rap needs centering, not effect.
10. **Learn your key/scale theory** — Dean: setting Auto-Tune right requires knowing the key; "so many songs with Auto-Tune are off."

## Direct Quotes

- "A setting of 0 ms produces instant, hard-tuned correction, the effect you know from T-Pain and Cher. A setting of 10 to 50 ms gives the correction time to smooth in naturally." — Antares [https://www.antarestech.com/blog/pitch-correction-the-complete-guide-to-tuning-vocals]
- "You can't catch your mistakes before they happen. So sometimes it gets a little wobbly." — T-Pain on adding Auto-Tune after singing (vs. his own live method) [Billboard, https://www.billboard.com/music/music-news/t-pain-kanye-west-auto-tune-6296959/]
- "On this record I actually tuned the raps!" — 40 [SOS, https://www.soundonsound.com/techniques/noah-40-shebib-recording-drakes-headlines]
- "For me, Melodyne sounds more natural than Auto-Tune. It's not as jerky…" — Kuk Harrell [SOS, https://www.soundonsound.com/people/kuk-harrell-vocal-producer?page=2]
- "It does help to be able to figure out what key a song is in… so you can set your Auto-Tune right." — Mike Dean [The FADER, https://www.thefader.com/2018/10/08/mike-dean-interview-travis-scott-and-kanye-west]

## What To Steal

1. Choose live-effect vs post-transparent tuning deliberately — they're different workflows.
2. Retune 0–5 ms for the effect; 20–80 ms + Flex Tune + Humanize for transparent (official numbers).
3. Key and scale before anything else; verify the beat's tuning.
4. Tune early in the chain, on clean audio, before compression.
5. Tune after comping and timing edits (Kuk's order).
6. In Melodyne: No Snap, split bends, ±15-cent finesse, 100% centre/drift as start, print results.
7. Pop lead vocals get transparent tuning; rap vocals get "centering" (40: "just a bit of pitch-correction").
8. Don't rescue bad takes with tuning — re-track instead (Antares).
9. Keep Auto-Tune latency in mind — nudge tracks if the tuned vocal drags (40's 1380-sample fix).
10. A vocal producer's job is emotion; tuning is the polish — Kuk: "I'm after a magical performance."
