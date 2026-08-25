# R1 — Local AI Image Generation for Roblox-Style Game Icons (RTX 3060 12GB, $0)

**Research wave:** AI image generation for Roblox-style game icons
**Scope:** R1 — Local generation path (free, on-device)
**Researcher:** leaf subagent (deepseek-v4-flash)
**Date:** 2026-08-21
**Hardware target:** RTX 3060 12GB, Windows, comfortable-with-technical user, commercial use assumed.
**Method note:** SearXNG instance was reachable but returned no organic results (only infoboxes) for all queries on 2026-08-21, so all discovery was done via the `websearch` (Exa) fallback per the opencode-web-research skill routing. Every material claim below was read from the cited page (not just a snippet). Claims I could not verify are marked **UNVERIFIED**.

---

## 1. Best open models for cartoony/stylized icon art on 12GB VRAM

### The short list (all verified to fit 12GB)

| Model | Base | Size | Min VRAM | Cartoon/icon fit | License (commercial?) | Source |
|---|---|---|---|---|---|---|
| **SDXL 1.0 base** | SDXL | ~6.6 GB fp16 | 8 GB | General-purpose; add icon/Roblox LoRAs | CreativeML Open RAIL++-M — commercial OK | specpicks.com/reviews/comfyui-rtx-3060-12gb-local-stable-diffusion-2026 (acc. 2026-08-21) |
| **Illustrious XL v2.0** | SDXL | 6.46 GB | 8 GB | Clean anime/illustration, best tag adherence; anchors huge LoRA ecosystem | CreativeML Open RAIL (SDXL) per OnomaAI — commercial OK (see §5) | civitai.com/models/1489531/illustrious-xl-v20-stable; huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0/discussions/1 (acc. 2026-08-21) |
| **NoobAI XL (Eps)** | Illustrious | 6.5 GB | 8 GB | Deepest booru character/tag knowledge, webtoon-lean | FAIPL 1.0-SD + own commercial prohibition — **risky for commercial** (see §5) | insiderllm.com/guides/best-anime-stylized-checkpoints-local-image-generation/; huggingface.co/Laxhar/noobai-XL-1.0 (acc. 2026-08-21) |
| **Pony Diffusion V6 XL** | SDXL | 6.9 GB | 8 GB | Stylized characters, biggest LoRA library | Modified FAIPL — commercial inference on monetized services **prohibited**; contact purplesmart.ai for commercial (see §5) | tensor.art/models/714585990280309972; huggingface.co/LyliaEngine/Pony_Diffusion_V6_XL (acc. 2026-08-21) |
| **FLUX.1 schnell** | Flux (DiT) | fp8 ~11 GB | 12 GB (tight) | Good prompt adherence; **no native alpha**; thin cartoon/icon LoRA ecosystem | **Apache 2.0 — commercial OK** | huggingface.co/black-forest-labs/FLUX.1-schnell; github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-schnell.md (acc. 2026-08-21) |
| **FLUX.1 dev** | Flux (DiT) | fp8 ~11 GB | 12 GB (tight, lowvram+tiled VAE) | Higher quality than schnell | **Non-commercial license — NOT usable** | github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev (acc. 2026-08-21) |
| **FLUX.2 [klein] 4B** | Flux2 | ~8–13 GB | 12 GB | Fast 4-step; **native image editing/multi-reference** (great for tier consistency); Apache 2.0 | **Apache 2.0 — commercial OK** | github.com/black-forest-labs/flux2; localaimaster.com/blog/flux-2-local-setup-guide; blog.comfy.org/p/flux2-klein-4b-fast-local-image-editing (acc. 2026-08-21) |
| **FLUX.2 [klein] 9B** | Flux2 | ~15 GB fp8 / ~10 GB GGUF Q8 | 16 GB (fp8); 12 GB via GGUF | Higher quality than 4B | **Non-commercial — NOT usable** | localaimaster.com/blog/flux-2-local-setup-guide; neurocanvas.net/blog/flux-2-klein-comfyui-guide (acc. 2026-08-21) |
| **SD 3.5 Medium** | SD3.5 | ~5.8 GB | 12 GB | Photoreal-leaning, not cartoon | SD3.5 license (commercial OK) | civitai.com/articles/8511/my-3060-12gb-speeds-sd35-or-flux-or-sdxl-or-hunyuan-video-or-ltxv (acc. 2026-08-21) |

### Which gives the "bold, rounded, playful Roblox catalog" look?

There is **no single base model** that natively produces the Roblox catalog look — it comes from **base model + style LoRA**. Verified community options:

- **Roblox-style LoRAs (verified to exist on Civitai):**
  - **ROBLOX Blocky | Style** (SD 1.5 LoRA, weights ~0.7–1.0) — civitai.com/models/197863/roblox-blocky-or-style (acc. 2026-08-21)
  - **Roblox-ify Anything - Illustrious** (Illustrious LoRA, trigger `by r0b10x, roblox style`, strength 0.8) — civitai.com/models/1136514/roblox-ify-anything-illustrious (acc. 2026-08-21)
  - **rorender style** (Roblox render style) — civarchive.com/models/817253 (acc. 2026-08-21)
  - **Roblox Chibi Doll Bundle Style** (Illustrious + PonyXL + Flux.2 Klein 4B/9B versions; prompt `3d, chibi, roblox, solid cirle eyes, no mouth, blush`) — civitai.com/models/400063/roblox-chibi-doll-bundle-style-illustrious-ponyxl (acc. 2026-08-21). This is the closest match to the rounded/chibi catalog look.
  - **vector game icons** (Illustrious LoRA, tagged "perfectly for roblox games") — civitai.com/models/1768849/vector-game-icons (acc. 2026-08-21)

- **Game-icon LoRAs (verified):**
  - **Game Icon Forge** (SDXL LoRA, trigger `gicon`, fantasy RPG inventory icons, "no frame, transparent background" option; Euler a, 30–32 steps, CFG 6–7, 1024×1024, weight 0.85) — civarchive.com/models/2750041 (acc. 2026-08-21)
  - **Zavy's Fantasy Icons - SDXL** (trigger `zavy-fntscn`) — civarchive.com/models/423581 (acc. 2026-08-21)
  - **[SDXL] RPG Item Icons** — civarchive.com/models/2507819 (acc. 2026-08-21)
  - **Game Icons Illustrious** (monochrome, white bg; convert white→transparent in an art program) — civitai.com/models/1232188/game-icons-illustrious (acc. 2026-08-21)
  - **Game-Icons.net Style** (SDXL, trained on 4131 CC BY 3.0 icons) — civitai.com/models/637160 (acc. 2026-08-21)
  - **2D Icon LoRA** (SD 1.5, `2d icon. <subject>. <lora:icon2:0.9>`) — civitai.com/models/94742/2d-icon-lora (acc. 2026-08-21)
  - **Game icon** (SDXL, `2d icon. <subject>. <lora:game_icon_v1.0:1>`) — civitai.com/models/141066/game-icon (acc. 2026-08-21)

**Recommended combo for the target look:** SDXL 1.0 base (or Illustrious XL v2.0) + a game-icon LoRA (e.g., Game Icon Forge) + a Roblox/chibi style LoRA (e.g., Roblox Chibi Doll or Roblox-ify Anything). Note LoRA ecosystems are **not cross-compatible** — a Pony LoRA won't work on Illustrious and vice versa (aiofm.info/en/guides/pony-vs-illustrious, acc. 2026-08-21; insiderllm.com, acc. 2026-08-21).

### Newer 2025–2026 base models worth knowing

- **FLUX.2 [klein] 4B** (released Jan 15, 2026) is the notable 2026 addition that fits 12GB and is Apache 2.0. It unifies text-to-image and **image editing with multi-reference** in one model — directly useful for tiered potion consistency (github.com/black-forest-labs/flux2; blog.comfy.org/p/flux2-klein-4b-fast-local-image-editing, acc. 2026-08-21). Caveat: no native alpha output (transparify.app/blog/ai-image-transparent-background, acc. 2026-08-21), and the cartoon/icon LoRA ecosystem is still thin.
- **FLUX.2 [dev]** (32B) needs ~19 GB even as GGUF Q4 — not a 12GB card (localaimaster.com/blog/flux-2-local-setup-guide, acc. 2026-08-21).
- **SD 3.5 Medium** runs on 12GB (~1.03 s/it at 1024²) but is photoreal-leaning, not cartoon (civitai.com/articles/8511, acc. 2026-08-21).
- **SDXL Turbo / Lightning** (4–8 step distilled) give ~4–6 s/images on the 3060 for fast iteration (specpicks.com/reviews/comfyui-sdxl-flux-rtx-3060-12gb-image-generation-2026, acc. 2026-08-21).

---

## 2. Frontends: ComfyUI vs Forge/A1111 vs InvokeAI

Verified comparison sources: mustafa.net/2026/07/07/stable-diffusion-webui-vs-comfyui-vs-invokeai-which-to-self-host/; plugnode.ai/blog/invokeai-vs-comfyui; aifoss.dev/blog/comfyui-vs-automatic1111-vs-forge-2026/; aifoss.dev/blog/invokeai-review-2026/; gigagpu.com/comfyui-vs-forge-vs-a1111-production/ (all acc. 2026-08-21).

| Dimension | ComfyUI | Forge (A1111 fork) | Automatic1111 | InvokeAI |
|---|---|---|---|---|
| Interface | Node graph | Form (A1111-style) | Form | Canvas-first + nodes |
| Learning curve | Steep (3–6 h+) | Low | Low | Moderate (1–2 h) |
| Batch / parameter sweeps | **Best** (native, reproducible graphs) | Good (scripts) | Good (scripts) | Limited vs ComfyUI |
| Consistency workflows (IP-Adapter, ControlNet, LayerDiffuse) | **Best** (first support, custom nodes) | Good (A1111-compatible extensions) | Good but slower | Good, curated |
| VRAM efficiency (SDXL 1024²) | ~5.5 GB | ~5.8 GB | ~7 GB | ~6 GB |
| Speed vs A1111 | 2–3× faster | 2–3× faster | baseline | ~A1111+ (Forge closes gap) |
| Flux native support | Yes | Yes | Partial (extensions) | Yes (incl. Flux.2 Klein) |
| License | GPL-3.0 | AGPL-3.0 | AGPL-3.0 | Apache 2.0 |
| Maintenance status 2026 | Active (Comfy-Org) | Upstream in maintenance mode; use **Forge Neo / reForge** forks | Stalled (last release Feb 2025) | Active |

**Verdict for this use case (batch icon generation + tier consistency):** **ComfyUI is the best fit.** Reasons, all verified:
- Batch generation and parameter sweeps are native and reproducible (same graph + seed = same output) — plugnode.ai and sider.ai (acc. 2026-08-21).
- New model/technique support lands first (Flux.2, LayerDiffuse, IP-Adapter) — aifoss.dev (acc. 2026-08-21).
- Best VRAM efficiency on the 3060 (gigagpu.com, acc. 2026-08-21).
- The transparency (LayerDiffuse) and consistency (IP-Adapter) nodes this task needs are ComfyUI-native.

**Forge** is the right pick if the user wants a form-based UI with zero learning curve and still good batch throughput; use the **Forge Neo or reForge** forks, not the stalled upstream (aifoss.dev, acc. 2026-08-21). **A1111** is not recommended for new setups in 2026 (stalled, slowest, most VRAM). **InvokeAI** is the most polished artist UI with the best inpainting canvas, but its batch automation is weaker than ComfyUI — a good secondary tool, not the primary batch engine (aifoss.dev/blog/invokeai-review-2026/, acc. 2026-08-21).

---

## 3. Transparent-background icon generation

### The "SDXL ICONS base model / ICONS-lora" — status: **UNVERIFIED / could not locate**

I could not verify a model literally named "SDXL ICONS base model" or "ICONS-lora" from live sources on 2026-08-21 (searched Civitai API `query=ICONS` for Checkpoint and LoRA types, plus multiple web queries). The Civitai API's top "ICONS" hits are **Icons.Redmond – App Icons LoRA** (civitai.com/models/122827) and **App Icons** (SD 1.5 checkpoint, civitai.com/models/93). If the caller has a specific model in mind, it needs a direct link to verify. **The verified equivalents that do the same job:**

### Verified approaches (all free/local except where noted)

1. **LayerDiffuse — native RGBA generation (recommended).** Turns SDXL (or SD 1.5) into a transparent-image generator via a rank-256 LoRA (`layer_xl_transparent_attn.safetensors`, ~709 MB) + a transparent VAE decoder (~199 MB). Works in ComfyUI (`huchenlei/ComfyUI-layerdiffuse`) and Forge (`lllyasviel/sd-forge-layerdiffuse`). Generation dims must be multiples of 64. Sources: github.com/huchenlei/ComfyUI-layerdiffuse; github.com/layerdiffusion/sd-forge-layerdiffuse; arxiv.org/html/2402.17113v3 (acc. 2026-08-21).
   - **Important caveat:** LayerDiffuse works with SDXL base and Pony, but **fails with retrained models like NoobAI/Illustrious/Animagine** (github.com/huchenlei/ComfyUI-layerdiffuse/issues/124, acc. 2026-08-21). Workaround exists: generate with a LayerDiffuse-compatible checkpoint, extract the alpha mask, then re-render with the desired checkpoint using ControlNet (depth + HED) and crop with the mask — civitai.com/models/1461145/layer-diffuse-with-any-model-comfyui-workflow (acc. 2026-08-21).
2. **Generate on a flat background + matte (the standard pipeline).** No current model emits a clean cut-out icon with transparency natively; the standard is generate-on-flat-bg then remove background (danmackinlay.name/notebook/image_ai_clients.html, acc. 2026-08-21). Matte options:
   - **rembg** — free, MIT, local CLI/library (U²-Net, IS-Net, BiRefNet, RMBG models), unlimited batch: `rembg p in/ out/`. github.com/danielgatis/rembg (acc. 2026-08-21).
   - **BRIA RMBG-2.0** — state-of-the-art, but **CC BY-NC 4.0 (non-commercial)**; commercial use needs a paid BRIA license. github.com/Bria-AI/RMBG-2.0 (acc. 2026-08-21).
   - **remove.bg** — paid API, ~€9/25 credits (~$0.36–0.39/img), first 50 API calls/month free. remove.bg/pricing; sammapix.com/blog/best-free-remove-bg-alternatives-2026 (acc. 2026-08-21).
   - **Photoroom API** — ~$0.02/img (imagic-ai.com/blog/batch-background-removal, acc. 2026-08-21).
   - **Chroma-key trick** — render on solid magenta/green, flood-fill key it out (pixa, icon-normalizer) — github.com/techarm/pixa; github.com/Jcd1230/icon-normalizer (acc. 2026-08-21).
3. **Iconator workflow** — sdxl-turbo + canny ControlNet + HSV color utilities to composite alpha; generates sticker/icon with transparency (openart.ai/workflows/bmad/iconator/zVU2gOA9AaHCWBti97Ub, acc. 2026-08-21).

**Recommendation:** Use LayerDiffuse for native alpha on SDXL base (fast, one pass), or generate on a flat background and matte with rembg (works with any checkpoint, including Illustrious). For a commercial product, avoid BRIA RMBG-2.0 without a license.

---

## 4. Consistency workflow for TIERED potions (same potion, color/rarity changes)

Verified sources: multigrid.ai/learn/consistent-characters; apatero.com/blog/comfyui-character-consistency-advanced-workflows-2026; creativetoolshub.com/2026/05/consistent-character-design-in-stable.html; dev.to/sm1ck/ip-adapter-lora-for-product-catalog-rendering-putting-shop-items-on-ai-characters-5h36; technolynx.com/post/control-image-generation-with-stable-diffusion (all acc. 2026-08-21).

Key principle (verified): a diffusion model has no persistent identity — consistency must be injected via conditioning. Ranked by reliability for a *single object* (a potion):

1. **Fixed seed + prompt template (free, zero setup).** A fixed seed reproduces composition/layout when the prompt changes slightly; it is a control for comparison, **not** identity — it fails once pose/scene changes (multigrid.ai, acc. 2026-08-21). For tiered potions where only color/rarity changes, this is the cheapest first attempt: same seed, same prompt, swap the color words.
2. **img2img recolor (free, no training).** Take the accepted tier-1 potion image, run img2img at low denoise (0.3–0.5) with the color/rarity words changed. This preserves the bottle shape while shifting color — the standard approach for color variants. (Consistency via img2img is standard practice; see stable-diffusion-art.com/consistent-character-view-angle/ for the img2img+ControlNet pattern, acc. 2026-08-21.)
3. **IP-Adapter (free, no training).** Reference-image conditioning; for item identity use moderate weight (~0.3–0.5, lower half of 0–1) with early handoff (`end_at` ~0.7–0.9) so the prompt still controls color (dev.to/sm1ck, acc. 2026-08-21). Good for "make tier 2 look like tier 1 but red."
4. **Trained LoRA (most reliable, needs a dataset + training).** Train a small LoRA on 20–40 images of the potion design; identity lives in the weights and holds across color/scene changes. Rank 16–32, alpha=rank, train at native resolution (multigrid.ai; creativetoolshub.com, acc. 2026-08-21). This is the only method that reliably carries non-facial object identity (a specific bottle shape).
5. **ControlNet (structure, not identity).** Canny/depth locks the silhouette — useful if the potion shape must be pixel-consistent across tiers, but it does not carry color/identity on its own; pair with prompt or LoRA (picovix.app/blog/consistent-character-stable-diffusion, acc. 2026-08-21).
6. **FLUX.2 [klein] 4B native image editing (2026 option).** Klein 4B does text-to-image **and** single/multi-reference image editing in one model — you can feed the tier-1 potion as a reference and ask for a red variant, no adapters needed (github.com/black-forest-labs/flux2; blog.comfy.org/p/flux2-klein-4b-fast-local-image-editing, acc. 2026-08-21). Apache 2.0, fits 12GB.

**Recommended tiered-potion recipe (SDXL path):** (1) lock a seed + prompt template for the base potion; (2) generate tier 1; (3) img2img at low denoise for tiers 2–3 color/rarity variants; (4) if the bottle shape drifts, add a canny ControlNet of the tier-1 image or train a small potion LoRA; (5) matte with rembg or LayerDiffuse for transparent PNGs. Batch all tiers in one ComfyUI workflow with a fixed seed and a prompt list.

---

## 5. Licensing for commercial use (critical for this user)

- **FLUX.1 schnell** — Apache 2.0, commercial use explicitly permitted (huggingface.co/black-forest-labs/FLUX.1-schnell; github.com/black-forest-labs/flux/blob/main/model_cards/FLUX.1-schnell.md, acc. 2026-08-21).
- **FLUX.1 dev / FLUX.2 dev / FLUX.2 klein 9B** — non-commercial license; commercial use requires a BFL license (github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev; github.com/black-forest-labs/flux2, acc. 2026-08-21).
- **FLUX.2 [klein] 4B** — Apache 2.0, commercial OK (github.com/black-forest-labs/flux2, acc. 2026-08-21).
- **SDXL 1.0** — CreativeML Open RAIL++-M; outputs usable commercially (ai-image-journey.com/2025/10/sdxl-license.html, acc. 2026-08-21).
- **Illustrious XL v2.0** — OnomaAI states they now redistribute under **CreativeML Open RAIL (SDXL)** (huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0/discussions/1, acc. 2026-08-21). One secondary source describes v2.0 as CreativeML Open RAIL-**M** (ai-image-journey.com, acc. 2026-08-21) — minor conflict between RAIL vs RAIL-M; both are permissive-with-ethical-use licenses, but the exact variant should be confirmed on the model card before shipping commercial assets. Note v0.1 was FAIPL 1.0-SD (share-alike, non-exclusive).
- **NoobAI XL** — FAIPL 1.0-SD **plus its own "commercial prohibition" and mandatory sharing of prompts/workflows** (huggingface.co/Laxhar/noobai-XL-1.0, acc. 2026-08-21). Community analysis argues these extra terms conflict with the underlying FAIPL and are likely unenforceable (civitai.com/articles/18619/what-the-license; civitai.com/articles/9931/regarding-noobai-derivatives, acc. 2026-08-21). **Legally murky — do not rely on NoobAI for commercial work.**
- **Pony Diffusion V6 XL** — modified FAIPL 1.0-SD: commercial inference on monetized websites/apps is prohibited; commercial use requires contacting purplesmart.ai (tensor.art/models/714585990280309972; huggingface.co/LyliaEngine/Pony_Diffusion_V6_XL, acc. 2026-08-21). **Not clean for commercial use without permission.**
- **BRIA RMBG-2.0** — CC BY-NC 4.0, non-commercial only (github.com/Bria-AI/RMBG-2.0, acc. 2026-08-21).
- **rembg** — MIT, free for commercial (github.com/danielgatis/rembg, acc. 2026-08-21).
- **LayerDiffuse** — open-source (Apache-2.0 repo), free for commercial (github.com/layerdiffusion/LayerDiffuse, acc. 2026-08-21).

**Bottom line for commercial:** SDXL 1.0, Illustrious XL v2.0, FLUX.1 schnell, FLUX.2 klein 4B, rembg, LayerDiffuse are the safe picks. Avoid NoobAI, Pony V6, FLUX.1/2 dev, FLUX.2 klein 9B, and BRIA RMBG-2.0 for commercial use. Always check each LoRA's own page for its license (Civitai shows per-model commercial-use flags).

---

## 6. VRAM/RAM needs and generation speed on the RTX 3060 12GB

Verified benchmarks (specpicks.com series, acc. 2026-08-21; civitai.com/articles/8511, acc. 2026-08-21):

| Workload | Steps | Time/img | Peak VRAM | Notes |
|---|---|---|---|---|
| SD 1.5 512² | 20 | ~2 s | ~3.4 GB | trivial |
| **SDXL 1024²** | 30 | **~11–22 s** | **8.5–9.8 GB** | batch=1 comfortable; batch=2 needs attention slicing (~26 s, 11.4 GB) |
| SDXL + refiner | 30+8 | ~16–22 s | ~9.9–11 GB | |
| SDXL + 1 ControlNet | 25 | ~18–30 s | ~10.6–11.3 GB | fits |
| SDXL + 2 ControlNets | — | — | ~11.9 GB | borderline, skip |
| SDXL Turbo | 4 | ~4 s | ~8.2 GB | fast iteration |
| SDXL Lightning | 8 | ~6 s | ~8.4 GB | |
| SD 3.5 Medium 1024² | 28 | ~12.5 s | ~9.2 GB | ~1.03 s/it |
| **FLUX.1 schnell fp8 1024²** | 4 | **~13–18 s** | **~10–11.4 GB** | 4-step distilled |
| FLUX.1 dev fp8 1024² | 20 | ~60–95 s | ~11.6 GB | needs `--lowvram` + tiled VAE; batch=1 only |
| FLUX.1 dev GGUF Q4 | 20 | ~55–92 s | ~8.5–9.2 GB | |
| FLUX.2 klein 4B | 4 | **UNVERIFIED on 3060** (sub-second on 5090; 12GB-class model) | ~8–13 GB | Apache 2.0; see §1 |

- **it/s:** SDXL ~1.6–4.6 it/s on the 3060 12GB (civitai.com/articles/8511; specpicks.com/reviews/best-gpu-for-stable-diffusion-under-400-2026, acc. 2026-08-21). Flux dev fp8 ~0.9–1.2 it/s.
- **System RAM:** 32 GB recommended; 16 GB is tight (specpicks.com/reviews/comfyui-rtx-3060-12gb-local-stable-diffusion-2026, acc. 2026-08-21). NVMe SSD strongly recommended (model loads 4–8 s on NVMe vs 30–60 s on HDD).
- **VRAM-saving flags that matter on this card:** `--medvram`/`--lowvram`, tiled VAE decode, fp8/GGUF weights for Flux, batch size 1, cap resolution at 1024² (specpicks.com/reviews/comfyui-sdxl-flux-rtx-3060-12gb-image-generation-2026, acc. 2026-08-21). Forge: `--xformers` gives ~20–40% throughput uplift on Ampere (specpicks.com/reviews/stable-diffusion-webui-forge-rtx-3060-12gb-2026, acc. 2026-08-21).

**Practical takeaway:** SDXL-class models are the sweet spot — interactive (~11–22 s/img), fit with headroom for 1 ControlNet + LoRA stack. Flux schnell is usable for quick drafts; Flux dev is one-image-per-90s territory (fine for final renders, not iteration). A 20-image icon batch at SDXL ≈ 4–8 minutes.

---

## 7. Verdict

**Local is clearly viable for this use case on an RTX 3060 12GB, at $0 marginal cost.**

- **Recommended model stack:** **ComfyUI + SDXL 1.0 base (or Illustrious XL v2.0) + a game-icon LoRA (Game Icon Forge / Zavy's Fantasy Icons) + a Roblox/chibi style LoRA (Roblox Chibi Doll / Roblox-ify Anything)**. This gives the bold, rounded, playful catalog look with **commercial-safe licensing** (SDXL and Illustrious v2.0 are permissive; avoid NoobAI/Pony/Flux-dev for commercial).
- **Recommended frontend:** **ComfyUI** — best batch generation, reproducible graphs, native LayerDiffuse + IP-Adapter + ControlNet support, and the best VRAM efficiency on 12GB. Forge (Neo/reForge) is the fallback if the user wants a form UI.
- **Transparency:** LayerDiffuse for native RGBA on SDXL base, or generate-on-flat-background + **rembg** (free, MIT) for any checkpoint. Avoid BRIA RMBG-2.0 commercially without a license.
- **Tiered potion consistency:** fixed seed + prompt template → img2img recolor at low denoise for tiers → add a small potion LoRA or canny ControlNet if the shape drifts. **FLUX.2 [klein] 4B (Apache 2.0, fits 12GB) is the promising 2026 alternative** with native multi-reference editing that does this in one model.
- **Speed:** ~11–22 s per SDXL 1024² icon; a full tier set of ~20 icons is a few minutes of GPU time. 32 GB RAM + NVMe recommended.
- **Cost:** $0 (all tools/models above are free; electricity only). remove.bg/Photoroom only if the user wants paid matting quality (~$0.02–0.39/img).

**Anomalies / dead ends:** (1) SearXNG returned no organic results all session — all discovery via Exa fallback. (2) A model literally named "SDXL ICONS base model" / "ICONS-lora" could not be located/verified — closest verified equivalents are LayerDiffuse + the icon LoRAs listed in §3; needs a direct link to confirm. (3) FLUX.2 klein 4B speed on a 3060 specifically is UNVERIFIED (only 5090 numbers found). (4) Illustrious v2.0 license variant (RAIL vs RAIL-M) conflicts between two sources — confirm on the model card before commercial shipping.
