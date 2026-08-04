# Task for researcher

LANE: The Weeknd (Abel Tesfaye; XO/Republic) — After Hours (2020), 'Blinding Lights' (longest-ever top-10 Hot 100 run, Diamond), Dawn FM (2022), Hurry Up Tomorrow (2025); 'Save Your Tears' (remix w/ Ariana), 'Die For You' 2023 rechart. DISTINCT ANGLE: signature Michael-meets-disco falsetto topline, co-written/produced with Max Martin / Oscar Holter / DaHeala / Belly / Savan Kotecha / Cirkut; persona-as-concept anchoring each album's hook emotion. SEAM: his collaboration method (co-writer-heavy, cuts vocals in his own studio), the falsetto-to-chest-voice switch as a hook device, and the melodic-math topline of 'Blinding Lights'/'Save Your Tears'/'Take My Breath'/'Dancing in the Flames'/'Timeless'. Get Abel, Max Martin, Oscar Holter, and Cirkut quotes.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step, as THIS person actually does it.
3) Lyric method — emotional distillation to one hook feeling; co-writing room.
4) Topline/singing method — melodic construction; falsetto/chest switches; phrasing; riffs; how the hook is SUNG.
5) Vocal-anchoring production — what the track does around the falsetto to make it land (synth line as counter-melody).
6) Proof songs (2020-2025 preferred) — 'Blinding Lights', 'Save Your Tears', 'Take My Breath', 'Die For You' re-chart.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Rolling Stone, NYT, Variety, Billboard, Apple Music Zane Lowe, Song Exploder). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/06-the-weeknd.md
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