# SYNTHESIS — ui-design-workflows research run

- Research date: 2026-08-17 · verification window: 2021-08-17 → 2026-08-17
- Scope: 11 verified craft-first designers with DEPTH-PASS workflow docs (Phase 2 output). Companion file: `INDEX.md` (rankings + rejects).

---

## 1. Headline answer

Across 11 independently verified, craft-first UI designers — from framework authors (Tailwind, Bootstrap, D3, Prism, styled-components) to Apple Design Award–winning solo game designers (Kamibox, Slopes, Blackbox) to a $41M-ARR SaaS brand studio lead (Kit) — the near-universal workflow is the same seven-beat loop, regardless of tool, domain, or era:

> **1. Ideate divergently from real material** — catalog real pages/products/data/users before designing anything. **2. Start with a feature, not the shell** — one piece of real functionality, not the layout. **3. Hold the detail early** — grayscale, grey-box, or ugly prototypes so structure does the work. **4. Build the real thing early** — in the browser/code as soon as possible; the design file is disposable. **5. Pass it through a named quality gate** — every one of the 11 has at least one named, falsifiable test (not vibes): a "housewife test", a dogfooding "binge-close" test, a hypothesis-per-prototype rule, a "no slop" bar, a "sleep on it" rule, "make it work, right, fast". **6. Iterate in a named loop** — cycles until no problems remain, then deliberately re-scan for gaps and repeat; iteration is a first-class stage, never a failure. **7. Converge and systematize** — constraint discipline + taste/personality decided once (systems: shades, type scale, spacing), extract survivors into reusable components, and — where a live product exists — measure post-launch.

The single deepest consensus: **divergent exploration gated by named, falsifiable quality tests, iterated in named loops on the real artifact.** The single biggest divergence: **where the real artifact lives** — code/browser-first (9 of 11) vs design-tool-first with a handoff (Schoger's Sketch series, Prangley's Figma pipeline) — and a secondary philosophical split between **ideal-first** (Verou's North Star) and **simple-first** (Wathan/Schoger/Stoiber/Palmer/Herbert's MVP-first loops). Notably, the three strongest-verified workflows (Wathan, Otto, Bostock) use *behavioral* gates (self-review, dogfooding, context-deprived friends) rather than formal usability testing; formal user/data testing appears in the mid-table (Verou, Herbert, Prangley, McLeod, Stollenmayer).

---

## 2. Method

This synthesis is the Phase 3 output of a 3-phase gate pipeline (see `working/MANIFEST.md` for wave-by-wave status):

- **Phase 0 (Discovery, wave 01):** 45 raw → **44 unique candidates** (lanes A17/B13/C14), 22 weak-flagged.
- **Phase 1 (Verification, waves 02–06):** → **12 verified PASS** (11 T1: usage-stat or top-tier award; 1 T2: revenue), **6 REJECT**, **1 FAIL-UNKNOWN** (Sorhus). Scale routes: official npm/GitHub API figures, Apple Design Award winner lists, Kit newsroom revenue.
- **Phase 2 (Depth docs, waves 07–09):** → **11 DEPTH-PASS / 1 DEPTH-REJECT** (shadcn: principles-only). Each PASS doc carries named stages + explicit quality gates/iteration loops with per-step first-party source links.
- **Phase 3 (this file):** cross-designer element extraction, matrix, and parallel analysis. No new facts invented; everything traces to `creators/*.md` and `working/evidence/*.json`.

### QA flags carried into this synthesis

- **Prangley — weak verification route.** T2 revenue ($41M ARR) rests on Kit's own newsroom + estimate-tracker (Sacra) corroboration only; no independent T1 press figure. Her *process* content is first-party and strong; the *route* is the weak point.
- **Verou / Stoiber — designer-credential judgment calls.** Verou's designer credit = graphic-design background + W3C TAG/CSS WG roles rather than a product-designer title; Stoiber = styled-components co-creator (with Glen Maddern), Moxy Studio claim unverified. Frame credits precisely (done in §3).
- **Palmer — thin first-party base.** Designer-era loop rests on Madrona/Latent Space interviews + the v0 launch post; several supporting posts are Vercel-official, not bylined to Palmer. Single-anchor claims flagged in §3.
- **Stoiber — single-anchor depth.** Shortest PASS doc; core workflow rests largely on one note (mxstbr.com/notes/taste). Flagged where cited.
- **Doc-currency warnings.** Mark Otto: blog stale since Jun 2024 (workflow itself re-verified Jan 2024 via "Shipping Blended Diffs"); Adam Wathan: 2021 ecommerce post is the flagship anchor (Tailwind UI rebranded Tailwind Plus in 2025; blog active May 2026); Ryan McLeod: Medium recency UNKNOWN (bot-blocked, read via web.archive.org snapshots).
- **Source-style normalization.** Bare URLs and "Source: same." cross-references in creator docs were normalized to markdown links here; no content changed. All files read as UTF-8 (em-dash mojibake is a non-UTF-8 reader artifact only; files are byte-clean).

### Element set (the auditable extraction grid)

Twelve cross-cutting workflow elements were extracted from the 11 depth docs. They form the matrix columns in §4 and the per-element writeups. A ● = core, named practice; ◐ = partial/secondary or inferred; — = absent/not documented in that creator's first-party corpus.

1. **Real-material research** — study existing pages/products/data/users before designing.
2. **Feature-first** — start from one piece of functionality, not the layout/shell.
3. **Low-fi early** — grayscale / grey-box / sketch-first; hold the detail.
4. **Constraints as engine** — a named constraint drives the design.
5. **Build the real thing early** — design/build in code or ship prototypes quickly.
6. **Divergent ideation** — generate many candidate options before converging.
7. **Named quality gate** — at least one named, falsifiable quality test.
8. **External validation** — real users/observers/testers, not just self-review.
9. **Named iteration loop** — an explicit, named loop (not "iterate" in the abstract).
10. **Extract & systematize** — abstraction, documentation, reusable systems as a stage.
11. **Taste/personality systems** — deliberate, one-time personality/system choices.
12. **Post-launch measurement** — analytics/data-driven iteration on the live thing.

---

## 3. Per-framework depth sections

### 3.1 Adam Wathan — dev tools (Tailwind CSS, Tailwind UI) · craft-first

**Named stages** (three complementary workflows, all first-party):

- **A. Component-kit workflow** ("Designing Tailwind UI Ecommerce", 2021): (1) *Research & catalog* — study dozens of real stores (Everlane, Allbirds, Grovemade…) and catalog every UI pattern, deliberately avoiding focus on one store type so only universal patterns emerge; (2) *Design full pages* (~50 complete pages from the start — components designed in isolation "feel off" when assembled); (3) *Build the pages + browser-review gate* — build, then review together **in the browser** and adjust (spacing is judgeable only in the browser; be ready to replace whole parts); (4) *Extract bigger components* — outside-in: pull components *out of* pages, erring toward "pre-built LEGO creations, not just the bricks"; (5) *Take inventory & repeat the whole thing* — the named iteration loop.
- **B. Feature-level process** (Refactoring UI, with Schoger): start with a **feature, not a layout** → detail comes later (thick-Sharpie sketches, grayscale, hold the color) → don't over-invest → **work in cycles** (design simple → make it real → iterate until no problems → next feature) → be a pessimist (smallest useful version) → choose a personality → limit your choices (8–10 shades, restrictive type scale).
- **C. Micro decision loop** (KiteTail build log, 2017): list the problems with the current design → generate candidate solutions → weigh each against the problems → iterate to breakthrough → time-box ("2.5 hours of screensharing and brainstorming").

**Gates/loops:** browser-review gate (A.3); "work in cycles" + "no amount of planning will lead to the right product on the first try — you have to keep iterating" (A.5, B.4); candidate-rejection loop (C).

**Signature idea:** **Outside-in component extraction** — design full pages first, extract components second ("LEGO creations, not bricks"), and the repeat-the-whole-thing law that treats gap-finding after a full cycle as a normal step, not a failure. Framed as "design with tactics, not talent."

### 3.2 Mark Otto — dev tools (Bootstrap, GitHub design, Pierre) · craft-first

**Named stages** (stated verbatim, A List Apart 2012): **"ideation, debate and feature review, implementation, and lastly abstraction and documentation"** — the same four stages applied to every feature, and the same process re-run in 2024 for Pierre.

- **1. Ideation** — work with PMs and actual users to identify real needs ("too many links in the topbar" → dropdowns).
- **2. Debate and feature review** *(gate)* — design in the browser, then "debated each component and weighed other options and implementations carefully before moving on" (multi-level dropdowns cut: "extra code that complicated our implementation").
- **3. Implementation** *(loop)* — "quickly implemented, tested, and iterated each new feature" in isolated components before they touch the shared library.
- **4. Abstraction and documentation** — promote the components into a shared, self-documenting codebase: "a toolkit built in style guide form"; "Treat the docs like they're the product."

**Cross-cutting gates:** feature admission ("only implement a new feature if it doesn't confuse users or unnecessarily inflate the framework"); the **dogfooding gate** — he caught GitHub Issues failing by noticing he was secretly reverting to the old interface to close Bootstrap issues: "I'd know we were on to something awesome if I could binge close dozens of issues without using the old interface"; the **prototype ≠ production honesty gate** (split diffs: "ultimately, none of it could ship" + concrete reasons); test-pass-then-merge; dark-shipping + feature flags + metrics before merge. 2024 re-run adds a **writing/PRD gate** ("Writing about a feature is arguably more powerful… than just designing it") and **design↔code ping-pong** ("no better way to fine-tune the details").

**Signature idea:** **Abstraction-and-documentation as a first-class final stage**, plus the designer-engineer pairing ("constant contact") as the core working unit across 13 years, and "say no all the time" as a design principle.

### 3.3 Mike Bostock — dev tools (D3.js, Observable) · craft-first

**Named workflow:** **"Design is a Search Problem"** (OpenVis 2014) — principles are necessary but not sufficient (they guide, never dictate); the process must explore the design space efficiently:

1. **Frame as search, not recipe** — budget time for exploring things that won't work.
2. **Explore widely & divergently at the start** — early commits were "wild explorations that looked nothing like the final graphic" (scatterplots, cartograms, box plots before stabilizing).
3. **Prototype to test one hypothesis at a time** *(gate)* — "your prototype only exists so that you can learn something… you have a hypothesis that you are testing."
4. **Evaluate with context-deprived people** *(gate)* — show work to people outside the department (his wife, friends): does it "communicate the way I expect it to"?
5. **Make exploration cheap & visible** — git branches as "a safe place to work on things that are potentially bad ideas", a commit-screenshotting preview server.
6. **Anneal** *(convergence gate)* — simulated annealing: explore hot early, cool toward commitment as the deadline approaches; "the art of design here is figuring out at what point you are in your process."
7. **Prune constantly & systematize survivors** — delete code as you go; "Makefiles are machine-readable documentation that make your workflow reproducible."
8. **Try bad ideas on real data** — "You can't really evaluate an idea without applying it to real data."

**Supporting loops:** the black→gray→white-box ladder (how much internal state a visualization exposes); the self-correction loop (published his own Prim's color-flood bug and the redesign); example-driven refinement ("don't generalize prematurely").

**Signature idea:** **The prototype-hypothesis gate + the annealing temperature schedule** — a named, time-aware rule for when to explore vs commit, plus infrastructure (branches, preview servers, Makefiles) treated as first-class design tools.

### 3.4 Lea Verou — dev tools (Prism.js, Color.js, Mavo) · craft-first

*(Designer credential: graphic-design background + W3C TAG / CSS WG roles — judgment call; process content is unambiguous and first-party.)*

**Named workflow:** **The Hovercar Framework** (2025) — break the problem into **North Star → Constraints → Compromises**:

1. **Articulate the North Star** — the ideal, *unconstrained* solution ("a guiding light"). Fundamental requirements (part of the problem) can't be ignored; only ephemeral constraints (resources, time, tech limits, backwards compat) may be.
2. **Identify the constraints** — ephemeral vs fundamental taxonomy ("the product version of tech debt": when a constraint lifts, only compromises need re-evaluation).
3. **Consensus on the North Star** *(gate 1)* — "when we… reach consensus on the North Star before moving on to the compromises, we know what is an actual design decision and what is a compromise"; effort arguments are proxy wars for vision arguments.
4. **User-test the North Star** *(gate 2)* — on a low-fi paper prototype, *before* committing to compromises: "there is no point in evaluating compromises if… even the 'perfect' solution was not actually all that great."
5. **Design compromises on the shipping spectrum** — Skateboard (pessimist MVP) → Scooter (target) → Bicycle (stretch) → Motorcycle → Car → Hovercar.
6. **Ship, then iterate toward the North Star** *(loop)* — "when constraints get lifted all we need to reevaluate is our compromises."
7. **Evaluate proposals against the North Star** *(evolution gate)* — is this "a milestone along a path that ends at the North Star" or does it "actively prevent us from ever getting there"? (CSS Nesting "Option 3" case study.)

**In action (Context Chips, 2024):** problem framing → five competing ideas → self-built working prototype → within-subjects usability study (6 participants; stopped at 5, results lopsided) → iterate (missed mobile — caught post-launch) → post-launch validation (24–59% response rates, avg 38%). Named lessons: "Never skimp on articulating the north star UI"; "User testing is also a consensus-building tool"; "Heuristic evaluations are not a substitute for usability testing."

**Signature idea:** **North Star first, MVP second — the anti-MVP move** ("without it, there is no skateboard — you can't reduce the unknown"), plus the **complexity-to-effort curve** for API/UI design (usability cliffs = small complexity increases that cost disproportionately large effort).

### 3.5 Steve Schoger — dev tools / design resources (Heroicons, Tailwind UI, Refactoring UI) · craft-first

**Named workflow:** the **Refactoring UI book's chapter sequence IS the process** (co-authored with Adam Wathan; both credited):

1. **Starting from Scratch** — feature not layout; detail later (grayscale); work in short cycles; choose a personality; limit your choices.
2. **Hierarchy is Everything** — size isn't everything; don't use grey text on colored backgrounds; de-emphasize to emphasize; labels are a last resort.
3. **Layout and Spacing** — start with too much white space; establish a spacing/sizing system.
4. **Designing Text** — type scale; line-height is proportional; letter-spacing.
5. **Working with Color** — ditch hex for HSL; define shades up front; "saturate your greys".
6. **Creating Depth** — emulate a light source; shadows with two parts; overlap to layer.
7. **Working with Images** — good photos; consistent contrast.
8. **Finishing Touches** *(gate)* — **"supercharge the defaults"** (borders, shadows, spacing) — the named closing pass of every cycle.
9. **Leveling Up** — treat the sequence as a repeatable skill.

**Applied loop:** the YouTube series refactors real, submitted app pages in Sketch with named before→after step sequences (e.g., WSS: Scroll Jacking → Background Photos → The Hierarchy → Icons → Nav → Plan Details → Font → …; Tuple: Headline placement → Inverted text → Font Stack → …). The before/after scannability improvement is the implicit gate; the series is an open loop (channel reboot 2025, collecting examples to redesign).

**Signature idea:** **Redesign-as-teaching with before/after gates** — refactoring real pages rather than blank-canvas designing, plus micro-tactic density (one tactic + one before/after mockup per X post) and the "supercharge the defaults" finishing gate. Sketch-first (design-tool), unlike the code-first majority.

### 3.6 Philipp Stollenmayer — mobile games (Kamibox: Song of Bloom, ZIP ZAP, PBJ) · craft-first

**Named workflow:** **"a very long jazz improvisation"** — deliberately anti-linear, but with named steps and one famous gate:

- **A. Song of Bloom (2018–19):** (1) start from a **real artifact** (a filmed sea on vacation), not a design doc; (2) build the tech as a creative constraint ("began with developing a 3D from a 2D engine"); (3) treat **code faults as design material** — "I would let myself be inspired by my own faults" (novice-knitter holes re-created digitally to sell "could this be real?"); (4) iterate story/styles/references in a loop; (5) build pieces first, justify the eclecticism later (the hallucinating-protagonist story retrofitted over 18 art styles); (6) iterate UI/transition until invisible (blinking-eye → pinch → a single curved line); (7) guide with haptics and test with a non-gamer.
- **B. ZIP ZAP (2017):** (1) start from a genre problem ("console games don't work on mobile"); (2) strip everything away ("the barest movement of the muscles — contract or release"); (3) prototype the minimal control; (4) run the named **housewife test** — "I give the phone to my mom… it is not just difficult to control, but impossible to control"; (5) **back to the drawing board** *(loop)* — whole concept changed to bite-sized physics puzzles; (6) teach without words in three phases; (7) expand functionality without changing mechanics.
- **C. PBJ – The Musical (2020–25):** partner pitch → pivot on rejection (Bacon→PBJ Romeo & Juliet) → **storyboard scaffold** first (ten acts) → music composed in parallel with 8/16-bar "buffers" → **physical-first rule** ("Every asset had to be physical before it became digital": printed, cut with children's scissors, photographed, ~500 figures, custom shader) → level design & physics only *after* the look (two years) → iterate interaction via playtesting ("had to discard everything to start again multiple times") → ship three escalating **hidden help layers** (nudge map → gravity tilt → guiding star) instead of difficulty.

**Signature idea:** **Faults as first-class design material + the housewife test** — converting his own coding errors into mechanics/aesthetics, and the named gate of handing the phone to a non-gamer parent. Also the physical-first asset pipeline and hidden-help-instead-of-difficulty.

### 3.7 Curtis Herbert — consumer app (Slopes, skiing/boarding tracker) · craft-first, data-gated

**Named workflow:** no single essay — the 48-post Slopes Diaries (2015–2025) documents the same named practices across a decade; synthesized 10-step order, each step source-linked:

1. **Anchor on "I get you"** — the core thesis: "displaying your ski data in a way that lines up with the way you think. For skiers / snowboarders, by a snowboarder."
2. **MVP as a lens** *(gate)* — "If I remove this feature, will customers be unable to use the product?" — with the nuance "Can I provide value to them, today?"
3. **Derive the paywall from a market division** — amateur vs enthusiast: "If an enthusiast would really want/need the feature, but an amateur probably wouldn't, it was a paid feature"; "show, don't tell" demo gate (best feature free for the first recording each season).
4. **Plan on the seasonal calendar** — April pick features → June WWDC stock-take (75% time kept free to pivot) → September crunch + aggressive cuts → November 10 launch → "Just Keep Shipping".
5. **Ship features, not versions** — 2–4 major features per season, dedicated bug weeks.
6. **Gate with "better, not just more" + future-self** — "I can't add a feature if it means next season I'll need to spend 30hrs a week supporting it"; the **80% polish** balance.
7. **The gut-check gate** — "I can't fight my gut" (shelved a month of localization work).
8. **Iterate with data** — A/B tests (Trial Quickstart: 25% more trial starts), kill-switch rollouts, SQL analysis of user classes (SQL revealed ~20% of premium customers used the Day Pass as a trial → free-trial decision).
9. **Reframe asks around the user's own content** — one call-to-action per screen.
10. **Re-check against the asymptote** — "You don't want to chase growth, you want to chase your ideal product."

**Signature idea:** **The one-person multi-hat advantage with a seasonal design calendar** — the ski season IS the planning cadence, and the solo user-designer-engineer-PM "cheat" is treated as a deliberate advantage. Stat curation as storytelling: "You really have to pick what matters to tell the story."

### 3.8 Ryan McLeod — mobile games (Blackbox, Blackbox for Vision) · craft-first

**Named workflow:** the challenge-design loop for Blackbox's 81 "lights" (puzzles solved *without* touching the screen), plus a documented visionOS port variant:

- **Core loop:** (1) **idea capture with the "observable change" test** *(gate)* — "a Challenge really only requires something that someone can change and that you can observe the change of" (ideas arrive while running/biking; 50–70-item backlog); (2) design the interface as a **"castle with a moat"** — an intuitive interface to something novel that nudges, "but you don't want it so easy that you look at it and you understand how it works immediately"; (3) **design satisfying visuals/audio, then dial them back** — the obvious satisfying answer "would just be an interface and not a puzzle"; (4) playtest by handing the phone over; (5) the **"months" iteration loop** — removing red herrings and tuning difficulty from playtester feedback; (6) beta-testing gate; (7) **"perfection is the enemy of good"** shipping gate (launched when savings ran out); (8) post-launch analytics loop (Telemetry Deck onboarding funnel — "how many people are not making it through the first puzzle").
- **Vision port (2023–24):** sketch in a notebook → find a medium-native metaphor (soap bubbles) → **redesign for the new context, don't port** → iterate by "following of my own rules — and breaking some of them" ("building this plane as he's flying it — something he views as a positive").

**Signature idea:** **The anti-touch constraint as the genre** — every solution must not involve touching the screen (sensors, celestial events, singing, a USB cable), plus the "observable change" falsifiability test and the "castle with a moat" difficulty dial. Accessibility as a design driver (fully sonified for blind players).

### 3.9 Max Stoiber — dev tools (styled-components; co-creator with Glen Maddern) · craft-first

*(Co-creator credit nuance + designer-credential judgment call; the taste note is the single strongest anchor.)*

**Named workflow:** **"How to have great taste"** (2024):

1. **Get more parts on the table** — exposure: "By seeing more examples, you have more data to be able to assess what works and what doesn't" (adjacent possible).
2. **Dissect the greats** — break world-class work into components and form an opinion about their combination, like a wine connoisseur.
3. **Iterate, iterate, iterate** *(core loop)* — "The only way I know of to make something great is to iterate": build & ship first version → dissect what works/doesn't → ship an iteration to test the dissection → repeat.
4. **"Make it work, make it right, make it fast — in that order!"** *(ordering gate)* — optimize before correctness forces rework.
5. **Apply the taste** (Ira Glass's "The Gap").

**Worked proof (same note):** the styled-components API as **five prior-knowledge pieces → three breakthroughs** (component-level styling from ElementalUI pain; CSS-in-JS from Glen's CSS Modules; tagged template literals from Glen's overnight prototype; React Context for `ThemeProvider`) — plus a documented **option-evaluation gate**: three candidate theme-injection APIs weighed against explicit criteria (ES5 compatibility, cognitive overhead, React conventions) — "the decision we spent the most time on, and that took the most taste." Then launch → community-feedback iteration (shorthands, natural-language naming) → performance phase (v5 "Beast Mode").

**Supporting notes:** decision-making loop (criteria first → write it down → share with one person → hindsight reflect); brainstorming rounds (2-min silent writing, "quantity over quality"); ship-faster techniques (outline speedrunning, tracer bullets).

**Signature idea:** **Taste as a learnable pipeline with a hard sequencing law** — "make it work → right → fast" — proven by the five-pieces-to-three-breakthroughs API case study. *Single-anchor flag: core workflow rests largely on this one note.*

### 3.10 Jared Palmer — dev tools (Formik, Turborepo, v0) · growth + craft

*(Weakest designer credentials of the set: designer-era process is self-disclosed; several supporting posts are Vercel-official, not bylined. Flags carried.)*

**Named workflows (two):**

- **A. Generative UI loop** (v0, 2023, bylined): **describe the interface → generate (React/Tailwind/shadcn) → select an iteration and keep editing → copy-paste into your app and develop from there.** Reinforced by Vercel-official guidance: iterate component-by-component, "build the pieces of your design first… then tell v0 how to arrange them."
- **B. Designer-era prototyping loop** (The Palmer Group, ~2013–16): design in Photoshop → import layers into Framer and animate with "a little bit of code" → reach super-high fidelity → **hand it to a client to play with before it was built** — the prototype is the reviewable artifact preceding any build. He explicitly frames v0 as "the AI version of it."

**v0 product process:** set the **"no slop" quality gate** up front ("no random acts of AI… it had to be pretty good") → generate options (DevGPT vs Webjourney) → prototype to find key unlocks (models are "really good at HTML and… Tailwind CSS") → **constrain scope deliberately** (ship SIUI markup-only; single framework — "That constraint was rather liberating") → launch, then iterate the modality (Midjourney-style → chat rebase in ~one month; "we are always building a model generation ahead").

**Principles:** solve your own problem (Formik from forms pain); "only do the least amount of work possible"; offer a solution not a new problem (incremental adoption); build fast, refactor, open source (Formik v0 in a day, refactored over a month); "it's a numbers game. Just keep on publishing stuff."

**Signature idea:** **A named workflow that is itself the product** — describe→generate→select-iteration→edit→copy-paste — plus constraint-as-liberation (markup-only, single framework) and the "no slop" quality bar as a named rejection criterion.

### 3.11 Charli Marie Prangley — marketing sites / B2B SaaS (Kit, ex-ConvertKit) · craft-first + growth

*(Weakest verification route (T2 revenue, Kit newsroom + estimate tracker) but the most complete, transferable end-to-end workflow in the set.)*

**Named workflow** (four first-party bodies forming one sequence):

- **A. Planning:** (1) define the **site's goal and the visitor's intent** ("content or hire me") before any pages; (2) plan the sitemap (pages + templates); (3) **scope an MVP first**; (4) design the MVP homepage as the **seed of a design system/brand**. Ordering rule: **content before design** — "Copy is the exact words… content is an outline of what points need to be communicated."
- **B. Wireframing:** know the content first → **Crazy 8's** (fold paper, 8 rapid wireframe ideas — "drawing nicely is not the point") → personal symbol key (line = headline, squiggle = body, crossed box = image) → star promising bits and combine → **grey-box wireframes only** ("I don't want the person who is critiquing this wireframe to think about anything other than the structure") → **"sleep on it" gate** — "come back to it the next day before you share for feedback or before you start on the visuals."
- **C. Full ConvertKit page process:** project arises → conversation → synthesize notes → content outline → solo wireframe → **share-for-structure gate** → copywriter + visual design in parallel → edit copy in → **sign-off gate** (requester + director of marketing) → prepare for build (**no red-lining**: final design on its own Figma page + GitHub issue + exported assets) → developer builds, designer QA loop → **ship → measure** (data-request dashboards) → goal-setting & testing loops (OKRs, NorthStar A/B tool, pre/post-mortems).
- **D. Post-launch loop:** analyze (Hotjar heatmaps/recordings — 75% vs 48% desktop/mobile reach) → change based on data (value-led header, buy buttons) → review & publish → **check back in weeks**; documented wins: 721% migrations-traffic increase, 65% more demo clicks, 5% signup uplift.
- **E. Rebrand:** research phase → three **brand personality traits (bold, sincere, expert)** as the decision frame → rebranding in public → post-launch iteration measured by name adoption + branded search.

**Signature idea:** **Content-before-design as a hard rule + solo-with-gated-sharing collaboration** — she works alone and shares only at deliberate gates ("I'll only really share it with the team when I'm ready for feedback"), using grey-box wireframes as a critique-control device and "sleep on it" as a named self-review gate. The set's clearest Figma-first, developer-handoff workflow.

---

## 4. Parallels

### 4.1 Creator × element matrix

● = core/named practice · ◐ = partial/secondary or inferred · — = absent/not documented in first-party corpus

| Creator | Real-material | Feature-first | Low-fi early | Constraints as engine | Build real early | Divergent ideation | Named gate | External validation | Named loop | Extract & systematize | Taste systems | Post-launch data |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wathan | ● | ● | ● | ◐ | ● | ● | ● | — | ● | ● | ● | — |
| Otto | ● | ● | ◐ | ◐ | ● | ● | ● | ● | ● | ● | ◐ | ● |
| Bostock | ● | ◐ | ● | — | ● | ● | ● | ● | ● | ● | ◐ | — |
| Verou | ◐ | ● | ● | ● | ● | ◐ | ● | ● | ● | ● | ◐ | ● |
| Schoger | ● | ● | ● | ◐ | ◐ | ◐ | ● | — | ● | ● | ● | — |
| Stollenmayer | ● | ● | ◐ | ● | ● | ◐ | ● | ● | ● | ◐ | ● | — |
| Herbert | ● | ◐ | — | ● | ● | ◐ | ● | ● | ● | ◐ | ● | ● |
| McLeod | ◐ | ● | ● | ● | ● | ◐ | ● | ● | ● | ◐ | ◐ | ● |
| Stoiber | ● | ◐ | ◐ | ◐ | ● | ● | ● | ◐ | ● | ◐ | ● | ◐ |
| Palmer | ◐ | ◐ | ◐ | ● | ● | ● | ● | ◐ | ● | ◐ | — | ◐ |
| Prangley | ● | ● | ● | ◐ | — | ● | ● | ● | ● | ● | ● | ● |
| **Count ●** | **8** | **7** | **6** | **5** | **10** | **7** | **11** | **8** | **11** | **6** | **7** | **5** |

### 4.2 Per-element writeups

**Named quality gate (11/11 — the only universal element).** Every one of the 11 has at least one *named, falsifiable* quality test, and most have several. Otto's debate gate and the dogfooding "binge-close" test ([Building Twitter Bootstrap](https://alistapart.com/article/building-twitter-bootstrap/), [Shipping the new GitHub Issues](https://markdotto.com/blog/shipping-the-new-github-issues/)); Bostock's prototype-hypothesis gate ("your prototype only exists so that you can learn something") and context-deprived evaluation ([Design is a Search Problem transcript](https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)); Stollenmayer's [housewife test](https://www.gamedeveloper.com/design/game-design-deep-dive-creating-a-one-touch-platformer-in-i-zip-zap-i-); McLeod's "observable change" test and ["perfection is the enemy of good"](https://podcast.going-indie.com/episodes/how-blackbox-won-an-apple-design-award-ryan-mcleod/transcript) shipping gate; Herbert's MVP lens, gut-check, future-self, and 80%-polish gates ([Slopes Diaries](https://blog.curtisherbert.com/tag/slopes-diaries/)); Verou's consensus + user-test-the-North-Star gates ([Hovercar Framework](https://lea.verou.me/blog/2025/hovercar/)); Stoiber's ["make it work, make it right, make it fast — in that order"](https://mxstbr.com/notes/taste); Palmer's ["no slop"](https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/) bar; Prangley's ["sleep on it"](https://www.youtube.com/watch?v=PmmQjLqJQlY); Schoger's ["supercharge the defaults"](https://www.youtube.com/watch?v=7Z9rrryIOC4); Wathan's in-browser review ([Designing Tailwind UI Ecommerce](https://tailwindcss.com/blog/designing-tailwind-ui-ecommerce)). The universal move is converting "good design" from a vibe into a checkable test with a name.

**Named iteration loop (11/11).** Equally universal, and always *named*: Wathan's "work in cycles" / repeat-the-whole-thing ([Refactoring UI](https://www.refactoringui.com/book)); Otto's design↔code ping-pong ([Shipping Blended Diffs](https://markdotto.com/blog/blended-diffs)); Bostock's annealing search loop; Schoger's work-in-cycles; Stollenmayer's "jazz improvisation" and "back to the drawing board" ([Song of Bloom files](https://kamibox.de/songofbloom-files)); Herbert's seasonal April→November loop ([#30 Planning Ahead](https://blog.curtisherbert.com/slopes-diaries-30-planning-ahead/)); McLeod's "months" red-herring-removal loop; Stoiber's iterate-dissect-ship-iteration; Palmer's select-iteration loop; Prangley's post-launch heatmap→change→check-back loop; Verou's ship-then-iterate-toward-the-North-Star. The near-universal attitude: iteration after a full pass is expected, not failure — Wathan states it as law ("no amount of planning will lead to the right product on the first try").

**Build the real thing early (10/11).** The deepest consensus behind gates and loops. Otto: "Most design work happened in code" ([Building Twitter Bootstrap](https://alistapart.com/article/building-twitter-bootstrap/)); Wathan builds pages and reviews them *in the browser* because spacing is only judgeable there; Bostock makes exploration cheap with git branches and a screenshotting preview server; McLeod ships barebones hardware test apps ("Dude. It's perfectly linear" — [digital scale post](https://web.archive.org/web/20241202145253/https://medium.com/swlh/turning-the-iphone-6s-into-a-digital-scale-f2197dc2b6e7)); Stollenmayer prototypes in code until "it feels good"; Stoiber ships the first version before optimizing; Palmer's Framer prototypes precede any build; Verou built her own working Context Chips prototype; Herbert ships features, not versions. The lone exception: **Prangley**, whose workflow is deliberately Figma-first with a developer handoff (and *no red-lining* — the developer measures in Figma himself, [Inside Marketing Design](https://insidemarketingdesign.com/at/convertkit)). Schoger occupies the middle: the joint book advocates making it real, but his own series stays in Sketch.

**Real-material research (8/11, 3 more partial).** Nearly everyone starts from existing artifacts rather than blank canvas: Wathan catalogs dozens of real stores; Schoger redesigns real submitted pages; Bostock requires real data ("You can't really evaluate an idea without applying it to real data"); Stollenmayer starts from a filmed sea; Prangley writes a content outline from competitor research and user insights; Herbert reads SQL before redesigning pricing; Stoiber "gets more parts on the table"; Otto's ideation is problem-driven with real users. The unifying belief: the idea emerges from studying what already exists, not from introspection.

**Divergent ideation (7/11, 4 partial).** Generate many candidates before converging: Bostock's "wild explorations that looked nothing like the final graphic"; Wathan's ~50 pages with unique elements; Stoiber's quantity-over-quality brainstorming rounds and five-pieces→three-breakthroughs; Prangley's Crazy 8's; Palmer's DevGPT-vs-Webjourney proposals; Otto's "as many artboards as possible"; Verou's five competing Context Chips ideas; McLeod's 50–70-challenge backlog.

**External validation (8/11).** The pattern inverts the verification ranking: the strongest-verified creators validate *informally* — Wathan documents no external testing at all (team browser review only), Otto's signature dogfooding gate is self-observation (plus "several casual user studies" for split diffs — hence ●), and Bostock shows work to context-deprived friends — while **formal** usability/data testing appears in the mid-table: Verou's within-subjects usability studies (stopped at 5 of 6 participants, results lopsided); Herbert's A/B + kill-switch rollouts; Prangley's heatmaps, recordings, and exit-intent surveys; McLeod's hand-the-phone playtests and beta testers; Stollenmayer's housewife test. **Behavioral/self-review gates correlate with the strongest-verified workflows; formal user/data testing with the mid-table.**

**Low-fi early (6/11, 4 partial).** Grayscale-and-Sharpie (Wathan/Schoger: "hold the color… detail comes later"), grey-box wireframes with a symbol key (Prangley), hypothesis-testing prototypes that "don't need to look good" (Bostock), notebook sketches (McLeod), paper North-Star wireframes (Verou). Herbert's MVP lens achieves the same by cutting features instead of fidelity (marked —).

**Extract & systematize (6/11, 5 partial).** The abstraction stage: Otto's "abstraction and documentation" as a *named final stage* ("a toolkit built in style guide form"; "treat the docs like they're the product"); Wathan's outside-in component extraction ("pre-built LEGO creations, not just the bricks"); Bostock's Makefiles-as-reproducible-documentation and reusable examples ("don't generalize prematurely"); Verou's tiny-core + hooks Prism architecture; Schoger's shade/type/spacing systems; Prangley's design system seeded from the MVP homepage.

**Taste/personality systems (7/11).** Deliberate, one-time personality decisions: Wathan/Schoger "choose a personality… and stay consistent" + "limit your choices"; Stoiber's taste pipeline (parts → dissect → apply); Herbert's "I get you" thesis; Prangley's three brand traits (bold, sincere, expert) as the decision frame; Stollenmayer's physical-first aesthetic rule; McLeod's medium-native metaphor + "dialing back" the obvious; Bostock's principles-guide-but-never-dictate (partial — his stance is the counterweight: principles are *necessary but not sufficient*).

**Constraints as engine (5/11 core).** A signature of the award-winning solo designers more than the framework authors: McLeod's anti-touch constraint as the genre; Stollenmayer's "strip everything away" and tech-built-first constraints; Verou's ephemeral-vs-fundamental constraint taxonomy; Herbert's future-self maintenance budget; Palmer's markup-only SIUI and single-framework ("That constraint was rather liberating"). **Bostock is the explicit outlier (—)**: his whole method argues principles must not dictate the search.

**Post-launch measurement (5/11).** Only the live-service/product designers close the loop with data: Herbert (A/B, SQL, kill-switches), Prangley (heatmaps, 721%/65%/5% documented uplifts), McLeod (onboarding funnel telemetry), Otto (dark-shipping, feature flags, metrics before merge), Verou (38% avg response rate validation). The framework authors (Wathan, Bostock, Schoger) and Stollenmayer stop at shipping — the artifact is the deliverable.

### 4.3 Biggest divergences

1. **Where the real artifact lives.** Code/browser-first majority (Otto, Wathan, Bostock, Verou, Stoiber, Palmer, McLeod, Stollenmayer, Herbert) vs design-tool-first (Schoger's Sketch series; Prangley's Figma pipeline with developer handoff and a deliberate no-red-lining rule). Bostock takes it furthest: the git repo, preview server, and Makefile *are* the design environment.
2. **Ideal-first vs simple-first.** Verou's anti-MVP North-Star-first (design the ideal, then cut to a skateboard) is the philosophical opposite of Wathan/Schoger's "build the simple version first", Stoiber's "make it work", Palmer's "least amount of work possible", and Herbert's MVP lens — though both poles converge on shipping small; they differ on whether the *ideal* is articulated before or after the first ship.
3. **Who validates the design.** Self/team behavioral gates (Wathan's browser review, Otto's dogfooding binge-close, Stoiber's community feedback) vs context-deprived outsiders (Bostock's wife/friends) vs formal usability testing and A/B data (Verou, Herbert, Prangley, McLeod, Stollenmayer).
4. **Constraints: engine or enemy.** Nine designers wield named constraints as the design's generative engine; Bostock's search metaphor explicitly rejects letting principles or recipes constrain exploration ("necessary but not sufficient").

### 4.4 Elements found only in the top-ranked workflows

*(Top-ranked = the three strongest-verified creators: Wathan, Otto, Bostock. None of these three practices appears as a named practice in any of the other eight docs.)*

- **Abstraction-and-documentation as a named, first-class final stage** — only Otto ("ideation, debate and feature review, implementation, and lastly abstraction and documentation"; "treat the docs like they're the product"). Wathan's component extraction and Bostock's examples/Makefiles are the nearest relatives.
- **The dogfooding gate as a personal behavioral test** — only Otto ("I'd know we were on to something awesome if I could binge close dozens of issues without using the old interface").
- **Design-as-search with a simulated-annealing temperature schedule** — only Bostock (explore hot early, cool toward commitment as the deadline approaches: "figuring out at what point you are in your process").
- **The prototype-hypothesis gate + context-deprived evaluators** — only Bostock (every prototype tests one named hypothesis; show work to people who lack your intent).
- **Infrastructure as design process** — only Bostock (branches as "a safe place to work on things that are potentially bad ideas", a commit-screenshotting preview server, Makefiles as machine-readable documentation).
- **Outside-in component extraction with a "repeat the whole thing" law** — only Wathan ("pre-built LEGO creations, not just the bricks"; "no amount of planning will lead to the right product on the first try").
- **Documented micro decision loops with time-boxing** — only Wathan (the 2.5-hour KiteTail candidate-generation-and-rejection log).

Two observations: (a) these practices cluster around *code-native, dev-tool* workflows, which dominate the top of the verification ranking (8 of 11 verified creators ship developer-facing products — a skew of the route itself: usage-stat verification favors libraries); (b) none of the top three documents formal usability testing — their gates are behavioral, self-administered, and personal, which may be exactly what made their process docs abundant enough to verify deeply.
