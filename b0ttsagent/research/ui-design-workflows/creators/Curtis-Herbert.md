# Curtis Herbert — Design Workflow Depth Doc

Researcher: wave-08 / Researcher · Research date: 2026-08-17
Verdict: **DEPTH-PASS**

---

## 1. Eligibility Evidence

- **Scale evidence (award route, T1):** Apple Design Award 2022, Interaction category winner — Slopes by Breakpoint Studio (announced 2022-06-01, Apple newsroom). *(Copied from `working/evidence/curtis-herbert-2026-08-17.json`; not re-verified per wave spec.)* Sources: https://www.apple.com/newsroom/2022/06/apple-announces-winners-of-the-2022-apple-design-awards/ ; https://developer.apple.com/design/awards/2022/
- **Route + tier:** award / T1.
- **5-year in-window check:** PASS — award announced 2022-06-01, inside the 2021-08-17 → 2026-08-17 verification window.
- **Doc-currency check (one line):** Slopes Diaries is an active 48-post build-in-public series on blog.curtisherbert.com; latest posts #46 (2025-06-04) and #45 (2025-05-15) — the series is still being published and referenced as current, and Apple's "Behind the Design: Slopes" (2022-08-15) is his own words.
- **Product-type tag:** consumer mobile app (iOS / Android / Apple Watch GPS fitness tracker for skiing & snowboarding).
- **Craft/growth tag:** craft-first, data-gated — the named design steps are craft-driven ("I get you", "better, not just more", MVP lens, stat curation, interaction design), but every design decision is validated through explicit data gates (A/B tests, kill-switch rollouts, SQL analysis of user classes, conversion metrics).

---

## 2. Step-by-Step Workflow

Curtis Herbert never writes a single "my process" essay; instead the 48-post Slopes Diaries series (2015–2025) documents the same named practices recurring across a decade, and Apple's "Behind the Design: Slopes" (2022) states his interaction-design principles in his own words. Synthesized, the ordered workflow is:

**Step 1 — Anchor on a core thesis ("I get you").** Herbert defines Slopes's core as "displaying your ski data in a way that lines up with the way you think. For skiers / snowboarders, by a snowboarder," and says v1 "had to prove — 'I get you.' Oh, and of course 'yeah, this works.'" (https://blog.curtisherbert.com/slopes-diaries-14-the-slopes-mvp/). Apple's profile restates it: "I designed Slopes to be as human as possible because I view it as a journal for your memories." (https://developer.apple.com/news/?id=wq48r7mj)

**Step 2 — Run every feature through the MVP lens (the first explicit gate).** "I view the idea of an MVP as less of a hard rule, and more of a lens to judge features against. 'If I remove this feature, will customers be unable to use the product?'" with the nuance "Can I provide value to them, today? Can I be a compelling solution, today?" He documents the v1 cut list (editing saved activities, full-screen 3D playback, photos/notes, a summary screen, social sharing, hemisphere metrics, offline support, "tons of polish") and calls v1.2 his "true" v1.0. (https://blog.curtisherbert.com/slopes-diaries-14-the-slopes-mvp/)

**Step 3 — Design the free/paid wall from a market division, not a feature list.** The "ah-ha moment" in #4: split the market into amateurs vs enthusiasts — "If an enthusiast would really want/need the feature, but an amateur probably wouldn't, it was a paid feature." He pairs this with a "show, don't tell" demo gate: the run/lift breakdown and 3D replay are free for the first recording of every season, then gated behind the Season Pass. (https://blog.curtisherbert.com/slopes-diaries-4-the-great-wall/)

**Step 4 — Plan on the seasonal calendar (April → June → September → November).** Named in #30: ~April step back and pick major features (quality-of-life wins in summer; big efforts like the 3D-engine rewrite prioritized for summer); ~June take stock of WWDC and keep 75% of time free to pivot; ~September crunch mode with "aggressive cuts" — "I often take a good hard look at any big feature I'm working on and asking what the MVP of that feature-arc is"; ~November 10 season launch, then "Just Keep Shipping" mode. (https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)

**Step 5 — Ship "features, not versions."** Named in #21: "The SaaS industry rarely ships versions... Bugfixes just go out as fast as possible and major features go out when they are ready." He ships 2–4 major features per season plus dedicated "bug weeks." (https://blog.curtisherbert.com/slopes-diaries-21-versionless/ ; https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)

**Step 6 — Gate features with "better, not just more" and future-self.** "I tend to... focus on making the experience of using Slopes better... Better, not just more." Plus the future-self constraint: "I can't add a feature if it means next season I'll need to spend 30hrs a week supporting it." And the 80% polish balance: "I need to polish Slopes, but not spend too much time past the 80% level of polish." (https://blog.curtisherbert.com/slopes-diaries-31-saying-yes/ ; https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)

**Step 7 — The gut-check gate.** #16 documents a full month lost to localization, then: "I can't fight my gut... I think I panicked, trying to be the savvy business dude, and took on something that wasn't a good fit." He shelves the branch and pivots to user-requested features. (https://blog.curtisherbert.com/slopes-diaries-16-recovering-from-a-stall/)

**Step 8 — Iterate with data: A/B tests, kill switches, and SQL.** #42 documents the "Trial Quickstart" A/B test (25% improvement in trial starts, converting at the same rate), a kill-switch rollout for the recording-screen popup, and YoY trial-start growth as the measurement when no A/B ran — explicitly balancing trial starts vs conversion. #25 shows SQL analysis of three user classes (free / Day+Trip / Season) driving the Trip Pass → 5-Day Bundle redesign. #36 shows SQL revealing ~20% of premium customers used the Day Pass as a trial, driving the free-trial decision. (https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/ ; https://blog.curtisherbert.com/slopes-diaries-25-a-new-lineup/ ; https://blog.curtisherbert.com/slopes-diaries-36-try-me/)

**Step 9 — Re-frame the ask around the user's own content.** #17: a customer conversation revealed a missed upsell; he reworked the banner to advertise the backdate option ("buy now" vs "don't forget"). #34: "Framing the upsell in terms of their own content... 'which run did I hit my top speed on, and where on the mountain was that?' has been much more effective," plus the "one call to action per screen" rule. (https://blog.curtisherbert.com/slopes-diaries-17-missed-conversions/ ; https://blog.curtisherbert.com/slopes-diaries-34-passive-vs-active/)

**Step 10 — Re-check against the asymptote / ideal-product lens.** #41: "You don't want to chase growth, you want to chase your ideal product." He reframes a stalled social feature by asking "what is holding me back, how am I shooting myself in the foot?" and chooses the recording-screen redesign (Find My Friends) over feature-stuffing. (https://blog.curtisherbert.com/slopes-diaries-41-asymptotes/)

**Cross-cutting interaction principle (Apple, his words).** "A lot of interaction design is thinking holistically about the ski experience... Does the thing on screen react the way I'd expect it to? Can I physically interact with this digital concept? Does it feel real?" And stat curation: "It's really easy to overwhelm with stats... You really have to pick what matters to tell the story." (https://developer.apple.com/news/?id=wq48r7mj)

---

## 3. What Makes It Distinct

- **The "I get you" thesis as a design anchor, not a feature list.** The core of Slopes is defined as "displaying your ski data in a way that lines up with the way you think. For skiers / snowboarders, by a snowboarder" — the product is designed around the user's mental model of their day, and every feature is judged against it. (https://blog.curtisherbert.com/slopes-diaries-14-the-slopes-mvp/)
- **The amateur-vs-enthusiast market division as the free/paid wall principle.** Instead of a generic "premium features" list, the paywall is derived from a market split: "If an enthusiast would really want/need the feature, but an amateur probably wouldn't, it was a paid feature." (https://blog.curtisherbert.com/slopes-diaries-4-the-great-wall/)
- **The ski season IS the design calendar.** The April→June→September→November planning cycle, the Nov 10 "season start" launch date, and "Just Keep Shipping" mode make the sport's seasonality a first-class design constraint — a rhythm few app designers have. (https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)
- **The "show, don't tell" demo gate.** The most compelling premium feature (run/lift breakdown + 3D replay) is given away free for the first recording of every season — a built-in trial that doubles as word-of-mouth. (https://blog.curtisherbert.com/slopes-diaries-4-the-great-wall/)
- **The gut-check as an explicit quality gate.** "I can't fight my gut" — he publicly documents shelving a month of localization work because the decision didn't pass his internal test. (https://blog.curtisherbert.com/slopes-diaries-16-recovering-from-a-stall/)
- **The future-self constraint.** Features are gated by their future maintenance burden: "I can't add a feature if it means next season I'll need to spend 30hrs a week supporting it." (https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)
- **The 80% polish balance.** "I need to polish Slopes, but not spend too much time past the 80% level of polish" — an explicit anti-perfectionism gate. (https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)
- **The "one call to action per screen" upsell rule.** A concrete design rule for monetization UI: focus each screen on the single most important unlock. (https://blog.curtisherbert.com/slopes-diaries-34-passive-vs-active/)
- **The asymptote / ideal-product framing.** "You don't want to chase growth, you want to chase your ideal product" — growth is treated as a byproduct of product quality, not a target. (https://blog.curtisherbert.com/slopes-diaries-41-asymptotes/)
- **"Features, not versions."** Continuous improvement borrowed from SaaS, shipped feature-at-a-time rather than bundled major versions. (https://blog.curtisherbert.com/slopes-diaries-21-versionless/)
- **The one-person multi-hat "cheat."** "I get to cheat a little because I'm the snowboarder, designer, developer, and product manager" — the user, designer, and engineer are the same person, which he treats as a deliberate advantage. (https://developer.apple.com/news/?id=wq48r7mj)
- **Stats as storytelling, not data.** "I view it as a journal for your memories... you become the hero of your own story" — stat curation ("pick what matters to tell the story") is a named design act. (https://developer.apple.com/news/?id=wq48r7mj)
- **Physical-context-driven interaction design.** "A lot of interaction design is thinking holistically about the ski experience" — gloves, sub-zero temperatures, lifts 100 feet up, and the Watch-vs-phone split are treated as design inputs, not constraints to work around. (https://developer.apple.com/news/?id=wq48r7mj)

---

## 4. Sources

Canonical first-party links (all read for this doc unless noted):

- Slopes Diaries series index (48 posts): https://blog.curtisherbert.com/tag/slopes-diaries/
- #2 Retrospective (2015-10-13): https://blog.curtisherbert.com/slopes-diaries-2-retrospective/
- #3 Removing Barriers (2015-10-26): https://blog.curtisherbert.com/slopes-diaries-3-removing-barriers/
- #4 The Great Wall (2015-11-02): https://blog.curtisherbert.com/slopes-diaries-4-the-great-wall/
- Slopes 2 relaunch post (2015-11-09): https://blog.curtisherbert.com/slopes-2/
- #9 For the Good of the Business (2015-12-10): https://blog.curtisherbert.com/slopes-diaries-9-for-the-good-of-the-business/
- #10 Understanding Value (2016-01-21): https://blog.curtisherbert.com/slopes-diaries-10-understanding-value/
- #12 Progress Check (2016-03-10): https://blog.curtisherbert.com/slopes-diaries-12-progress-check/
- #13 Slopes SE (2016-06-23): https://blog.curtisherbert.com/slopes-diaries-13-slopes-se/
- #14 The Slopes MVP (2016-07-14): https://blog.curtisherbert.com/slopes-diaries-14-the-slopes-mvp/
- #15 Indecision (2016-10-03): https://blog.curtisherbert.com/slopes-diaries-15-indecision/
- #16 Recovering from a Stall (2016-12-29): https://blog.curtisherbert.com/slopes-diaries-16-recovering-from-a-stall/
- #17 Missed Conversions (2017-01-09): https://blog.curtisherbert.com/slopes-diaries-17-missed-conversions/
- #21 Versionless (2017-10-26): https://blog.curtisherbert.com/slopes-diaries-21-versionless/
- #23 Featuring Numbers (2018-01-22): https://blog.curtisherbert.com/slopes-diaries-23-featuring-numbers/
- #24 Second Guessing My Way To Success (2018-03-15): https://blog.curtisherbert.com/slopes-diaries-24-second-guessing-my-way-to-success/
- #25 A New Lineup (2018-11-02): https://blog.curtisherbert.com/slopes-diaries-25-a-new-lineup/
- #28 Constraints (2019-02-14; slug collision — lives at the tag-page URL): https://blog.curtisherbert.com/slopes-diaries/
- #29 A Disappearing Trick (2019-03-07): https://blog.curtisherbert.com/slopes-diaries-29-a-disappearing-trick/
- #30 Planning Ahead (2019-04-08): https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/
- #31 Saying Yes (2019-08-19): https://blog.curtisherbert.com/slopes-diaries-31-saying-yes/
- #33 Hi There (2019-11-25): https://blog.curtisherbert.com/slopes-diaries-33-hi-there/
- #34 Passive vs Active (2020-03-23): https://blog.curtisherbert.com/slopes-diaries-34-passive-vs-active/
- #35 Abandonment Issues (2020-03-30): https://blog.curtisherbert.com/slopes-diaries-35-abandonment-issues/
- #36 Try Me (2020-09-09): https://blog.curtisherbert.com/slopes-diaries-36-try-me/
- #37 A Commitment to Y-Axis Values (2020-11-23): https://blog.curtisherbert.com/slopes-diaries-37-a-commitment-to-y-axis-values/
- #40 The Droid (Stats) You're Looking For (2021-06-06): https://blog.curtisherbert.com/slopes-diaries-40-the-droid-stats-youre-looking-for/
- #41 Asymptotes (2021-12-20): https://blog.curtisherbert.com/slopes-diaries-41-asymptotes/
- #42 Building Ramps, not Walls (2022-04-12): https://blog.curtisherbert.com/slopes-diaries-42-building-ramps-not-walls/
- #43 Chasing a Goldilocks Business (2022-06-01): https://blog.curtisherbert.com/slopes-diaries-43-chasing-a-goldilocks-business/
- #44 A Decade (2023-09-24): https://blog.curtisherbert.com/slopes-diaries-44-a-decade/
- #45 Building Trust (2025-05-15): https://blog.curtisherbert.com/slopes-diaries-45-building-trust/
- #46 An Intentional Dozen (2025-06-04): https://blog.curtisherbert.com/slopes-diaries-46-an-intentional-dozen/
- Apple — Behind the Design: Slopes (2022-08-15, his words): https://developer.apple.com/news/?id=wq48r7mj
- Apple Design Awards 2022 winners page: https://developer.apple.com/design/awards/2022/
- Apple newsroom — 2022 Apple Design Awards winners (2022-06-01): https://www.apple.com/newsroom/2022/06/apple-announces-winners-of-the-2022-apple-design-awards/

**Anomalies / dead ends:** SearXNG returned empty for the Apple "Behind the Design" query (fell back to Exa per skill routing; page then read directly). Post #28 "Constraints" has a slug collision — the tag index links it to /slopes-diaries/ and the content there is indeed #28 (verified by reading). The diaries are heavily business/growth-oriented; the design workflow is reconstructed from recurring named practices across the series rather than one canonical essay, with each step source-linked to the specific post that names it.
