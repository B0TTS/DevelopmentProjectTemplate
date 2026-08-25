# Philipp Stollenmayer (Kamibox) — Depth Doc

Research date: 2026-08-17 · Wave 07 (Phase 2, depth docs) · Researcher 1

## 1. Eligibility Evidence

- **Scale (route: award, tier T1):** Apple Design Award 2025, Innovation category (Games) — **Winner, PBJ – The Musical**, credited individually to "Philipp Stollenmayer, Germany"; announced June 3, 2025 (WWDC25). Apple Design Award is an allowed top-tier award; individually credited; in-window. Source: https://developer.apple.com/design/awards/2025/ *(Copied from `working/evidence/philipp-stollenmayer-2026-08-17.json`; scale not re-verified per wave spec.)*
- **5-year window:** in-window (2021-08-17 → 2026-08-17).
- **Doc currency (one line):** His own design documentation pages kamibox.de/songofbloom-files and kamibox.de/pbj-files are live as of 2026-08-17; Apple's "How Philipp Stollenmayer is spreading joy with PBJ – The Musical" (Jan 6, 2026) and the SUPERJUMP joint interview (Jul 2025) post-date the in-window award — workflow confirmably current.
- **Product-type tag:** mobile game designer/developer (one-man indie studio Kamibox; interactive narrative/puzzle games for iPhone/iPad).
- **Craft/growth tag:** craft-first — Stollenmayer documents his design process in depth across his own `-files` design docs, Apple's "Behind the Design" feature, and Game Developer deep dives/interviews, so the craft tag applies.

## 2. Step-by-Step Workflow

Stollenmayer's process is deliberately anti-linear — he calls it "a very long jazz improvisation" — but he names concrete steps, one named quality gate (the "housewife test"), and multiple explicit iteration loops across three documented projects. All steps are first-party (his own kamibox.de design docs, Apple's features in his words, and his Game Developer deep dives/interviews). All sources are in English; no German-only material was needed.

### A. The core loop — Song of Bloom (2018–2019)

1. **Start from a real artifact, not a design doc.** The game began when he filmed the sea on a vacation in Italy and tried adding device rotation to the looping video ("when the video flipped, the water would fall out of frame"). From there "it just became a process of triggering new ideas and new experiments." Source: https://developer.apple.com/news/?id=q9fq8jkq ; https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i-
2. **Build the tech as a creative constraint.** "I began with developing a 3D from a 2D engine, and let my faults and triumphs inspire new gameplay mechanics." Source: https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i- ; https://kamibox.de/songofbloom-files
3. **Treat code faults as design material (named method).** "As a designer who isn't the greatest programmer, my code usually creates visual errors... I would let myself be inspired by my own faults." He deliberately re-created faults digitally (e.g., the stray holes of a novice knitter) because "copying the faults creates moments where you ask yourself: Could this be real?" In the iMore interview: "Errors inspire new mechanics because some errors will produce weird esthetics that lead to something new." Source: https://developer.apple.com/news/?id=q9fq8jkq ; https://www.imore.com/how-flipping-bacon-led-apple-design-award-interview-developer-philip-stollenmayer
4. **Iterate story, styles, and references in a loop.** "From there, I constantly modified the story, found new styles, created references, and weaved a game around that." Source: https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i- ; https://kamibox.de/songofbloom-files
5. **Build pieces first, justify the eclecticism later.** "I get bored easily... So, I created pieces of gameplay with a style corresponding to the respective atmosphere, and later in the process tried to find an excuse for that eclecticism" — the story (a hallucinating protagonist) was retrofitted to justify the 18 art styles. Source: https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i-
6. **Iterate the UI/transition until it's invisible.** His earliest transition concept was a blinking-eye effect; he "experimented with several multitouch gestures around that concept, including a pinch gesture, before settling on a button — a single curved line — in the corner," because "I had to get it into the player's mind" without gestures that trigger by chance. Source: https://developer.apple.com/news/?id=q9fq8jkq
7. **Guide with haptics and test with a non-gamer (quality gate).** Because puzzles are abstract, he used haptics to signal mood and evaluate solves ("the player expects a reaction from every action"). He tests with his mother: "I always test with her... If she wants to play it, that's the best feedback I can get." Source: https://developer.apple.com/news/?id=q9fq8jkq ; https://developer.apple.com/articles/pbj-the-musical/

### B. Named quality gate + restart loop — ZIP ZAP (2017)

His Game Developer deep dive gives the most explicit named gate in his corpus:

1. **Start from a genre problem.** "Console games don't work on mobile" — platformers need three buttons (left, right, jump). Source: https://www.gamedeveloper.com/design/game-design-deep-dive-creating-a-one-touch-platformer-in-i-zip-zap-i-
2. **Strip everything away that could lead to a problem.** "I began to strip everything away... and ended up with the barest movement of the muscles — a game controlled by only two choices: contract or release." Source: same.
3. **Prototype the minimal control.** The single-muscle control was technically possible but "the frustration potential was very high... it just wasn't fun anymore." Source: same.
4. **Run the "housewife test" (named quality gate).** "At this point, I usually make what I call the housewife test — I give the phone to my mom. Then I found out that it is not just difficult to control, but impossible to control." Source: same.
5. **Go back to the drawing board (iteration loop).** "Back to the drawing board. I had to change the whole concept" — from platformer to a bite-sized physics puzzle that always fits on the whole screen, with very short levels. Source: same.
6. **Teach without words in three phases.** Level 1 is impossible to fail (learn touch), level 2 requires holding (learn hold), level 3 introduces the restart swipe (and teaches that swiping doesn't move the figure). Source: same.
7. **Expand functionality without changing mechanics.** New elements (two hinges, motorized blocks, a "virtual hip" swing) add timing and momentum layers on top of the same two-choice control. Source: same.

### C. Scaffold → music → physical-first visuals → interaction loop — PBJ – The Musical (2020–2025)

1. **Pick a partner whose humor matches, then pivot on rejection.** He saw Lorraine Bowen on Britain's Got Talent (2015) and wrote to her in March 2020; his first pitch ("Bacon – The Musical") was rejected, so he "dived a bit more into storytelling" and returned with Romeo & Juliet as peanut butter and jelly. Source: https://www.kamibox.de/pbj-files ; https://developer.apple.com/articles/pbj-the-musical/
2. **Structure the whole game first as a storyboard scaffold.** "I then broke everything down into ten acts and sent her the storyboards" — timed storyboards (intro, verse, 20–40s sections) that Bowen called "a scaffold." Source: https://www.kamibox.de/pbj-files ; https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/
3. **Compose music in parallel with "buffers."** Bowen wrote for ~10 months; songs were built as sections with 8/16-bar instrumental "buffers" so music loops seamlessly at any player pace. Source: https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/ ; https://developer.apple.com/articles/pbj-the-musical/
4. **Apply the physical-first rule to visuals.** "Every asset in the game had to be physical before it became digital." He printed hundreds of elements, cut them with children's safety scissors, photographed them on low-contrast mats, cut them out in Photoshop (~500 figures, ~2 months), and ran them through a custom shader adding crumple/gloss/inconsistencies; he forced flimsy newsprint through printers (destroying two) for the peanut world's bleed. Source: https://developer.apple.com/articles/pbj-the-musical/ ; https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/ ; https://www.kamibox.de/pbj-files
5. **Do level design and physics only after the look.** He "spent two years on the game's visuals before solidifying the level design and physics"; characters were differentiated by physics (strawberry "fresh and squishy," peanut "stiff and only bends on one axis"), and gravity became the "secret conductor" that nudges motion. Source: https://developer.apple.com/articles/pbj-the-musical/
6. **Iterate interaction through playtesting (explicit loop).** "Putting so much effort into the look made the interaction difficult... it took a long time to find clear and smooth user interfaces"; "I had to do many tests"; "I had many iterations where I added more and more clues and more help"; and "I lost myself in details now and then, and had to discard everything to start again multiple times." He also threw away a "drag the whole world" idea ("that just resulted in one big mess"). Source: https://www.kamibox.de/pbj-files ; https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/
7. **Ship three escalating help layers instead of difficulty.** (1) a hidden grayscale map that subtly rolls the character toward the goal; (2) a hidden gravity map that tilts the whole scene if the player lingers; (3) a guiding star / guided mode that pulls the character through. Source: https://www.kamibox.de/pbj-files ; https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/

### D. Cross-project constants

- **Boredom as a design driver:** "I'm easily bored... I just don't want the player to be bored when I am." Source: https://developer.apple.com/news/?id=q9fq8jkq
- **Device-first design:** "I design all of my games for the devices they are going to be played on." Source: https://www.imore.com/how-flipping-bacon-led-apple-design-award-interview-developer-philip-stollenmayer
- **Learn to code only as needed:** "I tend to learn to code until exactly at the point that I need it." Source: same.
- **Prototype fast, redo until it feels good:** "I have specific ideas and try to redo them with code and design until it feels good. I start experimenting with controls"; "Pancake — The Game took me 1 day to prototype!" Source: https://medium.com/@anulagarwal12/insights-into-a-successful-solo-game-devs-journey-an-interview-with-bacon-the-game-developer-a05dd41649c7 (verified via search-indexed content; direct fetch returned 403)
- **Test with non-gamers and read reactions as feedback:** "test it and testing is important with people who are not into playing games. Don't blame the player when they react on the wrong controls or gameplay, instead analyze the reaction as feedback." Source: same.

## 3. What Makes It Distinct

- **Faults as a first-class design material.** He explicitly converts his own coding errors into mechanics and aesthetics ("Errors inspire new mechanics"), and re-creates real-world faults digitally to sell the "could this be real?" illusion — the opposite of the polish-first instinct. Source: https://developer.apple.com/news/?id=q9fq8jkq ; https://www.imore.com/how-flipping-bacon-led-apple-design-award-interview-developer-philip-stollenmayer
- **The named "housewife test."** A concrete, named quality gate: hand the phone to his mother; if she can't control it, the design fails and the concept is restarted. Source: https://www.gamedeveloper.com/design/game-design-deep-dive-creating-a-one-touch-platformer-in-i-zip-zap-i-
- **"Jazz improvisation" as a deliberate method.** He frames development as an experimental loop (record real material → let faults/triumphs inspire mechanics → modify story → find styles → weave the game around it) rather than a plan-then-build pipeline. Source: https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i- ; https://kamibox.de/songofbloom-files
- **Physical-first asset pipeline.** A rigid self-imposed rule that every visual must exist physically (printed, cut with children's scissors, photographed, traced in Photoshop) before it becomes digital — including deliberately imperfect edges and newsprint bleed. Source: https://developer.apple.com/articles/pbj-the-musical/ ; https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/
- **Difficulty replaced by invisible help.** Instead of difficulty curves, he layers hidden guidance (nudge map → gravity tilt → guiding star) so the game adapts to the player — "a one hour experience is being tailored specifically for your needs." Source: https://www.kamibox.de/pbj-files
- **Story as a retrofitted excuse.** He builds gameplay pieces first and finds the narrative justification for the eclecticism afterward ("later in the process tried to find an excuse for that eclecticism"). Source: https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i-

## 4. Sources

- Song of Bloom — design/press documentation (his own words, incl. TECHNICAL BACKGROUND): https://kamibox.de/songofbloom-files
- PBJ – The Musical — design/press documentation (his own "Philipp's Comment (Game)"): https://www.kamibox.de/pbj-files
- Behind the Design: Song of Bloom (Apple Developer, Aug 21 2020, his words): https://developer.apple.com/news/?id=q9fq8jkq
- How Philipp Stollenmayer is spreading joy with PBJ – The Musical (Apple Developer, Jan 6 2026, his words): https://developer.apple.com/articles/pbj-the-musical/
- Road to the IGF: Kamibox's Song of Bloom (Game Developer, Feb 3 2020, interview): https://www.gamedeveloper.com/business/road-to-the-igf-kamibox-s-i-song-of-bloom-i-
- Game Design Deep Dive: Creating a one-touch platformer in ZIP ZAP (Game Developer, May 8 2017, his own deep dive): https://www.gamedeveloper.com/design/game-design-deep-dive-creating-a-one-touch-platformer-in-i-zip-zap-i-
- How flipping bacon led to an Apple Design Award (iMore, Jul 21 2020, interview): https://www.imore.com/how-flipping-bacon-led-apple-design-award-interview-developer-philip-stollenmayer
- PBJ: The Musical — How the Developers Cooked Up This Handmade Twist on Romeo and Juliet (SUPERJUMP, Jul 7 2025, joint interview with Philipp + Lorraine Bowen): https://www.superjumpmagazine.com/pbj-the-musical-how-the-developers-cooked-up-this-handmade-twist-on-romeo-and-juliet/
- Insights into a successful solo game-dev's journey (Medium, Mar 27 2024, interview; verified via search-indexed content, direct fetch 403): https://medium.com/@anulagarwal12/insights-into-a-successful-solo-game-devs-journey-an-interview-with-bacon-the-game-developer-a05dd41649c7
- Uses This / Philipp Stollenmayer (Jul 5 2018, tools interview): https://usesthis.com/interviews/philipp.stollenmayer/
- Apple Design Awards 2025 (eligibility anchor): https://developer.apple.com/design/awards/2025/

---

**Anomalies / dead ends:** (1) No GDC or conference talk transcript by Stollenmayer was found; he appears as a listed speaker at Hamburg Games Conference 2020 (https://www.gamesconference.com/team-member/philipp-stollenmeyer/, German bio only, no talk transcript) — not used for workflow claims. (2) The Medium interview page returned HTTP 403 to direct fetch; its quotes are cited from search-engine-indexed content of the page and flagged as such. (3) All workflow sources are in English (his own kamibox.de docs are written in English), so no German-only translation was required. (4) SearXNG returned empty for several queries mid-session; fallback to Exa (`websearch`) was used per routing rules.
