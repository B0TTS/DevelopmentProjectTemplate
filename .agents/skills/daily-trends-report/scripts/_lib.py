"""Shared stdlib helpers for the daily-trends-report scripts.

Every constant here is a locked decision documented in references/routing-rules.md:

- REPORT_TZ: fixed UTC-10 (Hawaii, no DST) is the canonical "today" and the
  base of the 7-day window. A fixed offset is used because the standard
  library's zoneinfo database is not available on this machine's Python.
- RECENCY_DAYS = 7: items older than 7 days appear nowhere.
- MAX_STILL_CIRCULATING = 10: Still circulating cap.
- MAX_MAIN_ITEMS = 5: a main section never exceeds 5 items.
- TRACKING_PARAMS: query params stripped from URL identity keys.

Do not change these constants without updating references/routing-rules.md
and re-running references/eval-fixtures.md.
"""

import re
from datetime import date, datetime, timedelta, timezone

REPORT_TZ = timezone(timedelta(hours=-10))  # HST, no DST
RECENCY_DAYS = 7
MAX_STILL_CIRCULATING = 10
MAX_MAIN_ITEMS = 5

MAIN_SECTIONS = ["AI trends", "SWE trends", "Productivity"]
STILL_SECTION = "Still circulating"
ALL_SECTIONS = MAIN_SECTIONS + [STILL_SECTION]

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "utm_id", "fbclid", "gclid", "gclsrc", "dclid", "msclkid", "twclid",
    "ref", "ref_src", "referrer", "source", "cmpid", "mc_cid", "mc_eid",
    "igshid", "srsltid", "vero_id", "yclid", "_hsenc", "_hsmi",
}

_URL_RE = re.compile(r"https?://[^\s)\]]+")
_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
_DASH_ROW_RE = re.compile(r"^[\s:\-|]+$")
_HEADER_COLS = {"Domain", "Headline", "Why it matters", "Date", "Link"}


def today_iso():
    """Canonical today (UTC-10) as YYYY-MM-DD."""
    return datetime.now(REPORT_TZ).date().isoformat()


def parse_date(s):
    """YYYY-MM-DD -> date, or None. Anything else is not a verifiable date."""
    if not s:
        return None
    try:
        return date.fromisoformat(str(s).strip())
    except ValueError:
        return None


def in_window(d, today):
    """True when d is between 7 days ago and today, inclusive."""
    return (today - timedelta(days=RECENCY_DAYS)) <= d <= today


def normalize_url(raw):
    """Identity URL key. Returns None when the input is not an http(s) URL.

    Normalization: lowercase scheme and host; strip www./m./mobile. host
    prefix; drop fragment; strip trailing slash; drop tracking query params
    (TRACKING_PARAMS). All other query params and the path are kept.
    """
    raw = str(raw or "").strip()
    if not re.match(r"^https?://", raw, re.I):
        return None
    scheme, rest = raw.split("://", 1)
    scheme = scheme.lower()
    rest = rest.split("#", 1)[0]  # drop fragment
    host, _, path = rest.partition("/")
    host = host.lower()
    for prefix in ("www.", "m.", "mobile."):
        if host.startswith(prefix):
            host = host[len(prefix):]
            break
    path, _, query = path.partition("?")
    if query:
        kept = [
            p for p in query.split("&")
            if p and p.split("=", 1)[0].lower() not in TRACKING_PARAMS
        ]
        if kept:
            path = path + "?" + "&".join(kept)
    path = path.rstrip("/")
    return scheme + "://" + host + ("/" + path if path else "")


def normalize_headline(s):
    """Identity headline key: lowercase, punctuation stripped, whitespace collapsed."""
    s = re.sub(r"[^a-z0-9]+", " ", str(s or "").lower())
    return re.sub(r"\s+", " ", s).strip()


def item_keys(url, headline):
    """Return (url_key, head_key) for an item."""
    return normalize_url(url), normalize_headline(headline)


def identity_key(url_key, head_key):
    """Canonical identity string for an item: url_key when present, else headline key."""
    if url_key:
        return url_key
    if head_key:
        return "headline:" + head_key
    return None


def find_streak(inv, url_key, head_key):
    """Look up a prior main-section item in inventory.json's streak maps.

    URL key wins (primary identity). Headline key is the fallback for
    different URLs that name the same story.
    """
    hits = inv.get("streak_hits") or {}
    hhits = inv.get("streak_headline_hits") or {}
    if url_key and url_key in hits:
        return hits[url_key]
    if head_key and head_key in hhits:
        return hhits[head_key]
    return None


def _extract_url(cell):
    m = re.search(r"\]\((https?://[^)]+)\)", cell or "")
    if m:
        return m.group(1)
    m = _URL_RE.search(cell or "")
    return m.group(0).rstrip(".,;:") if m else None


def _extract_date(cell):
    m = _DATE_RE.search(cell or "")
    return m.group(0) if m else None


def parse_report_md(text):
    """Parse a report.md into section item lists.

    Returns (sections, warnings) where sections is
    {"AI trends": [item], "SWE trends": [...], "Productivity": [...],
     "Still circulating": [...]} and each item is
    {headline, why, date, url, domain, section, url_key, head_key}.

    Table rows missing a YYYY-MM-DD date or a URL are skipped with a warning
    (they violate the report contract; the verify command turns those
    warnings into failures for today's report).
    """
    sections = {s: [] for s in ALL_SECTIONS}
    warnings = []
    current = None
    header = None
    for lineno, raw in enumerate(str(text).splitlines(), 1):
        line = raw.strip()
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            title = m.group(1).strip()
            current = title if title in ALL_SECTIONS else None
            header = None
            continue
        if not current or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            if _HEADER_COLS & set(cells):
                header = cells
            continue
        if all(_DASH_ROW_RE.match(c) for c in cells if c):
            continue  # separator row like |---|---|
        if len(cells) < len(header):
            cells += [""] * (len(header) - len(cells))
        row = dict(zip(header, cells[:len(header)]))
        headline = row.get("Headline", "")
        if not headline:
            warnings.append(f"line {lineno}: table row without Headline skipped")
            continue
        d = _extract_date(row.get("Date", ""))
        if not d:
            warnings.append(f"line {lineno}: item without YYYY-MM-DD date skipped ({headline})")
            continue
        url = _extract_url(row.get("Link", ""))
        if not url:
            warnings.append(f"line {lineno}: item without URL skipped ({headline})")
            continue
        url_key, head_key = item_keys(url, headline)
        sections[current].append({
            "headline": headline,
            "why": row.get("Why it matters", ""),
            "date": d,
            "url": url,
            "domain": row.get("Domain", ""),
            "section": current,
            "url_key": url_key,
            "head_key": head_key,
        })
    return sections, warnings
