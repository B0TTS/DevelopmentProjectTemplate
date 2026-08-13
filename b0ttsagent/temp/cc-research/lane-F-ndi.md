# Research: NDI vs HDMI Capture Card at 1080p60 for Dual-PC Livestreaming (Gaming PC → Stream Laptop)

**Scope:** Gaming PC currently sends OBS fullscreen projector over a free HDMI output into a capture card on the stream PC. Question: can NDI replace the capture card with **equal or better quality at 1080p60**, assuming network is either wired gigabit Ethernet or WiFi 6, with the user's priorities being **quality first** and **minimal gaming-PC overhead** (encoding on the stream PC is intentional).

## Summary

Yes — **high-bandwidth NDI over wired gigabit can match and marginally exceed a generic USB3 capture card's quality at 1080p60** (8-bit 4:2:2 SpeedHQ near-lossless vs. typical 8-bit 4:2:0 uncompressed from a cheap card), but it does so at the cost of adding CPU load to the gaming PC and a network dependency. **NDI HX3 does not beat the generic card on quality** (same 4:2:0 8-bit chroma, lossy short-GOP H.264) — it only wins where bandwidth is constrained (WiFi). Given the capture card **already achieves the offload goal at zero gaming-PC cost**, the added complexity of NDI is **not worth it** for a quality-first, minimal-overhead user: the marginal chroma-fidelity gain is mostly erased by the final 4:2:0 stream encode, and the projector+card path adds ~0% CPU. Keep the card; NDI is a viable zero-cost experiment on wired gigabit, and a WiFi fallback only in HX3 form.

---

## 0. Corrections to the task's premises (important)

- **High-bandwidth NDI at 1080p60 is ~105–150 Mbps, not 125–180.** Official NDI white paper: "up to 150 Mbps" per 1080p60 stream [Source](https://docs.ndi.video/all/getting-started/white-paper/bandwidth); official Vizrt bandwidth tables: 105–132 Mbps (128–165 Mbps with alpha) [Source](https://docs.vizrt.com/viz-now-launchpad/1.4/Estimating_Bandwidth_Requirements.html). Community guide: 135–150 Mbps [Source](https://jemproductions.fi/guides/ndi-bandwidth-explained/). Codec is SpeedHQ (intra-frame, "I-frame-ish" is accurate) — typically 8-bit **4:2:2** (SpeedHQ2) [Source](https://ndi.video/wp-content/uploads/2023/09/NDI-5.6-White-Paper-2023.pdf).
- **NDI HX3 is NOT 6–20 Mbps.** That range is NDI HX2 territory. Official HX3 numbers: **~62 Mbps (H.264) / ~50 Mbps (H.265) maximum at 1080p60**, short GOP, "no visible compression artifacts", glass-to-glass <100 ms average [Source](https://docs.ndi.video/brand/ndi-formats/understanding-ndi-formats/ndi-hx3); typical deployments run 30–60 Mbps [Source](https://jemproductions.fi/guides/ndi-bandwidth-explained/). HX2 (long-GOP HEVC/H.264): ~2–16 Mbps, 100–300 ms latency [Source](https://flussonic.com/blog/news/news-ndi-ingest).
- All NDI HX variants (HX/HX2/HX3) are **8-bit 4:2:0**; only high-bandwidth NDI carries 4:2:2/4:2:2:4 (SpeedHQ2/SpeedHQ7) [Source](https://docs.ndi.video/all/using-ndi/ndi-for-video/ndi-encoding-support-matrix/summary-table).

---

## Findings

### 1. NDI mode landscape (concrete numbers)

| Mode | Codec | Bandwidth @1080p60 | Chroma | Latency (glass-to-glass) |
|---|---|---|---|---|
| **NDI High Bandwidth** | SpeedHQ (intra-frame) | 105–132 Mbps typical; max ~150 Mbps (to ~165 with alpha) | 8-bit 4:2:2 | "Ultra low"; cert <100 ms avg; ~1–2 frames typical |
| **NDI HX3** | H.264/HEVC, short GOP | ~62 Mbps (H.264) / ~50 Mbps (H.265) max; 30–60 typical | 8-bit 4:2:0 | Cert <100 ms avg |
| **NDI HX2** | HEVC/H.264 long GOP | ~16 Mbps (H.264) / ~11 Mbps (H.265) max | 8-bit 4:2:0 | 100–300 ms — not for live |
| **Generic USB3 card** | None (uncompressed YUY2/NV12 to OBS) | n/a (USB3 bus) | 8-bit 4:2:2 or 4:2:0 | ~1–2 frames via HDMI |
| **High-end PCIe card** | None (uncompressed) | n/a | up to 10-bit 4:2:2 | ~1 frame via HDMI |

Sources: [NDI bandwidth white paper](https://docs.ndi.video/all/getting-started/white-paper/bandwidth), [NDI HX3 docs](https://docs.ndi.video/brand/ndi-formats/understanding-ndi-formats/ndi-hx3), [NDI certification latency requirements](https://docs.ndi.video/all/developing-with-ndi/ndi-certified/certification-guidelines/technical-requirements), [Flussonic NDI ingest table](https://flussonic.com/blog/news/news-ndi-ingest), [NDI 5.6 White Paper](https://ndi.video/wp-content/uploads/2023/09/NDI-5.6-White-Paper-2023.pdf).

### 2. Live quality comparison at 1080p60 (4-way)

Ranked by signal fidelity fed into the stream PC's encoder:

1. **High-end PCIe card** (e.g., DeckLink/Magewell/Elgato Pro): uncompressed digital HDMI copy, up to 10-bit 4:2:2. Best possible, zero gaming-PC load, most reliable. Only real downside: cost.
2. **High-bandwidth NDI (wired)**: 8-bit 4:2:2 SpeedHQ, near-lossless — no visible compression artifacts. **Measurably better chroma fidelity than a 4:2:0 USB3 card** (double chroma resolution; relevant for chroma keying, grading, and local recording), and it avoids cheap-card quirks (RGB→YUV conversion quirks, fixed-level/auto-level HDMI issues). No ADC stage at all — the "signal" is the rendered frame itself. NDI-certified latency is <100 ms but realistically ~1–2 frames on a clean LAN [Source](https://jemproductions.fi/guides/ndi-bandwidth-explained/). Community experience: quality comparable or better, but "often not 100% smooth" unless the network is clean [Source](https://www.reddit.com/r/Twitch/comments/83f1bo/ndi_vs_capture_card_whats_better/).
3. **Generic USB3 capture card**: uncompressed 8-bit 4:2:0 (NV12) or 4:2:2 (YUY2) depending on model — no lossy compression in the capture path, deterministic, zero gaming-PC load, no network failure modes. Caveats: 8-bit only, chroma subsampling on cheap cards, occasional HDMI handshake/level quirks.
4. **NDI HX3**: lossy H.264/HEVC 8-bit 4:2:0 at ≤62 Mbps. At that bitrate with short GOP it looks very good ("no visible artifacts" per NDI), but on fast-motion/particle-heavy gaming content it can show slight blocking/mosquito noise vs. the uncompressed card path — same subsampling, added lossy compression. It does **not** beat the generic card on a clean wired link; it exists to fit constrained links [Source](https://docs.ndi.video/brand/ndi-formats/understanding-ndi-formats/ndi-hx3).

**Key caveat:** the stream PC then encodes everything to x264/NVENC **8-bit 4:2:0 at ~6–8 Mbps** for Twitch/YouTube. At that point the capture-path differences (4:2:2 vs 4:2:0, near-lossless vs lossy) are largely erased for the viewer. The 4:2:2 advantage of full NDI/PCIe cards survives only in *pre-encode processing* (keying, grading, scaling, overlays) and high-bitrate local recording [Source](https://www.haivision.com/blog/broadcast-video/10-bit-pixels-422-chroma-subsampling-for-live-video-contribution/). Also note 4:2:2→4:2:0 cascade quality loss is a well-studied effect [Source](https://www.ntt-innovative-devices.com/en/info/digital_video/picture-quality-of-cascaded-video-codec/).

### 3. Sender overhead on the gaming PC

**Current path (projector + capture card):** OBS composites the scene, the fullscreen projector is an extra lightweight output render (OBS KB: projectors are "incredibly strong and lightweight" [Source](https://obsproject.com/kb/power-of-projectors)); the capture card digitizes over HDMI with **zero CPU/GPU cost** on the gaming PC ("it has absolutely no impact on your gaming PC" [Source](https://obsproject.com/forum/threads/capture-card-or-ndi-plugin-wich-is-better.125603/)). Cost ≈ near-zero CPU, a few % GPU for the extra blit/scanout.

**DistroAV "Main Output" (full NDI):** same OBS composition, but now SpeedHQ-encoded **on the CPU** — "The High Bandwidth NDI codec will operate on the CPU" [Source](https://community.ndi.video/mod/forum/discuss.php?d=214). Measured overhead reference points: DistroAV maintainer testing showed Main Output costs <3% CPU at 1080p30 media even with *no receiver* connected [Source](https://github.com/DistroAV/DistroAV/pull/1402); with an active receiver at 1080p60 and live gaming, community reports place it at single-digit to ~10% CPU depending on CPU generation, and a documented history of CPU spikes/frame-time issues on weak CPUs [Source](https://github.com/Palakis/obs-ndi/issues/94), [Source](https://github.com/DistroAV/DistroAV/issues/99). GPU delta vs. the projector is ~zero (same render texture path).

**NDI Screen Capture HX:** DXGI desktop capture + GPU-accelerated H.264/HEVC (NVENC) — "GPU acceleration significantly reduces your system's CPU workload" [Source](https://docs.ndi.video/all/using-ndi/ndi-tools/ndi-tools-for-windows/screen-capture-hx). Near-zero CPU, ~1–3% NVENC engine utilization (dedicated silicon on NVIDIA GPUs, minimal FPS impact), up to 4K120 [Source](https://docs.ndi.video/all/using-ndi/ndi-tools/ndi-tools-for-windows/screen-capture-hx). **But:** it captures the raw desktop, not the OBS composition — it only replaces OBS-as-sender if the gaming PC needs no overlays; and its output is NDI HX (4:2:0), so quality is below full NDI.

**Verdict for (2):** Yes, NDI adds load the projector+card path doesn't have — full NDI adds a CPU encode (modest but real, and it *increases* with game FPS if OBS must render more frames), Screen Capture HX adds NVENC/GPU load instead. The capture card path remains the only one with genuinely ~zero gaming-PC cost. Full NDI's CPU cost also competes with the game for cores/DRAM bandwidth; DistroAV's own guidance: "you can't game at 300 fps and expect OBS and NDI to perform well, for that case/scenario you need a capture card" [Source](https://github.com/DistroAV/DistroAV/wiki/4.-Extras).

### 4. Network requirements

- **Bandwidth:** full NDI 1080p60 ≈ 105–150 Mbps; plan for <80% link utilization (≈800 Mbps usable on 1 GbE) [Source](https://docs.ndi.video/all/getting-started/white-paper/bandwidth), [Source](https://jemproductions.fi/guides/ndi-bandwidth-explained/). One 1080p60 full-NDI stream fits gigabit easily; it does **not** fit 100 Mbps Ethernet.
- **Wired gigabit is the requirement for full NDI.** Official guidance: "Gigabit (1000 Mbps) networks are essential in production workflows" [Source](https://docs.ndi.video/all/getting-started/white-paper/bandwidth). vMix: "High Bandwidth NDI will work over a wireless network but at a reduced frame rate… 100 Mbit recommended per 1080p video feed" [Source](https://www.vmix.com/ndi/).
- **WiFi 6 is NOT acceptable for high-bandwidth NDI; it is marginal-to-acceptable for HX3.** NDI docs: wireless "can impact video performance. While not always recommended, if a device will be on wifi, you'll want to consider at least a WIFI6 or WIFI7 capable device" [Source](https://docs.ndi.video/all/using-ndi/using-ndi-with-hardware/recommended-network-switch-settings-for-ndi). DistroAV wiki: "possible to use OBS with DistroAV through wireless networks, we don't recommend it. The outcome might vary and cause video and audio stuttering or directly suffer sync and delay issues… I personally haven't had luck with high performance WiFi5 networks, only with WiFi6 with some tweaks" [Source](https://github.com/DistroAV/DistroAV/wiki/4.-Extras). Real-world report: "We'd been trying to run NDI over 5 GHz, and the jittering always caused some frame drops" (solved only with 60 GHz WiGig) [Source](https://ndi.video/stories/live-production-using-ndi-over-60-ghz-wi-fi-is-making-waves/). Even WiFi 6's ~500–900 Mbps practical throughput is half-duplex, shared, and jitter-prone — a 105–150 Mbps constant bitrate stream with near-zero jitter tolerance is fragile; HX3 at 50–62 Mbps is the only defensible WiFi option, and only with 5/6 GHz, close range, and a dedicated SSID.
- **Latency/jitter:** NDI default transport is Reliable UDP (RUDP) since NDI 5 — UDP speed with retransmission — so small losses recover but add latency; sustained jitter/loss produces stutter or dropped frames rather than glitches [Source](https://docs.ndi.video/all/getting-started/white-paper/ndi-protocols). On a clean wired LAN, jitter is sub-millisecond and irrelevant; on WiFi, airtime contention and retries are the failure mechanism. NDI ships an analysis CLI (NDI Analysis) for diagnosing this [Source](https://ndi.video/tools/analysis/).
- **Switching/NIC concerns (official NDI switch-settings doc):** all ports gigabit full-duplex; **disable QoS** (per NDI guidance, to avoid delays); **disable jumbo frames** (avoid fragmentation issues — standard 1500 MTU works); enable flow control for TCP; **IGMP snooping/querier only matters if using multicast — NDI defaults to unicast**, and a 1:1 sender→receiver is unicast, so IGMP is a non-issue for this setup [Source](https://docs.ndi.video/all/using-ndi/using-ndi-with-hardware/recommended-network-switch-settings-for-ndi), [Source](https://www.vizrt.com/wp-content/uploads/2024/11/NDI_Best_Practices_with_TriCaster__Final__1_-1.pdf). NIC offloads: defaults generally work; use quality NICs — avoid Killer network software, and Intel i225-V 2.5G has known fault revisions [Source](https://github.com/DistroAV/DistroAV/wiki/4.-Extras).

### 5. Practical setup (if attempted)

1. **Wired:** dedicated gigabit path gaming-PC NIC → switch (or direct cable) → stream-PC NIC; static IPs on a separate subnet; disable WiFi on both PCs during streaming; nothing else heavy on the LAN (NDI docs assume a video-priority network) [Source](https://docs.ndi.video/all/getting-started/white-paper/network-layout).
2. **Gaming PC:** install DistroAV (obs-ndi successor) → Tools → DistroAV Output Settings → enable **Main Output** (full NDI, 4:2:2); set NDI source Latency Mode to Low; enable OBS "Low latency Audio Buffering Mode" for NDI outputs (prevents growing A/V sync buffers) [Source](https://github.com/DistroAV/DistroAV/wiki/4.-Extras).
3. **Stream PC:** add NDI Source; set A/V sync to Source Timing, Latency Low [Source](https://github.com/DistroAV/DistroAV/wiki/4.-Extras).
4. **If WiFi 6 is unavoidable:** use **NDI Screen Capture HX** (GPU H.264/HEVC HX stream, ~50–62 Mbps) rather than full NDI; verify with NDI Analysis and watch for dropped frames. Accept that this is a fallback, not a primary path.
5. **Test discipline:** OBS Log Analyzer + NDI Analysis on both ends; compare against the capture-card path with identical scenes before switching.

---

## Conclusions (clear ranking)

**(a) Wired gigabit available — can high-bandwidth NDI BEAT a generic USB3 capture card at 1080p60 quality?**
**Yes, marginally, and only in signal terms.** Full NDI carries 8-bit 4:2:2 near-lossless vs. the typical card's 8-bit 4:2:0, and has no HDMI digitization stage. Measurably better chroma fidelity (keying/grading/local recording), equal-or-better latency (~1–2 frames vs ~1–2 frames). **But:** to viewers after the final 4:2:0 6–8 Mbps stream encode, the difference is effectively invisible; and "beat" assumes a clean, dedicated gigabit path — the card has zero network failure modes. Practical ranking at 1080p60, wired: PCIe card ≥ high-bandwidth NDI ≈ (very slightly) > generic USB3 card > NDI HX3.

**(b) Is NDI HX3 sufficient to beat the generic card?**
**No.** HX3 is lossy 4:2:0 H.264 at ≤62 Mbps — same chroma as the card's uncompressed NV12 path plus added compression. On a clean wired link the generic card (or full NDI) is better. HX3's only winning scenario is constrained bandwidth — i.e., WiFi — where it's the best available option but still not "better than the card," just "possible without a cable."

**(c) Given the offload is ALREADY achieved by the capture card, is NDI worth it (quality-first, minimal gaming-PC overhead)?**
**No — keep the capture card.** The projector+card path already delivers ~zero gaming-PC CPU cost, deterministic quality, and zero network risk. NDI adds: CPU encode load (full NDI, meaningful during gaming), NVENC/GPU load (Screen Capture HX), network dependency and jitter/stutter failure modes, plus setup/debugging complexity — for a chroma-fidelity gain the final stream encode mostly erases. NDI is the right answer when you *don't have* a card, want to free the HDMI output, or need to send OBS composition without hardware; it is not an upgrade *for this user's stated priorities*. If curiosity wins: A/B test full NDI on wired gigabit with identical scenes — expected outcome: same-to-slightly-better picture, slightly worse frame-time stability under load, and a few % CPU on the gaming PC.

**Confidence: HIGH on bandwidth/latency/chroma facts (official NDI/Vizrt docs, certification requirements); MEDIUM on CPU-percent figures (hardware-dependent, community-measured, no controlled benchmark); MEDIUM on "visibility" judgments (subjective; final-encode-dependent).** WiFi 6 viability for HX3 is best-effort — NDI's own guidance is wired for anything critical.

---

## Sources

**Kept:**
- NDI Bandwidth white paper (docs.ndi.video) — official 150 Mbps/1080p60 figure, gigabit requirement. https://docs.ndi.video/all/getting-started/white-paper/bandwidth
- NDI HX3 format docs — official 62/50 Mbps, <100 ms, "no visible artifacts". https://docs.ndi.video/brand/ndi-formats/understanding-ndi-formats/ndi-hx3
- NDI Screen Capture HX docs — GPU-accelerated H.264/HEVC capture up to 4K120. https://docs.ndi.video/all/using-ndi/ndi-tools/ndi-tools-for-windows/screen-capture-hx
- NDI 5.6 White Paper — SpeedHQ2 = 8-bit 4:2:2, HX3 = 8-bit 4:2:0. https://ndi.video/wp-content/uploads/2023/09/NDI-5.6-White-Paper-2023.pdf
- NDI certification technical requirements — latency caps (<100 ms HB/HX3, <150 ms HX2). https://docs.ndi.video/all/developing-with-ndi/ndi-certified/certification-guidelines/technical-requirements
- NDI recommended switch settings — QoS/jumbo/IGMP/flow-control guidance + WiFi 6/7 note. https://docs.ndi.video/all/using-ndi/using-ndi-with-hardware/recommended-network-switch-settings-for-ndi
- DistroAV wiki (4. Extras) — wireless not recommended, WiFi6 "with tweaks", gigabit minimum, sync/latency-mode guidance, NIC pitfalls. https://github.com/DistroAV/DistroAV/wiki/4.-Extras
- DistroAV PR #1402 — measured Main Output CPU overhead (<3% @1080p30 idle/no receivers). https://github.com/DistroAV/DistroAV/pull/1402
- JEM Productions NDI bandwidth explainer — 135–150 Mbps full NDI, HX3 30–60 Mbps, ~1-frame latency. https://jemproductions.fi/guides/ndi-bandwidth-explained/
- NDI community forum — "High Bandwidth codec operates on CPU; HX on GPU". https://community.ndi.video/mod/forum/discuss.php?d=214
- OBS forum "Capture Card or NDI Plugin" — card has "absolutely no impact on gaming PC". https://obsproject.com/forum/threads/capture-card-or-ndi-plugin-wich-is-better.125603/
- NDI 60 GHz Wi-Fi story — 5 GHz jitter caused frame drops. https://ndi.video/stories/live-production-using-ndi-over-60-ghz-wi-fi-is-making-waves/
- Flussonic NDI table — HX2/HX3/HB bandwidth+latency side-by-side. https://flussonic.com/blog/news/news-ndi-ingest
- vMix NDI page — NDI-over-WiFi caveat, 100 Mbit per 1080p feed. https://www.vmix.com/ndi/
- Haivision chroma/bit-depth blog — why 4:2:2/10-bit matters for contribution. https://www.haivision.com/blog/broadcast-video/10-bit-pixels-422-chroma-subsampling-for-live-video-contribution/
- NTT 4:2:2 vs 4:2:0 cascade study — quality loss in cascaded 4:2:0 encodes. https://www.ntt-innovative-devices.com/en/info/digital_video/picture-quality-of-cascaded-video-codec/
- Reddit r/Twitch NDI vs capture card — community experience: "good, but often not 100% smooth". https://www.reddit.com/r/Twitch/comments/83f1bo/ndi_vs_capture_card_whats_better/
- OBS KB Power of Projectors — projector outputs are lightweight by design. https://obsproject.com/kb/power-of-projectors

**Dropped:**
- yostream.io / streamersize.com / aliexpress wiki / vdo360 — SEO marketing summaries, numbers inconsistent with official docs (e.g., wrong HX3 bitrate ranges).
- Epiphan Pearl-2 docs — says ~125 Mbps for 1080p30 (30 fps), not 60; kept only as corroboration, superseded by official NDI tables.
- NearStream chroma-subsampling blog — useful background but vendor content; cited only via Haivision/NTT instead.
- obs-ndi issue #99 (100% CPU) — old bug report on a FX-6100, not representative of modern hardware; used only as historical evidence that weak CPUs are problematic.

## Gaps

- **No controlled public benchmark** measuring gaming-PC FPS delta (projector+card vs NDI Main Output vs Screen Capture HX) on identical modern hardware — CPU% figures are community-reported and hardware-dependent. A 15-minute A/B test on the actual rig would settle it definitively.
- Whether NDI Screen Capture HX emits HX3-certified streams vs generic HX (H.264 short/long GOP) is not clearly documented; assume "HX-mode H.264/HEVC" at ~HX2/HX3 bitrates depending on bandwidth preset.
- No hard data on WiFi 6 *specific* jitter stats for sustained 50–62 Mbps H.264 unicast; guidance is qualitative ("possible with tweaks, not recommended").
- Capture-card-path chroma detail (4:2:0 NV12 vs 4:2:2 YUY2) varies by model; the user's specific generic USB3 card's negotiated format should be checked in OBS before concluding the NDI 4:2:2 edge matters for them.

## Supervisor coordination
None needed — research complete, no blocking decisions.
