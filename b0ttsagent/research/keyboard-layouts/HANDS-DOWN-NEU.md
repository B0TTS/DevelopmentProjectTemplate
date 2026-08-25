# Hands Down Neu — Deep Research: Community Experience for a Developer

**Research date:** 2026-08-18
**Scope:** Hands Down Neu (the entry-point variant of the Hands Down family by R. Alan Reiser, hosted at alanreiser.com/handsdown). Focus: real community experience (learning curve, time-to-results, comfort, coding fit, failure modes), not just design rationale.
**Audience:** a typical developer (mixed general English typing + programming).

---

## 0. Executive summary (read this first)

- **What it is:** Hands Down Neu is the "base" variant of the Hands Down family — a fully-optimized, high-alternation + high-inward-roll English layout with very low same-finger bigrams (SFB ~0.95%), designed to work on **any keyboard** (row-stagger slab, ortholinear, or split ergo). It is the officially recommended entry point and the basis for the "precious metals" (Gold/Silver/Bronze) and "hard metals" (Titanium/Rhodium/Vibranium) thumb-alpha variants. Released early summer 2021. (Evidence: official site, layouts.wiki.)
- **The honest headline for a developer:** Hands Down Neu is a real, well-engineered layout with genuinely excellent comfort stats, but **community experience data is sparse and heavily confounded** — most Hands Down users pair it (or its siblings) with split/columnar ergo keyboards, home-row mods, layers, combos, and adaptive keys. Neu itself is explicitly designed to *not* require any of that, but the ecosystem around it assumes it. For coding specifically, the main friction points reported are: non-standard symbol placement, `j`/`z` living in extra columns (awkward on small boards and for vim), and the fact that most of the "smart keyboard" features that make Hands Down shine (adaptive keys, combos) are rarely actually implemented by users.
- **Time to results:** For Neu specifically, only ~2–3 usable individual data points exist. Range: "mid-20s WPM while still early" to "101 WPM after ~2 months of full-time use." Central estimate: **~1–2 months to reach respectable (60–100 WPM) speeds with disciplined daily practice**, consistent with the designer's own claims and the general alt-layout literature (2–6 months to recover prior QWERTY speed). Sample size is tiny and non-representative — treat as anecdote, not data.
- **Does it work for everyone?** No. Documented failure/abandonment modes: (a) vim users who can't tolerate `j`/`k`/`u` positions; (b) small-keyboard (≤34 key) users who can't fit Neu's extra columns; (c) people who don't want to learn combos/adaptive keys and find the "smart keyboard" complexity a dealbreaker; (d) people who just want a drop-in layout with OS support and pick Colemak-DH instead; (e) people switching for speed (it won't make you faster than a trained QWERTY typist).

---

## 1. What it is

### 1.1 Origin of the Hands Down family and Neu

- Hands Down was created by **R. Alan Reiser** starting ~2020 (first layout "Notarise", then Hands Down Reference, Alt, Élan, then Neu). The official site states: "Design of Neu began shortly after Élan in late 2020... Neu was released in early summer of 2021, leveraging a lot of the work that went into Élan and Polyglot, and ultimately succeeded them in the design lineage, with Gold/Silver/Bronze designed alongside as a part of the suite." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home — read)
- Reiser's stated motivation: after trying ASSET, Norman, Workman, Colemak-DH, Dvorak, he found them over-burdening the index fingers / center column, or too high in same-finger bigrams, and he needed a layout that also worked for Japanese (K is the 2nd most frequent consonant in Japanese). (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/faq — read)
- The family is large: Reference, Alt, Élan, Neu, Gold, Silver, Bronze, Platinum, Titanium, Rhodium, Vibranium, Promethium, plus "Hands On" (a transitional layout) and the in-progress "Polyglot". Reiser now says: "After feedback from many Hands Down users I'm now actively recommending only the Hands Down Neu variations." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home — read)

### 1.2 Neu's design goals

- **Works on any keyboard.** "Hands Down Neu is the place to start if you're new to ultra-high efficiency alt layouts... Neu works on any keyboard, so it is recommended if you are using a standard row-stagger slab keyboard, or a split ergo and you prefer to have modifiers (esp. shift) on a thumb." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu — read)
- **Thumb-modifier friendly.** "Hands Down Neu is recommended for those using traditional ansi/iso/jis keyboards, or who prefer thumb shift or other layer functions on the thumb instead of home-row mods." (Evidence: same page — read)
- **Ultra-high efficiency.** Neu's stated stats: **0.949% SFBs** (cf. QWERTY 6.6%, Dvorak 2.6%, Colemak 1.5%, MTGAP 1.2%), very high alternation, ~3:1 inward:outward roll ratio, graduated finger burden (pinky→index), and obsessive attention to the 22-key "Home Block." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu — read)
- **Standalone.** "Neu is great on its own, without any need for other 'Smart Keyboard' features (combos, Adaptive Keys, etc.), though they can certainly be deployed on Neu with great results." (Evidence: same page — read)

### 1.3 Where Neu sits vs other Hands Down variants

- Neu is the **base, all-alphas-in-the-finger-field** layout. The metals variants (Gold/Silver/Bronze/Titanium/Rhodium/Vibranium) are Neu-based but **require a dedicated thumb key for an alpha** (T, N, H, or R) — i.e., they need a split ergo with thumb clusters. "Hands Down Neu is the basis for the precious metals variations (Gold/Silver/Bronze) and the hard metals variations (Titanium/Rhodium/Vibranium), but these variations require a dedicated thumb key for an alpha character (T/N/H or R)." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu — read)
- Reiser's own guidance: choose Neu if you want all characters in the finger field, your thumbs are busy with layers/shift, you like a wide spacebar, or you can't wrap your head around typing a letter with a thumb. (Evidence: https://sites.google.com/alanreiser.com/handsdown/home — read)
- Independent third-party (layouts.wiki) recommendation: "For row-staggered boards, the current recommended Hands Down layout is Hands Down Neu. For split keyboards, [the AKL community] starting with Promethium." (Evidence: https://layouts.wiki/guides/start/recommendations/ — read)

### 1.4 Neu vs Colemak / Colemak-DH on the efficiency spectrum

- **Official claim:** Neu's SFB 0.949% vs Colemak 1.5% (per Reiser's own analyzer figures). Neu is an **alternating** layout (like Dvorak) with high rolling, whereas Colemak is a **same-hand roll** layout. Reiser: "While Hands Down does have some similarity to Dvorak (both are alternating layouts), it is quite different and has notably better stats in nearly all areas." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/faq — read)
- **Independent metric (Pascal Getreuer's table, KLA-based):** Hands Down Neu (2021): SFB 0.76%, scissors 1.26%, lateral stretch 0.42%, rolls 44.04%, redirects 1.48%, same-hand 2.89%. For comparison, Colemak-DH is in the same ballpark on SFB but with different tradeoffs. (Evidence: https://getreuer.info/posts/keyboards/alt-layouts/index.html — read)
- **Independent critique (layouts.wiki):** Neu "performs worse on three of AKL's preferred metrics: SFBs, scissors, and weak redirects" vs the AKL-recommended layouts (Gallium/Graphite etc.), though "the difference is small in absolute terms." Specifics: Neu has a "very bad PL scissor, as in 'play'" (0.23% of bigrams), and weak redirects like "hey" and "like." The wiki also notes the author suggests adaptive keys to fix these, "though in practice, most people do not end up implementing them." (Evidence: https://layouts.wiki/guides/start/recommendations/ — read)
- **keyboard-design.com (Ian Douglas) ranking:** Neu variants rank near the top of the site's "best layouts" lists for ANSI (e.g., hands-down-neu-sym.eu.ansi at #2, hands-down-neu-angle.ts.eu.ansi at #3 in the April 2024 list). (Evidence: https://keyboard-design.com/best-layouts.html — read)
- **Bottom line:** On paper Neu is a top-tier layout, arguably a step above Colemak-DH on SFB/rolling metrics, but the differences between top layouts are small and the choice is about which weaknesses you prefer. Colemak-DH's big practical advantages are: built-in OS support, keeps ZXCV shortcuts, huge community, and it's the default recommendation for split boards.

---

## 2. Short-term experience (first days/weeks)

**Data is sparse for Neu specifically.** What exists:

- **The one documented Neu speed case (molohov, YouTube "Hands Down Neu @ 101WPM", 2021):** video description states: "It's taken a lot longer to get my speed up with Hands Down than with Colemak. I've been training and using the layout full time for almost 2 months now (started on 8/11/2021). Still, I'm very..." (Evidence: video description surfaced via search; title/author confirmed via YouTube oEmbed https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=0mL5tM_fhzI — read). This is the single most-cited individual data point; the official FAQ links to it as proof that "some people have achieved very respectable speeds with modest training (a month or two)." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/faq — read)
- **A Reddit user early in the process (r/KeyboardLayouts, Oct 2022):** "I went from Neu to Rhodium recently. Thumb R is excellent. Still in mid-20's WPM but v.comfy." (Evidence: https://www.reddit.com/r/KeyboardLayouts/comments/y7jkyj/the_hands_down_ive_been_using_lately/ — snippet only; Reddit blocked full read). This shows the early phase is genuinely slow (mid-20s WPM) even for someone already experienced with Neu.
- **Designer's self-report (not Neu-specific, self-disclosed):** "In barely 10 weeks, I designed Hands Down from scratch, and adopted it as my primary layout... I have recovered almost 50% of my typing speed." Also: "I've been able to 'feel' comfortable in Hands Down more quickly than I did trying out Colemak-DH and even QWERTY derivatives such as ASSET/Norman/Workman." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/faq — read). Treat as biased (he designed it) but it's the only "first weeks" narrative on the official site.
- **General alt-layout short-term experience (transferable context):** "The first couple weeks are the hardest since your typing will be frustratingly slow" (Pascal Getreuer, who has switched layouts half a dozen times). (Evidence: https://getreuer.info/posts/keyboards/alt-layouts/index.html — read). A 2026 Graphite learner: "my very first weeks were more like 30 wpm." (Evidence: https://www.joa-ebert.com/posts/2026-04-30-learning-to-type/ — read). A 2026 Colemak/Workman/Norman tester: "15 WPM on Colemak after my first day. Brutal. At two weeks I was at 35 WPM." (Evidence: https://typingfastest.com/blog/qwerty-alternatives-best-keyboard-layouts-that-actually-stick-2026 — read; estimate-grade blog).

**Inference (flagged as inference, not evidence):** Neu is a *fully* different layout from QWERTY (unlike Colemak which keeps ~17 keys in place), so the first days/weeks are likely at the harder end of the alt-layout spectrum — expect single-digit-to-30 WPM and constant muscle-memory fighting. No Neu-specific "first week" report was found to confirm this directly.

---

## 3. Mid-term experience (first ~1–6 months)

- **molohov:** reached **101 WPM at ~2 months** of full-time use + training on Neu, though he explicitly said it took longer than Colemak had. (Evidence: YouTube description + official FAQ link — see §2.)
- **Designer's general claim:** "Some people seem to be able to recover their former typing speed on a new layout in just a month or two after switching completely and sticking to a disciplined training program." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/faq — read; self-disclosed, no sample given.)
- **Kristoffer Grönlund (developer, learned Hands Down Reference — the predecessor, not Neu):** "I worked on learning this layout and got to decent speeds for english text, and was even able to use it for programming without too many issues." No WPM numbers given. (Evidence: https://write.as/oferlund/designing-a-keyboard-layout-part-2 — read)
- **General alt-layout mid-term (transferable):** Getreuer: "40 wpm after the first month, 50 wpm after the second month, and 80 wpm after the first year." (Evidence: https://getreuer.info/posts/keyboards/alt-layouts/index.html — read). Joa Ebert (Graphite): "In the first three months I achieved a consistent 60 wpm... Then I made a good jump to 90 wpm." (Evidence: https://www.joa-ebert.com/posts/2026-04-30-learning-to-type/ — read). TypingFastest: "At 90 days, 72 WPM — almost back to my QWERTY baseline. By the six-month mark... 82-85 WPM." (Evidence: https://typingfastest.com/blog/qwerty-alternatives-best-keyboard-layouts-that-actually-stick-2026 — read; estimate-grade.)

**Inference:** For Neu specifically, the mid-term picture is "comfort clicks well before speed does" — the y7jkyj user was "v.comfy" at mid-20s WPM, and the designer emphasizes long-duration comfort (~80 WPM sustained) over burst speed. Expect usable-but-slower-than-QWERTY for the first 1–3 months, with speed recovery typically landing in the 2–6 month window.

---

## 4. Long-term experience (6+ months)

- **Designer (self-disclosed, 2+ years in):** "I'm still using Hands Down exclusively (Rhodium, a.k.a. Neu-rx+), and really couldn't be happier. I have been super busy writing all sorts of academic papers, tens of pages per day... I don't aspire to being a competitively fast typist, so all my design decisions are made for long duration comfort typing (~80wpm sustained for long periods of time)." (Evidence: https://sites.google.com/alanreiser.com/handsdown/home/design-notes — read)
- **A developer who stayed with the family but moved off Neu:** Kristoffer Grönlund learned Hands Down Reference, then designed his own layout (kheia) heavily influenced by Neu. He did NOT stick with Neu itself — his stated reason: Neu's extra columns (j, z) don't fit his 34-key Ferris Sweep, and j is heavily used in vim. He also had a vim-specific annoyance on Reference (u under right index = accidental undo). (Evidence: https://write.as/oferlund/designing-a-keyboard-layout-part-2 and https://write.as/oferlund/designing-a-keyboard-layout — read)
- **A layout designer who tried Neu and moved on:** empressabyss (author of the Nordrassil layout): "Of the layouts I've learned (Qwerty, Dvorak, Hands Down Neu (kinda), two iterations of Just Rhea...), Nordrassil is by far my favourite." (Evidence: https://github.com/empressabyss/nordrassil — read). This is a "tried Neu, preferred something else" data point.
- **No long-term WPM-ceiling data for Neu specifically was found.** No "I've been on Neu for 2+ years and here's my sustained WPM" community report exists in the indexed sources. UNKNOWN.
- **General alt-layout long-term (transferable):** Getreuer: "80 wpm after the first year." (Evidence: https://getreuer.info/posts/keyboards/alt-layouts/index.html — read). Jonas Hietala (custom layout): "I'm not close to my old QWERTY speed of +120 wpm simply because I got bored of practicing typing" — a candid admission that even a dedicated developer may never regain peak QWERTY speed. (Evidence: https://www.jonashietala.se/blog/2023/11/02/i_designed_my_own_keyboard_layout_was_it_worth_it/ — read)

---

## 5. Pros and cons (especially for coding)

### Pros (evidence-backed)

1. **Genuinely excellent comfort stats.** Very low SFBs (~0.95%), high alternation, ~3:1 in:out rolls, balanced hand/finger load. Independent analyzers confirm it's a top-tier layout. (Evidence: official site; getreuer.info; keyboard-design.com best-layouts list — all read)
2. **Works on any keyboard.** Neu is the rare "fully optimized" layout that doesn't require a split ergo or thumb keys. (Evidence: official site — read)
3. **Standalone — no smart-keyboard features required.** Combos/adaptive keys are optional. (Evidence: official site — read)
4. **Family coherence.** If you later want a thumb-alpha variant (Gold/Vibranium etc.), "you can do so without too much retraining." (Evidence: official site — read)
5. **Designer is responsive and the docs are unusually deep** (design notes, statistics, FAQ, per-variation rationale). (Evidence: official site — read)
6. **Independent-ish endorsement:** Jonas Hietala (developer who designed his own layout): "In the vast majority of cases it would be good enough to switch to something like Colemak-DH or Hands Down." (Evidence: https://www.jonashietala.se/blog/2023/11/02/i_designed_my_own_keyboard_layout_was_it_worth_it/ — read)

### Cons (evidence-backed)

1. **Non-standard symbol placement.** "Hands Down Neu is based on a total rethinking of a keyboard layout (many things are non-standard, including some shift states)." For a developer this means `;`, `'`, `"`, `/`, `-`, `,`, `.` are all relocated, and shift-pairs are non-standard. (Evidence: official site — read). This is the classic coding pain point for any non-Colemak alt layout; no Neu-specific "symbols were fine" report was found.
2. **`j` and `z` live in extra columns** (right of the standard 30-key grid). This is a real problem for (a) small/split boards without those columns and (b) vim users, since `j` is a primary navigation key. Grönlund: "This made neu a non-starter for me, especially considering that j in particular gets heavy use while coding in vim." (Evidence: https://write.as/oferlund/designing-a-keyboard-layout-part-2 — read)
3. **Vim friction generally.** Getreuer's guide (general alt-layout guidance, applies to Neu): alt layouts optimized for English put j/k in awkward spots for vim; solutions are a nav layer or remapping. Neu's j is in an extra column, which is worse than most. (Evidence: https://getreuer.info/posts/keyboards/alt-layouts/index.html — read)
4. **Independent critique: PL scissor + weak redirects.** layouts.wiki: "Neu has the very bad PL scissor, as in 'play'"; weak redirects like "hey"/"like"; and the suggested adaptive-key fixes "in practice, most people do not end up implementing." (Evidence: https://layouts.wiki/guides/start/recommendations/ — read)
5. **The "smart keyboard" complexity is a real adoption barrier.** Xah Lee (skeptical critic): "The Hands Down layouts seem silly and unprofessional... it requires you to type 2 keys together to input some letters [combos]... requires advanced keyboard firmware, such as QMK... requires a keyboard with 2 to 4 thumb keys." (Evidence: http://xahlee.info/kbd/hands_down_layout.html — read). Note: Xah's critique is aimed at the *family* (thumb-alpha variants + combos), and Neu specifically does NOT require thumb keys or combos — but the critique captures the perception problem and the ecosystem's complexity.
6. **No native OS support.** Neu is not built into Windows/macOS/Linux. You need a third-party remapper (Kanata, Karabiner, MSKLC, kmonad) or a programmable keyboard. (Evidence: layouts.wiki install page — read; official download page — read)
7. **Tiny community / few tools.** Compared to Colemak-DH, the Hands Down community is small ("adopted by dozens of other happy typists" per the designer). (Evidence: https://sites.google.com/alanreiser.com/handsdown/home — read)

### Split ergo + layers: requirement or optional?

- **For Neu: optional.** Neu is explicitly designed to work on a standard row-stagger slab keyboard with no layers/mods. (Evidence: official site — read)
- **In practice: heavily associated.** The designer's own implementations, the QMK/ZMK repos, and most community discussion assume split ergo boards with layers, home-row mods, combos, and adaptive keys. The metals variants (Gold/Vibranium/etc.) *require* thumb keys. So "Hands Down" as a brand is entangled with the split-ergo + layers ecosystem, even though Neu itself is not. (Evidence: official download page, moutis/HandsDown, neonfuzz/HandsDown, zeitlinger/keyboard GitHub repos — read)
- **Confound caveat (this is itself a finding):** Most Hands Down experience reports are confounded with "also switched to a split/columnar ergo keyboard + layers + home-row mods at the same time." When people report comfort gains, you cannot cleanly attribute them to the layout vs the hardware. This is the single most important caveat for interpreting any Hands Down experience claim.

---

## 6. Time to positive results — individual data points

### Neu-specific data points (n = 3 usable)

| # | Person / source | Data point | Notes |
|---|---|---|---|
| 1 | molohov (YouTube "Hands Down Neu @ 101WPM", 2021) | **101 WPM after ~2 months** of full-time use + training; said it took longer than Colemak | Best-documented Neu case; linked from official FAQ as the speed proof. Source: https://www.youtube.com/watch?v=0mL5tM_fhzI (description via search; title/author via oEmbed) |
| 2 | r/KeyboardLayouts user (y7jkyj, Oct 2022) | **mid-20s WPM** while "v.comfy", after switching Neu→Rhodium | Early-stage; shows comfort precedes speed. Source: https://www.reddit.com/r/KeyboardLayouts/comments/y7jkyj/ (snippet only) |
| 3 | R. Alan Reiser (designer, self-disclosed) | **~50% speed recovery in 10 weeks** (on the family, not Neu specifically); claims "a month or two" to recover former speed for disciplined switchers | Designer bias; no sample. Source: https://sites.google.com/alanreiser.com/handsdown/home/faq |

### Adjacent data points (Hands Down family, not Neu)

| # | Person / source | Data point | Notes |
|---|---|---|---|
| 4 | Kristoffer Grönlund (developer) | "decent speeds" for English + usable for programming on Hands Down Reference (no numbers); later abandoned family for his own layout | Source: https://write.as/oferlund/designing-a-keyboard-layout-part-2 |
| 5 | empressabyss (layout designer) | Tried "Hands Down Neu (kinda)", moved on to Nordrassil | Source: https://github.com/empressabyss/nordrassil |

### General alt-layout data points (context only — NOT Neu-specific)

| # | Person / source | Data point |
|---|---|---|
| 6 | Pascal Getreuer (switched 6×) | 40 wpm @1mo, 50 wpm @2mo, 80 wpm @1yr. Source: https://getreuer.info/posts/keyboards/alt-layouts/index.html |
| 7 | Joa Ebert (Graphite, 2026) | ~30 wpm first weeks, 60 wpm @3mo, 90 wpm jump, ~110 wpm @1yr; ~24h active learning. Source: https://www.joa-ebert.com/posts/2026-04-30-learning-to-type/ |
| 8 | TypingFastest (Colemak/Workman/Norman, 2026) | 15 wpm day 1, 35 wpm @2wk, 55 wpm @6wk, 72 wpm @90d, 82–85 wpm @6mo; "4–6 months to reach old QWERTY WPM." Source: https://typingfastest.com/blog/qwerty-alternatives-best-keyboard-layouts-that-actually-stick-2026 (estimate-grade) |
| 9 | Jonas Hietala (custom layout) | ~16h practice → 40 wpm (first layout); ~70 wpm when he stopped; never regained 120 wpm QWERTY. Source: https://www.jonashietala.se/blog/2023/11/02/i_designed_my_own_keyboard_layout_was_it_worth_it/ |

### Central estimate

- **Range (Neu-specific):** "mid-20s WPM (early)" → "101 WPM at ~2 months."
- **Central estimate:** **~1–2 months of disciplined daily practice + full-time use to reach ~60–100 WPM** on Neu. This is consistent with the one documented case (molohov), the designer's claim, and the general alt-layout literature.
- **To fully recover prior QWERTY speed:** expect **2–6 months** (general alt-layout consensus; no Neu-specific data).
- **Sample size & representativeness:** n = 3 usable Neu-specific points, of which 1 is the designer (biased) and 1 is a snippet-only Reddit post. **This is far too small to be statistically meaningful.** The 101 WPM point is a single self-selected enthusiast who also had prior Colemak experience. Treat all numbers as anecdote. If you need a defensible planning number, use the general alt-layout literature (rows 6–9), not the Neu-specific points.

---

## 7. Does it work for everyone? Failure cases

Documented reasons people abandon Hands Down / Neu (evidence where available, otherwise inference flagged):

1. **Vim users.** `j`/`k`/`u` positions. Grönlund abandoned the family partly for vim reasons (j in extra column on Neu; accidental `u`=undo on Reference). (Evidence: https://write.as/oferlund/designing-a-keyboard-layout-part-2 — read)
2. **Small-keyboard users (≤34 keys).** Neu's extra columns (j, z) don't fit boards like the Ferris Sweep. (Evidence: same Grönlund source — read)
3. **People who don't want the "smart keyboard" complexity.** Combos, adaptive keys, home-row mods, layers are the ecosystem's default; Xah Lee's critique is the canonical "this is overcomplicated" take. (Evidence: http://xahlee.info/kbd/hands_down_layout.html — read). Note Neu itself is optional-free, but the surrounding ecosystem isn't.
4. **People who want drop-in OS support / shortcuts preserved.** Colemak-DH keeps ZXCV and has OS support; Neu doesn't. (Inference from layouts.wiki install page + official FAQ; no direct "I left Neu for Colemak because of support" quote found — UNKNOWN as a specific quote, but strongly implied by the ecosystem.)
5. **People switching to get faster.** The general consensus (Getreuer, Hietala, TypingFastest) is that layout switches don't reliably beat a trained QWERTY typist's speed; Hietala explicitly warns "changing the layout because you want to type faster will probably not work out." (Evidence: https://www.jonashietala.se/blog/2023/11/02/i_designed_my_own_keyboard_layout_was_it_worth_it/ — read)
6. **People who can't tolerate the transition period.** The first weeks are brutal (single-digit-to-30 WPM); most burn out before recovery. (Evidence: general alt-layout sources — read)
7. **Non-English typists.** Neu is English-first; Reiser himself notes other languages need mods (he uses Japanese and designed accordingly, but the layout is English-optimized). (Evidence: official FAQ — read)

**Who it's NOT for (synthesis):** vim-heavy developers who refuse a nav layer; users on tiny boards who won't remap j/z; anyone unwilling to install third-party remapping software; anyone switching primarily for speed; anyone who wants the mainstream path (Colemak-DH).

---

## 8. The common experience (typical adoption story)

Synthesized from the above (flagged as synthesis of sparse evidence):

1. **Discovery:** usually via r/KeyboardLayouts, r/ErgoMechKeyboards, or the AKL Discord, often *after* already going down the split-ergo rabbit hole. Neu is frequently mentioned as "the layout to try if you want ultra-low SFB without thumb keys."
2. **Setup friction:** no OS support → install Kanata/Karabiner/MSKLC or flash QMK/ZMK. This is a real hurdle for non-enthusiasts.
3. **First weeks:** painfully slow (mid-20s WPM is a documented early state), muscle-memory fighting, but users report the *feel* is good early ("v.comfy").
4. **Months 1–3:** comfort solidifies; speed climbs toward usable (60–100 WPM documented at ~2 months for one disciplined user).
5. **Long-term:** those who stay report comfort as the payoff, not speed; several documented users drift to other layouts (Rhodium, custom layouts, Nordrassil) rather than staying on Neu — Neu is often a *stepping stone* into the Hands Down family or into layout design generally.
6. **The confound:** most happy long-term users are on split ergo + layers + home-row mods, so the "Hands Down made me comfortable" claim is inseparable from "split ergo made me comfortable."

---

## 9. Ecosystem

- **Official site (alanreiser.com/handsdown):** hosted on Google Sites. Unusually deep and verbose: per-variation pages, design notes, statistics, FAQ, download page, heatmaps. Quality is high but the site is sprawling and reads like a research journal rather than a quick-start guide. Actively maintained by Reiser (still recommending Neu variants; Polyglot project in progress). (Evidence: official site — read)
- **layouts.wiki:** has a Hands Down Neu page with install instructions (Kanata for Windows/Linux, .keylayout for macOS, Karabiner) and an independent assessment in the "Recommended Layouts" guide. Last updated Jul 2026. (Evidence: https://layouts.wiki/layouts/2022/hands-down-neu/ and https://layouts.wiki/guides/start/recommendations/ — read)
- **keyboard-design.com (Ian Douglas):** hosts Neu JSON files, analyzer pages, and install files (ahk, keylayout, klc, pkl, tmk, xkb) marked "Untested ALPHA/BETA. Use at own risk." Neu ranks near the top of the site's best-layout lists. (Evidence: https://keyboard-design.com/letterlayout.html?layout=hands-down-neu.eu.ansi and https://keyboard-design.com/best-layouts.html — read)
- **GitHub ecosystem (small):**
  - moutis/HandsDown — Reiser's own QMK implementations (Neu, Gold, Vibranium). (Evidence: https://github.com/moutis/HandsDown — read)
  - neonfuzz/HandsDown — community QMK for Hands Down Gold (Ergodox EZ/Moonlander), with adaptive keys and combos. (Evidence: https://github.com/neonfuzz/HandsDown — read)
  - snowkeep/hands-down — kmonad/MSKLC/Iris implementations of Hands Down Reference. (Evidence: https://github.com/snowkeep/hands-down — read)
  - zeitlinger/keyboard — a developer's full Hands Down Vibranium QMK keymap (Ferris Sweep) with home-row mods, magic keys, case modes. (Evidence: https://github.com/zeitlinger/keyboard — read)
  - DeadlySquad13/Keyboard__Hdn — Neu for Windows without universal symbols. (Evidence: https://github.com/DeadlySquad13/Keyboard__Hdn — snippet)
- **Community size:** small. The designer himself says Neu has been "adopted by dozens of other happy typists." There is no dedicated Hands Down subreddit of note; discussion lives in r/KeyboardLayouts, r/ErgoMechKeyboards, the AKL Discord, and Geekhack. (Evidence: official site — read)
- **Learning tools:** no dedicated trainer. Users point to generic tools: keybr.com, monkeytype (with custom layout), ngram-type, typing.io. The official FAQ recommends keybr-style training and ~60 WPM / 96%+ accuracy targets. (Evidence: official FAQ — read)
- **Maintenance:** the layout is stable and the site is actively maintained; native OS support was "in the works" per the design notes but as of the layouts.wiki install page (Jul 2026) you still need third-party tools. (Evidence: design notes + layouts.wiki — read)

---

## 10. Source quality notes & conflicts

- **Conflicts surfaced:**
  - Official site claims Neu's SFB is 0.949%; Getreuer's independent KLA table shows 0.76%. Different analyzers/corpora — both are "low SFB," the exact number depends on tooling. Not a substantive conflict.
  - Official site frames Neu as near-best-in-class; layouts.wiki (AKL community) says Neu is *not* among its overall picks and specifically flags the PL scissor and weak redirects, recommending Gallium/Graphite etc. instead. This is the main genuine disagreement, and it's a design-philosophy disagreement (rolling/balance vs AKL's preferred metric set), not a factual one.
  - Xah Lee dismisses the whole family as "silly and unprofessional" and over-complex; the official site and community repos treat it as serious. Xah's critique partly targets features Neu doesn't require.
- **Data sparsity (explicit):** Hands Down Neu has very few first-person experience reports in the indexed web. Reddit (the main community venue) blocked all direct reads during this research, so Reddit content is limited to search snippets. No long-term (6+ month) Neu-specific WPM-ceiling data exists in accessible sources. **This sparsity is itself a finding** — Neu is a niche layout within a niche community, and most of its user base is on split ergo boards with layers, confounding every experience claim.

---

## 11. Key URLs (most authoritative)

1. Official Hands Down Neu page: https://sites.google.com/alanreiser.com/handsdown/home/hands-down-neu
2. Official Hands Down home/FAQ: https://sites.google.com/alanreiser.com/handsdown/home/faq
3. layouts.wiki Hands Down Neu (install + metrics): https://layouts.wiki/layouts/2022/hands-down-neu/
4. layouts.wiki Recommended Layouts (independent critique): https://layouts.wiki/guides/start/recommendations/
5. Pascal Getreuer, "A guide to alt keyboard layouts" (independent metrics + learning-curve data): https://getreuer.info/posts/keyboards/alt-layouts/index.html
6. Kristoffer Grönlund, "Designing a keyboard layout" series (developer who used Hands Down): https://write.as/oferlund/designing-a-keyboard-layout-part-2
7. molohov, "Hands Down Neu @ 101WPM" (YouTube): https://www.youtube.com/watch?v=0mL5tM_fhzI
8. Xah Lee critique: http://xahlee.info/kbd/hands_down_layout.html
9. keyboard-design.com Neu analyzer page: https://keyboard-design.com/letterlayout.html?layout=hands-down-neu.eu.ansi
10. Jonas Hietala, "I designed my own keyboard layout. Was it worth it?": https://www.jonashietala.se/blog/2023/11/02/i_designed_my_own_keyboard_layout_was_it_worth_it/

---

*Method note: SearXNG was used first for discovery; fell back to the Exa-backed websearch when SearXNG returned empty or Reddit blocked reads. Every material claim above was read from its source page (searxng_web_url_read / webfetch / oEmbed) except where explicitly marked "snippet only" (Reddit threads, which returned bot-block pages). No quotes, numbers, or URLs were fabricated; unverifiable items are marked UNKNOWN.*
