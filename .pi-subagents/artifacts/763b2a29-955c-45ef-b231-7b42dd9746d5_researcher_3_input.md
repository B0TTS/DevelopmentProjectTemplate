# Task for researcher

LANE: Imagine Dragons + producer Alex da Kid (and later Mattman & Robin) — the most consistent mainstream rock Hot 100 act of the last decade: 'Believer', 'Thunder', 'Natural', 'Enemy' (w/ JID, 2022), 'Bones' (2022), 'Eyes Closed' (2023), Loom (2024). DISTINCT ANGLE: the music press often criticizes them as 'algorithmically-built hits' (anthemic build, universal-vocabulary lyrics, sync-placement-ready foot-stompers) — commercially irrefutable Hot 100 consistency. SEAM: how Dan Reynolds writes from a melodic germ + universal-vocabulary lyrics (pain/struggle/empowerment, single-word refrains like 'Believer'/'Thunder'/'Bones') and how Alex da Kid / Mattman & Robin engineer the 'verse->pre-chorus lift->explosive hook' structure. This is the documented 'rock songs that chart every time' lane — explain BOTH the workflow AND the critique. Get Dan Reynolds + Alex da Kid + Mattman & Robin quotes (Rolling Stone, Billboard, AltPress, Atwood, Forbes).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — the 'build -> explosive hook' song structure step-by-step.
3) Lyric method — single-word refrains; universal emotional vocabulary; sync-friendly abstraction; occasional biography.
4) Topline/singing method — Dan's determined-plain belt; pseudo-chants; rhythmic hook; how the title-word hook is SUNG.
5) Vocal-anchoring production — the lift/pre-chorus crescendo, stomp-clap drops, music-box pianos.
6) Proof songs (2020-2025 preferred) — 'Enemy', 'Bones', 'Eyes Closed', 'Nice to Meet You'.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — AND the press critique — repeatable but the press considers formulaic.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Rolling Stone, Billboard, AltPress, Atwood, Forbes, Variety). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline (anthem craft).
- Emphasize what's REPEATABLE — and the honest debate about it.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/12-imagine-dragons.md
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