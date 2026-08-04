# Task for researcher

LANE: Twenty One Pilots (Tyler Joseph — writes/sings/produces with drummer Josh Dun) — Scaled and Icy (2021), Clancy (2024, 'Overcompensate', 'Next Semester', 'The Craving'); earlier Hot 100 monoliths 'Stressed Out', 'Heathens'. DISTINCT ANGLE: conceptual worldbuilding + one-man-band songcraft (Tyler writes/produces most in home studio, deliberately 'do everything myself' to protect authorship); built via internet grassroots; hyper-specific imagery in lyrics (Trench/Clancy lore, Bandito) and genre-blend hooks that pop despite unconventional time/groupings. SEAM: how Tyler builds hooks while eschewing the LA co-write, his 'write the music then pore over it endlessly' overhaul method, vocal delivery (nasal-falsetto rapper-singer), and the concept-album metaverse which deepens loyalty & repeat play. Get Tyler Joseph & Josh Dun quotes (AltPress, NME, Zane Lowe/Apple Music, Rock Sound, Kerrang).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts.
2) The core repeatable workflow/formula — home-studio one-man-band process, concept-album sequencing.
3) Lyric method — specific imagery; biography; the revision/overhaul method; streams-of-consciousness edited later.
4) Topline/singing method — nasal falsetto, rap-singer delivery, ukulele/piano hook construction.
5) Vocal-anchoring production — self-produced beats framing the rap-singing topline.
6) Proof songs (2020-2025 preferred) — 'Overcompensate', 'Next Semester', 'The Craving', 'Shy Away' (2021).
7) Direct quotes with attribution + SOURCE URL per quote.
8) "The trick" in their words — repeatable vs. one-off.
9) Gaps.
10) Sources — kept vs. dropped.

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources (AltPress, NME, Apple Music, Rock Sound, Kerrang). Name the source.
- Skeptical; separate verified quotes from legend.
- FOCUS on lyric writing + singing/topline.
- Emphasize what's REPEATABLE.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/13-twenty-one-pilots.md
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