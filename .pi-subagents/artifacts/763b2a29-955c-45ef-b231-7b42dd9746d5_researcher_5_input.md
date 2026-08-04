# Task for researcher

LANE: Tyler, The Creator (Tyler Okonma; Camp Flog Gnaw/Columbia) — IGOR (2019/2020 Grammy nom), CALL ME IF YOU GET LOST (2022 Grammy Best Rap Album), CHROMAKOPIA (2024, 'St. Chroma', 'Noid', 'See You Again' renewed TikTok-era chart action, 'Darling, I'). DISTINCT ANGLE: maximalist self-produced auteur evolving from Odd Future shock-rap to brass-driven soul/hiphop — writing songs where the production paints and the topline is sung/rapped with unusual care; self-produced through entire albums; intentional craft over formula. SEAM: his distinctive writing process (compositions from chord loops, voice-memo melody on top, treats albums as 'movies' w/ sequenced transitions, writes bittersweet love songs with earned emotionality), his singing improvement (sings himself on hooks now vs. just rapping), and how he uses featured vocalists ('See You Again' Kali Uchis, 'St. Chroma' Daniel Caesar, 'Darling, I') for topline contrast. Get Tyler quotes (Apple Music Interviews, Complex, NME, GQ, Billboard) plus collaborators.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts, Grammys.
2) The core repeatable workflow/formula — chord-loop-first writing, sequenced album-as-movie, self-production.
3) Lyric method — bittersweet emotional specificity; chord-loop-driven vowels; revision over years.
4) Topline/singing method — his own sung hooks; melodic-rap topline; featured-vocalist contrast.
5) Vocal-anchoring production — brass/soul/live-instrument framing.
6) Proof songs (2020-2025 preferred) — 'St. Chroma', 'Noid', 'Darling, I', 'See You Again' recharting.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off; intentional craft over formula.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Apple Music Interviews, Complex, NME, GQ, Billboard). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE vs. what is deliberately one-off.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/14-tyler-the-creator.md
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