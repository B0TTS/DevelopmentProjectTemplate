# Research Mission: Deep-Documented Viral Short-Video Workflows

## Goal
Find workflows/formulas/frameworks that short-video content creators have documented **in depth, publicly** — step-by-step processes they use to make viral videos *consistently* (100k–1m+ views per video). I want the actual formulas, not vibes: hooks, pacing, structure, retention mechanics, posting cadence, replication tactics. Genre is irrelevant — I only care about frameworks with a proven, documented track record.

## Scope (hard requirements)
- **10–15 creators total.** Quality over quantity — pick the best-documented.
- **Verification bar (STRICT):** creator must be verified OR have a long public career, PLUS consistent evidence of 100k–1m+ views per video, PLUS verifiable career evidence (sub counts, documented earnings/brand deals, media coverage, platform stats). Reject anything borderline.
- **Recency cutoff applies to BOTH surfaces — hits AND documentation:**
  - **Hits:** viral/consistent-hit content within **2021–2026**. Older virality is excluded no matter how famous.
  - **Documentation:** the workflow explanations must also stem from **2021–2026** sources. A creator whose process write-up is frozen at 2019 is excluded — algorithms evolve, and stale workflows don't replicate. Tie the recency cutoff to the *source date*, not just the creator's career timeline.
  - **Staleness tag:** every citation carries a `still-current as of 2026?` flag (YES / NO / UNCLEAR + one-line reason). A 2021 source that the creator has since publicly revised is flagged NO with a pointer to the newer version.
- **Dominance weighting:** when selecting, rank candidates by how *recently* and *consistently* they produce hits. Recently-active-and-dominant beats famous-but-fading.
- **Documentation requirement:** the creator must have publicly explained their workflow (strategy videos, breakdowns, blogs, podcast appearances, interviews, course summaries). Skip creators who go viral but never explain how.
- **Source-author provenance:** flag each documentation source as FIRST-PARTY (creator explains own process) vs SECOND-HAND (analyst/reseller repackages it). Deep-dives weight first-party sources; second-hand claims carry a caveat and don't count toward verification.
- **Incentive bias:** flag each documentation source as MONETIZED (the explanation is tied to a course, community, or product the creator sells — treat as marketing until corroborated) vs INDEPENDENT (candid podcast/interview/breakdown with nothing attached to sell). Weight INDEPENDENT sources higher; a workflow described only in MONETIZED sources is a caveat, not a verified formula.
- **Language scope:** English-language documentation only. A non-English creator qualifies only if their workflow is documented in English.

## Consistency test & dominance score (measurement protocol)

### Consistency test (the definition of "consistent hits")
"Consistent" is mechanical, not impressionistic:
- **Hit-rate floor:** ≥60% of the creator's **last 20 eligible public videos** exceed 100k views, evidenced by per-video counts — never a channel-level claim. Report median views alongside; median >100k is the secondary check.
- **Channel-size normalization:** raw counts are judged against channel size. 100k views on a 10M-sub channel is *under*performance, not a hit. Flag any candidate whose views-to-follower ratio is chronically low even if absolute counts clear the floor.
- **New-upload exclusion:** exclude videos **<7 days old** from the hit-rate computation — a brand-new upload hasn't accumulated views yet and reads as a false "flop." On TikTok use the upload date; on YouTube (flat mode returns no dates) exclude the first 1–2 rows instead. This also mildly protects against the deleted-flops problem in the other direction.

### Measurement protocol — yt-dlp, not browsing
View counts are pulled with yt-dlp, not eyeballed from the platform UI:

```bash
# YouTube (exact counts; tab is reverse-chronological so row order = recency)
yt-dlp --flat-playlist --playlist-end 20 \
  --print "%(view_count)s | %(title).50s" "https://www.youtube.com/@HANDLE/shorts"

# TikTok (exact counts AND dates — dates let you verify the 2021–2026 window directly)
yt-dlp --flat-playlist --playlist-end 20 \
  --print "%(view_count)s | %(upload_date)s | %(title).40s" "https://www.tiktok.com/@HANDLE"
```

Platform caveats:
- **YouTube flat mode returns no upload dates** (all NA). "Last 20 by position" is the recency proxy — fine for the consistency test — but the 2021–2026 hits window is only directly auditable on TikTok. To prove recency of hits on YouTube, pull dates for the newest few videos individually, or cite dated third-party coverage.
- **Instagram/Reels-only creators are a verification tier, not a hard fail.** Anonymous Reels scraping is effectively dead. (a) Require every candidate to have a TikTok or Shorts presence where the consistency test runs (most cross-post). (b) Candidates with no TikTok/Shorts presence are marked `verification: PARTIAL — views unverifiable` and cannot anchor the shortlist.

### Dominance score (fixed formula — identical across all agents)
Every agent computes dominance with the same formula so scores are comparable at the dedup gate:

`dominance = 0.5 × hit_rate + 0.3 × hit_magnitude + 0.2 × activity`

- `hit_rate` (0–1): share of the last 20 eligible videos above 100k views (per the consistency test).
- `hit_magnitude` (0–1): median views of those videos ÷ 1,000,000, capped at 1.0.
- `activity` (0 / 0.5 / 1): most recent upload ≤14 days ago = 1.0; ≤60 days = 0.5; older = 0.

Report the three inputs and the arithmetic for every candidate — the ranking must be reproducible from the listed numbers.

## Orchestration (use sub-agents)

### Phase 1 — Discovery (partition by EVIDENCE TYPE, not platform)
Virality is cross-platform; splitting by platform risks both duplicates and misses. Partition by the *kind* of evidence:
- **Agent A — Course/blog authors:** creators who published written frameworks (blogs, course summaries, Substacks, public deck breakdowns). Returns up to 15 candidates.
- **Agent B — Podcast/interview circuit regulars:** creators whose process is documented across public podcasts/interviews. Returns up to 15 candidates.
- **Agent C — Channel strategy-video creators:** creators who film their own "how I make viral videos" breakdowns on their channel. Returns up to 15 candidates.

Return only candidates that plausibly pass the verification bar. **Padding the list to hit a quota is a failure mode** — an agent that finds 6 strong candidates returns 6.

Each agent returns candidates with: verification evidence, view-count evidence (per the consistency-test protocol above), career evidence, documentation depth (with FIRST-PARTY vs SECOND-HAND and MONETIZED vs INDEPENDENT flags + source dates), dominance score (per the fixed formula above — show the three inputs), and links.

### Phase 1.5 — Dedup + cull gate (mandatory)
A pool of up to 45 candidates funnels to 10–15. Culling is non-negotiable and rule-based:
- Merge duplicates across agents (track which agents surfaced each candidate).
- Apply hard cuts: fails verification, hits pre-2021, documentation frozen pre-2021, or no first-party workflow explanation.
- Rank survivors by dominance score ≥ documentation depth ≥ recency.
- Output the ranked shortlist **as a self-contained artifact** (see Phase 2 gate).
- **Shortfall fallback:** if fewer than 10 candidates survive the cuts, run one additional discovery wave with new search angles (new niches, new evidence-type queries). If still fewer than 10, proceed with the survivors and note the shortfall in the README. Never relax the 2021–2026 recency cutoffs or the verification bar to fill the list.

**Do not skip the discovery or dedup phase.**

### Phase 2 — Selection gate
Present the ranked shortlist (10–15) as a **self-contained evidence packet** so neither you nor I have to re-derive anything later, and so the deep-dive agents (which spawn fresh, with no discovery memory) can be seeded from the same artifact. Each shortlist entry MUST include, in-line:
- Creator name, handle, platform(s)
- Verification status + career evidence (sub count, brand deals, media coverage) with links
- View-count evidence (representative videos + per-video view range) with links
- Dominance score + how it was computed
- Documentation depth: which sources, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, source dates, `still-current as of 2026?` flags
- Pointer to the single best starting source for the deep dive

Get my sign-off before deep-diving.

### Phase 3 — Deep-dive (one agent per creator, parallel, WAVES not one-shot)
- Run in **waves of 3–5 agents**, not 10–15 simultaneously — parallel 5-page writers risk context/quality variance.
- Each produces an **exhaustive case study: as deep as sources support** (no fixed page floor). The floor is replaced by a depth gauge: a case study is "deep enough" when every workflow step has ≥1 first-party source, every claim is linked, and verified-vs-claimed + caveats + contradictions are all explicit. If sources run thin, say so explicitly and stop — do NOT pad to hit a length.
- Issue every agent the shared extraction schema (see Extraction Schema below) so the comparison matrix can be built without re-reading each file.
- **Quality-gate each case study before synthesis.** If shallow/thin despite adequate sources, re-spawn that creator's agent with a different angle or downgraded evidence tier (see Acceptance checklist).

### Phase 4 — Synthesis
You write: comparison matrix, recurring-patterns section (quantified — see below), dominance ranking, source library, README.

## Extraction Schema (fix the axes — issue to every deep-dive agent)
Every case study fills the same structured fields so the matrix is mechanical, not interpretive. Two discipline rules:
- **Closed vocabularies.** Enumerated fields use only the listed values — no free-form invention. If a creator genuinely uses a mechanism outside the vocabulary, propose it in a `## New Terms` section of the case study (term + one-line definition + source) so synthesis can normalize across creators; do not silently stuff it into the field.
- **Per-field citation.** Every populated field carries its own inline source reference. Matrix cells must be traceable to a source without re-reading the case study.

Fields:
- `creator`, `platform(s)`, `primary_niche`
- `hook_type` (question / visual / pattern-interrupt / claim / story / other)
- `first_frame_timing` (first 0–1s, 1–3s, 3–5s)
- `pattern_interrupt_cadence` (interval or beat structure)
- `payoff_placement` (when the viewer gets the reward)
- `loop_structure` (closed-loop / open-loop / cliffhanger / none)
- `retention_mechanism(s)` (closed list: curiosity gap / escalating stakes / stakes reset / payoff density / reaction bait / visual resets / open-question stack — additions only via `## New Terms`)
- `posting_cadence` (per-day/week, time-of-day rules)
- `replication_tactic` (how they say to repeat without burning out)
- `platform_specific_mechanics` (TikTok first-frame rules, Shorts watch-time loop, Reels hooks) — and whether the framework is `platform-agnostic` or `platform-specific`
- `source_date`, `still_current_as_of_2026`
- `evidence_tier` (FIRST-PARTY / SECOND-HAND) per source, plus `monetization_bias` (MONETIZED / INDEPENDENT) per source

## Tools & sources
- Web research: websearch/webfetch, creator channels, podcasts, interviews, blogs, articles — anything public.
- Paid content (courses/books): only capture if obtainable for free (summaries, breakdowns, leaked structure). Never ask me to pay; never pirate.
- **YouTube transcripts:** use the `youtube-transcript` skill (yt-dlp) for creators' strategy videos — transcripts go to `b0ttsagent/temp/youtube-transcripts/`. Always read the skill's SKILL.md first. **Sample most-recent-first:** recency is the binding constraint, so transcribe the creator's newest strategy/breakdown videos before older ones; older videos are fill-in only after the recent record is captured.

## Output structure (under `b0ttsagent/research/`)
Mirror the existing `viral-mixing-frameworks/` pattern:
- `README.md` — topic overview, methodology (incl. survivorship-bias caveat), dominance-ranked creator list; a new reader can pick a framework in 5 min
- `01-comparison-matrix.md` — every creator vs. the extraction-schema axes, **with a platform axis** and platform-agnostic-vs-specific tags
- `02-recurring-patterns.md` — quantified (see below)
- `03-source-library.md` — all links organized per creator. Per-source metadata, not bare URLs: title, URL, source date, source type (strategy video / podcast / blog / interview / course summary), FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag
- `case-studies/<category>/<creator-slug>.md` — one file per creator, filled to the extraction schema

## Non-negotiables
- Every claim in every doc must be linked to a source.
- Each creator's framework must be documented **individually and deeply** — no merging creators into one blob.
- Parallels must be built from the case studies, with cross-references back to them.
- If a creator fails verification mid-research, drop them and note the exclusion.
- Anything stale (no hits since 2021, OR documentation frozen since 2021) is out, period.

## Quantified Parallels (cross-reference discipline)
The "what works across the board" section is NOT impressionistic. It must contain:
- A **claim-frequency table:** `tactic → number of case studies that cite it → list of creator-slugs`.
- Every parallel entry must reference **≥2 case studies by slug + a specific source from each.** A pattern seen in only one creator is a tactic, not a parallel.

## Synthesis: platform-aware
- Matrix includes a **platform axis** (TikTok / Shorts / Reels / multi).
- Every parallel is tagged `platform-agnostic` or `platform-specific`. "Genre-irrelevant" must NOT silently become "platform-irrelevant" — front-frame rules and watch-time loops diverge across platforms.

## Acceptance checklist (definition of "done and good")
All must be true before synthesis is signed off:
- [ ] Every claim in every doc linked to a source
- [ ] ≥2 primary (first-party) sources per case study, or an explicit "thin sources" caveat
- [ ] Dominance ranking reproducible from the listed stats (show the numbers)
- [ ] All schema fields populated per case study (or marked N/A + reason)
- [ ] Every populated schema field carries its own source citation
- [ ] Source library entries carry full metadata (date, type, provenance, monetization bias, staleness flag)
- [ ] Quantified parallels table completed; every parallel refs ≥2 slugs + sources
- [ ] Platform axis populated in matrix; parallels tagged agnostic/specific
- [ ] Staleness tags (`still-current as of 2026?`) present on every citation
- [ ] README includes survivorship-bias caveat and lets a new reader pick a framework in 5 min

## Shallow-output protocol
If a case study comes back thin despite adequate surfaced sources:
1. Re-spawn that creator's deep-dive agent with a different angle prompt (new source trail, different schema lens).
2. If still thin after one re-spawn, **downgrade the creator's evidence tier** (FIRST-PARTY → SECOND-HAND caveated, or mark "documentation insufficient") rather than inflate.
3. If thin because sources genuinely don't exist, keep it but write the gap explicitly — never pad.

## Survivorship-bias caveat (state in README methodology, top)
These are **winners'** workflows — documented by creators who already broke out. Frameworks correlate with virality; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and audience you don't have yet.


Ask me any questions if you have before beginning.