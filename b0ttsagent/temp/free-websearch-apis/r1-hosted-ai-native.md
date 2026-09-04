# Hosted AI-Native Search APIs — Free-Tier Research (Round 1)

**Date of research:** 2026-09-03 (all pages fetched/read on this date)
**Scope:** Hosted search APIs built for LLM/RAG/agent use (clean content, not raw SERP HTML). Free tier must be genuinely available today.
**Method:** Searches via Exa-backed `websearch` (SearXNG instance returned empty results for all queries this session — noted as an anomaly). Material claims verified by reading vendor pages with `searxng_web_url_read`. Claims marked "(snippet)" come from a search-result snippet of the cited official page, not a full page read — treat as slightly weaker. Third-party sources are labeled as such.

---

## (a) Summary table

| API | Free tier | Cheapest paid | Signup URL | Notes |
|---|---|---|---|---|
| **Exa** (exa.ai) | $20 credits on sign-up + **$10 credits every month**, no payment method required; ~2,800 searches on signup, ~1,400/mo after; 10 QPS on free tier | Pay-as-you-go, no subscription: Search $7/1k requests (10 results incl. text+highlights); Contents $1/1k pages; Answer $5/1k; Deep $12/1k; Deep-Reasoning $15/1k; Monitors $15/1k | https://dashboard.exa.ai | Neural/keyword hybrid search, contents extraction, MCP server; unauthenticated MCP free tier 3 QPS / 150 calls/day |
| **Tavily** (tavily.com) | **1,000 API credits/month**, no credit card; basic search = 1 credit, advanced = 2; keyless (no-account) rate-limited access also exists | Project $30/mo for 4,000 credits ($0.0075/credit); PAYG $0.008/credit | https://app.tavily.com | Search + Extract + Map + Crawl + Research endpoints; dev keys 100 RPM, prod 1,000 RPM |
| **LangSearch** (langsearch.com) | **100% free, no credit card**; rate limits: 1 QPS / 60 QPM / 1,000 QPD (free tier) | No paid plans — rate tiers unlock by cumulative recharge ($10+ → 5 QPS, etc.) | https://langsearch.com/api-keys | Web Search API (hybrid keyword+vector) + Semantic Rerank API; docs say free "as we build AGI together" |
| **You.com** (you.com) | **$100 free API credits** on signup (no card per docs); plus keyless free tier: 100 queries/day via MCP free profile | PAYG: Web Search $5/1k calls (up to 100 results), Contents $1/1k pages, Answer $5/1k, Research from $12/1k | https://you.com/platform | Web+news in one call, LLM-ready snippets, full-page extraction add-on $1/1k pages; SOC 2, ZDR |
| **Linkup** (linkup.so) | **$20 credit on signup (professional email), topped back up to $20/month** for eligible accounts ≈ 4,000 standard searches/mo | PAYG: Search $0.005/request standard (raw results), $0.006 sourced/structured; deep $0.05–0.055; Fetch $0.001–0.005; Research $0.25–2.50 | https://app.linkup.so/sign-up | Search/Fetch/Research/Tasks endpoints; 1–3s latency; x402 payment protocol |
| **Jina AI** (jina.ai) | **10M free tokens one-time** on new API key (shared across Reader/Search/Embeddings/Reranker); keyless Reader 20 RPM; free key: Reader 500 RPM, Search (s.jina.ai) 100 RPM | PAYG tokens ~$0.05/1M (third-party reported; official page shows top-up model); Search min 10k tokens/request | https://jina.ai/api-dashboard | Reader r.jina.ai (URL→Markdown), Search s.jina.ai (web→LLM text); MCP at mcp.jina.ai |
| **Search1API** (search1api.com) | **100 free credits, no credit card, no expiry**; keyless free tier (IP-limited ~5 RPM/20 RPD); 1 credit = 1 search/news/crawl | Basic $19/mo = 25,000 credits (~$0.76/1k); PAYG $1 = 1,000 credits (+bonuses) | https://app.s1.dev | Multi-engine search (Google/Bing/Reddit…), crawl, screenshot, sitemap, deepcrawl, extract; credits never expire |
| **Firecrawl** (firecrawl.dev) | **1,000 credits/month, $0, no card** (current pricing page; older docs said 500 one-time — conflict noted below); keyless MCP for Search/Scrape/Parse | Hobby $16/mo (yearly billing) = 5,000 credits; Search = 2 credits/10 results | https://www.firecrawl.dev/signin?view=signup | Scrape/Crawl/Map/Search/Extract; search returns clean markdown; agent-friendly docs |

**Rejected — no genuine free tier:**

| API | Why rejected | Source |
|---|---|---|
| **Perplexity Sonar API** | No free tier; pay-as-you-go only (prepaid credits, payment method required to get a key). Pro-subscriber $5/mo API credit reportedly discontinued early 2026. Trial credits ($25–50) claimed by third parties but UNVERIFIED | https://docs.perplexity.ai/docs/getting-started/pricing ; https://www.cloudzero.com/blog/perplexity-api-pricing/ |
| **Kagi API** | No free tier for the API — $12/1k requests, invoiced at $100 usage; only the consumer search Trial plan (100 searches) is free | https://kagi.com/api/pricing |
| **Brave Search API** | Free plan eliminated Feb 2026; now paid plans ($5/1k) with $5 monthly credits, **credit card required** even for the credit; card becomes a billing instrument past the credit | https://brave.com/search/api/ ; https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/ |

---

## (b) Detail per API

### 1. Exa (exa.ai) — VERIFIED (official pages read)

**Free tier:** "Starter / Free: $20 credits on sign-up with $10 credits every month. No payment method required." Pricing page headline: "Start for free with over $120 in credits per year." Free tier includes MCP server access, all endpoints, 10 Search QPS, 50 agent concurrency.
Source: https://exa.ai/pricing (read 2026-09-03)

**Paid:** Pay-as-you-go, no subscription, no minimum. Endpoint pricing (per 1k requests): Search $7 (up to 10 results, text+highlights included), Deep Search $12, Deep-Reasoning Search $15, Contents $1 per 1k pages per content type, Monitors $15, Answer $5; +$1 per 1k for each additional result above 10; AI page summaries $1 per 1k pages.
Source: https://exa.ai/pricing (read 2026-09-03)

**Signup:** https://dashboard.exa.ai (onboarding-guest flow) — from pricing page "Sign up" / "Get started" buttons.
Source: https://exa.ai/pricing

**Docs:** https://exa.ai/docs (reference: https://exa.ai/docs/reference/search-api-guide, billing: https://exa.ai/docs/reference/billing)

**Capabilities:** Neural + keyword hybrid search over Exa's own web/people/company/scholarly indexes; Contents endpoint for full-page LLM context; configurable latency 180ms–1s; MCP server; unauthenticated MCP free tier at 3 QPS / 150 calls/day (changelog snippet). March 2026 pricing update retired the old keyword/neural tier split and included contents for first 10 results free.
Sources: https://exa.ai/pricing (read); https://exa.ai/docs/changelog (snippet)

**Note:** Third-party TinyFish blog interprets the free tier as "up to 20,000 requests a month" — an estimate, not official; official model is credit-based ($20 + $10/mo). https://www.tinyfish.ai/blog/exa-pricing (third-party)

### 2. Tavily (tavily.com) — VERIFIED (official docs read)

**Free tier:** "You get 1,000 free API Credits every month. No credit card required." (Researcher plan). Basic search = 1 credit; advanced search = 2 credits; basic extract = 1 credit per 5 URLs; map = 1 credit per 10 pages.
Source: https://docs.tavily.com/documentation/api-credits (read 2026-09-03)

**Paid:** Project $30/mo = 4,000 credits ($0.0075/credit); Bootstrap $100/mo = 15,000; Startup $220/mo = 38,000; Growth $500/mo = 100,000; Pay-as-you-go $0.008/credit; Enterprise custom.
Source: https://docs.tavily.com/documentation/api-credits (read 2026-09-03)

**Signup:** https://app.tavily.com ("Get an API key" link in docs; keyless option exists without account).
Source: https://docs.tavily.com/documentation/api-credits

**Docs:** https://docs.tavily.com (credits: /documentation/api-credits; rate limits: /documentation/rate-limits)

**Capabilities:** Search (basic/advanced), Extract, Map, Crawl, Research endpoints; MCP server; keyless free access (rate-limited, no account) for Search and Extract with identical responses to keyed calls (docs snippet). Rate limits: Development keys 100 RPM, Production 1,000 RPM; crawl 100 RPM both; research 20 RPM.
Sources: https://docs.tavily.com/documentation/rate-limits (read); https://docs.tavily.com/documentation/keyless (snippet)

### 3. LangSearch (langsearch.com) — VERIFIED (official docs read)

**Free tier:** 100% free, no credit card ("Absolutely Free. No upfront cost. No hidden costs."). Rate limits by cumulative recharge: Free Tier ($0) = 1 QPS, 60 QPM, 1,000 QPD; Tier 1 ($10–50) = 5 QPS/200 QPM/2,000 QPD; Tier 2 ($100) = 10 QPS/500 QPM/10,000 QPD; Tier 3 ($500) = 30 QPS/2,000 QPM/100,000 QPD.
Sources: https://docs.langsearch.com/limits/api-limits (read 2026-09-03); https://langsearch.com/pricing (snippet)

**Paid:** No subscription plans — higher rate tiers unlock via cumulative recharge (top-up). No per-query pricing published.
Source: https://docs.langsearch.com/limits/api-limits (read)

**Signup / API key:** https://langsearch.com/api-keys ("create an account and grab a free API key").
Source: https://docs.langsearch.com/getting-started/quickstart (snippet)

**Docs:** https://docs.langsearch.com (Web Search API: /api/web-search-api; Rerank: /api/semantic-rerank-api)

**Capabilities:** Web Search API — hybrid keyword+vector search, news/images, long-text summaries with markdown from raw content; Semantic Rerank API. Docs position it as free for individuals/small teams "as we build AGI together"; ToS notes service can be modified/suspended at discretion (free-access basis).
Sources: https://docs.langsearch.com/ (snippet); https://docs.langsearch.com/legal/terms-of-service (snippet)

### 4. You.com (you.com) — VERIFIED (official pricing page read)

**Free tier:** $100 free API credits on signup ("$100 free credit to get started"); plus a keyless free tier: 100 queries/day via the MCP free profile (`api.you.com/mcp?profile=free`, you-search only). "No credit card required" per You.com docs (snippet) and You.com's own pricing-announcement post.
Sources: https://you.com/pricing (read 2026-09-03); https://you.com/docs/administration/billing (snippet); https://you.com/resources/lower-search-api-cost (snippet)

**Paid:** PAYG, no minimum: Web Search API $5.00/1k calls (up to 100 results, news included); full-page extraction add-on $1.00/1k pages; Contents API $1.00/1k pages; Answer API $5.00/1k calls; Research API $12–$1,200/1k by effort tier (lite→frontier); Finance Research $110–$500/1k. March 2026 price cut (was $6.25–$8/1k).
Sources: https://you.com/pricing (read); https://you.com/resources/lower-search-api-cost (snippet)

**Signup / API key:** https://you.com/platform ("Sign in or create an account, then get an API key here… You'll start with $100 in complimentary credits").
Source: https://you.com/docs/quickstart (snippet)

**Docs:** https://you.com/docs (billing: /docs/administration/billing; search: /docs/guides/search)

**Capabilities:** Web+news in one request, LLM-ready snippets with rich metadata, country/language/recency/domain filters, livecrawl full-page extraction, MCP server, machine payments (USDC, no account) for agents; SOC 2 certified, ZDR available.
Sources: https://you.com/pricing (read); https://you.com/docs/guides/search (snippet)

### 5. Linkup (linkup.so) — VERIFIED (official docs read)

**Free tier:** "When you first sign up with a professional email address, your account is automatically credited with $20. We will top up eligible accounts back to $20 each month." ≈ 4,000 standard searches/month at $0.005. (Note: professional/work email required; eligibility for monthly top-up is at Linkup's discretion.)
Source: https://docs.linkup.so/pages/documentation/platform/pricing (read 2026-09-03)

**Paid:** PAYG prepaid credits: Search standard $0.005 (raw results) / $0.006 (sourcedAnswer/structured); deep $0.05 / $0.055; Fetch $0.001 (no JS) – $0.005 (JS); Research $0.25 (S) – $2.50 (XL); Tasks = same rates, no batching surcharge. Bulk top-up bonuses at $1k/5k/10k (10/15/20%).
Sources: https://docs.linkup.so/pages/documentation/platform/pricing (read); https://docs.linkup.so/pages/changelog/usd-pricing (snippet)

**Signup:** https://app.linkup.so/sign-up ("Create a Linkup account for free to get your API key").
Source: https://docs.linkup.so/pages/documentation/endpoints/search/overview (snippet)

**Docs:** https://docs.linkup.so (pricing: /pages/documentation/platform/pricing; rate limits: /pages/documentation/platform/rate-limits — not read)

**Capabilities:** Search endpoint optimized for AI consumption (ranked sources, optional cited natural-language answer, structured JSON output); Fetch for URL content; async Research; Tasks batch wrapper (up to 100 tasks); 1–3s synchronous latency; x402 payment protocol; SOC 2 Type II + ZDR on every plan (third-party costbench claim).
Sources: https://docs.linkup.so/pages/documentation/endpoints/search/overview (snippet); https://costbench.com/software/ai-search-apis/linkup/free-plan/ (third-party)

### 6. Jina AI (jina.ai) — VERIFIED (official page read; one price claim third-party)

**Free tier:** "Don't panic! Every new API key comes with 10M free tokens!" — one-time welcome grant shared across Reader/Search/Embeddings/Reranker (not recurring). Keyless Reader (r.jina.ai) works at 20 RPM with no key; s.jina.ai search is blocked without a key. Free API key: Reader 500 RPM, Search 100 RPM, Embeddings/Reranker 100 RPM & 100k TPM.
Sources: https://jina.ai/reader/ (read 2026-09-03; 10M-token line from page snippet); https://apio.sh/apis/jina-search (third-party tracker, confirms 10M one-time, no card)

**Paid:** Token top-up model (prepaid). ~$0.05 per 1M tokens reported by third-party trackers (apio.sh, markaicode); Search requests cost a fixed minimum from 10,000 tokens each. Official page shows top-up UI but no published per-token rate in the section read — treat $0.05/1M as third-party-reported.
Sources: https://apio.sh/apis/jina-search (third-party); https://markaicode.com/pricing/jina-ai-pricing/ (third-party); https://jina.ai/reader/ (read)

**Signup / API key:** https://jina.ai/api-dashboard (login/API key & billing).
Source: https://jina.ai/reader/ (read)

**Docs:** https://api.jina.ai/scalar (API reference); https://docs.jina.ai (agents)

**Capabilities:** Reader converts any URL to LLM-friendly Markdown (r.jina.ai); Search returns SERP as LLM text (s.jina.ai); DeepSearch, embeddings, reranker, classifier; MCP server at mcp.jina.ai; EU endpoints; GDPR. Note: third-party reports Elastic acquired Jina AI in October 2025 with pricing unchanged (serp.fast — third-party, UNVERIFIED on official channels).
Source: https://serp.fast/tools/jina-ai (third-party)

### 7. Search1API (search1api.com) — VERIFIED (official pricing page read)

**Free tier:** "Start with 100 free credits — no credit card required"; credits have no expiration date. 1 credit = 1 search, news, or crawl request. Also a keyless free tier (no API key) subject to IP-based rate limits (~5 RPM / 20 RPD per changelog).
Sources: https://www.search1api.com/pricing (read 2026-09-03); https://www.search1api.com/docs/essentials/credits-and-limits (snippet); https://blog.search1api.com/pages/changelog (snippet)

**Paid:** Subscriptions: Basic $19/mo = 25,000 credits (~$0.76/1k one-credit requests); Professional $99/mo = 150,000; Enterprise $499/mo = 1,000,000. PAYG: $1 = 1,000 credits with tier bonuses ($19 +5%, $99 +20%, $499 +60%); credits never expire. Credit costs: /search 1, /news 1, /crawl 1, /screenshot 2, /sitemap 1, /trending 1, /extract 10, /deepcrawl 20; deep search = 1 + n crawled pages.
Source: https://www.search1api.com/pricing (read 2026-09-03)

**Signup:** https://app.s1.dev (dashboard; "Get 100 Free Credits").
Source: https://www.search1api.com/pricing (read)

**Docs:** https://www.search1api.com/docs (also s1.dev/docs; OpenAPI at api.search1api.com/openapi.json)

**Capabilities:** Multi-engine search (Google, Bing, Reddit, etc. via search_service), news, web crawling with full page content, screenshots, sitemaps, trending, deepcrawl (whole-site markdown), schema-driven extract; MCP server; OAuth 2.1 for agents; agentic resource catalog (s1.dev/.well-known/ai-catalog.json).
Sources: https://www.search1api.com/docs (snippet); https://blog.search1api.com/posts/oauth-for-ai-agents (snippet)

### 8. Firecrawl (firecrawl.dev) — VERIFIED (official pricing page read; one conflict noted)

**Free tier:** "Free Plan: 1,000 credits / month, $0/month. No cost, no card, no hassle. Scrape 1,000 pages, 2 concurrent requests, low rate limits." Search costs 2 credits per 10 results; scrape/crawl/map 1 credit/page. Keyless MCP endpoint exposes Search/Scrape/Parse without an API key (IP-capped daily).
Sources: https://www.firecrawl.dev/pricing (read 2026-09-03); https://docs.firecrawl.dev/rate-limits (snippet)

**CONFLICT:** Firecrawl's GitHub-hosted billing doc (older revision) says "Free plan provides a one-time allotment of 500 credits… do not renew," while the current pricing page and docs say 1,000 credits/month. The current pricing page (read today) is authoritative; the 500-credit one-time text is stale.
Sources: https://www.firecrawl.dev/pricing (read); https://github.com/firecrawl/firecrawl-docs/blob/82e953cf4f45fa00808b8315590eb758ff67441a/billing.mdx (stale)

**Paid:** Hobby $16/mo (billed yearly; $19 monthly) = 5,000 credits; Standard $83/mo = 100,000; Growth $333/mo = 500,000; Scale $599/mo = 1,000,000; extra credits in $5 batches (1,000 credits on Hobby). Free-tier rate limits: /search 10 RPM, /scrape 10, /crawl 2, /agent 2.
Sources: https://www.firecrawl.dev/pricing (read); https://docs.firecrawl.dev/rate-limits (snippet)

**Signup:** https://www.firecrawl.dev/signin?view=signup
Source: https://www.firecrawl.dev/pricing (read)

**Docs:** https://docs.firecrawl.dev (billing: /billing; search: /features/search)

**Capabilities:** Scrape (URL→clean markdown/HTML/structured), Crawl, Map, Search (web search + optional scraping of results), Extract, Interact (browser), Monitor, Agent (preview, 5 free daily runs); Research Index paper endpoints free; ZDR search option (10 credits/10 results, enterprise).
Sources: https://www.firecrawl.dev/pricing (read); https://docs.firecrawl.dev/features/search (snippet)

---

## (c) Unverified / Unknown

- **Perplexity new-account trial credits ($25–50)** — claimed by third-party blog getaiperks.com; contradicts cloudzero.com analysis ("no free tier, payment method required"). Official docs show no free credits. UNVERIFIED. Sources: https://www.getaiperks.com/en/ai/perplexity-api-free-credits-2026 (third-party); https://www.cloudzero.com/blog/perplexity-api-pricing/ (third-party)
- **Perplexity Pro $5/mo API credit** — reported discontinued Feb 2026 by multiple third parties (cloudzero, puter.com, opslyft); official docs don't mention it. UNVERIFIED on official channels.
- **Jina AI $0.05/1M token rate** — third-party-reported; official reader page read showed the top-up model but not the per-token rate in the section captured. UNVERIFIED on official page read.
- **Jina AI acquisition by Elastic (Oct 2025)** — third-party claim (serp.fast); not confirmed on official pages read. UNVERIFIED.
- **Linkup monthly top-up eligibility criteria** — docs say "eligible accounts" without defining eligibility. UNKNOWN.
- **Linkup rate-limit numbers** — rate-limits page exists but was not read. UNKNOWN.
- **Exa free tier "20,000 requests/month"** — TinyFish blog estimate; official model is credit-based. Not official.
- **Search1API keyless rate limits (5 RPM/20 RPD)** — from changelog snippet; exact current numbers UNVERIFIED on pricing page.
- **You.com "no credit card required"** — from You.com docs/blog snippets; the pricing page read shows "$100 free credit" and keyless free tier but the no-card line was not in the rendered section. Reasonably reliable (official sources), flagged as snippet-level.
- **LangSearch longevity** — free-access model with ToS reserving the right to modify/suspend service; no paid plan exists, so no commercial commitment from vendor. Risk note, not a fact.

---

## (d) Full source list

**Official pages read in full or in part (2026-09-03):**
1. https://exa.ai/pricing
2. https://docs.tavily.com/documentation/api-credits
3. https://docs.tavily.com/documentation/rate-limits
4. https://docs.langsearch.com/limits/api-limits
5. https://docs.perplexity.ai/docs/getting-started/pricing
6. https://docs.perplexity.ai/docs/resources/faq
7. https://docs.linkup.so/pages/documentation/platform/pricing
8. https://kagi.com/api/pricing
9. https://www.search1api.com/pricing
10. https://jina.ai/reader/
11. https://www.firecrawl.dev/pricing
12. https://brave.com/search/api/
13. https://you.com/pricing

**Official pages cited via search snippets (not fully read):**
14. https://exa.ai/docs/reference/billing
15. https://exa.ai/docs/changelog
16. https://docs.tavily.com/documentation/keyless
17. https://langsearch.com/pricing
18. https://docs.langsearch.com/getting-started/quickstart
19. https://docs.langsearch.com/
20. https://docs.langsearch.com/legal/terms-of-service
21. https://you.com/docs/administration/billing
22. https://you.com/docs/quickstart
23. https://you.com/docs/guides/search
24. https://you.com/resources/lower-search-api-cost
25. https://docs.linkup.so/pages/documentation/endpoints/search/overview
26. https://docs.linkup.so/pages/changelog/usd-pricing
27. https://docs.linkup.so/pages/documentation/endpoints/tasks/overview
28. https://docs.linkup.so/pages/faq/faq
29. https://www.search1api.com/docs/essentials/credits-and-limits
30. https://blog.search1api.com/pages/changelog
31. https://blog.search1api.com/posts/oauth-for-ai-agents
32. https://www.search1api.com/docs
33. https://docs.firecrawl.dev/rate-limits
34. https://docs.firecrawl.dev/features/search
35. https://docs.firecrawl.dev/billing
36. https://api-dashboard.search.brave.com/documentation/pricing
37. https://brave.com/blog/most-powerful-search-api-for-ai/
38. https://help.kagi.com/kagi/api/overview.html
39. https://help.kagi.com/kagi/api/api-portal.html
40. https://github.com/firecrawl/firecrawl-docs/blob/82e953cf4f45fa00808b8315590eb758ff67441a/billing.mdx (stale revision)

**Third-party sources (labeled; used for corroboration or conflict reporting):**
41. https://www.tinyfish.ai/blog/exa-pricing
42. https://fastcrw.com/blog/exa-pricing-explained
43. https://serp.fast/tools/exa
44. https://tokenmix.ai/blog/tavily-ai-api-pricing-2026-credits-rate-limits
45. https://freetier.co/directory/products/tavily
46. https://www.cloudzero.com/blog/perplexity-api-pricing/
47. https://developer.puter.com/tutorials/perplexity-api-pricing/
48. https://www.opslyft.com/blog/perplexity-ai-pricing
49. https://www.getaiperks.com/en/ai/perplexity-api-free-credits-2026
50. https://coldiq.com/blog/linkup-pricing
51. https://costbench.com/software/ai-search-apis/linkup/free-plan/
52. https://apio.sh/apis/jina-search
53. https://apio.sh/apis/kagi-search
54. https://markaicode.com/pricing/jina-ai-pricing/
55. https://www.eggstriker.com/en/ai-api/jinaai
56. https://serp.fast/tools/jina-ai
57. https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/
58. https://aidiscoverr.com/coding-tools/brave-search-api
59. https://agentdeals.dev/vendor/brave-search-api
60. https://github.com/openclaw/openclaw/issues/16629
61. https://www.developer-tech.com/news/brave-search-api-revamp-makes-web-search-useful-for-ai-apps/

**Anomaly note:** The configured SearXNG instance (http://100.122.184.37:8082) was reachable per /config but returned zero results for every query attempted this session; all discovery was done via the Exa-backed `websearch` tool. No API keys, secrets, or PII were submitted to any tool.