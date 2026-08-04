# Task for researcher

LANE: Andrew Watt (Andrew Wotman) — current superstar producer-writer-guitarist (Post Malone country F-1 Trillion 'I Had Some Help' ft. Morgan Wallen 2024 Hot 100 #1; Post 'Pour Me A Drink' w/ Blake Shelton; Justin Bieber; Elton John 'Cold Heart' w/ Dua Lipa; Dua Lipa 'Dance The Night'; Rolling Stone Producer of the Year 2021). DISTINCT ANGLE: cross-genre (pop/rock/hip-hop/country) writer-producer who lands hits by treating the session like a BAND — co-writing toplines on acoustic guitar, building full-band productions around a killer vocal, working face-to-face in the studio. SEAM: how to write a hook that survives across genre (Post Malone's country 'I Had Some Help', 'Pour Me A Drink'), the acoustic-hook-FIRST workflow, and his stance on 'songwriting as band chemistry'. Get Andrew Watt quotes (Billboard, Variety, Lefsetz Letter, Apple Music) plus collaborators like Post Malone, Louis Bell.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts across cross-genre hits.
2) The core repeatable workflow/formula — documented step-by-step (acoustic hook -> band arrangement -> vocal -> full production).
3) Lyric method — co-writing in-room with the artist; what he prioritizes in lyrics.
4) Topline/singing method — guitar-accompanied melody writing; chest-voice hooks; phrasing across genres.
5) Vocal-anchoring production — band arrangements building around the vocal.
6) Proof songs (2020-2025 preferred) — 'I Had Some Help', 'Pour Me A Drink', 'Dance The Night' (2023), Elton/Dua collabs.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Billboard, Variety, Rolling Stone, Lefsetz, Apple Music). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE across genre.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/11-andrew-watt.md
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