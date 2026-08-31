# Phase 3 Synthesis — Scratch Notes

**STATUS: COMPLETE (2026-08-30).** Outputs written to research root: README.md (15.4 KB), recurring-patterns.md (43.5 KB, 21 patterns P1–P21 + claim-frequency table + 7-axis comparison matrix + single-creator tactics), source-library.md (29.9 KB, 15 creators). Verified: tom-scott/colin-and-samir/matt-davella appear in recurring-patterns.md only in the two exclusion statements (lines 5, 326), never as evidence.

Purpose: offload memory during synthesis. Section map + per-creator tactic extraction + source registry.
Hard rules: patterns need ≥2 slugs + specific source from each; 3 shortlisted creators (tom-scott, colin-and-samir, matt-davella) have NO case study — README ranking + source-library only, NEVER pattern tables.

## Section map (headings → line numbers)

| Doc | ~Lines | Key sections (line) | Sources @ |
|---|---|---|---|
| mrbeast.md | ~300 | 0 north star (11), 1 CTR/AVD/AVP (21), 2 CTR title+thumb (35), 3 first minute/5-10s (51), 4 minute-mark structure (68), 5 pacing quick cuts (99), 6 wow factor (111), 7 formats retention engines (121), 8 ideation+feasibility+critical components (137), 9 production system (149), 10 capture quantity (168), 11 retention editing (178), 12 cadence scaling (188), 13 replication/burnout (205), 14 audience info diet (230), 15 caveats (240), 16 own words (268) | 283 |
| mark-rober.md | ~185 | 1 north star visceral (11), 2 quality>quantity (23), 3 idea capture 1-3 sentence filter (33), 4 build-then-story (43), 5 edit rhythm story found in edit (57), 6 cadence pipeline is system (71), 7 burnout: treadmill/Super Mario/stay employed (83+), 8 what to ignore (114), 9 career (124), 10 caveats (134), 11 checklist (158) | 171 |
| airrack.md | ~360 | 1 mischief (13), 2 idea capture weekly mtg 3-thumb pitch (31), 3 identify & innovate + shoe swap (54), 4 buckets & branching follow-up (84), 5 A-plot=title (112), 6 hook front-loaded (132), 7 budget as filter (152), 8 one-day in-and-out production (177), 9 post: voice-note→Claude paper edit, editors as storytellers (218), 10 cadence/team humble era (242), 11 sawdust businesses (278), 12 stops documenting (298), 13 caveats (310), 14 checklist (328) | 346 |
| veritasium.md | ~250 | 0 element of truth (11), 1 PhD clarity vs confusion (21), 2 no intros/mystery hook (38), 3 problem→solution (56), 4 title+thumb promise not label (74), 5 edit rhythm/research backbone (97), 6 cadence solo→scaled (110), 7 burnout precariousness/hiring (130), 8 experimentation power laws (158), 9 career (184), 10 caveats (193), 11 checklist (221) | 237 |
| drew-gooden.md | ~250 | 0 do everything myself (13), 1 writing is work/slowest writer (27), 2 unscripted→script (45), 3 film/edit ~2 days plan-just-enough (65), 4 editing respect viewer time (79), 5 open "hey guy" not formula (117), 6 structure sitting yapping (127), 7 cadence 1/month (139), 8 solo replication (153), 9 caveats (193), 10 checklist (225) | 240 |
| kurtis-conner.md | ~310 | 0 Vine trauma (11), 1 scripting easy/topic-finding hard (19), 2 internet + audience idea pool (47), 3 hook right into it (63), 4 structure 20 min room→field (96), 5 editing blocks like writing (123), 6 thumbnails cottage industry (151), 7 cadence weekly→none stated (175), 8 business pies solo+thumbnail-dude (195), 9 burnout no codified system (219), 10 explicitly refuses (253), 11 caveats (263), 12 checklist (293) | 307 |
| johnny-harris.md | ~330 | 0 craftsmanship (11), 1 4-month pipeline (25), 2 team freelance remote (45), 3 idea capture story days (63), 4 packaging is a promise early (81), 5 hook drop into action (107), 6 structure history backbone (123), 7 two voices pace (139), 8 retention three legs no dashboard (154), 9 visual script = writing + coding (177), 10 edit rhythm frame-by-frame (194), 11 cadence/replication (234), 12 burnout constraints (252), 13 reps not template (267), 14 caveats (281), 15 checklist (311) | 328 |
| mkbhd.md | ~450 | 0 not the subject (11), 1 two buckets one script (29), 2 cadence 1.5/wk (51), 3 team octopus (73), 4 tooling Notion/GDocs/TickTick (105), 5 research live with device (139), 6 writing 90% written paragraph-read (171), 7 planning visuals cinematic intro (205), 8 shooting taste+skeleton (221), 9 open/hook Skillshare (237), 10 title+thumb half the story A/B (251), 11 structure length drift (277), 12 edit rhythm alternated editors (295), 13 retention thin dashboard (311), 14 burnout (324), 15 copy him voice over speed (352), 16 caveats (378), 17 checklist (413) | 431 |
| linus-tech-tips.md | ~400 | 0 cat herder factory (11), 1 17/wk calendar (21), 2 tooling tracker→monday.com Gantt (47), 3 writer's meeting greenlight (79), 4 script review Linus gate (91), 5 sponsor→teleprompter→ready-to-shoot (111), 6 shoot A/B-roll (131), 7 ingest→edit→pickup→QC (157), 8 open/hook (205), 9 Gantt is structure (217), 10 pacing scripted>vlog (232), 11 retention/editing/packaging (250), 12 cadence dial (267), 13 scaling factory (286), 14 burnout admissions (306), 15 caveats (337), 16 factory checklist (369) | 383 |
| wendover-productions.md | ~220 | 0 creative mass manufacturing (11), 1 cadence 2-weekly 11 yrs (21), 2 ideation no system (33), 3 solo→team virtuous cycle (49), 4 writers' room algo is boss (63), 5 pipeline research→script→animation→edit→fact-check (75), 6 pre-production is the job Jet Lag (87), 7 scaling no venture + Nebula why (115), 8 open/hook/structure/pacing (147), 9 cadence replication sustainable (161), 10 caveats (174), 11 checklist (202) | 214 |
| mina-le.md | ~250 | 0 fashion political if inspired (13), 1 ideas well-read follow threads (32), 2 research read-every-article JSTOR NYPL print-spread (54), 3 detailed script historical parallels (88), 4 editing meme-spliced density light hand-off (107), 5 packaging thin no doctrine (133), 6 cadence organic→systemized lightness (143), 7 burnout most explicit (163), 8 caveats (199), 9 checklist (228) | 243 |
| ryan-trahan.md | ~320 | 0 redemptive work filter (11), 1 thumbnails realism doctrine (25), 2 thumbnail-first reverse-engineer shoot (44), 3 idea factory 10 titles/day (62), 4 open/hook desk (80), 5 structure Double Arc repeatable segments (92), 6 pacing cut by feel (118), 7 pipeline iPhone GDoc Street View 5-person van (144), 8 cadence event vs bread-and-butter (172), 9 replication low overhead (204), 10 interactive/water-cooler TV (230), 11 caveats (264), 12 checklist (295) | 310 |

## Shortlist ranking (from working/shortlist.md — verbatim inputs)

dominance = 0.3×hit_rate + 0.5×hit_magnitude + 0.2×activity; ties → newer documentation recency wins.

1. MrBeast 1.0 (1.0/1.0/1.0) — median 111,467,670; 12/12; newest upload 7d
2. Mark Rober 0.9 (1.0/1.0/0.5) — median 28,199,830; 12/12; 70d
3. Airrack 0.894 (1.0/0.9885414/0.5) — median 9,885,414; 12/12; 33d
4. Veritasium 0.841 (1.0/0.6817628/1.0) — median 6,817,628; 12/12; 12d
5. Drew Gooden 0.735 (1.0/0.4698/1.0) — median 4,697,784; 12/12; 20d
6. Kurtis Conner 0.705 (1.0/0.4103/1.0) — median 4,103,208; 12/12; 15d
7. Johnny Harris 0.67 (1.0/0.3475773/1.0) — median 3,475,773; 12/12; 16d
8. MKBHD 0.654 (1.0/0.307/1.0) — median 3,071,970; 12/12; 5d
9. Linus Tech Tips 0.55 (1.0/0.1004889/1.0) — median 1,004,889; 12/12; 0d (8 excluded new uploads)
10. Wendover 0.543 (1.0/0.0859858/1.0) — median 859,858; 12/12; tie vs tom-scott broken by newer doc
11. Tom Scott 0.543 (1.0/0.0864985/1.0) — median 864,985; 12/12; 5d — NO CASE STUDY
12. Mina Le 0.527 (1.0/0.0530018/1.0) — median 530,018; 12/12; 3d
13. Ryan Trahan 0.516 (1.0/0.2323887/0.5) — median 2,323,887; 12/12; 42d
14. Colin and Samir 0.46 (0.833/0.0197541/1.0) — median 197,541; 10/12 — NO CASE STUDY
15. Matt D'Avella 0.428 (1.0/0.0556073/0.5) — median 556,073; 12/12; 53d — NO CASE STUDY

Formats: mrbeast spectacle challenge 10-20min; mark-rober science build 10-20min; airrack prank/challenge 15-25min; veritasium science essay 12-25min; drew-gooden commentary-comedy essay 15-30min; kurtis commentary-comedy 15-30min; johnny-harris geopolitics visual doc essay 15-30min; mkbhd tech review 12-20min; LTT tech explainer 10-25min; wendover logistics/geo/econ essay 10-20min; mina-le fashion/culture essay 20-45min; ryan-trahan travel/challenge 20-30min daily series.

## Per-creator extraction (fill during pass 2)

### mrbeast — sources: GUIDE=How to Succeed at MrBeast Production PDF 2024-09-15 FP/IND; LEX=Lex Fridman #351 2023-01-11 FP/MON; BI=Business Insider 2025-08-14 2H/MON
- Metrics triad CTR/AVD/AVP as virality definition [GUIDE]
- Title+thumbnail known before shoot — "critical components" [GUIDE]; title <50 chars, clear thumbnails [LEX]; ideation team sketches/log/pitch [BI 2nd]
- First minute = most loss; first 5–10 sec decide [GUIDE, LEX]
- Minute-mark structure; re-engagement content ~3min & ~6min; abrupt endings; never signal the end [GUIDE]
- Pacing: "quick scene changes and highly stimulating simple content" min 3–6 [GUIDE]
- "Wow factor" non-trackable metric — things no other creator can do [GUIDE]
- Formats as retention engines (last-to-leave, stair-stepping, chase); kill formats before saturation, no back-to-back same format [GUIDE]
- Ideation: daily study of most-viewed videos as pattern training [LEX]; feasibility gate before production [GUIDE, BI 2nd]
- Capture quantity-over-quality, "video everything" [GUIDE + BI 2nd]
- Editing = retention editing, minute-mark discipline; kill weak cuts even after investment [GUIDE, LEX, BI 2nd]
- Cadence: weekly ambition (guide/lex) → measured 1–2 longform/mo 2025 [BI 2nd]
- Work on multiple videos every day (anti-snowball) [GUIDE]
- Recharge/decompress counterweight + unemotional flop post-mortems [LEX]
- Obsessive YouTube consumption / information diet ("can't get inspired by things you don't know exist") [GUIDE, LEX]
- Budget: "creativity saves money"; >$10k spend should show on camera [GUIDE]
- Brand deals integrated as content to protect retention [GUIDE]
- Backup days; consultants for novel builds [GUIDE]
- Scaling: train/promote internally vs importing media execs [LEX]
- Sources (3): GUIDE, LEX, BI — exactly the 3 in shortlist

### mark-rober — sources: TED=TED WorkLife transcript 2026-06-02 FP/IND; CS=Colin and Samir "Full Story" 2022-12-07 FP/MON; VPD=Video Production Daily podcast 2021-04-03 FP/IND; LI=LinkedIn Samir Chaudry 2022-12-12 2H corroboration-only
- North star: evoke a visceral response; novelty as route [TED, CS]
- Idea filter: pitch in 1–3 sentences ("dope" test) [CS]
- Quality over quantity — ~10/yr, anti-algorithm/anti-trend [TED, VPD]
- Parallel pipeline: 9–10 videos in flight, ~1yr each idea→publish [CS]
- Build-then-story: shoot with general bullet points, film whatever happens, FIND STORY IN EDIT, film intro LAST to match actual outcome [CS]
- Never outsource story/edit; ~200 hours footage → 10-min video is the core job [CS, VPD]
- Burnout: treadmill/jog-not-sprint [CS, TED]; Super Mario Effect (gamify failure, cheap retries) [CS]; stay employed until 10M subs, self-fund, low friction/low overhead [TED, CS, VPD]
- Explicit refusals: no parasocial community, no TV deal at cost of channel discovery [TED, VPD]
- Sources (4): TED, CS, VPD + LI (2H, corroborates) — case study adds LI beyond shortlist 3

### airrack — sources: COMEBACK=Youshaei "Greatest Comeback" 2025-10-14 FP/MON; PRANK=Youshaei "Biggest Pranks Breakdown" 2025-12-23 FP/MON; FORBES=Forbes Youshaei 2022-05-29 2H/MON verification-only; +Wikipedia/YT/HR×2 verification-only
- One-word brand filter ("mischief"); shoe-swapping test (what would MrBeast/Ryan do with same topic) [COMEBACK]
- Weekly pitch meeting; pitch = 3 thumbnails + breakdown + "how" (physical feasibility); self-eliminates 9/10 [COMEBACK]
- Identify & innovate: triangulate validated interest (3 data points), then "what's the Airrack version?" [COMEBACK]
- Buckets & branching: "if it doesn't have a follow-up, we're not making it"; series reps compound skills (retention graphs studied per iteration) [COMEBACK]
- A-plot = title; B-plots overrated/distracting [COMEBACK]
- Intro exponentially front-loaded — first second most important, 0–2 min earns viewer; tighter+representative intros [COMEBACK]
- Packaging: intros/thumbnails "more important than we thought last month"; use YouTube native A/B split testing [COMEBACK]
- Budget as filter: "more expensive usually a worse idea" (compensating for lack of brainstorm); speedboat not cruise ship; avoid fixed costs [COMEBACK]
- Production: one-day in-and-out shoot; producer on ground 4 days early [PRANK]
- Post: nightly voice note → Claude → scene-by-scene paper edit [COMEBACK]
- Editors = storytellers: mics+cameras at desk, temp VO while editing, Loom for overseas, editors on set [COMEBACK]
- Team: "grow only as fast as I can find great people"; appreciation as leadership job [COMEBACK]
- Cadence: "sickeningly focused" on weekly videos [COMEBACK]
- Sawdust businesses (monetize byproducts, no new nucleus) [COMEBACK]
- Sources: COMEBACK, PRANK, FORBES (workflow 2) + verification-only (Forbes/Wiki/YT/HR)

### veritasium — sources: FIRESIDE="Building Veritasium to 20M Subs" Fireside Lisbon 2026-02-27 FP/MON; FUTURE="The Future of Veritasium" 2025-12-24 FP/MON; PETER NELSON Short 2026-01-15 2H (cited only to exclude); ABOUT=veritasium.com/about FP/IND career baseline; TUBEFILTER 2026-01-06 2H/IND corroborate; SCIAM=Scientific American 2025-05-28 2H/IND corroborate
- Hook: "no intros" — straight into material; first 1–2 seconds decide (platform data) [FIRESIDE]
- Structure: problem→solution never solution→problem; NO thesis statement; narrative + reflection order [FIRESIDE]
- Title/thumbnail = the PROMISE of the video, not the label; ~50 chars; 20–50 thumbnail options, YouTube ABC test top 3; "asteroids" 10x title/thumb rework story [FIRESIDE]
- Misconception-first pedagogy (PhD thesis: misconception dialogue doubled accuracy; polished clear lecture = learned nothing + false confidence) [FIRESIDE, SCIAM 2H]
- Storyboard "like a movie studio," hand-drawn animation [FUTURE]
- Fact-check scaffolding: multiple experts per video + Patreon early-access review + legal review for high-stakes topics [FUTURE]
- Experimentation doctrine — "a no is more informative than a yes"; power laws, play for the 0.1% [FIRESIDE]
- Burnout vector = precariousness (not hours); diversify income; Electrify deal offloaded hiring/production/compliance [FUTURE, FIRESIDE]
- Main-channel output volume held constant; did NOT shorten videos while scaling [FUTURE]
- Solo early ("slowest editor"); 2021 small-team attempt raised hours (coordination overhead) before infra existed [FUTURE, FIRESIDE]
- Bootstrap lean: kept side teaching job, minimal equipment/travel spend [FIRESIDE, FUTURE]
- Sources: FIRESIDE, FUTURE (workflow FP) + PETER NELSON (excluded), ABOUT, TUBEFILTER, SCIAM

### drew-gooden — sources: PADILLA=Anthony Padilla "I spent a day with Drew Gooden" 2024-03-08 FP/MON; AI="using AI to write a youtube video" 2022-08-31 FP/MON own-channel; WASTE="Everybody wants to waste your time" 2024-09-22 FP/MON own-channel essay; WIRED=Autocomplete Interview 2022-05-16 FP; TRIANGLE=Triangle Talks 2019-09-11 FP/IND STALE (pre-window); NBC=NBC News 2022-01-18 2H w/ FP quotes
- Solo operation: "I do everything myself" — ideas, write, star, edit [PADILLA, WIRED]
- Writing is the work/bottleneck: ~couple weeks per script, "world's slowest writer," 7hrs/paragraph days [AI, PADILLA]
- Script-first (switched from unscripted rant that took 2 weeks to edit) — scripting kills repetition [PADILLA]
- Plan just enough → film+edit in ~2 days [PADILLA]
- Editing ethic: respect the viewer's time — don't pad runtime for algorithm; middle between unedited yapping and hyperactive overstimulation [WASTE]
- Anti-manipulation: names/rejects fake progress-bar retention tricks [WASTE]
- Cadence: 1/month with built-in recharge gap; overcommitting to brand deals → worse videos + burnout [PADILLA]
- Post-publish ritual: a couple days reading comments/feeling good before next [PADILLA]
- Burnout: be own parent/schedule (no boss); separate work/life; don't refresh analytics; "live a life to have something to say" / refill the cup; calibrate praise; expect plateau not infinite growth [PADILLA]
- Hook: "hey guy" catchphrase — explicitly NOT a retention formula [WIRED]
- Make what you wish existed, not trend drama [WASTE]
- Sources: PADILLA, AI, WASTE, WIRED (workflow) + TRIANGLE (stale), NBC, Wikipedia (verification)

### kurtis-conner — sources: CS=Colin and Samir "funny uncle" 2023-11-07 FP/MON (+Podmarized digest 2H); PADILLA=Anthony Padilla "Kurtis Conner effect" 2023-04-01 FP/MON; OWN×4 own-channel 2026 videos (Cameron Dallas 08-14, Time Machine 07-04, Russell 07-31, Performative Males 10-19) FP; BI=Business Insider 2020-02-09 2H w/FP quotes; TILT=The Tilt 2022-10-10 2H thin
- Scripting over improv — confidence from knowing what he'll say; does best work planning [CS]
- Topic-finding = hardest part, solo internet browsing; audience recommendations feed idea pool [CS, BI]
- Cut the front door: killed signature greeting to "get right into" topic; cold-topic hook + ≤10–20s promo bumper [CS + OWN videos]
- Length: "I want at least 20 minutes" ideal; commentary→field/documentary drift [CS]
- Editing = writing with blocks ("this would be funnier if this piece went over here"); YouTube edits/sound effects carry joke weight [CS]
- Thumbnails: ignored on Vine → breakout unlock (1k→600k overnight) → dedicated thumbnail collaborator ("cottage industry") [CS]
- Cadence: weekly while working full-time day job ("gnarly", 2am edits) → no stated schedule; touring reduces output [CS, BI]
- Team via friends/trust: shared manager (Danny/Drew), buddy producer, direct raise talks [CS]
- Burnout: NO codified system — platform trauma (Vine loss), self-doubt, upload anxiety explicit [CS]
- Self-funded independent special = ownership [CS]
- Algorithm: "the game you got to play" [CS]
- Sources: CS, PADILLA, OWN×4 (workflow) + BI, TILT (corroboration)

### johnny-harris — sources: PERELL="Why Every Johnny Harris Video Goes Viral — How I Write with David Perell" 2025-03-12 2H/IND (Johnny guest, verbatim); TEAM=Join The Team + subpages 2021 FP/IND; PATREON 2023 FP/MON (public preview); MAPS="How I Make My Maps" 2020-12-11 FP/MON (Intel #ad); MAPS2="How Johnny Harris makes his maps" 2025-08-29 FP/MON (Adobe #ad); ANIM="The secrets behind my animations" 2025-10-23 FP/MON (Adobe #ad); MUSIC="Why I Hired A Music Composer" 2023-02-28 FP/MON; ABOUT 2021 FP/IND stale; WIKIPEDIA verification; START 2018 early-career
- 4-month pipeline/video: story day → greenlight+reporting brief in Slack → researcher 3–4 wks → 60–80-page info doc → outline → scripting week (3–4 days) → production kickoff → cuts chain (shame cut→rough→fine→fine two→audio lock→picture lock, ~150 notes, Frame.io/GDocs) → thumbnail + ad slot → scheduled ~6 months ahead; ~30 videos/year [PERELL]
- Packaging defined EARLY as "the Billboard" — not the story: 2–3 packagings per decision, 7+ titles (how/why), comps via one-of-10/ViewStats, A/B test distinct directions [PERELL]
- Reinforce the promise within first minute; pay it off by the end [PERELL]
- Open with action + "look at this"; inviting "I want to show you" peer framing; rejects tell-them-what-you'll-tell [PERELL]
- Two voices pacing: explainer (who did what to whom, Pinker) ↔ contemplative/poetic ending [PERELL]
- Visual script = two-column GDoc; every sentence/row gets visual direction; color macros; fact-checks as citation comments → public source dock [PERELL]
- Retention triad: naturally interesting + visual + surprise; explicitly NO dashboard [PERELL]
- Fresh art direction per video (no channel branding package); art-ingredients tab → mood board via visual producer [PERELL]
- Custom music per video via full-time composer since 2018 [MUSIC]
- Sacred writing blocks 9am–2pm, 3 days/wk, no meetings/slack [PERELL]
- Output ceiling 30/yr (down from 48; 17 concurrent "sucked the magic"); embraces being the bottleneck [PERELL]
- Team: ~25 self-taught scrappy freelancers, remote; "don't hire from traditional TV" [PERELL, TEAM]
- Maps workflow: AE + Geolayers anchored null, keyframe lat/lng/zoom; rough-animate in AE to direct without words [MAPS, MAPS2, ANIM]
- Constraints sharpen; sprint-sprint-sprint-rest; December/summer breaks [PERELL]
- Sources: PERELL, TEAM, PATREON, MAPS, MAPS2, ANIM, MUSIC, ABOUT, START + WIKIPEDIA (verification)

### mkbhd — sources: CORTEX=Cortex #174 Relay FM 2025-12-12 FP/IND (+YT mirror); STRAT=Stratechery interview 2024-06-26 FP/IND; TWG=Think with Google 2025-09-01 FP/IND; SKILL=Skillshare class 2016-08-01 orig / 2021 S21 update FP/MON UNCLEAR currency
- "I am not the subject" — tech is subject = burnout insulation; three hearts never delegated (on camera, writing, reviewing) [STRAT, TWG]
- Two buckets: SEO searchers vs subscribers — write for the searcher, entertain the rest [STRAT]
- Cadence: ideal ~1.5/week; per-video 24h–1wk; "playoffs" — experiment Jan–Mar, lock Aug–Jan [CORTEX, STRAT]
- Team: creator = octopus → robotic octopus; delegate "arms" to specialists; 15→17 people; head of production as bird's-eye coordinator [STRAT, TWG, CORTEX]
- Tooling: Notion project stage-gate DB + Google Docs scripts (suggestions mode) + TickTick per-product notes; one open room, ad-hoc whiteboard; process changes batched annually [CORTEX]
- Research: "mainline the device" (SIM in day 1, live with it); anti-benchmark stance; charts used sparingly [CORTEX]
- Writing: 90%+ scripted; paragraph-read delivery (not teleprompter/line-read); 45–60 min A-roll → 12 min video; second set of eyes for numbers [CORTEX]
- Reviews almost completely scripted; experiential videos semi-scripted [STRAT]
- Packaging: title+thumbnail "at least half the story"; pair them as ONE idea (Q/A continuation); YouTube A/B/C thumbnail test w/ fixed title; must deliver or algorithm stops serving [STRAT, CORTEX]
- Timing: drop at 6:02 to top the 6:00 flood; two-video iPhone strategy (day-1 impressions + full review) [CORTEX]
- Structure: length drift 3–4 min → 9–14 min (TV sessions); arc-hunting (EVs/AI vs flat phone arcs) [TWG, STRAT]
- Editing: alternated editors + notes on last 20%; perfection vs cadence balance [CORTEX]
- Retention: no dashboard; comment-pulse after first 30 min as recommendation-audience proxy [CORTEX]
- Burnout: say no to 99% of offers; win-win-win filter for 1%; "what was the point of this video?" question filter [STRAT, TWG, CORTEX]
- Sources: CORTEX, STRAT, TWG, SKILL + verification (SocialBlade/Wikipedia/TIME/channel)

### linus-tech-tips — sources: W17=LTT Forum "How We Make 17 Videos a Week" + embedded "Running a YouTube Business is EASY" 2021-06-03 FP/MON (monday.com); HVM="How Our Videos are Made" 2017-07-26 FP/MON out-of-window historical; ONEDAY="How We Make a Video in ONE Day" 2019-08-24 FP/MON out-of-window; MONEY="TRUTH About How LTT Makes Money" 2025-03-25 FP/MON (Odoo); NOW="What do we do now?" 2023-08-16 FP; PLAN="Here's the plan." 2023-08-26 FP; SPEND="how much does LTT spend" 2025-09-03 FP 44s; LAB="Two Years to Build a Laptop Test Lab" 2024-07-04 FP (MSI demo)
- Factory cadence: 17 videos/week LMG-wide (7 LTT + WAN + clips + 3 TechLinked + 3 ShortCircuit + 2 TechQuickie + 1 Carpool); ≤2 LTT shoots/day via Gantt; count the week before writing [W17]
- Pipeline w/ explicit handoffs: writer's meeting (evaluate leads → assign 1 project/writer) → Script Review (founder gate for accuracy/flow/hook) → sponsor injection → teleprompter → Ready-to-shoot Checklist (exists because host was "sick of" unready sets) → A-roll/B-roll split with "guidance" (suggestions, creative freedom kept) → ingest to fixed server path → edit (guidance + editor flare) → pickups → 3-deep QC → green-screen thumbnail → publish [W17, HVM, ONEDAY]
- Tooling: Excel tracker → monday.com status board w/ automation triggers; org-wide visibility ("Before we had management involved, it was just chaos") [W17, ONEDAY]
- Script Review preserves channel voice while founder writes <25% [HVM]
- Scripted > vlog: scripted decouples host; vlogs couple host + mental strain [W17]
- Time budget per video: writer ~24h avg, camera 8–9h, edit ~27h, logistics ~90m [SPEND]
- 2023 quality reform: killed 10+yr unbroken-upload streak; stop-the-presses rule; Labs pre-shoot/post-edit checks; error-severity rubric (pinned comment → reshoot → cancel); weekly writing postmortems; hired external CEO 2023 [PLAN, NOW, MONEY]
- Thumbnails: green-screen + "suitably grotesque" face scrub from footage [HVM, ONEDAY]
- Burnout/human cost explicit: Monday kid-day inviolable; turnover 7.5% avg vs 18% CA benchmark (self-reported); benefits/HR scaffolding after 2023 crisis [W17, PLAN]
- Sources: W17, MONEY, NOW, PLAN, SPEND, LAB (in-window) + HVM, ONEDAY (historical) + Wikipedia×2/channel/SocialBlade (verification)

### wendover-productions — sources: OXFORD=Oxford Union interview 2026-05-12 FP/IND (Rosetta+YT mirror); NEBULA=BTS video 2021-11-17 FP/MON paywall (only via Grokipedia 2H synthesis); PUBPRESS=Staff Picks 2023-11-16 interview profile w/FP quotes; WIRED=Jet Lag interview 2022-06-29 FP/IND adjacent; GROK=Grokipedia 2H; +content samples (Taiwan/Texas 2026, not workflow docs)
- "Creative mass manufacturing" — assembly-line framing; founder deliberately moves UPSTREAM to concept/pre-production [OXFORD]
- Cadence: one video every 2 weeks for ~11 years [OXFORD]
- Ideation: "I have no system. I wish I had a system" — shower thoughts, NPR, current-events background context; ideation unsystematic BUT evaluation systematic (biweekly writers' room arguing algorithm fit; "the boss is the YouTube algorithm", ~70% confidence) [OXFORD]
- Offload what you hate first — post-production entirely ("brain does not mesh with editing software") [OXFORD]
- Virtuous cycle: hate post → hire → need revenue → more videos → team [OXFORD]
- Second channel (Half as Interesting): topics/writing delegated; effort asymmetry (HAI 1–1.5-day scripts vs Wendover 2-week half-time writes) [OXFORD]
- Founder keeps writing the flagship: "if I'm leading a team of writers, I have to be a writer myself... it's a somewhat opinion-based channel" [PUBPRESS, OXFORD]
- Processes reluctantly adopted then proven: Notion/Slack/timekeeping; 20–25 people per Jet Lag season [OXFORD]
- Jet Lag: ~9-month design lead; virtual playtesting via spreadsheets/timetables; incentive design (last 5% of rules) [OXFORD]
- Nebula: no venture, incremental growth; paywall retention incentives counter-model to ad-click model [OXFORD]
- Pipeline (2H-synthesized): research → script → animation → edit → fact-check [GROK/NEBULA]
- Sources: OXFORD, NEBULA(2H-only), PUBPRESS, WIRED, GROK + samples (non-workflow)

### mina-le — sources: WAPO=Washington Post Creator Q+A 2026-05-06 FP/MON; ARDEN=Arden Yum Substack guest cheat-sheet 2025-08-25 FP/IND self-authored; CRIMSON=Harvard Crimson profile 2023-04-11 FP/IND; POLY=Polyester 2023-03-12 FP/IND; INVERSE=Inverse/Input 2022-06-01 2H/IND; NYLON=NYLON 2022-04-29 2H/IND
- Ideation: be well-read (WaPo/news cycle) + ask "what can I bring that wasn't covered"; "constantly asking questions every step of the way" thread-following [WAPO]
- Research: "read every single article" from reputable sources; JSTOR/Semantic Scholar; librarian-curated guides; NYPL membership [WAPO, CRIMSON, INVERSE]
- Physical synthesis: print all research, arrange papers on floor, move around to find argument flow [ARDEN]
- Meticulous detailed script — never ad-lib [INVERSE]
- Editing heuristic: "do I need a zoom here? is this boring?" — meme-splice dense info to keep entertaining [POLY, INVERSE]
- Light staffing: ONE trusted editor (co-created style) + research assistant hired ~2025 [WAPO, NYLON]
- Inspired-only filter: "I only want to make a video if I feel inspired"; anti-trend-chase; anti-money-hungry [INVERSE, POLY, NYLON]
- Burnout containment: name the "psychological terror" of deadlines → kinder self-talk, apartment work/life zoning, boredom offline, exposure control [NYLON, CRIMSON, ARDEN]
- Explicitly NO packaging/retention doctrine documented (thin) [case study §5]
- Sources: WAPO, ARDEN, CRIMSON, POLY (FP) + INVERSE, NYLON (2H) + Wikipedia/SocialBlade/channel/Variety (verification)

### ryan-trahan — sources: YTBLOG=YouTube Official Blog 2022-06-09 FP/IND; CS50=Colin and Samir "50-Day Marathon" 2025-07-13 FP/IND; CSPENNY=Colin and Samir "changed YouTube with $0.01" 2022-06-06 FP/MON; EDITPOD=The Editing Podcast 2022-09-10 FP/IND (audio; via public pages + Gist 2H summary); GIMBAL=Gimbal Blog (Preston White) 2025-12-25 2H/IND; PUBLISH=PublishPress 2H; PICKS=PickScribe 2H
- "Redemptive vs exploitative work" greenlight filter; "Did we make this with love?" [YTBLOG]
- Thumbnail realism doctrine: subtle face, art-not-clickbait; 3,000 photos/5:30am light; 3-word subtitle brainstorm [YTBLOG]
- Thumbnail-FIRST: 30 (Penny) / 50 (50 States) thumbnails finished before shooting → reverse-engineer each day [CSPENNY, CS50]
- 10 title ideas/day brainstorm ritual (host-retold; PickScribe "write 100 titles") [CS50, PICKS]
- Repeatable segments (Jammy Time, Game Plan) + Double Arc: mini-arc daily resolution + master-arc cumulative momentum [CS50, GIMBAL 2H]
- Familiarity = comfort food; same clothes = characters; new viewer orients fast [CS50]
- iPhone-native production (99% iPhone, native UI/Animojis) [CS50]
- Team of 5: Preston films, Zach+Cohen nightly edits [CSPENNY, CS50, PUBLISH 2H]
- Editing: cut by feel/intuition (not frame-by-frame retention), pacing variety, keep vulnerable human moments [EDITPOD via Gist 2H, CSPENNY]
- Cadence: bread-and-butter 2/mo (Tom Brady longevity, off-season) + event-mode daily series [CSPENNY, CS50]
- Low overhead: borrowed Oculus, accessible ideas vs MrBeastification [CSPENNY]
- No presenting sponsor — brands donate as stakes (Wheel of Doom, $50K Great Reset) [YTBLOG, CS50]
- Appointment viewing / water-cooler TV thesis [CS50]

## Pattern candidate tally (built bottom-up; every entry needs ≥2 slugs + specific source each)

| # | Pattern | Slugs (count) | Tag |
|---|---|---|---|
| P1 | Scripted, not improvised (host-led formats) | drew-gooden, kurtis-conner, mkbhd, mina-le, johnny-harris, wendover (6) | agnostic (note: challenge formats counter-example) |
| P2 | Protected/scheduled writing time | johnny-harris, drew-gooden, wendover (3) | agnostic |
| P3 | Packaging = promise, defined before production | mrbeast, ryan-trahan, airrack, johnny-harris, veritasium, mkbhd, mark-rober (7) | agnostic |
| P4 | Native YouTube A/B thumbnail testing | veritasium, mkbhd, airrack, johnny-harris (4; ryan mention thin) | agnostic |
| P5 | Front-loaded open / no intros | mrbeast, veritasium, airrack, kurtis-conner, johnny-harris (5) | agnostic |
| P6 | Deliver-the-promise / anti-clickbait ethic | mrbeast, mkbhd, veritasium, drew-gooden, ryan-trahan (5) | agnostic |
| P7 | Deliberately capped sustainable cadence | mark-rober, drew-gooden, ryan-trahan, johnny-harris, linus-tech-tips, mrbeast (6) | agnostic |
| P8 | Burnout via structure/recharge, not wellness SOP | mark-rober, mrbeast, drew-gooden, mina-le, ryan-trahan, mkbhd, veritasium (7) | agnostic |
| P9 | Delegate edit/post, keep voice via gates | wendover, linus-tech-tips, johnny-harris, mina-le, ryan-trahan, airrack, veritasium, mkbhd (8) — counter: mark-rober keeps edit | agnostic |
| P10 | Founder holds idea/voice core while scaling | mark-rober, wendover, mkbhd, linus-tech-tips (4) | agnostic |
| P11 | Recurring idea-capture rituals | ryan-trahan, mrbeast, airrack, johnny-harris, kurtis-conner (5) | agnostic |
| P12 | Repeatable formats/series/segments | mrbeast, airrack, ryan-trahan (+wendover Jet Lag adjacent) | format-specific (serialized challenge/game) |
| P13 | Exhaustive research + fact-check infra | mina-le, johnny-harris, veritasium, wendover (4; wendover via 2H pipeline) | agnostic |
| P14 | Pipeline/PM tooling for visibility | linus-tech-tips, mkbhd, johnny-harris, wendover (4) | agnostic |
| P15 | Lean core team by design | ryan-trahan, airrack, mina-le, wendover (4) — contrast scaled factories | agnostic |
| P16 | Diversified income/ownership as insurance | veritasium, linus-tech-tips, wendover, kurtis-conner, ryan-trahan (5) | agnostic |
| P17 | Craft/quality over algorithm-chasing | mark-rober, drew-gooden, johnny-harris, ryan-trahan, mina-le (5) | agnostic |
| P18 | Algorithm as partially-understood boss | kurtis-conner, wendover, drew-gooden, johnny-harris, mkbhd (5) | agnostic |
| P19 | AI tools entering pipeline (emerging) | airrack, mkbhd (2) | agnostic, emerging |
| P20 | Second channels/extension ventures | wendover, airrack, mrbeast, veritasium (4) | agnostic |
| P21 | Audience signals feed ideation + post-publish loops | kurtis-conner, mina-le, mkbhd, drew-gooden (4) | agnostic |

Single-creator tactics (NOT patterns — 1 slug only): mrbeast CTR/AVD/AVP triad, minute-mark architecture, wow factor, kill-formats rule, work-multiple-videos-daily, abrupt endings, brand-deals-as-content, critical components/backup days; mark-rober build-then-story + film-intro-last, Super Mario effect; airrack one-word brand + shoe-swap, voice-note→Claude paper edit, editors-with-mics, sawdust businesses, 4-day-prep/1-day shoot; veritasium misconception-first pedagogy, problem→solution-no-thesis, power-law 0.1%; drew-gooden respect-viewer's-time essay + post-publish comment ritual; kurtis editing=writing-blocks analogy, thumbnail cottage industry; johnny-harris two-column visual script, fact-check citation comments/source dock, two-voices pacing, fresh art direction per video, 150-notes cut chain; mkbhd two buckets, playoffs lock, 6:02 timing, mainline-the-device, alternated editors, comment-pulse-after-30-min, octopus→robotic octopus; LTT ready-to-shoot checklist, Gantt distribution ≤2/day, hour-long script review, sponsor pickups, 3-deep QC, stop-the-presses rule + error-severity rubric, killed 10-yr streak; wendover assembly-line upstream move, 70% algorithm-confidence; mina-le print-and-floor-sort, meme-splice density; ryan-trahan thumbnail realism + 3,000 photos, Double Arc (label via 2H), Wheel of Doom/no-presenting-sponsor, Tom Brady off-season, water-cooler thesis.


## Pattern candidate tally

(fill after extraction)
