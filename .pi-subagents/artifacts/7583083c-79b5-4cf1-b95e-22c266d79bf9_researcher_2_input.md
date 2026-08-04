# Task for researcher

LANE: Taylor Swift — folklore/evermore (2020), 'All Too Well (10 Minute Version)', Midnights (2022, Hot 100 #1 'Anti-Hero'), Speak Now TV, 1989 TV, THE TORTURED POETS DEPARTMENT (2024, biggest streaming week ever, 'Fortnight'). DISTINCT ANGLE: the most commercially consistent songwriter of her generation, with unusually well-documented songcraft discipline. SEAM: her specific narrative-detail method (random hook/title lists in a notes-app 'bright blue folder', 'third-verse plot twist', bridges that resolve, dropping specific nouns/names/places), co-writer rotation (Aaron Dessner, Jack Antonoff, earlier Max Martin + Shellback), and why each approach yields consistent chart + cultural dominance; conversational-plain-midrange vocal delivery singing the hook. Get Taylor's songwriting-process quotes (Song Exploder, Rolling Stone, NPR, Billboard, Variety) plus Aaron Dessner and Jack Antonoff.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step, as THIS person actually does it.
3) Lyric method — theme/story/rhyme/hook generation; the notes-app lists; bridge discipline; specificity of nouns.
4) Topline/singing method — melodic construction; phrasing; conversational midrange; how the hook is SUNG.
5) Vocal-anchoring production — brief: what Dessner/Antonoff do around her vocal.
6) Proof songs (2020-2025 preferred) — 'Anti-Hero', 'Cruel Summer' recharting, 'Fortnight', 'All Too Well (TMV)'.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (Song Exploder, Rolling Stone, Variety, NPR, Billboard). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE across her hits.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/05-taylor-swift.md
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