# Task for researcher

LANE: Metro Boomin (Leland Wayne; Atlanta trap super-producer) — co-signer/producer for Future, 21 Savage, Migos, Don Toliver; HEROES & VILLAINS (2022, Billboard 200 #1), SPIDER-VERSE score, WE DON'T TRUST YOU & WE STILL DON'T TRUST YOU (2024 w/ Future, 'Like That' Hot 100 #1), 2024-25. DISTINCT ANGLE: brand-as-tune tag ('Metro Boomin want some more!'), structural beat-hook discipline, and how a trap producer co-signs/positions a song to chart, including the writing/finding-the-hook process with the artist. SEAM: producer-LED song construction where the beat IS the hook and the topline is minimal but pivotal; his 'If Metro don't trust you I'ma shoot you' workflow, his instruction to artists ('don't mess up the beat'). Get Metro's direct quotes plus Future, 21 Savage, Don Toliver, The Weeknd collaborators. (Confirm you cover 2020-2025 work.)

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step, as THIS producer actually does it.
3) Lyric method (how he prescribes/drives the writer-artist's hook & lyric while staying producer) — hooks, callouts, repetition.
4) Topline/singing method — how minimal-lyric trap topline still functions as a sung hook (see 'Like That', 'Superhero', 'Creepin').
5) Beat-as-hook scaffolding — what the track does to make the vocal/chant land.
6) Proof songs (2020-2025 preferred) — name songs + what each shows.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources: Metro Boomin interviews (Complex, Billboard, Apple Music), songwriting credits. Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric/topline discipline (trap style).
- Emphasize what's REPEATABLE.
- No taboos: report credit/controversy facts frankly.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/04-metro-boomin.md
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