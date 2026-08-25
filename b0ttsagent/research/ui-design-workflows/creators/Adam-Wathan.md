# Adam Wathan — Depth Doc

Research date: 2026-08-17 · Wave 07 (Phase 2, depth docs) · Researcher 1

## 1. Eligibility Evidence

- **Scale (route: usage-stat, tier T1):** Tailwind CSS — npm **85,411,470 downloads/week** (2026-08-09 → 2026-08-15); GitHub **97,250 stars** (fetched 2026-08-17). Source: https://api.npmjs.org/downloads/point/last-week/tailwindcss. *(Copied from `working/evidence/adam-wathan-2026-08-17.json`; scale not re-verified per wave spec.)*
- **5-year window:** in-window (2021-08-17 → 2026-08-17).
- **Doc currency (one line):** Anchor workflow post "Designing Tailwind UI Ecommerce" (Aug 2021) is still live and linked from the active tailwindcss.com blog (latest post May 2026, v4.3); Wathan delivered a design-process talk "Designing a Component Library" at Laracon US 2024 (transcript on laracontv.com); Refactoring UI still sold (2026 copyright) — workflow confirmably current.
- **Product-type tag:** dev tool (Tailwind CSS framework; Tailwind UI/Plus component library for developers).
- **Craft/growth tag:** craft-first — Wathan documents his design process in depth (blog process posts, the Refactoring UI book, conference talks), so the craft tag applies.

## 2. Step-by-Step Workflow

Wathan documents two complementary named workflows plus a documented micro decision loop. The anchor is his component-kit workflow (A); the book supplies the feature-level "start from scratch" process (B); the build log supplies the single-problem decision loop (C). All steps are first-party (his own blog, book, gist, and talk).

### A. Component-kit workflow — "Designing Tailwind UI Ecommerce" (2021)

1. **Research and catalog.** Study as many real sites as possible and catalog every UI pattern you can pick out (product overviews, product lists, checkout forms, shopping carts, category filters, customer reviews, order history, category mega menus, product quickviews, promo sections). Scour dozens of store types (Everlane, Allbirds, Grovemade, Casper, Toontrack, and more) and deliberately avoid focusing on any one store type — that is what reveals which patterns are truly universal. This is where category concepts emerge (e.g., the "promo section": ecommerce "heroes" are almost never true heroes, so they invented a category that could also sit mid-page). "Organizing and categorizing all of these ideas was almost as much work as designing them." Source: https://tailwindcss.com/blog/designing-tailwind-ui-ecommerce
2. **Design full page examples.** Design everything as complete pages from the very beginning (~50 pages: home pages, category listings, product pages, checkout forms). Lesson learned from the earlier Application UI / Marketing kits: components designed in isolation feel off when assembled (font size a little too big, not enough whitespace, too much contrast making secondary content stand out). Reuse a few things across pages (footer/navbar) to move quickly, but make every core element of every page unique to generate as many ideas as possible. Source: same.
3. **Build the pages (quality gate).** Take the full-page designs in "pretty good" shape, build them as best you can, then review the finished designs together **in the browser** and make adjustments. Expect a lot of small changes (spacing details are easier to judge in the browser than in a design file) and sometimes drastic ones — totally replacing part of a design if it doesn't look as good as hoped, or if matching the design exactly would make the code needlessly complex for little benefit. "Definitely think everything turns out a lot better when we are open to iterating on designs as we go instead of just throwing them over the wall." Source: same.
4. **Extract the individual components.** Once page designs are finalized and built, extract the individual elements into their own templates (Product Overviews from product pages, Product Lists from category pages, Promo Sections from home pages). Err on the side of **bigger** components — "pre-built LEGO creations, not just the bricks" — because it's easy to pull a small piece out of a bigger component, but hard to assemble small pieces into a big idea. This is the "outside-in" approach. Source: same.
5. **Take inventory, and repeat the whole thing (iteration loop).** "A lesson I keep re-learning... no amount of planning will lead to the right product on the first try. You have to keep iterating and improving — it's not a linear process." After designing/building pages and extracting components, assess where you are and find the holes you were blind to at first (e.g., only two mega-menu ideas because the "open" state was never designed; a disproportionate number of card-based designs on off-white backgrounds and not enough flat designs). Go back to the design step, design new concepts to fill the gaps, and re-run the cycle. Source: same.

### B. Feature-level process — Refactoring UI, "Starting from Scratch" (book, Wathan & Schoger)

1. **Start with a feature, not a layout.** Don't design the shell (top nav, sidebar, container, logo) first — an app is a collection of features, and you don't have the information to decide navigation until you've designed features. Start with one piece of actual functionality (e.g., "searching for a flight": departure city, destination city, departure date, return date, search button). Source: https://www.refactoringui.com/book
2. **Detail comes later.** Don't get hung up on low-level decisions (typefaces, shadows, icons) in the earliest stages. Sketch on paper with a thick Sharpie (a Jason Fried trick) so detail is impossible; **hold the color** and design in grayscale so spacing, contrast, and size do the heavy lifting, then add color later. Source: same.
3. **Don't over-invest.** Low-fidelity exists to move fast so you can start building the real thing as soon as possible. Sketches and wireframes are disposable — use them to explore, leave them behind once you've made a decision. Source: same.
4. **Don't design too much → Work in cycles (iteration loop).** Don't design every feature up front. "Instead of designing everything up front, work in short cycles. Start by designing a simple version of the next feature you want to build. Once you're happy with the basic design, make it real... Iterate on the working design until there are no more problems left to solve, then jump back into design mode and start working on the next feature." "Build the real thing as early as possible so your imagination doesn't have to do all the heavy lifting." Source: same.
5. **Be a pessimist.** Don't imply functionality you aren't ready to build; expect features to be hard to build; design the smallest useful version you can ship. "Build the simple version first and you'll always have something to fall back on." Source: same.
6. **Choose a personality.** Pick font, color, border radius, and language deliberately and stay consistent (mixing square and rounded corners almost always looks worse than one or the other). Source: same.
7. **Limit your choices.** Define systems in advance (8–10 shades per color, a restrictive type scale) so you make each decision once instead of every time you design. Source: same.

### C. Single-problem decision loop — KiteTail build log (2017)

For one UI problem (the "publish product" button): (1) list the specific problems with the current design (it didn't show the current state explicitly, had no place for validation errors, and gave no confirmation for a high-consequence action); (2) generate multiple candidate solutions (confirmation modal, standard select menu, custom popover menu); (3) weigh each against the identified problems and reject those that don't solve them; (4) iterate to a breakthrough (the popover acts as a built-in confirmation step and can grey out the "Published" option with an explanation); (5) time-box the loop — "this whole thing probably took 2.5 hours of screensharing and brainstorming to really nail." Source: https://gist.github.com/adamwathan/ad0e5fe6c78f8239cf809b8153e7c274

### Component-design principles — "Designing a Component Library" (Laracon US 2024 talk)

When building component systems: prefer composable, HTML-like APIs over "prop city" (size / icon / iconLeft / iconRight / descriptionPlacement props that spiral out of control and can't change responsively); mark elements with `data-slot` attributes so parents can target them regardless of element type; never bake margins into components — handle spacing contextually; use CSS features (grid, `:has()`, `isolation`, subgrid, CSS custom properties as "responsive props") so components stay flexible without JavaScript. Source: https://laracontv.com/laracon-us/2024/designing-component-library (transcript of his own words; video: https://www.youtube.com/watch?v=MrzrSFbxW7M)

## 3. What Makes It Distinct

- **Design as a developer, for developers.** Wathan's framing is "design with tactics, not talent" — he explicitly positions his process as learnable tactics rather than artistic talent, which is why his workflow is unusually concrete and executable. Source: https://www.refactoringui.com/
- **Outside-in component extraction.** The counterintuitive claim that components are better when designed as complete pages first and then extracted ("LEGO creations, not bricks") — the opposite of the common "design components in isolation" approach. Source: https://tailwindcss.com/blog/designing-tailwind-ui-ecommerce
- **The "repeat the whole thing" loop as a product-design law.** "No amount of planning will lead to the right product on the first try" — he treats gap-finding after a full build-and-extract cycle as a normal, expected step, not a failure. Source: same.
- **Work in cycles / build the simple version first.** Explicitly refuses to design everything up front; the loop (design simple → make real → iterate → back to design mode) is a named method, not an aspiration. Source: https://www.refactoringui.com/book
- **Documented micro decision loops.** The KiteTail publish-button log shows his actual 2.5-hour candidate-generation-and-rejection loop, with the "good design is invisible" payoff. Source: https://gist.github.com/adamwathan/ad0e5fe6c78f8239cf809b8153e7c274
- **Low pain tolerance as a design driver.** In the Laracon Q&A: "having that low developer experience pain tolerance is a required ingredient for having the grit to sort of push through and make things the best they can be at any cost." Source: https://laracontv.com/laracon-us/2024/designing-component-library

## 4. Sources

- Designing Tailwind UI Ecommerce (Aug 2021, bylined Adam Wathan): https://tailwindcss.com/blog/designing-tailwind-ui-ecommerce
- Refactoring UI — book + site (Wathan & Schoger): https://www.refactoringui.com/ · https://www.refactoringui.com/book
- Building React + Vue support for Tailwind UI (Apr 2021): https://blog.tailwindcss.com/building-react-and-vue-support-for-tailwind-ui
- 7 Practical Tips for Cheating at Design (Feb 2018, Wathan & Schoger; tactics listicle — supplementary only): https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886
- Building KiteTail #6: New logo, cracking UI problems, and testing tricks (Jun 2017): https://gist.github.com/adamwathan/ad0e5fe6c78f8239cf809b8153e7c274
- Designing a Component Library — Laracon US 2024 (talk + transcript): https://laracontv.com/laracon-us/2024/designing-component-library · video: https://www.youtube.com/watch?v=MrzrSFbxW7M
- Designing with Tailwind CSS (free video course; process demonstrated, not cited for specific steps): https://v1.tailwindcss.com/course
- adamwathan.me (articles/talks/journal index): https://adamwathan.me/

---

**Anomalies / dead ends:** (1) No verbatim "build the ugly version first" quote found in first-party content; the verified first-party equivalents are the book's named "Work in cycles / build the simple version first" method and the ecommerce post's "repeat the whole thing" loop — documented as such above. (2) YouTube transcript services (youtubetranscript.com, tactiq, notegpt, downsub, youtube-transcript.io) all failed to return the Laracon 2024 transcript; it was instead obtained from laracontv.com's own transcript page. (3) Refactoring UI chapter text was verified via a third-party PDF copy of the book; citations point to the official book page, not the copy.
