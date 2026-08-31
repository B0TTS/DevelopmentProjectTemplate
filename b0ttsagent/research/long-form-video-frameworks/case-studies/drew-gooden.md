# Drew Gooden — Long-Form Workflow in His Own Terms

> First-party corpus for this note: one in-window first-party/monetized interview verified in `working/shortlist.md` — "I interviewed Drew Gooden so you don't have to" / I Spent a Day With... (2024-03-08, FIRST-PARTY/MONETIZED) — plus two first-party essays on his own channel that document workflow philosophy end-to-end: "using AI to write a youtube video" (2022-08-31) and "Everybody wants to waste your time" (2024-09-22, 30:30) — plus the WIRED Autocomplete Interview (2022-05-16) where he states the solo premise in his own words. Every workflow step carries ≥1 first-party link; every factual claim is linked. Verified-vs-claimed, caveats, and contradictions are explicit. Where Drew does not document a step (open/hook formula, retention targets, editing cadence), this note says so and stops — no padding, no paid-content inference.

**Who this is:** Drew Gooden — @drewisgooden, YouTube since Aug 21 2015 (channel UCTSRIY3GLFYIpkR2QwyeklA), 4.86M subscribers / 1.16B views per Wikipedia infobox last updated Aug 12 2026 [Wikipedia](https://en.wikipedia.org/wiki/Drew_Gooden_(internet_personality)) and 4.87M via `python -m yt_dlp` `channel_follower_count` on 2026-08-29 ([@drewisgooden](https://www.youtube.com/@drewisgooden) via [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json)), SocialBlade 4.86M/1.16B/173 videos [SocialBlade](https://socialblade.com/youtube/handle/drewisgooden), former Viner "Road Work Ahead" (2016) [NBC News 2022-01-18](https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168). Genres commentary/comedy, Streamy Commentary winner 2021 [Wikipedia](https://en.wikipedia.org/wiki/Drew_Gooden_(internet_personality)). Dominance 0.735, median 4,697,784 on last 12 eligible long-form (all 1,387–2,843s, 23–47 min) per [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json); activity 1.0 (newest upload 2026-08-09, 20 days before 2026-08-29) [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json). Representative highs: "The internet made me obsessed with protein" (7,430,720) and "Greed is Destroying the World" (6,881,324) per [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json).

**Best starting source per Phase 1.5:** "I spent a day with Drew Gooden — Anthony Padilla: I Spent a Day With..." — 2024-03-08, FIRST-PARTY/MONETIZED, most recent in-window [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) (Smosh Alike mirror "I interviewed Drew Gooden so you don't have to" same date/upload_date 20240308; audioboom listing [Audioboom 2024-03-08](https://audioboom.com/posts/8636844-i-spent-a-day-with-drew-gooden) confirms creator Anthony Padilla). Transcript via `youtube-transcript` skill (SKILL.md read first; `python -m yt_dlp` fallback) to `b0ttsagent/temp/youtube-transcripts/Smosh_Alike_I_interviewed_Drew_Gooden_so_you_dont_have_to.txt` (33,925 chars). The only first-party+independent doc (Triangle Talks 2019-09-11) is pre-2021/stale per [shortlist](../working/shortlist.md) — caveat MONETIZED on the primary, treat as marketing-adjacent but still Drew's own words.

Transcripts for own-channel strategy videos sampled most-recent-first per instructions: "Everybody wants to waste your time" (2024-09-22) [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) → `b0ttsagent/temp/youtube-transcripts/Drew_Gooden_Everybody_wants_to_waste_your_time.txt` (33,952 chars), then "using AI to write a youtube video" (2022-08-31) [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) → `b0ttsagent/temp/youtube-transcripts/Drew_Gooden_using_AI_to_write_a_youtube_video.txt` (30,964 chars). If bare `yt-dlp` fails use `python -m yt_dlp` — used for all three. WIRED Autocomplete Interview (2022-05-16) adds the solo-premise verbatim [WIRED 2022-05-16](https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete) (Rosetta transcript [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired)).

---

## 0. "I do everything myself" — the gate for everything else

> "I do everything myself yeah I do I come with the ideas which is why they suck which is why sometimes they're good and other times it's like that's what you're making a video about I don't know tried my best um but yeah I write them I I star in them it's me uh and I edit them myself" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Same premise, shorter, on WIRED:

> "I make a time to sit and work and I film and edit and editing can be a lot of work too I like doing every part of the video myself" [WIRED 2022-05-16](https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete) (also paraphrased [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired))

**What this rules out:** no writer's room, no editor, no thumbnail team documented. He even frames the *absence* of help as a content opportunity: "maybe that would be the next step is like having people find products for me so I can have like a live reaction I think that is maybe something that is missing ... cuz I'm finding all the stuff I already have an idea ... but if I could just be surprised with a mountain of crap ... now that's content cuz you're doing everything yourself" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — tension flagged below (solo vs delegate surprise).

**Verified vs claimed:** channel_follower_count 4,870,000 via `python -m yt_dlp` Aug 29 2026 and Wikipedia 4.86M [Wikipedia](https://en.wikipedia.org/wiki/Drew_Gooden_(internet_personality)) corroborate scale of a solo operation; claim that he *actually* edits every frame is self-reported but consistent across three first-party sources [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ), [WIRED 2022-05-16](https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete), [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — treat as claimed but directionally verified by the lack of any credited editor in his video descriptions.

---

## 1. Writing is the work — "the world's slowest writer"

> "I spend more time writing than I do any other part of the video making process part of the reason it takes me so long is because I happen to be the world's slowest writer I'll have days where I spend 7 hours at my computer and type a single paragraph This was today" [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg)

> "I'm writing every word of my videos that'll take me a couple weeks and then for the most part then I can film it and edit it in like 2 days it's really just like the writing it conceptualizing it trying to plan everything out so I can be as efficient as possible with the rest" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

On scale of that writing: "my last video which was 40 minutes long was only 8,000 words so 50,000 should be plenty" (pricing Jasper words) [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — gives a sense of words-per-minute: ~200 wpm spoken, dense but not padded.

**Forcing function because there is no boss:**

> "there is it is just like no one's going to hold me accountable necessarily like I don't have a boss ... I really need to be my own parent or my you know adult in the room to be like all right we're going to set a schedule like no video games this morning you're going to first thing you do have some coffee sit at your computer start writing like just because you don't feel like you're that creative right now it's like you the part of it is just forcing yourself to sit down and do it and then hey I I didn't even think I had a page of a script in me but I did because I sat down and forced myself to do it" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

He repeats the same "force to write" logic as the only value he saw in the AI tool: "it forces you to write something ... you have to give it a few sentences to begin with and sometimes you'll start typing, and then before you know it, you've got this whole paragraph flowing" [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — i.e., the tool's value was the *prompt to start*, not the output.

**Verified vs claimed:** "7 hours for a paragraph" and "couple weeks per script" are self-reported, not auditable [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg), [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ). The 8,000 words / 40 minutes ratio is claimed for *that* one video [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — not a channel average.

---

## 2. From unscripted rant to script — why he switched

Early method (pre-2020):

> "when I started I used to just sit down no script just rant and I'd be all over the place and it would take me like two weeks to edit it because I'm like I'm not even I'm saying things an hour in that I'm taking a mental note to actually put earlier in the video but then I don't remember by the time I go to edit I was like like two hours of content cutting it down ... I would repeat myself a lot because I'm not thinking about what I'm saying until I'm editing it" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Transition context (first-party corroboration via interview quotes inside second-hand articles — flagged second-hand framing, but quotes are Drew's):

- Vine left him with ~400k Vine followers but "like 500 YouTube subscribers so I really kind of had to start from scratch" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); same numbers in Triangle Talks: "I had to start from scratch on YouTube, with maybe 1000 subscribers" [Triangle Talks 2019-09-11](https://www.thetriangle.org/article/triangle-talks-youtube-stars-danny-gonzalez-and-drew-gooden) (stale, 2019) and NBC News: "His only other social media following was on a Twitter account with about a thousand followers ... he decided to give YouTube a try" [NBC News 2022-01-18](https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168).

- Experimentation period: "We both tried doing sketches or music or a whole bunch of other stuff until eventually Drew started doing commentary and so did Cody [Ko] and they were both killing it" — Danny Gonzalez quote in same Triangle Talks piece corroborating Drew's path [Triangle Talks 2019-09-11](https://www.thetriangle.org/article/triangle-talks-youtube-stars-danny-gonzalez-and-drew-gooden) (second-hand framing, but documents Drew's experimentation).

- Turning point he names: "a rant he made about a video by Business Insider ... about bagels' being cut in a weird way ... He said he was in a bad mood and decided to rant into the camera" and then: "For whatever reason, that format, where you sit and you're talking straight at the camera, I think it feels more personal ... That's what YouTube is all about" [NBC News 2022-01-18](https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168) — first-party quote inside NBC News.

Current method is the inverse: conceptualize + script first so the 2-day shoot/edit is efficient: "trying to plan everything out so I can be as efficient as possible with the rest of it because when I started ... [it] was so unorganized" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ). He does not document a beat sheet or scoring rubric beyond "writing every word."

**Caveat on shortlist summary:** shortlist's one-line doc summary for the Padilla interview lists "not over-planning, pure intuition, straight cuts" as takeaways [shortlist](../working/shortlist.md). **Verified-vs-claimed:** those three phrases were not found verbatim in the transcript when searched (`intuition`, `straight cut` returned no match); the closest is "plan everything out so I can be as efficient as possible" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — which actually suggests *planning*, not anti-planning. Treat "pure intuition / not over-planning" as the shortlist author's synthesis, not a direct Drew quote — thin, not relied on for a workflow step.

---

## 3. Production — plan just enough, then film/edit in ~2 days

The 2-day number is the only quantified production timeline he gives:

> "I'm writing every word ... couple weeks and then for the most part then I can film it and edit it in like 2 days" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Gear — only first-party camera mention found is WIRED:

> "Panasonic Lumix G 150 that's a pretty good camera it's good for sitting down and staying focused in one spot otherwise if i move around it's not as good of a camera because the autofocus isn't very good so if you're sitting down and making videos that's a good one to use" [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired) (full WIRED video [WIRED 2022-05-16](https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete))

Second-hand vloggingpro claims "Canon EOS R6 as primary, G7 X Mark III secondary, Adobe Premiere Pro on MacBook Pro 14 M3 Pro" [VloggingPro](https://vloggingpro.com/setups/drew-gooden/) — **not relied on** (second-hand, not Drew's words) and flagged thin. He never documents timeline structure, ingest, proxies, or color pipeline in any first-party doc — thin, stop.

---

## 4. Editing philosophy — respect the viewer's time (his own terms for pacing/retention)

Drew does not publish a retention formula, CTR target, or cuts-per-minute rule. His documented editing philosophy is an *ethic* against padding, articulated at length in his own essay:

> "I'm old enough to remember when the 10 minute mark was something videos got stretched out to Now it feels like half the videos I get recommended ... are 7-hour retrospectives" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

On the meta he names:

> "The current YouTube meta is to turn your video into a podcast It's to pad the absolute [expletive] out of the runtime because that's what the algorithm likes" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

> "If I just vomit out every word that remotely pertains to the topic at hand with no thought into brevity no consideration of the viewer's time it's actually more likely that YouTube will push my video ... The algorithm is teaching me that I shouldn't cut things out ... They'd prefer if I stretched out every video as long as I could But ... That their time is just something for me to leverage so I can get more views That's a little shitty" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

His length test (organic vs inflated):

> "When H bomber guy or Jenny Nicholson release a 4 Hour video I know it's not just because they're trying to inflate the watch time so it gets boosted by the algorithm it's because they spent months working on it and that's just how long the video ended up being" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

> "As long as a person making it is passionate about the subject and they put in the effort to make it entertaining I'll watch just about anything" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

He positions two poles and chooses middle:

> "There are videos that go on so long that large portions ... become nothing more than background noise And then there's the most hyperactive fever dream editing non-stop cacophony of colors and sounds meant to over stimulate the 8-year-old boys watching on their iPad and then there's a lot of space in between ... I'm just asking that we meet somewhere in the middle" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

> "Mr. Beast and all of the channels copying him have never made their videos that way because they value people's time they're just trying to keep their retention rate as high as possible It's just a different metric they're prioritizing" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

Retention manipulation he *names and rejects*:

> "they put this progress bar on the bottom that starts off really [fast] ... then once people have done the math ... the progress bar mysteriously slows down ... This [expletive] really pisses me off ... very deliberate ... You have to go out of your way to key frame it like this with the intention of deceiving your viewers" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) — first-party critique, not a how-to.

Practical pacing rules he *does* document:

- **Don't sell before you hook:** "You haven't even hooked me and you're already trying to sell me a water bottle that smells bad ... You don't have to do this I literally do I signed a contract" (sponsored SoFi read then self-aware) [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) — implies hook before ad, but no timestamp formula.
- **Get to the point, honor Nerdwriter/Tom Scott brevity as model:** "I have a lot of respect for creators that make algorithmically counterintuitive decisions because they don't want to waste their viewers time ... Internet Shaquille ... always just gets right to the point ... Nerd Writer is ... barely hitting that 7 minute mark ... here's this thing I noticed ... and that's all I got" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)
- **Make what you wish existed, not trend drama:** "don't just throw together a bunch of crappy videos about whatever drama is trending Make a retrospective about some niche hobby you had as a kid ... Remember this website is called YouTube not do the thing that you think will become popular tube" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)

**What is NOT documented (thin — say so and stop):** no hook template ("first 15 seconds must do X"), no chapter-card system, no A/B thumbnail test count, no CTR/AVD numeric target, no music/SFX cadence. He never shows a retention graph or YouTube Studio analytics screen. The only pacing numbers he gives are the *anti-numbers*: against padding. Sources thin on editing rhythm — stopped.

---

## 5. Open / hook — "hey guy" (not a retention formula)

> "For a long time I didn't know how to start my videos because a lot of people are like What's up guys Or they have a catchphrase or a nickname ... And for a while I was calling people Little stinkers and then I didn't really like that ... once I said Hey guy ... And people seemed to think it was funny So I've been saying it pretty much every video Why do I say it because it's funny" [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired) (video [WIRED 2022-05-16](https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete))

That is the entire first-party hook formula he documents. No cold-open, no stakes line, no preview structure documented elsewhere.

**Caveat:** shortlist's "open/hook" expectation (retention architecture) does not exist in Drew's docs — skip, not padded.

---

## 6. Structure — "here's what I'm annoyed/passionate about, sitting down yapping"

> "the thing that worked for me was just sitting down and yapping about something for like 15 minutes just whatever I was kind of annoyed about at the time I found a brand new audience from doing that" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Evolved positive version of same structure:

> "what I really love doing ... video ... about Star Wars ... what I really liked ... was talking about Andor a show that I love and talking very pass[ionately] about something that I think is good and the point of the video isn't like this sucks it's like really focusing on what I like about a show ... it's so fun to talk about something you're really passionate about in a positive way it's a much better heads space" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

He does not document a written structure template (no "act 1 at 0:00, midpoint at 7:00"). His structure is topic + personal angle + researched digressions, pruned for brevity per §4. The earlier "2 hours cutting to not repeat" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) is the only structural lesson: eliminate repetition via scripting.

---

## 7. Cadence — one a month, could do more, chooses not to

> "I do one a month I uh I could do more I used to do more I think I have at this point built-in time for me in between videos where I'm not working cuz I think it's important to just have kind of recharge a little bit um anytime I try to like overcommit to Brand deals or too do too many things I end up like putting out videos I'm not super happy with and then I'm more burnt out" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Post-publish ritual he builds into cadence:

> "I think it's good to take a couple days to just like read the comments and feel good about yourself and you know pat yourself on the back cuz you can be proud of something you spend a lot of time on and then you know and then move on to the next thing so I kind of like build that in" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

Verified cadence: newest uploads 2026-08-09, 2026-07-31, 2026-06-17, 2026-04-03, 2026-03-03 per [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json) via `python -m yt_dlp --print upload_date` — roughly 3–6 weeks, averaging one a month in 2026, consistent with his claimed "one a month" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ). The claim "I could do more" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) is self-reported; no audited calendar.

Historical cadence: Vine 2013 (started 2015) → dead 2017 → YouTube full-time "about three years after he started on the platform" (so ~2020) [NBC News 2022-01-18](https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168) — corroborates slow build, not overnight.

---

## 8. Replication without burnout — the solo system

Drew's burnout theory is personal discipline + life outside work, not a team playbook (he has no team). It is the most explicit of his workflow and is entirely first-party:

**Own the schedule because no one else will:**

> "I really need to be my own parent ... set a schedule like no video games this morning you're going to first thing you do have some coffee sit at your computer start writing like just because you don't feel like you're that creative right now it's like you the part of it is just forcing yourself to sit down and do it" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**Separate work from life (Amanda as anchor):**

> "my wife Amanda still has a 9 to 5 job ... I've gotten better about scheduling it so our days are compatible so like when she comes home I'm done ... not going to be like sorry I got to focus on this cuz I procrastinated this morning" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**Don't let it be your entire identity / don't refresh analytics:**

> "I think it's also important not to like have your entire life revolve around it because then it do it Everything feels like even more important ... I'm refreshing until it gives me the ranking H 10 out of 10 I can't I'm going to be miserable ... let me turn my computer off and go hang out with my wife or my cat or go outside and go for a walk it's like just it's not the end of the world" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**Refill the cup / live a life to have something to say:**

> "you really have to constantly be refilling your cup you're you have a certain amount of your Creative Juice ... if you're constantly pouring it out and you're obsessing over every detail ... you're never refilling it you have to take that moment away" (quoting Market Player, endorsed "absolutely") [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

> "you have to live a life to be ... able to make a joke about it ... you have to have a crappy experience at the airport sometimes to be able to be like actually this is a funny video idea" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**Manage validation (comment reading as calibrated reward):**

> "if it's a video that I've really spent a lot of time on and I really think is good then I will read a lot of the comments ... enjoy the praise ... I really only do that for videos where ... I feel like I deserve it cuz there's some where it's like ... I don't love this idea ... I'll see a comment where it's like this one wasn't that good and I'll be like you're right I agree and I'll get like depressed so ... when I make a video like that I'll focus on the next one" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

> "the more value that you give the praise the more value that you inadvertently give the negative comments well because like you hold them with the same value ... if it's a video I love ... it's easier to brush off a negative comment ... it's like well they just don't agree ... but if you're not happy with a video then ... you're like ah I knew it" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**Keep expectations honest as you plateau:**

> "of course yeah you always feel like you need to be making something better but that's just not human nature ... some months you're just like I don't know this is what I got this month and it maybe it's not as good ... maybe you'll make your the best video you ever make like a year in and then you want to do it for another 10 years ... think of all the musicians who close every concert with the song they wrote 20 years ago ... make stuff that you're happy with ... that's fulfilling" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

> "I think the internet especially can feel like there's such a short shelf life ... if you get a couple videos in a row that don't perform ... I guess I'm washed now ... I guess people don't care ... but I try ... keep it in perspective ... even if I Plateau it's like ... I'm getting 2 million views regularly like that's awesome ... why do we always have to be better ... you get so used to growing and at a certain point ... you got to keep your expectations in check ... I'm so lucky to get to do what I'm doing" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

> "it requires so much discipline to continue creating the videos and doing every single element" (Anthony's framing, Drew confirms) and Drew: "that still crops up for sure" re: laziness in high school [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — where he says he was "lazy cuz you're not putting enough effort into something but that doesn't mean you're incapable ... I'm an extremely hard worker when I'm working on a video that I'm obsessed with because it doesn't feel like work ... I'll be mid conversation and I'll just think ... wait I got to go write this down" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

**What is thin here:** no sleep protocol, no exercise, no hiring pipeline, no max-hours cap — because there is no team. Replication without burnout *is* the built-in gap between videos + separate life.

---

## 9. Caveats, contradictions, verified-vs-claimed — explicit

**Every developed workflow step above has a first-party link. Steps he does not document are skipped below — not padded.**

**Thin / not documented at all (say so explicitly):**

- **Open/hook architecture:** no timestamped cold-open breakdown, no preview/tease structure, no retention-graph hook test. Only anti-pattern "don't ad-read before hook" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) and "hey guy" origin [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired) — thin, stop.
- **Thumbnail / title / CTR / AVD / AVP:** no target numbers, no iteration count, no split-test tooling. He critiques others' retention manipulation [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) but never shares his own analytics — thin, stop.
- **Editing rhythm:** no cuts-per-minute, no sound/mix recipe, no color, no chapter markers. Only the philosophical middle between "unedited yapping" and "hyperactive fever dream" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY) — thin, stop.
- **Course / paid workflow doc:** no course. Jasper/AI sponsorship [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) and SoFi/NordVPN reads are product sponsors, not workflow products — per instructions, no fabrication from marketing copy; stopped.
- **Shortlist synthesis phrases:** "not over-planning, pure intuition, straight cuts" appears in [shortlist](../working/shortlist.md) doc summary but not verbatim in transcript (search found no match) — treat as synthesis, not first-party fact — thin, not relied on.

**Contradictions / tensions (Drew flags or implies):**

- "I do everything myself" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs "maybe next step is having people find products for me so I can have ... surprise with a mountain of crap" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — solo purity vs delegated surprise; he acknowledges the gap.
- "Forcing yourself to sit down even when not creative" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs "built-in time ... where I'm not working ... important to ... recharge" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — discipline vs rest, unresolved.
- Early "yapping about whatever I'm annoyed about" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs later "it's so fun to talk about something you're really passionate about in a positive way" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — retained both modes, not a contradiction but a portfolio shift.
- Labeled lazy in high school / "barely went to school" vs "extremely hard worker when obsessed ... doesn't feel like work" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — passion-gated effort, explicit.
- "Extreme" burnout protection via "don't let entire life revolve around it ... turn computer off" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs earlier career "I think the amount of hours you work is irrelevant" logic he does *not* espouse — Drew never espouses hustle metric; his ethic is opposite, but the tension with "requires so much discipline ... doing every single element" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) remains.

**Verified-vs-claimed flags:**

- Subscriber/view growth: Padilla 2024 says "over 4 million subscribers and over 800 million views" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs Wikipedia Aug 12 2026 4.86M/1.16B [Wikipedia](https://en.wikipedia.org/wiki/Drew_Gooden_(internet_personality)) vs yt-dlp Aug 29 2026 4.87M [evidence JSON](../working/evidence/drew-gooden-2026-08-29.json) — directionally verified, lag explained by 2.5 years growth; totals not independently audited beyond those two points.
- "Two weeks to edit ... two hours of content" early era [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs "film and edit in like 2 days" current [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) — both self-reported, plausibly evolution.
- "World's slowest writer ... 7 hours ... single paragraph" [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — self-reported, not audited.
- "8,000 words = 40 minutes" [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg) — claimed for that one video, math checks (~200 wpm).
- Vine follower counts: "400k fine followers to 500 YouTube subscribers" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) vs Triangle Talks "maybe 1000 subscribers" [Triangle Talks 2019-09-11](https://www.thetriangle.org/article/triangle-talks-youtube-stars-danny-gonzalez-and-drew-gooden) — order consistent (400k→~500–1000), not a contradiction; exact numbers rounding.
- "About three years after he started ... making YouTube his full-time job" [NBC News 2022-01-18](https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168) — claim published Jan 2022, would imply ~2020 full-time after Vine died 2017; plausible but not payroll verified.
- Triangle Talks [Triangle Talks 2019-09-11](https://www.thetriangle.org/article/triangle-talks-youtube-stars-danny-gonzalez-and-drew-gooden) is dated Sep 11 2019 — outside 2021–2026 window, per [shortlist](../working/shortlist.md) flagged "NO - ... cannot alone satisfy recency" — used only for Vine→YouTube transition corroboration, not for current workflow, flagged stale.

---

## 10. In his own words — compressed replication checklist (solo edition)

1. **Come with your own idea, expect it might suck.** "I come with the ideas which is why they suck ... sometimes they're good and other times it's like that's what you're making a video about I don't know tried my best" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
2. **Write every word — it's the bottleneck.** Couple weeks, even 7 hours for a paragraph is normal [Drew Gooden 2022-08-31](https://www.youtube.com/watch?v=BaVpeJlcQzg), [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); script so you don't ramble for 2 hours then spend 2 weeks editing repeats [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
3. **Force the sit-down.** No boss, be your own parent: coffee, no games, sit at computer even when not creative — page appears because you sat [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
4. **Plan just enough to shoot/edit in ~2 days.** Conceptualize so the shoot is efficient [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); gear is sitting-down camera (Lumix) [Rosetta 2022-05-16](https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired)
5. **Hook is "hey guy" + topic you care about.** No growth-hacked open; "talking very pass[ionately] about ... Andor ... point isn't this sucks it's ... what I like" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ) and "sitting down yapping about something for like 15 minutes ... whatever I was ... annoyed about" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
6. **Respect the viewer's time — cut, don't pad.** Don't yammer to stretch, don't hyper-edit to overstimulate; meet in middle [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY); "I shouldn't cut things out if they feel superfluous ... They'd prefer if I stretched ... But ... their time is just something for me to leverage ... that's a little shitty" [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY); don't front-load ad before hook [Drew Gooden 2024-09-22](https://www.youtube.com/watch?v=56EyKNjhUDY)
7. **One a month, with recharge built in.** "I think it's important to just have ... recharge ... good to take a couple days to ... read the comments and feel good ... and then ... move on" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); don't overcommit to brand deals [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
8. **Live a life, then talk about it.** Refill cup, have airport crappy experience, don't let channel be your entire life, turn off computer and walk [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
9. **Calibrate praise.** Only read comments hard when you earned it; otherwise negative validates self-doubt [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); don't refresh to 10/10 ranking [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)
10. **Expect plateau, not infinite growth.** "I'm getting 2 million views regularly ... awesome ... why do we always have to be better ... keep expectations in check" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ); some months just "here's a bad movie I can make fun of" [Anthony Padilla 2024-03-08](https://www.youtube.com/watch?v=8t_JqQXg5qQ)

---

## Sources

- I spent a day with Drew Gooden — Anthony Padilla: I Spent a Day With... / Smosh Alike: "I interviewed Drew Gooden so you don't have to" — 2024-03-08 — FIRST-PARTY/MONETIZED — https://www.youtube.com/watch?v=8t_JqQXg5qQ — audioboom listing https://audioboom.com/posts/8636844-i-spent-a-day-with-drew-gooden ; transcript via `python -m yt_dlp` + `flatten-json3.js` to `b0ttsagent/temp/youtube-transcripts/Smosh_Alike_I_interviewed_Drew_Gooden_so_you_dont_have_to.txt` (33,925 chars)
- Drew Gooden — "using AI to write a youtube video" — 2022-08-31 — FIRST-PARTY/MONETIZED (own channel) — https://www.youtube.com/watch?v=BaVpeJlcQzg — transcript to `b0ttsagent/temp/youtube-transcripts/Drew_Gooden_using_AI_to_write_a_youtube_video.txt` (30,964 chars) via `python -m yt_dlp --write-auto-subs --sub-format json3`
- Drew Gooden — "Everybody wants to waste your time" — 2024-09-22 — FIRST-PARTY/MONETIZED (own essay on pacing/retention) — https://www.youtube.com/watch?v=56EyKNjhUDY — transcript to `b0ttsagent/temp/youtube-transcripts/Drew_Gooden_Everybody_wants_to_waste_your_time.txt` (33,952 chars) via `python -m yt_dlp`
- Drew Gooden — WIRED Autocomplete Interview — 2022-05-16 — FIRST-PARTY (guest) — https://www.wired.com/video/watch/autocomplete-interviews-drew-gooden-autocomplete — Rosetta transcript https://rosetta.to/u/wired/drew-gooden-answers-the-web-s-most-searched-questions-wired
- Triangle Talks: YouTube stars Danny Gonzalez and Drew Gooden — The Triangle — 2019-09-11 — FIRST-PARTY/INDEPENDENT but **stale** (outside 2021–2026) — https://www.thetriangle.org/article/triangle-talks-youtube-stars-danny-gonzalez-and-drew-gooden — used only for Vine→YouTube transition corroboration
- Confidence to shine: Drew Gooden says Vine came around right when he needed it — NBC News — 2022-01-18 — SECOND-HAND framing, FIRST-PARTY quotes — https://www.nbcnews.com/pop-culture/confidence-shine-drew-gooden-says-vine-came-right-needed-rcna12168
- Drew Gooden (internet personality) — Wikipedia — last updated Aug 12 2026 — https://en.wikipedia.org/wiki/Drew_Gooden_(internet_personality) — verification only
- Evidence JSON — working/evidence/drew-gooden-2026-08-29.json — view-count, dominance, documentation array source of truth

*No paid-content inference; no marketing-copy fabrication. Where Drew does not document a step (hook formula beyond "hey guy", CTR/AVD targets, editing cadence, thumbnail iteration, team ops), this note states the gap and stops.*
