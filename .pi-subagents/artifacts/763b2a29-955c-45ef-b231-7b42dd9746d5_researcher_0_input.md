# Task for researcher

LANE: Travis Scott (Jacques Webster; Cactus Jack/Epic) — auto-tune melodic-trap innovator. Astroworld (2018) -> Utopia (2023, Billboard 200 #1, 'FE!N' w/ Playboi Carti, 'MY EYES', Circus Maximus film), 2024-25 festival residencies, '4x4' (2025). DISTINCT ANGLE: his vocal IS the production — treats the voice as an instrument, stacking/chopping harmonized autotuned takes, calls his method 'rager'/'psychedelic' architecture; song structure is a 'vibe' built in-studio with WondaGurl/Mike Dean/Allen Ritter/Oz/Southside. SEAM: the difference between 'writing a song' and 'building a sonic moment' for him, and the hook/topline craft in 'Sicko Mode', 'Goosebumps', 'FE!N', 'MELTDOWN', '4x4'. Get his, Mike Dean's, and WondaGurl's quotes (Rolling Stone cover, Complex, Billboard, NME).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step from idea to finished master, as THIS person actually does it.
3) Lyric method — theme/story/rhyme/hook generation; room vs. top-down; tools.
4) Topline/singing method — melodic construction; phrasing; range/falsetto/stacking/autotune; how the hook is SUNG; delivery.
5) Vocal-anchoring production — brief: what the track does around the vocal to make the hook land.
6) Proof songs (2020-2025 preferred) — name songs + what each shows of the formula + why it hit.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — the ONE thing they say makes it land; repeatable vs. one-off.
9) Gaps / uncertainties.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources: named interviews (Rolling Stone, Complex, Beats 1/Apple Music, NME). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE.
- No taboos: report facts (Astroworld-tragedy context only if it shapes the music/process answer).

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/03-travis-scott.md
This path is authoritative for this run.
Ignore any other output filename or output path mentioned elsewhere, including output destinations in the base agent prompt, system prompt, or task instructions.

## Acceptance Contract
Acceptance level: attested
Completion is not accepted from prose alone. End with a structured acceptance report.

Criteria:
- criterion-1: Return concrete findings with file paths and severity when applicable

Required evidence: review-findings, residual-risks

Finish with a fenced JSON block tagged `acceptance-report` in this shape:
Use empty arrays when no items apply; array fields contain strings unless object entries are shown.
`criteriaSatisfied[].status` must be exactly one of: satisfied, not-satisfied, not-applicable.
`commandsRun[].result` must be exactly one of: passed, failed, not-run.
`manualNotes` and `notes` are optional strings; an empty string means no note and does not satisfy `manual-notes` evidence.
```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "specific proof"
    }
  ],
  "changedFiles": [
    "src/file.ts"
  ],
  "testsAddedOrUpdated": [
    "test/file.test.ts"
  ],
  "commandsRun": [
    {
      "command": "command",
      "result": "passed",
      "summary": "short result"
    }
  ],
  "validationOutput": [
    "validation output or concise summary"
  ],
  "residualRisks": [
    "none"
  ],
  "noStagedFiles": true,
  "diffSummary": "short description of the diff",
  "reviewFindings": [
    "blocker: file.ts:12 - issue found, or no blockers"
  ],
  "manualNotes": "anything else the parent should know"
}
```