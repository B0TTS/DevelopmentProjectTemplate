# Wave Report — AI Image Generation for Roblox Game Icons

**Date:** 2026-08-21
**Wave lead QA:** All 3 outputs verified on disk against scope — every bullet addressed, pricing/licensing cited to live sources (accessed 2026-08-21), unverifiable claims flagged, verdicts present. No re-runs required.

## Researcher status

| ID | Scope | Output file | Status | Verdict |
|---|---|---|---|---|
| R1 | Local ComfyUI/SD path (RTX 3060, $0) | `R1-local-comfyui.md` | done | VIABLE — recommended: SDXL/Illustrious + icon/Roblox LoRAs, or FLUX.2 klein 4B |
| R2 | Cheap BYO-model cloud APIs ($10–25/mo) | `R2-cloud-apis.md` | done | Top 3: fal.ai, Replicate, DeepInfra — budget never the constraint |
| R3 | Licensing / commercial use / Roblox | `R3-licensing-roblox.md` | done | Safe combos: Illustrious/SDXL local + Qwen-Image or FLUX dev via API |

## Top findings per scope

### R1 — Local path (cost $0)
- **Models:** SDXL 1.0 + game-icon LoRA (Game Icon Forge, Zavy's Fantasy Icons) + Roblox/chibi style LoRA (Roblox Chibi Doll, Roblox-ify Anything) delivers the bold/rounded catalog look. **FLUX.2 klein 4B (Apache 2.0, fits 12GB, native multi-reference editing) is the standout 2026 option.** Avoid for commercial: NoobAI (murky license), Pony V6 (commercial inference banned), FLUX.1/2 dev + klein 9B (non-commercial).
- **Frontend:** ComfyUI wins for batch + consistency + LayerDiffuse/IP-Adapter + VRAM efficiency (~5.5GB SDXL). Forge for a form UI; A1111 stalled — skip.
- **Transparency:** LayerDiffuse = native RGBA on SDXL; else flat-bg + rembg (free, MIT). "SDXL ICONS base model" could not be verified — closest equivalents documented.
- **Tiered potions:** fixed seed + prompt template → img2img recolor (low denoise) → small LoRA or canny ControlNet if shape drifts; Klein 4B does it in one model.
- **Speed:** SDXL 1024² ≈ 11–22s/img (8.5–9.8GB); Flux schnell ~13–18s; Flux dev ~60–95s. 32GB RAM + NVMe recommended.

### R2 — Cloud APIs (300 images/mo, 1024²)
- **fal.ai** — FLUX.1 schnell $0.003/img, SDXL ~$0.0025; LoRA upload; no min deposit; commercial OK → **~$0.90/mo**
- **Replicate** — schnell $0.003, SDXL $0.0037, flux-dev $0.025; explicit commercial grant in ToS; one-line SDXL LoRA fine-tune; prepaid credits → **~$0.90–7.50/mo**
- **DeepInfra** — schnell ~$0.002 (cheapest), Civitai LoRA adapters, zero data retention; catalog-only base models → **~$0.60/mo**
- **Modal** — $30/mo free credit covers a hobbyist; full BYO-code → ~$0. **RunPod serverless** — ~$0.002–0.003/img on L4; $10 min deposit; needs Docker/ComfyUI.
- Others: Novita (LoRA upload, ~$6.75 Kontext Dev), Segmind (SDXL ~$0.036/img — priciest), Tensor.Art TAMS (~$0.003/img, custom models via accessKey), SiliconFlow ($0.0014 schnell, China-hosted).
- **Verdict:** Top 3 = **fal.ai** (best overall), **Replicate** (easiest + commercial grant), **DeepInfra** (cheapest). Budget is never the constraint — model choice/ToS are.

### R3 — Licensing / Roblox
- **Safest local:** Illustrious XL v1.x/v2.0 & SDXL (Open RAIL++-M/RAIL-M, commercial OK), FLUX.2 klein 4B (Apache 2.0), FLUX.1 schnell (Apache 2.0), Z-Image-Turbo (Apache 2.0), SD 3.5 (free under $1M revenue).
- **Safest API:** Qwen-Image via fal/Replicate/Novita/Segmind (Apache 2.0, ~$0.02/img on Novita); FLUX.1/2 dev via BFL API or licensed providers (outputs commercial OK).
- **Avoid:** NoobAI XL (explicit commercial prohibition). **Conditional:** Pony v6 (license conflict); self-hosted FLUX dev (outputs OK, but self-hosting commercially needs BFL license).
- **Roblox:** AI-generated assets allowed and treated as UGC; no disclosure required for static icons (only interactive AI features trigger Content Maturity disclosure); you must own rights to content; don't strip provenance metadata.
- **USCO:** Purely AI-generated images aren't copyrightable (human authorship required); human edits/arrangement are protectable.
- **Verdict:** Illustrious XL/SDXL locally + Qwen-Image or FLUX dev via API are the safe-to-commercialize combos; modify outputs and avoid brand/IP prompts.

## Anomalies / notes
- SearXNG returned no organic results all session (all 3 researchers fell back to Exa `websearch` per the opencode-web-research skill routing). No impact on coverage.
- Unverified items flagged in files: fal/Novita free-credit amounts, Novita SDXL price & rate limits, RunPod $5–500 bonus, several API rate limits, Pony v6 FAQ (404), Illustrious v2.0 license variant (RAIL vs RAIL-M) conflict, FLUX.2 klein 4B speed on 3060.
- Banana.dev confirmed shut down (Mar 2024) — excluded.

## Next actions (for orchestrator)
1. Recommend primary path: **local ComfyUI + SDXL/Illustrious + icon/Roblox LoRAs** (free, full model control, commercial-safe) with FLUX.2 klein 4B as the 2026 upgrade for tiered-potion consistency.
2. Cloud fallback/scale: **fal.ai** (or Replicate for ease) — ~$1–3/mo at hobbyist volume, well under the $10–25 budget.
3. Commercial green-light: Illustrious/SDXL local + Qwen-Image or FLUX dev via API; avoid NoobAI; treat Pony v6 and self-hosted FLUX dev as conditional.
