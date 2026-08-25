# Max Stoiber — Depth Doc

Research date: 2026-08-17 · Wave 07 (Phase 2, depth docs) · Researcher (leaf subagent)

## 1. Eligibility Evidence

- **Scale (route: usage-stat, tier T1):** styled-components — npm **9,437,267 downloads/week** (2026-08-09 → 2026-08-15); GitHub **41,120 stars** (fetched 2026-08-17). Source: https://api.npmjs.org/downloads/point/last-week/styled-components. *(Copied from `working/evidence/max-stoiber-2026-08-17.json`; scale not re-verified per wave spec.)*
- **5-year window:** in-window (2021-08-17 → 2026-08-17).
- **Doc currency (one line):** First-party process content is live and actively maintained — his digital-garden notes (taste, decision-making, brainstorming, ship-faster) are dated Aug–Sep 2024 and linked from his current homepage; the 2019 CSS-in-JS essay remains listed on his homepage Essays list (67,287 views) and the site's Work section is current (OpenAI 2026–now).
- **Product-type tag:** dev tool (styled-components CSS-in-JS library; also react-boilerplate, Spectrum).
- **Craft/growth tag:** craft-first — Stoiber documents his design process in depth (the "How to have great taste" note contains a full named workflow plus a detailed case study of how the styled-components API was designed), so the craft tag applies.

## 2. Step-by-Step Workflow

Stoiber's anchor process is the named, ordered workflow in his note "How to have great taste" (Sep 05 2024), which he explicitly applies to the design of the styled-components API in the same note. He frames it as a taste-building + iteration method for making great things (products, libraries, systems). Supporting notes add named sub-techniques for ideation, decision-making, and shipping.

### A. The taste workflow — "How to have great taste" (2024)

1. **Get more parts on the table.** The first step is exposure: see more examples so you have more data to assess what works and what doesn't. "By seeing more examples, you have more data to be able to assess what works and what doesn't." He ties this to the "adjacent possible" idea that innovation happens by combining existing things in new ways (see also his note "How do you invent the future?"). Source: https://mxstbr.com/notes/taste
2. **Dissect the greats.** Break world-class work into its components and form an opinion about how they combine — the way a wine connoisseur breaks wine into taste/aroma/texture. He cites people who do this regularly (Brian Lovin's app dissections, Samuel Hulick's onboarding dissections, Harry Dry's marketing dissections) as evidence it works. Source: same.
3. **Iterate, iterate, iterate (the core loop).** "The only way I know of to make something great is to iterate": (a) build and ship the first version; (b) dissect what works and what doesn't; (c) ship an iteration to test your dissection; (d) repeat. Source: same.
4. **Quality gate — "Make it work, make it right, make it fast — in that order!"** This is his explicit ordering gate: if you try to make it right before shipping, you won't have enough feedback to iterate toward "right"; if you make it fast before it's right, you'll have to redo the fast work once it's right. So: make it work → ship → use feedback to iterate until right → then make it fast. Source: same.
5. **Apply taste (do the work).** Taste alone isn't enough — you have to learn how to apply it (Ira Glass's "The Gap"). This is the step where the taste workflow meets execution. Source: same.

### B. Case study — how the styled-components API came to be (same note)

Stoiber walks through the workflow applied to the styled-components API design (with Glen Maddern) — the strongest first-party demonstration of the process:

- **Making it work — five "pieces on the table" → three breakthroughs.** (1) Knowledge of component-library styling problems (ElementalUI at Thinkmill; Less required a fragile build setup; Radium/JSS lacked theming). (2) The style-specific-components pattern (`Grid`, `Row`) → breakthrough #1: move styling to component level by default, `function('tag')` syntax. (3) Injecting CSS from JS (Glen invented CSS Modules) → breakthrough #2: write actual CSS syntax in JS; a `margin(1)` function prototype "didn't feel right," so they kept real CSS syntax. (4) Tagged template literals (Glen's overnight prototype) → breakthrough #3: interpolated functions for conditional styling based on props. (5) React Context for theming → the Provider-style `ThemeProvider` API. Source: https://mxstbr.com/notes/taste
- **A named decision gate inside "making it work": the theme-injection choice.** For getting the theme into components he lists three candidate APIs (two-argument function; one destructured argument; `props.theme`) and evaluates each against explicit criteria (annoying empty-variable assignment; ES5 compatibility; cognitive overhead for newcomers; interplay with React's `defaultProps`/prop-override conventions). "This might've been the decision we spent the most time on, and that took the most taste." This is a documented option-evaluation gate. Source: same.
- **Making it right — launch + community feedback loop.** After the core API, "we spent a few weeks writing extensive docs... we launched the library." Then "from the community feedback and our own experiences, we kept iterating on many smaller decisions": `elem.div` shorthands for editor autocomplete, restyling components via `elem(Component)`, naming the library `styled-components` / `styled.div` to match natural language, overriding styles within a parent, Sass-style nesting, and changing `injectGlobal` → `createGlobalStyle`. Source: same.
- **Making it fast — performance phase.** "once we felt like the abstractions were just right, we started focusing on performance and making it fast. Super fast." He links the styled-components v5 "Beast Mode" announcement as the evidence (that Medium post is bot-blocked from direct reading; cited here as referenced within his note). Source: https://mxstbr.com/notes/taste (link: https://medium.com/styled-components/announcing-styled-components-v5-beast-mode-389747abd987)

### C. Supporting named sub-techniques (his other notes)

- **Decision-making loop** ("How to be better at making decisions", Sep 02 2024): (1) Write it down — evaluation criteria first, in order of priority, then considered options with pros/cons, then preferred option and why; (2) share it with at least one person (writing for a reader forces clear thinking); (3) reflect with the benefit of hindsight months/years later (his RethinkDB regret at Spectrum as the worked example). Ships a reusable decision-log template. Source: https://mxstbr.com/notes/decision-making
- **Brainstorming structure** ("How we make brainstorming work", Aug 22 2024): multiple rapid rounds of divergence and convergence — (1) silent writing (2 min, quantity over quality); (2) review the combined list (2 min); (3) discussion (5 min); (4) repeat. "Quantity over quality" is called absolutely critical. Source: https://mxstbr.com/notes/brainstorming
- **Shipping techniques** ("How to ship faster", Aug 22 2024): outline speedrunning (recursively outline an MVP, speedrun filling it in, then perfect); tracer bullets (short develop→deliver→ask cycles to make the target visible); eliminate low-velocity stuff. Source: https://mxstbr.com/notes/how-to-ship-faster
- **Innovation framing** ("How do you invent the future?", Sep 02 2024): "get more parts on the table" / the adjacent possible — everything he's invented came from connecting existing ideas in new ways. Source: https://mxstbr.com/notes/innovation

## 3. What Makes It Distinct

- **A named taste workflow, not just rationale.** Unlike many designers who only publish design rationale, Stoiber publishes an explicit ordered method — get parts on the table → dissect the greats → iterate (build/ship → dissect → ship iteration → repeat) — with a hard ordering gate ("make it work, make it right, make it fast"). Source: https://mxstbr.com/notes/taste
- **The "pieces on the table" theory of API design.** His account of the styled-components API is structured as five discrete prior-knowledge pieces combining into three breakthroughs — a concrete, named mechanism for how design ideas emerge, not a vague "we iterated." Source: same.
- **Documented option-evaluation gate with explicit criteria.** The three-way theme-injection decision is shown as a real trade-off analysis (ES5 compatibility, cognitive overhead, React conventions) — a rare first-party look at a specific API fork and why one option won. Source: same.
- **"Make it work → right → fast" as a sequencing law.** The argument that optimizing before correctness forces rework is stated as a general principle, and the styled-components timeline (work → docs/launch/community iteration → v5 performance) is the worked proof. Source: same.
- **Process as a public digital garden.** His notes are explicitly an "ongoing log of what I have learned" with maturity statuses (seedling/budding/evergreen) — the process itself is versioned and open to contribution ("tell me about them"). Source: https://mxstbr.com/notes/taste

## 4. Sources

- How to have great taste (Sep 05 2024): https://mxstbr.com/notes/taste
- How to be better at making decisions (Sep 02 2024): https://mxstbr.com/notes/decision-making
- How we make brainstorming work (Aug 22 2024): https://mxstbr.com/notes/brainstorming
- How to ship faster (Aug 22 2024): https://mxstbr.com/notes/how-to-ship-faster
- How do you invent the future? (Sep 02 2024): https://mxstbr.com/notes/innovation
- Why I Write CSS in JavaScript (Feb 18 2019): https://mxstbr.com/thoughts/css-in-js
- styled-components v5 "Beast Mode" (referenced within the taste note; Medium bot-blocked, not directly read): https://medium.com/styled-components/announcing-styled-components-v5-beast-mode-389747abd987
- Homepage / notes index: https://mxstbr.com/ · https://mxstbr.com/notes

---

**Anomalies / dead ends:** (1) The styled-components v5 Medium post is bot-blocked (403) — cited only as referenced within his note, not as a read source. (2) The thoughts index page returned only headings via extraction; the css-in-js essay was read directly and is confirmed live. (3) No interview/talk transcript was needed — his own notes carry the full process; the evidence JSON's note that his verifiable agency design work (Animade Frankensim) is out of window and not used for scale stands.
