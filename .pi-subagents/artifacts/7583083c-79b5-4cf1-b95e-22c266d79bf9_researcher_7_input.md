# Task for researcher

LANE: Max Martin (Martin Sandberg; Swedish songwriter/producer) — the single most documented 'hit-every-time' methodologist in modern pop: co-wrote/co-produced The Weeknd 'Blinding Lights' Hot 100 #1 (longest top-10 run ever), 'Save Your Tears', 'Die For You'; earlier foundational Britney '...Baby One More Time', Katy 'Roar'/'Dark Horse', Taylor 'Shake It Off'. DISTINCT ANGLE: his repeatable methodology IS the 'how to make a famous song every time' blueprint — 'melodic math', thesis-chorus-repetition, no more than ~3 melodic parts, the 'monkey-chant test', the chorus must arrive before 60s, every section introduced with a new sound, repetition-with-variation. SEAM: the foundational framework is well-attested in John Seabrook's book 'The Song Machine' and long Rolling Stone/NYT profiles — frame this lane as the REFERENCE formula lane; show how Max's method STILL produces 2020-2025 Hot 100 hits via The Weeknd. Prioritize the book and direct producer quotes (Max rarely interviews — use Seabrook, vetted second-hand from co-producers like Shellback, Rami, Savan Kotecha, Oscar Holter).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — The Weeknd songs + chart reign.
2) The core repeatable workflow/formula — 'melodic math' step-by-step (chorus placement, parts count, monkey-chant test, new sound per section).
3) Lyric method — minimal-and-memorable; secondary to melody; how toplines dictate rhymes.
4) Topline/singing method — recording toplines; production-driven melody writing; the 'math' of repeated hooks.
5) Vocal-anchoring production — his method of weaving chorus with production drops.
6) Proof songs (2020-2025 preferred; older as theory demo) — 'Blinding Lights', 'Save Your Tears', 'Die For You'.
7) Direct quotes with attribution + SOURCE URL per quote (Max via Seabrook book / second-hand producers).
8) "The trick" in their words — the 'melodic math' as the repeatable engine.
9) Gaps (Max interviews are rare — note reliance on intermediaries).
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (John Seabrook 'The Song Machine', NYT, Rolling Stone, Billboard). Name the source.
- Skeptical; flag where quotes are second-hand.
- FOCUS on the repeatable topline/lyric FORMULA as documented.
- Emphasize what's REPEATABLE — this is the reference lane.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/10-max-martin.md
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