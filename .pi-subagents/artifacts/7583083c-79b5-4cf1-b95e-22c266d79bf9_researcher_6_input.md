# Task for researcher

LANE: Jack Antonoff — Bleachers frontman + the defining pop producer-writer of the 2020s (Taylor Swift Midnights/TTPD/folklore-adjacent, Lorde 'Solar Power'/earlier 'Melodrama' producer, Clairo 'Sling'/'Immunity', Lana Del Rey 'Did you know that there's a tunnel under Ocean Blvd', Sabrina Carpenter 'Short n' Sweet' 2024 'Espresso'/'Please Please Please', Kevin Abstract). DISTINCT ANGLE: 'writing/producing in the room, no matter how big the artist' philosophy, runs his own small studio (Electric Lady + his home '2088'), punch-in vocals, 80s-indebted Bleachers hooks; 'specific taste is the weapon'. SEAM: the Bleachers->Taylor/Lana/Sabrina TRANSFERABLE workflow — how Antonoff makes songs with a consistent sonic signature while letting the artist's voice dominate; his quote 'I'm only trying to make songs that sound like they've always existed.' Get Antonoff quotes (NYT, Vulture, New York mag profile, Apple Music, NME, Pitchfork) and his stated Bleachers songwriting process.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts across his productions.
2) The core repeatable workflow/formula — the in-room writing/producing methods he repeats across artists.
3) Lyric method — how he writes/co-writes with stars; contribution rules; lyrical plain-spokenness.
4) Topline/singing method — he co-derives melodies live in room; punch-ins; he sings guide vocals; rhyme/payoff discipline.
5) Vocal-anchoring production — 80s drums/strings/synth pads framing the vocal (Antonoff signature).
6) Proof songs (2020-2025 preferred) — e.g. Taylor 'Anti-Hero'/'Cruel Summer', Sabrina 'Espresso'/'Please Please Please', Lorde 'Solar Power' (2021), Lana 'A&W'/'Did You Know'.
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (NYT, Vulture, New York magazine, Pitchfork, Apple Music). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline orchestration as a co-writer-producer.
- Emphasize what's REPEATABLE across artists.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/09-jack-antonoff.md
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