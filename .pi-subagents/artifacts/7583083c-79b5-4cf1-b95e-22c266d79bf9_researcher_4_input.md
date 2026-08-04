# Task for researcher

LANE: Billie Eilish + Finneas O'Connell (sister-brother writer-producer duo) — Happier Than Ever (2021), Guitar Songs era, HIT ME HARD AND SOFT (2024, 'BIRDS OF A FEATHER', 'LUNCH', 'WILDFLOWER'; 2025 accolades/performances); earlier 'Bad Guy', 'Ocean Eyes'. DISTINCT ANGLE: bedroom-born ANTI-formula that became THE formula for intimate pop — near-whispered close-mic vocals, unconventional song structures (fake-out tempo/section changes), Finneas builds tracks from mouth-sounds/percussion then writes the topline to the production, lyrics written fast from real feeling. SEAM: their self-contained room writing, why soft/quiet songs cut through loudly on streaming, the specific melodic shapes of hooks like 'Bad Guy', 'Happier Than Ever', 'BIRDS OF A FEATHER'. Get Finneas/Billie quotes (Apple Music Zane Lowe, Song Exploder, Rolling Stone cover, NYT, interviews).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step, as THIS person actually does it (note single-room, sibling trust).
3) Lyric method — fast from feeling; diary-confession; revision rules; co-writing with each other.
4) Topline/singing method — whisper-to-belt dynamic; close-mic; intonation; the 'quiet hook'; rhythmic phrasing.
5) Vocal-anchoring production — mouth-sounds/percussive scaffolding under the whisper.
6) Proof songs (2020-2025 preferred) — 'Happier Than Ever', 'BIRDS OF A FEATHER', 'LUNCH'.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Apple Music Zane Lowe, Song Exploder, Rolling Stone, NYT, Billboard). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/07-billie-finneas.md
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