# Mike Bostock — Depth Doc

**Designer:** Mike Bostock (D3.js, Observable, ex-NYT Graphics)
**Research date:** 2026-08-17 · **Verdict:** DEPTH-PASS

---

## 1. Eligibility Evidence

- **Scale (usage-stat route, T1):** npm **15,818,249 downloads/week** (2026-08-09 → 2026-08-15) and GitHub **113,478 stars** for D3.js — fetched live 2026-08-17 from official APIs: https://api.npmjs.org/downloads/point/last-week/d3 and https://api.github.com/repos/d3/d3. *(Copied from evidence JSON `working/evidence/mike-bostock-2026-08-17.json`; not re-verified per wave spec.)*
- **Route + tier:** usage-stat / T1 (official API figures, no award route needed).
- **5-year in-window check:** in-window (evidence JSON `window_5yr`).
- **Doc-currency check (one line):** bost.ocks.org/mike/ is live and its essays are still cited as current — official D3 docs (d3js.org/d3-selection/joining) cite "Thinking With Joins" as the introduction to data joins, the UW IDL D3 tutorial cites "Thinking with Join" and "How Selections Work", and Observable's March 2026 blog Q&A still frames Bostock as D3's author (per evidence JSON `doc_currency`).
- **Product-type tag:** dev tool (data-visualization library + notebook platform).
- **Craft/growth tag:** **craft-first** — Bostock documents his design process in depth and in his own words (the "Design is a Search Problem" talk, the "For Example" and "Visualizing Algorithms" essays, Observable design essays), so the craft-first tag is fully evidenced.

---

## 2. Step-by-Step Workflow

Bostock's named, ordered design workflow is **"Design is a Search Problem"** (OpenVis 2014 keynote, https://www.youtube.com/watch?v=fThhbt23SGM; transcript read at https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM). His thesis: design principles are *necessary but not sufficient* — they are not blueprints, so a successful process must explore the design space efficiently. The workflow below is his own sequence, supplemented by the named loops in his essays.

### Step 1 — Frame the problem as a search, not a recipe
Treat design as a maze to be explored: you know only the local space around you, not where approaches dead-end. Principles (he cites Rams's "less but better" and Fitts's law) guide which paths look promising but never dictate the answer. Consequence: budget time for exploring things that *won't* work, because that is how you find what does. *(Source: "Design is a Search Problem" transcript, opening + "the reality of the design space is more like this" maze section, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 2 — Explore widely and divergently at the start
Begin with "wild explorations that looked nothing like the final graphic." He documents this concretely: for the NYT "Taking the Battle to the States" graphic the early commits were scatterplots, connected scatterplots on log scales, box plots, and multiple cartogram forms (discontinuous, Dorling donut, rectangular/Demers) before stabilizing; the corporate-tax graphic tried scatter, connected-scatter, box plots, and beeswarm variants. The goal is breadth — try many encodings, not polish. *(Sources: "Design is a Search Problem" transcript — "Taking the Battle to the States" and corporate-tax commit-history walkthroughs, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 3 — Prototype to test one hypothesis at a time
"Your prototype only exists so that you can learn something… every time you make a prototype you should know in your head what is the prototype trying to show you… you have a hypothesis that you are testing." Prototypes do not need to look good, be polished, or be labeled. This is an explicit quality gate: a prototype with no stated hypothesis is wasted effort. *(Source: "Design is a Search Problem" transcript — "your prototype only exists so that you can learn something" passage, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 4 — Evaluate constantly, with people who lack your context
Because you are "too close" to your own work, you cannot fairly judge it. His gate: show the graphic to people outside the graphics department (his wife, friends) who don't share his biases, and check whether it "communicates the way I expect it to do." He also verbalizes what is working and not working so that when he changes paths he carries forward the parts that work instead of restarting from scratch. *(Source: "Design is a Search Problem" transcript — "it's really hard for you to evaluate your own work… show your work to somebody else" passage, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 5 — Make exploration cheap and visible (git + branches + live preview)
Every NYT graphic is a git repo; he uses branches as "a safe place to work on things that are potentially bad ideas" (colleague Shan Carter names risky branches "controversy"). The internal "preview" server serves any commit live and screenshots every commit, so feedback becomes passive and fast — you can see what others are working on without being asked. *(Source: "Design is a Search Problem" transcript — git/branches/preview section, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 6 — Anneal: cool down from exploration to commitment
He models the process as **simulated annealing**: early on the "temperature" is hot — you accept bad ideas and explore widely; as the deadline approaches you cool down, explore less, and commit to the idea. "Part of the art of design here is figuring out at what point you are in your process, how much time you have left, and whether you should start slowing down." This is the convergence gate that ends the search loop. *(Source: "Design is a Search Problem" transcript — "this process is sort of like simulated annealing" passage, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Step 7 — Prune constantly and systematize the survivors
Move fast by deleting code as you go — he notes he deleted more lines than he added on the NYT Senate-model project, and that pruning "helps for my sanity." He also captures surviving workflows as machine-readable build files: "Makefiles are machine-readable documentation that make your workflow reproducible," letting him re-run a six-month-old data pipeline with `make` and recycle rules across projects. *(Sources: "Design is a Search Problem" transcript — "if you want to move quickly you have to delete code as you go" passage, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM; "Why Use Make", https://bost.ocks.org/mike/make/)*

### Step 8 — Try bad ideas on real data
"You can't really evaluate an idea without applying it to real data" — a design that looks good in the abstract may fail on the characteristics of the actual dataset, so evaluation requires real data, not mockups. *(Source: "Design is a Search Problem" transcript — "you have to try these bad ideas as you're going along" passage, https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM)*

### Supporting named loops (used inside the search process)

- **The visualization-depth ladder (black box → gray box → white box).** When designing an algorithm visualization, he classifies the design by how much internal state it exposes: Level 0/black box (output only — good for comparing algorithms), Level 1/gray box (intermediate output — shows *how* but not *why*), Level 2/white box (internal state — most explanatory but highest reader burden). Choosing the level is a deliberate design decision per graphic. *(Source: "Visualizing Algorithms", https://bost.ocks.org/mike/algorithms/)*
- **The self-correction loop.** He documents catching his own visualization bug: an earlier Prim's color-flood "had a bug where the color scale rotated twice as fast as intended; this suggested that Prim's and Wilson's algorithms produced very different trees, when in fact they appear much more similar than different." The correction is an explicit quality gate — the visualization was redesigned until it no longer misled. *(Source: "Visualizing Algorithms", https://bost.ocks.org/mike/algorithms/)*
- **The example-driven refinement loop.** His "For Example" talk (Eyeo 2013) describes distilling each finished graphic into small reusable examples ("an extension of working knowledge… an apothecary capturing some precious essence"), with the rules: know your audience, show *why* a feature matters (not just what it does), and "don't generalize prematurely" — keep a low bar to sharing. *(Source: "For Example", https://bost.ocks.org/mike/example/)*
- **The 4-step algorithm workflow.** For building TopoJSON's topology inference he names an ordered pipeline — **extract → join → cut → dedup** — each step implemented in its own source file, debugged with a purpose-built visual debugger, and validated by a test suite (he rewrote the whole implementation for TopoJSON 1.4.0). *(Source: "How To Infer Topology", https://bost.ocks.org/mike/topology/)*
- **The reusable-component convention.** For chart code he specifies a named pattern — "implement charts as closures with getter-setter methods" — so components are configurable, chainable, and inspectable. *(Source: "Towards Reusable Charts", https://bost.ocks.org/mike/chart/)*

### The four design principles for the Observable platform (2017)
When designing the Observable notebook environment he names four ordered principles — **Reactivity, Visibility, Reusability, Portability** — each with a concrete mechanism (reactive cells, inline visual outputs, imports with `with`-clause rewiring, browser-native portability). These are the design contract he used to build the tool, and they show his principle-then-verify method applied at platform scale. *(Source: "A Better Way to Code", https://medium.com/@mbostock/a-better-way-to-code-2b1d2876a3a0)*

---

## 3. What Makes It Distinct

- **Design-as-search with a temperature schedule.** The simulated-annealing metaphor is not generic "iterate a lot" advice — it gives a *named, time-aware* rule for when to explore widely vs. commit, tied to deadline pressure. Few designers articulate the exploration→commitment transition as an explicit control knob.
- **The prototype-hypothesis gate.** "Every prototype tests a hypothesis" turns prototyping from a vague activity into a falsifiable experiment — a concrete quality gate rather than a vibe.
- **Evaluation by context-deprived observers.** His feedback loop is specifically about removing *his own* intent-bias by showing work to people who don't know what he's trying to do — a precise, non-obvious mechanism (not "get feedback" in the abstract).
- **Infrastructure as part of the design process.** He treats git branches, a commit-screenshotting preview server, and Makefiles as first-class design tools — making exploration cheap and reproducible is itself a design decision, not an afterthought.
- **The black/gray/white-box ladder.** A named taxonomy for choosing how much internal state a visualization exposes, with explicit trade-offs (explanatory power vs. reader burden vs. comparability) — a decision framework specific to algorithm/process visualization, not generic chart advice.
- **Self-documented failure.** He publishes his own caught bugs (the Prim's color-flood error) and "disasters" from early commits, treating the correction loop as evidence of process rather than something to hide.
- **Example-driven tool design.** "For Example" argues examples are the primary design medium for a library — a working-knowledge repertoire that precedes and informs formal abstraction ("don't generalize prematurely").

---

## 4. Sources

Canonical first-party locations (all by Bostock himself):

- **Design is a Search Problem** (OpenVis 2014 talk): https://www.youtube.com/watch?v=fThhbt23SGM — transcript: https://videodb.org/mike-bostock-design-is-a-search-problem/fThhbt23SGM
- **Visualizing Algorithms** (Eyeo 2014 essay/talk): https://bost.ocks.org/mike/algorithms/
- **How To Infer Topology** (essay): https://bost.ocks.org/mike/topology/
- **For Example** (Eyeo 2013 talk transcript): https://bost.ocks.org/mike/example/
- **A Better Way to Code** (2017, Observable design): https://medium.com/@mbostock/a-better-way-to-code-2b1d2876a3a0
- **Towards Reusable Charts** (essay): https://bost.ocks.org/mike/chart/
- **How To Scroll** (essay): https://bost.ocks.org/mike/scroll/
- **Object Constancy** (essay): https://bost.ocks.org/mike/constancy/
- **Thinking with Joins** (essay): https://bost.ocks.org/mike/join/
- **How Selections Work** (essay): https://bost.ocks.org/mike/selection/
- **Why Use Make** (essay): https://bost.ocks.org/mike/make/
- **Essay index / talks list:** https://bost.ocks.org/mike/
- **Observable notebooks:** https://observablehq.com/@mbostock
