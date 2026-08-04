# Task for researcher

LANE: Kendrick Lamar (Compton; TDE/pgLang/Interscope) — Pulitzer for DAMN. (2017), Mr. Morale & The Big Steppers (2022), 2024-25 Drake-diss run ('Like That', 'Not Like Us' Hot 100 #1 + multiple 2025 Grammys, 'squabble up', GNX surprise album). DISTINCT ANGLE: unusually documented lyric process — notebooks, concept-album architecture, writes with producers Sounwave/DJ Dahi in Top Dawg's studio, plus co-writers (Terrace Martin, Baby Keem). SEAM: how he writes conceptually dense but hooky rap (double/triple entendres, narrative structures, polyrhythmic flow) AND how the sung-rapped topline of hooks like 'HUMBLE.', 'Not Like Us', 'N95' makes a hit bounce. Get Kendrick's, Sounwave's, DJ Dahi's, and Dave Free's direct quotes.

=== REQUIRED OUTPUT (markdown, into the file path given) ===
1) Verified credentials & 2020-2025 relevance — specific Billboard Hot 100 facts, RIAA, key releases.
2) The core repeatable workflow/formula — documented step-by-step from idea to finished master, as THIS person actually does it.
3) Lyric method — theme/story/rhyme/hook generation; room vs. top-down; tools (Voice Memos/notes); revision discipline.
4) Topline/singing method — melodic construction; phrasing; range/delivery; how the hook is SUNG.
5) Vocal-anchoring production — brief: what the track does around the vocal to make the hook land.
6) Proof songs (2020-2025 preferred) — name songs + what each shows of the formula + why it hit.
7) Direct quotes with attribution + SOURCE URL per quote — the artist/writer/producer explaining how to make a song that works.
8) "The trick" in their words — the ONE thing they say makes it land; repeatable vs. one-off.
9) Gaps / uncertainties.
10) Sources — kept (with URLs) vs. dropped (why).

=== CONSTRAINTS ===
- web_search ALWAYS with workflow:"none".
- PRIORITIZE primary sources: named interviews/podcasts/magazine profiles/books. Name the source for each claim.
- Skeptical by default: separate verified quotes from internet legend/lore. Note when a claim is unsourced.
- FOCUS on lyric writing + singing/topline; treat production only as scaffolding for the vocal.
- Emphasize what's REPEATABLE across their hits for the 'how to make a famous song every time' answer.
- No taboos: report credit/ghostwriting/controversy facts frankly where they affect the answer.
- End with concise kept/dropped source list.

---
**Output:**
Write your findings to exactly this path: C:/Users/intel/DevelopmentProjectTemplate/b0ttsagent/research/songwriting-formulas/briefs/01-kendrick-lamar.md
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