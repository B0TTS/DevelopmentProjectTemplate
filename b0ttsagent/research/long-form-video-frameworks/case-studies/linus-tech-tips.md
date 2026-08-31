# Linus Sebastian — Long-Form Workflow in His Own Terms

> First-party corpus for this note: the only 2021–2026 doc listed in `working/shortlist.md` — **How We Make 17 Videos a Week** — forum topic + embedded video **Running a YouTube Business is EASY (just kidding)** (2021-06-03, FIRST-PARTY/MONETIZED, monday.com sponsor) [LTT Forum Topic](https://linustechtips.com/topic/1344340-how-we-make-17-videos-a-week/) / [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — transcript via `python -m yt_dlp` to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__Running_a_YouTube_Business_is_EASY_just_kidding.txt` (16,545 chars, manual English `en` json3 → txt via `flatten-json3.js`, `python -m yt_dlp` fallback per `youtube-transcript` skill); plus corroborating first-party workflow videos in-window sampled most-recent-first: **how much does LTT spend on each video?** (2025-09-03, 44s, FIRST-PARTY) [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg) → `Linus_Tech_Tips__how_much_does_LTT_spend_on_each_video.txt`; **Why it took TWO YEARS to Build a Laptop Test Lab** (2024-07-04, FIRST-PARTY, MSI demo) [Two Years Lab](https://www.youtube.com/watch?v=Qju1aITk_WY) → `Linus_Tech_Tips__TWO_YEARS_to_Build_a_Laptop_Test_Lab.txt` (manual `en` 15k) + `Linus_Tech_Tips__TWO_YEARS_Lab_manual.txt` (auto `en` 15k); **The TRUTH About How LTT Makes Money** (2025-03-25, FIRST-PARTY/MONETIZED, Odoo) [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) → `Linus_Tech_Tips__TRUTH_About_How_LTT_Makes_Money.txt`; **What do we do now?** (2023-08-16, FIRST-PARTY) [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) → `Linus_Tech_Tips__What_do_we_do_now.txt`; **Here's the plan.** (2023-08-26, FIRST-PARTY) [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) → `Linus_Tech_Tips__Heres_the_plan.txt`; plus out-of-window historical context **How Our Videos are Made** (2017-07-26, FIRST-PARTY, Lenovo) [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) → `Linus_Tech_Tips__How_Our_Videos_are_Made_2017.txt` and **How We Make a Video in ONE Day** (2019-08-24, FIRST-PARTY, monday.com) [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) → `Linus_Tech_Tips__How_We_Make_a_Video_in_ONE_Day_2019.txt` — read end-to-end via `python -m yt_dlp` (bare `yt-dlp` not on PATH). No first-party+INDEPENDENT source exists — caveat MONETIZED throughout — treat sponsor framing as marketing. Every workflow step below carries ≥1 first-party link; every factual claim is linked. Verified-vs-claimed, caveats, and contradictions explicit. Where Linus does not document a step (hook formula, retention dashboard, act structure, cuts-per-minute), this note says so explicitly and stops — no padding. Paid content only summarized from public previews per instruction.

**Who this is:** Linus Gabriel Sebastian (born 1986) Canadian YouTuber, founder and former CEO (2013-2023) now Chief Vision Officer of Linus Media Group, years active 2007–present, creator of Linus Tech Tips on Nov 24 2008 [Wikipedia — Linus Sebastian](https://en.wikipedia.org/wiki/Linus_Sebastian); Linus Media Group privately held, founded Oct 3 2012 by Linus Sebastian and Yvonne Ho, 120 employees as of January 2026, headquartered Surrey BC, owns flagship Linus Tech Tips (7,009 videos) plus TechQuickie/TechLinked/ShortCircuit [Wikipedia — Linus Media Group](https://en.wikipedia.org/wiki/Linus_Media_Group); Linus Tech Tips channel 16.9M subscribers / 9.63B views (main) per Wikipedia infobox corroborated by SocialBlade and FollowerCharts averaging 1.2M per video [Wikipedia — Linus Sebastian](https://en.wikipedia.org/wiki/Linus_Sebastian) / [SocialBlade — linustechtips](https://socialblade.com/youtube/handle/linustechtips); direct `channel_follower_count 16900000` via `python -m yt_dlp` on 2026-08-29 [YouTube @LinusTechTips](https://www.youtube.com/@LinusTechTips) (evidence JSON). Niche/format tech explainer / documentary 10–25 min (median 1,004,889 on last 12 eligible, 12/12 >100k, activity 1.0 newest 2026-08-29 0 days, dominance 0.55) per evidence JSON. Longest actively documented factory in this corpus: daily upload including weekends since at least 2017 [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).

**Best starting source per Phase 1.5:** the forum-embedded **Running a YouTube Business is EASY (just kidding)** itself — only doc that walks a literal calendar week at LMG shooting LTT/ShortCircuit/TechQuickie as 17 videos/week pipeline [LTT Forum Topic](https://linustechtips.com/topic/1344340-how-we-make-17-videos-a-week/) / [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). No caveat beyond MONETIZED per shortlist.

---

## 0. North star in his own terms: "cat herder" — the factory exists so Linus doesn't have to be the system

The only time Linus names the job in-video, he hands it to Ed: "day in the life of editor extraordinaire and professional cat herder edel" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) — and Ed's own opening: "it's my job to know at what stage of the process each video is at at all times and to coordinate everyone so our videos get released on time" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).

By 2023 Linus reframes that herding as the reason he stepped back: "What the team does like though is getting paid... My strength is being a bottomless pit of creativity and I found that while I could spend my time on the details, it wasn't necessarily the best thing for the company and the team. ... This is a big part of the reason that I hired a CEO back in early 2023 and have asked the rest of the leadership team to step up" — "I don't actually sit in annual business reviews anymore. So, when I reviewed the script with Elijah, that was legitimately my first look at these numbers for 2024" [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE). New CEO Terren (Taryn/Terren in transcript) introduced 2023-08-16: "6 weeks into the job... my main focus has been to be a fly on the wall" [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) / [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

That handoff gates everything below: the system is documented by the people who run it day-to-day (James, Ed, Yvonne, Gary, Nick, Colton) more than by Linus monologuing craft.

---

## 1. The 17-videos-a-week calendar — what counts, what stacks, what flexes

Quoted in full because the count is the structure:

> "17 videos is a lot of videos. That's seven LTTs, a WAN Show, clips from the previous week's WAN Show, three TechLinks, three ShortCircuits, two Techquickies and a Carpool Critics." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

Real week narrated in that video: last week shot six LTTs not seven, promised Monday makeup shoot — "But my kids are on spring break. Now, Linus isn't in on Mondays. He spends Mondays with his kids, but we can still do some work here at the office to chip away at this number. So now if you want to go on vacation next week ... We need to shoot more than seven LTTs this week and it's already Tuesday." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

Historical baseline: "we release a video every single day including weekends and that takes a lot of planning and management because each video has lots of people doing different jobs over a period of several days" — "the week starts with me telling the writing team how many videos need to be made that we hit our Target and not be screwed the next week which can happen if someone goes on vacation or if parts we ordered arrive broken" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).

What breaks the calendar is also documented in the same week: writer's meeting didn't happen Monday and can't happen Tuesday morning because guest Luke is coming for an LTT build — "Yeah, Luke's build could take a while depending on if his case fits a radiator" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); Sarah's Secret Shopper may not finish because Sarah is busy, split to two parts [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); water-cooled PS5 may not make it because Alex is in Delta today and tomorrow — "That gives him Thursday, Friday to water-cool a PlayStation 5" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); Ultimate Camper Van shoot shifted outside to avoid set build [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); Intel Home Upgrade for David only Friday "if we kick ass leading up to Friday" otherwise shorter easier videos [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

**Distribution rule he states for replication:**

> "Another thing to think about is how all those videos we're gonna make in a week, are distributed throughout that week, because we can't make 17 or 18 videos in one day. So a Gantt chart is a good tool for that. Obviously, there's videos that never move, TechLinked is always Monday, Wednesday, Friday, but things like the LTTs, it's way better to spread them out, we can't really do more than two in a day, reliably." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "It's actually a good thing to shoot a bunch of videos all at once, try to shoot three or four videos in a day and then allow for Linus to go do something else. It doesn't actually cause problems for the editing department, because then we just have a bunch of videos and they can be divvied out to individual people." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "This week, I've got a stack of three on Thursday, even though we try to avoid this, a lot of the time a writer starts a project on Monday and is ready to shoot it on Thursday or Friday. So it's pretty typical to see a stack on Thursday." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "I think this is manageable, but if you can shoot two on Monday, the rest of the week is so much easier. So today Linus is doing a thing that he does once a week, which is called, Floatplane lunch, so here I have on the phone, Luke." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — Floatplane call around lunchtime where Linus as CEO of Floatplane "doesn't really see the day-to-day ... If he has any input, he can throw it on us at that time" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

**Verified vs claimed:** 17 = 7+1+1+3+3+2+1 decomposition is his own count on that week [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). Seven LTTs/week is consistent with daily uploads claimed in 2017 [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) and with 7,009 videos lifetime [Wikipedia — Linus Media Group](https://en.wikipedia.org/wiki/Linus_Media_Group) → ~7009/≈13.5 years ≈ 10/week across all channels, not 17 LTT-only — 17 is LMG-wide that week, not his solo output. The "1 video every single day including weekends" 2017 line [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) and the 2021 17/week line [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) are two snapshots, not a stable claim — evolution noted.

---

## 2. Tooling: from video tracker spreadsheet with conditional formatting to monday.com and a Gantt

2017 stack: "all the projects are added to our video tracker spreadsheet which contains all the deadlines and progress info for all our projects we use fancy conditional formatting to make the colors change automatically then the video status is updated and we use the exact same project names here on the server and on the calendar so that every part of the project is easy to find no matter where you're looking" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).

2021 stack: monday.com. Forum description: "Thanks to monday.com for sponsoring this video! Get a 30 day Pro plan trial for free at https://lmg.gg/G4WPB In this video, we follow a typical week at LMG as the team works to shoot all the Linus Tech Tips, ShortCircuit, and TechQuickie videos that our fans expect." [LTT Forum Topic](https://linustechtips.com/topic/1344340-how-we-make-17-videos-a-week/).

In-video monday.com language:

> "The writer's meeting is where leads come in, either from the writers themselves or from the business team for sponsor projects. We evaluate them and then we assign each writer, a project to work on for that week and it all gets put into Monday, so that anyone in the organization can see it and follow along." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "But, with monday.com, it doesn't matter if you're on your parents' computer or pulled over on the side of the road using your phone." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) / "Everyone's updating their projects, all at one place." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "Before we had management involved, it was just chaos." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) / "Our ability to communicate is so much better now. Back in the old days we just used Excel to track all our projects, which was great when there was three us, but ... Nobody knew what anybody was doing. Nobody knew what was finished." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

ONE Day variant (TechLinked daily) shows monday.com automation at column level:

> "the very first thing i do when i get to the office is open monday.com ... i have my dashboard set up so i have all of the tasks that we need to complete for tech linked right there ... they actually auto populate every monday wednesday and friday" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "i go to monday.com and i click done on gather sources and because of the automation that i've set up that'll actually send a notification to dennis and then he can start screenshotting them and putting them in the timeline it's one click and it's all done" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "i think it's really convenient ... not just using like a group messaging service ... where i can put in on monday.com that the set is prepared and that it'll notify riley automatically" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "once i'm done filming i ingest the footage and then i update the monday.com which will send a notification to dennis that he's ready to start editing" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "after we've reviewed it's a matter of dennis rendering the video and then when that's done he marks done on monday.com i get a notification that it's ready to upload i upload and publish" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

2023 reform reframes tooling as process, not software: "flowcharts are good for more than just memes and we have just such a process now every video with Labs testing will be checked by Labs one to two times before shooting and then an additional time after the video has been edited any show stopping issues found during these reviews will do exactly that they will stop the show" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

**Verified vs claimed / caveat:** monday.com praise sits inside a sponsored video [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) and ONE Day's monday.com walkthrough is also monday.com sponsored [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) — treat efficiency claims as marketing-adjacent self-report, not independent benchmark. Excel → monday.com evolution is self-reported but consistent across two separate sponsored videos 2017 spreadsheet → 2019/2021 monday.com [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) / [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) / [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). The Gantt's claim that it allows non-Monday work to "chip away" is documented that Monday Linus kid day [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

---

## 3. Writer's meeting → assignment — the greenlight in their words

As above, the 2021 definition is the greenlight: leads from writers or business team for sponsor projects, evaluate, assign each writer a project for that week, into monday.com visible to org [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

Example reactions in meeting: "[Linus] As we finish going through people's sections, feel free to sign out and get back to work, 'cause I think we're a little tight this week. I mean, this is work, but like... So... Who does not have something they're turning in this week?" — "[James] I'm listed so far with Anthony and Alex." — "[Linus] Okay, Anthony's busy. Alex, do you need an easy one to bang out here?" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — freelisting capacity.

Follow-up line explicitly about time famine: "The hardest part of working here is when something goes wrong and then you suddenly just have to pull a video straight out of your butt." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — fielded as choosing "silicon shortage or water-cooled PS5? PS5 would be more, Linus time, most likely." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

**What is NOT documented:** no scoring rubric for lead selection is stated beyond early 2021 sponsor vs writer-origin [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); no intake form template shown. Thin — stated and stop.

---

## 4. Script Review — Linus as the single-node style gate and when to steal his time

Script Review is defined as writer-finished-before-shoot, writer sits with Linus, go through whole script for factual accuracy, flow, excitement, hook:

> "Okay, so it's quarter to noon and Linus is finally sitting down to do the first Script Review of the week. Script Review is what happens when the writer is finished writing a script, but before we shoot it, they sit down with Linus and go through the whole script looking for factual accuracy, flow. Is it an exciting video, does it have a good intro that's gonna hook you guys? All that kind of stuff. Once it's done, we switch the status of that item to, Script Reviewed and that triggers an action for our friend, Geoff, to go in, add sponsors to the script. And then when he's done that, put it onto the teleprompter so we can shoot." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

Proactivity praised: "You're being very proactive, it's 9:30, Linus has just got here and you're already Script Reviewing. That is exactly what we need to succeed today, 'cause we need to shoot three videos today." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — and conflict: "I actually don't know Anthony's readiness level yet. Well, ideally, we can shoot all three of these today, so that we have a full day tomorrow to do David's Intel Home Upgrade." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

2017 version of same gate, pre-monday.com, with same hour-long cost:

> "I harass the writers to update me on their progress so that I can schedule a time for them to sit down with lonus for script review the more people we hire the tougher it is to get one-on-one time with lonus but at the same time these script reviews even though they can take as long as an hour or more have become more important than ever to ensure that even though lonus is written less than 25% of our videos this year all our content still maintains a consistent style dick jokes and all" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "So, let's do a scripted voiceover as much as we can." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — decision point for Linus-time rationing.

Charge for lunch used as scheduling leverage in the transcript: "So buddy, how bad do you wanna eat lunch today? - You've lost your lunch privileges." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

**Verified vs claimed:** One-hour script review [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) and quarter-to-noon first review that week [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) are that week's observations, not SLAs. "<25% written by Linus" is 2017 self-reported [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), not re-measured in 2021 video.

---

## 5. Sponsor injection → teleprompter → Ready-to-shoot Checklist

Sequential trigger chain:

> "Once it's done, we switch the status ... to, Script Reviewed and that triggers an action for our friend, Geoff, to go in, add sponsors to the script. And then when he's done that, put it onto the teleprompter so we can shoot." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "Once a script is reviewed, has sponsors on it and is on the teleprompter. The writer will come downstairs and work with the shooters to complete this, the Ready-to-shoot Checklist. This thing exists because Linus was sick of coming down to shoot and finding out they weren't actually ready for him." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "Once that's done and only then, you can send a notification to Linus saying that, the video is actually ready to shoot and he or whatever host there is, will come to the set and do the talky talky." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

Corollary — sponsor pickups as separate line item that doesn't help the weekly count:

> "Now everybody knows LTT is famous for its sponsor, Segues. We don't always get to do the sponsor read in the video naturally, but when that happens, we film them like this 210314 Pre-roll keysight." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "We call it sponsor pickups and that's what Linus is gonna do right now. It's an annoying thing, that's in his schedule, that doesn't help me fulfill my goals." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

2025 spend video reframes sponsor economics as business-system, not just screen time: Sponsorships 21% of 2024 revenue with invideo reads 9% and dedicated sponsor videos 12%, across 13 categories (PC parts 34.6%, SaaS 25.5%, lifestyle 13.6%), 26 partners in PC parts, 150+ overall, none >5% — "Business 101 says to diversify" [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE).

---

## 6. Shoot — A-roll/B-roll split, guidance, lights, and who's on camera

2017 handoff definition still used as terminology:

> "sometimes the first major handoff is from the writers to the shooters the people behind the camera I assign one shooter to film The a roll that's the footage of the host talking and another shooter to film the b roll that's all the other footage you see like shots of the product or silly skits or whatever" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "and next time you see a product appear in 5 to eight locations consider that it can take up to 45 minutes to wipe the fingerprints off the product set up the 2 to six lights being used and Wrangle up any actors you may need hello Hollywood I'd like one actor please" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "the writers meet with a b-roll shooter to collaborate on the visuals that will accompany the host voiceover by the time this meeting is over nearly the entire script will have what we call guidance and we call it that because it's a suggestion for how it should be done but we don't want to take all the creative freedom away from the folks further down the production chain" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

Staffing named in 2017: "Brandon and Max are a regular Shooters but if we're in a hurry sometimes I just grab whoever's available since most of our editors are actually pretty handy behind the camera too hey I need someone to shoot something real quick I can help Dennis I know you're not doing anything let's go" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw). In 2021 week: shooters are Andy, Brandon, David — "we only have Andy, Brandon and David and then Brandon is actually offsite, doing the B-roll for that van upgrade video. They're out in the woods setting up solar panels" leaving "we don't have any shooters here that are our normal shooters" on WAN Friday [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); Ed and James figure out how everything's going to go together and how it's going to get uploaded, Ed tells editor to work late [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

ONE Day TechLinked shows same split at daily scale:

> "once i've written the three main stories and then i've gotten to the quick bits section i let the shooter know that i'm going to be done the script in about 15 minutes because that's about as long as it takes me to write the quick bits" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "technically you set up in a moment it's a little late i'm sorry wait you don't say sorry to me i say sorry brandon i love everything you do" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "it's like we're telepathically linked" after monday.com notification [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

LTT business video adds the host-availability constraint for replication:

> "Vlogs are more difficult to edit than something that's scripted already." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) and decision gate "It depends what they are. If they're all vlogs, that's harder for our people to do than for you to do, so if we have scripted stuff, then..." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) when asked "can you guys shoot videos while I'm gone?" — scripted decouples Linus presence.

---

## 7. Ingest → Edit → Pickup → QC — where time actually goes

**Ingest as defined:**

> "next the shooters have to ingest their footage putting it in a specific location on our server where the next people in the assembly line the editors will know where to look for it" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) / same ingest step after TechLinked shoot: "once i'm done filming i ingest the footage and then i update the monday.com" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "a lot more went into hooking up our ingest stations than just hooking up an SD card reader we're able to ingest footage at 200 to 300 megabytes per second keep your eyes peeled for an upcoming video all about our inest process and server infrastructure upgrades" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

**Edit:**

> "once all the shots are on the server the editors can get to work put putting it all together they use the writer's guidance to arrange all the shots and of course add their own flare some of which is subtle and some of which is pretty obvious" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "these jokes are horrible so while dennis is editing it's time for me to make the thumbnail" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) — parallel thumbnail while edit runs.

**Pickup when edit finds gaps:**

> "but it's not always smooth sometimes the editors find out that a shot is too short compared to the voiceover or maybe the host misspoke or some shots are just flat out missing then we'll have to find someone available to shoot a pickup so the editor can keep working" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "(indistinct), just gonna do a pickup for gold controller and then a sponsored Vizio ShortCircuit. - Not sure we'll do all of those things today." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "after Taran pulls an all nighter and uses all 200 of his macro Keys finishing up the video it's time for quality control" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

**QC chain:**

> "the writer sits down with the editor and reviews the video to make sure the information is accurate and that no unreleased products or email addresses accidentally wind up in the background then another editor usually me or Taran reviews it for glitches and then finally assuming we can find him lonus reviews it" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

2025 quantified cost of that chain: "For our camera team, it takes usually about 8 to 9 hours. And then it gets passed on to our editor team. Usually takes about 27 hours to get a copy for our writers to review." [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg) — plus writer's time "At the low end, I would say it's 8 hours, but at the higher end, it could be a year. On average, though, it's probably about 24 hours of work time on a project, but it's hard to count things like coordination" [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg); logistics "With an on-site assistant, we spend roughly 90 minutes per project." [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg)

2023 reform adds a formal flowchart on top of that QC, specifically for Labs-tested videos: "every video with Labs testing will be checked by Labs one to two times before shooting and then an additional time after the video has been edited any show stopping issues found during these reviews will do exactly that they will stop the show" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

WAN-week reality check on how QC competes with publishing:

> "Well, it's Friday, which means it's WAN Show day and the host of the WAN Show don't just go off the top of their heads, they have notes in the WAN doc. So, every Friday at about 10 a.m., a notification comes up automatically from monday.com, that says, hey, it's WAN SCRUM and that tells every writer to go and contribute one or two stories and then I go and look over it and I reorder the stories for most interesting, to least interesting." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "My guess is that they're scrambling to finish and he hasn't even left Vancouver, so I'm gonna call 'em... Did you hear the despair in his voice?... And so then the question becomes, do we just push WAN Show to be super, super late or get someone else to co-host the WAN Show? Which Alex actually volunteered to do, so he walked down here ... and he turned around and came back and said, apparently it's gonna be a 7:30, three hours late WAN Show." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

**Thumbnail as last-mile:**

> "and finally it's time for you guessed it our wonderful thumbnails we try to shoot these on the green screen and then use SPL shop to make them more how you say clickable before posting them online" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)

> "before i can do the thumbnail i need to find a face that linus is making that is suitably grotesque the thumbnail and usually that means i have to scrub through the video uh the end portion of the video where linus makes a lot of crazy faces" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

> "okay thumbnail time okay wait oh my gosh i can't believe it no yeah give me straight at the camera like you're pissed perfect i love that i love those faces you make" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM)

**Verified vs claimed:** 200–300 MB/s ingest [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) is claimed hardware capability, not benchmarked in doc; 8–9h camera / 27h edit / 24h writer avg / 90m logistics [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg) is self-reported by department leads in a 44-second short — treat as claimed, directionally consistent with 2017 macro-keys all-nighter anecdote [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).

---

## 8. Open / hook — what he actually says, and what he doesn't

The only first-party hook definition appears inside Script Review:

> "looking for factual accuracy, flow. Is it an exciting video, does it have a good intro that's gonna hook you guys? All that kind of stuff." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

No timestamped open template (0:00 cold open must do X, 0:15 stakes, 0:30 promise) is documented, no retention graph is shown, no first-30-seconds script recipe is given beyond "good intro that hooks" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). By contrast, TechLinked's *delivery* is characterized as performance-led: "I would describe techlinked as the tech news but we don't care about the tech news ... it's one take because that's all i have time for and if it's kind of weird and goofy or i miss something ... i'm just be like yeah this is a stupid joke forget it" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) — one-take looseness is the hook, not a formula. ONE Day also shows thumbnail face-search *after* shoot selects grotesque Linus face for click [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM), but no CTR target is stated.

**Sources thin on hook — say so explicitly and stop.** No first-party A/B test count, no hook minute-mark architecture, no CTR/AVD threshold is published by Linus in any 2021–2026 doc on file. Do not pad with MrBeast-style retention doctrine; Linus documents factory gates, not viewer-retention tactics.

---

## 9. Structure — no narrative act template; the Gantt *is* the structure

Linus never publishes a story-beat map (problem→solution→twist) for an LTT explainer in any doc on file. The only structure he codifies is calendar distribution and handoff sequence:

- Distribution: TechLinked fixed Mon/Wed/Fri, LTTs spread ≤2/day via Gantt, Thursday stack typical [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
- Handoff: Writer → Script Review (Linus) → Geoff sponsors → teleprompter → Ready-to-shoot Checklist → notification → A-roll/B-roll (+ guidance meeting) → ingest → edit (guidance + flare) → pickup if needed → writer+editor review → Ed/Taran glitch review → Linus final → green-screen thumbnail (SPL shop) → publish [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) / [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

He acknowledges structure variance by topic: "If they're all vlogs, that's harder for our people to do than for you to do, so if we have scripted stuff, then..." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — and "Vlogs are more difficult to edit than something that's scripted already. It takes a mental strain, where you have to just go home and ... Well, I just watch YouTube or something and just zone out." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) / "Scraps guys, fully scripted videos." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — scripted decouples host presence; vlogs couple it.

2023 reform adds structure at verification layer but not at narrative: "we reduced video output to get a handle on all of our new quality focused process changes we have officially killed the haven't missed an upload in 10 plus years mentality and we've made it explicitly clear that if a video is not ready for prime time we're going to stop the presses until we've had a chance to make the proper fixes now that might sometimes come in the form of an on-screen correction but there's going to be better transparency we've created a clear rubric that defines error severity and prescribes the appropriate fix which can range from a pinned comment to a full reshoot or even the outright cancellation of the video" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

**Sources thin on narrative structure — say so explicitly and stop.** Do not infer act breaks Linus never names.

---

## 10. Pacing — "scripted is easier than vlog" is the only first-party pacing rule

The only explicit pacing contrast he repeats:

> "Vlogs are more difficult to edit than something that's scripted already. It takes a mental strain" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "Scraps guys, fully scripted videos." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

> "I think we're doing more scripted content these days, I could be wrong, am I wrong?" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)

ONE Day quantifies pacing consequence for the only place he must ship in hours: TechLinked is "is very intense challenge for me every day and they try to be funny so hard but as you can see in most of my editing time i'm not really laughing because i just i don't know it's because the jokes are not funny or just because i was under really really high pressure" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) — edit under daily pressure, one take [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM), versus LTT's multi-day handoffs.

He also documents the *counter-pacing* lever after 2023: allowing formal rigor to slow him: "That is not going to stop, but others like GPU and CPU releases certainly require all the rigor we can muster. Those launches don't happen as often these days, so it will take some time before you see the full payoff of our continuous improvement, but it has already started happening. Not only did the community love our 4060 review, but our team found it less stressful to put out." [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — and "we have officially killed the haven't missed an upload in 10 plus years mentality" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

**Sources thin on numeric pacing — say so explicitly and stop.** No cuts-per-minute, no music/SFX bible, no retention-graph pacing rule is published by Linus in these docs.

---

## 11. Retention, editing rhythm, and packaging — only what he shows

**What he shows:**

- Thumbnails: shot green-screen then "use SPL shop to make them more how you say clickable" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); for TechLinked, scrub for "suitably grotesque" Linus face at end portion [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) and direct "give me straight at the camera like you're pissed perfect" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM).
- Edit flare: "they use the writer's guidance to arrange all the shots and of course add their own flare some of which is subtle and some of which is pretty obvious" [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).
- Sponsor integration as retention hazard: pickups are "annoying ... doesn't help me fulfill my goals" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — later 2023 business side systematizes disclosures: "if a sponsor doesn't like it, we'll just drop them like we've dropped so many others" and open forum sponsor complaint thread with weekly updates, internal sponsorship guidelines now public [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

**What he does NOT document (thin — stop):**

- No CTR/AVD/AVP targets, no thumbnail A/B test count or tooling named (beyond SPL shop/Photoshop inference), no chapter-card or end-screen retention doctrine, no sound-design or color-grade recipe. He says "it's the team's job to know thumbnail iteration" nowhere with a number in these docs — thin explicitly.
- The Labs laptop workflow *does* document retention-adjacent rigor at the **data** level, not viewer-retention level: bloat removal (McAfee/Norton) and full reset, write down default power profile then switch to most battery economical (super battery), 20°C environmental chamber, 720p YouTube playback at 200 nits 100% scaling keyboard RGB off with Hardware Info logging, endurance overnight, second max-stress test (prime95 + combuster), Markbench automated gaming suite, weight-class sort via Total War Warhammer 3 1080p quick bench to decide Esports vs Cyberpunk tier [Two Years Lab](https://www.youtube.com/watch?v=Qju1aITk_WY) — but that is test-methodology, not edit pacing.

Every viewer-retention claim above carries a first-party link where it exists; the gap is flagged, not padded.

---

## 12. Cadence — the factory's dial, and why he turned it down

**Documented dial positions:**

- 2017: daily including weekends, 1/day [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw).
- 2021: 17/week LMG-wide with ≤2 LTT/day via Gantt, Thursday stack, floatplane lunch, WAN scrum Fri 10am, 3-hour-late WAN possible [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
- 2019 ONE Day variant: TechLinked daily obligatory Mon/Wed/Fri auto-populated, gather sources → writer notifies Dennis → screenshots → timeline movement → quick bits finish in 15 min warning to shooter → set prepared notification → one-take shoot → ingest → Dennis edits while Riley makes thumbnail → review (Riley/Dennis) → render → monday.com done → upload/publish [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM).
- 2023 turn-down: "it's about a four month process for each video" is Johnny Harris, not Linus — Linus's stated fix is simpler: kill streak. "we have officially killed the haven't missed an upload in 10 plus years mentality and we've made it explicitly clear that if a video is not ready for prime time we're going to stop the presses until we've had a chance to make the proper fixes" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo); plus Labs-tested videos checked 1-2x pre-shoot + post-edit with show-stopping stop [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo); plus "for the first time in over 12 years, LTT will be missing not just one daily upload, but many. But improving to the degree that we want and need is going to take more than a week" [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY); plus weekly writing team postmortems [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo); plus open-sourcing Markbench harnesses and publishing testing standards living documents [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY).

**Hours dial that makes cadence possible:**

- Writer avg 24h (8 low, up to year), logistics 90m with on-site assistant, camera 8–9h, edit 27h to writer review [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg).

**Business dial that funds cadence:**

- 2024 finalized revenue split pie shown in video [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE): LTStore.com 55% (up from 15% in 2020), shipped 1M+ orders, hand tools + bags ~half, Black Friday 45% YoY growth and 60% faster fulfillment than 2023 [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); AdSense down as % (was 18%→26% 2016→2020, now smaller share — claimed good because less reliance on Google) [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) — 61.5% of AdSense from ads, 37.3% from Premium (55% of Premium fee split by watch time; Shorts 45% creator share; top Short 13M = $1,300 vs top VOD 20× more per view vs live archive 1.8c per view; LTT main = 76% of AdSense, ShortCircuit/TechLinked podium) [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); Sponsors 21% (9% invideo reads +12% dedicated, 13 categories, PC parts 34.6% SaaS 25.5% lifestyle 13.6%, none >5%, 150+ partners) [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); Affiliate Links ~3% [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); Floatplane 7% (up 1%, offer $5/$10 4K tier, lost ton after great reset Aug 2023 then 3 pushes back to near where left off) [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); misc <1% [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE). All percentages self-reported from 2024 pie [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE), not audited — flagged verified-vs-claimed below.

---

## 13. Replication — how he scales the factory without just adding Linus hours

**Headcount and footprint:**

- 120 employees as of January 2026 [Wikipedia — Linus Media Group](https://en.wikipedia.org/wiki/Linus_Media_Group) (infobox last updated Aug 2026 via verification).
- That week in 2021: writers, shooters (Andy/Brandon/David), editors, Geoff (sponsors/teleprompter), James/Ed (management/uploader), plus merch meeting weekly 9:30–11, plus construction/city calls [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).

**Role specialization as replication:**

- Ed as cat-herder owner of stage map [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) → by 2021 Ed + James as co-coordinators who "figure out how everything's going to go together and how it's going to get uploaded. Ed's the one that has to tell the editor, hey, you get to work late" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
- In 2017, only brand inject was Geoff → teleprompter [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); in 2021 same Geoff step triggered by Script Reviewed status [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
- Writer writes <25% by Linus in 2017 [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) → Script Review keeps voice consistent without Linus writing; later Linus says hiring CEO is explicitly to preserve his creativity while leadership scales [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE).

**What replication is NOT at LMG:**

- Not thumbnail iteration at scale beyond "SPL shop clickable" and grotesque face scrub [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) / [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) — thin, no 20–50 options doctrine like Veritasium.
- Not AI/test-retest for viewer retention — his science replication is Labs data rigor (heartbeat system for item tracking to avoid "we don't need it back" turning into loan, Christmas party pile confusion) [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) and method open-sourcing [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY), not content virality cloning.

---

## 14. Replication without burnout — in his and his team's own admissions

Linus is unusually blunt about human cost even before 2023 crisis:

- Monday kid day inviolable: "Linus isn't in on Mondays. He spends Mondays with his kids" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — used as scheduling constraint the team must work around.
- Same week headache: "It's 10:15 in the morning on Tuesday and I already have a splitting headache." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)
- Scripted vs vlog strain as burnout lever: "Vlogs are more difficult to edit than something that's scripted already. It takes a mental strain, where you have to just go home and ... Well, I just watch YouTube or something and just zone out." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — push to "Scraps guys, fully scripted videos." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE)
- Construction/city impingement on merch meeting 9:30–11 pushed back half hour by impromptu construction meeting at 9:30 plus 10:30 city call — "I don't know what we're gonna do, man." [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — example of 2021 coordination fragility before 2023 process formalization.

2023 crisis as burnout articulation (team, not just founder):

> "it's been a long time since my boss called me into their office and gave me a string talking to ... But the good news is that most of what the boss that's you is asking for has been underway for months or in some cases even years ... Under New Management ... step one was an all hands meeting to hear directly from everyone ... step two was to kick off an unprecedented company-wide period of introspection no videos no tweets no product launches for an entire week we have done almost nothing but dig through every misstep and conduct face-to-face meetings between our teams with the goal of surfacing the communication and the teamwork challenges" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo)

And the fix he sells as anti-burnout realism:

> "I'm only 6 weeks into the job... I asked the team to unflinchingly address both the concerns that have been raised and how we intend to move forward ... There's a lot of both." [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — Terren CEO intro.

> "Yvonne lays out the plan for content reduction ... Gary, head of labs talks transparency ... James, head of writing on process improvement ... Ed, head of production on communication ... Nick ... on quality control" [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — chapter list from description.

> "We will be spending our time looking at how we can improve communication ... A personal task for me will be putting the finishing touches on some cool ways we can make small edits that avoid the slap dash text on screen corrections whenever possible." [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — Ed.

> "We know that some of our best videos are centered around Linus and other members of the team just goofing around with tech and having fun. That is not going to stop" [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — James, explicitly guarding joy vs rigor balance.

> "Our morning and night surveillance footage of our parking lot at the studio for five work days leading up to our week of introspection ... some people roll in starting around 8 30 and then as you can see the ones who arrive later are typically gone by around 6 30 ... Our cleaning contractors come in after hours so that's their van ... to characterize our environment as some kind of 24 7 Sweatshop is frankly ridiculous ... We also do work overtime sometimes ... but we care ... turnover ... from 2013 to 2023 inclusive our average turnover rate was 7.5 percent with a median value of 7.7 ... Workforce research for Mercer ... Canadian average is 18 ... in the U.S it's around 20 percent ... even then we were lower than average ... removing the people who were dismissed ... 3.65 average 1.9 percent median" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo)

> "We offer a solid benefits package including extended Health mental health and dental coverage as well as Retirement savings contributions and matching we proactively host regular team building events including summer of fun which gives every full-time local employee up to 300 to spend on any activities they want ... bi-weekly gaming nights in the lounge with free food weekly badminton nights bi-weekly softball nights and a quarterly budget for department-wide team building events ... surprise field trips where people are paid to have fun ... Christmas parties ... surprise bonuses ... ten thousand dollars in bonus money per person not once but twice ... effective September 2023 we have doubled our coverage for mental health counseling ... we engaged an outside HR Council ... 25 employees ... outside HR firm ... 40 team members ... dedicated in-house HR department with the goal of providing even more resources ... Yvonne and I do both still have an open door policy" [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo)

**Verified vs claimed:** Parking-lot footage and turnover stats are his own 5-day sample and 2013–2023 internal HR calculation presented in [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) — not independently audited; Mercer 18%/20% is cited as external benchmark inside same video — treat as claimed framing. Mental health doubling Sep 2023 [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) after harassment is claimed response to documented community outcry that week. The "haven't missed an upload in 10+ years" kill [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) contradicts 2017 "every single day including weekends" brag [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) — flagged as evolution, not lie; cadence intentionally reduced to protect people.

---

## 15. Caveats, contradictions, verified-vs-claimed — explicit

**Every developed workflow step above has a first-party link. Steps he does not document are explicitly skipped below — not padded.**

**Thin / not documented first-party (say so explicitly, stop):**

- **Open/hook formula:** No cold-open template, no first-5-seconds doctrine, no retention-graph walkthrough in any doc on file. Only "good intro that hooks you" during Script Review [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). Sources thin.
- **Structure:** No narrative act structure beyond calendar Gantt [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) and handoff chain [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) / [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). No problem→solution thesis stated like Veritasium. Thin.
- **Pacing:** No numeric rhythm, no beat sheet. Only "scripted easier than vlog" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) and one-take loosening for TechLinked [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM). Thin.
- **Retention dashboard:** No CTR/AVD/AVP targets, no chapter-card timing, no A/B win-rate. Thumbnail made via SPL shop [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) and grotesque-face scrub [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) without numeric goal. Thin.
- **Editing rhythm:** No cuts-per-minute, sound-design or color recipe. Only guidance→flare, pickup for short vs VO, 27h edit → writer review [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg), 200 macro keys [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), and quirky TechLinked "jokes are horrible under pressure" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM). Thin beyond handoff description.
- **Course / paid workflow:** No course. Forum topic is strategy walkthrough, not curriculum [LTT Forum Topic](https://linustechtips.com/topic/1344340-how-we-make-17-videos-a-week/); Floatplane exclusives referenced as $5/$10 tiers [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) but paywalled — only public sponsor mentions used, never fabricated.
- **Independent benchmark:** No first-party+INDEPENDENT 2021–2026 doc exists — all workflow docs MONETIZED (monday.com, Lenovo, MSI, Odoo, Intel) per provenance. Treat sponsor praise as marketing.

**Contradictions / tensions:**

- "We release a video every single day including weekends" 2017 [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) vs "we have officially killed the haven't missed an upload in 10 plus years mentality" 2023 [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) — explicit reversal after community/Bilbo Labs crisis; workflow was intentionally slowed to add Labs 1–2× pre-shoot + post-edit checks that stop the show [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).
- "If you ... only work on one video during a day, you failed as a MrBeast employee" is MrBeast, not Linus — Linus's inverse is "we can't really do more than two [LTT] in a day, reliably" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) and "we can't make 17 or 18 videos in one day" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE). Contradiction flagged because both document factories but with opposite flex — MrBeast parallelizes per person; LMG parallelizes via Gantt distribution, not per-person overload. Not padded as flaw, noted as design choice.
- "Vlogs are more difficult to edit than something that's scripted already" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) vs "Some of our best videos are centered around ... goofing around ... That is not going to stop" [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY) — tension between burnout-costly vlog and joy-preserving vlog; resolved by labeling rigor tier by launch type [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY).
- "Nobody knew what anybody was doing ... we just used Excel ... great when there was three us" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) vs now "Everyone's updating their projects, all at one place" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) — same contradiction as MrBeast's Hollywood claim, but for Linus it is stale-tool vs sponsored-tool evolution.
- Money pie 55% store 2024 [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) vs "we literally call ourselves YouTubers" [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) — flagged self-awareness: AdSense% down called good due to diversification, not failure.

**Verified-vs-claimed flags:**

- All finance percentages are 2024 finalized revenue split shown in-video [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) — self-reported, not audited financials; no dollar amounts ever given ("you'll notice that we never gave you guys any specific dollar amounts ... there really are some things we just can't talk about" [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE)).
- 17-video breakdown [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE), 1/day including weekends [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), 16.9M/9.63B infobox [Wikipedia — Linus Sebastian](https://en.wikipedia.org/wiki/Linus_Sebastian) vs yt-dlp 16900000 [YouTube @LinusTechTips](https://www.youtube.com/@LinusTechTips) — directionally verified; exact view counts dated.
- 200–300 MB/s ingest [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), 24h writer avg / 90m logistics / 8–9h camera / 27h edit [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg), 50% growth and "quadrupled" expenses parallel not claimed here — Linus never claims growth multiple, only process cost; those hours are claimed department-lead self-estimates in a 44s short [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg), not timesheet-verified.
- Turnover 7.5% avg / 7.7 median 2013–2023 inclusive, 3.65/1.9 ex-dismissals, Mercer 18% CA 20% US, parking lot 8:30–6:30 [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) — all internal calculation + self-selected 5-day footage sample — claimed, not audited HRIS export.
- Material Ning? Not used.

---

## 16. In his own words — compressed factory checklist to copy the 17/week model without copying his team size

1. **Count the week before you write the week** — tell writing team how many need to be made to hit target and not be screwed next week if someone's on vacation or parts arrive broken [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); for LMG 2021 that was seven LTTs plus WAN+clips+3+3+2+1 =17 [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); for TechLinked that is Mon/Wed/Fri auto-populated [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM).
2. **Gantt it and never bank a Monday** — put every project into Monday/monday.com so anyone can see it [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); never plan 17 in one day, never >2 LTT/day reliably [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); Thursday stack is pilot error (writers ready Thu/Fri) — shoot two on Monday instead [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); respect Linus not in Mondays — chip away anyway [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
3. **Evaluate leads then assign — one project per writer per week** — writer leads + business team sponsor projects evaluated in writer's meeting, assigned, into Monday [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); when tight, ask "Who does not have something they're turning in?" and hand easy banger [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); hardest day is when suddenly you pull a video out of your butt — have silicon-shortage vs water-cooled-PS5 fallback [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
4. **Steal Linus time only after Script Reviewed + Geoff + teleprompter + Ready-to-shoot Checklist** — Script Review for accuracy/flow/exciting intro that hooks [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) (hour-long when needed [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), tougher with more hires [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw), preserves consistent style despite <25% Linus-written [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw)) → switch status → Geoff adds sponsors → teleprompter [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) → writer+shooter complete Ready-to-shoot Checklist because Linus was sick of not-ready sets [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE) → then notification to host [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); sponsor pickups filmed separately as pre-roll and acknowledged as schedule annoyance [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE).
5. **Hand off with guidance — keep creative freedom** — assign one shooter A-roll host talk + one B-roll (product/silly skits) [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); budget 2–6 lights + up to 45 min fingerprint wipe per product [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); writers meet B-roll shooter to co-create visuals — script gets "guidance" suggestion not command [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); grab whoever's handy including editors if rushed [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); scripted decouples host for replication [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); ONE Day variant: warn shooter 15 min before quick bits done, one-take TechLinked with goof flag [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM).
6. **Ingest once to the right server path at 200–300 MB/s, then let editors flare** — distinct server location next pipeline knows [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); ingest notification triggers Dennis [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM); editors use guidance + own flare subtle/obvious [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); when VO too long/short or shot missing → find available shooter for pickup [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) via gold-controller pickup example [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); allocate 8–9h camera +27h edit to review +24h writer avg +90m logistics per project as 2025 budgeting anchor [how much does LTT spend](https://www.youtube.com/watch?v=Us7qSE44XOg).
7. **QC three-deep plus thumbnail green-screen** — writer+editor accuracy/pass (no unreleased product/email left in) → Ed/Taran glitch pass → Linus final if findable [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw); thumbnail green-screen → SPL shop clickable [How Our Videos are Made](https://www.youtube.com/watch?v=LtNdKoXbZMw) via grotesque-face scrub at end [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM) + directed "straight at camera like you're pissed" [ONE Day](https://www.youtube.com/watch?v=X3KLyDWPpEM); for Labs videos add flowchart: 1–2 Labs checks pre-shoot + post-edit stop-the-show if show-stopper [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).
8. **Accept thin on hook/retention — then decide stop rule** — no hook template beyond "good intro that hooks" [YouTube mirror gC6dQrScmHE](https://www.youtube.com/watch?v=gC6dQrScmHE); don't pad. Instead enforce stop rule: kill 10+ year streak — stop presses until proper fix (pinned comment → full reshoot → cancellation per error-severity rubric) [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) and weekly postmortems [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) + ECC Squad alpha (<10 external experts) as early-access fact check [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo) — trade speed for correctness.
9. **Fund the slowing** — know shift: 2016–2020 AdSense 18→26% now diluted, now 55% store / 21% sponsors (9+12) / ~3% affiliate / 7% Floatplane ($5/$10 4K) / <1% misc per 2024 pie [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE); intro-mission finance hire CEO 2023 so founder stays creativity pit while team steps up [Truth Money](https://www.youtube.com/watch?v=GeCP-0nuziE) / Terren fly-on-wall [What do we do now](https://www.youtube.com/watch?v=0cTpTMl8kFY); benefits, fun budget ($300 summer, gaming/badminton/softball), and HR scaffolding to keep turnover 7.5% vs 18% benchmark despite overtime reality and 8:30–6:30 window [Here's the plan](https://www.youtube.com/watch?v=qAE5KoyFEUo).

---

## Sources

- How We Make 17 Videos a Week — LTT Forum Topic (by mynameGeoff, 2021-06-03, 2021-06-10 updated_time) — FIRST-PARTY/MONETIZED — https://linustechtips.com/topic/1344340-how-we-make-17-videos-a-week/ — embedded video https://www.youtube.com/watch?v=gC6dQrScmHE — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__Running_a_YouTube_Business_is_EASY_just_kidding.txt` (manual `en`, `python -m yt_dlp` + `flatten-json3.js`)
- Running a YouTube Business is EASY (just kidding) | Linus Tech Tips | 2021-06-03 | 1164s | gC6dQrScmHE — same as above — FIRST-PARTY/MONETIZED — monday.com sponsor, `og:description` "we follow a typical week at LMG as the team works to shoot all the Linus Tech Tips, ShortCircuit, and TechQuickie videos that our fans expect."
- How Our Videos are Made | Linus Tech Tips | 2017-07-26 | 370s | LtNdKoXbZMw — FIRST-PARTY/MONETIZED (Lenovo Flex 5) — https://www.youtube.com/watch?v=LtNdKoXbZMw — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__How_Our_Videos_are_Made_2017.txt` — out-of-window historical context per `working/evidence/linus-tech-tips-2026-08-29.json` dead_ends_searched, used only for corroboration not as recency doc
- How We Make a Video in ONE Day | Linus Tech Tips | 2019-08-24 | 603s | X3KLyDWPpEM — FIRST-PARTY/MONETIZED (monday.com) — https://www.youtube.com/watch?v=X3KLyDWPpEM — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__How_We_Make_a_Video_in_ONE_Day_2019.txt`
- The TRUTH About How LTT Makes Money | Linus Tech Tips | 2025-03-25 | 991s | GeCP-0nuziE — FIRST-PARTY/MONETIZED (Odoo) — https://www.youtube.com/watch?v=GeCP-0nuziE — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__TRUTH_About_How_LTT_Makes_Money.txt`
- What do we do now? | Linus Tech Tips | 2023-08-16 | 1252s | 0cTpTMl8kFY — FIRST-PARTY — https://www.youtube.com/watch?v=0cTpTMl8kFY — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__What_do_we_do_now.txt`
- Here's the plan. | Linus Tech Tips | 2023-08-26 | 864s | qAE5KoyFEUo — FIRST-PARTY — https://www.youtube.com/watch?v=qAE5KoyFEUo — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__Heres_the_plan.txt`
- how much does LTT spend on each video? | Linus Tech Tips | 2025-09-03 | 44s | Us7qSE44XOg — FIRST-PARTY — https://www.youtube.com/watch?v=Us7qSE44XOg — transcript to `b0ttsagent/temp/youtube-transcripts/Linus_Tech_Tips__how_much_does_LTT_spend_on_each_video.txt`
- Why it took TWO YEARS to Build a Laptop Test Lab | Linus Tech Tips | 2024-07-04 | 950s | Qju1aITk_WY — FIRST-PARTY (MSI demo, LTT Labs) — https://www.youtube.com/watch?v=Qju1aITk_WY — manual transcript `Linus_Tech_Tips__TWO_YEARS_Lab_manual.txt` + auto `Linus_Tech_Tips__TWO_YEARS_to_Build_a_Laptop_Test_Lab.txt`
- Linus Sebastian — Wikipedia — https://en.wikipedia.org/wiki/Linus_Sebastian — verification baseline
- Linus Media Group — Wikipedia — https://en.wikipedia.org/wiki/Linus_Media_Group — headcount, dates, channel table
- Linus Tech Tips — YouTube channel — https://www.youtube.com/@LinusTechTips — `channel_follower_count 16900000` via `python -m yt_dlp --print` 2026-08-29
- SocialBlade — Linus Tech Tips — https://socialblade.com/youtube/handle/linustechtips — 16.9M / 9.74B corroboration

*No other first-party 2021–2026 workflow blog/podcast/interview with publicly readable body found beyond the above YouTube corpus + forum topic. Where Linus does not document a step (retention hook, CTR target, act structure, cuts-per-minute, A/B tooling), this note states the gap and stops. No paid Floatplane transcript fabricated; no marketing copy inference beyond sponsor-flagged self-report.*

