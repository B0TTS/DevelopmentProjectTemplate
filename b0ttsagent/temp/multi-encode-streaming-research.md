# Research: Simultaneous Multi-Encode Streaming Pipeline (Dedicated Stream Laptop)

> **TL;DR** — Let the streaming app (vanilla OBS **or** StreamLabs, never both) own the Vixlw capture card and output **H.264 1080p60 CBR 6000 Kbps via NVENC H.264 (new)** to the Prism relay; record locally with **QSV AV1 (ICQ ~20-22, Target Usage: Quality)** on the Intel media engine; feed TikTok Live Studio through **OBS Virtual Camera** (TikTok has no NDI and cannot share the UVC card) and let TikTok's internal encoder auto-select (expect hardware NVENC/QSV). This splits the three encodes across two independent hardware engines + one auto engine. Verdict: **CONDITIONAL YES** — the three engines are all free because this laptop renders no games; the caveats are Wi-Fi variance, chassis thermals, and updating both apps so the modern encoder lists (incl. NVENC AV1) are exposed.

---

## 1. Core architecture — how to feed the same capture-card video to BOTH apps

**Explicit statement first:** because you alternate vanilla OBS Studio and StreamLabs Desktop (never simultaneously), capture-card contention between *those two* is moot. The only true simultaneous contention is **streaming-app vs TikTok Live Studio**, and that is solved 100% by making the streaming app the single owner of the card and handing TikTok a virtual camera stream. The Windows UVC/DirectShow model is exclusive-open for generic devices, so only one process may open the Vixlw card at a time — verified: DirectShow webcams are exclusive-use resources and apps throw "camera is already in use" on second open ([StackOverflow, DirectShow exclusive capture](https://stackoverflow.com/questions/28605444/two-instances-from-one-webcam)); multi-app sharing is a *special vendor feature* that only certain Elgato devices implement, not a generic UVC capability ([Elgato KB — Multi App Support](https://help.elgato.com/hc/en-us/articles/360042392672-Elgato-Capture-Devices-and-Multi-App-Support)).

### Ranked methods (definitive order)

**1. OBS Virtual Camera → TikTok Live Studio — RECOMMENDED (winner).**
- The streaming app opens the card once (OBS owns it), runs its normal live+record pipeline, and additionally exposes the composed 1080p60 scene as a standard webcam device via *Start Virtual Camera* ([OBS KB — Virtual Camera Guide](https://obsproject.com/kb/virtual-camera-guide)).
- TikTok Live Studio consumes it as an ordinary **Camera** source: official current help shows `Add source > Camera`, with per-source resolution/FPS/video-format settings (YUY2/NV12/I420) ([TikTok official — Add a camera source](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-camera-source-to-let-viewers-know-you)). Third-party guides confirm "OBS Virtual Camera" appears in TikTok's device dropdown and that the workflow is current (Hollyland guide dated **Apr 2026**: requires OBS v26+ built-in virtual camera, TikTok desktop app, Windows 10+; troubleshooting table covers "not listed / black screen / laggy" — resolution mismatch is the leading cause of blurry output) ([Hollyland — OBS Virtual Camera to TikTok Live Studio](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)). The same workflow is documented by TikTok-ecosystem tooling vendors ([TIKTORY — OBS Virtual Camera with TikTok LIVE Studio](https://help.tiktory.com/en/pages/how-to-setup-obs-virtual-camera-with-tiktok-live-studio)).
- **On Windows, one virtual camera can feed multiple consumers simultaneously** — DirectShow shared-mode opens are allowed; multiple programs can use the OBS virtual camera at once without conflict ([obs-versions.com — OBS Virtual Camera multi-app](https://obs-versions.com/blog/obs-virtual-camera-how-to-use), [Microsoft Learn Q&A — same webcam in multiple programs](https://learn.microsoft.com/en-us/answers/questions/4301512/how-to-use-the-same-webcam-on-multiple-programs)). You only need one consumer (TikTok), so this is safe.
- Cost: near-zero. The virtual camera shares the already-composited frame buffer (no re-encode, no window management). It carries **video only** — audio comes via your existing NDI/audio guide ([Hollyland FAQ](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).

**2. Fullscreen Projector (Source) → TikTok Display/Window capture — current method, WORKING but inferior.**
- TikTok Live Studio does support Game/Display/Window capture sources ([TikTok official — Add a capture source](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-capture-source-to-share-your-computer-screen?lang=en)), so the projector method functions. Why it is worse than Virtual Camera:
  - TikTok must capture a *screen*: DWM window composition → screen-capture copy → resolution/FPS conversion. The virtual camera delivers clean frames at the exact canvas resolution; the projector path can letterbox, pick up the cursor, capture occluders, and is hostage to monitor sleep/arrangement. Resolution mismatch is the #1 cause of blurry TikTok output ([Hollyland troubleshooting table](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).
  - Extra GPU work: one extra full-screen window render (OBS projector) + a full-desktop capture pass in TikTok. Both are small on this hardware, but they are *pure overhead* that Virtual Camera eliminates. No published benchmark quantifies projector-vs-vcam load; the OBS KB positions the virtual camera as the designed mechanism for "applications that cannot capture the screen directly" ([OBS KB](https://obsproject.com/kb/virtual-camera-guide)) — i.e., the projector→screen-capture chain is a workaround, not a pipeline.
  - Keep it only as a fallback if a TikTok build ever fails to list the virtual camera.

**3. NDI as the ingest (replaces the card) — viable alternative ingest, but it does NOT solve TikTok.**
- NDI is one-to-many, so multiple OBS-class apps can subscribe. But **TikTok Live Studio has no NDI support** — you still need an OBS-class app converting NDI → OBS Virtual Camera → TikTok. So NDI adds a hop and Wi-Fi bandwidth without removing the virtual-camera requirement.
- **DistroAV in StreamLabs Desktop: not supported.** DistroAV (formerly OBS-NDI) is an OBS Studio plugin; v6.1+ hard-requires OBS 31 + NDI 6 and refuses to load otherwise ([DistroAV release 6.1.0](https://github.com/DistroAV/DistroAV/releases/tag/6.1.0)). StreamLabs Desktop is its own fork: it can **receive** external NDI sources natively, but does **not** ship DistroAV-style NDI *output* — Streamlabs' own docs describe NDI output as an OBS 31 + DistroAV task and NDI reception as a Streamlabs source capability ([Streamlabs — Create NDI Stream Output with OBS Studio](https://streamlabs.com/content-hub/post/create-ndi-stream-output-with-obs-studio), [Streamlabs — NDI Receiving Setup](https://streamlabs.com/content-hub/post/ndi-receiving-setup-in-streamlabs-desktop)). That matches your "historically spotty" experience — treat NDI in SLOBS as receive-only.
- **OBS Virtual Camera + NDI coexist fine** in vanilla OBS: virtual camera and DistroAV are independent outputs of the same compositor; the known conflict is only if NDI output is left running while another app grabs the vcam (black-screen symptom listed in the Hollyland troubleshooting table) ([Hollyland](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).
- Net: keep your documented NDI Screen Capture HX path (see `b0ttsagent/NavGuides/NdiStreamingNavGuide.md`) as the *alternative ingest* when you want to drop the card, not as the TikTok bridge.

**4. SplitCam / e2eSoft VCam / vMix VirtualCam — not recommended.**
- These third-party virtual-camera layers solve the same "one device, many apps" problem, but add driver installs, latency, watermarks/paid tiers, and an extra copy hop. They only make sense if you refused to run OBS. Since OBS's built-in virtual camera is free, maintained, and already in your pipeline, they add nothing ([context: the general webcam-sharing pattern these tools implement is documented on StackOverflow](https://stackoverflow.com/questions/13262836/access-webcam-from-multiple-applications-simultaneously)).

**5. DirectShow multi-open / capture-card splitter filters for Vixlw-class UVC cards — NOT viable.**
- Cheap UVC cards do not expose multi-open; "Multi App Support" is a proprietary feature of specific Elgato hardware ([Elgato KB](https://help.elgato.com/hc/en-us/articles/360042392672-Elgato-Capture-Devices-and-Multi-App-Support)). DirectShow cameras are exclusive resources; splitting requires a virtual-camera layer ([StackOverflow](https://stackoverflow.com/questions/28605444/two-instances-from-one-webcam)). Magewell's USB Capture line even documents per-client limitations (one resolution config) ([Magewell KB](https://www.magewell.com/kb/detail/0002050001/usb-capture)). Do not pursue this path.

---

## 2. TikTok Live Studio specifics (current, cited)

**Inputs — all confirmed on current official docs:**
- **Camera/webcam sources: YES** — `Add source > Camera`, with per-source Resolution, FPS (60 recommended, 30 for effects), and video format (YUY2 / NV12 / I420) ([TikTok — Add a camera source](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-camera-source-to-let-viewers-know-you)). OBS Virtual Camera enumerates as one of these cameras ([Hollyland](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).
- **Game / Display / Window capture: YES** — all three source types exist ([TikTok — Add a capture source](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-capture-source-to-share-your-computer-screen?lang=en)).
- **Multi-source scenes: YES** — scene-based layout like OBS, up to 20 sources per scene, dual layout (portrait + landscape) ([TikTok — What's a source?](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Whats-a-source?lang=en), [TikTok — Learn the basics of LIVE](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Learn-the-basics-of-LIVE?lang=en)).

**Encoder — user does NOT reliably control it:**
- The encoder is a parameter inside "Video quality"; official guidance: *"LIVE Studio can automatically select an appropriate encoder for you"*, hardware encoders recommended over software ([TikTok — Configure LIVE settings](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US), [TikTok — Adjust LIVE quality](https://www.tiktok.com/live/studio/help/article/Enhance-visuals/Adjust-LIVE-quality-for-smooth-and-clear-video?lang=en)).
- The older official operation manual shows a selectable "encoding scheme" list (V265 soft codec / CPU H.264 / NVIDIA H.264 / Intel 265) with the constraint *"You can only select a different encoding scheme when you stop your LIVE"* ([TikTok — How to go LIVE in TikTok](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)). Practical takeaway: on this hybrid laptop expect **hardware auto-select (NVENC or QSV)**; you cannot force "pass-through" — there is no such mode; TikTok always re-encodes what it captures.
- Related settings to check: **Encoder compatibility mode** (fixes green-screen artifacts, keep default off), **Stream latency**, and the built-in **Test speed** which proposes a quality tier from a real TikTok-ingest speed test ([TikTok — Configure LIVE settings](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US)).

**Resolution/FPS caps:**
- No follower-tier resolution lock is documented in current official help — the quality presets offered are **1080P60 / 720P60 / 1080P / 720P / 480P**, with per-parameter customization (resolution, FPS 20–60, bitrate, audio bitrate) ([TikTok — Adjust LIVE quality](https://www.tiktok.com/live/studio/help/article/Enhance-visuals/Adjust-LIVE-quality-for-smooth-and-clear-video?lang=en)). The legacy table listed 1080P = 8000 Kbps video / 256 Kbps audio at 60 FPS; 720P+ = 4000 Kbps; 720P = 2000 Kbps ([TikTok — How to go LIVE](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)). In practice newer builds auto-suggest ~6400 Kbps for 1080p60 on a ~46 Mbps upload ([ozject — TikTok LIVE Studio setup, field report](https://ozject.media/ozhole/tiktok-live-studio-mac-autistic-friendly-setup)).
- The **account gate is access itself, not resolution**: US gaming creators need 1,000 followers; non-gaming creators need 10,000 followers to use LIVE Studio ([TikTok official — LIVE Studio access](https://www.tiktok.com/live/creators/en-US/article/tiktok-live-studio-access_en-US)). How to tell your tier: open the LIVE quality panel — whichever preset set is enabled is your tier; if 1080P60 isn't selectable, your account/device hasn't been granted it (access requirements above), and/or your machine misses the recommended specs (1080p60 needs "recommended" tier hardware per [TikTok — LIVE Studio Troubleshooting](https://www.tiktok.com/live/creators/en-US/article/live-studio-troubleshooting-guides_en-US?name=undefined)).

**Recommended settings at each cap (consensus of official tables + current guides):**
- 1080p60: video 4000–6000 Kbps (auto-test will suggest ~6000–6400), audio 64–256 Kbps, ≥7.5 Mbps upload ([TikTok — How to go LIVE](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)).
- 720p60: 2000–2500 Kbps, ≥3 Mbps upload.
- 1080p30: 2000–4000 Kbps, ≥5 Mbps.
- 720p30: 1200–2000 Kbps, ≥2.5 Mbps.
- Keyframe: TikTok does not expose a keyframe interval in the LIVE-quality UI; it manages the encoder itself. For OBS-originated content there is nothing to set on the TikTok side. Third-party guidance for TikTok-style setups: 2s keyframes, hardware encoder, 4000–6000 Kbps ([theapp.vip — TikTok LIVE setup](https://www.theapp.vip/blog/tiktok-live-setup)).

---

## 3. Encoder selection matrix (definitive picks)

**Engine inventory (all free — this laptop runs no games):**
- **NVENC**: RTX 4050 Laptop = 8th-gen NVENC on AD107; H.264/HEVC/AV1 hardware encode ([NVIDIA — OBS 29.1 AV1 on RTX 40](https://blogs.nvidia.com/blog/av1-obs29-youtube/), [Bandicam NVENC support matrix incl. RTX 4050 Laptop AV1](https://www.bandicam.com/how-to-use-nvidia-nvenc-encoder/)). One physical engine; consumer session limit is **8 concurrent** since driver 551.23 (Jan 2024) ([NVIDIA NVENC Application Note — non-qualified GPUs capped at 8 sessions](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html), [VideoCardz — 8 concurrent sessions](https://videocardz.com/newz/nvdia-geforce-gpus-now-support-up-to-8-concurrent-nvenc-encoding-sessions), [Stream Guides — driver 551.23 analysis](https://streamguides.gg/2024/01/nvenc-update-all-nvidia-geforce-cards-quietly-updated-to-8-encoding-sessions/)). Sessions time-share the one physical engine → latency/quality cost grows with session count, negligible at 2 sessions of 1080p60.
- **QSV**: Core Ultra 9 185H (Meteor Lake) — Intel media engine with **H.264, HEVC, and AV1 hardware encode** ([VideoCardz — Intel confirms Meteor Lake AV1 encode](https://videocardz.com/newz/intel-confirms-meteor-lake-has-av1-video-encoding-and-decoding-support), [Intel Core Ultra datasheet — hardware accelerated video encode](https://edc.intel.com/content/www/cn/zh/design/products/platforms/details/meteor-lake-u-p/core-ultra-processor-datasheet-volume-1-of-2/003/hardware-accelerated-video-encode/)).
- **x264**: 16 cores/22 threads available as a third, slower-but-highest-quality H.264 option — unnecessary here.

### A) OBS → Prism LIVE feed (must be H.264; Priority HIGH) — **DEFINITIVE: NVIDIA NVENC H.264 (the "new" implementation)** with QSV H.264 as the documented no-contention fallback.
Justification:
- At Twitch-tier 6,000 Kbps/1080p60, Ada 8th-gen NVENC H.264 with lookahead + psycho-visual tuning is the strongest stable hardware H.264 option OBS exposes — the official NVIDIA/OBS NVENC guide's exact live-stack: CBR, keyframe 2, P6, High profile, lookahead ON, psycho-visual ON, max B-frames 4, multipass two-pass quarter-res, tuning High Quality ([OBS Forum — NVIDIA NvEnc Guide](https://obsproject.com/forum/resources/nvidia-nvenc-guide.740/)). Independent encoder shootouts consistently rank NVENC ≥ QSV at equal H.264 bitrates (QSV is close but softer in high motion) ([Kim2091/codec-comparisons — NVENC vs QSV at matched bitrate](https://github.com/Kim2091/codec-comparisons), [Stream Guides — Ultimate Encoder Quality Analysis](https://streamguides.gg/2020/04/ultimate-encoder-quality-analysis-2020-nvenc-vs-amf-vs-quicksync-vs-x264/)).
- Contention math: even in the worst case (TikTok also picks NVENC) you run **2 of 8 allowed sessions** — supported, and the per-session quality/latency penalty at 1080p60 is minor. If you ever see OBS dropped frames *and* TikTok is confirmed on NVENC, the fallback is: Prism live → **QuickSync H.264** (engine #2), which zeroes contention at a small high-motion quality cost.
- Exact values: **CBR 6000 Kbps · keyframe 2s · preset P6 (P5 if encoder overloads) · Tuning: High Quality · Multipass: Two Passes (Quarter Resolution) · Profile: High · Lookahead ON · Psycho Visual Tuning ON · Max B-frames 4 (2 if lookahead off) · GPU 0 · Enforce Streaming Service Encoder Settings ON**. Note: 1080p60@6000 is the Twitch ceiling; the Prism relay re-serves this to Twitch/YouTube/Kick as-is (Twitch ingest is H.264-only — your hard constraint) ([OBS Forum — NVENC guide bitrate/keyframe notes](https://obsproject.com/forum/resources/nvidia-nvenc-guide.740/)).

### B) Recording to disk (Priority LOWEST) — **DEFINITIVE: QuickSync AV1 (QSV AV1), LA-ICQ, ICQ level 20–22, Target Usage: Quality.**
- Rationale: AV1 is ~40% more efficient than H.264 at equal quality per NVIDIA's own 8th-gen figures ([NVIDIA blog](https://blogs.nvidia.com/blog/av1-obs29-youtube/)); QSV AV1 rides the **separate Intel engine**, so recording steals nothing from the two live feeds. NVENC HEVC (CQP 19-21, P6) is the alternative if you'd rather keep QSV free, but QSV AV1 is the better fidelity-per-byte pick and keeps NVENC's single engine exclusively for the lives.
- Exact values: **Encoder: QuickSync AV1 · Rate control: LA-ICQ (or CQP) · ICQ/CQ level 20–22 (20 = higher fidelity) · Target Usage: Quality · Profile: main · Keyframe interval 0 (or 2) · Container: MKV (safe) or MP4 · Color: Rec.709, Partial (limited) range default; switch to Full only if the capture source is full-range and blacks look washed in editing** ([salivity — Intel Arc/QSV AV1 in OBS settings guide](https://salivity.github.io/obs-studio/article/how-to-use-intel-arc-av1-encoder-in-obs-studio)).
- Audio: use OBS multitrack recording (up to 6 tracks) so mic/game/NDI stems stay separate ([OBS KB — Advanced Recording Guide & Multi-Track Audio](https://obsproject.com/kb/advanced-recording-guide-and-multi-track-audio)) — one line, since your audio already runs through the NDI guide.

### C) TikTok Live Studio — **report-only: expect internal auto hardware encode (NVENC or QSV), 1080p60 ≈ 6000–6400 Kbps.** Nothing to configure beyond the quality preset; verify in the LIVE-quality panel that the encoder line shows a hardware encoder, and leave "Encoder compatibility mode" off unless green-screen artifacts appear ([TikTok — Configure LIVE settings](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US), [TikTok — Adjust LIVE quality](https://www.tiktok.com/live/studio/help/article/Enhance-visuals/Adjust-LIVE-quality-for-smooth-and-clear-video?lang=en)).

### Encoder assignment summary
> **Prism live = NVENC H.264 (new) · Recording = QSV AV1 · TikTok = TikTok-internal (likely NVENC).**
> Anti-contention logic: NVENC carries the two *live* streams at most (2/8 sessions, fine); QSV carries only the record; x264 stays idle. If TikTok is observed on NVENC *and* OBS shows encoder overload, flip Prism live to QSV H.264 (then NVENC=1 session, QSV=2). Never add a third NVENC session (e.g., don't switch recording to NVENC HEVC while both lives use NVENC).

### NVENC AV1 availability — VERIFIED
- Your encoder list has no "NVENC AV1": that's a **version artifact, not a hardware limit**. RTX 4050 Laptop (AD107, 8th-gen NVENC) supports AV1 encode ([NVIDIA blog](https://blogs.nvidia.com/blog/av1-obs29-youtube/), [Bandicam matrix](https://www.bandicam.com/how-to-use-nvidia-nvenc-encoder/)); OBS exposes "NVIDIA NVENC AV1" since OBS 29.1 ([NVIDIA blog](https://blogs.nvidia.com/blog/av1-obs29-youtube/), [AVerMedia FAQ](https://www.avermedia.com/support/faq/how-to-set-up-the-av1-encoder-in-obs)), and current OBS 31 keeps it plus new advanced NVENC options ([OBS 31.0.0 release notes](https://github.com/obsproject/obs-studio/releases/tag/31.0.0), [OBS KB — Advanced NVENC Options](https://obsproject.com/kb/advanced-nvenc-options)). **StreamLabs Desktop now runs the OBS 31.1.2 core** (per current patch notes), so current SLOBS exposes the same encoder families (nvenc/qsv, incl. AV1) ([Streamlabs patch notes](https://streamlabs.com/content-hub/post/streamlabs-desktop-patch-notes), [Streamlabs PR #5931 — backend encoder metadata incl. nvenc/qsv families and AV1](https://github.com/streamlabs/desktop/pull/5931)). → Update vanilla OBS to 31.x and StreamLabs to latest; the AV1 entries will appear in both.

---

## 4. Feasibility verdict

**CONDITIONAL YES.** This exact hardware runs the full 4-way load — card ingest + OBS live-to-Prism + OBS record + TikTok Live Studio — stably at 1080p60 over 30 Mbps Wi-Fi, *because the laptop renders no games, so NVENC, QSV, and the CPU are entirely available for encoding*. That is the key enabler, and it holds:
- Encode load is trivially inside budget: 2× NVENC 1080p60 sessions (limit 8), 1× QSV AV1 1080p60, ~5-10% CPU at most. x264 never engaged. 32 GB shared LPDDR5x-7467 is ample for 1080p60 frame queues ([NVENC app note](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html), [VideoCardz](https://videocardz.com/newz/nvdia-geforce-gpus-now-support-up-to-8-concurrent-nvenc-encoding-sessions)).
- Network: Prism feed ~6 Mbps + TikTok ~4–6 Mbps ≈ **10–12 Mbps of ~30 Mbps upload** — ~60% headroom for Wi-Fi variance; TikTok's built-in test-speed will confirm ([toktutorials 2026 — targets for 1080p: 10 Mbps+, TikTok test-speed](https://www.toktutorials.com/post/how-to-set-up-tiktok-live-studio-in-2026-complete-beginner-guide-streaming-best-practices), [TikTok — How to go LIVE table](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)).

Caveats that make it CONDITIONAL:
1. **Thermals**: Ultra 9 185H runs 85 W short-burst / **65 W sustained (PL1)** ([Notebookcheck — Ultra 9 185H specs](https://www.notebookcheck.net/Intel-Core-Ultra-9-185H-Processor-Benchmarks-and-Specs.783353.0.html)); the 16IMH chassis cooling is shared with the iGPU-only design, so sustained dual-hardware-encoder load means "louder noise and higher temperatures on average" per Notebookcheck's RTX-4050 sibling review ([Notebookcheck — IdeaPad Pro 5 16IMH G9](https://www.notebookcheck.net/Lenovo-IdeaPad-Pro-5-16IMH-G9-review-90-W-GeForce-RTX-4050-almost-as-good-as-the-RTX-4060.880099.0.html)). Mitigations: Best Performance + plugged in (already set), vents clear, laptop stand/cooling pad, monitor temps with HWiNFO; the **first casualty to cut is recording** (matches your priority order).
2. **Capture-card sharing**: only the streaming app may open the Vixlw card; TikTok must use the virtual camera. If TikTok also grabs the card, you get "device in use" ([StackOverflow](https://stackoverflow.com/questions/28605444/two-instances-from-one-webcam), [Elgato KB](https://help.elgato.com/hc/en-us/articles/360042392672-Elgato-Capture-Devices-and-Multi-App-Support)).
3. **Dual-GPU routing**: UVC frames land in system memory; OBS composites on one adapter and OBS handles cross-GPU copies to the NVENC/QSV encoder — at 1080p60 this is a non-event *because no game is competing for the GPU*. Keep Windows **Hardware-accelerated GPU scheduling** ON so NVENC sessions and DWM coexist smoothly ([OBS Forum — NVENC guide, GPU scheduling](https://obsproject.com/forum/resources/nvidia-nvenc-guide.740/)).
4. **Wi-Fi variance**: two concurrent upstreams on Wi-Fi near a wired extender; if TikTok's test-speed drops its suggested tier, accept 720P60/4 Mbps rather than fight it; keep Prism at fixed CBR 6000.
5. **App versions**: both apps must be current to expose NVENC AV1/QSV AV1 (OBS ≥29.1 for AV1; SLOBS on OBS 31.1.2 core) ([NVIDIA blog](https://blogs.nvidia.com/blog/av1-obs29-youtube/), [Streamlabs patch notes](https://streamlabs.com/content-hub/post/streamlabs-desktop-patch-notes)).

---

## 5. Concrete settings tables (paste-ready)

### Vanilla OBS Studio (Settings → Output → **Advanced** mode)

| Streaming tab | Value |
|---|---|
| Encoder | NVIDIA NVENC H.264 (the "new" one; never the "(old)" variant) |
| Rate control | CBR |
| Bitrate | 6000 Kbps |
| Keyframe interval | 2 |
| Preset | P6: Slower (Better Quality) — drop to P5 only if encoder overload |
| Tuning | High Quality |
| Multipass mode | Two Passes (Quarter Resolution) |
| Profile | High |
| Look-ahead | ON |
| Psycho Visual Tuning | ON |
| Max B-frames | 4 |
| GPU | 0 |
| Enforce Streaming Service Encoder Settings | ON |

| Recording tab | Value |
|---|---|
| Encoder | QuickSync AV1 (QSV AV1) |
| Rate control | LA-ICQ (or CQP) |
| ICQ quality / CQ level | 20–22 (lower = better; 20 for 1080p60 fidelity) |
| Target usage | Quality |
| Profile | main |
| Keyframe interval | 0 (or 2) |
| Container | MKV (safe for crash recovery); remux to MP4 after |
| Audio | multitrack (up to 6 tracks) per your NDI audio guide |

| Advanced/Video tab | Value |
|---|---|
| Base canvas | 1920×1080 (matches card) |
| Output scaled | 1920×1080, Lanczos |
| Color space / range | Rec. 709 / Partial (limited) — flip to Full only if capture source is full-range |

**Simple-mode equivalent** (if you prefer): Output → Simple → Streaming: "Hardware (NVENC, H.264)", 6000 Kbps, 2s keyframe (OBS enforces); Recording: quality preset "High Quality" and **encoder "Hardware (QSV, AV1)" — only available when Recording Quality ≠ "Same as stream"** ([OBS KB — Recording Encoder Presets Guide](https://obsproject.com/kb/recording-encoder-presets-guide), [OBS KB — OBS Studio Overview](https://obsproject.com/kb/obs-studio-overview)). Advanced mode is recommended so stream vs record encoders are fully independent ([OBS KB — Advanced Recording Guide](https://obsproject.com/kb/advanced-recording-guide-and-multi-track-audio)).

### StreamLabs Desktop (SLOBS)
- **VERIFIED: current StreamLabs lets you use a different encoder for Recording vs Streaming — in Advanced mode only.** Documented path: Settings → Output → change mode from **Simple to Advanced** → **Streaming tab** (stream encoder) and **Recording tab** (own encoder, path, file type, resolution, up to 6 audio tracks) ([Streamlabs — How to use multi-track recording (Advanced mode)](https://support.streamlabs.com/hc/en-us/articles/4413174859291-How-to-use-multi-track-recording-in-Streamlabs-Desktop)). The codebase separates `streaming`, `recording`, and `replayBuffer` encoder settings, and encoder discovery is backend-driven (nvenc/qsv families incl. AV1) ([streamlabs/desktop output-settings.ts](https://github.com/streamlabs/desktop/blob/829b4df2/app/services/settings/output/output-settings.ts), [PR #5931](https://github.com/streamlabs/desktop/pull/5931)).
- **Caveat (confirmed): in Simple mode, recording can only use "Same as stream" (or the stream encoder) — a separate recording encoder is NOT selectable in Simple mode** ([StreamlabsSupport/Streamlabs-Desktop — recording+streaming performance notes](https://github.com/StreamlabsSupport/Streamlabs-Desktop)). Historical limitation — use Advanced mode, or use vanilla OBS for the record+live combo.
- SLOBS exact settings = same values as the vanilla tables above (encoder names: "NVIDIA NVENC H.264", "QuickSync AV1 (QSV AV1)"), given the OBS 31.1.2 core ([Streamlabs patch notes](https://streamlabs.com/content-hub/post/streamlabs-desktop-patch-notes)).
- SLOBS also has Replay Buffer with its own encoder settings if you want a third, separate quick-capture encoder (keep it off or on QSV AV1 to avoid a 3rd NVENC session).

### TikTok Live Studio
- Source: Add source → **Camera** → select **OBS Virtual Camera**; set source Resolution 1920×1080, FPS 60, format default (NV12). Match TikTok scene dimensions to the OBS canvas (mismatch = blur) ([TikTok — camera source](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-camera-source-to-let-viewers-know-you), [Hollyland](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).
- LIVE quality: preset **1080P60** (if granted) → video bitrate auto (expect ~6000–6400); audio via your NDI/audio guide; latency default; Encoder: **leave auto**; verify in the panel it shows a hardware encoder; encoder changes only possible while not live ([TikTok — Configure LIVE settings](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US), [TikTok — How to go LIVE](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)).
- If upload variance bites: drop to 720P60 (~2500 Kbps) — TikTok mobile viewers won't see the difference ([TikTok — How to go LIVE](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en)).

### Per-game hints (all three arrive via the same card, so this is bitrate/motion tuning only)
- **Fortnite** (high motion): at 1080p60/6000 Kbps expect occasional blockiness; options: 720p60/6000 (the classic Twitch compromise — [OBS NVENC guide](https://obsproject.com/forum/resources/nvidia-nvenc-guide.740/) cites Fortnite 720p60@6000 explicitly) or cap game fps/quality to reduce motion complexity.
- **Minecraft** (low motion, blocky textures): 6000 Kbps is overkill — you can run 4500–5000 Kbps and keep 1080p60 clean; keep keyframes 2s.
- **Roblox** (mixed): 5000–6000 Kbps 1080p60; identical keyframe 2s.
- All: keep OBS "dynamic bitrate" OFF for stable CBR; recording quality is unaffected since QSV AV1 ICQ adapts automatically.

---

## 6. Risks & gotchas (checklist)

1. **Capture card exclusive-open** — one app owns the Vixlw card (the streaming app). TikTok must use OBS Virtual Camera, never the card ([Elgato KB](https://help.elgato.com/hc/en-us/articles/360042392672-Elgato-Capture-Devices-and-Multi-App-Support), [StackOverflow](https://stackoverflow.com/questions/28605444/two-instances-from-one-webcam)).
2. **SLOBS single-encoder caveat** — Simple mode cannot decouple record from stream encoder; Advanced mode can. Don't fight it — use Advanced ([Streamlabs multi-track article](https://support.streamlabs.com/hc/en-us/articles/4413174859291-How-to-use-multi-track-recording-in-Streamlabs-Desktop), [GitHub notes](https://github.com/StreamlabsSupport/Streamlabs-Desktop)).
3. **TikTok chooses its own encoder** — auto-select, hardware preferred; can't force NVENC vs QSV, no pass-through; changes only when not live ([TikTok docs](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US)).
4. **Prism VPS RTMP destination regenerates on restart** — re-check the OBS/SLOBS stream destination after any relay restart (your known operational gotcha; no research needed).
5. **Wi-Fi variance** — 10–12 Mbps of 30 Mbps used; 5 GHz, near extender; let TikTok's test-speed calibrate; be ready to drop TikTok to 720P60.
6. **Thermal** — 65 W sustained PL1 in a slim chassis; fans will be audible; monitor temps; recording is the first thing to cut ([Notebookcheck](https://www.notebookcheck.net/Lenovo-IdeaPad-Pro-5-16IMH-G9-review-90-W-GeForce-RTX-4050-almost-as-good-as-the-RTX-4060.880099.0.html)).
7. **NVENC serialization** — one physical engine; 2 concurrent 1080p60 sessions are fine (8 allowed); avoid a 3rd NVENC session (don't record with NVENC while both lives run NVENC) ([NVENC app note](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html)).
8. **Missing NVENC AV1 in your list = stale build** — update OBS to 31.x and StreamLabs to latest; AV1 entries will appear ([NVIDIA blog](https://blogs.nvidia.com/blog/av1-obs29-youtube/), [Streamlabs patch notes](https://streamlabs.com/content-hub/post/streamlabs-desktop-patch-notes)).
9. **NDI ≠ TikTok bridge** — TikTok has no NDI input; even on the NDI ingest path you still need OBS → Virtual Camera for TikTok; DistroAV won't run in SLOBS (receive-only) ([Streamlabs NDI articles](https://streamlabs.com/content-hub/post/ndi-receiving-setup-in-streamlabs-desktop), [DistroAV 6.1.0](https://github.com/DistroAV/DistroAV/releases/tag/6.1.0)).
10. **Resolution mismatch** between OBS canvas and TikTok scene = blurry/letterboxed output — match 1080p60 on both ([Hollyland](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio)).

---

## Sources

**Kept (primary / current):**
- TikTok official help: Add a camera source — establishes Camera/webcam sources, per-source res/FPS/format ([url](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-camera-source-to-let-viewers-know-you))
- TikTok official: Add a capture source — establishes Game/Display/Window capture ([url](https://www.tiktok.com/live/studio/help/article/Get-started-with-your-first-LIVE/Add-a-capture-source-to-share-your-computer-screen?lang=en))
- TikTok official: Configure LIVE settings — encoder auto-select, hardware recommended, compatibility mode, test-speed ([url](https://www.tiktok.com/live/creators/en-US/article/configure-live-settings-in-live-studio-en-US))
- TikTok official: Adjust LIVE quality — current quality presets 1080P60…480P, parameter ranges ([url](https://www.tiktok.com/live/studio/help/article/Enhance-visuals/Adjust-LIVE-quality-for-smooth-and-clear-video?lang=en))
- TikTok official: How to go LIVE in TikTok — legacy bitrate table (1080p=8000, 720p+=4000…), encoder scheme list, ≥7.5 Mbps for 1080p60 ([url](https://www.tiktok.com/live/studio/help/article/1023/how-to-go-live-in-tiktok_en-US?lang=en))
- TikTok official: LIVE Studio access — 1K gaming / 10K non-gaming followers ([url](https://www.tiktok.com/live/creators/en-US/article/tiktok-live-studio-access_en-US))
- OBS KB: Virtual Camera Guide — Start/Stop, output selection, purpose ([url](https://obsproject.com/kb/virtual-camera-guide))
- OBS Forum: NVIDIA NvEnc Guide — full NVENC stream/record value set (CBR 6000, P6, High, lookahead, psycho, B-frames 4, multipass) ([url](https://obsproject.com/forum/resources/nvidia-nvenc-guide.740/))
- OBS KB: Advanced Recording Guide / Recording Presets — separate record encoder, multitrack ([url](https://obsproject.com/kb/advanced-recording-guide-and-multi-track-audio), [url](https://obsproject.com/kb/recording-encoder-presets-guide))
- OBS 31.0.0 release notes + OBS KB Advanced NVENC Options — current OBS 31 feature set ([url](https://github.com/obsproject/obs-studio/releases/tag/31.0.0), [url](https://obsproject.com/kb/advanced-nvenc-options))
- NVIDIA blog: OBS 29.1 AV1 on RTX 40 — 8th-gen NVENC, AV1 on all RTX 40 (incl. laptop) ([url](https://blogs.nvidia.com/blog/av1-obs29-youtube/))
- NVIDIA NVENC Application Note + VideoCardz + Stream Guides — 8 concurrent NVENC sessions since driver 551.23 ([url](https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html), [url](https://videocardz.com/newz/nvdia-geforce-gpus-now-support-up-to-8-concurrent-nvenc-encoding-sessions), [url](https://streamguides.gg/2024/01/nvenc-update-all-nvidia-geforce-cards-quietly-updated-to-8-encoding-sessions/))
- Streamlabs: patch notes (OBS 31.1.2 core), multi-track recording (Advanced mode recording tab = own encoder), GitHub output-settings.ts + PR #5931 (separate streaming/recording/replayBuffer encoders, backend encoder metadata) ([url](https://streamlabs.com/content-hub/post/streamlabs-desktop-patch-notes), [url](https://support.streamlabs.com/hc/en-us/articles/4413174859291-How-to-use-multi-track-recording-in-Streamlabs-Desktop), [url](https://github.com/streamlabs/desktop/blob/829b4df2/app/services/settings/output/output-settings.ts), [url](https://github.com/streamlabs/desktop/pull/5931))
- StreamlabsSupport/Streamlabs-Desktop (GitHub) — "same as stream" only in simple output mode ([url](https://github.com/StreamlabsSupport/Streamlabs-Desktop))
- Streamlabs NDI articles + DistroAV 6.1.0 release — SLOBS NDI receive-only; DistroAV needs OBS 31 ([url](https://streamlabs.com/content-hub/post/ndi-receiving-setup-in-streamlabs-desktop), [url](https://streamlabs.com/content-hub/post/create-ndi-stream-output-with-obs-studio), [url](https://github.com/DistroAV/DistroAV/releases/tag/6.1.0))
- Elgato KB Multi App Support — multi-open is a special vendor feature ([url](https://help.elgato.com/hc/en-us/articles/360042392672-Elgato-Capture-Devices-and-Multi-App-Support))
- StackOverflow (DirectShow exclusive) + obs-versions + Microsoft Learn — exclusive UVC; OBS vcam multi-consumer on Windows ([url](https://stackoverflow.com/questions/28605444/two-instances-from-one-webcam), [url](https://obs-versions.com/blog/obs-virtual-camera-how-to-use), [url](https://learn.microsoft.com/en-us/answers/questions/4301512/how-to-use-the-same-webcam-on-multiple-programs))
- VideoCardz + Intel datasheet — Meteor Lake AV1 encode via QSV ([url](https://videocardz.com/newz/intel-confirms-meteor-lake-has-av1-video-encoding-and-decoding-support), [url](https://edc.intel.com/content/www/cn/zh/design/products/platforms/details/meteor-lake-u-p/core-ultra-processor-datasheet-volume-1-of-2/003/hardware-accelerated-video-encode/))
- salivity — QSV AV1 OBS settings (LA-ICQ/CQP 20-23, Target Usage Quality) ([url](https://salivity.github.io/obs-studio/article/how-to-use-intel-arc-av1-encoder-in-obs-studio))
- Kim2091/codec-comparisons + Stream Guides 2020 — NVENC vs QSV H.264 quality evidence ([url](https://github.com/Kim2091/codec-comparisons), [url](https://streamguides.gg/2020/04/ultimate-encoder-quality-analysis-2020-nvenc-vs-amf-vs-quicksync-vs-x264/))
- Notebookcheck — IdeaPad Pro 5 16IMH9 specs; Ultra 9 185H 85W/65W power; 16IMH G9 cooling note ([url](https://www.notebookcheck.net/Lenovo-IdeaPad-Pro-5-16IMH9-Ultra-9-185H.995390.0.html), [url](https://www.notebookcheck.net/Intel-Core-Ultra-9-185H-Processor-Benchmarks-and-Specs.783353.0.html), [url](https://www.notebookcheck.net/Lenovo-IdeaPad-Pro-5-16IMH-G9-review-90-W-GeForce-RTX-4050-almost-as-good-as-the-RTX-4060.880099.0.html))
- Hollyland (Apr 2026) + TIKTORY — OBS Virtual Camera → TikTok Live Studio workflow, current-version confirmation ([url](https://store.hollyland.com/blogs/creator-hub/add-obs-virtual-camera-to-tiktok-live-studio), [url](https://help.tiktory.com/en/pages/how-to-setup-obs-virtual-camera-with-tiktok-live-studio))
- toktutorials 2026 — 1080p needs ~10 Mbps upload; use TikTok test-speed ([url](https://www.toktutorials.com/post/how-to-set-up-tiktok-live-studio-in-2026-complete-beginner-guide-streaming-best-practices))
- Bandicam NVENC matrix — RTX 4050 Laptop: NVENC H.264/HEVC/AV1 ([url](https://www.bandicam.com/how-to-use-nvidia-nvenc-encoder/))

**Dropped:**
- Shopify blog how-to-go-live — secondary aggregation of follower requirements, superseded by TikTok's own access article.
- eklipse/tiktokstats/vivo Q&A guides — generic re-skins of official docs, no added evidence.
- Medium "AV1 bitrate trap" — opinion piece, no hardware-specific data.
- AVerMedia FAQ — kept only for the OBS encoder-name confirmation; otherwise generic.

---

## Gaps

1. **TikTok's exact auto-encoder choice on this hybrid laptop is not documented** — official docs only say "auto-select, hardware preferred." Can't confirm NVENC vs QSV on your unit without opening TikTok's LIVE-quality panel; fallback plan (Prism live → QSV H.264) covers both outcomes.
2. **TikTok resolution-tier gating**: no official doc lists follower-count → resolution unlocks; only access gating (1K/10K) and quality presets are documented. If 1080P60 is greyed out, cause = account eligibility or device specs, per the access/troubleshooting articles.
3. **Projector vs virtual camera load delta** has no published benchmark; the projector's extra cost (window render + full-screen capture) is argued from OBS KB purpose statements, not numbers.
4. **SLOBS UI drift**: the Advanced-mode Recording tab path is documented in Streamlabs' help article and code, but the exact current build's menu labels were not verified on a live install.
5. **IdeaPad Pro 5 16IMH9-specific sustained thermal behavior** under *encoding-only* load (vs games) is not measured in reviews; the 65 W PL1 and shared-cooling notes are from Notebookcheck's sibling reviews.

Suggested next steps: (a) run one 30-min test with all three outputs live and HWiNFO logging CPU/GPU temps + OBS dropped-frame stats; (b) open TikTok's LIVE-quality panel during the test to read the auto-selected encoder; (c) verify SLOBS Advanced-mode labels on the installed build; (d) if thermals exceed ~90°C CPU sustained, drop recording or add a cooling pad.

---

## Supervisor coordination
No supervisor contact needed — research completed without blocking decisions; the runtime-bridge instructions required no coordination for this run.