# Free Web Search APIs — Verified Comparison

**Research date:** 2026-09-03 · **Lifespan:** reference snapshot (pricing changes fast — re-verify at the linked source before relying on numbers)
**Method:** four parallel researchers; every factual claim below was read at an official source during this session. Raw researcher notes with full source lists: `b0ttsagent/temp/free-websearch-apis/r1-hosted-ai-native.md`, `r2-serp-apis.md`, `r3-self-hosted.md`, `r4-mcp-coverage.md`.
**Companion evidence:** `SEARXNG-ENGINE-TEST-RESULTS.md` + the `test_*.json` / `search*.json` files in this folder (local SearXNG engine tests that motivated this research).

Purpose: pick free web-search APIs for the agent harness and decide which keys to wire into MCP.

---

## Recommendation matrix (short answers)

| Decision | Pick | Why |
|---|---|---|
| Highest recurring free quota (hosted) | **Tavily** — 1,000 credits/mo, no card ([docs](https://docs.tavily.com/documentation/api-credits)) | Grant renews monthly; 1 credit ≈ 1 basic search. Runner-up: You.com's larger but one-time $100 grant ([pricing](https://you.com/pricing)) |
| Most free volume, zero cost forever | **LangSearch** — free tier 1,000 queries/day ([limits](https://docs.langsearch.com/limits/api-limits)) | ~30k queries/mo possible, capped at 1 QPS. No paid plan exists — vendor longevity is a trust call, not a contract |
| Best AI-optimized results | **Exa** — neural+keyword over its own index ([pricing](https://exa.ai/pricing)) | Built for LLM use; contents included for the first 10 results. Tavily and You.com close behind for agent-shaped results |
| Truly free self-hosted | **SearXNG + Searcharvester** ([SearXNG](https://github.com/searxng/searxng) · [Searcharvester](https://github.com/vakovalskii/searcharvester)) | No keys, no quota; Searcharvester adds a Tavily-compatible REST layer. Caveat: upstream engines rate-limit/CAPTCHA — see the engine-test evidence |
| Best official MCP support | **Exa, Tavily, Brave** | Vendor-maintained npm packages (see MCP table). SearXNG's community `mcp-searxng` is the de-facto standard and already configured in this harness |

**Do not onboard:** Bing Search API (retired) · Google Custom Search JSON API (closing) · Whoogle (archived). Details in the next section.

---

## Deprecation and restructuring warnings

| API | What happened | Official source |
|---|---|---|
| **Bing Search API (Azure)** | **Retired 2025-08-11** — all instances decommissioned, new signups closed, no free replacement. Successor "Grounding with Bing" is an Azure agent-tool at $14/1k transactions (an older $35/1k figure circulates — conflict flagged below) | [Microsoft Learn lifecycle](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement) |
| **Google Custom Search JSON API** | **Closed to new customers; discontinued 2027-01-01.** Existing customers keep 100 queries/day free, then $5/1k. Since 2026-01-20 no new "search the entire web" engines can be created | [developers.google.com — CSE overview](https://developers.google.com/custom-search/v1/overview) · [official blog 2026-01-20](https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html) |
| **Brave Search API** | Standalone free plan eliminated **Feb 2026**. All plans now include $5 credits/mo (≈1,000 search requests), but a **credit card is required** at signup and **attribution** is required to keep the credits | [brave.com/search/api](https://brave.com/search/api/) · [Brave blog 2026-02-12](https://brave.com/blog/most-powerful-search-api-for-ai/) |
| **Whoogle** (self-hosted) | Repo **archived 2026-07-24** — "no longer returns search results" (Google blocked it). No JSON API ever existed | [GitHub](https://github.com/benbusby/whoogle-search) |

---

## Hosted AI-native search APIs

Built for LLM/RAG use — return clean content and structured results, not raw SERP HTML.

| API | Free tier | Cheapest paid | Signup | MCP server |
|---|---|---|---|---|
| [Exa](https://exa.ai/pricing) | $20 credits at signup + $10/mo recurring, no card; 10 QPS | PAYG Search $7/1k (contents included for 10 results) | `https://dashboard.exa.ai` | **Official** `exa-mcp-server` |
| [Tavily](https://docs.tavily.com/documentation/api-credits) | 1,000 credits/mo, no card (basic search = 1 credit, advanced = 2) | Project $30/mo = 4,000 credits | `https://app.tavily.com` | **Official** `tavily-mcp` |
| [LangSearch](https://docs.langsearch.com/limits/api-limits) | 100% free, no card; 1 QPS / 60 QPM / 1,000 QPD | None — higher rate tiers unlock by cumulative recharge ($10+ → 5 QPS) | `https://langsearch.com/api-keys` | Community `langsearch-mcp-server` |
| [You.com](https://you.com/pricing) | $100 credits at signup + keyless 100 queries/day via MCP free profile | PAYG Web Search $5/1k | `https://you.com/platform` | Hosted `api.you.com/mcp` (free profile works keyless) |
| [Linkup](https://docs.linkup.so/pages/documentation/platform/pricing) | $20 credit at signup (professional email), topped back to $20/mo for eligible accounts ≈ 4,000 searches | PAYG $0.005/search | `https://app.linkup.so/sign-up` | Not researched this session |
| [Jina AI](https://jina.ai/reader/) | 10M tokens one-time, no card (shared across Reader/Search/etc.); keyless Reader 20 RPM | Token top-ups; ~$0.05/1M tokens is third-party-reported, unverified | `https://jina.ai/api-dashboard` | Hosted `mcp.jina.ai` (snippet-level) |
| [Search1API](https://www.search1api.com/pricing) | 100 credits, no card, no expiry; keyless tier ~5 RPM IP-limited | Basic $19/mo = 25,000 credits | `https://app.s1.dev` | Docs mention an MCP server (snippet-level) |
| [Firecrawl](https://www.firecrawl.dev/pricing) | 1,000 credits/mo, no card; search costs 2 credits/10 results | Hobby $16/mo yearly = 5,000 credits | `https://www.firecrawl.dev/signin?view=signup` | Keyless MCP for search/scrape/parse (snippet-level) |

**No free tier (verified):** Perplexity Sonar API — PAYG only, payment method required ([docs](https://docs.perplexity.ai/docs/getting-started/pricing)) · Kagi API — $12/1k, only the consumer search trial is free ([pricing](https://kagi.com/api/pricing)).

---

## SERP / traditional search APIs

Programmatic Google/Bing-style results.

| API | Free tier | Cheapest paid | Signup | MCP server |
|---|---|---|---|---|
| [Serper](https://serper.dev/) | 2,500 queries one-time, no card | $50 = 50k credits ($1/1k), valid 6 months | `https://serper.dev` | Community `serper-search-mcp` |
| [Brave Search API](https://brave.com/search/api/) | $5 credits/mo ≈ 1,000 requests — **card + attribution required** | $5/1k requests | `https://api-dashboard.search.brave.com/register` | **Official** `@brave/brave-search-mcp-server` |
| [SerpApi](https://serpapi.com/pricing.md) | 250 searches/mo, recurring (50/hr) | $25/mo = 1,000 searches | `https://serpapi.com/users/sign_up` | Not researched this session |
| [HasData](https://hasdata.com/prices) | 1,000 credits/mo ≈ 100 Google SERP calls (10 credits each; recurrence conflict flagged below) | $49/mo = 200k credits | `https://app.hasdata.com/sign-up` | Not researched this session |
| [Scrappa](https://scrappa.co/) | 500 credits/mo, no card | PAYG from $0.30/1k | `https://scrappa.co/register` | Not researched this session |
| [Scale SERP](https://trajectdata.com/serp/scale-serp-api/pricing/) | 125 searches/mo, no card | $66/mo = 10,000 (annual) | `https://app.scaleserp.com/signup/10k` | Not researched this session |
| [SearchApi.io](https://www.searchapi.io/pricing) | 100 requests one-time, no card | $40/mo = 10,000 ($4/1k) | `https://www.searchapi.io/users/sign_up` | Not researched this session |
| [Zenserp](https://zenserp.com/pricing-plans/) | 50 searches/mo | $49.99/mo = 25,000 | `https://app.zenserp.com/register` | Not researched this session |
| [DataForSEO](https://dataforseo.com/apis/serp-api) | $1 credit, unlimited-duration trial | PAYG, **min deposit $50**; SERP $0.6/1k | `https://dataforseo.com/apis/serp-api` | Not researched this session |
| [Oxylabs SERP](https://oxylabs.io/products/scraper-api/serp) | One-time trial up to 2,000 results — no permanent free tier | $49/mo Micro | `https://dashboard.oxylabs.io` | Not researched this session |

**Dead:** Bing Search API · Google Custom Search JSON API (both in the warnings table above — do not wire).

---

## Self-hosted options

All free of keys and quotas; the real cost is running them and the fragility of scraping upstream engines.

| Project | What it is | API surface | License | Maintenance |
|---|---|---|---|---|
| [SearXNG](https://github.com/searxng/searxng) | Metasearch aggregator, 70+ engines — the incumbent (already deployed on the VPS) | Native JSON API (`/search?format=json`), own format | AGPL-3.0 | Very active — pushed 2026-09-03, 36.5k stars |
| [Searcharvester](https://github.com/vakovalskii/searcharvester) | Tavily-compatible layer over SearXNG + trafilatura | Tavily-compatible `POST /search`, `/extract`, `/research` | AGPL-3.0 | Most-adopted adapter — 258 stars, pushed 2026-04-27 |
| [OpenSERP](https://github.com/karust/openserp) | Browser-rendered SERP scraper for Google/Bing/Yandex/Baidu/DDG/Ecosia | Own REST (`GET /{engine}/search`), not Tavily | MIT | Mature — 1.3k stars, pushed 2026-07-22; CAPTCHA-prone by design |
| [4get](https://git.lolcat.ca/lolcat/4get) | PHP proxy metasearch with rotating per-scraper proxies | JSON API `/api/v1/{web,images,videos,news,music}` | AGPL-3.0 | Very active — last commit 2026-09-02; single maintainer on personal Gitea |
| [LibreY](https://github.com/Ahwxorg/LibreY) | PHP metasearch (Google/DDG/Brave/Ecosia/Yandex/Mojeek) | Own JSON (`api.php`) | AGPL-3.0 | Moderate — pushed 2026-06-10, 316 stars |
| [YaCy](https://github.com/yacy/yacy_search_server) | P2P search with its own crawler + index (Java/Solr) — no upstream scraping | Own JSON API | GPL-2.0+ | Active — pushed 2026-07-07, ~4k stars; heavy to run |
| [OrioSearch](https://github.com/vkfolio/orio-search) | Tavily-compatible layer over SearXNG + Redis | Tavily-compatible `/search`, `/extract` | **License discrepancy** — README says MIT, no LICENSE file in repo | Young — 42 stars, upstream quiet since 2026-06-07 |
| [WebSearchFree](https://github.com/drmikecrypto/WebSearchFree) | Keyless C++ binary, Tavily-shaped search+extract over DDG/Brave/Wikipedia | Tavily-shaped `/search`, `/extract` | MIT | Very new — 5 stars, created 2026-08-03; unproven |
| [SearchForge](https://github.com/divyanshu-iitian/SearchForge) | Intent-routed search (Wikipedia/GitHub/Crossref/HN + private SearXNG) | Own REST + built-in MCP server | MIT | New — 2 stars, v0.2.0 |
| [Whoogle](https://github.com/benbusby/whoogle-search) | Google proxy — **dead** | None (HTML only) | MIT | **Archived 2026-07-24** |

Brief finds worth knowing: [trawl](https://github.com/adityaparab/trawl) (Tavily wire-compatible, local dev), [tavily-open](https://github.com/jianjungki/tavily-open) (Tavily-like over SearXNG+Crawl4AI, 31 stars), [YagoSeek](https://github.com/D4rk4/yago) (Go YaCy node with Tavily-compatible API, alpha), [agent-search](https://github.com/brcrusoe72/agent-search) (FastAPI over SearXNG, 78 stars).

**Why the local engine failures matter here:** SearXNG's own limiter docs state that SearXNG is "classified as a bot" by upstream engines and "then receives a CAPTCHA or is blocked" ([docs](https://docs.searxng.org/admin/searx.limiter.html)); searx.space warns public instances get blocked by Google/Qwant/Bing/Startpage ([source](https://searx.space/)). Whoogle's death and SearchForge's decision to avoid public SearXNG instances corroborate the same fragility. Local test evidence: `SEARXNG-ENGINE-TEST-RESULTS.md`.

---

## MCP server coverage

How each candidate wires into an MCP-configured harness (stdio via `npx` unless noted).

| API | Official / Community | Package | Key env var | Run command |
|---|---|---|---|---|
| Exa | **Official** ([exa-labs](https://github.com/exa-labs/exa-mcp-server)) | [`exa-mcp-server`](https://www.npmjs.com/package/exa-mcp-server) | `EXA_API_KEY` | `npx -y exa-mcp-server` · remote `https://mcp.exa.ai/mcp` |
| Tavily | **Official** ([tavily-ai](https://github.com/tavily-ai/tavily-mcp)) | [`tavily-mcp`](https://www.npmjs.com/package/tavily-mcp) | `TAVILY_API_KEY` | `npx -y tavily-mcp@latest` · remote `https://mcp.tavily.com/mcp` |
| Brave | **Official** ([brave org](https://github.com/brave/brave-search-mcp-server)) | [`@brave/brave-search-mcp-server`](https://www.npmjs.com/package/@brave/brave-search-mcp-server) | `BRAVE_API_KEY` | `npx -y @brave/brave-search-mcp-server` |
| Serper | Community ([serper-search-mcp](https://github.com/smjahid012/serper-search-mcp-server)) | [`serper-search-mcp`](https://www.npmjs.com/package/serper-search-mcp) | `SERPER_API_KEY` | `npx -y serper-search-mcp` |
| LangSearch | Community ([langsearch-mcp-server](https://github.com/fusman60/langsearch-mcp-server)) | `langsearch-mcp-server` | `LANGSEARCH_API_KEY` | `npx -y langsearch-mcp-server` |
| SearXNG | Community, de-facto standard ([mcp-searxng](https://github.com/ihor-sokoliuk/mcp-searxng), in GitHub MCP Registry) | [`mcp-searxng`](https://www.npmjs.com/package/mcp-searxng) | `SEARXNG_URL` | `npx -y mcp-searxng` — **already configured in this harness** |
| OpenSERP | **Official** ([openserpapi](https://github.com/openserpapi/mcp)) | [`@openserp/mcp`](https://www.npmjs.com/package/@openserp/mcp) | `OPENSERP_API_KEY` (cloud) / `OPENSERP_BASE_URL` (self-host) | `npx -y @openserp/mcp` |
| Google CSE | Community only ([google-search-mcp](https://github.com/thejusdutt/google-search-mcp)) | `@thejusdutt/google-search-mcp` | `GOOGLE_API_KEY` + `GOOGLE_CX` | Not viable — API closed to new customers, dies 2027-01-01 |
| Bing | **None** — API retired 2025-08-11; legacy community servers target the dead API | — | — | Not viable |

Self-hosted adapters: OrioSearch and WebSearchFree bundle in-repo Python MCP servers (`ORIOSEARCH_BASE_URL`, `WSF_BASE_URL`); SearchForge has a built-in MCP server (`SEARCHFORGE_SEARXNG_URL`); Searcharvester is REST-only with a third-party MCP adapter ([MaYunFei/searcharvester-mcp](https://github.com/MaYunFei/searcharvester-mcp), `SEARCHARVESTER_INTERNAL_URL`).

**Package-name trap:** Tavily docs reference `@tavily/mcp`, but that npm package does not exist (registry 404, verified this session). The real package is `tavily-mcp`.

---

## Conflicts and unverified claims

Treat these as open questions, not facts:

- **Brave card billing** — Brave's FAQ still says the signup card "will not be charged"; third-party reporting (2026-06) says cards are billed once credits run out ([Brave FAQ](https://brave.com/search/api/) vs [implicator.ai](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/)).
- **Grounding with Bing price** — Microsoft's pricing page says $14/1k transactions; a Microsoft Q&A answer and ppc.land say $35/1k ([microsoft.com/bing/apis](https://www.microsoft.com/en-us/bing/apis) vs [MS Q&A](https://learn.microsoft.com/en-us/answers/questions/5568912/azure-sponsorship-subscription-request-bing-grounding)).
- **HasData free tier** — `/prices` says 1,000 credits every month; the product page says one-time ([hasdata.com/prices](https://hasdata.com/prices) vs [hasdata.com/apis/google-serp-api](https://hasdata.com/apis/google-serp-api)).
- **Google's replacement "Web Search Service"** — $15 CPM / $30k-month-minimum pricing comes from an HN-quoted Google email, not an official page ([HN](https://news.ycombinator.com/item?id=46730436)).
- **Jina AI token rate** (~$0.05/1M) and the Elastic acquisition (Oct 2025) — third-party only.
- **OrioSearch license** — README claims MIT; GitHub API finds no LICENSE file.
- **`mcp-searxng` version** — npm page shows 2.1.0 (updated 2026-08-25) while repo `package.json` says 1.15.0; direct npm read was 403-blocked.
- **Snippet-level only** (official page seen via search snippet, not fully read): You.com "no credit card" wording, Search1API keyless rate limits, Firecrawl keyless MCP, Jina hosted MCP.

---

## Key official sources

Load-bearing URLs behind the tables above (all fetched 2026-09-03):

1. https://exa.ai/pricing — Exa free tier + PAYG pricing
2. https://docs.tavily.com/documentation/api-credits — Tavily credits
3. https://docs.langsearch.com/limits/api-limits — LangSearch rate tiers
4. https://you.com/pricing — You.com credits + PAYG
5. https://serper.dev/ — Serper 2,500 free queries
6. https://brave.com/search/api/ + https://api-dashboard.search.brave.com/documentation/pricing — Brave restructure
7. https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement — Bing retirement
8. https://developers.google.com/custom-search/v1/overview + https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html — Google CSE shutdown
9. https://docs.searxng.org/admin/searx.limiter.html + https://searx.space/ — SearXNG engine-block reality
10. https://github.com/exa-labs/exa-mcp-server · https://github.com/tavily-ai/tavily-mcp · https://github.com/brave/brave-search-mcp-server · https://github.com/ihor-sokoliuk/mcp-searxng — MCP servers

Full per-claim source lists (150+ URLs) are in the raw researcher notes under `b0ttsagent/temp/free-websearch-apis/`.
