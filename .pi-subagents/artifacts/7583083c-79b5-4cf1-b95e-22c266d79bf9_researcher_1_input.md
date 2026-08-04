# Task for researcher

LANE: Drake (Aubrey Graham; OVO/Republic) — holds the record for most Billboard Hot 100 entries ever. Recent 5 yr: Certified Lover Boy (2021), Honestly, Nevermind (2022), Her Loss (2022 w/ 21 Savage), For All The Dogs (2023), Scary Hours 3, $ome $exy $ongs 4 U (2025 w/ PartyNextDoor). DISTINCT ANGLE: prolific genre-hopping hit machine with a specific melodic-rap-singing hook method (the 'Drake melody', unshakeable earworm hooks). SEAM: monthly output volume, freestyle vs. written, rotating writer-producer team system (Boi-1da, Gordo, Lil Yachty, Southside, PartyNextDoor, Noah '40' Shebib), and how singable hooks like 'First Person Shooter', 'Rich Baby Daddy', 'Nokia', 'Slime You Out' are built. Handle the long-running ghostwriting/credit controversy (Quentin Miller/Meek Mill 2015; 2024-25 Kendrick 'Like That'/'Not Like Us' allegations; reference-tracks) as no-taboos — just report documented credit/collaborator FACTS. Get Drake's own quotes plus producers (Boi-1da, Gordo, Noah '40' Shebib, Southside).

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts, RIAA, key releases.
2) The core repeatable workflow/formula — documented step-by-step from idea to finished master, as THIS person actually does it.
3) Lyric method — theme/story/rhyme/hook generation; room vs. top-down; tools (Voice Memos/notes); revision discipline.
4) Topline/singing method — melodic construction; phrasing; range/falsetto/stacking/autotune; how the hook is SUNG; delivery.
5) Vocal-anchoring production — brief: what the track does around the vocal to make the hook land.
6) Proof songs (2020-2025 preferred) — name songs + what each shows of the formula + why it hit.
7) Direct quotes with attribution + SOURCE URL per quote — the artist/writer/producer explaining how to make a song that works.
8) "The trick" in their words — the ONE thing they say makes it land; repeatable vs. one-off.
9) Gaps / uncertainties.
10) Sources — kept (with URLs) vs. dropped (why).

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources: named interviews (Apple Music, Complex, OVO Sound Radio), Billboard, Rolling Stone, NYT, Vulture, Rap Radar podcast. Name the source.
- Skeptical by default: separate verified quotes from internet legend.
- FOCUS on lyric writing + singing/topline; production only as scaffolding for the vocal.
- Emphasize what's REPEATABLE across their hits for 'how to make a famous song every time'.
- No taboos: report credit/ghostwriting/controversy facts frankly.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/02-drake.md
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