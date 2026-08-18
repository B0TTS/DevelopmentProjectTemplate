# Colemak-DH — Deep Research: Real Community Experience

**Research date:** 2026-08-18
**Scope:** Colemak-DH / Colemak Mod-DH / Colemak-DHk / Colemak-DHm, ANSI vs matrix/columnar variants, for a developer (mixed English + programming).
**Method:** SearXNG-first discovery, then read each cited page in full (Reddit was blocked to direct fetch; Reddit-derived claims are marked as such and backed by search-snippet evidence only). Evidence vs inference vs unknown is flagged inline.

---

## 1. What it is

**Origin.** Colemak Mod-DH ("Colemak-DH") is an unofficial modification of the Colemak layout, created by SteveP and launched **October 2014**. It is a light mod that keeps all of Colemak's strengths (home-row placement, low same-finger bigrams) while fixing the two most-cited Colemak flaws: the awkward placement of **D** and **H** in the hard-to-reach centre column. Source: https://colemakmods.github.io/mod-dh/

**The changes from vanilla Colemak** (all keys stay on the same finger, so it's easy for existing Colemak users to adopt):
- **Left hand ("D" change):** applies the **Angle Mod** to Z/X/C (moves them one key left, conventional finger assignment kept), relocates **D** (to the index-finger bottom-row spot), **G** (reverts to its QWERTY position), and **B** (moves from bottom-middle to the top row).
- **Right hand ("H" change):** **H** and **M** swap places, putting the common H under the index finger and making the very common **HE** bigram comfortable ("the", "then", "where").
- Net effect: **centre-column usage roughly halves** (14.78% → 7.80% in the mod's own analysis). Source: https://colemakmods.github.io/mod-dh/

**Angle Mod / Curl Mod.** On standard row-staggered keyboards, DH is designed to be used with the **Angle Mod** (bottom-left keys shifted left for a straighter left wrist) and is described as a **Curl Mod** (index fingers curl inward to reach D/H). DreymaR notes that on row-staggered boards the Curl(DH) mod should be combined with Angle/AngleWide to work as designed; "CurlAngle is the Colemak-DH standard for row-staggered keyboards." Source: https://dreymar.colemak.org/ergo-mods.html

**ANSI vs ISO vs matrix/columnar variants.** There are separate implementations optimized for ISO, ANSI, and matrix (ortholinear/columnar) keyboards. The matrix version was formerly called **Colemak-DHm**. Source: https://colemakmods.github.io/mod-dh/ and https://colemakmods.github.io/mod-dh/keyboards.html

**DHk vs DHm (revision history).** The original 2014 release had M in the middle row. A May 2017 revision swapped M and K for standard staggered keyboards, producing **Colemak-DHk** (K in middle row). The original mapping (M in middle row) was kept for ortho/ergo boards as **Colemak-DHm**. In **October 2020** the M–K switch was reverted; the original release (a.k.a. DHm) is now recommended on **all** keyboard types. Source: https://colemakmods.github.io/mod-dh/ (Revision History). *Note: this means "DHk" is now a legacy/less-recommended variant; a 10-month DHk user on the forum reported difficulty even getting the DHk layout configured on their hardware.* Source: https://forum.colemak.com/topic/2954-my-expereince-after-typing-colemakdhk-for-about-10-months/

**Metrics (why it's "good on paper").** Getreuer's layout table: Colemak-DH has SFBs 0.91%, LSBs 1.27%, scissor 0.15%, rolls 49.20%, redirects 5.33%, pinky-off 0.78% — essentially identical to vanilla Colemak except LSBs drop from 2.26% to 1.27%. Getreuer calls it "a solid layout and continues to be quite popular in the custom keyboard community," noting it keeps QWERTY positions of Z/X/C (and vanilla Colemak keeps V) for hotkeys, and has very low off-home pinky use. Source: https://getreuer.info/posts/keyboards/alt-layouts/index.html

**Caveat from the modern-layout crowd.** Several newer-layout advocates argue Colemak-DH is "old" (pre-analyzer) and that post-2022 layouts (Canary, Graphite, Magic Sturdy, Gallium) have better statistics; Raphael Ruban says he switched away from Colemak-DH because of **redirects**, and recommends skipping "old layouts like Dvorak and Colemak-DH." Middlemak's author lists DH's remaining issues (right-index overwork, pinballing, NFBs, hand balance, ring-to-pinky rolls). These are *design-critique* opinions, not experience reports. Sources: https://ratoru.com/blog/choose-the-right-base-layout/ , https://github.com/KeyboardLayout2/Middlemak

---

## 2. Short-term experience (first days/weeks)

Consistent across nearly all reports: the first days–weeks are **frustratingly slow and mentally exhausting**, with constant muscle-memory fighting.

- **Speed collapse.** A 90 WPM QWERTY typist can drop to under 20 WPM on DH; "simple sentences quickly become tiring." (typingbattles guide — general/estimate-grade, not a first-person data point) https://www.typingbattles.com/blog/colemak-dh-typing-practice-what-changing-from-qwerty-is-really-like
- **Concrete starts:** Vale started at **4.8 WPM** (from 64 QWERTY) https://vale.rocks/posts/typing-systems ; Hannah went from **120 WPM QWERTY to 15 WPM** https://hannahswainlovik.eu/2017/02/07/the-experience-of-switching-to-colemak/ ; Picador from **110 to 20 WPM overnight** https://thepicador.org/2491/showcase/qwerty-vs-colemak-whats-your-type/ ; Silvestri scored **9 WPM** on first attempt https://www.silvestri.cloud/blogs/redox-build-part-three/ ; ollyjarvis ~**20 WPM after 5 days** https://ollyjarvis.uk/posts/crkbd/
- **Muscle-memory fighting.** "Every letter I typed involved consciously stopping my muscle memory from taking over… Frustrating is an understatement." (Callum Oakley) https://callumoakley.net/posts/colemak ; BeerRiot describes the "in-between" state where fingers autopilot to QWERTY and produce "50% decrypted" garbage, and a low emotional point when switching back felt impossible. https://blog.beerriot.com/2024/10/19/learning-colemak-dh/
- **The "same-position" trap.** BeerRiot notes that Colemak's QWERTY-similarity can *hurt*: a letter in the same spot (e.g. Q) re-awakens QWERTY muscle memory mid-word. https://blog.beerriot.com/2024/10/19/learning-colemak-dh/
- **Frustration-driven abandonment is common here.** Muirium (deskthority) "barely reaching 20 lousy wpm" and ditched the experiment after about a week; Protesilaos gave up after ~3 weeks. Sources: https://deskthority.net/viewtopic.php?p=515790 , https://protesilaos.com/keeb/2024-05-18-colemak-layout-lessons/
- **Sleep helps.** BeerRiot reports major progress happens overnight between practice days. https://blog.beerriot.com/2024/10/19/learning-colemak-dh/

---

## 3. Mid-term experience (first ~1–6 months)

- **"Click" timing.** The typingbattles guide (general) puts the "click" at **month 2 and beyond**; some faster, some months. https://www.typingbattles.com/blog/colemak-dh-typing-practice-what-changing-from-qwerty-is-really-like
- **Speed recovery is the dominant theme.** Getreuer's own progression across several layout switches: **40 WPM after month 1, 50 after month 2, 80 after year 1**; he says "realistically expect at least a couple months of daily practice." https://getreuer.info/posts/keyboards/alt-layouts/index.html
- **Forum consensus on regaining QWERTY speed: ~3 months (~90 days).** "Main consensus here is that you will get back to your Qwerty speed in three months (~90 days) but with more comfort." One user reached it in ~1 month with 1hr+ daily practice; another took 3 months to 100 WPM and ~1.5x that in half a year more. https://forum.colemak.com/topic/1747-typing-speed-progress/
- **Individual mid-term milestones:** engiwengi hit **50 WPM in ~1 week, 70 in 2, 90 in 3, 100 in 5–6 weeks** (heavy ~2hr/day practice) https://forum.colemak.com/topic/2272-my-layout-switching-experience/ ; Vale reached high-40s by ~2 months and **surpassed his 64 WPM QWERTY on 20 Apr 2023 (~5 months)** https://vale.rocks/posts/typing-systems ; Sabih hit **65 WPM in 2 months** https://medium.com/@irisman/the-peak-programming-keyboard-and-key-layout-57cded217236 ; Hannah hit **100 WPM at ~100 days** https://hannahswainlovik.eu/2017/02/07/the-experience-of-switching-to-colemak/ ; Mac Merritt was at **50 WPM after 1 month** (from 80 QWERTY) and still recovering https://www.linkedin.com/posts/macmerritt_techlife-productivityhacks-softwareengineering-activity-7263268918885007361-zHsj
- **A common mid-term dip:** one HN user reports being "slow at both qwerty and colemak" around 3 months and thinking it was a mistake, only to be "totally happy" by 6 months. https://news.ycombinator.com/item?id=36005823
- **Comfort gains often arrive before speed.** Multiple users report reduced fatigue/wrist strain even while still slower than QWERTY (see §4).

---

## 4. Long-term experience (6+ months / years)

- **Sustained comfort is the most-cited long-term benefit.** "I've been using Colemak for about 14 years now… haven't had a repeat of the wrist pain I lived with with QWERTY." (HN) https://news.ycombinator.com/item?id=36005823 ; Lily Oliveira switched to Colemak-DHm for wrist pain and "no longer experience[s] pain after hours typing" https://lilyoliveira.com/40s-keyboard-software-engineer/ ; Luke Brannagan: 6 months / 70 hours fixed his RSI (but he had to sacrifice Vim muscle memory) https://www.linkedin.com/posts/luke-brannagan_switching-from-qwerty-to-colemak-dh-a-journey-activity-7429155174734131200-MogZ ; a 6-year Iris/Colemak-DH user reports far more comfortable typing and that trying to return to QWERTY made his hands hurt https://tilde.club/~jbd/posts/iris-keyboard-layout/
- **WPM ceiling.** Most long-term users report speed roughly **equal to or modestly above their old QWERTY**, not dramatically higher. Examples: engiwengi eventually reached **115–135 WPM** (from 110 QWERTY) https://forum.colemak.com/topic/2272-my-layout-switching-experience/ ; Sabih **120 WPM at 1 year** (maxed 125 QWERTY) https://medium.com/@irisman/the-peak-programming-keyboard-and-key-layout-57cded217236 ; Garrett Leber ~**100 WPM** (from 110 QWERTY) but "much faster when writing code" https://garrettleber.com/blogs/ergo-keyboards-are-fun/ ; Hannah **80–100 WPM** (from 120) https://hannahswainlovik.eu/2017/02/07/the-experience-of-switching-to-colemak/ ; Callum "fairly commonly reach[es] 100 WPM" https://callumoakley.net/posts/colemak
- **Some never regain QWERTY speed and are fine with it.** "I too never got as fast as I did with qwerty but it's so much more comfortable that I don't care." (HN) https://news.ycombinator.com/item?id=36005823
- **Do people stick with it?** Many do long-term (6–14 years reported). But a meaningful minority switch away — see §7. The forum notes the two 220+ WPM Colemak typists use different variants (Sophie = vanilla, Viper = Colemak-CAWS), showing speed isn't DH-specific. https://forum.colemak.com/topic/2739-why-i-switched-back-to-colemak-again/
- **Regrets are rare but exist.** The most common long-term regret is **losing QWERTY fluency** (shared machines, pair programming, other people's keyboards) rather than the layout itself. See §7.

---

## 5. Pros and cons (especially for coding)

**Pros**
- **Comfort/ergonomics** is the dominant, repeatedly-reported win — reduced wrist/finger fatigue and RSI relief for many. (multiple sources above)
- **Keeps QWERTY hotkeys Z/X/C** (and vanilla keeps V) — undo/cut/copy/paste stay put, a real advantage over Dvorak. Sources: https://getreuer.info/posts/keyboards/alt-layouts/index.html , https://colemakmods.github.io/mod-dh/
- **Fixes Colemak's two worst keys (D, H)** and roughly halves centre-column use. https://colemakmods.github.io/mod-dh/
- **No keys change fingers from Colemak**, so it's an easy upgrade for existing Colemak users. https://colemakmods.github.io/mod-dh/
- **Huge ecosystem** (see §9) — best-supported alt layout after QWERTY/Dvorak.
- **For coding specifically:** several programmers report being *faster at code* even at similar raw WPM, because symbol layers on ergo boards + comfort dominate. Garrett Leber: "I can type MUCH faster when it comes to writing code." https://garrettleber.com/blogs/ergo-keyboards-are-fun/ ; Sabih: "a big boost for comfort and speed (especially when it comes to symbols)." https://medium.com/@irisman/the-peak-programming-keyboard-and-key-layout-57cded217236

**Cons**
- **Big upfront time cost** — weeks to months of reduced productivity. (universal)
- **Vim/Neovim friction.** HJKL navigation breaks; users either remap (many plugins exist) or lose Vim muscle memory. BeerRiot: default vim bindings "seem like a bad idea in Colemak" (colon leaves home row; J/K up/down are top/bottom row). https://blog.beerriot.com/2024/10/19/learning-colemak-dh/ ; Luke Brannagan explicitly "had to sacrifice my Vim muscle memory." https://www.linkedin.com/posts/luke-brannagan_switching-from-qwerty-to-colemak-dh-a-journey-activity-7429155174734131200-MogZ ; one HN user abandoned the layout partly because "half the shortcuts are positional… but the other half are mnemonics and now in Colemak they can't be both." https://news.ycombinator.com/item?id=36005823
- **Emacs bindings also shift** (BeerRiot documents the relearning). https://blog.beerriot.com/2024/10/19/learning-colemak-dh/
- **Symbols/punctuation.** On a standard board, symbols stay where QWERTY put them (they're not part of the alpha remap), so no direct loss — but on ergo/40% boards you must design a symbol layer. BeerRiot notes colon moves off the home row for vim. https://blog.beerriot.com/2024/10/19/learning-colemak-dh/
- **DH-specific gripes:** the top/bottom-row jumping for index-finger keys (P/B on left, L on right) bothers some; one user went back to vanilla Colemak after ~100 hours because of it. https://forum.colemak.com/topic/2739-why-i-switched-back-to-colemak-again/ ; the "sloping home row" feel is a real adjustment.
- **Losing QWERTY fluency** on shared machines / other people's keyboards. (multiple sources)
- **Not a speed hack.** Getreuer: "speed is a matter of typing practice, not layout." https://getreuer.info/posts/keyboards/alt-layouts/index.html

---

## 6. Time to positive results — individual data points

**Definition used:** time to reach former QWERTY speed, or to a "usable" speed (~40–50 WPM). Sample is small and self-selected (people who post online skew toward success or strong opinion), so treat the average as indicative, not predictive.

**Explicit "time to former QWERTY speed" data points:**
| Person | QWERTY speed | Time to former speed | Source |
|---|---|---|---|
| HN user (cold turkey, 10–20hr weekend) | ~110 WPM | ~"a few weeks" | https://news.ycombinator.com/item?id=36005823 |
| engiwengi (heavy ~2hr/day practice) | 110 WPM | ~5–6 weeks (100 WPM) | https://forum.colemak.com/topic/2272-my-layout-switching-experience/ |
| Vale | 64 WPM | ~5 months (surpassed on 20 Apr 2023) | https://vale.rocks/posts/typing-systems |
| Hannah Swain Løvik | 120 WPM | ~3 months (100 WPM @100 days) | https://hannahswainlovik.eu/2017/02/07/the-experience-of-switching-to-colemak/ |
| Picador (Isabella Qian) | 110 WPM | "a few months" (matched, not surpassed) | https://thepicador.org/2491/showcase/qwerty-vs-colemak-whats-your-type/ |
| Forum "Typing Speed Progress" consensus | — | ~3 months (~90 days) | https://forum.colemak.com/topic/1747-typing-speed-progress/ |
| Sabih Sarowar | 125 WPM (max) | 65 WPM @2mo; 120 WPM @1yr | https://medium.com/@irisman/the-peak-programming-keyboard-and-key-layout-57cded217236 |

**Explicit "time to usable speed (~40–50 WPM)" data points:**
- engiwengi: 50 WPM @~1 week (heavy practice) — https://forum.colemak.com/topic/2272-my-layout-switching-experience/
- HN user: 40–50 WPM after one weekend (10–20 hrs) — https://news.ycombinator.com/item?id=36005823
- Alex Gustafson: 45 WPM @5 days (Typing Club) — https://alexjgustafson.blog/2016/01/30/switching-to-colemak/
- Getreuer (own progression): 40 WPM @1 month — https://getreuer.info/posts/keyboards/alt-layouts/index.html
- Mac Merritt: 50 WPM @1 month — https://www.linkedin.com/posts/macmerritt_techlife-productivityhacks-softwareengineering-activity-7263268918885007361-zHsj
- Garrett Leber: 40 WPM @2 months (keybr) — https://garrettleber.com/blogs/ergo-keyboards-are-fun/
- Silvestri: 30 WPM @2 weeks — https://www.silvestri.cloud/blogs/redox-build-part-three/
- Tim Wade: 30 WPM "acceptable", then 50–60 — https://timjwade.com/2017/07/01/adventures-in-colemak.html

**Central estimate.** For **time to regain former QWERTY speed**: the explicit data points cluster around **2–3 months** (range ~2 weeks for fast learners with heavy practice, up to ~5–6 months). Simple average of the 6 explicit "former-speed" points {~1, ~1.5, 5, 3, 3, 3} months ≈ **2.8 months** (n=6). For **time to a usable ~40–50 WPM**: roughly **1–4 weeks** (n≈8).

**Representativeness caveat (explicit):** n is small (~6–8 explicit data points for each metric), all self-selected from people who chose to write about it, and heavily skewed toward those who *succeeded* (people who quit usually don't post a timeline). Practice volume varies enormously (30 min/day vs 2 hr/day), which is the single biggest driver of the spread. **Do not treat the ~2.8-month average as a guarantee** — treat it as "most people who stick with it report regaining QWERTY speed in roughly 2–3 months, with a wide range."

---

## 7. Does it work for everyone? — failure cases and abandonment

**Who it does NOT work for / reasons people abandon:**
- **Vim/shortcut users who won't remap.** Losing HJKL and positional-vs-mnemonic shortcuts is a recurring deal-breaker. (HN user; Luke Brannagan's "sacrificed Vim muscle memory"; BeerRiot's vim concerns) Sources: https://news.ycombinator.com/item?id=36005823 , https://www.linkedin.com/posts/luke-brannagan_switching-from-qwerty-to-colemak-dh-a-journey-activity-7429155174734131200-MogZ , https://blog.beerriot.com/2024/10/19/learning-colemak-dh/
- **People who must use shared/QWERTY machines.** One HN user switched back after a job required a shared QWERTY computer and hated "finger pecking like a complete n00b"; 15 years later still on QWERTY with wrist guards and RSI. Another switched back to QWERTY after 6 years citing "convenience of qwerty being there everywhere." https://news.ycombinator.com/item?id=36005823 , https://maudlinruminations.com/posts/colemak_6years.html (cited via HN; direct fetch failed)
- **Impatience with the slow phase.** Muirium quit at ~20 WPM after a week; Protesilaos quit after ~3 weeks unconvinced of comfort benefit. Sources: https://deskthority.net/viewtopic.php?p=515790 , https://protesilaos.com/keeb/2024-05-18-colemak-layout-lessons/
- **People who find the layout itself uncomfortable.** One HN user (5–10 years ago, ~1 year on Colemak) found it "rather uncomfortable" and his WPM dropped ~25%; he preferred QWERTY's hand alternation. https://news.ycombinator.com/item?id=36005823
- **DH-vs-vanilla switchers.** One user went back to **vanilla Colemak** after ~100 hours on DH because of top/bottom-row jumping and the "sloping home row." https://forum.colemak.com/topic/2739-why-i-switched-back-to-colemak-again/
- **People whose RSI is not layout-driven.** Protesilaos concluded his problem was ulnar deviation from standard keyboard design, not QWERTY; a split columnar keyboard fixed it, and he saw "minimal" RSI benefit from the layout. Mac Merritt similarly found "RSI improvement seems minimal compared to my ergonomic keyboard switch." Sources: https://protesilaos.com/keeb/2024-05-18-colemak-layout-lessons/ , https://www.linkedin.com/posts/macmerritt_techlife-productivityhacks-softwareengineering-activity-7263268918885007361-zHsj
- **People who can't maintain QWERTY + Colemak simultaneously.** Many report QWERTY fluency degrades; some can context-switch (esp. if they weren't QWERTY touch-typists), others can't. (multiple sources)
- **Caveat:** learning a new layout is itself "literally repetitive stress" — BeerRiot warns against doing it during an active RSI/carpal-tunnel flare-up. https://blog.beerriot.com/2024/10/19/learning-colemak-dh/

**Bottom line:** it works for a large share of people who (a) have a real comfort/RSI motivation, (b) can tolerate weeks of slowness, and (c) either don't depend on Vim's default keys or are willing to remap. It fails for people who can't tolerate the slow phase, must live on shared QWERTY machines, or whose pain is caused by keyboard *hardware* rather than layout.

---

## 8. The common experience (consensus view)

The typical adoption story, synthesized across sources:
1. **Motivation:** usually wrist/finger fatigue or RSI, sometimes curiosity/optimization; rarely pure speed (and speed is explicitly *not* the point — Getreuer and others stress layout ≠ speed).
2. **The plunge:** most go cold turkey (or use Tarmak for a gentler ramp); the first days–weeks are a brutal speed collapse (often to <20 WPM) with constant QWERTY muscle-memory fighting.
3. **The grind:** daily practice (keybr/monkeytype/10fastfingers/Amphetype); usable ~40–50 WPM typically in 1–4 weeks; a mid-term "am I stuck?" dip around 1–3 months is common.
4. **The payoff:** regaining former QWERTY speed in roughly 2–3 months (wide range), with the real, durable win being **comfort** — reduced fatigue and, for many, RSI relief that persists for years.
5. **Long-term:** most who stick with it stay for years and report speed equal-to-slightly-better than QWERTY plus much better comfort; the main long-term cost is degraded QWERTY fluency on shared machines.
6. **The honest caveat:** a meaningful minority quit (impatience, Vim, shared machines, or finding it no more comfortable), and several experts argue the *hardware* (split/columnar keyboard, posture) matters more than the layout.

---

## 9. Ecosystem

- **Official/authoritative:** colemak.com (official Colemak; notes Colemak is "3rd most popular layout… pre-installed on Windows, Mac and Linux"; Windows 11 24H2+ and Mac/Linux ship it; links Mod-DH as the unofficial variant) https://colemak.com/ ; colemakmods.github.io/mod-dh/ (canonical Mod-DH site, compare tool, downloads) https://colemakmods.github.io/mod-dh/compare.html ; DreymaR's Big Bag of Keyboard Tricks (Angle/Wide/Curl mods, Tarmak, implementations for Win/Linux/TMK) https://dreymar.colemak.org/ergo-mods.html
- **OS support:** Colemak-DH available for Windows, Linux, macOS. Windows: AutoHotKey scripts, OS-level installers (e.g. urob/colemak-win via MSKLC), DreymaR's PKL. Linux: xkeyboard-config (≥2.34), xmodmap, kbd console maps, EurKEY. macOS: contributed mappings + `brew install --cask colemak-dh` / `colemak-dhk`. Cross-platform: kmonad, Kanata. Sources: https://colemakmods.github.io/mod-dh/keyboards.html , https://github.com/urob/colemak-win , https://github.com/ColemakMods/mod-dh
- **Learning tools:** **Tarmak** (incremental 2–5-step transition; Tarmak-DH variants exist for Mac/ANSI) https://github.com/shelbyd/tarmak , https://github.com/Caffa/Tarmak-DH-Mac ; **keybr.com** (most-recommended for learning), **monkeytype.com** (speed/stats), **10fastfingers**, **Amphetype** (focused lessons), **Typing Club**, **The Typing Cat**, **gtypist** (CLI), **keyzen-colemak**, **zentyping**. (multiple sources above)
- **Vim support:** several remap plugins exist — drewherron/colemak-vim, ~ashie/colemak_dh.vim, NightEel/Vim-configuration-for-Colemak-DH-ISO. Sources: https://github.com/drewherron/colemak-vim , https://git.sr.ht/~ashie/colemak_dh.vim , https://github.com/NightEel/Vim-configuration-for-Colemak-DH-ISO
- **Community size:** Colemak is the 3rd most popular layout (after QWERTY and Dvorak) and pre-installed on major OSes; Colemak-DH is the most popular *mod* and is ubiquitous in the custom/ergo keyboard community (Miryoku, many QMK/ZMK configs default to it). But absolute numbers are tiny — typingbattles estimates **<1% of typists** use Colemak, and DH is a subset of that (estimate-grade). https://colemak.com/ , https://www.typingbattles.com/blog/colemak-dh-typing-practice-what-changing-from-qwerty-is-really-like
- **Community/maintenance:** active forum (forum.colemak.com), r/Colemak, r/ErgoMechKeyboards, r/KeyboardLayouts, Discord, and the ColemakMods GitHub org. The mod is public-domain and actively maintained (revision history through 2020). https://github.com/ColemakMods/mod-dh
- **Resources for programmers:** symbol-layer designs (Getreuer's "Designing a Symbol Layer", Miryoku, Pnohty for Python, ratoru's keymap) and vim-friendly layer setups. Sources: https://getreuer.info/posts/keyboards/alt-layouts/index.html , https://ratoru.com/blog/layout-customizing/ , https://oppi.li/posts/programming_on_34_keys/

---

## Key sources (most authoritative)
1. https://colemakmods.github.io/mod-dh/ — canonical "what it is" (origin, changes, DHk/DHm history, Angle/Curl)
2. https://getreuer.info/posts/keyboards/alt-layouts/index.html — layout metrics + realistic time-to-speed estimates
3. https://forum.colemak.com/topic/2272-my-layout-switching-experience/ — detailed first-person timeline (engiwengi)
4. https://forum.colemak.com/topic/1747-typing-speed-progress/ — community consensus on ~3-month recovery
5. https://news.ycombinator.com/item?id=36005823 — many long-term + failure-case anecdotes
6. https://vale.rocks/posts/typing-systems — clean, data-backed 1-year timeline (Monkeytype CSV)
7. https://protesilaos.com/keeb/2024-05-18-colemak-layout-lessons/ — dissenting view (switched back; hardware > layout)
8. https://deskthority.net/viewtopic.php?p=515790 — Tarmak + early-stage + abandonment anecdotes

## Anomalies / dead ends
- **Reddit threads (r/Colemak, r/ErgoMechKeyboards) could not be fetched directly** (403 / empty HTML). Reddit-derived claims in this report are backed only by search-snippet evidence and are marked as such; the two most-cited threads ("Will I be able to reach my current QWERTY speed", "Colemak vs Colemak-DH") were not read in full.
- maudlinruminations.com/posts/colemak_6years.html (6-year switch-back) failed to fetch directly; its content is cited only via the HN thread that quotes it.
- SearXNG returned nothing for several targeted queries (vim/coding, switched-back); the Exa-backed `websearch` fallback was used for those.
- No reliable data found on exact Colemak-DH *user counts*; the <1% figure is estimate-grade from a typing-site blog.
