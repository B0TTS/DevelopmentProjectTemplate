#!/usr/bin/env python3
"""Model benchmarks: fetch openrouter model list + lmarena-ai Chatbot Arena into one cache, then query it."""

import argparse
import datetime
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

USER_AGENT = "model-benchmarks/1.0"
TIMEOUT = 30  # seconds per request: bounded wait, keeps CLI responsive
ARENA_TIMEOUT = 60  # datasets-server pages are slower and rate-limited; allow a longer wait
ARENA_RETRIES = 5  # retries per arena page: 429/5xx are transient on the shared endpoint
ARENA_BACKOFF = 5.0  # initial retry delay in seconds, doubles each attempt
ARENA_RETRY_CODES = (429, 502, 503, 504)  # HTTP codes worth retrying; others fail fast
ARENA_PAGE_DELAY = 0.5  # pause between pages: be polite to the shared rate-limited endpoint
FRESH_SECONDS = 12 * 60 * 60  # 12h: query auto-refreshes when cache older than this
PAGE_SIZE = 100  # datasets-server max rows per call
OPENROUTER_URL = "https://openrouter.ai/api/v1/models"
ARENA_URL = ("https://datasets-server.huggingface.co/rows?dataset=lmarena-ai%2Fleaderboard-dataset"
             "&config=text_style_control&split=latest&offset={offset}&length={length}")

VENDOR_PREFIXES = ["openai", "anthropic", "google", "meta-llama", "mistralai", "deepseek",
                   "x-ai", "qwen", "cohere", "nvidia", "moonshotai", "ai21", "amazon"]

SKILL_DIR = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_CACHE = SKILL_DIR / "cache" / "cache.json"


def now_iso():
    return datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def http_json_retry(url, timeout):
    delay = ARENA_BACKOFF
    for attempt in range(ARENA_RETRIES):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.load(resp)
        except Exception as exc:
            if attempt == ARENA_RETRIES - 1:
                raise
            if isinstance(exc, urllib.error.HTTPError) and exc.code not in ARENA_RETRY_CODES:
                raise
            time.sleep(delay)
            delay *= 2


def errmsg(exc):
    if isinstance(exc, urllib.error.HTTPError):
        return "HTTP %s" % exc.code
    txt = str(exc).strip()
    return txt or exc.__class__.__name__


def canonical(name):
    s = (name or "").lower().strip()
    s = s.lstrip("~")
    s = re.sub(r":free$", "", s)
    for p in VENDOR_PREFIXES:
        if s.startswith(p + "/"):
            s = s[len(p) + 1:]
            break
    s = re.sub(r"(\d{8}|\d{4}-\d{2}-\d{2})$", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def _num(v):
    if v is None:
        return None
    if isinstance(v, str) and v.strip() in ("", "N/A"):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _int(v):
    if v is None:
        return None
    try:
        return int(round(float(v)))
    except (TypeError, ValueError):
        return None


def _price(v):
    if v is None:
        return None
    try:
        return round(float(v) * 1_000_000, 3)
    except (TypeError, ValueError):
        return None


def _date_from_unix(u):
    if not u:
        return None
    try:
        return datetime.datetime.fromtimestamp(u, tz=datetime.timezone.utc).date().isoformat()
    except (TypeError, ValueError, OSError):
        return None


def openrouter_records(models):
    out = {}
    for m in models or []:
        if not isinstance(m, dict) or not m.get("id"):
            continue
        oid = m["id"]
        c = canonical(oid)
        arch = m.get("architecture") or {}
        pricing = m.get("pricing") or {}
        reasoning = m.get("reasoning") or {}
        aa = (m.get("benchmarks") or {}).get("artificial_analysis") or {}
        vendor = oid.split("/", 1)[0].lstrip("~")
        out[c] = {
            "aliases": sorted({oid.lower(), (m.get("name") or "").lower()}),
            "creator": vendor or None,
            "context_window": m.get("context_length") or None,
            "modality": arch.get("modality") or None,
            "release_date": _date_from_unix(m.get("created")),
            "reasoning": {
                "supported": bool(reasoning),
                "efforts": list(reasoning.get("supported_efforts") or []),
                "default": reasoning.get("default_effort"),
            },
            "price": {
                "input_per_m": _price(pricing.get("prompt")),
                "output_per_m": _price(pricing.get("completion")),
                "cache_read_per_m": _price(pricing.get("input_cache_read")),
            },
            "indices": {
                "intelligence": _num(aa.get("intelligence_index")),
                "coding": _num(aa.get("coding_index")),
                "agentic": _num(aa.get("agentic_index")),
            },
        }
    return out


def arena_records(rows):
    out = {}
    for item in rows or []:
        row = item.get("row") or {}
        if row.get("category") != "overall":
            continue
        name = row.get("model_name")
        if not name:
            continue
        c = canonical(name)
        out[c] = {
            "aliases": sorted({name.lower()}),
            "organization": row.get("organization") or "",
            "arena": {
                "elo": _num(row.get("rating")),
                "elo_ci_lower": _num(row.get("rating_lower")),
                "elo_ci_upper": _num(row.get("rating_upper")),
                "votes": _int(row.get("vote_count")),
                "rank": _int(row.get("rank")),
                "category": row.get("category") or "",
                "publish_date": row.get("leaderboard_publish_date"),
            },
        }
    return out


def fetch_openrouter():
    try:
        data = http_json(OPENROUTER_URL)
        return openrouter_records(data.get("data") or []), None
    except Exception as exc:  # noqa: BLE001 - boundary catches all per-source
        return None, errmsg(exc)


def fetch_arena():
    try:
        first = http_json_retry(ARENA_URL.format(offset=0, length=PAGE_SIZE), ARENA_TIMEOUT)
        total = int(first.get("num_rows_total") or 0)
        rows = list(first.get("rows") or [])
        offset = PAGE_SIZE
        while offset < total:
            time.sleep(ARENA_PAGE_DELAY)
            page = http_json_retry(ARENA_URL.format(offset=offset, length=PAGE_SIZE), ARENA_TIMEOUT)
            rows.extend(page.get("rows") or [])
            offset += PAGE_SIZE
        return arena_records(rows), None
    except Exception as exc:  # noqa: BLE001 - boundary catches all per-source
        return None, errmsg(exc)


def read_cache(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, dict) and isinstance(data.get("models"), dict):
            return data
        return None
    except Exception:
        return None


def write_cache(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=True)
    tmp.replace(path)


def source_fetched_at(cache, name):
    for s in cache.get("sources") or []:
        if s.get("name") == name:
            return s.get("fetched_at")
    return None


def openrouter_fields_from_cache(models):
    out = {}
    for c, rec in models.items():
        out[c] = {
            "aliases": rec.get("aliases") or [],
            "creator": rec.get("creator"),
            "context_window": rec.get("context_window"),
            "modality": rec.get("modality"),
            "release_date": rec.get("release_date"),
            "reasoning": rec.get("reasoning"),
            "price": rec.get("price"),
            "indices": rec.get("indices"),
        }
    return out


def arena_fields_from_cache(models):
    out = {}
    for c, rec in models.items():
        out[c] = {
            "aliases": rec.get("aliases") or [],
            "organization": rec.get("creator") or "",
            "arena": rec.get("arena"),
        }
    return out


def merge(or_data, arena_data):
    or_data = or_data or {}
    arena_data = arena_data or {}
    merged = {}
    for c in sorted(set(or_data) | set(arena_data)):
        o = or_data.get(c)
        a = arena_data.get(c)
        aliases = set()
        if o:
            aliases.update(o.get("aliases") or [])
        if a:
            aliases.update(a.get("aliases") or [])
        creator = ""
        if o and o.get("creator"):
            creator = o["creator"]
        if a and not creator and a.get("organization"):
            creator = a["organization"]
        merged[c] = {
            "aliases": sorted(aliases),
            "creator": creator or None,
            "context_window": (o or {}).get("context_window") or None,
            "modality": (o or {}).get("modality") or None,
            "release_date": (o or {}).get("release_date") or None,
            "reasoning": (o or {}).get("reasoning") or {"supported": False, "efforts": [], "default": None},
            "price": (o or {}).get("price") or {"input_per_m": None, "output_per_m": None, "cache_read_per_m": None},
            "indices": (o or {}).get("indices") or {"intelligence": None, "coding": None, "agentic": None},
            "arena": (a or {}).get("arena") or {"elo": None, "elo_ci_lower": None, "elo_ci_upper": None,
                                                "votes": None, "rank": None, "category": "", "publish_date": None},
        }
    return merged


def run_fetch(cache_path):
    prior = read_cache(cache_path)
    now = now_iso()
    sources = []

    or_data, or_err = fetch_openrouter()
    if or_data is None:
        if prior:
            or_data = openrouter_fields_from_cache(prior.get("models") or {})
            fetched = source_fetched_at(prior, "openrouter") or now
            reused = True
        else:
            fetched = now
            reused = False
        sources.append({"name": "openrouter", "url": OPENROUTER_URL, "fetched_at": fetched,
                        "status": "failed", "error": or_err, "reused": reused})
    else:
        sources.append({"name": "openrouter", "url": OPENROUTER_URL, "fetched_at": now, "status": "ok"})

    arena_data, arena_err = fetch_arena()
    if arena_data is None:
        if prior:
            arena_data = arena_fields_from_cache(prior.get("models") or {})
            fetched = source_fetched_at(prior, "chatbot_arena") or now
            reused = True
        else:
            fetched = now
            reused = False
        sources.append({"name": "chatbot_arena", "url": ARENA_URL.format(offset=0, length=PAGE_SIZE),
                        "fetched_at": fetched, "status": "failed", "error": arena_err, "reused": reused})
    else:
        sources.append({"name": "chatbot_arena", "url": ARENA_URL.format(offset=0, length=PAGE_SIZE),
                        "fetched_at": now, "status": "ok"})

    ok = [s for s in sources if s["status"] == "ok"]
    if not ok and prior is None:
        return None, "all sources failed and no prior cache exists"

    # file-level fetched_at reflects the OLDEST data in the cache, so reused (failed)
    # sources keep their true age: the header stays honest and staleness re-triggers
    # a refresh instead of being masked by the current fetch time.
    fetched_at = min((s.get("fetched_at") or now) for s in sources)
    cache = {"fetched_at": fetched_at, "sources": sources, "models": merge(or_data, arena_data)}
    write_cache(cache_path, cache)
    return cache, None


def age_str(iso):
    if not iso:
        return "?"
    try:
        dt = datetime.datetime.fromisoformat(iso)
        ref = datetime.datetime.now(dt.tzinfo) if dt.tzinfo else datetime.datetime.now()
        secs = max(0, int((ref - dt).total_seconds()))
    except Exception:
        return "?"
    if secs < 60:
        return "%ss ago" % secs
    if secs < 3600:
        return "%sm ago" % (secs // 60)
    return "%sh ago" % (secs // 3600)


def arena_publish_date(cache):
    ds = [m["arena"]["publish_date"] for m in cache.get("models", {}).values()
          if (m.get("arena") or {}).get("publish_date")]
    return max(ds) if ds else None


def header_line(cache):
    by_name = {s.get("name"): s for s in cache.get("sources") or []}
    notes = []
    labels = []
    for key, label in (("openrouter", "openrouter.ai models list"), ("chatbot_arena", "lmarena-ai Chatbot Arena")):
        src = by_name.get(key)
        if src and src.get("status") == "ok":
            labels.append(label)
        elif src:
            labels.append(label)
            if src.get("reused"):
                notes.append("%s fetch failed, using cached data (%s)" % (
                    key.replace("_", " "), age_str(src.get("fetched_at"))))
            else:
                notes.append("%s fetch failed, no data" % key.replace("_", " "))
    line = "Data: " + " + ".join(labels) + " (fetched %s)" % age_str(cache.get("fetched_at"))
    pub = arena_publish_date(cache)
    if pub:
        line += "; Arena publish date %s" % pub
    if notes:
        line += " [%s]" % "; ".join(notes)
    return line


def resolve(models, query):
    q = (query or "").lower()
    if q in models:
        return [q]
    hits = []
    for c, rec in models.items():
        if q in c:
            hits.append(c)
        elif any(q in a for a in rec.get("aliases") or []):
            hits.append(c)
    return sorted(set(hits))


def err_exit(msg):
    sys.stderr.write(msg + "\n")
    sys.exit(1)


def fmt_num(x):
    if x is None:
        return "-"
    try:
        x = float(x)
    except (TypeError, ValueError):
        return "-"
    # treat values within 1e-9 of an integer as integers for display
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.1f" % x).rstrip("0").rstrip(".")


def fmt_price(x):
    if x is None:
        return "-"
    try:
        return "$" + ("%.3f" % round(float(x), 3)).rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return "-"


def fmt_ctx(x):
    if x is None:
        return "-"
    try:
        return format(int(x), ",")
    except (TypeError, ValueError):
        return "-"


def fmt_text(x):
    return str(x) if x else "-"


def fmt_ci(arena):
    elo, lo, hi = arena.get("elo"), arena.get("elo_ci_lower"), arena.get("elo_ci_upper")
    if elo is None:
        return "-"
    if lo is None and hi is None:
        return fmt_num(elo)
    return "%s (%s-%s)" % (fmt_num(elo), fmt_num(lo), fmt_num(hi))


def fmt_reasoning(rec):
    r = rec.get("reasoning") or {}
    if not r.get("supported"):
        return "not supported"
    bits = []
    if r.get("efforts"):
        bits.append("efforts: " + ", ".join(r["efforts"]))
    if r.get("default"):
        bits.append("default: " + r["default"])
    return "supported" + (": " + "; ".join(bits) if bits else "")


def price_line(rec):
    p = rec.get("price") or {}
    return "%s / %s / %s" % (fmt_price(p.get("input_per_m")), fmt_price(p.get("output_per_m")),
                             fmt_price(p.get("cache_read_per_m")))


def aa_line(rec):
    i = rec.get("indices") or {}
    return "%s / %s / %s" % (fmt_num(i.get("intelligence")), fmt_num(i.get("coding")), fmt_num(i.get("agentic")))


def cmd_top(cache, n):
    items = [(c, rec) for c, rec in cache["models"].items() if (rec.get("arena") or {}).get("rank") is not None]
    items.sort(key=lambda t: t[1]["arena"]["rank"])
    items = items[:n]
    print(header_line(cache))
    print()
    print("| Rank | Model | Creator | ELO (95% CI) | Votes |")
    print("|---|---|---|---|---|")
    for c, rec in items:
        a = rec["arena"]
        print("| %s | %s | %s | %s | %s |" % (fmt_num(a["rank"]), c, fmt_text(rec.get("creator")),
                                              fmt_ci(a), fmt_num(a.get("votes"))))


def print_disambiguation(models, query, hits):
    print("multiple models match '%s':" % query)
    for c in hits:
        print("  %s - %s" % (c, fmt_text(models[c].get("creator"))))


def cmd_model(cache, query):
    models = cache["models"]
    hits = resolve(models, query)
    if not hits:
        err_exit("no model matches '%s'" % query)
    if len(hits) > 1:
        print_disambiguation(models, query, hits)
        return
    c = hits[0]
    rec = models[c]
    a = rec.get("arena") or {}
    print(header_line(cache))
    print()
    print("| Field | Value |")
    print("|---|---|")
    rows = [
        ("Canonical name", c),
        ("Creator", fmt_text(rec.get("creator"))),
        ("Context window", fmt_ctx(rec.get("context_window"))),
        ("Modality", fmt_text(rec.get("modality"))),
        ("Released", fmt_text(rec.get("release_date"))),
        ("Reasoning", fmt_reasoning(rec)),
        ("Price in/out/cache-read $/M", price_line(rec)),
        ("AA intelligence/coding/agentic", aa_line(rec)),
        ("Arena ELO (95% CI)", fmt_ci(a)),
        ("Arena votes", fmt_num(a.get("votes"))),
        ("Arena rank", fmt_num(a.get("rank"))),
    ]
    for field, value in rows:
        print("| %s | %s |" % (field, value))


def cmd_compare(cache, names):
    models = cache["models"]
    resolved = []
    for name in names:
        hits = resolve(models, name)
        if not hits:
            err_exit("no model matches '%s'" % name)
        if len(hits) > 1:
            print_disambiguation(models, name, hits)
            return
        resolved.append(hits[0])
    print(header_line(cache))
    print()
    print("| Metric | " + " | ".join(resolved) + " |")
    print("|" + "---|" * (len(resolved) + 1))
    rows = [
        ("Price in $/M", lambda r: fmt_price(r["price"]["input_per_m"])),
        ("Price out $/M", lambda r: fmt_price(r["price"]["output_per_m"])),
        ("Cache read $/M", lambda r: fmt_price(r["price"]["cache_read_per_m"])),
        ("Context window", lambda r: fmt_ctx(r["context_window"])),
        ("Modality", lambda r: fmt_text(r["modality"])),
        ("Reasoning", lambda r: fmt_reasoning(r)),
        ("Released", lambda r: fmt_text(r["release_date"])),
        ("AA intelligence", lambda r: fmt_num(r["indices"]["intelligence"])),
        ("AA coding", lambda r: fmt_num(r["indices"]["coding"])),
        ("AA agentic", lambda r: fmt_num(r["indices"]["agentic"])),
        ("Arena ELO", lambda r: fmt_num(r["arena"]["elo"])),
        ("Arena ELO 95% CI", lambda r: fmt_ci(r["arena"])),
        ("Arena votes", lambda r: fmt_num(r["arena"]["votes"])),
    ]
    for label, fn in rows:
        print("| %s | %s |" % (label, " | ".join(fn(models[c]) for c in resolved)))


def cache_is_fresh(path, cache):
    # key the staleness check on the recorded fetched_at (the data's true age),
    # not file mtime: hand-editing the cache (supported per SKILL.md), git
    # checkouts, or copies would otherwise reset mtime and mask stale data.
    iso = (cache or {}).get("fetched_at")
    if iso:
        try:
            dt = datetime.datetime.fromisoformat(iso)
            ref = datetime.datetime.now(dt.tzinfo) if dt.tzinfo else datetime.datetime.now()
            return (ref - dt).total_seconds() < FRESH_SECONDS
        except (TypeError, ValueError):
            pass
    try:
        return (time.time() - path.stat().st_mtime) < FRESH_SECONDS
    except OSError:
        return False


def load_for_query(cache_path, no_refresh, force):
    cache = read_cache(cache_path)
    if no_refresh:
        if cache is None:
            err_exit("no cache at %s and --no-refresh given" % cache_path)
        return cache
    if force or cache is None or not cache_is_fresh(cache_path, cache):
        fresh, err = run_fetch(cache_path)
        if fresh is None:
            if cache is None:
                err_exit("refresh failed: %s" % err)
            sys.stderr.write("note: refresh failed (%s); using existing cache\n" % err)
            return cache
        cache = fresh
    return cache


def summary(cache):
    print("fetched_at: %s" % cache["fetched_at"])
    print("model_count: %d" % len(cache.get("models", {})))
    for s in cache.get("sources", []):
        if s.get("status") == "ok":
            print("%s: ok (%d via %s)" % (s["name"], len(cache.get("models", {})), s["url"]))
        else:
            print("%s: failed (%s)" % (s["name"], s.get("error")))
        print("  fetched_at: %s" % s.get("fetched_at"))


def main(argv=None):
    root = argparse.ArgumentParser(prog="model_benchmarks")
    root.add_argument("--cache", default=None,
                      help="cache JSON path (default: %s)" % DEFAULT_CACHE)
    subs = root.add_subparsers(dest="command")
    subs.add_parser("fetch", help="fetch sources and write cache")
    q = subs.add_parser("query", help="query cached models")
    group = q.add_mutually_exclusive_group(required=True)
    group.add_argument("--top", type=int, metavar="N", help="top N arena models by rank")
    group.add_argument("--model", metavar="NAME", help="show one model")
    group.add_argument("--compare", nargs="+", metavar="NAME", help="compare 2+ models")
    q.add_argument("--no-refresh", action="store_true", help="use cache as-is, never refresh")
    q.add_argument("--force", action="store_true", help="refresh before querying")
    for sub in (subs.choices["fetch"], q):
        sub.add_argument("--cache", default=argparse.SUPPRESS, help=argparse.SUPPRESS)

    args = root.parse_args(argv)
    cache_path = pathlib.Path(args.cache) if args.cache else DEFAULT_CACHE

    if args.command in (None, "fetch"):
        cache, err = run_fetch(cache_path)
        if cache is None:
            err_exit("fetch failed: %s" % err)
        summary(cache)
        return 0

    if args.command == "query":
        if args.top is not None and args.top < 1:
            root.error("--top must be a positive integer")
        if args.compare is not None and len(args.compare) < 2:
            root.error("--compare requires at least 2 model names")
        cache = load_for_query(cache_path, args.no_refresh, args.force)
        if args.top is not None:
            cmd_top(cache, args.top)
        elif args.model is not None:
            cmd_model(cache, args.model)
        else:
            cmd_compare(cache, args.compare)
        return 0

    root.error("unknown command: %s" % args.command)
    return 2


if __name__ == "__main__":
    sys.exit(main())
