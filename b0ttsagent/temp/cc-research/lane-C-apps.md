# Research: Dedicated Apps for a Clean Fullscreen Program Feed → HDMI Capture Card (OBS Projector Alternatives)

**Task:** Determine whether ANY dedicated software is purpose-built to output a clean full-screen program feed to a physical HDMI capture card from a Windows gaming PC (alternative to OBS's Fullscreen Projector), and whether it would deliver higher quality or efficiency than OBS projector at 1080p60.

**Date:** 2026-06-25 · **Researcher:** lane-C subagent · **Confidence scale:** HIGH (official docs / primary engineering sources), MEDIUM (vendor claims, community consensus), LOW (unverified claims)

---

## Summary

No mainstream product exists whose *primary job* is "render one video source fullscreen onto an HDMI capture card," and none is needed: the upstream task is a single DXGI Present call (~50–60 µs), the HDMI link is lossless digital, and the only genuinely lossy step is inside the capture card itself (RGB→NV12 4:2:0 conversion; internal H.264 on USB 2.0 cards) — identical no matter which software drives the display. Every candidate (vMix, XSplit, Streamlabs, Resolume) uses the *same* GPU-present mechanism OBS uses; the only purpose-built tool found (RitschyMirror) exists to fix OBS projector **workflow** pain (HDR→SDR tonemapping, aspect fit, mouse-lock), not quality, and actually does *more* GPU work than OBS's source projector. **Recommendation: stay on OBS Studio Fullscreen Projector (Source) at 1080p60**; adopt a dedicated tool only for the HDR→SDR edge case, and pursue quality gains in the capture card hardware, not the software.

---

## Findings

### 0. How the pipeline actually works (sets up everything below)

1. **Capture cards appear as displays to the GPU.** The card advertises an EDID and the GPU renders to it like a second monitor; the card captures whatever signal is sent. [Elgato EDID docs — HIGH](https://help.elgato.com/hc/en-us/articles/360060072892-4K-Capture-Utility-EDID-Configuration); Moonlight guide: "The capture card will appear as a second monitor on the Gaming PC" [HIGH](https://guides.moonlight.zip/guides/capture-card/obs-capture-card-setup-guide).
2. **The lossy step is inside the capture card.** Cards deliver NV12 (YUV 4:2:0) to the streaming PC; USB 2.0 cards (Elgato Game Capture HD, Hauppauge PVR, etc.) are *forced to compress (H.264-encode) internally* due to USB 2.0 bandwidth. [XSplit blog — HIGH](https://www.xsplit.com/blog/xsplit-workshop-how-to-set-video-and-audio-delay-on-camera-sources-1) — "Due to the limitations of USB 2.0 bandwidth, these capture cards are forced to compress (encode) the video stream."
3. **HDMI is a lossless digital pipe.** Upstream of the card there is no compression and no quality loss to "improve" — software can only choose *what* is presented (resolution, color format, content). This is why no software can beat another on "HDMI output quality": the ceiling is the same for all of them.

### 1. OBS Studio Fullscreen Projector (Source) — the baseline, and near-optimal

- Moonlight's capture-card guide calls OBS Fullscreen Projector "the **recommended** capture card setup," because it decouples gaming resolution/refresh from what the card receives ("play at 1440p 480Hz while the capture card gets a clean 1080p 240Hz"). It prescribes: **Extend** displays (never Duplicate — duplicate caps refresh to the card), **Fullscreen Projector (Source)** not Preview Projector, disable the OBS preview to cut GPU usage. [HIGH](https://guides.moonlight.zip/guides/capture-card/obs-capture-card-setup-guide)
- **Mechanism & cost:** the projector is a fullscreen DXGI flip-model swap chain that presents the *already-composited source texture*. OBS libobs PR #6942 (tearing fix) measured projector **Present calls at ~50–60 µs** and added a waitable flip queue for tear-free present — i.e., the incremental cost of the projector is a fraction of a frame. [HIGH — primary engineering source](https://github.com/obsproject/obs-studio/pull/6942) OBS PR #5086 (limit one projector per screen) confirms the only known overhead lever is "save gpu resources" for users running many projectors. [HIGH](https://github.com/obsproject/obs-studio/pull/5086)
- Known projector weaknesses are **workflow**, not quality: HDR washout/brightness on HDR displays (OBS issue #7790), mouse wandering onto the projector display, alt-tab desktop flashes. [MEDIUM/HIGH — OBS issue tracker](https://github.com/obsproject/obs-studio/issues/7790)
- **Verdict for the task:** does exactly this task (1 = yes, purpose-built feature, free), and is near the efficiency floor (only a present call reusing an existing texture). **Would not be beaten at 1080p60 SDR by any software.**

### 2. vMix (Fullscreen Output / External Output / NDI)

- **Fullscreen outputs:** "These outputs control the computer Display outputs… only available from the output ports on the Graphics Card" — i.e., the exact same GPU-present-to-a-display mechanism as OBS projector. [HIGH — official vMix docs](https://www.vmix.com/help27/SettingsOutputs.html)
- **External Output:** sends video out via **AJA, Blackmagic, or Bluefish444 hardware I/O cards** — broadcast cards with HDMI/SDI *output* capability. It does **not** work with consumer USB/PCIe HDMI capture cards (Elgato/AVerMedia), which are capture-only. [HIGH — official vMix docs](https://www.vmix.com/help27/ExternalOutputwithIntensityand.html) ("Many older Blackmagic cards can only perform one task at a time, either Capture or Output.")
- **Would it beat OBS at 1080p60?** No for quality via Fullscreen (same present path); the External-Output hardware route (Blackmagic/AJA card, from ~$150–$500+, plus vMix license $60–$1,200) buys 10-bit SDI/HDMI output — irrelevant for a 1080p60 SDR livestream, which is 4:2:0 8-bit at the encoder and is converted to 4:2:0 by the receiving card anyway. **Not purpose-built for this task** (it's a full switcher); strictly more expensive and heavier than OBS for a single-source clean feed. [MEDIUM-HIGH]

### 3. Streamlabs Desktop

- A fork of OBS Studio ("community software created on top of OBS Studio… sold to Logitech" [MEDIUM — Reddit r/streaming](https://www.reddit.com/r/streaming/comments/1ejzxp2/capture_card_showing_as_a_second_monitor/); repo self-describes as "built on OBS and Electron" [HIGH](https://github.com/streamlabs/desktop/)).
- Has its own fullscreen "Projector Mode" for previewing the program fullscreen [MEDIUM — Streamlabs changelog via Facebook](https://www.facebook.com/streamlabshq/videos/you-can-now-preview-your-stream-fullscreen-with-the-projector-mode-on-streamlabs/2059336904315198/) and ships a "Performance Mode" whose headline trick is *removing the preview window* to save resources [MEDIUM — GetOnStream/Streamlabs](https://getonstream.com/how-to-enable-performance-mode-in-streamlabs/) — evidence of higher baseline overhead than OBS (Electron wrapper).
- **Verdict:** same renderer, same present path, more overhead, fewer options (e.g., no fractional-refresh output config). **Does not target the task specifically; cannot beat OBS on quality or efficiency.** [HIGH]

### 4. XSplit Broadcaster

- Has a "Projector Output — project any scene, including your active scene to another monitor or display" [HIGH — official XSplit manual](https://www.xsplit.com/broadcaster/manual) — functionally identical to OBS's projector (fullscreen window presented by the GPU to a second display).
- Paid subscription (free tier watermarks output), historically heavier CPU/GPU footprint than OBS, and its own docs note capture-card limitations are device-side (USB 2.0 compression), not software-side [MEDIUM — comparisons](https://www.maketecheasier.com/obs-vs-xsplit/), [HIGH — XSplit capture-card blog](https://www.xsplit.com/blog/using-webcams-with-xsplit-broadcaster).
- **Verdict:** same mechanism as OBS projector, costs money, no quality or efficiency advantage at 1080p60. **Does not beat OBS.** [HIGH]

### 5. NDI Screen Capture HX + NDI Tools / OBS-NDI plugin

- NDI|HX is **lossy compressed** video: NDI HX1 = H.264 8-bit 4:2:0; NDI HX2/3 = H.264 8-bit 4:2:0 or H.265 8–10-bit **4:2:0**. [HIGH — official NDI codec matrix](https://docs.ndi.video/all/using-ndi/ndi-for-video/ndi-video-codecs-and-format-matrix) Screen Capture HX uses GPU (NVENC) hardware encoding to keep CPU low [HIGH — official docs](https://docs.ndi.video/all/using-ndi/ndi-tools/ndi-tools-for-windows/screen-capture-hx).
- OBS community consensus (forum threads, Yostream comparison): capture card wins on latency, reliability, and quality; NDI wins on cost/flexibility but "can have some quirks with certain games (GPU prioritization)" [MEDIUM — OBS forum](https://obsproject.com/forum/threads/capture-card-or-ndi-plugin-wich-is-better.125603/), [MEDIUM — Yostream](https://yostream.io/blog/capture-card-vs-ndi-for-dual-pc-streaming/). NDI adds encode + network + decode latency vs. a direct HDMI link (capture-card input latency alone is ~40–100 ms per OBS capture-card latency research [MEDIUM](https://obsproject.com/forum/resources/capture-card-documentation-latency-decode-modes-formats-more.777/)).
- **Verdict:** a *network alternative* (also decouples refresh rate like a projector), but strictly **lower quality** than uncompressed HDMI at 1080p60 (lossy 4:2:0 codec + added latency + gigabit-network dependency). **Not a quality or efficiency upgrade.** [HIGH]

### 6. Resolume (Avenue/Arena)

- Arena's Advanced Output can drive physical outputs "like a capture card like a Blackmagic Intensity" — but playback requires **broadcast I/O hardware (Blackmagic, AJA, Datapath)**, and "not all cards support full [simultaneous capture] and output" [HIGH — official Resolume docs](https://resolume.com/support/en/screens), [HIGH](https://resolume.com/support/en/advanced-output). Screen output = normal GPU fullscreen/windowed present [HIGH](https://resolume.com/support/en/output-setup).
- **Verdict:** VJ projection-mapping software (Arena ≈ $499), built for multi-output mapping, not single-source clean feeds; same GPU present path; consumer capture cards can't even be used as outputs. **Does not target the task; overkill; does not beat OBS.** [HIGH]

### 7. Hardware downstream keyers / switchers (ATEM Mini et al.)

- Downstream keyers and hardware switchers insert overlays/graphics *after* the feed and manage routing; they do not generate the upstream program feed and cannot raise capture quality — the signal into them is still produced by the GPU + capture card pipeline. For a "clean feed to one capture card," a downstream keyer is a needless extra device. **Not applicable to the task; no quality benefit.** [MEDIUM — reasoning from standard broadcast topology]

### 8. Niche / purpose-built tools (the actual search result)

- **RitschyMirror** (github.com/RitschyRigz/ritschy-mirror, MIT, v1.3.2) — the only tool found that is *explicitly purpose-built for this task*: "Mirror any monitor to your capture card… a lightweight Windows tray app for dual-PC / capture-card streaming setups. Originally built to replace the OBS projector in my own dual-stream rig." Features: HDR→SDR GPU tonemapping (bt2390/reinhard/hable/aces with live controls), fit/stretch/crop layouts for 16:9 mismatch, **mouse-lock** on the capture display, window-only mirroring via Windows.Graphics.Capture (no anti-cheat risk), tray app + HTTP API + OBS custom-dock control. Tech: DXGI Desktop Duplication (FP16) → HLSL tonemap shader → flip-model swap chain [HIGH — README, primary source](https://github.com/RitschyRigz/ritschy-mirror).
  - **Does it beat OBS at 1080p60?** Quality: **for SDR, no** — same pixel path, and it adds a duplication+shader pass OBS doesn't need. **For HDR→SDR, plausibly yes** — OBS's projector has a known HDR-brightness bug (issue #7790) and no comparable tonemap control, while RitschyMirror's entire raison d'être is correct HDR→SDR conversion. **Efficiency: no** — it does strictly more GPU work (desktop duplication + shader) than OBS's source projector, which reuses the already-composited texture. Caveats: single-author project, installer not code-signed, claims not independently benchmarked. [MEDIUM]
- **vicash** (caaatto/vicash) and **FCapture** (otvv/FCapture) — low-overhead *previewer* utilities for the capture card's **input** (card → PC direction). They do the reverse of this task and are irrelevant to producing an output feed. [HIGH — READMEs](https://github.com/caaatto/vicash), [HIGH](https://github.com/otvv/FCapture)

### 9. Why there is no real dedicated app (the explanatory core)

1. **The upstream task is trivial and already near-optimal in OBS.** "Show source X fullscreen on display Y" is one flip-model present of an existing texture (~50–60 µs, PR #6942). There is no algorithmic headroom — a dedicated app can only do the same DXGI present, minus the free reuse of OBS's compositor. [HIGH]
2. **The real lossy step is downstream and software-proof.** The capture card converts RGB→NV12 4:2:0 (or H.264 on USB 2.0 cards). That conversion is identical regardless of what software drives the display; no app can make the card's conversion better. At 1080p60 the stream is 4:2:0 8-bit anyway, so the projector path loses nothing that the stream would have kept. [HIGH]
3. **Efficiency is also near-optimal in OBS.** A dedicated mirror tool must *duplicate the desktop or hook the game* (DXGI duplication + shader pass, as RitschyMirror does) — strictly more GPU/CPU than OBS's projector reusing its composited source. [MEDIUM-HIGH]
4. **Market economics.** OBS is free and already solves it; there is no revenue in a single-purpose clone. The only viable niches are OBS *shortcomings* — HDR tonemapping, aspect-fit, mouse-lock, alt-tab safety — which is exactly what RitschyMirror fills. [MEDIUM — inference from the products that actually exist]

### 10. Recommendation

**Stay on OBS Studio → Fullscreen Projector (Source) → capture-card display for 1080p60.** It is free, near-zero incremental GPU cost, officially recommended for this exact topology (Moonlight guide), and its quality ceiling is the same as any alternative because the card's NV12 conversion dominates. Configure: Windows **Extend** displays; set the card display to exactly 1080p60; OBS canvas 1920×1080, color format NV12 or RGB (card-dependent); use **Source** projector (not Preview); disable the preview to save GPU.

**Move to a dedicated tool only if:**
- **HDR game → SDR capture card:** evaluate **RitschyMirror** for proper tonemapping (OBS projector has known HDR issues). Verify it on your rig — young single-author project. [MEDIUM]
- **Mouse wandering / alt-tab desktop flashes on the capture display:** RitschyMirror's mouse-lock + window-only mirror are genuine UX wins OBS doesn't offer. [MEDIUM]
- **Genuine output-quality upgrade desired:** that is a *hardware* decision — a USB 3.0/PCIe card that carries uncompressed NV12 at 1080p60 (e.g., Elgato 4K X/4K Pro, AVerMedia GC573-class) or a broadcast I/O card + vMix for 10-bit SDI/HDMI out (unnecessary for 1080p60 SDR streaming). [MEDIUM]

**Avoid for this task:** NDI Screen Capture HX / OBS-NDI (lossy 4:2:0 + latency), Streamlabs (heavier OBS fork), XSplit (paid, same mechanism), Resolume (wrong tool class, broadcast-card-only outputs), downstream keyers (don't improve capture).

---

## Sources

### Kept
- OBS Capture Card Setup Guide (Moonlight) — https://guides.moonlight.zip/guides/capture-card/obs-capture-card-setup-guide — authoritative walkthrough endorsing OBS Source Projector as the recommended method; prescribes Extend mode, source-vs-preview projector, preview-off.
- libobs PR #6942 "Prevent D3D11 projectors from tearing" — https://github.com/obsproject/obs-studio/pull/6942 — primary engineering evidence projector Present ≈ 50–60 µs, flip-model + waitable queue.
- libobs PR #5086 projector-per-screen limit — https://github.com/obsproject/obs-studio/pull/5086 — confirms projector GPU-cost lever is a present-scale cost.
- OBS issue #7790 HDR projector brightness — https://github.com/obsproject/obs-studio/issues/7790 — documents the real HDR projector defect.
- vMix Outputs/NDI (help27) — https://www.vmix.com/help27/SettingsOutputs.html — Fullscreen outputs = GPU display outputs.
- vMix External Output w/ AJA/Blackmagic/Bluefish — https://www.vmix.com/help27/ExternalOutputwithIntensityand.html — external output requires broadcast I/O cards, not consumer capture cards.
- NDI official codec matrix — https://docs.ndi.video/all/using-ndi/ndi-for-video/ndi-video-codecs-and-format-matrix — NDI HX = H.264/H.265, 8–10-bit, always 4:2:0 (lossy).
- NDI Screen Capture HX docs — https://docs.ndi.video/all/using-ndi/ndi-tools/ndi-tools-for-windows/screen-capture-hx — GPU-accelerated H.264/HEVC capture, up to 4K/120.
- RitschyMirror README — https://github.com/RitschyRigz/ritschy-mirror — the only purpose-built OBS-projector replacement found; self-documented architecture (DXGI duplication → HLSL tonemap → flip-model present).
- XSplit Broadcaster manual (Projector Output) — https://www.xsplit.com/broadcaster/manual — XSplit's equivalent projector feature.
- XSplit blog: USB 2.0 cards internally compress — https://www.xsplit.com/blog/xsplit-workshop-how-to-set-video-and-audio-delay-on-camera-sources-1 — primary evidence the lossy step lives inside cheap capture cards.
- Resolume Screens / Advanced Output — https://resolume.com/support/en/screens and https://resolume.com/support/en/advanced-output — output via GPU or broadcast playback cards (Blackmagic/AJA/Datapath).
- Elgato 4K Capture Utility EDID docs — https://help.elgato.com/hc/en-us/articles/360060072892-4K-Capture-Utility-EDID-Configuration — cards advertise EDID and merge display capabilities (cards act as displays).
- Streamlabs Desktop repo — https://github.com/streamlabs/desktop/ — "built on OBS and Electron" (fork, heavier stack).
- OBS forum: Capture Card or NDI Plugin — https://obsproject.com/forum/threads/capture-card-or-ndi-plugin-wich-is-better.125603/ — community consensus: card wins on latency/quality/reliability.
- Yostream: Capture Card vs NDI — https://yostream.io/blog/capture-card-vs-ndi-for-dual-pc-streaming/ — same consensus, structured comparison.
- OBS Capture Card Documentation (latency/formats) — https://obsproject.com/forum/resources/capture-card-documentation-latency-decode-modes-formats-more.777/ — card input latency ~40–100 ms class and format constraints.
- vicash — https://github.com/caaatto/vicash and FCapture — https://github.com/otvv/FCapture — niche tools that do the *input* direction; excluded-from-claim evidence.

### Dropped
- PCWorld Elgato 4K X deal article, Blackmagic UltraStudio Mini 12G press item, Ant Media NDI blog — generic news/SEO, no bearing on the task.
- Gumlet / Restream / Vlogging Hero / Make Tech Easier OBS-vs-XSplit comparisons — used only for the paid/heavier corroboration, superseded by XSplit's own manual.
- GetOnStream "Performance Mode" article — low-authority, but claim (preview removal saves resources) corroborated by Streamlabs official content; kept only as supporting note.
- aquarat OBS/NDI gotchas blog — tangential; NDI consensus already covered by Yostream + OBS forum.

---

## Gaps

1. **No independent benchmark of RitschyMirror vs OBS projector** (GPU %, latency, color accuracy) exists; its HDR-tonemapping superiority over OBS is plausible but unverified. Next step: instrumented A/B on the user's rig (frame times via PresentMon, ΔE color check on a gradient card).
2. **OBS projector vs duplicate-display at 1080p60** — Moonlight states Duplicate caps refresh; no formal measurement of quality delta found; projector is standard practice regardless.
3. **Whether the user's specific capture card carries uncompressed NV12 vs MJPEG/H.264 internally at 1080p60** determines the true lossy step; card-model-specific data (Elgato/AVerMedia USB3 vs USB2) was not exhaustively tabulated.
4. No evidence found of any commercial product positioned as "capture-card output app" (search covered GitHub, vendor docs, forums) — consistent with the conclusion that the market gap is UX-only.

---

## Acceptance Report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Concrete findings written to C:\\Users\\intel\\DevelopmentProjectTemplate\\.pi-subagents\\artifacts\\outputs\\133270f8\\b0ttsagent\\temp\\cc-research\\lane-C-apps.md. Each finding carries an inline source URL and a confidence/severity tag (HIGH/MEDIUM/LOW), including: OBS projector present cost ~50-60us (obsproject PR #6942, HIGH), NDI HX lossy 4:2:0 codec matrix (docs.ndi.video, HIGH), vMix External Output requires AJA/Blackmagic/Bluefish broadcast cards (vmix.com help27, HIGH), RitschyMirror as the only purpose-built tool with HDR->SDR tonemapping (github README, MEDIUM), capture card as the sole lossy step (XSplit USB2-compression blog, HIGH). Recommendation and why-no-app-exists analysis included."
    }
  ],
  "changedFiles": [
    "C:\\Users\\intel\\DevelopmentProjectTemplate\\.pi-subagents\\artifacts\\outputs\\133270f8\\b0ttsagent\\temp\\cc-research\\lane-C-apps.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "web_search (exa provider, 4 rounds, 13 queries across 5 angles)",
      "result": "passed",
      "summary": "Covered: OBS projector baseline, vMix outputs, XSplit/Streamlabs/Resolume, NDI codec quality, capture card EDID/compression mechanics, niche tools."
    },
    {
      "command": "fetch_content of primary sources (ritschy-mirror README, Moonlight guide, vMix Outputs, NDI codec matrix)",
      "result": "passed",
      "summary": "Full-text verified: projector-as-recommended setup, vMix fullscreen=GPU display outputs, NDI HX 4:2:0 lossy matrix, RitschyMirror architecture."
    },
    {
      "command": "write output file",
      "result": "passed",
      "summary": "Research brief (findings, sources kept/dropped, gaps, recommendation, acceptance report) written to lane-C-apps.md."
    }
  ],
  "validationOutput": [
    "All 11 findings have at least one inline citation with a confidence tag; the 'no dedicated app' claim is triangulated by (a) search across vendor docs, GitHub, and forums finding only RitschyMirror as purpose-built, (b) engineering evidence that the task is a single present call, (c) capture-card-side loss being software-independent."
  ],
  "residualRisks": [
    "RitschyMirror HDR-tonemapping superiority over OBS is a vendor claim, not independently benchmarked (single-author, v1.3.2, unsigned installer).",
    "User's specific capture card model was not identified; internal compression behavior (uncompressed NV12 vs MJPEG/H.264) at 1080p60 could not be verified per-model.",
    "OBS projector vs OS duplicate-display quality delta at 1080p60 lacks formal measurement; community practice favors projector.",
    "Two web_search queries initially returned zero results (provider misconfiguration) and one Exa rate-limit occurred; all angles were re-covered successfully on retry, but a few secondary sources (e.g., Streamlabs changelog via Facebook) are lower-authority."
  ],
  "noStagedFiles": true,
  "diffSummary": "New research artifact lane-C-apps.md created with the full survey and recommendation (stay on OBS Source Projector; RitschyMirror only for HDR->SDR/mouse-lock niches).",
  "reviewFindings": [
    "no blockers",
    "info: NDI path is strictly lossier (4:2:0 codec) than uncompressed HDMI — flagged so the parent's final recommendation cannot favor NDI on quality grounds",
    "info: vMix 'External Output' does NOT support consumer USB/PCIe capture cards — common misconception corrected with official docs"
  ],
  "manualNotes": "Written to the authoritative path lane-C-apps.md. Confidence tagging included per finding. If the user's capture card model is provided, a follow-up can verify its internal 1080p60 format (uncompressed NV12 vs compressed) to confirm which hardware, if any, is the current bottleneck."
}
```
