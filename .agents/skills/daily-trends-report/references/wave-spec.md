# Wave spec — daily-trends-report

The research-wave contract for one daily run. The orchestrator is a thin conductor: it sequences phase-owned agents, keeps only the ship phase for itself, and never reads `anchors.md`, `inventory.json`, or `routed.json` contents. Each phase agent reads the contract it needs from this doc itself; the orchestrator composes short spawn instructions from it — never templates, never heavy artifacts. Routing rules live in [routing-rules.md](routing-rules.md); the report the writer produces is defined by [report-contract.md](report-contract.md). This doc covers the research flow: folder layout, leaf schema, caps, phase sequence, QA, gap-fill, write-boundaries, and bounded summaries.

## Contents

- [Canonical timezone](#canonical-timezone)
- [Day folder](#day-folder)
- [Leaf schema](#leaf-schema)
- [Coverage domains](#coverage-domains)
- [Per-leaf caps](#per-leaf-caps)
- [Phase ownership](#phase-ownership)
- [Wave sequence](#wave-sequence)
- [What leaves receive](#what-leaves-receive)
- [Lead QA checklist](#lead-qa-checklist)
- [Gap-fill rules](#gap-fill-rules)
- [Who may write what](#who-may-write-what)
- [Bounded summaries](#bounded-summaries)
- [Failure handling](#failure-handling)
- [Copy-in checklist](#copy-in-checklist)
- [Harness](#harness)

## Canonical timezone

The canonical clock is a fixed UTC−10 offset (HST, no DST). "Today" and the 7-day recency window are computed against it. Both scripts default `--today` to this clock; fixtures and tests pass `--today YYYY-MM-DD` explicitly for determinism. Prose never makes recency decisions — the scripts own the window.

## Day folder

One day folder per run, A1 layout. `<base>` = `b0ttsagent/reports/daily-reports/AI-Development Trends`.

```
<base>/<YYYY-MM>/<YYYY-MM-DD>/
  report.md           writer only
  anchors.md          anchors lead (stitched from the two leaf files)
  anchors-hn.md       HN leaf (throwaway-intermediate)
  anchors-github.md   GitHub Trending leaf (throwaway-intermediate)
  inventory.json      build-inventory.py (run by the Explorer; throwaway)
  ai.json             AI leaf
  swe.json            SWE leaf
  productivity.json   Productivity leaf
  routed.json         route-and-verify.py (run by the routing agent; FROZEN once routed)
  wave-1.md           Explorer authors; research lead + routing agent append
```

`index.md` is a single file at `<base>/index.md` — the parent of the month folders.

| File | Written by | When | Throwaway? / Frozen? |
|---|---|---|---|
| `inventory.json` | `build-inventory.py` (run by Explorer) | Setup | throwaway — rebuilt every run, never hand-edited |
| `wave-1.md` | Explorer authors; research lead + routing agent append | Setup / research / gap-fill | no |
| `anchors-hn.md`, `anchors-github.md` | the matching anchors leaf | anchors wave | throwaway-intermediate — rebuilt every run |
| `anchors.md` | anchors lead (stitches the two leaf files) | anchors wave | no — the only consumer-facing anchors file |
| `ai.json`, `swe.json`, `productivity.json` | the matching research leaf | research wave | yes at QA pass |
| `routed.json` | `route-and-verify.py` (run by routing agent) | route / gap-fill | **frozen — the writer only words from it** |
| `report.md` | **writer only** | writer phase | yes at verify pass |
| `index.md` | orchestrator | ship | upsert, newest row on top |

## Leaf schema

Each research leaf writes exactly one file: `ai.json` (section "AI trends"), `swe.json` (section "SWE trends"), `productivity.json` (section "Productivity"). Shape — an object with one key, `items`, an array of:

```json
{
  "items": [
    {
      "headline": "Frontier lab ships open-weights model",
      "why": "A new open-weights frontier model lands with permissive licensing, resetting the self-host cost floor.",
      "url": "https://example.com/frontier-v3",
      "published_date": "2026-08-17",
      "domain": "frontier model releases",
      "source_type": "blog post",
      "delta_or_null": null
    }
  ]
}
```

| Field | Rule |
|---|---|
| `headline` | Non-empty, plain, claim-faithful. |
| `why` | Why it matters, ≤2 sentences / ~40 words. |
| `url` | Primary source, `http(s)`, the page actually read to verify the claim. |
| `published_date` | `YYYY-MM-DD` — the page's published/updated date, or the HN submission time only when the cited item *is* that post. No guessed dates; an empty string means undated (the router drops it). |
| `domain` | One of the section's coverage-domain hints (hints, not a quota). |
| `source_type` | What the source is: paper, advisory, release notes, blog post, news, changelog… |
| `delta_or_null` | `null`, or the concrete dated delta (version, number, decision, CVE id, ship date) when re-proposing a prior identity. "Still being discussed" is not a delta. |

Anchors leaves do **not** use this schema — they write raw title/link (or repo/link) lists to `anchors-hn.md` / `anchors-github.md`, discovery seeds only.

Leaves propose; they do not route. Placement decisions (main / Still circulating / excluded / dropped) are the router's job — never the leaf's, the lead's, or the writer's.

## Coverage domains

Each section's research scope is a fixed domain list — **hints, not a quota**; leaves are not asked to hit every domain. Max 2 items per domain per section is a router *preference* (see routing-rules.md); if honoring it would drop a better item or empty a thin section, keep the better item and note the cluster. The coverage-domain list below is what a research leaf receives for its section.

| Section | Domain hints |
|---|---|
| AI trends | frontier model releases · AI research papers · AI company news · open-source AI · AI policy/regulation · AI infra/hardware |
| SWE trends | security & CVEs · OSS licensing & governance · cloud & pricing · languages & frameworks · web platform & standards · dev tools & editors |
| Productivity | new SWE productivity tools · AI-assisted dev workflows · emerging practices & workflows |

**Productivity constraint.** An item must be a shipped or newly documented tool, workflow, or practice with a dated primary source. No "10 tips" roundups, no evergreen blog posts, no "remember to use a todo list".

Gap-fill's "empty domain hints" (see Gap-fill rules) are the thin section's coverage domains that currently have zero survivors.

## Per-leaf caps

Hard caps, per research leaf, per wave — the first wave and any gap-fill wave each get the same fresh budget:

- **≤8 web searches**
- **≤5 full page-reads** (fetch + read a page to verify claims)

A search snippet is discovery, not evidence — but at these caps, when the budget is spent the leaf stops and writes what it has. Thin > padded; never invent to fill.

Anchors leaves are single-page raw fetches (HN front page, GitHub Trending) — they are **not** subject to the 8/5 research budget; each fetches its one page, writes the raw list, and stops.

The research lead does no research at all: its QA is summaries-only — it reads each leaf's ≤250-word final message, never the full leaf files, and never re-researches. (The anchors lead is the documented exception: it reads the two small anchor-leaf files to stitch `anchors.md` — see Lead QA checklist.)

## Phase ownership

| Phase | Agent | Owns | Returns (bounded) |
|---|---|---|---|
| Setup — Explorer | `b0tts-general-agent` | run `build-inventory.py`; author `wave-1.md` (path-references only) | ≤150 words: inventory count, `wave-1.md` path, edge-case warnings |
| Setup — anchors wave | `b0tts-lead-researcher` + 2 `b0tts-researcher` leaves | fetch HN + GitHub Trending; stitch `anchors.md` | ≤500 words: status, `anchors.md` path, per-source counts, anomalies |
| Research wave | `b0tts-lead-researcher` + 3 `b0tts-researcher` leaves | fan out AI/SWE/Productivity; QA; append wave report to `wave-1.md` | ≤500 words |
| Route + gap-fill | `b0tts-smart-agent` | run `route`; read survivors; author one gap-fill spec if needed; re-spawn thin-section leaf; re-route; stop | ≤250 words: survivors-per-section, gap-fill ran?, frozen `routed.json` path |
| Writer | `b0tts-smart-agent` | word `report.md` from frozen `routed.json` + report-contract | ≤250 words: `report.md` path, section/item counts, the 3 glance bullets, demoted count |
| Ship | orchestrator | verify; ≤1 rewrite; upsert `index.md`; post chat pointer | (run's closing voice) |

The Setup-Explorer and Setup-anchors phases are **parallel siblings** spawned in ONE message; the orchestrator joins both before spawning the research wave. Neither depends on the other's contents — the Explorer authors `wave-1.md` by path-reference (never reads `anchors.md` or `inventory.json`), and the anchors wave produces `anchors.md` (never reads `wave-1.md`).

## Wave sequence

1. **Setup (parallel).** Orchestrator spawns, in ONE message:
   - **Explorer** (`b0tts-general-agent`): run

     ```
     python scripts/build-inventory.py --base "b0ttsagent/reports/daily-reports/AI-Development Trends" --today <YYYY-MM-DD>
     ```

     then author `wave-1.md` from the contract above (folder layout, leaf schema, coverage domains, caps, write-boundaries) using path-references only — it writes the day-folder path, the 3 sections + their output paths, the `anchors.md` + `inventory.json` paths, and the caps; it never reads `anchors.md` or `inventory.json` contents. Return ≤150 words.
   - **Anchors wave** (`b0tts-lead-researcher`): read the anchors contract (this doc) and execute — fan out 2 `b0tts-researcher` leaves (HN front page / GitHub Trending); each leaf fetches its one page, writes its raw title/link list to `anchors-hn.md` / `anchors-github.md`, and returns only a count; the lead QC's existence + non-emptiness, reads the two small leaf files, and stitches them into `anchors.md`. Return ≤500 words.

   The orchestrator waits for both summaries. It reads neither the leaf files nor `anchors.md`.

2. **Research wave.** Orchestrator spawns `b0tts-lead-researcher` pointing at the Explorer-authored `wave-1.md`. The lead fans out 3 leaves (AI / SWE / Productivity) in one message; each leaf reads `anchors.md` + `inventory.json` itself, researches per the schema + caps, writes its leaf file, returns ≤250 words; the lead QA's disk outputs (checklist below) and appends its wave report to `wave-1.md`.

3. **Route + gap-fill.** Orchestrator spawns `b0tts-smart-agent` as the routing agent. It runs

   ```
   python scripts/route-and-verify.py route --folder "<base>/<YYYY-MM>/<YYYY-MM-DD>" --today <YYYY-MM-DD>
   ```

   reads survivors-per-section from the now-frozen `routed.json`; if any main section has 0–2 survivors it authors exactly ONE gap-fill spec from `routed.json`'s exclusions, prior identities, and the thin section's empty domain hints (Gap-fill rules below), appends it to `wave-1.md`, re-spawns the research lead for the thin section, and re-runs `route`; then stops — no third wave. Declares `routed.json` frozen (no one hand-edits it from here; the writer only words from it). Return ≤250 words.

4. **Writer.** Orchestrator spawns `b0tts-smart-agent` with the frozen `routed.json` path + instruction to read `references/report-contract.md` and write `report.md` — wording only: no research, no routing, no rescue of rejects. Only the writer writes `report.md`. Return ≤250 words including the 3 glance bullets + demoted count (so the orchestrator can post the chat pointer without reading `report.md`).

5. **Ship.** Orchestrator runs

   ```
   python scripts/route-and-verify.py verify --folder "<base>/<YYYY-MM>/<YYYY-MM-DD>" --today <YYYY-MM-DD>
   ```

   Exit 0 = gates clean (format nudges may still warn). Exit 1 = gate violations → exactly **one** writer rewrite, then ship with a "verify failed" note — never loop. Then upsert `index.md` (newest row on top; a same-day rerun updates today's row, never appends a duplicate) and post the chat pointer from the writer's summary: path + the 3 glance bullets + "N items demoted" when Still circulating is non-empty.

## What leaves receive

Each research leaf receives, via its spawn instruction (composed by the research lead from `wave-1.md` + this contract): its section name, the day-folder path, the paths to `anchors.md` and `inventory.json`, its exact output path, the caps, and a pointer to the leaf schema + coverage domains in this doc. The leaf reads `anchors.md` and `inventory.json` itself.

Rules the research leaf must honor:

- **Do not re-propose prior identities.** Any identity in `inventory.json`'s streak maps (the last 2 reports' main-section items) is off the proposal list unless the leaf holds a dated, concrete delta — then it may propose the item with `delta_or_null` set and the item's own date ≤7 days old. No delta → skip it; at most the router will demote it to Still circulating.
- **Anchors are seeds, never items.** Use HN / Trending only to discover a dated primary source.
- **Coverage domains are hints, not a quota.** Leaves are not asked to hit every domain.

Each anchors leaf receives: its source (HN front page or GitHub Trending), its exact output path (`anchors-hn.md` / `anchors-github.md`), and the rule that an HN thread or trending row is **never** a report item — discovery seeds only. It fetches its one page, writes the raw title/link (or repo/link) list, and returns only a count.

## Lead QA checklist

**Research lead** (summaries-only — never pull leaf files into context):

- [ ] Every leaf output exists at the exact path the spec names; each is valid JSON with an `items` list (an explicitly empty list is a valid result).
- [ ] Every item carries all 7 schema fields; `published_date` is `YYYY-MM-DD`; `url` is `http(s)`.
- [ ] No item re-proposes an inventory streak identity without a non-empty `delta_or_null`.
- [ ] No item is an anchor used as the item itself (HN thread / trending row).
- [ ] Every delta is concrete — version, number, decision, CVE id, ship date — not "still being discussed".
- [ ] Counts in each leaf's final summary reconcile with its file.
- [ ] QA reads summaries only; never pull leaf files into context.
- [ ] A missing/invalid output → one targeted re-run of that leaf; second failure → record the gap, never fabricate.

**Anchors lead** (documented exception — the anchors wave's leaf outputs are small raw lists, not research findings, so the lead reads them to stitch):

- [ ] Both `anchors-hn.md` and `anchors-github.md` exist and are non-empty.
- [ ] `anchors.md` is stitched from the two leaf files and is non-empty.
- [ ] The lead reads **only** the two small anchor-leaf files (raw title/link lists) to stitch `anchors.md` — never the page content, which died in the leaf contexts. This is the sole exception to the lead's summaries-only rule, justified because anchors leaf outputs are raw discovery lists, not research findings.
- [ ] A leaf that dies or returns empty → retry once; second failure → record the gap, never fabricate.

## Gap-fill rules

- **Trigger.** Any main section ends wave 1 with 0–2 survivors in `routed.json`.
- **Owner.** The routing agent (`b0tts-smart-agent`) — it holds the frozen `routed.json` in its own context, not the orchestrator.
- **Exactly ONE gap-fill wave.** One gap-fill leaf per thin section, each targeting **exactly 3** new items.
- **Inputs, from the frozen `routed.json`.** The exclusion list (`exclusions` — every identity already surfaced this run, accepted or rejected), the prior identities (`prior_identities` — the last 2 reports' streak set), and the empty domain hints (the thin section's coverage domains with zero current survivors — the literal gaps).
- **Mechanics.** The routing agent authors the gap-fill spec (composed from this contract + the frozen inputs — no template), appends it to `wave-1.md`, re-spawns the research lead pointing at the thin section; the lead runs it, QA's it, appends its report; the routing agent re-runs `route`.
- **Then stop.** No third wave. If the section still cannot reach 3, ship short — 1–2 items is a valid thin day.

## Who may write what

| Actor | May write |
|---|---|
| Orchestrator | runs the verify script; upserts `index.md`; posts the chat pointer. Spawns every phase; reads only their bounded summaries. |
| Explorer (`b0tts-general-agent`) | authors `wave-1.md`; runs `build-inventory.py` (which alone writes `inventory.json`) |
| Anchors lead (`b0tts-lead-researcher`) | `anchors.md` (stitched); its anchors-wave report appended to `wave-1.md` |
| Anchors leaves (`b0tts-researcher`) | only their assigned anchor-leaf file (`anchors-hn.md` / `anchors-github.md`) |
| Research lead (`b0tts-lead-researcher`) | its wave report appended to `wave-1.md` |
| Research leaves (`b0tts-researcher`) | only their assigned leaf file (`ai.json` / `swe.json` / `productivity.json`) |
| Routing agent (`b0tts-smart-agent`) | the gap-fill spec appended to `wave-1.md`; runs `route-and-verify.py route` (which alone writes `routed.json`) |
| Writer (`b0tts-smart-agent`) | **only `report.md`** — and the writer is the only agent allowed to write it |

Leaves and leads write only their assigned paths inside the day folder; no subagent ever writes outside it. `inventory.json`, `routed.json`, and the two anchor-leaf files are derived/throwaway — never hand-edited by anyone.

## Bounded summaries

Every phase returns a bounded summary; the orchestrator reads only these, never the heavy artifacts (anchors page content, inventory, routing output, or `report.md`).

| Phase | Return cap | Must include |
|---|---|---|
| Explorer | ≤150 words | inventory count, `wave-1.md` path, edge-case warnings |
| Anchors lead | ≤500 words | status, `anchors.md` path, per-source counts, anomalies |
| Research lead | ≤500 words | per-leaf status/verdicts, paths, next actions |
| Routing agent | ≤250 words | survivors-per-section, whether a gap-fill wave ran, frozen `routed.json` path |
| Writer | ≤250 words | `report.md` path, section/item counts, the 3 glance bullets, demoted count (when Still circulating non-empty) |

Never paste file contents into a summary.

## Failure handling

- A leaf that dies or fails → retry once with the same instruction (resume via task_id if possible, else respawn fresh pointing at its output path). Second failure → record the gap, never fabricate.
- A missing/invalid output → one targeted re-run before declaring the phase done.
- **Exactly one gap-fill wave, then stop** — a thin day ships short rather than looping.
- No phase ever fabricates work to fill a hole.

## Copy-in checklist

The orchestrator pastes this into the run and ticks it as it goes:

- [ ] Explorer spawned (inventory + wave-1.md)
- [ ] Anchors wave spawned (anchors.md stitched)
- [ ] Setup joined
- [ ] Research lead spawned
- [ ] QA passed
- [ ] Route + gap-fill done (routed.json frozen)
- [ ] Writer spawned
- [ ] Verify script pass
- [ ] Index updated
- [ ] Chat pointer posted

## Harness

The runtime is opencode. The orchestrator is the agent the user spawned with this skill loaded; it is a thin conductor that spawns phase-owned agents and keeps only the ship phase. Phase agents: Explorer = `b0tts-general-agent`; anchors and research waves led by `b0tts-lead-researcher` with `b0tts-researcher` leaves; routing + gap-fill + writer = `b0tts-smart-agent`. Leaves use the `opencode-web-research` skill for web tool routing; subagents are the existing opencode agent definitions — no new definitions. This skill is written for no other harness and carries no dual-harness path.
