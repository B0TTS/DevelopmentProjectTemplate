# Case Study: Sam Sulek — The Zero-Production Daily Vlog (with TikTok Clips as the Discovery Funnel)

> **HYBRID CAVEAT (read first):** Sam Sulek's primary content is **long-form daily vlogs on YouTube** (car talks + gym sessions, ~30 min). His **TikToks are clips/cuts** — short-form-first in format, but *derived* from a long-form engine. His documentation depth is the **lightest in the shortlist**: only **2 first-party independent podcast sources** (Modern Wisdom #994, 2025-09-15; Cutler Cast #147, 2024-12-23). Per the shallow-output protocol, schema fields unsupported by those sources are marked **N/A + reason**. Nothing below is padded or invented.

---

## Header / Creator Meta

| Field | Value |
|---|---|
| **creator** | Sam Sulek (Samuel Bishop Sulek, b. 2002-02-07, Delaware, Ohio, USA) [source: Wikipedia] |
| **platform(s)** | YouTube (primary — daily long-form vlogs), TikTok (clips/edits — historically the seeding platform), Instagram (secondary, passive) [source: Wikipedia; Cutler Cast; Modern Wisdom #994] |
| **primary_niche** | Fitness / bodybuilding — documenting his own training, bulking, dieting, and competition prep [source: Wikipedia; vidIQ] |
| **verification** | LONG-CAREER-VERIFIED: career span ~2022 (TikTok) / Jan 2023 (YouTube) through present [source: Ex Nihilo; Cutler Cast; Wikipedia]. YouTube 4.49M subs / 346M views as of 2026-07-12 [source: Wikipedia]. vidIQ documented 8K → 2.26M subs in 2023 (1.8M of those in Aug–Oct 2023) [source: vidIQ]. TikTok @sam_sulek: 2.6M followers; 20 eligible videos (2023-09-04 → 2026-08-04) all ≥ 365K views, median ~3.35M (= 130% view-to-follower) [source: yt-dlp pull, this session — see Evidence section] |
| **source_date** | Primary evidence window: 2024-12-23 (Cutler Cast #147) → 2025-09-15 (Modern Wisdom #994); corroborated by 2023–2026 second-hand sources |
| **still_current_as_of_2026** | YES for the YouTube mechanics (daily vlogs, tripod format, authenticity framing — restated 2025-09-15, format still per Wikipedia Jul 2026). PARTIAL for TikTok cadence (TikTok has slowed to hiatuses/monthly posts since ~2024 — see `posting_cadence`) |

---

## Schema Fields (every populated field cited inline)

- **`hook_type`**: **visual** (for the TikTok clips) — the clip's hook is the physique/lift itself: "if you're squatting five plates in a little leg day edit people are kind of curious about what the train looks like behind that" [Cutler Cast]; "post a workout video that's just really cool and hype" [Modern Wisdom #994]. **N/A for long-form** — he explicitly rejects engineered hooks/intros: "I'm doing like a YouTube intro… that's just not what I do" [Modern Wisdom #994]; his first video is "the same as this one" [Modern Wisdom #994].
- **`first_frame_timing`**: **first 0–1s** (TikTok clips only) — his early clips were "a 5-second edit [with] transition music" — the whole clip is the frame [Cutler Cast]. **N/A for long-form**: no engineered first-frame; vlogs open with him already in the car [Cutler Cast: format = "Drive sets pose drive back"; Wikipedia corroborates car → gym → car structure]. No source specifies any hook timing rule because he doesn't use one.
- **`pattern_interrupt_cadence`**: **N/A — anti-framework**. He rejects the conventional interrupt toolkit: no jump cuts, no B-roll, no lower thirds, no special effects [vidIQ — SECOND-HAND]; no "welcome back to the show" style intros [Modern Wisdom #994]. The only recurring beat is natural, not engineered: "I'll say a little 5-second thing after a set… all the talking is in the car" [Cutler Cast]. No interval-based interrupt structure exists in any source.
- **`payoff_placement`**: **Immediate** for clips — the lift IS the payoff within the 5–10s clip [Cutler Cast]. **Deferred/serialized** for long-form — the payoff is the compounding progress arc: the recognizable look ("the hat, the hair, the oversized [clothes]… the clothes come off and everyone's like 'wow, this guy's actually got a physique'" — "that's kind of the big buildup") [Cutler Cast]; "There's not going to be Sam 2.0. It'll only be a gradual evolution… check back in two years and we'll have a lot of updates" [Modern Wisdom #994].
- **`loop_structure`**: **open-loop** — a serialized daily series: each video is one day of a continuing progress narrative, so the loop closes only by returning tomorrow ("the video I'm going to post **tomorrow** about working out is the exact same [format]" [Cutler Cast]; "Day 1,300 of the macro track" framing [Cutler Cast]). vidIQ (SECOND-HAND) independently notes daily uploads make "viewers… depend on his content" [vidIQ].
- **`retention_mechanism(s)`**: **escalating stakes** — the bulk-up/progress arc compounds daily (see `payoff_placement`) [Cutler Cast; Modern Wisdom #994]. **Plus 2 mechanisms outside the closed vocabulary — see `## New Terms`**: (1) *companion/ambient retention* — content consumed while doing cardio or falling asleep [Cutler Cast; Modern Wisdom #994]; (2) *deadpan-contrast captioning* — serious visual + absurd caption [Modern Wisdom #994]. Explicitly REJECTED: curiosity-gap/clickbait hooks and trend-chasing ("you can't just only post stuff that does well because that's when you get into… trend videos" [Cutler Cast]; "I'm not exactly even thinking like, okay, I want to improve my content engagement" [Modern Wisdom #994]).
- **`posting_cadence`**: **YouTube: daily** — "the dailies… it's a lot of work" [Cutler Cast]; "you have to do it every day… it's like training" [Cutler Cast]; vidIQ confirms daily uploads (266 videos posted at 2.26M subs, Nov 2023) [vidIQ — SECOND-HAND]. **TikTok: 2–3 posts/day at the start** [Ex Nihilo — SECOND-HAND], then slowed: video titles self-document the decay — "Your monthy post sir" (Oct 2023), "Yearly post" (Jun 2024), "Tiktok hiatus has come to an end" (Apr 2024), and multi-month gaps through 2025 [source: yt-dlp metadata, this session]. **Time-of-day rule: none** — "as long as it's reasonably consistent you're probably all right… you probably won't want to post them like 2 am" [Cutler Cast].
- **`replication_tactic`**: (a) Document the thing you **already do daily** — zero incremental effort: "everything that was being recorded was already going to happen anyway" [Cutler Cast]; "the best thing that you could do is pick something that you already do and you already like and just try to document that" [Modern Wisdom #994]. (b) **No "content days"** — never a filming day separate from a life day [Cutler Cast]. (c) **Freeze the format** — "the format hasn't changed at all" [Cutler Cast]. (d) Adjust in small, periodic analytics review — monthly look-back at what did well ("did I use fancier music… did I say something more natural") while never abandoning what you like [Cutler Cast]. (e) Expect **years with no reward** — "you ready to do that with no reward?" [Cutler Cast]; growth is "a steady kind of climb… 0.1% increases over time" [Cutler Cast; Modern Wisdom #994]. (f) Do not chase trends [Cutler Cast; Ex Nihilo].
- **`platform_specific_mechanics`**: **TikTok = discovery funnel**: ~6 months of 5-second joke edits with transition music seeded the audience; the clips created curiosity about the full workout ("people are kind of curious about what the train looks like behind that"), funneling to long-form YouTube [Cutler Cast]. **YouTube = the retention engine**: raw ~30-min daily vlogs; "a lot of guys want to watch the video during their cardio… 30 is the sweet spot" [Cutler Cast]; avg length 35.14 min / most-viewed 57:26 (Nov 2023) [vidIQ — SECOND-HAND]; YouTube has "the most real viewers and the most real feedback… there's a lot of intent to watch a whole workout" [Modern Wisdom #994]. **Instagram = passive**: "on Instagram… something can be shown to you, scroll it away, it's like nothing" [Modern Wisdom #994]. Framework verdict: **platform-specific mechanics** (each platform used per its native viewing behavior) over a **platform-agnostic core** (consistency + authenticity + zero production). No source frames the method as a TikTok-first or Shorts-first formula — it is long-form-first with clips as trailers.
- **`source_date`**: 2024-12-23 → 2025-09-15 (first-party); 2023-11-21 → 2026-07-12 (second-hand). All within the 2021–2026 window.
- **`still_current_as_of_2026`**: see per-source flags in `## Sources`.
- **`evidence_tier` / `monetization_bias`**: per source in `## Sources`. Summary: 2 FIRST-PARTY INDEPENDENT podcasts (no course, no community, nothing sold), 4 SECOND-HAND INDEPENDENT articles. **No MONETIZED source exists for Sam** — he sells no course; caveat: he does take brand sponsorships (Hostile, Raw Nutrition) [Ex Nihilo; Raw Nutrition Facebook — SECOND-HAND], so his "no monetization" framing applies to course/community products, not brand deals (see Caveats).

---

## Workflow / Framework Breakdown (step-by-step, each step ≥1 first-party source)

**Step 0 — Seed on TikTok with short clips before long-form.** "I did six months of like little editing like joke stuff like a 5-second edit transition music… it was a pretty strong following like small cuz it was all coming from TikTok" [Cutler Cast]. First YouTube video January 2023; ~100K TikTok followers accumulated before/while transitioning [Cutler Cast: "probably about four months into that when that account was like 100,000 followers"]; TikTok start ~July 2022 [Ex Nihilo — SECOND-HAND, consistent with Sam's own 6-months-before-January-2023 timeline].

**Step 1 — Pick something you already do every day and already like; document it, don't emulate.** "The best thing that you could do is pick something that you already do and you already like and just try to like document that… you already have something really valuable and it's your own individuality" [Modern Wisdom #994]. His format choice was borrowed from Rich Piana's "Bigger by the Day" daily-vlog format because it was seamless with his routine, and "nobody was doing" it at the time [Modern Wisdom #994]. Iterated 3 failed phone attempts before the first posted video (first failed on audio; sent to his brother for feedback) [Cutler Cast].

**Step 2 — Zero production: tripod, no videographer, no content days.** "I was going to work out anyway… throw the tripod on" [Cutler Cast]; "I used to think… if I want to be serious I need a videographer, but after like a few weeks… the tripod's like, this is perfect… not easy but smooth, just keep pumping them out" [Cutler Cast]; "everything that was being recorded was already going to happen anyway" — i.e., no dedicated filming days [Cutler Cast]. He rejected a camera crew ("I thought I'd get a camera guy cuz that's what everyone does") [Modern Wisdom #994].

**Step 3 — The one technical investment: audio.** "Maybe don't get a $20 mic from Amazon because it's going to sound real scratchy. That's like 30 percent — how you're showing off what you're doing" [Cutler Cast]. His first attempt failed precisely because "I didn't have a microphone and if you're in a gym… you can't hear anything" [Cutler Cast].

**Step 4 — Freeze a fixed daily format: Drive → talk in car → sets → pose → drive back.** "The format hasn't changed at all… the exact same: drive, sets, pose, drive back" [Cutler Cast]. Corroborated: "all his videos follow the same format, showing him speaking in his car on the way to the gym, his workout at the gym, then him speaking in his car again" [Wikipedia — SECOND-HAND]. He edits it himself ("do you do all the editing yourself too? — yeah") — minimal editing, not none [Cutler Cast].

**Step 5 — In-gym capture cadence: record every working set; 5-second bits between sets; ALL the talking happens in the car.** "I'll just record every working set… I'll say a little 5-second thing after a set, 'oh that was a good one, let's do another one,' cut to the next one. All the talking is in the car" [Cutler Cast]. He records the set "for me… nobody else watched it happen" — the workout precedes the recording, not vice versa [Modern Wisdom #994].

**Step 6 — Length: ~30 minutes, tuned to a specific consumption context.** "A lot of guys want to watch the video during their cardio… I think 30 is the sweet spot" [Cutler Cast]. vidIQ confirms avg 35.14 min (Nov 2023) [vidIQ — SECOND-HAND]. Same companion logic produced the sleep-content phenomenon: "there are 4-hour compilations of your car talks to go to sleep to" [Modern Wisdom #994 — Chris Williamson; Sam acknowledges "I actually heard that before"].

**Step 7 — Post daily, indefinitely.** "The dailies — I'll keep those up for a little while, it's a lot of work" [Cutler Cast]; when Cutler says "this is the first time I've heard someone just straight up say you have to do it every day," Sam answers "well, it's like training" [Cutler Cast]. No time-of-day optimization: "as long as it's reasonably consistent you're probably all right" [Cutler Cast].

**Step 8 — For shorts: deadpan-contrast captioning.** "Post a workout video that's just really cool and hype… but then the caption is just something silly, something you wouldn't expect… 'I had to cut this workout short today, my mom had to pick me up to go get groceries'… if you're big, you have already said that you are serious… to say anything motivational on top of that is putting a hat on a hat" [Modern Wisdom #994]. The "scared of women" bit ran on the same contrast: "big muscular dude… 'can I work in with you?' and then I just disappear" [Modern Wisdom #994; Cutler Cast].

**Step 9 — Periodic small analytics adjustments, never trend-chasing.** "Number one: consistent posting… but there's an extra step where you got to adjust a little… look back at 10 videos… 'this one did well' — go back, what did I do differently? Fancier music? Better editing? Something more natural?… But there's a balance: you have to post stuff you like. You can't just only post stuff that does well… before you know it you're doing a 10-OnlyFans-girls workout" [Cutler Cast].

**Step 10 — Long horizon; growth is gradual, not viral.** "You got to post this stuff for like years — you ready to do that with no reward?… you're not just going to be jacked after three posts… it takes a while to build it up" [Cutler Cast]; "the whole time… it was always just a steady kind of climb… there was never like it never went down… a gradual 5% up this week, 10 [next]" with one big YouTube spike in Aug–Dec 2023 [Cutler Cast]; "there was no moment where the frog jumped out of the boiling water because it just raised temperature super slowly" [Modern Wisdom #994].

**Step 11 — Anti-algorithm framing as the operative philosophy.** "I'm not exactly even thinking like, okay, I want to improve my content engagement… I want to boil it all down to the gym specifically… the better all my workouts are, it will bleed out and raise everything else up" [Modern Wisdom #994]; "my first YouTube video is the same as this one… it wasn't a Mr. Beast story of 'I analyzed the whatever'… if you tried to plan it in advance, it would have probably sounded like a failure" [Modern Wisdom #994]. Note the 2025 framing coexists with the 2024 analytics-adjustment advice (Step 9) — see Verified vs Claimed.

**Step 12 — Platform split.** YouTube = intent-to-watch retention engine (~4% female viewers on long-form) [Modern Wisdom #994]; Instagram = passive scroll (~20% female — "that's not really watching your stuff") [Modern Wisdom #994]; TikTok = discovery/clips [Cutler Cast].

---

## Evidence — View-Count Data (yt-dlp, @sam_sulek, pulled fresh this session 2026-08-13)

25 videos returned; newest (2026-08-13, 25.6K views, <24h old) excluded by the ≤2026-08-06 eligible rule. The 20 eligible rows (2026-08-04 → 2023-09-04):

| Range | Value |
|---|---|
| Count eligible | 20 / 20 |
| Min / Max | 722.6K / 10.2M views |
| Median | **3.35M** |
| All ≥ 365K (hit threshold) | **20/20 → hit_rate 1.0** |
| Newest eligible upload | 2026-08-04 (10.2M views) |

Median 3.35M on a 2.6M-follower base = **~130% view-to-follower** — he vastly outperforms his follower base on TikTok. Cadence decay is visible in the same data: dense Sep–Oct 2023 posting → "Yearly post" (Jun 2024) → multi-month gaps 2025 → partial return 2026.

---

## Verified vs Claimed

| Claim | Status | Basis |
|---|---|---|
| Daily YouTube uploads, ~30 min, tripod-only, self-edited | **VERIFIED (first-party)** | Cutler Cast #147 verbatim; corroborated vidIQ (daily, 35.14 min avg, Nov 2023); Wikipedia (format unchanged, 2024) |
| TikTok 5-sec edits seeded the audience; clips → long-form funnel | **VERIFIED (first-party)** | Cutler Cast #147 |
| Audio quality ≈ 30% of presentation | **VERIFIED (first-party)** | Cutler Cast #147 |
| Growth was gradual, no single viral video | **VERIFIED (first-party + data)** | Cutler Cast; Modern Wisdom #994; yt-dlp spread (0.72M–10.2M, no outlier cluster beyond one 10.2M) |
| "No edits" / raw footage framing | **PARTIALLY VERIFIED — overstated as stated** | vidIQ/NYT-style "lo-fi" framing is second-hand; Sam confirms he edits every video himself [Cutler Cast]. Correct claim: *minimal* editing, not none |
| "No analytics / no plan" (2025) vs "adjust via analytics" (2024) | **BOTH VERIFIED — reconciled** | MW #994 (2025): rejects *engagement-optimization as the driver*; CC #147 (2024): endorses *periodic small adjustments* after posting what you like. He never claimed to ignore performance data entirely |
| Posting time-of-day rules | **CLAIMED ABSENT** — Sam explicitly says timing is near-irrelevant | Cutler Cast |
| TikTok 2–3 posts/day at start | **SECOND-HAND only** | Ex Nihilo (2025) — consistent with, but not stated in, either podcast |
| Titles = "day number + bodyweight" | **SECOND-HAND only, unverified** | vidIQ/analyst claims; not stated in either first-party source; treat with caveat |
| Dominance score inputs (hit_rate 1.0, median 3.35M, newest upload ≤14 days) | **VERIFIED (this session)** | Independent yt-dlp re-pull reproduces the mission numbers exactly — see Evidence |

---

## Caveats / Contradictions

1. **Hybrid caveat (structural):** Sam is a *long-form-first* creator whose TikTok output is derived clips. His "formula" is a daily-vlog formula with a TikTok seeding layer, not a short-form-native viral formula. Any transfer to short-only creators is a judgment call, not something he documents.
2. **Lightest documentation in the shortlist:** only 2 first-party sources; both are podcasts (one auto-captioned). **Fields marked N/A (unsupported):** `pattern_interrupt_cadence`, long-form `hook_type`, long-form `first_frame_timing`. Everything else traces to at least one of the two podcasts; second-hand claims are flagged and do not count toward verification.
3. **Auto-transcript caveat:** both transcripts (provided MW transcript; yt-dlp auto-subs for Cutler Cast) are machine-generated; quotes are faithful in substance, approximate in wording.
4. **"No content days" wording:** the shortlist described the Cutler Cast as covering "no content days." The verbatim transcript supports the *concept* ("everything that was being recorded was already going to happen anyway") but the exact phrase appears only in second-hand paraphrase [Ex Nihilo].
5. **"No brand monetization" correction:** the shortlist's "no course/brand monetization" is half-wrong. Sam sells **no course or community** (true), but he **does** take brand sponsorship: Hostile (signed after ~200K YouTube subs) [Ex Nihilo — SECOND-HAND], Raw Nutrition (2026) [Raw Nutrition Facebook — SECOND-HAND], and Gymshark-adjacent events [Modern Wisdom #994: "if this bodybuilding thing and all this Gym Shark stuff, you know, if that doesn't go well"]. This doesn't affect the workflow claims but corrects the framing.
6. **Career-start discrepancy:** Wikipedia says "2023–present" (YouTube); the shortlist says 2022. Reconciled: TikTok ~July 2022 [Ex Nihilo], first YouTube video January 2023 [Sam's own words, Cutler Cast; Wikipedia]. Both are right for their platform.
7. **Recency/staleness:** vidIQ's numbers (2.26M subs, 266 videos) are stale — he is at 4.49M / 346M views [Wikipedia, 2026-07-12] — but vidIQ's qualitative format observations still match 2026 reality. TikTok cadence claims are the only genuinely *changed* mechanic since 2023.
8. **TikTok view counts float:** TikTok view counts fluctuate; the pull above is a snapshot (2026-08-13). The mission's earlier pull (median ~3.35M) matches this one exactly.

---

## New Terms

1. **Companion/ambient retention** — a retention mechanic where the video is designed to be consumed *while doing something else* (cardio, falling asleep): viewers watch the 30-min vlogs "during their cardio" [Cutler Cast]; "4-hour compilations of your car talks to go to sleep to" exist and he acknowledges them [Modern Wisdom #994]. Distinct from attention-grabbing retention: the goal is steady, low-arousal presence in the viewer's routine — "a part of *their* routine" [Ex Nihilo — SECOND-HAND paraphrase].
2. **Deadpan-contrast captioning** — for short clips: pair a serious/hype visual (heavy lift, physique) with an absurd, low-stakes caption ("my mom had to pick me up to go get groceries"), on the logic that "if you're big, you have already said that you are serious… [a motivational line] is putting a hat on a hat" [Modern Wisdom #994]. Same contrast engine drove the "scared of women" bit [Modern Wisdom #994; Cutler Cast].

---

## Sources

**S1 — Modern Wisdom #994: "Sam Sulek: The Endless Pursuit of Progress" (Chris Williamson)**
- URL: https://podcasts.apple.com/us/podcast/994-sam-sulek-the-endless-pursuit-of-progress/id1347973549?i=1000726851509 (video: youtube.com/watch?v=5117cPLuqB0)
- Source date: 2025-09-15 · Length ~2h10m · Type: podcast
- Transcript used: `b0ttsagent/temp/youtube-transcripts/Chris_Williamson_How_to_Get_Better_Every_Single_Day_-_Sam_Sulek_4K.txt` (auto-captioned; wording approximate)
- **FIRST-PARTY** (Sam's own words) · **INDEPENDENT** (nothing sold; no course) · `still-current as of 2026?` = **YES** — most recent (2025) first-party statement of his philosophy; nothing since contradicts it

**S2 — Cutler Cast #147: Sam Sulek (Jay Cutler)**
- URL: https://www.youtube.com/watch?v=1ugnYoB5XGM (audio: https://open.spotify.com/episode/2UE70rP3SZmABg50bG002S)
- Source date: 2024-12-23 · Type: podcast
- Transcript: pulled via yt-dlp auto-subs this session (deduplicated; wording approximate)
- **FIRST-PARTY** · **INDEPENDENT** (Cutler's show; Sam sells nothing on it) · `still-current as of 2026?` = **YES** for YouTube format/cadence/philosophy; **PARTIAL** for TikTok cadence (since changed — see S7)

**S3 — Wikipedia: "Sam Sulek"**
- URL: https://en.wikipedia.org/wiki/Sam_Sulek
- Source date: last updated 2026-07-12 · Type: encyclopedia
- **SECOND-HAND** (compiles NYT, Guardian, Generation Iron, etc.; includes NYT's "defiant commitment to a lo-fi strategy" line) · **INDEPENDENT** · `still-current as of 2026?` = **YES**

**S4 — vidIQ: "Sam Sulek Breaks Every YouTube Rule, Yet Still Goes Viral" (Lydia Sweatt)**
- URL: https://vidiq.com/blog/post/sam-sulek-breaks-youtube-rules-goes-viral/
- Source date: 2023-11-21 · Type: analyst blog (YouTube analytics vendor)
- **SECOND-HAND** · **INDEPENDENT** (nothing monetized for Sam; note: publisher is a for-profit analytics SaaS — content-marketing caveat) · `still-current as of 2026?` = **NO for numbers** (2.26M subs / 266 videos are stale vs 4.49M / 346M today); **YES for qualitative format observations** (daily uploads, minimal edits, thumbnail style), which match S3/S1/S2

**S5 — Ex Nihilo Magazine: "Sam Sulek: Meathead Bodybuilder or Marketing Genius?" (Dean Tran)**
- URL: https://exnihilomagazine.com/sam-sulek-meathead-bodybuilder-or-marketing-genius/
- Source date: 2025-06-12 · Type: long-form article; quotes the Cutler Cast episode
- **SECOND-HAND** (repackages S2, with verbatim first-party quotes — quotes corroborate S2 but the article itself does not count toward verification) · **INDEPENDENT** · `still-current as of 2026?` = **YES** (consistent with both podcasts)

**S6 — FitnessVolt: "Sam Sulek Joins Jay Cutler to Discuss His Fame…" (Doug Murray)**
- URL: https://fitnessvolt.com/sam-sulek-talks-with-jay-cutler-classic-physique-plans/
- Source date: 2024-12-23 · Type: news article; quotes the Cutler Cast episode
- **SECOND-HAND** (contains verbatim first-party quotes — "cardio, calorie tracking, and… consistency"; "$20 mic… that's like 30 percent" — which match S2's transcript verbatim) · **INDEPENDENT** · `still-current as of 2026?` = **YES** for the quoted claims

**S7 — Mission data + yt-dlp pull of TikTok @sam_sulek (this session, 2026-08-13)**
- Source date: 2026-08-13 · Type: platform metadata (view counts, upload timestamps, video titles)
- 20 eligible videos 2023-09-04 → 2026-08-04, all ≥ 365K, median 3.35M, max 10.2M; titles self-document cadence decay ("Yearly post", "Tiktok hiatus has come to an end")
- **FIRST-PARTY-by-artifact** (his own uploads) · **INDEPENDENT** · `still-current as of 2026?` = **YES** (snapshot of live data)
