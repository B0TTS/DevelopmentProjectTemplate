import urllib.request, json

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": "model-benchmarks-probe/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)

# 1) HF total size
u = ("https://datasets-server.huggingface.co/rows"
     "?dataset=lmarena-ai%2Fleaderboard-dataset"
     "&config=text_style_control&split=latest&offset=0&length=1")
d = get(u)
print("HF num_rows_total:", d.get("num_rows_total"),
      "per_page:", d.get("num_rows_per_page"),
      "partial:", d.get("partial"))

# 2) find a model with populated benchmarks
d = get("https://openrouter.ai/api/v1/models")
data = d.get("data", d)
found = 0
for m in data:
    b = m.get("benchmarks")
    if isinstance(b, dict):
        print("\nmodel with benchmarks:", m.get("id"))
        print("benchmarks keys:", sorted(b.keys()))
        aa = b.get("artificial_analysis")
        if isinstance(aa, dict):
            print("artificial_analysis keys:", sorted(aa.keys()))
            print(json.dumps(aa, indent=1, default=str)[:900])
        da = b.get("design_arena")
        if isinstance(da, dict):
            print("design_arena keys:", sorted(da.keys()))
        found += 1
    if found >= 2:
        break

# 3) architecture shape (modality)
for m in data[:3]:
    a = m.get("architecture")
    print("\narch for", m.get("id"), "->", json.dumps(a, default=str)[:400] if a else a)
