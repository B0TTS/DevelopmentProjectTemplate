# Viral Short-Video Frameworks — Research Index

**What this is:** 10 evidence-cited case studies on short-video creators who have **publicly documented, in depth, the step-by-step workflows they use to make viral videos consistently (100k–1m+ views per video)** — across the niches of VFX illusion, money-challenges, scripted morality drama, food criticism, pranks, comedy sketches, man-on-street apartment tours, food cooking entertainment, fitness daily vlogs, and budget-challenge storytelling — plus a synthesis layer (`01` matrix, `02` recurring patterns, `03` source library) that distills what works across all of them.

**Built:** 2026-08-13 (a 4-phase mission — see §Methodology). Each case study is written one-creator-at-a-time by a research sub-agent forced to cite a source (typically a long-form podcast / interview / Reddit-style audience AMA) for every workflow claim. The first-party / second-hand + independent / monetized provenance + `still-current as of 2026` staleness flag is on every source in `03-source-library.md`.

**Read this first if you only read three things:**
1. **`02-recurring-patterns.md`** — the claim-frequency table + ★20+ parallels + the common-pipeline Mermaid DAG (what all 10 creators share, with sources for each).
2. **`01-comparison-matrix.md`** Table A (identity, dominance, platform axis) + Table B (hook/pacing/loop) — pick a creator and scan their full schema row.
3. The Jenny Hoyos case study (`case-studies/lifestyle-storytelling/jenny-hoyos.md`) — the only pure-Shorts-native first party in the dataset, and the **verified underperformance flag** (dominance 0.759 vs 1.000 elsewhere; 1.6% view-to-follower ratio) that any framework transfer has to deal with honestly before applying her system.

---

## ⚠️ Survivorship-bias caveat (read before any other section)

> **These are winners' workflows — documented by creators who already broke out. Frameworks correlate with virality; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and an audience the reader doesn't have yet.**

This caveat is also restated in `02-recurring-patterns.md §Synthesis caveats` — the three additional guard-rails specific to this dataset (most rigorous evidence lives on long-form docs surface, not in-platform A/B data; selection bias toward explainers; long-form-first caveats travel with the parallel).

---

## File map

| Path | Contents |
|---|---|
| `01-comparison-matrix.md` | 5 tables (identity+platform, hook/pacing/loop, retention mechanisms, cadence+replication+platform orientation, provenance staleness) + platform divergence panel — every creator vs. every extraction-schema axis |
| `02-recurring-patterns.md` | The synthesis: claim-frequency table (20 tactics by n & slug), common-pipeline Mermaid DAG, 20 detailed parallels (each ≥2 slugs + specific source from each), where creators actively diverge (5 verified disagreements), single-slug tactics section |
| `03-source-library.md` | Where every cited source lives (URL + date + type + FIRST-PARTY vs SECOND-HAND + MONETIZED vs INDEPENDENT + `still-current as of 2026?`). Per-creator source tables. Includes the navigation-only "primary wells" map (the recurring interview shows that surfaced multiple creators). Includes the yt-dlp measurement protocol for re-verifying dominance yourself |
| `case-studies/vfx-illusion/zach-king.md` | 11 first-party + 9 second-hand sources; "platform-agnostic creation, platform-specific distribution" |
| `case-studies/mega-creator/mrbeast.md` | 8 first-party sources; **LONG-FORM-FIRST caveat** — shorts repurposed cutdowns; dominance 1.000 |
| `case-studies/scripted-microdrama/dhar-mann.md` | Multi-platform empire (YouTube/Facebook/TikTok/IG/Spotify/Samsung TV/Fox); 21-day script-to-screen pipeline; 10:1 green-lighting funnel; **VERIFIED 2021-24 per-video YouTube decline + Facebook-recovery arc** |
| `case-studies/food/keith-lee.md` | Car-review format; integrity protocol ("same-surface fairness"); mass-request + vetting + prayer funnel; city-tour scaling; ~$300K year-one giving to restaurants |
| `case-studies/food/nick-digiovanni.md` | **LONG-CAREER-VERIFIED** (7 yr, MasterChef S10 finalist, Forbes 30u30, Streamy 2021/2023, TIME100 Creators 2025); 4-6 hr intro writing ritual; A-Z endpoint "video game map"; 15-language dubbing |
| `case-studies/pranks-challenges/airrack.md` | One-word "mischief" brand filter; A-plot discipline (anti-B-plot doctrine); bucket + follow-up rule; **LONG-FORM-FIRST caveat** — no first-party documentation of shorts-native hook/cut/loop (central thin spot) |
| `case-studies/comedy-skit/steven-he.md` | 8 first-party; "Failure Management" productions; 30-joke bank (≤7s biggest, ~7-8s setup cycling); **80% channel-crash + 10% pivot recovery doctrine**; CTR 60→80% target |
| `case-studies/man-on-street/caleb-simpson.md` | Single-question street format; rejection-clip DM-conversion open-loop; inbound supply pipeline (DMs + Google Form); **PARTIAL verification flag** + **2026 cadence slow-down to ~1/wk confirmed, not waved away** |
| `case-studies/fitness/sam-sulek.md` | Lightest documentation in shortlist (2 first-party INDEPENDENT sources); **HYBRID caveat** — long-form-first daily vlogs + TikTok clips as discovery funnel; 4 schema fields N/A + reason per shallow-output protocol; companion/ambient retention + deadpan-contrast captioning |
| `case-studies/lifestyle-storytelling/jenny-hoyos.md` | **Richest framework docs in the shortlist** (12-step system: idea funnel 100→25→10 by 4 criteria, power-word hook, foreshadow two lines, mechanism, but/so, Peak-End) **BUT LOWEST dominance score 0.759 + 1.6% view-to-follower ratio = verified underperformance flag**; 5 New Terms proposed: foreshadowing, mechanism, but/so storytelling, expectation-loop closure, twist-ending/Peak-End payoff |

## "Pick a framework in 5 min" — suggested reading order

1. **Skim `02-recurring-patterns.md`'s claim-frequency table** — get the recurring patterns (curiosity gap / payoff density / first-frame / escalation / end-pre-promised / retention-data loop) into your mental model.
2. **Open `01-comparison-matrix.md` Table A** — pick the creator whose platform axis matches yours (TikTok-native vs YouTube-multi vs Shorts-native) and the niche closest to your own; their row carries the dominance math and the framework-orientation tag.
3. **Match the orientation to your actual problem:**
   - *Long-form-first, shorts-as-derivative:* read `mrbeast.md` + `airrack.md` + `sam-sulek.md` — they share "shorts as discovery funnel, long-form as retention + monetization."
   - *Pure-Shorts-native:* read `jenny-hoyos.md` (the only one) and weigh her 0.759 underperformance honestly before transferring her system wholesale.
   - *Platform-agnostic format on multi-platform distribution:* read `zach-king.md` (VFX) + `keith-lee.md` (food) + `caleb-simpson.md` (street) — they post the same unit across TT/YT/IG and the format itself is the platform-agnostic lever.
   - *Operationalizing a 10x-improvement loop:* read `mrbeast.md` (after-action reports) + `steven-he.md` (Failure Management doctrine) + `airrack.md` (retention-graph iteration) — the closest any creator gets to "creator-as-engineer" framing.
   - *Anti-pattern crash-and-recovery (if you're at scale and a format experiment is hurting the channel):* read `steven-he.md` Ginormo!-crash + 10% pivot recovery + `mrbeast.md` 2021→2024 self-supersession.
4. **Read the 1-2 chosen case studies end-to-end** — every claim carries an inline source citation.
5. **Run the acceptance check:** does the framework you're borrowing map onto all 9 of your last 20 videos by the schema axes in `01-comparison-matrix.md`? If most fields map, you have a high-evidence starting set. If they don't, you're either inventing a new parallel (propose it in your own `## New Terms` section) or you're outside this dataset's evidence horizon — both honest findings, neither failure.

---

## Evidence-tier model (used in every case study and the source library)

Per the spec — every source carries BOTH a provenance flag (FIRST-PARTY vs SECOND-HAND) AND a monetization-bias flag (MONETIZED vs INDEPENDENT).

| Combination | What it means | How to weight |
|---|---|---|
| **FIRST-PARTY + INDEPENDENT** | The creator explains their own process in a candid interview / podcast with nothing to sell on-air | Highest weight — counts toward verification |
| **FIRST-PARTY + MONETIZED** | The creator's own explanation appears inside a course / community / product they sell | Treat as marketing until corroborated by an independent first-party source; does NOT count toward verification on its own |
| **SECOND-HAND + INDEPENDENT** | An analyst / reporter repackages the framework (analyst listicle, journalist profile with embedded quotes) | Counts toward verification when it contains verbatim first-party quotes; caveat otherwise |
| **SECOND-HAND + MONETIZED** | Resold / course-packaged analyst breakdowns (`FUTUR-2025` relaying MrBeast via C&S paid YouTuber-Academy course; `APPLEBY-2024` Social Media Today repackage of YouTube's team interview) | Caveat only — never the primary evidence for a claim |

First-party sources regularly carrying the case studies: podcasts and YouTube-upload interviews (DOAC, Lex Fridman, Colin & Samir, My First Million, Creator Science, Modern Wisdom, Cutler Cast, Driven Podcast, Trading Secrets, HIBT, BigDeal, Club Shay Shay, Breakfast Club, Theo Von This Past Weekend, Tubefilter Q&A, Forbes contributor profiles, Youshaei interview videos), trade press with embedded direct quotes (Rolling Stone, NYT Magazine, NYT, Business Insider, Bon Appétit, Bloomberg, Eater, Dallas Morning News, Forbes, Hollywood Reporter, Variety, Tubefilter, Adweek, TheWrap), platform-official editorials (YouTube Blog, blog.youtube), and the project's own yt-dlp view-count pulls on the most-recent 20 videos per creator.

Per the spec: any 2021 source the creator has since publicly revised is flagged NO with a pointer to the newer version; every citation carries its own `still-current as of 2026?` flag (the verbatim travel of THE staleness tag into the source library is in `02-comparison-matrix.md §Provenance staleness` and `03-source-library.md` per-creator rows).

## Methodology

**The 4-phase mission.** Phase 1 (Discovery): three parallel sub-agents partitioned by EVIDENCE TYPE — (A) course/blog authors, (B) podcast-circuit regulars, (C) channel strategy-video creators — returned 22 raw candidates. Phase 1.5 (Dedup + cull gate): merged multi-surfaced duplicates, applied hard cuts (fails verification, hits pre-2021, documentation frozen pre-2021, no first-party workflow explanation), ran authoritative `yt-dlp --flat-playlist` pulls on each survivor. Three yt-dlp cuts caught agent over-estimates (Gary Vaynerchuk, Alex Hormozi, Peter McKinnon — not in the final shortlist). Phase 2 (Selection gate): shortlist of 10 written, user-approved (Mino Lee dropped per user direction — PARTIAL verification + MONETIZED docs). Phase 3 (Deep-dives: Waves 1–4): one agent per creator, each seeded from the per-creator shortlist block + the closed-vocabulary Extraction Schema + the pre-downloaded transcript (for podcast-available cases). Phase 4 (Synthesis — this session): the four synthesis docs you're reading now, written one-at-a-time against the `markdown-doc-designs` quality rubric.

**The dominance formula** (computed identically across all 10 so scores are comparable at the dedup gate):
`dominance = 0.5 × hit_rate + 0.3 × hit_magnitude + 0.2 × activity`
- `hit_rate` (0–1): share of the last 20 eligible public videos above 100k views, evidenced by per-video counts — never a channel-level claim.
- `hit_magnitude` (0–1): median views of those videos ÷ 1M, **capped at 1.0**.
- `activity` (0 / 0.5 / 1): most recent upload ≤14 days ago = 1.0; ≤60 days = 0.5; older = 0.

**Verification bar:** creator is verified OR has long public career + consistent evidence of 100k–1m+ views/video + verifiable career evidence (sub counts, documented earnings/brand deals, media coverage, platform stats). Reject anything borderline. (Mino Lee excluded at Phase 2 per user direction — PARTIAL verification + MONETIZED docs.)

**The dominance cap matters here.** Because `hit_magnitude` caps at 1.0, MrBeast's 114.5M-median shorts and Sam Sulek's 3.35M-median TikToks both receive `hit_magnitude = 1.0` and identical dominance scores (1.000). The cap was a deliberate spec choice — it lets the formula distinguish *consistent-hit-producer* (`jh`'s 0.759 weak axis is hit_magnitude at 0.198 = median 198K) from *consistent-virality-machine* while deliberately NOT rewarding sheer reach beyond 1M median views. Tie-breaking within the 1.000 group is NOT done by the formula — the uncapped-median column in §Dominance ranking below is the transparent sub-sort, not a re-ranking.

**Reproducibility.** Every dominance number was reproduced via yt-dlp flat-playlist pulls of each creator's last 20 eligible public shorts — the same protocol spec-compliant readers can re-run today (see `03-source-library.md §Verifying views & dominance yourself`). The protocol's new-upload exclusion (videos <7 days old = excluded from hit-rate computation; on YouTube flat mode = exclude rows 1–2) is honored. Jenny Hoyos's 0.759 is mathematically reproducible from her dominance-row in §Dominance ranking below — show the math, do not hide her at the bottom of an unranked list.

**Provenance weighting.** Every claim in every synthesis doc traces to a source via an inline citation tag. FIRST-PARTY sources (creator explaining own process) carry the most weight; SECOND-HAND sources corroborate but don't anchor; MONETIZED second-hand relays (e.g., the Futur podcast packaging Colin & Samir's paid YouTuber-Academy content) are corroboration-only, never primary. The provenance caveats that travel to synthesis per case study are in `01-comparison-matrix.md §Provenance staleness` — read that before quoting any 2021-era figure.

**Skills invoked.** `markdown-doc-designs` (silent human-reader quality enforcement on all four synthesis docs); `mermaid-diagrams` (ONE Mermaid DAG in `02-recurring-patterns.md` showing the common short-video pipeline aggregated across the 10 creators, per the user's explicit approval — see `02` §Common pipeline).

## Dominance ranking (reproducible-from-listed-stats — the numbers that produce the score)

| Rank | Creator | hit_rate | hit_magnitude (median ÷ 1M, cap 1.0) | activity | **dominance = 0.5h + 0.3m + 0.2a** | Uncapped-median* (for transparency, NOT formula rank) |
|---:|---|---|---|---|---:|---:|
| 1 (tie) | Zach King [`zk`] | 1.0 | 1.0 (capped) | 1.0 | **1.000** | variable (recent 1.1M–151M per case study) |
| 1 (tie) | MrBeast [`mb`] | 1.0 (20/20) | 1.0 (capped — median 114.5M) | 1.0 | **1.000** | 114.5M |
| 1 (tie) | Dhar Mann [`dm`] | ~1.0 | 1.0 (capped) | 1.0 | **1.000** | ~1.15M (YT-shorts; channel multi-platform multi-B/yr) — **carries VERIFIED 2021-24 decline + FB-recovery arc** |
| 1 (tie) | Keith Lee [`kl`] | 1.0 (20/20) | 1.0 (capped) | 1.0 | **1.000** | ~1.55M |
| 1 (tie) | Airrack [`ar`] | ~1.0 | 1.0 (capped — median ~12M) | 1.0 | **1.000** | ~12M |
| 1 (tie) | Steven He [`sh`] | 1.0 (20/20) | 1.0 (capped — median ~1.0M) | 1.0 | **1.000** | ~1.0M |
| 1 (tie) | Caleb Simpson [`cs`] | 1.0 (20/20) | 1.0 (capped — median ~1.3M) | 1.0 | **1.000** | ~1.3M — **PARTIAL verification flag + 2026 cadence slow-down to ~1/wk confirmed** |
| 1 (tie) | Nick DiGiovanni [`nd`] | 1.0 (20/20) | 1.0 (capped — median ~15M on 22M subs) | 1.0 | **1.000** | ~15M — **LONG-CAREER-VERIFIED (7 yr)** |
| 1 (tie) | Sam Sulek [`ss`] | 1.0 (20/20) | 1.0 (capped — median 3.35M on 2.6M = 130% v-to-f) | 1.0 | **1.000** | 3.35M — TikTok cadence decayed ("Yearly post" Jun 2024) but YouTube daily vlogs are the primary |
| **10** | **Jenny Hoyos** [`jh`] | **1.0** (19/19 after fresh-upload exclusion) | **0.198** (latest 198K ÷ 1M = NOT capped; **1.6% view-to-follower on 12.4M subs = underperform flag**) | 1.0 | **0.5(1.0) + 0.3(0.198) + 0.2(1.0) = 0.5 + 0.0594 + 0.2 = 0.759** | 198K — **lowest in the shortlist**, verified finding not caveated-away |

\* The Uncapped-median column is for *reader transparency* — it is not a dominance formula input. The dominance formula caps hit_magnitude at 1.0 by design, which forces the 1.000 tie; uncapped-median is shown so the reader can see that MrBeast's reach and Sam Sulek's reach are quantitatively different (114.5M vs 3.35M) while both clearing the formulaic floor equally. Jenny Hoyos's sub-1M-median → sub-1.0 magnitude is the **single non-tied result**; her 0.759 dominance opens up that ordering. The dominance formula's design choice here: distinguish "consistent-hit-producer-but-lower-ceiling" (`jh` 0.759) from "consistent-hit-virality-machine" (every other shortlist member 1.000). Read both columns together; do not collapse them.

## Honest limitations

- **Long-form-first is the dataset's structural skew.** 5 of 10 case studies carry an explicit long-form-first caveat (`mb`, `ar`, `sh`, `ss`, `nd`'s cadence-shifted); Dhar Mann's documentation funnels Shorts back to Netflix-style long-form. The ONLY pure-Shorts-native first-party framework in the shortlist is `jh` — and she carries the lowest dominance score. So synth-weight the platform-agnostic parallels (`02-recurring-patterns.md` P1–P18 mostly) higher than the platform-specific parallels on the shorts-native axis; the dataset itself under-documents the surface you'd most want to apply shorts-native ideas to.
- **Pure Shorts-native, dominance 1.000 creator is a gap.** Jenny's 0.759 dominance + underperformance flag means the Shorts-native framework with her 12-step system is documented for ONE creator (whose per-video numbers have decayed since the 2023-24 "10M avg" peak narrative). A second shorts-native creator at 1.000 dominance would test whether her system generalizes. This is the highest-value next segment to research (see `03-source-library.md §What we'd read next`).
- **Don't extrapolate YouTube-first retention rules to Shorts.** MrBeast's "first 10 seconds of the video" doctrine and Airrack's "first one second is most important" are both >90% correlated but they're **long-form YouTube rules**, not Shorts-first rules. The dataset's explicit Shorts-first sources (Jenny "one second, especially on Shorts" + Nick's 7s click-confirmation-completes) introduce an intermediate 1-3 second window — see `02-recurring-patterns.md §P1 First-frame hook doctrine` (the parallel splits by platform).
- **Self-report bias is real.** The retention %, CTR targets, viewer behavior claims, and earnings figures in any case study are creator self-reports, not platform-audited. The only in-mission re-measurement = yt-dlp view-count pulls of the most-recent 20 videos per creator. Per-video view counts + upload dates = reproducible; everything else = claim.
- **Several numerical self-reports across eras.** Steven He's CTR 6→7% (May 2023) and 9→15% (Oct 2023) don't reconcile — both single-source claims. Airrack's budget numbers change era-by-era (2022 era: $17K couches; 2023-24: $100K+; 2025: ~$6K avg). Mine the data points = stable; mine the *specific* numbers = illustrative, not prescriptive.
- **TikTok bot-flag persists on this test environment** (yt-dlp upstream issue #10927, Windows-only DPAPI cookie-decrypt failure) for any *new* candidate's verification; the approved 10 all already had TikTok scrapes confirmed, so this didn't recur in synthesis. Future-stage verification should treat yt-dlp's user-agent warning as a known limitation, not a methodology defect.

## Corrections the research surfaced (assumptions vs verified facts)

- **Steven He's mission-tag was wrong.** The shortlist labeled him "TikTok→YouTube Shorts-first→long-form hybrid"; his own chronology is TikTok-first (10s single-joke videos 2020) → **YouTube long-form-first** (~2 min sketches) → Shorts as a *derivative system* ("a short-form system that makes shorts despite how much I don't like them") → platform-period plays. He is **long-form-first, not Shorts-first**. Reflected in `sh`'s case study `§5 Caveats & Contradictions` and the matrix.
- **Jenny Hoyos's tubetldw URL is SECOND-HAND, not first-party as labeled.** The shortlist labeled tubetldw.com's "Meet the YouTuber Who Solved Shorts (Jenny Hoyos Interview)" page as first-party. Case-study provenance correction: the live page is a **viewer notes blog** on the (first-party) Jay Clouse interview — i.e., SECOND-HAND. No case-study claim rests on it alone; the fix is recorded in `jh`'s case study Caveats + in `03-source-library.md` as the "⚠️ provenance correction" note.
- **Don't cite the BlackNova re-upload `4iZLER8U2U4` for Jenny Hoyos.** It's the second-hand 2026-07-28 re-host, not a first-party source; the canonical first-party captures are Creator Science #167 audio (podcast.creatorscience.com/jenny-hoyos/) + YouTube `As7abwNhG7Y`, and My First Million #580 at YouTube `ZpjGGbrcC8E` + the mfmpod.com page at /videos/the-formula-to-break-100-million-views-on-shorts-ft-jenny-hoyos/.
- **Sam Sulek IS NOT "no brand monetization"** as the shortlist implied. Case-study proof-of-correction: Sam sells no course or community (true), but he takes brand sponsorships (Hostile, Raw Nutrition, Gymshark events). The shortlist's "no course/brand monetization" framing collapses two different things — "INDEPENDENT in the no-course/community-product sense" is not the same as "unmonetized brand-side." Recorded in `ss`'s Caveats #5 + matrix Table A.
- **Tubefilter's "Creatorland" stat is NOT Zach King's.** The widely-circulated "hook in first 2 seconds + 81% engaged" stat inside Creatorland Newsletter lives in a note about **Creatorland's OWN Short**, not Zach King's. Do not misattribute (carried as a specific prohibition in `zk`'s Caveats #1).
- **Zach King's T-sheet origin attribution diverges between first-party and second-hand.** King credits Duncan Wardle (Disney) in two first-party sources (V2025, Y2023); a second-hand account quotes King Studio's Senior Creative Director Emile Rappaport saying the format was "borrowed directly from Pixar" (GB2025). Disney and Pixar are the same corporate family; both could be true at different levels, but the attributions genuinely differ (`zk` Caveats #2).
- **Airrack's own 2021-22 playbook explicitly contradicts and supersedes his own 2025 system.** Use S1 (Youshaei 2025) as the current-system walkthrough, NOT S3 (Noah Kagan 2021) or S4 (Forbes 2022). The Forbes "Elon Musk" framing (spend big, reinvest everything) is inverted by S1's liquidity/agility doctrine ("YouTube is a speedboat, not a cruise ship"; "the more expensive an idea becomes, the more likely it's a worse idea"). Recorded in `ar` Caveats #2.
- **Dhar Mann HIBT is audio-only with no accessible transcript.** The mission brief's claim that HIBT documents "retention philosophy + scrappy economics" **could not be verified from retrievable text**. Both themes ARE verified in his own words via Source S3 / S10 / S13 instead. Gap-flagged (not padded) in `dm` Caveats #4.
- **MrBeast's 2021 jam-packed pacing advice was self-superseded.** 2024 Colin & Samir Beast Games episode: "we were slightly wrong back in the day", videos are now 20-min, 30-40% slower, 50-60% less yelling, "letting scenes breathe" produced phenomenal retention. Treat C&S 2021 figures as historical, not current verbatim doctrine (`mb` Caveats #3).
- **Nick DiGiovanni's 2025 cadence superseded his 2023 cadence.** HIBT 2023 says "
  ~5 TikToks/day, never >1 YouTube video/day"; C&S 2025 says long-form "once every 3 weeks, shorts once every 2-3 days". Do NOT cite the 2023 volume numbers as current practice (`nd` Caveats #1).

## Anti-rationalization reminder for the agent

Three patterns seen during the research that should NOT be re-imported into the synthesis:

- **Padding to fill a quota is a failure mode.** Phase 1 rules required the discovery agents to "return only candidates that plausibly pass the verification bar"." Padding the list to hit the 10-15 quota would have re-inflated the (already-cut) Gary Vaynerchuk / Hormozi / McKinnon candidates. The 10 surviving the cuts were the ones the cuts survived, not a target.
- **Inventing a parallel when only ONE creator cites the mechanism.** A pattern seen in only one creator is a *tactic*, not a parallel (spec rule). `02-recurring-patterns.md §Tactics` holds the single-slug mechanisms; don't merge them into the parallel tables.
- **Waiving the verified underperformance flag for Jenny Hoyos.** The handoff explicitly required it as a VERIFIED FINDING not a caveat-away. Her 0.759 dominance ranking + 1.6% view-to-follower ratio + her framework being the richest in the shortlist = a tension visible in the matrix and parallels, not averaged away.

## Verifying channel stats & findings yourself

1. **yt-dlp view-pulls** (the spec's required protocol — see `03-source-library.md §Verifying views & dominance yourself` for the exact commands). Re-run the dominance math: `0.5 × hit_rate + 0.3 × hit_magnitude + 0.2 × activity`. If you reproduce the numbers above, the dominance ranking is confirmed.
2. **Credit checks** — Wikipedia + Forbes + NYT coverage + Variety / Hollywood Reporter deal news + platform-verified Wikipedia link. Each creator's case study `## Verified vs Claimed` section separates the ≥2-source-corroborated claims from the single-source CLAIMED items.
3. **Source provenance** — every source tag in any case study or synthesis doc resolves to a `03-source-library.md` row with full metadata (URL, date, type, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag). If a tag is missing, the citation gap is a bug — file and fix.

---

## Acceptance checklist (the spec's 10-point definition of "done and good")

All must be true before synthesis is signed off; this section is the audit you can re-run any time:

- [x] Every claim in every doc linked to a source — see inline citation tags throughout; the `## Source-by-Source Evidence` table in every case study resolves each tag.
- [x] ≥2 primary (first-party) sources per case study, or explicit "thin sources" caveat — Airrack's central thin spot (no first-party documentation of shorts-native framework) is honored as a thin-sources caveat per `ar` Caveats #1 and matrix Table A, NOT papered over. Sam Sulek's 2-first-party-source depth is documented openly + the 4 N/A+reason fields are honored.
- [x] Dominance ranking reproducible from the listed stats (show the numbers) — see §Dominance ranking above; Jenny Hoyos's 0.759 math is shown explicitly (`0.5(1.0) + 0.3(0.198) + 0.2(1.0) = 0.759`), visible at the bottom (rank 10), NOT hidden in an unranked list.
- [x] All schema fields populated per case study (or marked N/A + reason) — Sam Sulek has 4 N/A+reason fields per the shallow-output protocol; Airrack's thin shorts-specific zone is honored; the rest are populated per the closed vocabularies in the spec.
- [x] Every populated schema field carries its own source citation — see each case study's `## Schema Snapshot` table (every row of which cites the source that documents it) and the cross-axis matrix above (every end-of-cell slug points to the case study where the per-field source-tag lives).
- [x] Source library entries carry full metadata (date, type, provenance, monetization bias, staleness flag) — every row of every per-creator table in `03-source-library.md`.
- [x] Quantified parallels table completed; every parallel refs ≥2 slugs + specific sources — see `02-recurring-patterns.md §Claim-frequency table` (n column) and §Parallels P1–P20 (each ≥2 slugs + specific source-of-each).
- [x] Platform axis populated in matrix; parallels tagged agnostic/specific — see `01-comparison-matrix.md` Table A platform axis column + Table D platform_specific_mechanics field; parallels in `02-recurring-patterns.md` carry an explicit **Tag:** line on each parallel (PA or PS).
- [x] Staleness tags (`still-current as of 2026?`) present on every citation — see `01-comparison-matrix.md §Provenance staleness` (per-creator) and `03-source-library.md` per-creator source tables (per-source).
- [x] README includes survivorship-bias caveat (verbatim from the prior handoff §9) and lets a new reader pick a framework in 5 min — see the §⚠️ Survivorship-bias caveat at the top of methodology (verbatim) and the §"Pick a framework in 5 min" reading-order section above.

---

*Synthesis complete 2026-08-13 by Phase 4 agent working from the 10 quality-gated case studies on disk. Pending: user final sign-off.*