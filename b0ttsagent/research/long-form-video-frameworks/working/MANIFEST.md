# MANIFEST — long-form-video-frameworks run (resume index)

Run: Deep-Documented Long-Form Video Workflows V3
Started: 2026-08-29
Target: 12-15 verified PASS -> 10-15 shortlist -> case studies -> synthesis
Tooling: yt-dlp = `python -m yt_dlp` (bare `yt-dlp` may not resolve in subagent shells)
Wave 01 | Phase 0 Discovery | OK | 30 candidates (A=12 B=10 C=8), deduped, schema-complete | next: Phase 1 verification waves
Wave 02 (attempt 1) | Phase 1 Verification | FAIL-TOOLING | b0tts-researcher workers had no shell -> no yt-dlp, estimate-grade counts | fix: re-run wave-02 with b0tts-general-agent workers
Wave 02 (re-run) | Phase 1 Verification | OK | 4 PASS (mrbeast 1.0, mark-rober 0.9, johnny-harris 0.67, mkbhd 0.654) exact yt-dlp counts | next: wave-03 (veritasium, ryan-trahan, ali-abdaal, tom-scott)
Wave 03 | Phase 1 Verification | OK | 3 PASS (veritasium 0.841, tom-scott 0.543, ryan-trahan 0.516), 1 REJECT (ali-abdaal 50% hit-rate) | run total 7 PASS | next: wave-04
Wave 04 | Phase 1 Verification | OK | 4 PASS (kurtis-conner 0.705, colin-and-samir 0.460, matt-davella 0.428, thomas-frank 0.261) | run total 11 PASS | next: wave-05
Wave 05 | Phase 1 Verification | OK | 3 PASS (drew-gooden 0.735, wendover-productions 0.543, dan-mace 0.269), 1 REJECT (solar-sands, no 2021-2026 first-party workflow doc) | run total 14 PASS | next: wave-06
Wave 06 | Phase 1 Verification | OK | 3 PASS (airrack 0.894, linus-tech-tips 0.55, mina-le 0.527), 1 REJECT (dan-koe 58.3% hit-rate) | run total 17 PASS > 15 cap | next: Phase 1.5 dedup+cull
Phase 1.5 | Cull gate (orchestrator) | cuts: thomas-frank (0.261, dormant 890d), dan-mace (0.269, dormant 274d) -> shortlist 15 | rejects logged: ali-abdaal, solar-sands, dan-koe | next: Phase 2 deep-dives
Phase 2 | Deep-dive | delegated to a b0tts-general-agent phase orchestrator (per user) | plan: working/waves/phase-2-plan.md | waves 07-10 | next: phase orchestrator report
Wave 07 | Phase 2 Deep-dive | OK | mrbeast DEPTH-PASS, mark-rober DEPTH-PASS, airrack DEPTH-PASS (3/3) | next: wave-08
Wave 08 | Phase 2 Deep-dive | OK | veritasium DEPTH-PASS, drew-gooden DEPTH-PASS, kurtis-conner DEPTH-PASS, johnny-harris DEPTH-PASS (4/4) | next: wave-09
Wave 09 | Phase 2 Deep-dive | PARTIAL | wendover-productions DEPTH-PASS; mkbhd, linus-tech-tips, tom-scott SKIPPED (user decision) | next: wave-10
Wave 09 (final) | Phase 2 Deep-dive | PARTIAL | wendover, mkbhd, linus-tech-tips DEPTH-PASS; tom-scott NOT-COMPLETED (agent crashes) | next: wave-10
Wave 10 (final) | Phase 2 Deep-dive | PARTIAL | mina-le, ryan-trahan DEPTH-PASS; colin-and-samir, matt-davella NOT-COMPLETED (agent crashes) | next: phase closed
Phase 2 | Deep-dive | CLOSED by user | 12/15 case studies; 3 NOT-COMPLETED (tom-scott, colin-and-samir, matt-davella) after repeated subagent crashes | next: Phase 3 synthesis
Phase 3 | Synthesis | OK | README.md, recurring-patterns.md (21 patterns, claim-frequency table), source-library.md written by b0tts-smart-agent | 12 case studies + 3 shortlist-only creators | RUN CLOSED 2026-08-30
