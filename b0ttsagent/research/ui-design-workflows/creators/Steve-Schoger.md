# Steve Schoger — Depth Doc

Research date: 2026-08-17 · Wave (Phase 2, depth docs) · Researcher 1

## 1. Eligibility Evidence

- **Scale (route: usage-stat, tier T1):** GitHub **23,748 stars** (tailwindlabs/heroicons, fetched 2026-08-17); npm **2,704,587 downloads/week** for @heroicons/react (2026-08-09 → 2026-08-15). Source: https://api.github.com/repos/tailwindlabs/heroicons. *(Copied from `working/evidence/steve-schoger-2026-08-17.json`; scale not re-verified per wave spec.)*
- **5-year window:** in-window (2021-08-17 → 2026-08-17).
- **Doc currency (one line):** First-party site steveschoger.com is live and still referenced as his current personal site in recent content (YesPress profile 2025–26, tokyn credits appendix); Refactoring UI still sold (2026 copyright, refactoringui.com); he announced a Refactoring UI YouTube channel reboot in 2025 (X post) — workflow confirmably current.
- **Product-type tag:** dev tool / design resource (Heroicons icon library; Tailwind UI component library; Refactoring UI book + video course for developers).
- **Craft/growth tag:** craft-first — Schoger documents his design process in depth (the Refactoring UI book, the video walkthrough series, conference talks, and X design-tip threads), so the craft tag applies.

## 2. Step-by-Step Workflow

Schoger's named, ordered workflow is the Refactoring UI book's chapter sequence (co-authored with Adam Wathan — joint first-party content, credit both), applied live in his YouTube redesign series and conference talks. The book supplies the ordered process (A); the videos supply the applied iteration loop with named per-episode steps (B); the X threads supply per-step micro-tactics linked to specific posts (C). All steps are first-party.

### A. The ordered process — Refactoring UI book (Wathan & Schoger)

The book's table of contents is itself the workflow, in order:

1. **Starting from Scratch.** (a) *Start with a feature, not a layout* — don't design the shell first; start with one piece of real functionality. (b) *Detail comes later* — hold the color, design in grayscale so spacing/contrast/size do the work, add detail after. (c) *Don't design too much* — work in short cycles: design a simple version, make it real, iterate on the working design until no problems remain, then jump back into design mode for the next feature (explicit iteration loop). (d) *Choose a personality* — pick font, color, border radius, language deliberately and stay consistent. (e) *Limit your choices* — define systems (shades per color, a restrictive type scale) so each decision is made once. Source: https://www.refactoringui.com/
2. **Hierarchy is Everything.** Not all elements are equal; size isn't everything (use weight/color); don't use grey text on colored backgrounds; de-emphasize to emphasize; labels are a last resort; separate visual from document hierarchy; balance weight and contrast; semantics are secondary. Source: same.
3. **Layout and Spacing.** Start with too much white space; establish a spacing and sizing system; you don't have to fill the whole screen; grids are overrated; relative sizing doesn't scale; avoid ambiguous spacing. Source: same.
4. **Designing Text.** Establish a type scale; use good fonts; keep line length in check; baseline, not center; line-height is proportional; not every link needs a color; align with readability in mind; use letter-spacing effectively. Source: same.
5. **Working with Color.** Ditch hex for HSL; you need more colors than you think; define your shades up front; don't let lightness kill your saturation; greys don't have to be grey; accessible doesn't have to mean ugly; don't rely on color alone. Source: same.
6. **Creating Depth.** Emulate a light source; use shadows to convey elevation; shadows can have two parts; even flat designs can have depth; overlap elements to create layers. Source: same.
7. **Working with Images.** Use good photos; text needs consistent contrast; everything has an intended size; beware user-uploaded content. Source: same.
8. **Finishing Touches.** Supercharge the defaults; add color with accent borders; decorate your backgrounds; don't overlook empty states; use fewer borders; think outside the box. Source: same.
9. **Leveling Up.** The closing chapter — treat the whole sequence as a repeatable skill to keep raising. Source: same.

The book ships three applied video tutorials that walk the process end-to-end on common scenarios: *Designing a complex form interface* (11:13), *Building a data-focused dashboard* (17:20), *Styling a text-focused landing page* (12:08). Source: https://www.refactoringui.com/

### B. The applied iteration loop — Refactoring UI YouTube series (2018–2019)

Each episode takes a real, submitted app page and refactors it in Sketch with named, ordered steps (the "before → after" structure is the quality gate: the redesign must beat the original on scannability/hierarchy). Episode step sequences (from each video's own chapter/key-moment list):

- **Bad About topic page** (Apr 2018) — "organizing content, creating a hierarchy, and improving typography." Source: https://www.youtube.com/watch?v=S6-q5BheEYU
- **WP Pusher checkout page** (Mar 2018) — "designing forms, finding layout inspiration, and making bland design more exciting." Source: https://www.youtube.com/watch?v=5gdYHlYAKDY
- **Resolute properties page** (2018) — forms, scannability, reskinning. Source: https://www.youtube.com/watch?v=BMHUKij1yUE
- **WSS plan details page** (May 2018) — named steps: Scroll Jacking → Background Campus Photos → The Hierarchy → Update the Icons → Top Navigation → Plan Details → Font → Geometric Shapes → Table View → Horizontal Scrolling. Source: https://www.youtube.com/watch?v=ZJj7uNdzPpM
- **Tuple hype page** (Jun 2018) — named steps: Headline placement → Inverted text → Headline → Font Stack → Background Color → Color Picker → Text Styling → Drop Caps → Background Colors → Main Features → Description Text → Icons → FAQ. Source: https://www.youtube.com/watch?v=RC9cYdbQ-_c
- **Transistor integration page** (Aug 2019) — "lots of tips on layout and form design." Source: https://www.youtube.com/watch?v=ZT4WRRhacWk · announced on X: https://x.com/steveschoger/status/1162048820957630465

The talk "The Little Details of UI Design" (Laracon Online Winter 2018) is the same method as a systematic walkthrough with named steps: The Header → Add a bit of color to your greys → Use a consistent corner radius → Use a consistent icon set → Use font size to emphasize important information → Use color to create hierarchy → Use a consistent spacing scale → Use color to draw attention → Saturate greys when using a colored background → Offset box-shadows → Easy on the link styles → Use contrast to create balance → Pick an appropriate line height → Use alignment to clean up your design → Give actions hierarchy → Consider space instead of borders → Use color to create depth and hierarchy → Finishing touches → Use good fonts. Source: https://www.youtube.com/watch?v=EjEYTRD-W-M

The CSS Day 2019 talk ("Refactoring UI") is the same process with the book's chapter names as the agenda: Give text consistent contrast → Don't use grey text on colored backgrounds → Use perceived brightness → Start with too much whitespace → Balance weight and contrast → Supercharge the defaults → Overlap elements to create depth. Source: https://www.youtube.com/watch?v=7Z9rrryIOC4

**Quality gate / iteration loop (explicit):** the book's "Don't design too much → work in cycles" loop (design simple → make real → iterate until no problems remain → next feature) is the named iteration loop; the "Finishing Touches / Supercharge the defaults" pass is the named quality gate that closes each cycle. Both are first-party (book TOC + CSS Day agenda). The series itself is an open iteration loop — he solicits real sites to redesign and announced a channel reboot in 2025, "starting to collect some examples to redesign." Source: https://x.com/steveschoger/status/1897373865220956292

### C. X design-tip threads mapped to the workflow (per-post links)

His "Little UI Details" X threads are the per-step micro-tactics that feed the book's phases (listicle-grade alone, so used here only to link each step to the specific post; quotes as documented by digitalsynopsis.com, which links each to the original tweet):

- **Hierarchy:** "Use font color/weight for emphasis" — https://twitter.com/steveschoger/status/910162010754748416 · "Uniformity in text of different sizes" — https://twitter.com/steveschoger/status/979055525060055040
- **Color:** "Saturate your greys" — https://twitter.com/steveschoger/status/975796307196604417 · "Saturated text on colored backgrounds" — https://twitter.com/steveschoger/status/874333097168314370 · "Vibrant gradients (shift hue 10–20°)" — https://twitter.com/steveschoger/status/879365654238941184
- **Depth:** "Offset your box shadows" — https://twitter.com/steveschoger/status/877209916179709955 · "Overlapping elements create depth" — https://twitter.com/steveschoger/status/892077100705996801 · "Overlapping images with matching border" — https://twitter.com/steveschoger/status/981606881255976961
- **Text:** "16px font, 1.5 line height" — https://twitter.com/steveschoger/status/870328030270500864 · "Tighten line-height as text grows" — https://twitter.com/steveschoger/status/968519052800024577 · "Letter-spacing in all-caps" — https://twitter.com/steveschoger/status/869932734466195456 · "Aligning text cleans up design" — https://twitter.com/steveschoger/status/875427320147972098
- **Layout/spacing:** "Multiples to define spacing" — https://twitter.com/steveschoger/status/885514519182802944 · "Two-column form layout" — https://twitter.com/steveschoger/status/905830324139155458 · "Keylines connect content" — https://twitter.com/steveschoger/status/882621941684850688
- **Finishing touches:** "Use fewer borders" — https://twitter.com/steveschoger/status/897849211110273024 · "Color on top (4–6px accent)" — https://twitter.com/steveschoger/status/872114194816126977 · "Subtle CTA for negative links" — https://twitter.com/steveschoger/status/892808889535737868 · "Contrast vs keyline on panels" — https://twitter.com/steveschoger/status/871757453033132034 · "Checkmarks vs bullets" — https://twitter.com/steveschoger/status/872478203016826880
- **Components:** "Styling icons (shape behind small icons)" — https://twitter.com/steveschoger/status/931198630333165568 · "Light icons for inactive states" — https://twitter.com/steveschoger/status/872865304719892480 · "Input form styling" — https://twitter.com/steveschoger/status/920706913624625152 · "Designing tables" — https://twitter.com/steveschoger/status/913062604540653568 · "Dropdowns as boxes" — https://twitter.com/steveschoger/status/953297226985549825 · "Think outside the database" — https://twitter.com/steveschoger/status/997125312411570176 · "Hero banners (desaturated photo + multiply)" — https://twitter.com/steveschoger/status/888021897782362114 · "Make your own map" — https://twitter.com/steveschoger/status/882949496388321284

The co-authored Medium article "7 Practical Tips for Cheating at Design" (Feb 2018) is the same tactic set in article form (hierarchy via color/weight, no grey on color, offset shadows, fewer borders, don't blow up small icons, accent borders, button hierarchy). Source: https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886

## 3. What Makes It Distinct

- **"Design with tactics, not talent."** The entire brand is that design is learnable tactics for developers, not artistic talent — which is why his workflow is unusually concrete and executable (the book's own framing). Source: https://www.refactoringui.com/
- **The book's chapter sequence IS the workflow.** Unlike most design content, the ordered process is literally the book's table of contents (Start with a feature → Hierarchy → Layout → Text → Color → Depth → Images → Finishing Touches → Leveling Up), and his talks reuse the same chapter names as their agendas — the process is stable and named. Source: https://www.refactoringui.com/ · https://www.youtube.com/watch?v=7Z9rrryIOC4
- **Redesign-as-teaching.** His signature format is refactoring a real, submitted app page live in Sketch with a before/after quality gate — the "Refactoring UI" series (Bad About, WP Pusher, Resolute, WSS, Tuple, Transistor) — rather than designing from a blank canvas. Source: https://www.youtube.com/@SteveSchoger
- **"Supercharge the defaults" as a named finishing gate.** A closing pass that upgrades browser defaults (borders, shadows, spacing) — his distinctive final step in both the book and the CSS Day talk. Source: https://www.refactoringui.com/ · https://www.youtube.com/watch?v=7Z9rrryIOC4
- **Micro-tactic density with before/after mockups.** His X threads pair one tactic with a before/after image (e.g., "saturate your greys", "offset your shadows"), making each step self-contained and immediately testable. Source: https://twitter.com/i/moments/994601867987619840
- **Developer-tooling tie-in.** The workflow is inseparable from his own products — Heroicons, Zondicons, Hero Patterns, and the Refactoring UI component gallery/color palettes/font suggestions — so the process ships with its own assets. Source: https://www.steveschoger.com/ · https://www.refactoringui.com/

## 4. Sources

- Refactoring UI — book + site (Wathan & Schoger; full TOC = the ordered process): https://www.refactoringui.com/ · https://www.refactoringui.com/book
- Steve Schoger — personal site + book page: https://www.steveschoger.com/ · https://www.steveschoger.com/book/
- Refactoring UI YouTube series (channel): https://www.youtube.com/@SteveSchoger
  - Bad About: https://www.youtube.com/watch?v=S6-q5BheEYU
  - WP Pusher Checkout: https://www.youtube.com/watch?v=5gdYHlYAKDY
  - Resolute: https://www.youtube.com/watch?v=BMHUKij1yUE
  - WSS: https://www.youtube.com/watch?v=ZJj7uNdzPpM
  - Tuple: https://www.youtube.com/watch?v=RC9cYdbQ-_c
  - Transistor: https://www.youtube.com/watch?v=ZT4WRRhacWk
- Talks: The Little Details of UI Design (Laracon Online Winter 2018): https://www.youtube.com/watch?v=EjEYTRD-W-M · Refactoring UI (CSS Day 2019): https://www.youtube.com/watch?v=7Z9rrryIOC4 · How to Think Like a Visual Designer (StreamACon): https://www.youtube.com/watch?v=hlI6xGfBjkQ
- 7 Practical Tips for Cheating at Design (Feb 2018, Wathan & Schoger): https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886
- X / Twitter: profile https://x.com/steveschoger · Little UI Details moment: https://twitter.com/i/moments/994601867987619840 · Transistor episode post: https://x.com/steveschoger/status/1162048820957630465 · channel-reboot post: https://x.com/steveschoger/status/1897373865220956292 · individual tip posts linked in Section 2C
- Heroicons (scale anchor): https://github.com/tailwindlabs/heroicons · https://www.npmjs.com/package/@heroicons/react

---

**Anomalies / dead ends:** (1) X.com and the Twitter moments are bot-blocked — individual tip-post quotes were verified via digitalsynopsis.com (secondary), which quotes each tweet and links to the original first-party post URL; the post URLs themselves are first-party. (2) YouTube pages don't render via direct fetch; video titles, descriptions, and chapter/key-moment lists were read via the r.jina.ai reader proxy (first-party page content). (3) Transcript services (youtubetranscript.com, tactiq, notegpt, youtube-transcript.io, timedtext API) all failed (JS-gated / 403 / 429); chapter lists were used as the named-step evidence instead. (4) The "Redesigning Laravel.io" Medium case study is 403-blocked; only its existence and topic were confirmed (freek.dev link post). (5) Refactoring UI book chapter text is paywalled; the TOC (which is the ordered process) was read in full from refactoringui.com.
