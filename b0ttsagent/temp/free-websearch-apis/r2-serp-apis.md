# SERP / Traditional Search APIs — Free-Tier Research (Round 2)

**Date of research:** 2026-09-03 · **Scope:** programmatic web-search (SERP) APIs with free access · **Method:** SearXNG + Exa web search, then direct reads of official vendor pages. Every claim below carries a URL fetched/read this session. Third-party sources are labeled as such.

---

## (a) Summary table

| API | Free tier (current, 2026) | Cheapest paid | Signup URL | Status / Deprecation |
|---|---|---|---|---|
| **Serper** (serper.dev) | 2,500 free queries, one-time, no credit card | $50 top-up = 50k credits ($1.00/1k), credits valid 6 months | https://serper.dev/ (Sign up) | Active. No deprecation. |
| **Brave Search API** | No standalone free plan since Feb 2026 — $5 free credits/month on paid plans ≈ 1,000 Search requests/mo; credit card required; attribution required for credits | $5/1k requests (Search plan) | https://api-dashboard.search.brave.com/register | Active. Free tier replaced by metered credits (official blog, 2026-02-12). |
| **Bing Search API (Azure)** | **RETIRED** — none | N/A (replacement: Grounding with Bing Search $14/1k transactions) | N/A — new signups closed | **Retired 2025-08-11** (official Microsoft Learn lifecycle). |
| **Google Custom Search JSON API** | 100 queries/day free (existing customers only) | $5 per 1,000 queries, up to 10k/day (existing customers only) | N/A — **closed to new customers** | **Discontinued 2027-01-01** (official Google docs + blog, 2026-01-20). |
| **SerpApi** | 250 searches/month, 50/hr, recurring | $25/mo = 1,000 searches | https://serpapi.com/users/sign_up | Active. |
| **SearchApi.io** | 100 free requests, one-time, no credit card | $40/mo = 10,000 searches ($4/1k) | https://www.searchapi.io/users/sign_up | Active. |
| **DataForSEO** | $1 free credit on signup (unlimited trial period); free sandbox | Pay-as-you-go, min deposit $50; SERP from $0.0006/SERP ($0.6/1k, standard queue) | https://dataforseo.com/apis/serp-api ("Get a Free Account") | Active. Pricing update 2026-07-01 (+~20%, monthly commitments removed). |
| **Zenserp** | 50 searches/month, recurring, no credit card | $49.99/mo = 25,000 searches | https://app.zenserp.com/register | Active. |
| **Scale SERP** | 125 free searches/month, no credit card | $66/mo = 10,000 searches (annual billing) | https://app.scaleserp.com/signup/10k | Active; now owned by Traject Data (joined ScraperAPI). |
| **HasData** | 1,000 credits/month recurring (≈100 Google SERP calls at 10 credits each), no credit card | $49/mo = 200,000 credits | https://app.hasdata.com/sign-up | Active. |
| **Oxylabs SERP Scraper API** | One-time trial up to 2,000 results (Google capped at 1,000 per official help-center table), no credit card; **no permanent free tier** | $49/mo Micro (Google ≈ $1.00/1k results) | https://dashboard.oxylabs.io (via "Start free trial") | Active. |
| **Scrappa** (discovered) | 500 free credits/month, recurring, no credit card | Pay-as-you-go from $0.30/1k | https://scrappa.co/register | Active. |

**Rejected / no-free-tier (with source):**
- **Bing Search API** — retired 2025-08-11, no replacement free tier (official: https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement).
- **Google Custom Search JSON API** — closing 2027-01-01, closed to new customers (official: https://developers.google.com/custom-search/v1/overview).
- **ValueSERP** — no free tier per third-party comparison (https://serpapi.org/posts/serpapi-vs-valueserp-vs-scale-serp-2026-comparison).
- **Zyte** — no permanent free tier; $5 signup credits per third-party roundup (https://scrape.do/blog/google-serp-api/).
- **Bright Data** — no free tier found in this session's sources (no source fetched — see Unverified).

---

## (b) Detail per API

### 1. Serper (serper.dev) — ACTIVE
- **Free tier:** 2,500 free queries, one-time allowance, **no credit card required** — confirmed by direct read of https://serper.dev/ ("Get 2,500 free queries / No credit card required"). Third-party analysis confirms it is a one-time allowance, not monthly (https://apiserpent.com/blog/serper-pricing-credits-explained, 2026-07-17).
- **Paid:** prepaid credit top-ups, no subscription: $50 = 50,000 credits ($1.00/1k, 50 QPS) → $375 = 500k ($0.75/1k) → $1,250 = 2.5M ($0.50/1k) → $3,750 = 12.5M ($0.30/1k); credits valid 6 months. Source: serper.dev homepage pricing section (fetched via search snippet of https://serper.dev/ and https://serper.dev/?from=explinks.com) + https://apiserpent.com/blog/serper-pricing-credits-explained. Note: serper.dev/pricing reportedly 404s; pack prices shown after signup (apiserpent, 2026-07-17).
- **Signup:** https://serper.dev/ (Sign up button on homepage).
- **Docs:** https://serper.dev/ (docs link from homepage; exact /docs path not independently verified this session).
- **Deprecation:** none found.

### 2. Brave Search API — ACTIVE, free tier restructured Feb 2026
- **Free tier (current):** No standalone free plan. All plans include **$5 in free credits every month** — at $5/1k requests that is ≈ **1,000 Search requests/month**. Confirmed by direct reads of https://brave.com/search/api/ and https://api-dashboard.search.brave.com/documentation/pricing ("Includes free $5 in credits every month. Credits are automatically applied to your account.").
- **Credit card:** required at signup even for free usage — Brave FAQ on https://brave.com/search/api/ ("The credit card requirement serves as an anti-fraud measure… the card is only used to confirm your identity and will not be charged"). Third-party reporting (https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/, 2026-06-08) claims the card is now billed once credits are exceeded — Brave's own FAQ text appears stale; treat the "will not be charged" wording as outdated.
- **Attribution requirement:** official Brave blog (2026-02-12): "To take advantage of this free credit, all you need to do is attribute the Brave Search API in your project's website / about pages" (https://brave.com/blog/most-powerful-search-api-for-ai/).
- **History:** old free tier was 2,000 queries/mo (2023), raised to 5,000 under Aug 2025 AI Grounding update; replaced Feb 2026 by $5 monthly credits (https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/; https://agentdeals.dev/vendor/brave-search-api).
- **Paid:** Search $5/1k requests (50 QPS); Answers $4/1k + $5/M tokens (2 QPS); Spellcheck & Autosuggest $5/10k requests (https://api-dashboard.search.brave.com/documentation/pricing).
- **Signup:** https://api-dashboard.search.brave.com/register (linked from https://brave.com/search/api/).
- **Docs:** https://api-dashboard.search.brave.com/documentation (verified).
- **Deprecation:** none.

### 3. Bing Search API (Azure) — RETIRED 2025-08-11
- **Status:** **Fully retired.** Official Microsoft Learn lifecycle announcement (read directly): "Bing Search APIs will be retired on August 11, 2025. Any existing instances of Bing Search APIs will be decommissioned completely, and the product will no longer be available to be used or new customer signup." — https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement (page last updated 2025-05-16). Applies to Bing Search F1/S1–S9 and Bing Custom Search F0/S1–S4 resources (https://www.seroundtable.com/bing-search-apis-retiring-august-11-2025-39406.html; https://winbuzzer.com/2025/05/12/microsoft-retires-bing-search-apis-pushes-azure-ai-agents-xcxwbn/).
- **Free tier:** none — product gone. New deployments were already blocked before retirement (https://learn.microsoft.com/en-us/answers/questions/2225180/how-to-resolve-deployment-of-new-bing-resources-is).
- **Replacement:** "Grounding with Bing Search" in Azure AI Foundry Agent Service — **$14 per 1,000 transactions**, 150 TPS, 1M transactions/day (official pricing snippet from https://www.microsoft.com/en-us/bing/apis, fetched this session; page is nav-heavy, table text captured via search snippet of the same URL). **Conflict:** a Microsoft Q&A answer and ppc.land cite $35/1k transactions (https://learn.microsoft.com/en-us/answers/questions/5568912/azure-sponsorship-subscription-request-bing-ground; https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/). The $14 figure is from Microsoft's current official pricing page; the $35 figure may be stale or SKU-specific — flagged.
- **Signup:** N/A (retired). Grounding with Bing requires a paid/pay-as-you-go Azure subscription; sponsored/free-credit subscriptions not eligible (https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/bing-grounding).
- **Docs:** https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/bing-grounding (linked from the retirement notice).

### 4. Google Custom Search JSON API (Programmable Search Engine) — CLOSING 2027-01-01
- **Status:** **Closed to new customers; discontinued January 1, 2027.** Official docs (read directly, English): "The Custom Search JSON API is closed to new customers… Existing Custom Search JSON API customers have until **January 1, 2027** to transition to an alternative solution." — https://developers.google.com/custom-search/v1/overview.
- **Official announcement:** Programmable Search Engine Blog, "Updates to our Web Search Products & Programmable Search Engine Capabilities", **2026-01-20** — https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html. Key points (from the blog + its HN discussion quoting Google's follow-up email): new engines restricted to "Sites to search" (≤50 domains) as of 2026-01-20; "Search the entire web" engines keep working until 2027-01-01; Google is building a new enterprise "Web Search Service" (HN-quoted email: $15 CPM, $30,000/month minimum — third-party quote, UNVERIFIED).
- **Free quota (current, existing customers):** 100 search queries/day free; additional requests **$5 per 1,000 queries**, up to 10k queries/day — official pricing text read directly at https://developers.google.com/custom-search/v1/overview.
- **Signup:** N/A — closed to new customers.
- **Docs:** https://developers.google.com/custom-search/v1/overview (also reference: https://developers.google.com/custom-search/v1).
- **Related:** Site Restricted JSON API already shut down 2025-01-08 (https://apiserpent.com/blog/google-custom-search-api-replacement-code, third-party).

### 5. SerpApi — ACTIVE
- **Free tier:** 250 searches/month, 50 searches/hour, recurring monthly — official pricing markdown read directly: https://serpapi.com/pricing.md (Free | $0 | 250 | 50/hr).
- **Paid:** Starter $25/mo = 1,000 searches ($25/1k); Developer $75/mo = 5,000; Production $150/mo = 15,000; Big Data $275/mo = 30,000; up to Cloud 40M tiers (https://serpapi.com/pricing.md).
- **Signup:** https://serpapi.com/users/sign_up (from official pricing.md frontmatter).
- **Docs:** https://serpapi.com/search-api (link verified in site nav on https://serpapi.com/pricing).
- **Deprecation:** none.

### 6. SearchApi.io — ACTIVE
- **Free tier:** 100 free requests, one-time trial, **no credit card** — https://www.searchapi.io/ ("Get 100 Free Requests… No credit card required") and https://www.searchapi.io/pricing ("Sign up for 100 free requests").
- **Paid (official pricing page, read directly):** Developer $40/mo = 10,000 searches ($4/1k); Production $100/mo = 35,000 ($3/1k); BigData $250/mo = 100,000 ($2.5/1k); Scale $500/mo = 250,000 ($2/1k); Octo 500K $900/mo ($1.8/1k); Octo 1M $1,500/mo ($1.5/1k); Octo 2M $2,800/mo ($1.4/1k); Octo 5M $5,000/mo ($1/1k) — https://www.searchapi.io/pricing. Pay-per-success (only 200-status responses billed).
- **Signup:** https://www.searchapi.io/users/sign_up (link in site nav on pricing page).
- **Docs:** linked from https://www.searchapi.io/ ("View Documentation"); exact path not verified.
- **Deprecation:** none.

### 7. DataForSEO — ACTIVE
- **Free tier:** $1 credit added on registration, unlimited trial period (no expiry); free Sandbox for testing — official FAQ: https://dataforseo.com/help-center/how-does-your-free-unlimited-trial-work and https://dataforseo.com/apis/serp-api/pricing. $1 ≈ 833 high-priority SERPs (official help-center).
- **Paid:** pay-as-you-go, **minimum deposit $50** (https://dataforseo.com/pricing). SERP API: $0.0006/SERP standard queue ($0.6/1k), $0.0012 priority, $0.002 live (https://dataforseo.com/apis/serp-api; https://dataforseo.com/serp-api-v3). **2026-07-01 pricing update:** ~+20% across APIs, monthly commitments cancelled (https://dataforseo.com/update/pricing-update-in-dataforseo-apis).
- **Signup:** "Get a Free Account" CTA on https://dataforseo.com/apis/serp-api (app domain app.dataforseo.com verified in site nav; exact signup path not fetched).
- **Docs:** https://docs.dataforseo.com/v3 (verified in site nav).
- **Deprecation:** none.

### 8. Zenserp — ACTIVE
- **Free tier:** 50 searches/month, recurring, no credit card — official pricing page read directly: https://zenserp.com/pricing-plans/ ("Get started with our free plan and get 50 requests / month for free").
- **Paid:** Small $49.99/mo = 25,000 searches; Medium $149.99/mo = 100k; Large $299.99/mo = 250k; Premium $499.99/mo = 500k; Enterprise $899.99/mo = 1M; yearly billing −20% (https://zenserp.com/pricing-plans/).
- **Signup:** https://app.zenserp.com/register (verified on pricing page).
- **Docs:** https://app.zenserp.com/documentation (verified in site nav).
- **Deprecation:** none.

### 9. Scale SERP — ACTIVE (owned by Traject Data / ScraperAPI)
- **Free tier:** 125 free searches/month, no credit card — official FAQ on the current owner's pricing page: https://trajectdata.com/serp/scale-serp-api/pricing/ ("Our free tier gives you 125 free searches a month to use to evaluate Scale SERP. No credit card is required.").
- **Paid (official, read directly):** 10,000 searches $66/mo; 50,000 $199/mo; 250,000 $599/mo; 1M $1,699/mo; 5M $4,999/mo (annual billing; overage per-search fees listed) — https://trajectdata.com/serp/scale-serp-api/pricing/.
- **Status note:** scaleserp.com now redirects to trajectdata.com; banner "Traject Data joins ScraperAPI" (https://trajectdata.com/serp/scale-serp-api/pricing/).
- **Signup:** https://app.scaleserp.com/signup/10k (from pricing page "Get Started" links).
- **Docs:** https://docs.trajectdata.com (verified in site nav).
- **Deprecation:** none.

### 10. HasData — ACTIVE
- **Free tier:** **1,000 credits every month**, recurring, no credit card — official pricing page read directly: https://hasdata.com/prices ("The free plan gives 1,000 credits every month with access to every tool. No credit card required."). Google SERP API costs 10 credits/request (official docs: https://hasdata.mintlify.app/apis/google-serp-api/quickstart) → ≈ **100 Google SERP calls/month free**. **Conflict:** the Google SERP API product page says "100 SERPs to start, 1,000 credits, one time" (https://hasdata.com/apis/google-serp-api) — one-time vs recurring wording differs between HasData's own pages; the /prices page (fetched directly) says monthly.
- **Paid:** Startup $49/mo = 200k credits; Basic $99/mo = 1M; Growth $208/mo = 3M (https://hasdata.com/prices). Google SERP API per-1k: $2.46 (Startup), $0.99 (Basic), $0.69 (Growth) (https://hasdata.com/prices).
- **Signup:** https://app.hasdata.com/sign-up (verified on prices page).
- **Docs:** https://docs.hasdata.com (verified in site nav).
- **Deprecation:** none.

### 11. Oxylabs SERP Scraper API — ACTIVE (trial only, no permanent free tier)
- **Free tier:** one-time trial **up to 2,000 results, no credit card** — official: https://oxylabs.io/products/scraper-api/serp ("Try SERP Scraper API with up to 2K free results… No credit card required"). Official help-center table caps Google trial results at 1,000 (https://developers.oxylabs.io/help-center/billing-and-payments/how-does-web-scraper-api-pricing-work). No permanent free tier (https://webscraping.cc/blog/oxylabs-free-trial/, third-party, 2026-07-30).
- **Paid:** Web Scraper API Micro $49/mo; Google results $1.00/1k (Micro) down to $0.60/1k (Business) (https://oxylabs.io/products/scraper-api/serp; https://scrappa.co/oxylabs-alternative).
- **Signup:** https://dashboard.oxylabs.io (verified in site nav; "Start free trial" CTA on product page).
- **Docs:** https://developers.oxylabs.io (verified).
- **Deprecation:** none.

### 12. Scrappa (discovered) — ACTIVE
- **Free tier:** **500 free credits every month** after email verification, no credit card — official homepage read directly: https://scrappa.co/ ("500 free credits every month after email verification. No credit card required.").
- **Paid:** pay-as-you-go from $0.30/1k requests (https://scrappa.co/; https://scrappa.co/pricing linked).
- **Signup:** https://scrappa.co/register (verified on homepage).
- **Docs:** https://scrappa.co/docs (verified).
- **Deprecation:** none. (Vendor is small/new; treat as lower-trust than the majors.)

---

## (c) Unverified / Unknown

- **Google "Web Search Service" replacement pricing ($15 CPM, $30k/mo minimum)** — quoted from a Google email in an HN comment; no official Google page fetched. UNVERIFIED (https://news.ycombinator.com/item?id=46730436).
- **Grounding with Bing Search price conflict** — official Microsoft pricing page shows $14/1k transactions; Microsoft Q&A answer and ppc.land say $35/1k. Official page fetched this session (snippet-level); $35 sources are older. Flagged, not resolved (https://www.microsoft.com/en-us/bing/apis; https://learn.microsoft.com/en-us/answers/questions/5568912/; https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/).
- **Brave card-billing behavior** — Brave's own FAQ still says the card "will not be charged"; third-party reporting says cards are billed after credits are exhausted. UNVERIFIED which is true today (https://brave.com/search/api/ vs https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/).
- **HasData free tier recurrence** — /prices says 1,000 credits/month recurring; /apis/google-serp-api says one-time. Conflict within vendor's own pages (https://hasdata.com/prices vs https://hasdata.com/apis/google-serp-api).
- **Serper paid pack prices** — shown on homepage search snippets but serper.dev/pricing reportedly 404s; pack prices confirmed only via third-party breakdown (https://apiserpent.com/blog/serper-pricing-credits-explained).
- **Bright Data free tier** — no source fetched this session; excluded from rejected list on that basis. UNKNOWN.
- **Serper docs exact URL** — https://serper.dev/docs not independently fetched. UNVERIFIED path.
- **SearchApi.io docs exact URL** — not fetched. UNVERIFIED path.
- **DataForSEO signup exact URL** — app.dataforseo.com/signup not fetched; CTA page verified only.
- **Oxylabs trial duration** — not stated on official page (third-party: https://webscraping.cc/blog/oxylabs-free-trial/).
- **Zyte free tier** — "$5 free credits on signup" is a third-party claim (https://scrape.do/blog/google-serp-api/), not verified against Zyte's own site.

---

## (d) Source list (all fetched/read this session unless noted)

**Official vendor pages**
1. https://serper.dev/ — free tier 2,500 queries, no card; pricing tiers (fetched)
2. https://brave.com/search/api/ — plans, $5 monthly credits, FAQ (fetched)
3. https://api-dashboard.search.brave.com/documentation/pricing — official pricing docs (fetched)
4. https://brave.com/blog/most-powerful-search-api-for-ai/ — 2026-02-12 revamp, attribution requirement (search snippet)
5. https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement — Bing retirement (fetched)
6. https://www.microsoft.com/en-us/bing/apis — Grounding with Bing pricing $14/1k (fetched, table via snippet)
7. https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/bing-grounding — eligibility (snippet)
8. https://developers.google.com/custom-search/v1/overview — CSE closure + pricing (fetched, English)
9. https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html — official announcement 2026-01-20 (snippet)
10. https://serpapi.com/pricing.md — official pricing table (fetched)
11. https://serpapi.com/pricing — site nav, docs link (fetched)
12. https://www.searchapi.io/pricing — official plans (fetched)
13. https://www.searchapi.io/ — 100 free requests, no card (snippet)
14. https://dataforseo.com/apis/serp-api/pricing — $1 credit, $50 min (snippet)
15. https://dataforseo.com/help-center/how-does-your-free-unlimited-trial-work — trial mechanics (snippet)
16. https://dataforseo.com/apis/serp-api — SERP pricing $0.0006–$0.002 (snippet)
17. https://dataforseo.com/update/pricing-update-in-dataforseo-apis — 2026-07-01 update (snippet)
18. https://zenserp.com/pricing-plans/ — free 50/mo + paid tiers (fetched)
19. https://trajectdata.com/serp/scale-serp-api/pricing/ — 125 free/mo + paid tiers (fetched)
20. https://hasdata.com/prices — 1,000 credits/mo free + plans (fetched)
21. https://hasdata.com/apis/google-serp-api — 100 SERPs one-time wording (snippet)
22. https://hasdata.mintlify.app/apis/google-serp-api/quickstart — 10 credits/request (snippet)
23. https://oxylabs.io/products/scraper-api/serp — 2k free trial, Google $1.00/1k (snippet)
24. https://developers.oxylabs.io/help-center/billing-and-payments/how-does-web-scraper-api-pricing-work — trial result caps (snippet)
25. https://scrappa.co/ — 500 free credits/month, $0.30/1k (fetched)

**Third-party (labeled in text)**
26. https://apiserpent.com/blog/serper-pricing-credits-explained (2026-07-17)
27. https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/ (2026-06-08)
28. https://agentdeals.dev/vendor/brave-search-api (verified 2026-06-27)
29. https://scrapegraphai.com/blog/brave-search-api (2026-07-09)
30. https://www.theverge.com/news/667517/microsoft-bing-search-api-end-of-support-ai-replacement (2025-05-15)
31. https://www.seroundtable.com/bing-search-apis-retiring-august-11-2025-39406.html (2025-05-14)
32. https://winbuzzer.com/2025/05/12/microsoft-retires-bing-search-apis-pushes-azure-ai-agents-xcxwbn/ (2025-05-12)
33. https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/ (2025-06-09)
34. https://learn.microsoft.com/en-us/answers/questions/5568912/azure-sponsorship-subscription-request-bing-ground — $35/1k claim
35. https://news.ycombinator.com/item?id=46730436 — Google email quote ($15 CPM / $30k min)
36. https://apiserpent.com/blog/google-custom-search-api-shutdown-migration (2026-06-08)
37. https://apiserpent.com/blog/google-custom-search-api-replacement-code (2026-07-21)
38. https://thenextgennexus.com/2026/05/14/google-kills-custom-search-api-on-jan-1-2027-you-have-9-months/ (2026-05-14)
39. https://thatmarketingbuddy.com/pricing/searchapi (verified 2026-05-26)
40. https://serpapi.org/posts/serpapi-vs-valueserp-vs-scale-serp-2026-comparison (2026-08-11)
41. https://scrape.do/blog/google-serp-api/ (2026-08-20)
42. https://webscraping.cc/blog/oxylabs-free-trial/ (2026-07-30)
43. https://scrappa.co/oxylabs-alternative (June 2026 review)
44. https://freeserp.com/pricing — FreeSERP 100 credits/mo free (discovered, not in main table)
45. https://www.searchcans.com/blog/zenserp-scale-serp-searchcans-comparison/ (2026-01-02)
46. https://trajectdata.com/serp/scale-serp-api/pricing/ (Scale SERP FAQ quote)