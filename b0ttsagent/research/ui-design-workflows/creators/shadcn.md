# shadcn (shadcn/ui) — Depth Doc

**Verdict: DEPTH-REJECT** — first-party content is design *principles* and technical docs only; no named, ordered design/build workflow with an explicit quality gate or iteration loop documented by the designer himself.

---

## 1. Eligibility Evidence

- **Scale/award evidence (copied from `working/evidence/shadcn-2026-08-17.json`, not re-verified):** GitHub stars 121,508 (≥20k threshold); npm `shadcn` 6,864,700 downloads/week (≥1M threshold). Date: 2026-08-17 (live fetch). Source: https://api.github.com/repos/shadcn-ui/ui
- **Route + tier:** usage-stat, T1.
- **5-year in-window check:** in-window (project launched Jan 2023; verification window 2021-08-17 → 2026-08-17).
- **Doc-currency check (one line):** ui.shadcn.com/docs is live and current as of 2026-08-17 (Beautiful Defaults, Open Code, Composition, Distribution, AI-Ready present; Vercel "What is shadcn/ui?" guide published 2026-07-07 confirms ongoing currency) — currency is NOT the rejection reason; the rejection is the absence of an ordered first-party process.
- **Product-type tag:** dev tool (open-source React component library / code-distribution platform).
- **Craft/growth tag:** craft-first — but the designer does not document his design process in depth anywhere first-party; his public output is principles + shipped artifacts + product-announcement threads, not process walkthroughs. Tagged craft-first with a documented-process caveat (fails the depth gate).

---

## 2. Step-by-Step Workflow

**Not applicable — DEPTH-REJECT.** No first-party named, ordered design/build workflow with ≥1 explicit quality gate or iteration loop was found. What exists instead:

- **Design principles, not process.** The docs intro page states five principles — Open Code, Composition, Distribution, Beautiful Defaults, AI-Ready — each described as a property of the system ("carefully chosen default styles… designed to look good on their own and to work well together"), not as an ordered sequence of steps a designer executes. Source: https://ui.shadcn.com/docs
- **Theming/token system, not a design workflow.** The theming docs describe the semantic token convention (background/foreground pairs, radius scale, base colors, CSS-variable theming) and how to add tokens — a specification of the system's structure, not a step-by-step design process with gates. Source: https://ui.shadcn.com/docs/theming
- **Distribution schema, not a design workflow.** The registry docs define the flat-file schema and CLI for distributing components — an engineering/distribution mechanism. Source: https://ui.shadcn.com/docs/registry
- **Product-announcement X threads, not process.** His threads announce shadcn/create (defaults + 5 visual styles), the registry MCP, and chat components — they state goals ("give you solid defaults… let you take it from there") but do not walk through a named ordered design/build method with a quality gate. Sources: https://threadreaderapp.com/thread/1999530406744293593.html ; https://threadreaderapp.com/thread/1917597228513853603.html ; https://threadreaderapp.com/thread/2070561306038653247.html
- **No talks or in-depth first-party interviews surfaced.** Searches for his talks (Vercel Ship, Next.js Conf, React Summit) and interviews where HE describes his process returned no first-party process content. The closest items are secondhand (e.g., Theo's "How Shadcn/ui ACTUALLY Works" video, RedMonk's "Revenge of Copypasta") — explicitly excluded as anchor sources by the depth gate.

**Conclusion:** The material is principles + system specification + shipped artifacts. There is no extractable named, ordered workflow with an explicit quality gate or iteration loop documented by shadcn himself. Per the wave-07 depth gate ("if it's only principles without ordered process → DEPTH-REJECT with reason"), this fails.

---

## 3. What Makes It Distinct

Not applicable (DEPTH-REJECT). For completeness, the non-generic signature elements of the *system* (not a documented process) are: copy-paste/CLI distribution instead of npm packages; open code owned by the consumer; semantic CSS-variable tokens; CVA variant system; composable headless primitives (Radix/Base UI); and an AI-ready registry schema. These are system properties documented in the docs, not steps in a designer-authored workflow.

---

## 4. Sources

First-party (all read):
- https://ui.shadcn.com/docs — design principles (Open Code, Composition, Distribution, Beautiful Defaults, AI-Ready)
- https://ui.shadcn.com/docs/theming — token convention, radius scale, base colors, CSS-variable theming
- https://ui.shadcn.com/docs/registry — registry schema + CLI distribution
- https://shadcn.com — personal site (bio, newsletter, product links; no blog/talks)
- https://threadreaderapp.com/thread/1999530406744293593.html — shadcn/create announcement thread (defaults + 5 visual styles)
- https://threadreaderapp.com/thread/1917597228513853603.html — registry MCP thread
- https://threadreaderapp.com/thread/2070561306038653247.html — chat components thread
- https://vercel.com/i/what-is-shadcn — Vercel's official "What is shadcn/ui?" guide (2026-07-07; currency confirmation, not process)

Supplementary (secondhand, NOT used as anchor):
- https://www.youtube.com/watch?v=AqmMx_JidGo — Theo's "How Shadcn/ui ACTUALLY Works" (third-party analysis)
- https://redmonk.com/kholterhoff/2025/04/22/ui-component-libraries-shadcn-ui-and-the-revenge-of-copypasta/ — RedMonk analysis
- https://vercel.com/academy/shadcn-ui/extending-shadcn-ui-with-custom-components — Vercel Academy lesson (Vercel's educational content, not shadcn's own process documentation)

---

## Research notes / dead ends

- SearXNG returned empty for shadcn process queries; fell back to Exa (`websearch`) per skill routing.
- Searched: "how I build components" talk, Vercel Ship / Next.js Conf / React Summit talks, podcast interviews where he describes his process, X threads on design process — none yielded first-party ordered-process content.
- The Vercel Academy "extending shadcn/ui" lesson is a step-by-step component-build guide but is Vercel-authored educational content, not the designer's own documented process; excluded as anchor per the depth gate.
