# Wave Spec: AI Image Generation for Roblox Game Icons

**Date:** 2026-08-21
**Requester context:** User wants cartoony/stylized (Roblox-like) tiered potion game icons. RTX 3060 12GB VRAM, comfortable with technical setup. Budget: prefers API-style pricing but max $10–25/month total. Commercial use of outputs: UNKNOWN — assume commercial rights are required unless a license explicitly forbids it (flag per-option).

## Deliverables

Each researcher writes a complete findings markdown file to its assigned path, then returns only a compact summary (key options, costs, verdict).

All pricing/feature claims MUST be verified against live web sources (prices, minimum deposits, free credits, custom model support) — the date is 2026-08-21; do not rely on training data. Cite source URLs + access dates in the findings. If something can't be verified, say so.

## Researchers

### R1 — Local generation path (cost: $0)
- **Output:** `b0ttsagent/temp/research-ai-imagegen/R1-local-comfyui.md`
- **Scope:** Free local text-to-image on RTX 3060 12GB for stylized/cartoon game icons.
  - Best current open models for cartoony/stylized icon art (e.g., SDXL family, Illustrious XL, NoobAI, Pony Diffusion v6, Flux schnell/dev, any newer 2025–2026 base models) — which run in 12GB VRAM and which give the "bold, rounded, playful Roblox catalog" look.
  - Recommended frontends: ComfyUI vs Forge/A1111 vs InvokeAI for a comfortable user — which is best for batch generation and consistency workflows.
  - Transparent-background icon generation (SDXL ICONS base model / ICONS-lora, or remove.bg style approaches) for game assets.
  - Consistency workflow for TIERED potions: same potion across tiers (color/rarity changes) via prompts, seeds, img2img, LoRA, or ControlNet — what actually works.
  - Approx VRAM/RAM needs and generation speed expectations on a 3060.
- **Verdict:** is local viable for this use case, and what's the recommended model + workflow.

### R2 — Cheap cloud APIs with custom model choice
- **Output:** `b0ttsagent/temp/research-ai-imagegen/R2-cloud-apis.md`
- **Scope:** Cloud image-gen APIs (2026) where you can choose your own models (SDXL checkpoints, Flux, etc.), priced within $10–25/month for a hobbyist making maybe 100–500 images/month.
  - Compare: fal.ai, Replicate, Novita.ai, Segmind, RunPod (serverless), Tensor.Art API, Modal, DeepInfra, and any other notable "bring your own model" image APIs.
  - For each: pricing model (per-image cost for a typical SDXL/Flux schnell generation), minimum deposit / free credits, whether custom model upload (your own LoRA/checkpoint) is supported, API ergonomics, rate limits, commercial use of outputs per ToS.
  - Flag which platforms are pure "choose from hosted model catalog" vs "upload your own custom model".
  - Realistic monthly cost math: e.g., 300 generations at typical prices on the top 3 candidates.
- **Verdict:** top 2–3 recommendations for a $10–25/month hobbyist who wants model choice.

### R3 — Licensing, commercial use, and Roblox-specific angle
- **Output:** `b0ttsagent/temp/research-ai-imagegen/R3-licensing-roblox.md`
- **Scope:**
  - Commercial-use terms of the key models: SDXL base license, Flux schnell (Apache 2.0?) vs Flux dev (non-commercial restriction — exact terms), Pony v6, Illustrious XL, NoobAI, plus any 2025–2026 models from R1's findings.
  - Commercial-use terms of the key API platforms (from R2): who grants rights to generated outputs, any restrictions on selling/using in games.
  - Roblox-specific: Roblox's stance on AI-generated assets in games (ToS, IP guidelines, and whether AI-generated art is treated like user-generated content; any Roblox policy requiring disclosure or prohibiting AI content).
  - Copyright status of AI-generated images (US Copyright Office stance) — a one-paragraph practical summary, not a legal deep dive.
  - Practical risk level for using AI-generated icons in a published Roblox game, per model/platform.
- **Verdict:** which combos are safe to commercialize.

## Wave notes
- Researchers should use web tools (searxng, websearch, webfetch) and check the `opencode-web-research` skill if they are uncertain how to route their search.
- All files go in `b0ttsagent/temp/research-ai-imagegen/`.
- Lead researcher QA-checks each output against scope, then writes a compact WAVE-REPORT.md summary.
