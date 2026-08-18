# Jared Palmer — Depth Doc

Research date: 2026-08-17 · Phase 2 (depth docs) · Researcher: leaf subagent

## 1. Eligibility Evidence

- **Scale (route: usage-stat, tier T1):** Formik — npm **3,844,046 downloads/week** (2026-08-09 → 2026-08-15); GitHub **34,325 stars** (fetched 2026-08-17). Source: https://api.npmjs.org/downloads/point/last-week/formik. *(Copied from `working/evidence/jared-palmer-2026-08-17.json`; scale not re-verified per wave spec.)*
- **5-year window:** in-window (2021-08-17 → 2026-08-17).
- **Doc currency (one line):** Anchor 2018 blog post is a launch story, but the depth workflow comes from the bylined "Announcing v0: Generative UI" post (Oct 2023, still live on vercel.com/blog) and 2025 first-party interviews (Madrona Jul 2025; Latent Space Nov 2025) — workflow confirmably current.
- **Product-type tag:** dev tool (Formik form library; Turborepo build system; v0 Generative UI tool — all developer-facing).
- **Craft/growth tag:** growth/experimentation — Palmer is a designer-turned-developer whose documented process is launch-fast-and-iterate ("speed matters", "numbers game", "only do the least amount of work possible"). Because he documents his design process in depth (the named Generative UI workflow, the designer-era Framer prototyping loop, the v0 quality gate), the craft tag also applies per schema.

## 2. Step-by-Step Workflow

Palmer has no single book-length process doc; his workflow is reconstructed from his own words across a bylined blog post and interviews. The named, ordered workflow is the **Generative UI** loop (A); his designer-era prototyping loop (B) is the design-side process; the v0 product process (C) carries the explicit quality gate; the Formik/Turborepo methodology (D) supplies the governing principles. All steps are first-party (his bylined post or his own words in interviews).

### A. Generative UI workflow — the named, ordered loop (v0, 2023)

Named in his own bylined post: "We call it Generative UI—combining the best practices of frontend development with the potential of generative AI." The ordered sequence as documented:

1. **Describe the interface you want to build.**
2. **Generate** — v0 produces code using open-source tools like React, Tailwind CSS, and Shadcn UI.
3. **Select an iteration and keep editing in v0** (iteration loop — the workflow is explicitly not one-shot).
4. **Copy and paste that code into your app and develop from there.**

Source: https://vercel.com/blog/announcing-v0-generative-ui (bylined Jared Palmer, Oct 11 2023)

The iteration loop is reinforced in the Vercel-official guidance for the v0 workflow (product-level first-party, not bylined to Palmer): "Take the iterative approach — Start by focusing on individual components; Test and refine each one before moving on to the next; Fine-tune the smaller pieces... Gradually build up to complete landing pages by piecing together the components, rather than attempting a lengthy single-piece generation all at once." And: "Build the pieces of your design first, like buttons and images, and then tell v0 how to arrange them." Source: https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0

### B. Designer-era prototyping loop (his time as a designer, ~2013–2016)

From his own account of his freelance/agency design days (The Palmer Group):

1. **Design in Photoshop** — his tool of the era for app design.
2. **Import the Photoshop layers into Framer and animate them quickly with a little bit of code** — "not like scary amounts of code, but a little bit of code."
3. **Reach super-high fidelity** — "you'd see it and it would feel like super high fidelity."
4. **Hand it to a client to play with before it was built** (client-feedback iteration loop) — the prototype becomes the reviewable artifact that precedes any build.

Source: https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/ (Jul 23 2025). He explicitly frames v0 as "the AI version of it" — the same preview-on-the-right / code-on-the-left interface.

### C. v0 product-development process — quality gate + iteration (2023)

From his own account (Madrona + Latent Space interviews):

1. **Set a quality gate up front:** "we had one rule, which was that no random acts of AI, no slop, it had to be pretty good." He rejects prior "random acts of AI" (docs, chatbots) as not good enough. Source: https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/
2. **Generate options:** two proposals to leadership — DevGPT (a ChatGPT/Perplexity-style dev assistant) and Webjourney (Midjourney-style UI generation). Source: same.
3. **Prototype to find key unlocks:** "we did some prototypes, and I soon realized that summer that a couple of things were key unlocks. The first was that these models are really good at HTML and they're really good at Tailwind CSS" — Tailwind co-locates all style info at each div, which is ideal for LLM output. Source: same.
4. **Constrain scope deliberately:** ship "SIUI" — markup only, not full code generation — "an important constraint because it allowed us to render the user interface on the fly" and gave a Midjourney-style pick-one experience. Source: same. The single-framework constraint is echoed in Latent Space: "focused on building Next.js apps, specifically Next.js apps. That constraint was rather liberating for the team at the time and it lets us really like laser focus." Source: https://podscan.fm/podcasts/latent-space-the-ai-engineer-podcast/episodes/inside-githubs-ai-revolution-jared-palmer-reveals-agent-hq-amp-the-future-of-coding-agents (Nov 10 2025)
5. **Launch, then iterate on the modality:** the initial interface was Midjourney-like (click components, reprompt) because chat wasn't possible at 4k-token context; ~9 months later "we rebased towards chat in the course of a month. We wrote the whole app." Source: Madrona + Latent Space. His stated iteration arc: "we've gone from text to UI to now we're at this text to app modality, and I think we're going to get to text to business in the future." Source: Madrona.

### D. Personal methodology — Formik / Turborepo principles

- **Solve your own problem / frustration-driven.** Formik came from forms pain in React; Turborepo from 10-minute deploys ("I'm very impatient... I need to stay nimble"). Source: https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/
- **Do the least work possible:** "only do the least amount of work possible, be as lazy as we possibly can. Only incrementally do what's necessary, and then cash as much as possible." Source: same.
- **Offer a solution, not a new problem:** "I often think about, are you creating a new problem or actually offering a solution? And the goal is to always actually offer a solution, and 9 times out of 10, that involves some sort of migration and adoption plan that is incremental." Source: https://syntax.fm/show/460/supper-club-turborepo-with-jared-palmer/transcript (May 20 2022)
- **Build fast, refactor, then open source:** "Ian White and I wrote Formik v0 in a day and refactored it over the course of a month or so before open sourcing it in 2017." Source: https://reactiflux.js.org/transcripts/jared-palmer-2 (Jan 15 2021)
- **Learn by solving problems:** "I learn new tools/frameworks when researching or solving a problem. This is my guiding light." Source: same.
- **Build a breakable toy:** "Build a breakable toy for yourself like a blog or a CMS or a todo list app... Something small... Use it to learn about the tools you're interested in." Source: same.
- **Keep building / numbers game:** "Keep on building. Don't be afraid to try out new stuff. It's a numbers game. Just keep on publishing stuff." Source: https://reactiflux.js.org/transcripts/jared-palmer (May 4 2018)
- **Work in public / radical transparency; speed matters.** Source: https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/

## 3. What Makes It Distinct

- **A named design workflow that is itself a product:** "Generative UI" is not just a method he uses — it is the product (v0). The workflow (describe → generate → select iteration → edit → copy-paste) is documented in his own bylined launch post as the product's core loop. Source: https://vercel.com/blog/announcing-v0-generative-ui
- **Designer-turned-developer with a documented designer-era loop:** the Photoshop → Framer → high-fidelity prototype → hand-to-client-before-build loop is a genuine design workflow from his time as a designer, and he explicitly maps v0 onto it ("it's just the AI version of it"). Source: https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/
- **The "no slop" quality gate as a product rule:** "no random acts of AI, no slop, it had to be pretty good" — a named rejection criterion used to filter whole product directions (docs, chatbots) before building. Source: same.
- **Constraint as a liberating design move:** deliberately shipping markup-only (SIUI) and a single framework (Next.js) as "an important constraint" that enabled the product — the opposite of scope-creep. Sources: Madrona + Latent Space.
- **Model-generation-ahead iteration:** "we are always building a model generation ahead" — the product's design is explicitly re-based when the underlying capability (context length, tool calls) matures, e.g. the one-month rebase from Midjourney-style to chat. Sources: Madrona + Latent Space.
- **Incremental adoption as a design goal:** "I'm all about building tools that can be incrementally adopted" — applied to Turborepo and to v0's copy-paste-into-your-app handoff. Source: https://syntax.fm/show/460/supper-club-turborepo-with-jared-palmer/transcript

## 4. Sources

- Announcing v0: Generative UI (bylined Jared Palmer, Oct 11 2023): https://vercel.com/blog/announcing-v0-generative-ui
- V0's Creator on What's Next for AI Dev Tools — Madrona "Founded & Funded" interview (Jul 23 2025, his own words): https://www.madrona.com/v0-creator-jared-palmer-on-whats-next-for-ai-dev-tools/
- Latent Space: Inside GitHub's AI Revolution — Jared Palmer (Nov 10 2025, his own words): https://podscan.fm/podcasts/latent-space-the-ai-engineer-podcast/episodes/inside-githubs-ai-revolution-jared-palmer-reveals-agent-hq-amp-the-future-of-coding-agents
- Reactiflux Q&A transcript #1 (May 4 2018, his own words): https://reactiflux.js.org/transcripts/jared-palmer
- Reactiflux Q&A transcript #2 (Jan 15 2021, his own words): https://reactiflux.js.org/transcripts/jared-palmer-2
- Syntax #460 Supper Club × Turborepo (May 20 2022, his own words): https://syntax.fm/show/460/supper-club-turborepo-with-jared-palmer/transcript
- Working with Figma and custom design systems in v0 (Vercel-official, iterative approach): https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0
- AI-powered prototyping with design systems (Vercel-official, design-system-as-model-input): https://vercel.com/blog/ai-powered-prototyping-with-design-systems
- Formik: Taming Forms in React (anchor post, Sept 22 2018 — launch story only): https://jaredpalmer.com/blog/formik-taming-forms-in-react
- Formik docs — Resources (doc-currency check; still lists the 2018 post as top talk resource): https://formik.org/docs/resources

---

**Anomalies / dead ends:** (1) The anchor 2018 blog post is confirmed to be a launch/talk announcement only ("Learn Formik, by building it" + talk link) — the body carries no process. (2) SearXNG returned empty results for several queries (Palmer Group design process, Turborepo launch story, Formik 2.0 talk); fell back to `websearch` (Exa) per skill. (3) youtubetranscript.com loads captions via JS and returned no transcript; the React Alicante talk was not transcribed — the talk is "mostly live coding" per its own description, so no process was lost. (4) The "Working with Figma" and "AI-powered prototyping" posts are Vercel-official but not bylined to Palmer — cited as product-level first-party, not as his personal byline. (5) No standalone pre-Formik design portfolio found (matches evidence JSON dead-end note); designer-era process rests on his own Madrona account of the Photoshop/Framer/client loop.
