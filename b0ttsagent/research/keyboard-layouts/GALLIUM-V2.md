# Gallium v2 Keyboard Layout — Deep Research

**Research date:** 2026-08-18
**Scope:** Real community experience (not just design rationale/metrics) for the Gallium v2 ("Rowstag") layout, aimed at a developer doing mixed general English + programming.
**Method note:** SearXNG-first discovery; every material claim below was read from its source page where possible. Reddit blocks direct fetching (403 on HTML and .json, old.reddit, and webfetch), so Reddit-sourced items are flagged **[snippet]** — recovered from search-result snippets/highlights, not full-page reads. Treat those as lower-confidence. Everything else was read in full.

> **NOTE ON FILE LOCATION:** The requested path `b0ttsagent/research/keyboard-layouts/GALLIUM-V2.md` could not be created — the `keyboard-layouts/` folder does not exist and this agent has no directory-creation tool (the write tool requires an existing parent dir). This file is therefore written to the existing `b0ttsagent/research/` root. Move it into a `keyboard-layouts/` subfolder if desired.

---

## 1. What it is

**Origin.** Gallium is an open-source alternative keyboard layout created by **Bryson James (online handle "GalileoBlues")**, first published on GitHub in **March 2023** (earliest documented activity: Linux support added March 2023). It is named after the chemical element gallium. (https://github.com/GalileoBlues/Gallium ; https://grokipedia.com/page/Gallium_keyboard_layout)

**Lineage.** Gallium "takes inspiration from nerps and tries to improve on it in comfort and speed." It traces lineage from **Nerps by Smudge** (changing the vowel block and removing the need to alt-finger `SP/PS`), and is extremely similar to **Graphite** (by Richard Davison), whose predecessor predates Gallium by a few weeks. Both Gallium and Graphite draw on the earlier **Sturdy** (Oxey). (https://github.com/GalileoBlues/Gallium ; https://github.com/noodleweapon/gallium-v2)

**v1 vs v2.** There are two primary variants:
- **Gallium Colstag** (the original, "v1") — designed for column-staggered / ortholinear keyboards.
- **Gallium Rowstag** (previously named "Gallium v2") — made "to cater directly to the average user on a Row staggered keyboard based on feedback I received after the original version." The two differ mainly by a cycle of **Y, P, F** on the right index finger. (https://github.com/GalileoBlues/Gallium ; https://getreuer.info/posts/keyboards/alt-layouts/index.html)

The task's "Gallium v2" = **Gallium Rowstag**. Note the naming is confusing: the author has since renamed "v2" → "Rowstag" and "v1" → "Colstag" in the main repo, but the community and many forks (e.g. `noodleweapon/gallium-v2`) still call it "Gallium v2." (https://github.com/GalileoBlues/Gallium)

**Design goals.** Per the author: "Gallium tries to break up repetitive patterns, balance fatigue between the hands and be generally compatible with most people." Concretely:
- Low **same-finger bigrams (SFBs)** — a headline metric.
- Balance **alternation vs rolls** (bring the ratio closer together) by making **H** the root vowel-hand index letter.
- **Hand balance** — left ~46.6% / right ~53.4% of keypresses.
- **Pinky usage** deliberately maximized up to a threshold (based on observation of 200 wpm typists' "floating pinky" form), while cautioning people with chronic pinky/ring issues. (https://github.com/GalileoBlues/Gallium ; https://github.com/noodleweapon/gallium-v2 ; https://grokipedia.com/page/Gallium_keyboard_layout)

**Where it sits vs Nerps/others.** Gallium is one of the "NRTS HAEI" family (home row = N R T S G / H A E I), alongside Graphite. It is a **"balanced"** layout — decent across all main AKL metrics (SFB, scissors, lateral stretch, redirects) but not the best at any single one. Getreuer's guide: "If you don't know what to pick, Gallium is recommended." The AKL Discord typically recommends starting with Gallium. (https://getreuer.info/posts/keyboards/alt-layouts/index.html ; https://layouts.wiki/guides/start/recommendations/)

**Key metrics (analyzers, English):** SFB ~0.57–0.64% (vs QWERTY 4.38%, Dvorak 1.87%); finger travel ~72.65 (ANSI QWERTY=100); hand balance ~46.6/53.4. (https://layouts.wiki/layouts/2023/gallium/ ; https://grokipedia.com/page/Gallium_keyboard_layout ; https://getreuer.info/posts/keyboards/alt-layouts/index.html)

**Known weaknesses (author-disclosed):** Gallium "does particularly poorly at much more complex words such as Monkeytype's 450k wordlist" — SFBs `HY`, `PY`, `PH`, `PF` appear more in advanced vocabulary. Layouts Wiki adds: the right-index patterns in words like "happy," "physics," "python," and the **B on the pinky top row** causing uncomfortable patterns with R and M ("broad," "thumb"). (https://github.com/GalileoBlues/Gallium ; https://layouts.wiki/guides/start/recommendations/)

---

## 2. Short-term experience (first days/weeks)

Individual reports (all short-term, all self-selected):

- **Zaid (Substack, Nov 2024):** Practiced 20–30 min/day on Monkeytype for 7 days; hit **40 wpm on day 7** (was ~20 wpm on day 1). Previous QWERTY ~100 wpm. Verdict: "the effort is not worth the gains" — cited practice time, QWERTY muscle-memory conflict, gaming-keybind compatibility, and relearning shortcuts as costs. (https://weeklymission.substack.com/p/keyboard-layouts-arent-worth-it-kinda) **[read]**
- **Matt Maguire (teachmaths.org, Oct 2024):** After ~1 week of practice, "still fighting the muscle memory that I built up with the ISRT layout," at **~25 wpm**. (https://www.teachmaths.org/20241010_updates-to-gallium-keyboard-layout/) **[read]**
- **r/typing "Week 1 progress switching from QWERTY to gallium v2" (2024):** OP still types QWERTY at 90+ wpm on occasion during week 1, wants "a better, more relaxed and balanced typing layout." (https://www.reddit.com/r/typing/comments/1d8993w/week_1_progress_switching_from_qwerty_to_gallium/) **[snippet]**
- **r/KeyboardLayouts "14 days to Graphite/Gallium layout" (Sep 2025):** Went cold-turkey "all in from the get go"; used Keybr until all keys unlocked then Monkeytype. "It took me 14 days and 22 hours of practice to unlock all keys at default 35+ WPS. But real world speed is around 45+ these days." QWERTY baseline 70–85 wpm. (https://www.reddit.com/r/KeyboardLayouts/comments/1nudm7y/14_days_to_graphitegallium_layout/) **[snippet/highlights]**

**Common short-term pattern:** Gallium changes nearly every key position from QWERTY (only G stays), so the first days are a steep, frustrating drop — typically to ~20–40 wpm — with active muscle-memory fighting against QWERTY. SureTyping (a learning tool) describes it as "unfamiliar enough to demand a real retraining window." (https://suretyping.com/keyboard-layouts/gallium) **[read]**

---

## 3. Mid-term experience (first ~1–6 months)

- **r/KeyboardLayouts "Gallium v2" commenter (Mar 2024):** "I've been using gallium v2 for the past couple of months, before this I was using canary, currently averaging around **80 wpm** with it. I'm using it on a 34 key ortholinear keyboard. I really really like this layout." — i.e., ~2 months to ~80 wpm from a Canary baseline. (https://www.reddit.com/r/KeyboardLayouts/comments/196ow4k/gallium_v2/) **[snippet]**
- **Matt Maguire:** at ~25 wpm after a week; no later update found confirming his eventual speed. (https://www.teachmaths.org/20241010_updates-to-gallium-keyboard-layout/) **[read]**
- **General alt-layout reference (not Gallium-specific):** Getreuer's own progression across half a dozen layouts: "40 wpm after the first month, 50 wpm after the second month, and 80 wpm after the first year." (https://getreuer.info/posts/keyboards/alt-layouts/index.html) **[read]**

**Mid-term pattern:** For dedicated daily practice, most reach a usable ~40–50 wpm within ~1–2 months and ~80 wpm within ~2 months to a year. Comfort gains (reduced SFB, better hand balance) are the commonly cited payoff rather than raw speed.

---

## 4. Long-term experience (6+ months)

**Sparse — this is a genuine finding.** I found **no dedicated 6-month+ Gallium-specific experience reports** (no "one year in on Gallium" posts). The layout is young (2023) and niche, and most public reports are short-term (days–weeks) or mid-term (~2 months). Long-term claims below are therefore **inference from adjacent layouts**, not Gallium evidence:

- Getreuer's general alt-layout trajectory (80 wpm after ~1 year) is the closest proxy. (https://getreuer.info/posts/keyboards/alt-layouts/index.html)
- Several community members describe Gallium as a **stepping stone** rather than a destination: "I made a couple quick hops Canary -> Gallium v2 -> Graphite" (https://l.hostux.net/post/47729) **[snippet]**; and a r/KeyboardLayouts commenter notes Graphite "seems to be an evolution of gallium" (https://www.reddit.com/r/KeyboardLayouts/comments/1dnlcqg/where_to_find_updated_gallium_layouts/) **[snippet]**.
- No regrets/abandonment-after-6-months reports specific to Gallium were found. **UNKNOWN** whether people stick with it long-term.

---

## 5. Pros and cons (especially for coding / general typing)

**Pros**
- **Excellent SFB avoidance** (~0.57–0.64%) — the headline comfort win; much lower than QWERTY/Dvorak. (https://layouts.wiki/layouts/2023/gallium/ ; https://grokipedia.com/page/Gallium_keyboard_layout)
- **Balanced metrics** — "decent across the board, none especially good, none especially bad"; a safe default pick. (https://layouts.wiki/guides/start/recommendations/ ; https://getreuer.info/posts/keyboards/alt-layouts/index.html)
- **Good hand balance** (~46.6/53.4) and reduced finger travel (~27% less than QWERTY). (https://grokipedia.com/page/Gallium_keyboard_layout)
- **Vim-friendliness:** Getreuer lists Gallium (with Colemak) among layouts that "play well with default Vim bindings," and notes "considering the j key, Gallium may be preferable for Vim" vs Graphite. (https://getreuer.info/posts/keyboards/alt-layouts/index.html) **[read]**
- **Recommended default** by Getreuer and the AKL Discord for people who can't decide. (https://getreuer.info/posts/keyboards/alt-layouts/index.html ; https://layouts.wiki/guides/start/recommendations/)

**Cons**
- **Vim is still a real friction point.** The r/KeyboardLayouts "Gallium v2" commenter who liked the layout "ended up changing because of how godawful vim is" with it. (https://www.reddit.com/r/KeyboardLayouts/comments/196ow4k/gallium_v2/) **[snippet]** Another user: "the j/k positions didn't sit right with me... which is what Gallium showed me" and "I definitely didn't like the stretch for j on modded Gallium." (https://l.hostux.net/post/47729) **[snippet]**
- **Symbols/shortcuts:** Gallium's punctuation is on the base layer but non-standard; for coding, Getreuer's general advice is that the real bottleneck is symbols, and recommends a **symbol layer** regardless of alpha layout. Graphite (not Gallium) is the one explicitly optimized for programming punctuation. (https://getreuer.info/posts/keyboards/alt-layouts/index.html) **[read]**
- **Pinky/ring load:** author explicitly warns people with chronic pinky/ring issues to prefer Colemak; Gallium "does have some pinky and ring usage that would require work to transition to from Qwerty." (https://github.com/GalileoBlues/Gallium) **[read]**
- **Advanced-vocabulary SFBs** (`HY`, `PY`, `PH`, `PF`) — matters for long-form technical writing. (https://github.com/GalileoBlues/Gallium)
- **B on pinky top row** — uncomfortable with R/M ("broad," "thumb"). (https://layouts.wiki/guides/start/recommendations/)
- **QWERTY muscle-memory conflict** and needing to keep QWERTY for other people's machines / gaming keybinds (Zaid's main complaint). (https://weeklymission.substack.com/p/keyboard-layouts-arent-worth-it-kinda) **[read]**

---

## 6. Time to positive results — individual data points

**Gallium-specific individual data points (n = 5):**

| # | Source | Baseline (QWERTY) | Time | Result |
|---|--------|-------------------|------|--------|
| 1 | Zaid, Substack (Nov 2024) | ~100 wpm | 7 days (20–30 min/day) | 40 wpm; judged not worth it |
| 2 | Matt Maguire, teachmaths.org (Oct 2024) | (from ISRT) | ~1 week | ~25 wpm, still fighting muscle memory |
| 3 | r/typing "Week 1 progress" (2024) | 90+ wpm | 1 week | still slow; keeps QWERTY for speed |
| 4 | r/KeyboardLayouts "14 days to Graphite/Gallium" (Sep 2025) | 70–85 wpm | 14 days / 22 hrs practice | 35+ wpm (all keys), ~45 wpm real-world |
| 5 | r/KeyboardLayouts "Gallium v2" commenter (Mar 2024) | (from Canary) | ~2 months | ~80 wpm avg; likes it |

**Range:** ~1–2 weeks of dedicated daily practice to reach a usable **~35–45 wpm** (data points 1, 4; point 2 slower at 25 wpm). ~2 months to reach **~80 wpm** (point 5, single report).

**Central estimate:** With ~20–30 min/day of deliberate practice, expect **~40 wpm within ~1–2 weeks** and **~80 wpm within ~2 months to a year**. This aligns with Getreuer's general alt-layout trajectory (40 wpm/1 mo, 50 wpm/2 mo, 80 wpm/1 yr) and SureTyping's "2–3 month transition to reach your previous speed" estimate. (https://getreuer.info/posts/keyboards/alt-layouts/index.html ; https://suretyping.com/keyboard-layouts/gallium)

**Sample-size / representativeness caveat (important):** n=5 is **very small**, heavily self-selected (people who post about a niche layout), and skewed to short-term (4 of 5 are ≤2 weeks). There is **no long-term (6+ month) Gallium-specific data point**. Three of the five are **[snippet]**-grade (Reddit blocked full reads). Do not treat the ~80 wpm/2-month figure as robust — it is a single report. The honest statement is: **usable speed in ~1–2 weeks is the most consistent finding; everything beyond ~2 months is under-evidenced.**

---

## 7. Does it work for everyone? Failure cases / who it's NOT for

- **Vim users:** the strongest documented failure mode. One satisfied user abandoned Gallium v2 specifically because of Vim; another disliked the j stretch. (https://www.reddit.com/r/KeyboardLayouts/comments/196ow4k/gallium_v2/ ; https://l.hostux.net/post/47729) **[snippet]**
- **People with chronic pinky/ring-finger issues:** author explicitly urges caution and points them to Colemak. (https://github.com/GalileoBlues/Gallium) **[read]**
- **People who can't tolerate a long productivity dip:** Zaid's "not worth it" verdict is the archetype — practice time, QWERTY conflict, gaming keybinds, relearning shortcuts. (https://weeklymission.substack.com/p/keyboard-layouts-arent-worth-it-kinda) **[read]**
- **Switch-fatigued / layout-hoppers:** multiple reports of Gallium being a hop on the way to Graphite or elsewhere ("Canary -> Gallium v2 -> Graphite"). (https://l.hostux.net/post/47729) **[snippet]**
- **Ecosystem/tooling gaps:** Windows and macOS installers in the main repo are "out of date currently" (only Kanata is fully current across all variants/OSes) — a real maintenance risk for non-Linux users. (https://github.com/GalileoBlues/Gallium) **[read]**
- **Too-new layout:** Gallium is 2023; community experience is thin vs Colemak. This is a documented ecosystem-maturity risk (see §9).

---

## 8. The common experience (typical adoption story / consensus view)

The consensus picture across sources:
1. **It's a strong, safe, "balanced" modern layout** — the community's default recommendation for someone who can't decide, alongside Graphite. (https://getreuer.info/posts/keyboards/alt-layouts/index.html ; https://layouts.wiki/guides/start/recommendations/)
2. **The switch is a real slog** — nearly every key moves, so the first 1–2 weeks are a frustrating drop to ~20–40 wpm with active QWERTY muscle-memory fighting. (multiple sources above)
3. **With daily practice it clicks within ~1–2 months** to a usable ~40–50 wpm, and ~80 wpm within ~2 months–1 year. (data points + Getreuer)
4. **The payoff is comfort, not speed** — reduced SFBs and better hand balance; speed gains are marginal once you're past ~70 wpm. (Getreuer; Zaid's counterpoint)
5. **Vim is the recurring caveat** — workable (better than Graphite on j) but a documented reason people leave. (Getreuer; reddit/lemmy reports)
6. **Many treat it as a stepping stone** to Graphite or a custom layout rather than a final destination. (lemmy; r/KeyboardLayouts)

---

## 9. Ecosystem

**Learning tools**
- **Monkeytype** — Gallium is available as a layout ("Now on Monkeytype!" per the repo README). (https://github.com/GalileoBlues/Gallium) **[read]** (Direct monkeytype layout URL 404'd in this research; the README claim is the evidence.)
- **SureTyping** — full Gallium lesson path (422 lessons: home-row → upper/lower row → full-keyboard fluency) plus an AI trainer; also publishes a "2–3 month transition" estimate. (https://suretyping.com/keyboard-layouts/gallium) **[read]**
- **Keybr** — used by the "14 days" OP for initial key unlocking. (https://www.reddit.com/r/KeyboardLayouts/comments/1nudm7y/14_days_to_graphitegallium_layout/) **[snippet]**
- **Keycraft** — has a `gallium-v2` layout page. (https://rbscholtus.github.io/keycraft/layouts/gallium-v2.html)
- **Alt Alpha** (timvink.nl) — layout try-out tool that includes gallium v2. (https://altalpha.timvink.nl/try-layout.html)
- **keyboard-layout-try-out.pages.dev** — translate-text tool to preview a layout. (https://www.teachmaths.org/20241010_updates-to-gallium-keyboard-layout/) **[read]**

**OS support / remapping**
- **Kanata** — the most complete and current implementation, cross-platform (Windows/macOS/Linux), covers all variants. (https://github.com/GalileoBlues/Gallium) **[read]**
- **Linux XKB** — provided by GalileoBlues (both Rowstag and Colstag). (https://github.com/GalileoBlues/Gallium) **[read]**
- **Windows** (by CTGAP) and **macOS** (by Dainternetdude) — **currently out of date** per the repo. (https://github.com/GalileoBlues/Gallium) **[read]**
- **EPKL** (DreymaR's Windows tool) — Gallium added (2024), with an Extend layer; DreymaR favors the v2/Rowstag version. (https://www.teachmaths.org/20241010_updates-to-gallium-keyboard-layout/ ; https://github.com/DreymaR/BigBagKbdTrixPKL/tree/master/Layouts/Gallium) **[read]**
- **Karabiner Elements** (macOS) — used by Matt Maguire for his Gallium keymap. (https://www.teachmaths.org/20241002_gallium-keyboard-layout/) **[read]**
- **QMK/ZMK firmware** — flashable on programmable boards; community configs exist (e.g. Kanata configs with combos and QWERTY-shortcut layers). (https://github.com/zachpoblete/kanata-guide-for-alt-layouts)
- **keyboard-design.com** — hosts `gallium2.en.ansi` with install files (Linux/Mac/Windows, marked untested alpha/beta). (https://keyboard-design.com/letterlayout.html?layout=gallium2.en.ansi)

**Community size / maintenance status**
- **Maintenance:** actively maintained by GalileoBlues (repo has 47 commits, 211 stars, 13 forks at research time; ongoing changes to bring installs up to date). (https://github.com/GalileoBlues/Gallium) **[read]**
- **How new:** first published March 2023; v2/Rowstag July 2023. (https://grokipedia.com/page/Gallium_keyboard_layout)
- **Community size:** niche but established within the AKL scene — recommended by Getreuer and the AKL Discord, present on Monkeytype, layouts.wiki, SureTyping, EPKL, Keycraft. Still far smaller and younger than Colemak/Dvorak. (multiple sources)
- **Availability on keyboards:** not a stock OS layout; requires remapping software (Kanata/Karabiner/EPKL) or flashing firmware (QMK/ZMK). No prebuilt keyboard ships with it.

**Ecosystem-maturity caveat (explicit finding):** Gallium is young (2023) and niche. Tooling is decent (Monkeytype, SureTyping, EPKL, Kanata, layouts.wiki), but: (a) Windows/macOS installers are currently stale; (b) community experience data is thin and short-term; (c) it's frequently a stepping stone to Graphite. Anyone adopting it should expect to maintain their own remap config and accept a small, enthusiast community.

---

## Source conflicts / caveats

- **v1/v2 naming:** The author renamed v2→"Rowstag" and v1→"Colstag" in the main repo, but community/forks still say "v2." Both refer to the same row-stagger-focused variant. (https://github.com/GalileoBlues/Gallium)
- **Rowstag vs Colstag preference:** Matt Maguire chose v1/Colstag for column-staggered boards, while DreymaR favors v2/Rowstag even on row-staggered boards; the author says either works on either keyboard type. (https://www.teachmaths.org/20241002_gallium-keyboard-layout/ ; https://github.com/DreymaR/BigBagKbdTrixPKL/tree/master/Layouts/Gallium)
- **Metric values vary by analyzer/corpus** (SFB 0.57% on layouts.wiki vs 0.64% on Getreuer vs 0.80% on Monkeyracer) — normal for the field; not a contradiction. (https://layouts.wiki/layouts/2023/gallium/ ; https://getreuer.info/posts/keyboards/alt-layouts/index.html ; https://ratoru.com/blog/choose-the-right-base-layout/)
- **Reddit data is snippet-grade** (full reads blocked). The 80 wpm/2-month figure and the "godawful vim" quote are from search snippets, not full-page reads — treat as directional, not confirmed verbatim.

---

## Key URLs (canonical)
- https://github.com/GalileoBlues/Gallium (author repo, README)
- https://getreuer.info/posts/keyboards/alt-layouts/index.html (Getreuer's guide — recommended default, Vim section)
- https://layouts.wiki/layouts/2023/gallium/ and https://layouts.wiki/guides/start/recommendations/ (metrics + balanced-layout assessment)
- https://grokipedia.com/page/Gallium_keyboard_layout (overview + metrics)
- https://www.teachmaths.org/20241002_gallium-keyboard-layout/ and .../20241010_updates-to-gallium-keyboard-layout/ (Matt Maguire's hands-on blog)
- https://weeklymission.substack.com/p/keyboard-layouts-arent-worth-it-kinda (Zaid's 7-day "not worth it" report)
- https://suretyping.com/keyboard-layouts/gallium (learning tool + transition estimate)
- https://www.reddit.com/r/KeyboardLayouts/comments/196ow4k/gallium_v2/ (community thread; snippet-grade)
- https://www.reddit.com/r/KeyboardLayouts/comments/1nudm7y/14_days_to_graphitegallium_layout/ (14-day report; snippet-grade)
