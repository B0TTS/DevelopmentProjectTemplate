"""Extract the three fenced python blocks from eval-fixtures.md and save them
into this directory, relocating the fixture ROOT to this throwaway base."""
import re
from pathlib import Path

src = Path(".agents/skills/daily-trends-report/references/eval-fixtures.md").read_text(encoding="utf-8")
blocks = re.findall(r"```python\n(.*?)```", src, re.DOTALL)
assert len(blocks) == 3, f"expected 3 python blocks, got {len(blocks)}"

names = ["make-fixtures.py", "inject-s7.py", "check-s8.py"]
for name, body in zip(names, blocks):
    if name == "make-fixtures.py":
        body = body.replace(
            'ROOT = Path("b0ttsagent/temp/daily-trends-report-eval")',
            'ROOT = Path("b0ttsagent/temp/daily-trends-report-skill/validation")',
        )
    (Path(__file__).parent / name).write_text(body + "\n", encoding="utf-8")
    print("wrote", name, len(body.splitlines()), "lines")
