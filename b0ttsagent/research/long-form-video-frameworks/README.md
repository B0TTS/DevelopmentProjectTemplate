# Long-Form Video Frameworks — Deep-Documented Creator Workflows

**What this is:** A research run (2026-08-29 → 2026-08-30) that identified the 15 most dominant, most consistent, deep-documented long-form YouTube creators, then built 12 full case studies of their workflows from first-party and corroborating sources, and synthesized the cross-creator patterns.

**Read this first if you want the findings:** [recurring-patterns.md](recurring-patterns.md) — 21 patterns built bottom-up from the 12 case studies, each backed by ≥2 creators with linked sources.
**Read this if you want the evidence:** [source-library.md](source-library.md) — every documentation source for all 15 creators, with provenance and currency flags.
**Read this if you want one creator in depth:** [`case-studies/`](case-studies/) — 12 case studies, ~31–81 KB each, every claim linked.

---

## Methodology

> **⚠️ Survivorship bias — read before using anything below.** These are *winners'* workflows. Every creator in this corpus has ≥60% hit rate on their last 12 eligible long-form uploads and a median above 100k views; the run selected for exactly that. Their tactics are therefore **correlated with success in this sample, not proven to cause it** — failed creators used many of the same tactics and are absent by construction. Treat this corpus as a **high-evidence starting set**, not a formula.

### Pipeline (four phases, one cull)

1. **Phase 0 — Discovery (30 candidates).** Pooled candidate list across spectacle, science, commentary, tech, essay, and travel formats; deduped, schema-complete.
2. **Phase 1 — Verification.** Per-creator evidence JSON built from **exact yt-dlp view counts** (not estimates), Wikipedia/press career evidence, and a **documentation gate**: at least one first-party workflow doc inside the recency window.
3. **Phase 1.5 — Shortlist (15).** Cull gate applied: two passing creators were cut for dormancy (thomas-frank — newest upload 890 days old; dan-mace — 274 days) and low hit magnitude; three were rejected outright at Phase 1 (ali-abdaal — 50% hit rate; solar-sands — no in-window first-party workflow doc; dan-koe — 58.3% hit rate).
4. **Phase 2 — Deep dives (12 of 15 completed).** Case studies written per creator; three (tom-scott, colin-and-samir, matt-davella) were **not completed** after repeated subagent crashes — they are ranked below on shortlist evidence only and excluded from pattern analysis.
5. **Phase 3 — Synthesis (this doc set).** Patterns, source library, and this README.

### The verification bar

A creator passes verification only with multi-source career evidence (platform measurements via yt-dlp, Wikipedia infoboxes, press coverage) confirming identity, scale, and years-active. View counts are measured directly per video (`python -m yt_dlp`), never estimated.

### The consistency test

**Hit rate** = the share of the creator's **last 12 eligible long-form videos** exceeding 100,000 views. Very recent uploads are excluded from eligibility (each creator's `excluded_new_uploads` count is in the shortlist) so freshness doesn't masquerade as failure. **The gate is ≥60%.** All 12 case-studied creators and 11 of 15 shortlisted creators hit 12/12; the one exception (colin-and-samir, 10/12 = 0.833) still clears the bar.

### The dominance formula

```
dominance = 0.3 × hit_rate + 0.5 × hit_magnitude + 0.2 × activity
```

- **hit_rate** — 12-eligible hit rate, as above.
- **hit_magnitude** — median views of those 12 eligible videos ÷ 10,000,000, capped at 1.0.
- **activity** — 1.0 if the newest upload is ≤30 days old; 0.5 if ≤90 days; 0.0 beyond that (which is what dormancy-cut the two Phase 1.5 culls).
- **Ties** are broken by documentation recency (newer doc wins) — this decided wendover-productions over tom-scott at 0.543.

### Recency windows and staleness flags

The documentation gate requires workflow docs dated **2021–2026**. Docs outside the window are flagged **stale (NO)** and used only for historical corroboration (e.g., Drew Gooden's 2019 Triangle Talks interview, LTT's 2017/2019 pipeline videos). Where a doc is inside the window but its update extent is unknown, it is flagged **UNCLEAR** (e.g., MKBHD's Skillshare class, Wendover's paywalled Nebula BTS video).

### Provenance flags (used throughout the case studies and source library)

- **FIRST-PARTY vs SECOND-HAND** — first-party means the creator's own words or production (own channel, own site, verified guest appearance). Second-hand docs (press, summaries, AI syntheses) are used only for corroboration and are flagged at every use.
- **MONETIZED vs INDEPENDENT** — monetized docs (sponsored videos, paywalled courses, marketing-adjacent interviews) carry a standing caveat: treat self-reported claims as marketing-adjacent. Nine of the twelve case-studied creators have **no first-party + independent source at all** — their case studies say so explicitly.
- **Verified-vs-claimed** — every case study separates verified facts (measured, corroborated) from self-reported claims (hours, budgets, team sizes, revenue splits are *claimed*, not audited).

---

## The 15 shortlisted creators, dominance-ranked

Scores, inputs, and arithmetic are transcribed verbatim from [`working/shortlist.md`](working/shortlist.md) (which transcribed them from the per-creator evidence JSONs — no recomputation at any step). "Median" = median views of the last 12 eligible long-form uploads.

| # | Creator | Score | Inputs (hit_rate / hit_magnitude / activity) | Arithmetic (as recorded) | Median views | Case study |
|---|---|---|---|---|---|---|
| 1 | **MrBeast** | **1.000** | 1.0 / 1.0 / 1.0 | 0.3×1.00 + 0.5×1.00 + 0.2×1.00 = 1.00 — 12/12 hits; median 111,467,670 ÷ 10M = 11.15, capped 1.0; newest upload 7 days before measurement | 111,467,670 | [mrbeast.md](case-studies/mrbeast.md) |
| 2 | **Mark Rober** | **0.900** | 1.0 / 1.0 / 0.5 | 0.3×1.0 + 0.5×1.0 + 0.2×0.5 = 0.9 — 12/12; median 28,199,830 ÷ 10M = 2.82, capped 1.0; newest upload 70 days (≤90, >30) | 28,199,830 | [mark-rober.md](case-studies/mark-rober.md) |
| 3 | **Airrack** | **0.894** | 1.0 / 0.9885414 / 0.5 | 0.3×1.00 + 0.5×0.9885414 + 0.2×0.5 = 0.8942707 ≈ 0.894 — 12/12; median 9,885,414 ÷ 10M = 0.9885414; newest upload 33 days | 9,885,414 | [airrack.md](case-studies/airrack.md) |
| 4 | **Veritasium** | **0.841** | 1.0 / 0.6817628 / 1.0 | 0.3×1.00 + 0.5×0.6817628 + 0.2×1.00 = 0.8408814 ≈ 0.841 — 12/12; median 6,817,628 ÷ 10M = 0.6817628; newest upload 12 days | 6,817,628 | [veritasium.md](case-studies/veritasium.md) |
| 5 | **Drew Gooden** | **0.735** | 1.0 / 0.4698 / 1.0 | 0.3×1.0 + 0.5×0.4698 + 0.2×1.0 = 0.7349 ≈ 0.735 — 12/12; median 4,697,784 ÷ 10M = 0.4698; newest upload 20 days | 4,697,784 | [drew-gooden.md](case-studies/drew-gooden.md) |
| 6 | **Kurtis Conner** | **0.705** | 1.0 / 0.4103 / 1.0 | 0.3×1.0 + 0.5×0.4103 + 0.2×1.0 = 0.705 — 12/12; median 4,103,208 ÷ 10M = 0.4103; newest upload 15 days | 4,103,208 | [kurtis-conner.md](case-studies/kurtis-conner.md) |
| 7 | **Johnny Harris** | **0.670** | 1.0 / 0.3475773 / 1.0 | 0.3×1.0 + 0.5×0.3475773 + 0.2×1.0 = 0.67378865 ≈ 0.67 — 12/12; median 3,475,773 ÷ 10M = 0.3475773; newest upload 16 days | 3,475,773 | [johnny-harris.md](case-studies/johnny-harris.md) |
| 8 | **MKBHD** | **0.654** | 1.0 / 0.307 / 1.0 | 0.3×1.00 + 0.5×0.307 + 0.2×1.00 = 0.654 — 12/12; median 3,071,970 ÷ 10M = 0.307; newest upload 5 days | 3,071,970 | [mkbhd.md](case-studies/mkbhd.md) |
| 9 | **Linus Tech Tips** | **0.550** | 1.0 / 0.1004889 / 1.0 | 0.3×1.00 + 0.5×0.10 + 0.2×1.00 = 0.55 — 12/12 (8 new uploads excluded); median 1,004,889 ÷ 10M = 0.1005; newest upload 0 days | 1,004,889 | [linus-tech-tips.md](case-studies/linus-tech-tips.md) |
| 10 | **Wendover Productions** | **0.543** | 1.0 / 0.0859858 / 1.0 | 0.3×1.0 + 0.5×0.0859858 + 0.2×1.0 = 0.5429929 ≈ 0.543 — 12/12; median 859,858 ÷ 10M = 0.0859858; newest upload 4 days. *Tie with tom-scott broken by newer documentation* | 859,858 | [wendover-productions.md](case-studies/wendover-productions.md) |
| 11 | **Tom Scott** ⚠️ | **0.543** | 1.0 / 0.0864985 / 1.0 | 0.3×1.00 + 0.5×0.0864985 + 0.2×1.00 = 0.54324925 ≈ 0.543 — 12/12; median 864,985 ÷ 10M = 0.0864985; newest upload 5 days | 864,985 | **No case study** — ranking on shortlist evidence only |
| 12 | **Mina Le** | **0.527** | 1.0 / 0.0530018 / 1.0 | 0.3×1.00 + 0.5×0.0530018 + 0.2×1.00 = 0.5265009 ≈ 0.527 — 12/12; median 530,018 ÷ 10M = 0.0530018; newest upload 3 days | 530,018 | [mina-le.md](case-studies/mina-le.md) |
| 13 | **Ryan Trahan** | **0.516** | 1.0 / 0.2323887 / 0.5 | 0.3×1.00 + 0.5×0.2323887 + 0.2×0.50 = 0.51619435 ≈ 0.516 — 12/12; median 2,323,887 ÷ 10M = 0.2323887; newest upload 42 days | 2,323,887 | [ryan-trahan.md](case-studies/ryan-trahan.md) |
| 14 | **Colin and Samir** ⚠️ | **0.460** | 0.833 / 0.0197541 / 1.0 | 0.3×0.833 + 0.5×0.0197541 + 0.2×1.00 = 0.45987705 ≈ 0.460 — 10/12 hits (0.833, still above the 60% gate); median 197,541 ÷ 10M = 0.0197541; newest upload 10 days | 197,541 | **No case study** — ranking on shortlist evidence only |
| 15 | **Matt D'Avella** ⚠️ | **0.428** | 1.0 / 0.0556073 / 0.5 | 0.3×1.0 + 0.5×0.0556073 + 0.2×0.5 = 0.4278037 ≈ 0.428 — 12/12; median 556,073 ÷ 10M = 0.0556073; newest upload 53 days | 556,073 | **No case study** — ranking on shortlist evidence only |

**⚠️ = incomplete.** Tom-scott, colin-and-samir, and matt-davella passed every gate and belong in this ranking, but their Phase 2 deep dives were not completed (repeated subagent crashes closed the phase early — see [`working/MANIFEST.md`](working/MANIFEST.md)). They are included here and in the [source library](source-library.md) from shortlist metadata, and **excluded from every pattern claim** in [recurring-patterns.md](recurring-patterns.md).

**Not listed (cut/rejected at Phase 1.5):** thomas-frank (dormant 890 days), dan-mace (dormant 274 days), ali-abdaal (50% hit rate), solar-sands (no in-window first-party doc), dan-koe (58.3% hit rate). Their full records are in [`working/shortlist.md`](working/shortlist.md).

---

## Pick a framework in 5 minutes

Which case study to read first, depending on what you're trying to fix. Every mapping below reflects what that document actually contains (each case study marks undocumented steps as "thin" rather than padding them).

| You want to fix… | Read first | Why (what's actually in the doc) |
|---|---|---|
| **Hooks & packaging** | [veritasium.md](case-studies/veritasium.md) | The promise-not-label doctrine, 20–50 thumbnail options, native A/B/C testing, and the asteroids 10x title/thumbnail rework story. Then [mrbeast.md](case-studies/mrbeast.md) for the pre-shoot "critical components" rule and [ryan-trahan.md](case-studies/ryan-trahan.md) for thumbnails-finished-before-filming. |
| **Retention** | [mrbeast.md](case-studies/mrbeast.md) | The only full retention doctrine in the corpus: CTR/AVD/AVP triad, first-minute loss math, minute-mark architecture with 3/6-minute re-engagements, abrupt endings. Pair with [drew-gooden.md](case-studies/drew-gooden.md) for the opposing "respect the viewer's time" ethic if you find the MrBeast model distasteful. |
| **Structure** | [johnny-harris.md](case-studies/johnny-harris.md) | The most prescriptive: problem→solution never thesis→evidence, action-first opens, two-voice pacing, the full 4-month pipeline. For serialized formats, [ryan-trahan.md](case-studies/ryan-trahan.md) (Double Arc + repeatable segments) and [airrack.md](case-studies/airrack.md) ("A-plot = title"). |
| **Editing rhythm** | [mark-rober.md](case-studies/mark-rober.md) | "Story is found in the edit": shoot with bullet points, film the intro last, 200 hours → 10 minutes. Then [kurtis-conner.md](case-studies/kurtis-conner.md) (editing as re-arrangeable writing blocks) and [mina-le.md](case-studies/mina-le.md) (meme-splice density for information-heavy essays). |
| **Cadence** | [wendover-productions.md](case-studies/wendover-productions.md) | Every 2 weeks for 11 years — the purest sustainability-through-regularity case. Also [mkbhd.md](case-studies/mkbhd.md) (1.5/week ideal + the January-experiment/August-lock "playoffs"), [ryan-trahan.md](case-studies/ryan-trahan.md) (event mode vs bread-and-butter), and [linus-tech-tips.md](case-studies/linus-tech-tips.md) if you want the opposite extreme (a 17/week factory). |
| **Team workflow** | [linus-tech-tips.md](case-studies/linus-tech-tips.md) | The most complete operations doc anywhere in the corpus: writer's meeting → script review → ready-to-shoot checklist → ingest → edit → 3-deep QC, with monday.com status automation. Then [mkbhd.md](case-studies/mkbhd.md) (octopus delegation, Notion stack, one-room studio) and [johnny-harris.md](case-studies/johnny-harris.md) (25-person freelance pipeline with info docs and Frame.io note chains). |
| Research depth *(bonus)* | [mina-le.md](case-studies/mina-le.md) | Read-every-article doctrine, JSTOR/NYPL, and the print-and-floor-sort synthesis ritual. Then [johnny-harris.md](case-studies/johnny-harris.md) for the 60–80-page info doc and public source dock. |
| Budget discipline *(bonus)* | [airrack.md](case-studies/airrack.md) | "The more expensive an idea becomes, it's usually a worse idea" — the $100K-era vs <$10K-era comparison, fixed-cost scars. Then [ryan-trahan.md](case-studies/ryan-trahan.md) for low-overhead production (borrowed gear, iPhone-native). |
| Burnout & longevity *(bonus)* | [mark-rober.md](case-studies/mark-rober.md) | The treadmill/jogging metaphor, Super Mario Effect, stay-employed/self-fund logic. Also [veritasium.md](case-studies/veritasium.md) for the precariousness thesis (it's income uncertainty, not hours) and [drew-gooden.md](case-studies/drew-gooden.md) / [mina-le.md](case-studies/mina-le.md) for solo-creator life-separation tactics. |
| You're a solo creator *(bonus)* | [drew-gooden.md](case-studies/drew-gooden.md) | The fully-solo reference: everything in-house, one video a month, recharge built in. Also [kurtis-conner.md](case-studies/kurtis-conner.md) and [mina-le.md](case-studies/mina-le.md) (team of two). |

**One caution before you copy anyone:** start with the survivorship caveat at the top of [Methodology](#methodology), and check the "Caveats, contradictions, verified-vs-claimed" section at the end of whichever case study you read — every document in this corpus separates what the creator actually does from what they merely claim.

---

## Repository map

- [`recurring-patterns.md`](recurring-patterns.md) — the 21 cross-creator patterns, claim-frequency table, comparison matrix, single-creator tactics.
- [`source-library.md`](source-library.md) — all documentation sources for all 15 creators, flagged.
- [`case-studies/`](case-studies/) — the 12 primary documents (this corpus's evidence base).
- [`working/shortlist.md`](working/shortlist.md) — the Phase 1.5 evidence packet (verbatim from per-creator evidence JSONs).
- [`working/MANIFEST.md`](working/MANIFEST.md) — run log: waves, passes, failures, and the early Phase 2 closure.
- [`working/evidence/`](working/evidence/) — per-creator verification JSONs (the source of truth for every number above).
