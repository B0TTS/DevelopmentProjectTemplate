import json, pathlib, re
p=pathlib.Path(r"C:\Users\Jonah\DevelopmentProjectTemplate\b0ttsagent\temp\youtube-transcripts")
files=list(p.glob("*.json3"))
print([f.name for f in files if "Prankster" in f.name])
f=[x for x in files if "Prankster" in x.name][0]
data=json.loads(f.read_text(encoding="utf-8"))
named={"amp":"&","lt":"<","gt":">","quot":chr(34),"apos":"'" ,"nbsp":" "}
def unescape(t):
    t=re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), t)
    t=re.sub(r"&#x([0-9a-f]+);", lambda m: chr(int(m.group(1),16)), t, flags=re.I)
    t=re.sub(r"&([a-z]+);", lambda m: named.get(m.group(1).lower(), m.group(0)), t, flags=re.I)
    return t
lines=["".join(s.get("utf8","") for s in e.get("segs",[])) for e in data.get("events",[])]
lines=[l for l in lines if l.strip()]
text=unescape(" ".join(lines))
text=re.sub(r"\s+"," ",text).strip()
out=p / "airrack_prankster.txt"
out.write_text(text+"\n",encoding="utf-8")
print(len(text))
print(text[:8000])
