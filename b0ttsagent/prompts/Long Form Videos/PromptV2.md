# Research Mission: Deep-Documented Long-Form Video Workflows

## Goal
Find workflows/formulas/frameworks that long-form video content creators have documented **in depth, publicly** — step-by-step processes they use to make consistently high-performing videos. I want the actual formulas, not vibes: opening hooks/cold opens, structure/act design, pacing, retention mechanics, editing rhythm, posting cadence, replication tactics. Genre is irrelevant — I only care about frameworks with a proven, documented track record.

**Target format:** edited YouTube long-form videos, roughly 10–30 minutes — video essays, deep dives, explainers, documentary-style, storytelling, edited commentary-comedy. **Exclude:** podcasts, livestreams, let's-plays/walkthroughs, raw unedited vlogs, music videos, compilations/reaction channels, news broadcasts. The workflow is the point — genre only matters insofar as it's edited, single, cohesive, and not a talk-format episode.

## Scope (hard requirements)
- **10–15 creators total.** Quality over quantity — pick the best-documented.
- **Verification bar (STRICT):** creator must be verified OR have a long public career, PLUS consistent evidence of 100k+ views per video, PLUS verifiable career evidence (sub counts, documented earnings/brand deals, media coverage, platform stats). Reject anything borderline.
- **View-magnitude preference:** 1m+ median-view creators are prioritized for inclusion; 10m+/video creators anchor the top of the shortlist and rank highest. Magnitude drives ranking.
- **Recency cutoff applies to BOTH surfaces — hits AND documentation:**
  - **Hits:** consistent-hit content within **2021–2026**. Older virality is excluded no matter how famous.
  - **Documentation:** the workflow explanations must also stem from **2021–2026** sources. A creator whose process write-up is frozen at 2019 is excluded — algorithms evolve, and stale workflows don't replicate. Tie the recency cutoff to the *source date*, not just the creator's career timeline.
  - **Staleness tag:** every citation carries a `still-current as of 2026?` flag (YES / NO / UNCLEAR + one-line reason). A 2021 source that the creator has since publicly revised is flagged NO with a pointer to the newer version.
- **Dominance weighting:** when selecting, rank candidates by how *recently* and *consistently* they produce hits, weighted toward view magnitude. Recently-active-and-dominant beats famous-but-fading.
- **Documentation requirement:** the creator must have publicly explained their workflow (strategy videos, breakdowns, blogs, podcast appearances, interviews, course summaries). Skip creators who hit big but never explain how.
- **Source-author provenance:** flag each documentation source as FIRST-PARTY (creator explains own process) vs SECOND-HAND (analyst/reseller repackages it). Deep-dives weight first-party sources; second-hand claims carry a caveat and don't count toward verification.
- **Incentive bias:** flag each documentation source as MONETIZED (the explanation is tied to a course, community, or product the creator sells — treat as marketing until corroborated) vs INDEPENDENT (candid podcast/interview/breakdown with nothing attached to sell). Weight INDEPENDENT sources higher; a workflow described only in MONETIZED sources is a caveat, not a verified formula.
- **Language scope:** English-language documentation only. A non-English creator qualifies only if their workflow is documented in English.

## Consistency test & dominance score (measurement protocol)

### Consistency test (the definition of "consistent hits")
"Consistent" is mechanical, not impressionistic:
- **Hit-rate floor:** ≥60% of the creator's **last 12 eligible public videos** exceed 100k views, evidenced by per-video counts — never a channel-level claim. Report median views alongside.
- **New-upload exclusion:** exclude videos **<14 days old** from the hit-rate computation — long-form accumulates views slower than short-form, and a brand-new upload reads as a false "flop." YouTube flat mode returns no upload dates, so exclude the first 1–2 rows instead, and pull dates for the newest few videos individually to verify recency.

### Measurement protocol — yt-dlp, not browsing
View counts are pulled with yt-dlp, not eyeballed from the platform UI:

```bash
# YouTube long-form (exact counts; /videos tab is reverse-chronological so row order = recency)
yt-dlp --flat-playlist --playlist-end 12 \
  --print "%(view_count)s | %(title).50s" "https://www.youtube.com/@HANDLE/videos"
```

Platform caveat:
- **YouTube flat mode returns no upload dates** (all NA). "Last 12 by position" is the recency proxy — fine for the consistency test — but the 2021–2026 hits window is auditable by pulling dates for the newest few videos individually, or by citing dated third-party coverage.
- Candidates with no YouTube presence cannot qualify (the target format is YouTube long-form).

### Dominance score (fixed formula — identical across all agents)
Every agent computes dominance with the same formula so scores are comparable at the dedup gate. Magnitude is weighted heaviest, per the view-magnitude preference:

`dominance = 0.3 × hit_rate + 0.5 × hit_magnitude + 0.2 × activity`

- `hit_rate` (0–1): share of the last 12 eligible videos above 100k views (per the consistency test).
- `hit_magnitude` (0–1): median views of those videos ÷ 10,000,000, capped at 1.0 → 10m/video = 1.0, 1m = 0.1, 100k = 0.01.
- `activity` (0 / 0.5 / 1): most recent upload ≤30 days ago = 1.0; ≤90 days = 0.5; older = 0 (windows widened for long-form cadence, which is weekly-to-monthly, not daily).

Report the three inputs and the arithmetic for every candidate — the ranking must be reproducible from the listed numbers.

## Orchestration (use sub-agents)

### Phase 1 — Discovery (partition by EVIDENCE TYPE)
Partition by the *kind of evidence* a creator's documentation comes in:
- **Agent A — Course/blog authors:** creators who published written frameworks (blogs, course summaries, Substacks, public deck breakdowns). Returns up to 15 candidates.
- **Agent B — Podcast/interview circuit regulars:** creators whose process is documented across public podcasts/interviews. Returns up to 15 candidates.
- **Agent C — Channel strategy-video creators:** creators who film their own "how I make my videos" breakdowns on their channel. Returns up to 15 candidates.

Return only candidates that plausibly pass the verification bar. **Padding the list to hit a quota is a failure mode** — an agent that finds 6 strong candidates returns 6.

Each agent returns candidates with: verification evidence, view-count evidence (per the consistency-test protocol above), career evidence, documentation depth (with FIRST-PARTY vs SECOND-HAND and MONETIZED vs INDEPENDENT flags + source dates), dominance score (per the fixed formula above — show the three inputs), and links.

### Phase 1.5 — Dedup + cull gate (mandatory)
A pool of up to 45 candidates funnels to 10–15. Culling is non-negotiable and rule-based:
- Merge duplicates across agents (track which agents surfaced each candidate).
- Apply hard cuts: fails verification, hits pre-2021, documentation frozen pre-2021, or no first-party workflow explanation.
- Rank survivors by dominance score ≥ documentation depth ≥ recency. Magnitude-weighted dominance puts the 1m+/10m+ creators at the top.
- Output the ranked shortlist **as a self-contained artifact** (see Phase 2 gate).
- **Shortfall fallback:** if fewer than 10 candidates survive the cuts, run one additional discovery wave with new search angles (new niches, new evidence-type queries). If still fewer than 10, proceed with the survivors and note the shortfall in the README. Never relax the 2021–2026 recency cutoffs or the verification bar to fill the list.

**Do not skip the discovery or dedup phase.**

### Phase 2 — Selection gate
Present the ranked shortlist (10–15) as a **self-contained evidence packet** so neither you nor I have to re-derive anything later, and so the deep-dive agents (which spawn fresh, with no discovery memory) can be seeded from the same artifact. Each shortlist entry MUST include, in-line:
- Creator name, handle, platform(s)
- Verification status + career evidence (sub count, brand deals, media coverage) with links
- View-count evidence (representative videos + per-video view range) with links
- Dominance score + how it was computed (the three inputs and arithmetic)
- Documentation depth: which sources, FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, source dates, `still-current as of 2026?` flags
- Pointer to the single best starting source for the deep dive

Get my sign-off before deep-diving.

### Phase 3 — Deep-dive (one agent per creator, parallel, WAVES not one-shot)
- Run in **waves of 3–5 agents**, not 10–15 simultaneously — parallel writers risk context/quality variance.
- Each produces an **exhaustive case study: as deep as sources support** (no fixed page floor). The depth gauge: a case study is "deep enough" when every workflow step has ≥1 first-party source, every claim is linked, and verified-vs-claimed + caveats + contradictions are all explicit. If sources run thin, say so explicitly and stop — do NOT pad to hit a length.
- **No imposed extraction schema.** Let each creator's framework speak in its own terms. Document *that* creator's workflow as they describe it — their vocabulary, their structure, their mechanics — not a shared set of fields. Do not force-fit creators into a common vocabulary; if a shared pattern exists across creators, it will surface in synthesis.
- **Guidance, not fields.** A thorough case study generally covers (where the creator documents it): how they open the video, structure/act design, pacing and retention strategy, editing rhythm, posting cadence, and how they say to replicate without burning out. Skip anything the creator doesn't address — don't invent it.
- **Quality-gate each case study before synthesis.** If shallow/thin despite adequate sources, re-spawn that creator's agent with a different angle or downgraded evidence tier (see Shallow-output protocol).

### Phase 4 — Synthesis
You write: recurring patterns (emergent — see below), dominance ranking, source library, README. Build a comparison matrix *only if* common axes genuinely surface across case studies; otherwise let the patterns section carry the cross-creator view. Do not fabricate a matrix to fill a slot.

## Emergent patterns (cross-reference discipline)
The "what works across the board" section is NOT impressionistic and is NOT imposed — it is built bottom-up by reading the case studies and finding what actually recurs:
- A **claim-frequency table:** `tactic → number of case studies that cite it → list of creator-slugs`.
- Every pattern entry must reference **≥2 case studies by slug + a specific source from each.** A tactic seen in only one creator is a tactic, not a pattern.
- Patterns get tagged `format-agnostic` (works across video-essay / deep-dive / explainer / documentary-style / edited commentary-comedy) or `format-specific` (tied to one format). Do not assume a tactic is universal — if it shows up in only one format, tag it.

## Tools & sources
- Web research: websearch/webfetch, creator channels, podcasts, interviews, blogs, articles — anything public.
- Paid content (courses/books): only capture if obtainable for free (summaries, breakdowns, leaked structure). Never ask me to pay; never pirate.
- **YouTube transcripts:** use the `youtube-transcript` skill (yt-dlp) for creators' strategy videos — transcripts go to `b0ttsagent/temp/youtube-transcripts/`. Always read the skill's SKILL.md first. **Sample most-recent-first:** recency is the binding constraint, so transcribe the creator's newest strategy/breakdown videos before older ones; older videos are fill-in only after the recent record is captured.

## Output structure (under `b0ttsagent/research/long-form-video-frameworks/`)
Mirror the existing `viral-mixing-frameworks/` pattern:
- `README.md` — topic overview, methodology (incl. survivorship-bias caveat), dominance-ranked creator list; a new reader can pick a framework in 5 min
- `recurring-patterns.md` — emergent cross-creator patterns, with the claim-frequency table and ≥2-slug sourcing per pattern
- `source-library.md` — all links organized per creator. Per-source metadata, not bare URLs: title, URL, source date, source type (strategy video / podcast / blog / interview / course summary), FIRST-PARTY vs SECOND-HAND, MONETIZED vs INDEPENDENT, `still-current as of 2026?` flag
- `case-studies/<creator-slug>.md` — one file per creator, documented in the creator's own terms, as deep as sources support (no imposed schema)

## Non-negotiables
- Every claim in every doc must be linked to a source.
- Each creator's framework must be documented **individually and deeply** — no merging creators into one blob.
- Patterns must be built from the case studies, with cross-references back to them.
- If a creator fails verification mid-research, drop them and note the exclusion.
- Anything stale (no hits since 2021, OR documentation frozen since 2021) is out, period.

## Acceptance checklist (definition of "done and good")
All must be true before synthesis is signed off:
- [ ] Every claim in every doc linked to a source
- [ ] ≥2 primary (first-party) sources per case study, or an explicit "thin sources" caveat
- [ ] Dominance ranking reproducible from the listed stats (show the numbers — the three inputs and arithmetic)
- [ ] Source library entries carry full metadata (date, type, provenance, monetization bias, staleness flag)
- [ ] Claim-frequency table completed; every pattern refs ≥2 slugs + sources
- [ ] Patterns tagged format-agnostic vs format-specific
- [ ] Staleness tags (`still-current as of 2026?`) present on every citation
- [ ] README includes survivorship-bias caveat and lets a new reader pick a framework in 5 min

## Shallow-output protocol
If a case study comes back thin despite adequate surfaced sources:
1. Re-spawn that creator's deep-dive agent with a different angle prompt (new source trail, different framing).
2. If still thin after one re-spawn, **downgrade the creator's evidence tier** (FIRST-PARTY → SECOND-HAND caveated, or mark "documentation insufficient") rather than inflate.
3. If thin because sources genuinely don't exist, keep it but write the gap explicitly — never pad.

## Survivorship-bias caveat (state in README methodology, top)
These are **winners'** workflows — documented by creators who already broke out. Frameworks correlate with consistent performance; they are not proven to cause it. Treat the output as a high-evidence starting set for replication, not a guaranteed formula. Replicability depends on execution, niche, platform state, and audience you don't have yet.

---

Ask me any questions if you have before beginning.
