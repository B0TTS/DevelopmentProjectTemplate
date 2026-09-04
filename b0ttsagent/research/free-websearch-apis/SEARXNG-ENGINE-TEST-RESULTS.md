# SearXNG Local Instance — Engine Test Results

**Evidence origin:** untracked JSON files produced while testing the local SearXNG instance from the repo root in a prior session; moved into this folder on 2026-09-03 as the evidence base. Each file is a raw SearXNG JSON-API response (`/search` with `format=json`) for the query shown.
**Instance under test:** standalone SearXNG Docker container on the VPS (`searxng`, `0.0.0.0:8082->8080`), reached directly at `http://100.122.184.37:8082` — port 8082 is in the Tailscale ACL allow-list (per `b0ttsagent/NavGuides/VpsNavGuide.md`, refreshed 2026-08-16; that guide marks the standalone instance's VPS-side settings path as *unconfirmed* — it is distinct from the LobeChat `lobe-searxng` container, whose settings live at `/home/lobehub/searxng-settings.yml` per `VpsLobeHubNavGuide.md`).
**Companion doc:** `FREE-WEB-SEARCH-APIS.md` — the API comparison this evidence motivated.

---

## Verdict at a glance

- **6 engines returned results:** bing, mwmbl, sepiasearch, wiby, yandex, wikipedia
- **8 engines failed with explicit errors:** brave (rate limit), duckduckgo (CAPTCHA), startpage (CAPTCHA), qwant (access denied), yep (access denied), presearch (timeout), yacy (timeout), yahoo (HTTP protocol error)
- **2 engines returned zero results with no error reported:** google, mojeek
- **Default multi-engine queries returned 0 results** — the default engine set (brave + duckduckgo + startpage) fails as a group

## Per-file results

| File | Query | Results | Engine(s) that returned | Failure detail (`unresponsive_engines`) |
|---|---|---|---|---|
| `test_bing.json` | python | 10 | bing | — |
| `test_mwmbl.json` | python | 116 | mwmbl | — |
| `test_wiby.json` | python | 12 | wiby | — |
| `test_yandex.json` | python | 10 | yandex | — |
| `test_sepiasearch.json` | python | 10 | sepiasearch | — |
| `test_marginalia.json` | python | 1 | wikipedia | brave: too many requests · duckduckgo: CAPTCHA · startpage: CAPTCHA |
| `search_wiki.json` | python | 1 | wikipedia | — |
| `test_brave.json` | python | 0 | — | brave: Suspended: too many requests |
| `test_duckduckgo.json` | python | 0 | — | duckduckgo: CAPTCHA |
| `test_startpage.json` | python | 0 | — | startpage: Suspended: CAPTCHA |
| `test_qwant.json` | python | 0 | — | qwant: Suspended: access denied |
| `test_yep.json` | python | 0 | — | yep: Suspended: access denied |
| `test_presearch.json` | python | 0 | — | presearch: timeout |
| `test_yacy.json` | python | 0 | — | yacy: timeout |
| `test_yahoo.json` | python | 0 | — | yahoo: HTTP protocol error |
| `test_google.json` | python | 0 | — | *(none listed — silent zero)* |
| `test_mojeek.json` | python | 0 | — | *(none listed — silent zero)* |
| `search.json` | python programming | 0 | — | brave · duckduckgo · startpage (all three, as above) |
| `search2.json` | latest AI news | 0 | — | brave · duckduckgo · startpage (all three, as above) |
| `search_google.json` | python | 0 | — | *(silent zero)* |
| `search_google2.json` | python | 0 | — | *(silent zero)* |

## Failure taxonomy

| Failure mode | Engines | Meaning |
|---|---|---|
| Rate-limit suspension ("Suspended: too many requests") | brave | Upstream engine throttled the instance's IP |
| CAPTCHA ("CAPTCHA" / "Suspended: CAPTCHA") | duckduckgo, startpage | Upstream engine served a bot-check instead of results |
| Access denied ("Suspended: access denied") | qwant, yep | Upstream engine refused the instance outright |
| Timeout | presearch, yacy | Engine did not answer in time |
| HTTP protocol error | yahoo | Response was malformed/blocked at the protocol level |
| Silent zero (no error entry, empty results) | google, mojeek | Engine nominally responded but returned nothing — typical of silent blocking or a broken parser |

## Instance configuration (as captured in `searx_config.json`)

`searx_config.json` in this folder is a dump of the instance's `/config` endpoint:

- SearXNG version `2026.6.19+5c38d2fea`, 270 engines listed
- **`limiter.enabled: False`** — the instance's own bot-detection/rate-limiter is OFF, so the failures above are **upstream engines blocking the instance**, not local throttling
- `public_instance: False` (private instance), `instance_name: SearXNG` (default)

Where configuration lives:

| Layer | Location |
|---|---|
| Instance | VPS Docker container `searxng` (`0.0.0.0:8082->8080`), direct Tailscale access — `b0ttsagent/NavGuides/VpsNavGuide.md` |
| VPS-side settings file for the standalone instance | *Unconfirmed* per `VpsNavGuide.md` (no dedicated nav guide yet; do not SSH to find out) |
| Harness MCP wiring | `.opencode/opencode.json` → `mcp.searxng` (local, `npx -y mcp-searxng`, `SEARXNG_URL=http://100.122.184.37:8082`) |

## Interpretation (separate from the evidence above)

- The pattern — major scraped engines (brave, duckduckgo, startpage, google) failing while independent-index engines (bing, mwmbl, wiby, yandex, wikipedia) succeed — matches SearXNG's documented reality: SearXNG passes bot-like traffic through, gets classified as a bot, and "then receives a CAPTCHA or is blocked by the search engine (the origin)" ([SearXNG limiter docs](https://docs.searxng.org/admin/searx.limiter.html)); searx.space likewise warns instances "have a higher chance of being blocked by search providers such as Google, Qwant, Bing, Startpage" ([searx.space](https://searx.space/)).
- **Follow-up observation (2026-09-03, this session):** during the free-API research, all four researcher sub-agents reported this same instance reachable but returning **zero results for every query** via the `mcp-searxng` tool, forcing fallback to other search tools. The engine set may have degraded further since these tests — worth re-testing before relying on the instance. Raw notes: `b0ttsagent/temp/free-websearch-apis/r1`–`r4`.
- Consequence for API selection: a hosted AI-native API (Tavily/Exa/LangSearch class) or a keyless independent-index engine set is needed as the primary search path; the self-hosted instance works only for the engines that still tolerate it. See `FREE-WEB-SEARCH-APIS.md` for the comparison.

## Evidence manifest (files in this folder)

`searx_config.json` (instance `/config` dump) · `search.json`, `search2.json`, `search_google.json`, `search_google2.json`, `search_wiki.json` (multi-engine exploratory queries) · `test_bing.json`, `test_brave.json`, `test_duckduckgo.json`, `test_google.json`, `test_marginalia.json`, `test_mojeek.json`, `test_mwmbl.json`, `test_presearch.json`, `test_qwant.json`, `test_sepiasearch.json`, `test_startpage.json`, `test_wiby.json`, `test_yacy.json`, `test_yahoo.json`, `test_yandex.json`, `test_yep.json` (per-engine tests, query "python").
