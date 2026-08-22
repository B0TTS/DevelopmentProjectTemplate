import urllib.request, json, sys

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "model-benchmarks-probe/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)

print("=== OpenRouter /api/v1/models ===")
try:
    d = get("https://openrouter.ai/api/v1/models")
    data = d.get("data", d) if isinstance(d, dict) else d
    print("type:", type(d).__name__, "count:", len(data))
    m = data[0]
    print("top-level keys:", sorted(m.keys()))
    sub = {k: m.get(k) for k in
           ["id", "name", "context_length", "modality", "created",
            "reasoning", "pricing", "top_provider", "benchmarks"]}
    s = json.dumps(sub, indent=1, default=str)
    print(s[:1800])
except Exception as e:
    print("OPENROUTER FAILED:", type(e).__name__, str(e)[:300])

print("\n=== HF datasets-server /rows (length=1) ===")
try:
    u = ("https://datasets-server.huggingface.co/rows"
         "?dataset=lmarena-ai%2Fleaderboard-dataset"
         "&config=text_style_control&split=latest&offset=0&length=1")
    d = get(u)
    print("top keys:", list(d.keys()))
    rows = d.get("rows", [])
    print("rows returned:", len(rows))
    if rows:
        row = rows[0].get("row", rows[0])
        print("row keys:", sorted(row.keys()))
        print(json.dumps(row, indent=1, default=str)[:1500])
except Exception as e:
    print("HF /rows FAILED:", type(e).__name__, str(e)[:300])

print("\n=== HF datasets-server /filter (category=overall, length=2) ===")
try:
    u = ("https://datasets-server.huggingface.co/filter"
         "?dataset=lmarena-ai%2Fleaderboard-dataset"
         "&config=text_style_control&split=latest"
         "&where=%22category%22%3D%27overall%27&offset=0&length=2")
    d = get(u)
    print("top keys:", list(d.keys()))
    rows = d.get("rows", [])
    print("filtered rows returned:", len(rows))
    if rows:
        row = rows[0].get("row", rows[0])
        print("row keys:", sorted(row.keys()))
        cats = sorted({r.get("row", r).get("category") for r in rows})
        print("categories seen:", cats)
        print(json.dumps(row, indent=1, default=str)[:1200])
except Exception as e:
    print("HF /filter FAILED:", type(e).__name__, str(e)[:300])
