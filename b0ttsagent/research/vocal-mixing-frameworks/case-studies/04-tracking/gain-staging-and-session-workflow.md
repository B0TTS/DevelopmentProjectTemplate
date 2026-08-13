# Gain Staging & Session Workflow (Recording Levels, Headroom, Templates, Organization)

- **Lane:** Recording / Tracking — documented levels, headroom conventions, session architecture, and templates from engineers on mainstream records
- **Anchored in:** Sound On Sound technical guidance; Noah "40" Shebib (Drake 'Headlines' session); Bainz (YSL recording template); Thomas "Tillie" Mann (QC/Lil Baby); Kuk Harrell (vocal session structure); Finneas (bedroom studio normalization)
- **Evidence base:** A-tier: SOS (gain-staging Q&A; Inside Track articles; Kuk Harrell feature; Melodyne feature). B-tier: Mixonline (Take Care; Finneas). C-tier: none used for core claims.

## Why This Matters

The documented pro pattern is: **capture a healthy signal with generous headroom, keep every session organized the same way, and let the template carry the speed.** Levels are boring — that's the point. Every engineer profiled in this lane runs a rigid, repeatable session system so that the *music* decisions (not the tech) take the time.

## Documented Level Standards (SOS, A-tier)

- **Recording:** "you need to ensure you're capturing a healthy signal (relative to the noise floor) without clipping your interface's converters. Ensuring the peak signals hit around -6dBFS will certainly do that… as long as you're recording through 24-bit conversion (never mind 32-bit), you don't need to sail so close to clipping."
- **The -18dBFS figure:** "would refer to an average (RMS) level, rather than the peak… this leaves almost as much headroom as professional analogue gear does."
- **Practical meter discipline:** set DAW meters to RMS/VU with 0VU calibrated at -18dBFS (or -20/-16 — "it doesn't much matter which figure you pick as long as you're consistent"), with a peak LED at -6dBFS. [SOS, https://www.soundonsound.com/sound-advice/q-should-gain-stage-6dbfs-or-18dbfs]
- **Inside the DAW:** floating-point means no clipping internally; the real reasons to stay disciplined are that meters stay meaningful, plugin A/B comparisons stay honest, and analog-modeled plugins (threshold-based, nonlinear) respond to input level the way their hardware did. [SOS, ibid.]

**Kuk Harrell on recording resolution:** "From there I go straight into Pro Tools, if possible at a higher resolution, because it is where we are right now. I can hear the difference." [SOS, https://www.soundonsound.com/people/kuk-harrell-vocal-producer?page=2]

**40 on fidelity:** "I want it as clean as humanly possible." He also explains why bit-depth matters coming in: producer beats arriving as 16-bit files get run through analog gear at Metalworks "to give these files more feel and life, and I then track them back into Pro Tools at 24/44.1. You can upgrade a 16-bit file to 24 bits in the computer, but this doesn't add anything." [SOS, https://www.soundonsound.com/techniques/noah-40-shebib-recording-drakes-headlines]

## Documented Session Architecture (the templates)

### Bainz's YSL recording template (rap, A-tier)
"Essentially the template is built for speed and low latency. It's got two record tracks, with Antares AutoTune, a playlist track, a bunch of vocal audio tracks, and a dozen aux effects tracks. A lot of the stuff gets removed when we move into the mix world." [SOS, https://www.soundonsound.com/techniques/inside-track-young-thug-gunna-ski]

Plus (Live with Matt Rad): the artist *knows* the template — "Thug knows exactly how to get around on the template… He needs to have control over it so that he can execute his crazy ideas himself"; Thug "likes to duplicate playlist instead of making new playlists on every take." [https://www.livewithmattrad.com/episodes/51]

### 40's 'Headlines' session (rap/pop, A-tier)
"The 'Headlines' session is meticulously organised, starting with a stereo track at the top containing Boi-1da's original backing, then 10 drum tracks… six 40 synth tracks, a drum master track, 12 Drake vocal tracks and one Divine Brown vocal track, a Drake vocal master track and the same for Divine Brown, four aux tracks, a general vocal master track and a general music master track, and the final stereo master. In total, there are only 37 audio tracks." [SOS, https://www.soundonsound.com/techniques/noah-40-shebib-recording-drakes-headlines]

Key workflow facts from that session:
- **Latency compensation by hand:** "I noticed that Auto-Tune was giving me 1380 samples of latency on every track it was on, so I compensated for that by hitting my great friend Alt-H… and moving all the vocals 1380 samples earlier." [SOS, ibid.]
- **One vocal chain for the whole song, committed early:** "a single processing chain was used for the entire lead vocal on 'Headlines'" — because "the vocal chains we use [mean] Drake's vocals are in pretty good shape by the time the recordings are done… the records are nearly finished" by the time mixing starts. [SOS, ibid.]

### Tillie's organization doctrine (trap, A-tier)
"The first thing my assistant and I do when we get a session in to mix is organise everything… Many records are not recorded to a grid, so we put everything in tempo, and then line it up to the grid. We also label and colour-code everything. Organisation is the biggest thing for me. If there's clutter all over the place in a session, I can't work with it." And templates transfer between engineers: Mattazik "actually used one of my templates, which made mixing easier." [SOS, https://www.soundonsound.com/techniques/inside-track-lil-baby-sum-2-prove]

### Kuk Harrell's vocal-session structure (pop, A-tier)
- Record start-to-finish, one pass through the song; "If everything is going great, you should be able to cut the lead vocals in an hour and a half." [SOS, https://www.soundonsound.com/people/kuk-harrell-vocal-producer?page=2]
- Monitor chain is part of the workflow: EQ (Renaissance 6-band), compressor, "a Renaissance Reverb medium hall reverb, and Digirack Mod Delay a quarter note/half note ping-pong delay. That is for monitoring, to give it space in the headphones… The artist is hearing exactly what I'm hearing in the room, so they feel like they are in the record." [SOS, ibid.]
- Post-session: "I start with timing… After that I tune." Then a rough mix goes to the mix engineer — the vocals arrive finished: "When I send the session to the mix engineer, the vocal sound is what it is supposed to be." [SOS, ibid.]

## Home Setup Translation

1. **Record at peaks around -6 dBFS, average around -18 dBFS RMS.** In Audacity: keep the waveform peaking between -12 and -6 dBFS; never let the red clip. 24-bit means you have room to spare — no need to record hot.
2. **Set a consistent "0VU" mental reference:** your vocal fader should sit where the average level reads around -18 dBFS on a meter; check with the free Youlean Loudness Meter or your DAW's RMS meter.
3. **Build Bainz's template** in any DAW (Audacity included, adapted): 2 record tracks, 1 playlist/comp area (Audacity: separate takes on separate tracks, or the Take system in Reaper/Logic), 4-6 vocal layer tracks, 4 aux effect tracks (reverb, delay, de-ess, parallel comp). Same order every session.
4. **Commit early, like 40:** bounce your vocal chain (tuning → EQ → comp) to audio once it sounds right, so mixing later is fast and CPU-light.
5. **Organize like Tillie:** label every track with the same naming scheme every time ("Vox Lead", "Vox Double 1", "Adlibs", "Vox FX Reverb"), color-code, and align everything to a grid if your DAW has one.
6. **Check plugin latency:** if your tuned vocal sounds slightly late, nudge the clip earlier (40's 1380-sample trick — Audacity can nudge via time shift).
7. **Monitor yourself like a record:** put a light reverb + delay on your monitoring path (in Audacity: real-time effects via the Playback Effects chain, or just record dry and render a "headphone mix" aux). Dry vocals make singers over-sing and over-tune.

## Direct Quotes

- "Ensuring the peak signals hit around -6dBFS will certainly do that… you don't need to sail so close to clipping." — SOS Reviews Editor Matt Houghton [https://www.soundonsound.com/sound-advice/q-should-gain-stage-6dbfs-or-18dbfs]
- "Essentially the template is built for speed and low latency. It's got two record tracks, with Antares AutoTune, a playlist track, a bunch of vocal audio tracks, and a dozen aux effects tracks." — Bainz [https://www.soundonsound.com/techniques/inside-track-young-thug-gunna-ski]
- "Organisation is the biggest thing for me. If there's clutter all over the place in a session, I can't work with it." — Tillie [https://www.soundonsound.com/techniques/inside-track-lil-baby-sum-2-prove]
- "I want it as clean as humanly possible." — 40 [https://www.soundonsound.com/techniques/noah-40-shebib-recording-drakes-headlines]
- "I start with timing. It's all based on feel… After that I tune." — Kuk Harrell [https://www.soundonsound.com/people/kuk-harrell-vocal-producer?page=2]

## What To Steal

1. -6 dBFS peak / -18 dBFS RMS while recording; never chase hot levels in 24-bit.
2. One template, every session — Bainz's structure (2 record + playlist + layers + 12 aux) scaled down to your DAW.
3. Vocal chain committed before mixing starts (40: vocals "in pretty good shape by the time the recordings are done").
4. Comp as you go — never re-record what you already comped (Kuk's momentum rule).
5. Hand-nudge latency issues instead of ignoring them (40's 1380-sample fix).
6. Print/freeze heavy plugins; keep the tracking session light (Bainz).
7. Monitor with reverb/delay so the singer performs, not just sings (Kuk).
8. Keep a "master" vocal bus and a "master" music bus from day one (40's Headlines routing: all vocals to one bus, drums+music to another).
9. Write down your chain settings per session — recall beats memory.
10. Record 24-bit/44.1 or higher; never bounce a 16-bit file "up" to 24 and call it improved (40).
