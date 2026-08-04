# Task for researcher

LANE: Olivia Rodrigo + Dan Nigro (writer-producer duo) — SOUR (2021, Hot 100 #1 'drivers license', 'good 4 u'), GUTS (2023, 'vampire' #1, 'bad idea right?'). DISTINCT ANGLE: Gen-Z pop-punk/confessional revival, diary-to-Hot-100-#1 pipeline; Nigro came from indie band As Tall As Lions and now co-writes/produces/records Olivia at his home studio with intentional 90s/2000s songcraft references (Paramore, Avril, Michelle Branch, Jack Antonoff lineage). SEAM: how a teenager's diary confession becomes a #1 single — TITLE-as-hook, specificity in nouns, ballad-then-angst song structure, Olivia's delivery (chest-belt + spoken-word bridges), and Dan's method of building topline on top of piano riffs from Olivia's Voice Memos. Get Nigro producer-interview quotes (And The Writer Is podcast, Trapital, Variety, Billboard, Rolling Stone) and Olivia's (Apple Music, NPR).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — documented step-by-step, as THIS pair actually does it (Voice Memo -> piano -> room co-write).
3) Lyric method — diary/biographical; specificity; title-as-hook; bridge dynamics.
4) Topline/singing method — chest-belt falsetto/mix; consonant-attack delivery; pop-punk aggro vs ballad ache; how the hook is SUNG.
5) Vocal-anchoring production — GUTS/SOUR live-band texture around the vocal.
6) Proof songs (2020-2025) — 'drivers license', 'good 4 u', 'vampire', 'bad idea right?'.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (And The Writer Is, Trapital, Variety, Billboard, Apple Music, Rolling Stone). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/08-olivia-rodrigo-dan-nigro.md
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