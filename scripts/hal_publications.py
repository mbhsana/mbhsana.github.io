"""Generate _hal_list.md (conference and workshop papers) from HAL.

Runs automatically before each Quarto build (pre-render). Uses the idHAL
'sana-ben-hamida', so the homonym (ISET Gabès) is never included.
If HAL cannot be reached, the existing _hal_list.md is kept unchanged.
"""
import json
import pathlib
import sys
import urllib.parse
import urllib.request

IDHAL = "sana-ben-hamida"
OUT = pathlib.Path(__file__).resolve().parent.parent / "_hal_list.md"
DOC_TYPES = {"COMM", "POSTER"}  # conference papers; journals/books are curated by hand
FIELDS = ("title_s,authFullName_s,producedDateY_i,docType_s,conferenceTitle_s,"
          "bookTitle_s,doiId_s,halId_s")

url = ("https://api.archives-ouvertes.fr/search/?" + urllib.parse.urlencode({
    "q": f"authIdHal_s:{IDHAL}", "fl": FIELDS, "rows": 500,
    "sort": "producedDateY_i desc", "wt": "json"}))

try:
    with urllib.request.urlopen(url, timeout=30) as r:
        docs = json.load(r)["response"]["docs"]
except Exception as exc:  # network error: keep previous list
    print(f"[hal] HAL unreachable ({exc}); keeping existing {OUT.name}", file=sys.stderr)
    sys.exit(0)

docs = [d for d in docs if d.get("docType_s") in DOC_TYPES]
if not docs:
    print("[hal] no documents returned; keeping existing list", file=sys.stderr)
    sys.exit(0)


def authors(names):
    out = []
    for n in names:
        parts = n.split()
        short = n if len(parts) < 2 else f"{parts[0][0]}. {' '.join(parts[1:])}"
        out.append(f"**{short}**" if "Ben Hamida" in n else short)
    return ", ".join(out)


lines, year = [], None
for d in docs:
    y = d.get("producedDateY_i")
    if y != year:
        year = y
        lines.append(f"\n### {y}\n")
    venue = d.get("conferenceTitle_s") or d.get("bookTitle_s") or ""
    links = [f"[{d['halId_s']}](https://hal.science/{d['halId_s']})"]
    if d.get("doiId_s"):
        links.append(f"[doi](https://doi.org/{d['doiId_s']})")
    title = d["title_s"][0] if isinstance(d["title_s"], list) else d["title_s"]
    lines.append(f"- {authors(d.get('authFullName_s', []))}. {title}. *{venue}*, {y}. {' · '.join(links)}")

OUT.write_text("::: {.pubs}\n" + "\n".join(lines) + "\n:::\n", encoding="utf-8")
print(f"[hal] wrote {len(docs)} entries to {OUT.name}")
