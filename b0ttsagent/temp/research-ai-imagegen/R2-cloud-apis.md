# R2 — Cheap Cloud Image-Gen APIs with Custom Model Choice (2026)

Research wave: AI image generation for Roblox-style game icons.
Scope: cloud image-gen APIs where you can choose your own models (SDXL checkpoints, Flux, LoRAs), priced within $10–25/month for a hobbyist making ~100–500 images/month.
Research date: 2026-08-21. All prices/features verified against live web sources on 2026-08-21 unless marked "unverified" or "third-party".

User profile: cartoony/stylized (Roblox-like) tiered potion icons; RTX 3060 12GB local GPU; comfortable with technical setup; wants cheap options with model choice; commercial use assumed.

---

## 1. Executive summary

For a $10–25/month hobbyist who wants to pick their own models (SDXL checkpoints / Flux / LoRAs) and use outputs commercially, the realistic cost of 300 images/month is **$1–11 on every platform surveyed** — the budget is not the constraint; model choice, API ergonomics, and ToS are.

**Top 3 recommendations:**
1. **fal.ai** — best overall: per-image pricing (~$0.003 for FLUX.1 schnell, ~$0.0025 for SDXL), upload your own LoRAs, fast/reliable, commercial use OK, no minimum deposit, prepaid credits.
2. **Replicate** — easiest API + huge catalog; explicit commercial-use grant in ToS; one-line SDXL LoRA fine-tuning; prepaid credits. Caveat: deploying a *private custom model* bills dedicated hardware (idle included) — fine-tunes via "fast booting" bill only active time.
3. **DeepInfra** — cheapest per-image for schnell (~$0.002), supports Civitai LoRA adapters, zero data retention, commercial OK. Caveat: base models are catalog-only (no full checkpoint upload), no free credits.

Honorable mentions: **Modal** ($30/month free credit covers a hobbyist entirely; full bring-your-own-code control; needs Python), **RunPod serverless** (cheapest raw GPU; needs Docker/ComfyUI worker), **Tensor.Art TAMS API** (very cheap credits + custom model upload; API approval + China-hosted), **Novita.ai** (cheap + LoRA upload; China-hosted).

**Model-license caveat (matters for commercial use):** FLUX.1 [dev] and FLUX.2 [klein-9b] are **non-commercial** licenses. For commercial output use FLUX.1 [schnell] (Apache 2.0), FLUX.2 [klein-4b] (Apache 2.0), or SDXL (CreativeML Open RAIL-M). See §7.

---

## 2. Per-platform comparison

### 2.1 fal.ai
- **Pricing model:** Per-output (per image or per megapixel). FLUX.1 [schnell] = **$0.003 per megapixel**, billed rounding up to the nearest MP (so a 1024×1024 image ≈ $0.003). fast-sdxl ≈ **$0.0025 per inference** (typical 2.3 s). Some models use GPU-based pricing. Source: https://fal.ai/models/fal-ai/flux/schnell ; https://fal.ai/docs/examples/image-generation/fast-sdxl ; https://fal.ai/pricing
- **Minimum deposit / free credits:** Prepaid credits; no published minimum top-up (third-party guides suggest $5–10 to start). Purchased credits expire 365 days; free credits/coupons expire 1 week–1 year. Third-party trackers report a ~$20 signup credit (business email reportedly unlocks the larger grant); fal's own docs do not state a number. Sources: https://fal.ai/docs/documentation/model-apis/faq ; https://e8.team/resources/fal-ai/ (third-party) ; https://crepal.ai/blog/aivideo/hailuo-2-3-pro-image-to-video-fal/ (third-party)
- **Custom model upload:** Yes for LoRAs — dedicated LoRA endpoints (fal-ai/lora "Run Any Stable Diffusion model with customizable LoRA weights", fal-ai/flux-lora, fal-ai/flux-general with LoRA + ControlNet + IP-Adapter); upload weights via fal.storage. Full custom deployments via fal Serverless GPU fleet (H100 from $1.89/hr, committed). Sources: https://fal.ai/models/fal-ai/lora/api ; https://fal.ai/models/fal-ai/flux-general/api ; https://fal.ai/pricing
- **API ergonomics:** Clean REST + client SDKs (Python/JS), queue + async, webhooks. Concurrency limit starts at 2 concurrent requests, scales to 40 as you buy credits. Cold start not billed; only successful outputs billed. Source: https://fal.ai/docs/documentation/model-apis/faq
- **Rate limits:** Concurrency-based (2 → 40), not a hard RPM cap. Source: https://fal.ai/docs/documentation/model-apis/faq
- **Commercial use:** ToS (last updated 2026-07-31): customer owns Customer Input; fal does not claim IP rights in Output Content; commercial use permitted subject to model licenses. Source: https://fal.ai/legal/terms-of-service

### 2.2 Replicate
- **Pricing model:** Official models billed per output; community models billed per hardware-second. SDXL ≈ **$0.0037/run** (270 runs/$1); flux-schnell ≈ **$0.003/image**; flux-dev **$0.025/image**; flux-1.1-pro **$0.04/image**. Sources: https://replicate.com/stability-ai/sdxl ; https://replicate.com/pricing ; https://n8n.io/workflows/7192-generate-images-with-replicate-and-flux/ (third-party) ; https://huggingface.co/black-forest-labs/FLUX.1-schnell/discussions/154 (third-party)
- **Minimum deposit / free credits:** Prepaid credit since July 2025 (new accounts). No stated minimum purchase; auto-reload min threshold $5, min reload $15; credit valid 1 year, non-refundable. New accounts get a small intro credit (amount varies). Sources: https://replicate.com/docs/topics/billing/prepaid-credit ; https://replicate.com/changelog/2025-07-29-prepaid-credit
- **Custom model upload:** Yes — deploy your own models via Cog (Docker). Private models run on dedicated hardware and are billed while online (including idle); "fast booting fine-tunes" are billed only for active processing. One-line SDXL LoRA fine-tuning API. Sources: https://replicate.com/pricing ; https://replicate.com/blog/fine-tune-sdxl
- **API ergonomics:** Very mature — sync/async predictions, webhooks, SDKs, huge community catalog. No hard published RPM cap (queue-based). Source: https://replicate.com/docs/reference/how-does-replicate-work
- **Rate limits:** No hard published limit (unverified — not documented on pricing/docs pages reviewed).
- **Commercial use:** ToS §5.1 explicitly grants you all right/title/interest in Output, "including your use of Output for commercial purposes such as sale or publication, subject to any Third Party Terms" (model licenses). Source: https://replicate.com/terms

### 2.3 Novita.ai
- **Pricing model:** Per-model per-image on model detail pages. FLUX.1 Kontext Dev **$0.0225** ($0.018 fast mode), Pro **$0.036**, Max **$0.072** (Novita blog, 2026-06-26). Qwen-Image **$0.02/image** (2025-08). SDXL exact price: **unverified** — third-party cites "from $0.01/image for SD1.5". Sources: https://blogs.novita.ai/flux-1-kontext-pro-max-dev-on-novita-ai-guide/ ; https://blogs.novita.ai/qwen-image-on-novita/ ; https://devtoollab.com/ai-tools/novita-ai (third-party)
- **Minimum deposit / free credits:** Baseline signup voucher ~**$0.50**; promotional campaigns sometimes $10 (sources conflict — third-party). No card required to sign up. Sources: https://pricepertoken.com/endpoints/novita/free (third-party) ; https://aicreditmart.com/ai-credits-providers/how-to-get-10-in-free-novita-ai-credits-2026-guide/ (third-party)
- **Custom model upload:** Yes — upload your own LoRA (currently free, limit 5 uploads/user). Source: https://novita.ai/docs/guides/model-apis-custom-model
- **API ergonomics:** Async REST (task_id + poll), OpenAI-compatible LLM endpoints, LoRA + ControlNet + IP-Adapter support. Rate limit ~60 RPM default, per-modality caps ~10–20 images/min (third-party). Source: https://novita.ai/docs/api-reference/model-apis-txt2img ; https://pricepertoken.com/endpoints/novita/free (third-party)
- **Commercial use:** ToS retains your rights in Input; AUP permits "personal, internal business, or permitted commercial use." Sources: https://novita.ai/legal/terms-of-service ; https://novita.ai/legal/acceptable-use-policy

### 2.4 Segmind
- **Pricing model:** Pay-as-you-go credits; serverless billed **per GPU-second per model**. SDXL (sdxl-torch) = **$0.0072/GPU-sec**, ~5 s latency → ≈ **$0.036/image** (expensive vs per-image rivals). Dedicated endpoints from $0.00024–$0.0031/GPU-sec. Sources: https://www.segmind.com/models/sdxl-torch/pricing ; https://segmind.com/pricing
- **Minimum deposit / free credits:** Flexible plan "Get started with $10"; Pro $39/mo ($50 credits); Business $99/mo. 60 RPM on flexible. Fine-tuning requires min $10 balance. Source: https://segmind.com/pricing
- **Custom model upload:** Yes — import LoRA from Hugging Face or direct file upload (.safetensors/.sft/.ckpt) for FLUX dev/schnell, SDXL, SD2.1, SD1.5; also Flux LoRA fine-tuning (A100/H100/L40S). Sources: https://docs.segmind.com/model-hub ; https://docs.segmind.com/readme/flux-fine-tuning
- **API ergonomics:** REST + Python SDK, sync/async, model catalogue with per-run cost estimates. Source: https://docs.segmind.com/docs/get-started/models
- **Rate limits:** 60 RPM (flexible) → 120/500/1000 on paid tiers. Source: https://segmind.com/pricing
- **Commercial use:** ToS §2.4.1 — you retain ownership of Customer Content; Segmind FAQ confirms API images can be used commercially (subject to model policies). Sources: https://www.segmind.com/terms ; https://www.segmind.com/models/imagen-4-fast

### 2.5 RunPod (serverless)
- **Pricing model:** Per-second GPU billing (worker start → stop). Serverless rates: A4000/A4500/RTX4000 (16GB) **$0.58/hr**; L4/A5000/3090/MIG24 **$0.69/hr**; 4090 **$1.10/hr**; A100 **$2.72/hr**; L40/L40S/6000Ada **$1.75/hr**. At ~10–15 s per SDXL image on L4 → ≈ **$0.002–0.003/image** (plus cold-start/idle overhead). Source: https://www.runpod.io/pricing
- **Minimum deposit / free credits:** Min deposit **$10**; credits non-refundable; official FAQ says no trial credits. A third-party site claims a $5–$500 new-user bonus after first $10 spend — **unverified** (RunPod's own FAQ contradicts "trial credits"). Sources: https://docs.runpod.io/accounts-billing/billing ; https://github.com/runpod/docs/blob/6e244ab3/docs/references/faq/faq.md ; https://aicreditmart.com/ai-credits-providers/how-to-get-5-500-in-runpod-free-credits-for-new-users-2026/ (third-party, unverified)
- **Custom model upload:** Full bring-your-own-container (any Docker image / ComfyUI worker); official SDXL worker template. Source: https://github.com/runpod-workers/worker-sdxl
- **API ergonomics:** Endpoint-based; you build the worker (technical). Autoscaling, FlashBoot cold starts. No rate limit (autoscale). Source: https://docs.runpod.io/serverless/pricing
- **Commercial use:** Compute provider — no content-generation IP claims; model licenses govern. (Inference; not explicitly re-verified in ToS this pass.)

### 2.6 Tensor.Art (TAMS API)
- **Pricing model:** Credit-based; **$0.003/credit**. SD/SDXL model factor = 1, FLUX = 2. Typical SDXL 1024²/25-step ≈ 1 credit ≈ **$0.003/image**; FLUX ≈ 2 credits ≈ **$0.006/image**. Formula: MODEL_FACTOR × COUNT × (CEIL(STEPS/5)/5). Source: https://tams-docs.tensor.art/docs/use-cases/intro-to-billing/
- **Minimum deposit / free credits:** 1,000 free credits on first login (≈ $3). Credit packs: 10k credits, 100k, 1M, 10M (gift credits scale with purchase). Source: https://tams-docs.tensor.art/docs/use-cases/intro-to-billing/
- **Custom model upload:** Yes — upload models via the Tensor.Art model page; private models/LoRAs/embeddings usable in the API via an `accessKey`. Note: the "self-selected Models / AI Tools list" feature requires the 1M-credit purchase tier. Sources: https://tams-docs.tensor.art/docs/use-cases/model/private-model/ ; https://tams-docs.tensor.art/docs/api/guide/integration-faq/
- **API ergonomics:** Workspace API (SD WebUI-like) + Workflow API (ComfyUI-like); SDKs (JS/Python). API requires app creation/approval. Rate limits: **unknown** (not documented in pages reviewed).
- **Commercial use:** Web ToS: free tier is personal-use only; commercial use requires a paid subscription (Basic $5/mo+, Pro ~$9.90/mo with 300 daily credits). Third-party reviews consistently confirm this. Sources: https://tensor.art/about/terms-of-service-new ; https://tensor.art/about/terms-of-vip-membership ; https://www.tooljunction.io/ai-tools/tensor-art (third-party)

### 2.7 Modal
- **Pricing model:** Per-second GPU/CPU/memory. GPU: T4 **$0.000164/s**, L4 **$0.000222/s**, A10 **$0.000306/s**, L40S **$0.000542/s**, A100 80GB **$0.000694/s**, H100 **$0.001097/s**. SDXL on A10 (~8 s) ≈ **$0.0024/image**; FLUX schnell ≈ **$0.0012/image**. Source: https://modal.com/pricing
- **Minimum deposit / free credits:** Starter plan **$0 + $30/month free compute credit**; no minimum deposit; pay-as-you-go. Source: https://modal.com/pricing
- **Custom model upload:** Full bring-your-own-code/container (Python functions; any model incl. fine-tuned LoRA stacks). Sources: https://modal.com/blog/how-to-run-stable-diffusion-xl-on-modal ; https://modal.com/blog/how-to-run-flux1-dev-on-modal
- **API ergonomics:** Python-first; you write the serving code (technical). Autoscaling, scale-to-zero; cold start billed unless keep_warm. No rate limit (autoscale).
- **Commercial use:** Compute provider — no content-generation IP claims; model licenses govern. (Inference; not explicitly re-verified in ToS this pass.)

### 2.8 DeepInfra
- **Pricing model:** Per-image. FLUX-1-schnell **$0.0005 × (w/1024) × (h/1024) × iters** (≈ **$0.002** at 1024²/4 steps); FLUX-2-klein-4b **$0.014**; FLUX-1-dev **$0.009 × (w/1024) × (h/1024) × (iters/25)**; SDXL-turbo **$0.0002 × (w/1024) × (h/1024) × (iters/5)**. Sources: https://deepinfra.com/flux ; https://deepinfra.com/models/text-to-image/2
- **Minimum deposit / free credits:** Pay-as-you-go; must add a card or pre-pay; invoicing tiers (Tier 1 threshold $20). No documented free signup credit. Source: https://deepinfra.com/pricing
- **Custom model upload:** Partial — deploy **LoRA image adapters from Civitai** (public models only) on supported base models; no full checkpoint upload. Sources: https://docs.deepinfra.com/private-models/lora-image ; https://docs.deepinfra.com/private-models/overview
- **API ergonomics:** OpenAI-compatible images API; simple. Rate limits: **unknown** (not documented in pages reviewed).
- **Commercial use:** ToS — customer retains IP in Customer Data; zero data retention; no training on your data; commercial use broadly allowed (prohibits competitive use of the service itself). Sources: https://deepinfra.com/terms ; https://docs.deepinfra.com/account/data-privacy

### 2.9 Other notable platforms
- **SiliconFlow** (China): FLUX.1-schnell **$0.0014/image** (cheapest found), FLUX.1-dev $0.014, Qwen-Image $0.02. OpenAI-compatible. Caveats: China-hosted (data-residency), custom-model support unclear (unverified). Source: https://www.siliconflow.com/models/image
- **Civitai API** (Orchestration): generate with any community model incl. your own uploads; paid in Buzz (SDXL ≈ 4–6 Buzz/image; memberships $5–$50/mo). Buzz-dollar value is opaque. Sources: https://developer.civitai.com/orchestration/guide/submitting-work ; https://civitai.com/articles/4797/generating-now-costs-buzz-why ; https://apis.io/plans/civitai/civitai-plans-pricing/
- **Banana.dev**: **shut down March 31, 2024** — do not consider. Source: https://www.banana.dev/blog/sunset

---

## 3. "Hosted catalog" vs "upload your own custom model"

| Platform | Type | Custom model support |
|---|---|---|
| fal.ai | Hybrid | LoRA upload via storage + LoRA endpoints; full custom deploys via Serverless GPU fleet |
| Replicate | Hybrid | Deploy via Cog (Docker); private models on dedicated hardware; one-line LoRA fine-tune |
| Novita.ai | Hybrid | LoRA upload (5 max, currently free) |
| Segmind | Hybrid | LoRA import (HF or file upload); Flux LoRA fine-tuning |
| RunPod serverless | **Bring-your-own** | Any Docker/ComfyUI container |
| Modal | **Bring-your-own** | Any code/container |
| Tensor.Art TAMS | Hybrid | Upload models; private models via accessKey |
| DeepInfra | Mostly catalog | Civitai LoRA adapters only (no full checkpoints) |
| SiliconFlow | Catalog | Custom model support unverified |
| Civitai API | Hybrid | Any community model incl. your uploads |

---

## 4. Realistic monthly cost math (300 generations, 1024×1024)

| Platform | Model | Per image | 300 images/mo |
|---|---|---|---|
| fal.ai | FLUX.1 schnell | $0.003 | **$0.90** |
| fal.ai | fast-sdxl | ~$0.0025 | **$0.75** |
| Replicate | flux-schnell | $0.003 | **$0.90** |
| Replicate | SDXL | $0.0037 | **$1.11** |
| Replicate | flux-dev | $0.025 | **$7.50** |
| DeepInfra | FLUX-1-schnell | ~$0.002 | **$0.60** |
| DeepInfra | FLUX-2-klein-4b | $0.014 | **$4.20** |
| Novita.ai | FLUX.1 Kontext Dev | $0.0225 | **$6.75** |
| Novita.ai | SDXL | ~$0.004–0.01 (unverified) | **$1.20–3.00** |
| Segmind | SDXL (serverless) | ~$0.036 | **$10.80** |
| RunPod serverless | SDXL on L4 | ~$0.002–0.003 (+overhead) | **$0.60–0.90** |
| Modal | SDXL on A10 | ~$0.0024 | **$0.72** (covered by $30 credit) |
| Tensor.Art TAMS | SDXL | ~$0.003 | **$0.90** |
| SiliconFlow | FLUX.1 schnell | $0.0014 | **$0.42** |

Even at 500 images/month, every platform stays well under $25. The budget is not the binding constraint.

---

## 5. Verdict (for a $10–25/mo hobbyist wanting model choice + commercial use)

1. **fal.ai** — Top pick. Per-image pricing (~$0.003 schnell / ~$0.0025 SDXL), upload your own LoRAs, fast and reliable, commercial use OK, no minimum deposit, prepaid credits, concurrency scales with spend. 300 images ≈ **$1–3/mo**.
2. **Replicate** — Best ergonomics + explicit commercial-use grant in ToS; one-line SDXL LoRA fine-tuning; huge catalog. 300 schnell images ≈ **$0.90/mo**. Caveat: private custom-model deploys bill dedicated hardware (idle included) — stick to hosted models + fast-booting fine-tunes.
3. **DeepInfra** — Cheapest per-image for schnell (~$0.002), Civitai LoRA adapters, zero data retention, commercial OK. Caveat: catalog-only base models, no free credits.

**If you want maximum model control and don't mind code:** **Modal** (free $30/mo credit covers a hobbyist entirely; bring your own container) or **RunPod serverless** (cheapest raw GPU; bring your own Docker/ComfyUI worker; $10 min deposit).

**Budget wildcard:** **Tensor.Art TAMS** (≈$0.003–0.006/image, custom model upload via accessKey, 1k free credits) — but API approval + China-hosted + free-tier commercial restrictions on the web platform.

**Note for this user:** with an RTX 3060 12GB you can already run SDXL locally for free; cloud APIs are for scale, batch, or when you want hosted Flux. For commercial output, prefer FLUX.1 schnell / FLUX.2 klein-4b / SDXL (permissive licenses) over FLUX.1 dev / FLUX.2 klein-9b (non-commercial).

---

## 6. Sources (all accessed 2026-08-21)

- fal.ai pricing: https://fal.ai/pricing ; schnell: https://fal.ai/models/fal-ai/flux/schnell ; fast-sdxl: https://fal.ai/docs/examples/image-generation/fast-sdxl ; FAQ/billing: https://fal.ai/docs/documentation/model-apis/faq ; LoRA: https://fal.ai/models/fal-ai/lora/api ; flux-general: https://fal.ai/models/fal-ai/flux-general/api ; ToS: https://fal.ai/legal/terms-of-service
- Replicate pricing: https://replicate.com/pricing ; SDXL: https://replicate.com/stability-ai/sdxl ; prepaid credit: https://replicate.com/docs/topics/billing/prepaid-credit ; changelog: https://replicate.com/changelog/2025-07-29-prepaid-credit ; fine-tune: https://replicate.com/blog/fine-tune-sdxl ; ToS: https://replicate.com/terms ; how it works: https://replicate.com/docs/reference/how-does-replicate-work
- Novita: pricing page https://novita.ai/pricing ; Kontext blog: https://blogs.novita.ai/flux-1-kontext-pro-max-dev-on-novita-ai-guide/ ; Qwen blog: https://blogs.novita.ai/qwen-image-on-novita/ ; LoRA upload: https://novita.ai/docs/guides/model-apis-custom-model ; txt2img API: https://novita.ai/docs/api-reference/model-apis-txt2img ; ToS: https://novita.ai/legal/terms-of-service ; AUP: https://novita.ai/legal/acceptable-use-policy
- Segmind: pricing: https://segmind.com/pricing ; sdxl-torch: https://www.segmind.com/models/sdxl-torch/pricing ; model hub: https://docs.segmind.com/model-hub ; fine-tuning: https://docs.segmind.com/readme/flux-fine-tuning ; ToS: https://www.segmind.com/terms ; Imagen FAQ: https://www.segmind.com/models/imagen-4-fast
- RunPod: pricing: https://www.runpod.io/pricing ; serverless billing: https://docs.runpod.io/serverless/pricing ; billing/credits: https://docs.runpod.io/accounts-billing/billing ; FAQ: https://github.com/runpod/docs/blob/6e244ab3/docs/references/faq/faq.md ; SDXL worker: https://github.com/runpod-workers/worker-sdxl
- Tensor.Art TAMS: billing: https://tams-docs.tensor.art/docs/use-cases/intro-to-billing/ ; private model: https://tams-docs.tensor.art/docs/use-cases/model/private-model/ ; FAQ: https://tams-docs.tensor.art/docs/api/guide/integration-faq/ ; ToS: https://tensor.art/about/terms-of-service-new ; membership: https://tensor.art/about/terms-of-vip-membership
- Modal: pricing: https://modal.com/pricing ; SDXL guide: https://modal.com/blog/how-to-run-stable-diffusion-xl-on-modal ; Flux guide: https://modal.com/blog/how-to-run-flux1-dev-on-modal
- DeepInfra: flux: https://deepinfra.com/flux ; models: https://deepinfra.com/models/text-to-image/2 ; pricing: https://deepinfra.com/pricing ; LoRA image: https://docs.deepinfra.com/private-models/lora-image ; ToS: https://deepinfra.com/terms ; data privacy: https://docs.deepinfra.com/account/data-privacy
- SiliconFlow: https://www.siliconflow.com/models/image
- Civitai: https://developer.civitai.com/orchestration/guide/submitting-work ; https://civitai.com/articles/4797/generating-now-costs-buzz-why ; https://apis.io/plans/civitai/civitai-plans-pricing/
- Banana.dev sunset: https://www.banana.dev/blog/sunset

## 7. Unverified / conflicting claims flagged
- fal.ai signup credit amount (~$20) — third-party trackers only; fal docs don't state a number.
- Novita free-credit amount ($0.50 baseline vs $10 promo) — third-party sources conflict.
- Novita SDXL per-image price — not found on a primary page; third-party cites "from $0.01 (SD1.5)".
- Novita rate limits (~60 RPM, 10–20 images/min) — third-party.
- RunPod $5–$500 new-user bonus — third-party; RunPod's own FAQ says no trial credits.
- Replicate / DeepInfra / Tensor.Art API rate limits — not published in pages reviewed.
- SiliconFlow custom-model support — unverified.
