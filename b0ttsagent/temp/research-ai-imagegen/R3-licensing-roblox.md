# R3 — Licensing, Commercial Use & Roblox Angle for AI-Generated Game Icons

**Research wave:** AI image generation for Roblox-style game icons (cartoony/stylized tiered potion icons)
**Researcher:** leaf subagent (R3 scope)
**Date of research / access dates for all citations:** 2026-08-21
**User profile kept in mind:** cartoony/stylized (Roblox-like) tiered potion icons; RTX 3060 12GB; comfortable with technical setup; wants cheap options that allow choosing their own models; commercial use assumed needed.

> **Disclaimer:** This is a practical research summary, not legal advice. License/ToS text changes over time; verify against the linked primary sources before relying on any single claim. Claims I could not verify against a live source are explicitly marked **unverified**.

---

## 1. Per-model commercial-use terms

### 1.1 SDXL 1.0 base (Stability AI) — **SAFE for commercial use**
- **License:** CreativeML Open RAIL++-M, dated July 26, 2023.
- **Terms:** Permits commercial use, modification, fine-tuning, and redistribution. Use-based restrictions in Attachment A (no illegal/harmful uses, no generating certain content categories). Outputs clause: *"The Output You Generate. Except as set forth herein, Licensor claims no rights in the Output You generate using the Model."* — i.e., outputs are yours.
- **Sources:** https://github.com/Stability-AI/generative-models/blob/main/model_licenses/LICENSE-SDXL1.0 (accessed 2026-08-21); community analysis: https://www.ai-image-journey.com/2025/10/sdxl-license.html (accessed 2026-08-21).
- **Hardware note:** SDXL runs comfortably on 12GB VRAM (practical estimate, not a license claim).

### 1.2 FLUX.1 schnell (Black Forest Labs) — **SAFE for commercial use**
- **License:** Apache 2.0. Full commercial use, modification, distribution; no revenue caps, no fees, no usage tracking.
- **Sources:** HF model card https://huggingface.co/black-forest-labs/FLUX.1-schnell ("Released under the apache-2.0 licence, the model can be used for personal, scientific, and commercial purposes"); license file https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-schnell (both accessed 2026-08-21).
- **Hardware note:** 12B params; runs on 12GB VRAM with fp8/quantization (practical estimate).

### 1.3 FLUX.1 dev (Black Forest Labs) — **CONDITIONAL: outputs commercial OK; self-hosting the model commercially requires a BFL license**
- **License:** FLUX.1 [dev] Non-Commercial License v1.1.1 (current text; v2.0 "FLUX [dev] Non-Commercial License" now covers FLUX.2 dev too).
- **Key nuance — outputs vs model:** The license restricts *use of the model* to non-commercial purposes, but explicitly states **Outputs are not Derivatives** and: *"We claim no ownership rights in and to the Outputs… You may use Output for any purpose (including for commercial purposes), except as expressly prohibited herein."* So **images you generate with dev can be used commercially**, even though you may not self-host/serve the dev model for commercial purposes without a BFL commercial license.
- **Practical paths to commercial use of dev outputs:** (a) generate via the BFL API (commercial rights included in per-image price), or (b) generate via a licensed provider (fal.ai, Replicate, DeepInfra, etc. hold commercial agreements with BFL), or (c) self-host for non-commercial use only. Self-hosting dev weights for a commercial product requires a BFL commercial license (https://bfl.ai/pricing/licensing).
- **Sources:** https://bfl.ai/legal/non-commercial-license-terms (accessed 2026-08-21); https://github.com/black-forest-labs/flux/blob/main/model_licenses/LICENSE-FLUX1-dev (accessed 2026-08-21); BFL helpdesk https://help.bfl.ai/articles/4375863104-can-i-use-the-api-for-a-commercial-application (accessed 2026-08-21); HF discussion confirming outputs-commercial interpretation https://huggingface.co/black-forest-labs/FLUX.1-dev/discussions/7 (accessed 2026-08-21).

### 1.4 FLUX.2 family (Black Forest Labs, Nov 2025) — **klein 4B SAFE; dev / klein 9B CONDITIONAL (same as dev)**
- **FLUX.2 [klein] 4B:** Apache 2.0 — full commercial use, no fees/approvals. Runs in ~8GB VRAM (RTX 3090/4070+; fits an RTX 3060 12GB). **Highly relevant to this user.**
- **FLUX.2 [klein] 9B / FLUX.2 [dev] (32B):** FLUX Non-Commercial License (renamed from "FLUX.1 [dev] Non-Commercial License"; no material changes). Same outputs-commercial / model-non-commercial structure as 1.3. Commercial local use requires a BFL license; commercial rights included via BFL API.
- **Sources:** https://github.com/black-forest-labs/flux2 (accessed 2026-08-21); https://help.bfl.ai/articles/7108141705-can-i-run-or-fine-tune-flux-2-klein-locally (accessed 2026-08-21); https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence (accessed 2026-08-21).

### 1.5 Pony Diffusion V6 XL (AstraliteHeart / PurpleSmartAI) — **CONDITIONAL / MODERATE RISK (license conflict)**
- **Conflict to report:** The official site FAQ (ponydiffusion.com/faq) previously stated *"Pony Diffusion is available under the CreativeML OpenRAIL-M license, permitting commercial use and redistribution"* — but that page now returns 404 (checked 2026-08-21), so I could not re-verify it live. The **actual model card** on Civitai/HF/Tensor.Art says the model is licensed under a **modified Fair AI Public License 1.0-SD** with this addendum: *"You are not permitted to run inference of this model on websites or applications allowing any form of monetization (paid inference, faster tiers, etc.). This applies to any derivative models or model merges. If you want to use this model commercially, please reach us at contact@purplesmart.ai."*
- **Practical reading:** The restriction targets **monetized inference platforms** (paid APIs/websites), not the use of locally generated outputs. Local generation + commercial use of outputs is generally treated as acceptable by the community, but the license is murky and the official FAQ is offline. **Avoid running Pony v6 on paid inference platforms; if you want certainty for commercial output use, contact PurpleSmartAI.**
- **Sources:** https://civitai.com/models/257749 (accessed 2026-08-21); https://huggingface.co/AKEOR/Pony_Diffusion_V6_XL (accessed 2026-08-21); https://tensor.art/models/714585990280309972 (accessed 2026-08-21); ponydiffusion.com/faq (404 on access, cited from search snippet only — treat as unverified).

### 1.6 Illustrious XL (Onoma AI) — **SAFE for commercial use**
- **v1.0 / v1.1:** CreativeML Open RAIL++-M (commercial use permitted).
- **v2.0:** CreativeML Open RAIL-M (commercial use permitted; note this older variant retains a remote-update clause giving the licensor rights to modify derivatives/outputs — practically unenforced, but worth knowing).
- **Sources:** https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0 (license tag `creativeml-openrail-m`; discussion https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0/discussions/4 accessed 2026-08-21); https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0/discussions/1 (accessed 2026-08-21); https://www.ai-image-journey.com/2025/10/sdxl-license.html (accessed 2026-08-21).
- **Hardware note:** SDXL-based; runs on 12GB VRAM.

### 1.7 NoobAI XL (Laxhar Dream Lab) — **AVOID for commercial use (explicit prohibition)**
- **License:** inherits FAIPL 1.0-SD from Illustrious-xl-early-release-v0 **plus an added "Commercial Prohibition"**: *"We prohibit any form of commercialization, including but not limited to monetization or commercial use of the model, derivative models, or model-generated products."*
- **Note:** A community analysis argues this added restriction conflicts with the underlying FAIPL/RAIL licenses and may be unenforceable (https://civitai.com/articles/18619/what-the-license, accessed 2026-08-21). That is a legal argument, not settled law. **Practically: NoobAI's own license text prohibits commercial use of model-generated products, so treat it as not safe for a published commercial game.**
- **Sources:** https://huggingface.co/Laxhar/noobai-XL-1.0 (accessed 2026-08-21); https://civitai.com/models/833294 (accessed 2026-08-21).

### 1.8 2025–2026 models relevant to stylized/cartoon icon generation

| Model | Released | License | Commercial use | Local on 12GB? |
|---|---|---|---|---|
| **Qwen-Image** (Alibaba, 20B) | Aug 2025 | Apache 2.0 | ✅ Full | ❌ Too big (~24GB+); use via API (fal/Replicate/Novita/Segmind) |
| **Z-Image / Z-Image-Turbo** (Alibaba, 6B) | Nov 2025 | Apache 2.0 | ✅ Full, no revenue cap | ⚠️ Turbo claims <16GB VRAM (vendor claim); tight/quantized on 12GB |
| **FLUX.2 [klein] 4B** (BFL) | Jan 2026 | Apache 2.0 | ✅ Full | ✅ ~8GB VRAM |
| **SD 3.5 Large/Medium** (Stability) | Oct 2024 | Stability AI Community License | ✅ Free commercial under $1M annual revenue; Enterprise license above $1M; must register for commercial use | ⚠️ Large is 8B — runs on 12GB quantized |
| **Nano Banana / Gemini image models** (Google) | 2025–2026 | Hosted API only (Gemini API terms) | ✅ Commercial via paid API; "Google won't claim ownership over that content"; SynthID watermark on all outputs | ❌ API-only, not local |

- **Sources:** Qwen-Image: https://github.com/QwenLM/Qwen-Image/blob/main/LICENSE + https://huggingface.co/Qwen/Qwen-Image (accessed 2026-08-21). Z-Image: https://github.com/Tongyi-MAI/Z-Image (Apache 2.0) + https://howaiworks.ai/models/z-image (accessed 2026-08-21). FLUX.2 klein: https://github.com/black-forest-labs/flux2 (accessed 2026-08-21). SD 3.5: https://stability.ai/license + https://huggingface.co/stabilityai/stable-diffusion-3.5-large/blob/main/LICENSE.md (accessed 2026-08-21). Nano Banana/Gemini: https://ai.google.dev/gemini-api/terms ("Google won't claim ownership over that content") + https://ai.google.dev/gemini-api/docs/image-generation (accessed 2026-08-21).

---

## 2. Per-platform commercial-use terms (who grants rights to outputs)

**Key pattern:** Every platform reviewed lets you use generated outputs commercially and does not claim ownership of them. The binding constraint is almost always the **underlying model's license**, not the platform ToS. Platforms that host FLUX dev models (fal, Replicate, DeepInfra) hold commercial agreements with BFL, so dev outputs via those APIs are commercially usable.

| Platform | Output ownership / grant | Commercial use of outputs | Notes / source (all accessed 2026-08-21) |
|---|---|---|---|
| **fal.ai** | Customer owns Customer Input; fal does not claim IP in Output Content (ToS §4(c) disclaimer). No explicit output-assignment clause found (unlike Replicate). | ✅ Permitted; model pages state "suitable for personal and commercial use" (e.g., FLUX.1 dev page). | https://fal.ai/legal/terms-of-service (read in full); https://fal.ai/models/fal-ai/flux/dev |
| **Replicate** | **Explicit grant:** "Replicate hereby grants to you all right, title and interest, if any, in and to Output, including your use of Output for commercial purposes such as sale or publication, subject to any Third Party Terms (as determined by the Models you use to generate the Output)." | ✅ Permitted, subject to the model's license. | https://replicate.com/terms (§5.1) |
| **Novita.ai** | You retain rights in Input; you grant Novita a license to process Input/Output to provide the service. No explicit output-assignment clause found in the fetched portion (**unverified** whether one exists elsewhere in the ToS). | ✅ Permitted ("permitted commercial use" per AUP). | https://novita.ai/legal/terms-of-service; https://novita.ai/legal/acceptable-use-policy |
| **Segmind** | "As between you and Segmind, you retain all ownership or license rights in Customer Content" — Customer Content includes Customer Results (outputs). | ✅ Permitted; model pages confirm "Images generated via the Segmind API can be used commercially." | https://www.segmind.com/terms; https://www.segmind.com/models/sd1.5-outpaint |
| **RunPod** | "We do not assert any ownership over Your Content. You retain full ownership." Raw GPU cloud — you bring your own models/weights. | ✅ Permitted; model license governs. | https://www.runpod.io/legal/terms-of-service |
| **Tensor.Art** | ToS §3.1: "No claims on the ownership or copyright of models and AI-generated images are made by Tensor.Art, and all created content may be freely used by yourself." §3.9: subscribed AI tools must use commercially-available models; author bears consequences if not. | ✅ Permitted, subject to model license. | https://tensor.art/about/terms-of-service-new |
| **Modal** | "Input and Output shall be considered Customer Data"; "Customer shall retain all right, title and interest in and to the Customer Data." Compute platform — you bring your own models. | ✅ Permitted; model license governs. | https://modal.com/legal/terms |
| **DeepInfra** | "Customer retains all intellectual property rights in and to such Customer Data" (includes generated outputs); zero data retention; no training on your data. | ✅ Permitted; model license governs (e.g., FLUX dev models: outputs commercial OK per BFL license). | https://deepinfra.com/terms; https://docs.deepinfra.com/account/data-privacy |

**Cross-cutting caveats (all platforms):** outputs may not be unique (others can generate the same/similar image); platforms disclaim warranties that outputs are original or non-infringing; you bear the risk if an output resembles a third party's copyrighted work; most ToS prohibit using outputs to train competing models.

---

## 3. Roblox-specific: stance on AI-generated assets

**Bottom line: Roblox does NOT prohibit AI-generated assets in games, and does NOT require disclosure for static AI-generated assets (like icons).** AI-generated content is treated as user-generated content (UGC) for which the creator is responsible.

Verified points (all accessed 2026-08-21):

1. **AI-generated content is allowed and treated as UGC.** Roblox's "Games with Generative AI" documentation: *"all content, including content created by or using generative AI, must adhere to Roblox's Community Standards."* Source: https://create.roblox.com/docs/generative-AI.

2. **You must have rights to everything you upload.** Roblox devforum (Mar 2024): *"You are responsible for ensuring you have the rights to anything you upload to Roblox, regardless of whether you use generative AI."* Also: don't use brand names, existing protected characters, or real people in prompts. Source: https://devforum.roblox.com/t/protecting-intellectual-property-when-using-generative-ai/2881851.

3. **No disclosure required for static AI assets.** Disclosure in the Content Maturity questionnaire is required **only if your game allows players to interact with a generative AI model** (text chat, voice, images, 3D generations, avatar movement). Static pre-generated icons do not trigger this. Extended AI interactions (chatbots, cross-session memory) force a "Restricted" content rating. Source: https://create.roblox.com/docs/generative-AI.

4. **Roblox ToS (updated April 2026) — AI Features section:** you retain rights in your Prompts and Outputs ("to the extent permitted by applicable law, you retain any right, title, and interest that you have in the Prompts and Outputs"); you grant Roblox a license to use them for business purposes; prohibited uses include removing/altering provenance or metadata tags from Outputs, and deceiving others into thinking an Output was created by a human. Source: https://en.help.roblox.com/hc/en-us/articles/115004647846-Roblox-Terms-of-Use; update announcement https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-april-2026/4548394.

5. **Roblox may train on your UGC.** The April 2026 ToS grants Roblox broad rights to UGC "including without limitation in connection with the training of machine learning and related models." A per-asset data-sharing toggle (default ON) controls this. Sources: https://devforum.roblox.com/t/review-your-generative-ai-data-sharing-preferences/3062106; https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-april-2026/4548394.

6. **Protectability on Roblox:** Roblox explicitly warns that purely AI-generated content may not be protectable — *"This lava would not be protectable because AI is solely generating it… you can't submit a DMCA takedown notice if someone used the same lava pattern."* Human modification and combining AI + non-AI elements strengthens protectability. Source: https://devforum.roblox.com/t/protecting-intellectual-property-when-using-generative-ai/2881851.

---

## 4. US Copyright Office — practical one-paragraph summary

The US Copyright Office requires **human authorship** for copyright. Purely AI-generated images (a prompt in, an image out, with no meaningful human control over the expressive elements) are **not copyrightable** in the US — confirmed by the March 2023 Registration Guidance, the January 2025 "Part 2: Copyrightability" report (prompts alone are insufficient; creative selection/arrangement, creative modifications, or human-authored elements perceptible in the output can be protected), and the D.C. Circuit's 2025 affirmance in *Thaler v. Perlmutter*. Practical takeaway for game icons: a purely AI-generated icon can't be protected by copyright (a competitor could copy it and you couldn't stop them via DMCA), but the game as a whole — your code, layout, and any human-modified/arranged art — is protectable, and distinctive branding can be protected by trademark. When registering, you must disclose and disclaim AI-generated material. The bigger practical risk is the flip side: if an AI output closely resembles an existing copyrighted work, you could face an infringement claim — so review outputs before shipping. Sources: https://www.copyright.gov/ai/ai_policy_guidance.pdf (Mar 16, 2023); https://copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf (Jan 29, 2025); https://www.copyright.gov/newsnet/2025/1060.html; https://www.congress.gov/crs-product/LSB10922 (all accessed 2026-08-21).

---

## 5. Practical risk level per model/platform (for a published Roblox game)

| Model | Commercial risk | Why |
|---|---|---|
| SDXL 1.0 base | 🟢 Low | Open RAIL++-M, outputs yours |
| Illustrious XL (v1.x / v2.0) | 🟢 Low | Open RAIL++-M / RAIL-M, commercial OK |
| FLUX.1 schnell | 🟢 Low | Apache 2.0 |
| FLUX.2 [klein] 4B | 🟢 Low | Apache 2.0 |
| Z-Image / Z-Image-Turbo | 🟢 Low | Apache 2.0, no revenue cap |
| Qwen-Image (via API) | 🟢 Low | Apache 2.0 |
| SD 3.5 (Large/Medium) | 🟢 Low (under $1M revenue) | Community License; Enterprise license above $1M |
| FLUX.1 dev / FLUX.2 dev — outputs via BFL API or licensed provider | 🟢 Low | Outputs commercial OK; provider holds commercial rights |
| FLUX.1 dev / FLUX.2 dev — self-hosted | 🟡 Medium | Outputs commercial OK per license, but self-hosting the model commercially requires a BFL license |
| Pony Diffusion V6 XL | 🟡 Medium | License conflict (FAQ offline vs model card); monetized-inference restriction; contact PurpleSmartAI for certainty |
| NoobAI XL | 🔴 High | Explicit commercial prohibition on model-generated products |
| Nano Banana / Gemini (API) | 🟢 Low | Google doesn't claim ownership; commercial via paid API; SynthID watermark |

| Platform | Commercial risk | Why |
|---|---|---|
| Replicate | 🟢 Low | Explicit output-rights grant (§5.1), subject to model license |
| Segmind | 🟢 Low | You retain ownership of Customer Content incl. results |
| RunPod / Modal | 🟢 Low | Raw compute; you own everything; model license governs |
| Tensor.Art | 🟢 Low | No claims on generated images; must use commercially-licensed models |
| DeepInfra | 🟢 Low | You retain IP in Customer Data incl. outputs; zero retention |
| fal.ai | 🟢 Low | No IP claim on outputs; commercial use permitted; model license governs |
| Novita.ai | 🟢 Low–🟡 | Commercial use permitted; explicit output-assignment clause not found in fetched ToS (**unverified**) |

---

## 6. Verdict — which combos are safe to commercialize

**Recommended safe combos for this user (cartoony/stylized potion icons, RTX 3060 12GB, commercial use):**

1. **Local, zero marginal cost, fully commercial:**
   - **Illustrious XL v1.x/v2.0** (or SDXL base) — Open RAIL++-M/RAIL-M, runs on 12GB, strong for stylized/anime-cartoon art. **Best fit for the user's "choose your own models, cheap, local" profile.**
   - **FLUX.2 [klein] 4B** — Apache 2.0, ~8GB VRAM, modern quality, full commercial.
   - **FLUX.1 schnell** (quantized) — Apache 2.0, full commercial.
   - **Z-Image-Turbo** — Apache 2.0, no revenue cap (verify it fits 12GB; vendor claims <16GB).
   - **SD 3.5 Large/Medium** — free commercial under $1M annual revenue (register for commercial use).

2. **API-based, cheap per-image, fully commercial:**
   - **Qwen-Image** via fal.ai / Replicate / Novita / Segmind (Apache 2.0; ~$0.02/image on Novita).
   - **FLUX.1 dev / FLUX.2 dev** via BFL API or licensed providers (fal, Replicate, DeepInfra) — outputs commercial OK.
   - **Nano Banana / Gemini** via Google API (hosted only; SynthID watermark).

3. **Avoid for commercial:** **NoobAI XL** (explicit commercial prohibition on outputs). **Pony v6** only if you accept the license ambiguity and never run it on paid inference platforms — or get written permission from PurpleSmartAI.

**Universal risk-reduction steps (recommended regardless of combo):**
- **Modify AI outputs** (recolor, outline, composite, arrange into a set) — strengthens protectability and reduces infringement risk; Roblox and the USCO both point the same direction.
- **Never prompt with brand names, existing characters, or real people.**
- **Review outputs** for accidental resemblance to existing copyrighted art before shipping.
- **Keep records** of prompts/edits (supports any future copyright claim on your human contribution).
- **Don't strip provenance/metadata** from outputs (Roblox ToS prohibits this).
- **Check the specific model's license on its model card**, not just the platform ToS — the model license is the binding constraint.

---

## 7. Anomalies / dead ends

- **SearXNG instance** (http://100.122.184.37:8082) was reachable but returned zero results for every query attempted; all discovery was done via the Exa-backed `websearch` fallback. No SearXNG results were used.
- **ponydiffusion.com/faq** returned 404 on access (2026-08-21); the "CreativeML OpenRAIL-M" claim for Pony v6 is cited from a search snippet only and is **unverified** — the live model card (modified FAIPL 1.0-SD) is treated as authoritative here.
- **Novita.ai** ToS: no explicit output-assignment clause found in the fetched portion; marked **unverified**.
- **fal.ai** ToS: no explicit output-assignment clause (unlike Replicate); fal disclaims IP in outputs and permits commercial use — treated as low risk but noted.
- **Hardware/VRAM figures** (12GB fits, 8GB for klein 4B, <16GB for Z-Image-Turbo) are vendor/practical estimates, not license claims.
