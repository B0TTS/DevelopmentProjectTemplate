# Task for researcher

Research documented, repeatable YouTube video-making workflows used by established creators with 1M+ YouTube subscribers. Must include MrBeast and Jenny Hoyos, plus at least 6 other creators across gaming/Minecraft, challenge/storytelling, education, commentary, business/software, or podcasts. Prioritize primary sources: creator interviews, talks, podcasts, official channel/creator resources, direct statements. Find specific formulas/workflows, not generic advice. For each creator, provide: evidence URL, exact claim or passage summary, what is creator-reported vs your inference, audience/channel scale evidence, and practical transfer to a Minecraft Hardcore long-form channel with 6h recording + Sunday editing. Also find YouTube official guidance on retention, thumbnails/titles, audience satisfaction. Do not edit project files. Return a structured research brief with URLs and caveats; flag weak or unverifiable claims.

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