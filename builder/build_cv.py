"""Build TR and EN CVs (Typst source + DOCX) from one content file.

Usage:
    python builder/build_cv.py <candidate_dir> <out_dir>

<candidate_dir> must contain content.py (EN and TR dicts, same block order)
and may contain photo.jpg. Writes <out_dir>/<file>.typ and <out_dir>/<file>.docx.
Compile the .typ files with:  typst compile <file>.typ
(the rendercv Typst package is fetched automatically; install the
"Source Sans 3" font or pass --font-path).
"""
import importlib.util
import os
import shutil
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

spec = importlib.util.spec_from_file_location("content", os.path.join(SRC, "content.py"))
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)
EN, TR = content.EN, content.TR

PHOTO = os.path.join(SRC, "photo.jpg")
HAS_PHOTO = os.path.exists(PHOTO)
if HAS_PHOTO:
    shutil.copy(PHOTO, os.path.join(OUT, "photo.jpg"))


# ---------- parity check: both languages must have the same block structure ----------
def shape(cv):
    return [(b[0], len(b[3]) if b[0] == "entry" else 0) for b in cv["blocks"]]


assert shape(EN) == shape(TR), "EN and TR block structures differ"


# ---------- Typst ----------
def esc(s):
    for ch in "\\#$@*_<>`[]":
        s = s.replace(ch, "\\" + ch)
    return s


def typst(cv):
    pre = open(os.path.join(HERE, "preamble.typ"), encoding="utf-8").read()
    pre = pre.replace("__NAME__", cv["name"]).replace("__LANG__", cv["lang"])
    out = [pre]
    photo = 'image("photo.jpg", width: 2.6cm)' if HAS_PHOTO else "[]"
    out.append(f"""#grid(
  columns: (1fr, 2.6cm),
  column-gutter: 0.6cm,
  align: (left + horizon, right + top),
  [
    = {esc(cv["name"])}

    #headline([{esc(cv["headline"])}])

    #connections(
      [#connection-with-icon("location-dot")[{esc(cv["location"])}]],
      [#connection-with-icon("phone")[{esc(cv["phone"])}]],
      [#connection-with-icon("envelope")[{esc(cv.get("email", ""))}]],
    )
  ],
  {photo},
)
""")
    blocks = cv["blocks"]
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b[0] == "section":
            out.append(f"\n== {esc(b[1])}\n")
        elif b[0] == "para":
            out.append(f"\n{esc(b[1])}\n")
        elif b[0] == "labeled":
            out.append(f"\n#strong[{esc(b[1])}] {esc(b[2])}\n")
        elif b[0] == "entry":
            bullets = []
            while i + 1 < len(blocks) and blocks[i + 1][0] == "bullet":
                i += 1
                bullets.append(blocks[i][1])
            head = f"#strong[{esc(b[1])}]" + (f", {esc(b[2])}" if b[2] else "")
            body = "\n\n".join([f"    {head}"] + [f"    - {esc(x)}" for x in bullets])
            right = "\n\n".join(f"    {esc(x)}" for x in b[3])
            out.append(f"\n#regular-entry(\n  [\n{body}\n\n  ],\n  [\n{right}\n\n  ],\n)\n")
        i += 1
    path = os.path.join(OUT, cv["file"] + ".typ")
    open(path, "w", encoding="utf-8", newline="\n").write("".join(out))
    return path


# ---------- DOCX ----------
NAVY, GREY, FONT = RGBColor(18, 38, 74), RGBColor(60, 70, 90), "Calibri"


def docx(cv):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(1.3), Cm(1.2)
    sec.left_margin = sec.right_margin = Cm(1.8)
    st = doc.styles["Normal"]
    st.font.name, st.font.size = FONT, Pt(10)
    st.font.color.rgb = RGBColor(25, 28, 36)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    st.paragraph_format.space_after = Pt(0)
    st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.line_spacing = 1.08
    doc.styles["List Bullet"].font.name = FONT
    doc.styles["List Bullet"].font.size = Pt(10)
    rpr = st.element.get_or_add_rPr()
    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), "tr-TR" if cv["lang"] == "tr" else "en-US")
    rpr.append(lang)

    def bottom_border(p):
        pPr = p._p.get_or_add_pPr()
        bdr, e = OxmlElement("w:pBdr"), OxmlElement("w:bottom")
        for k, v in (("w:val", "single"), ("w:sz", "4"), ("w:space", "1"), ("w:color", "12264A")):
            e.set(qn(k), v)
        bdr.append(e)
        pPr.append(bdr)

    t = doc.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    left, right = t.rows[0].cells
    left.width, right.width = Cm(14.6), Cm(2.8)
    p = left.paragraphs[0]
    r = p.add_run(cv["name"])
    r.bold, r.font.size, r.font.color.rgb = True, Pt(24), NAVY
    p = left.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    r = p.add_run(cv["headline"])
    r.font.size, r.font.color.rgb = Pt(10.5), GREY
    p = left.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    contact = "   ·   ".join(x for x in (cv["location"], cv["phone"], cv.get("email", "")) if x)
    r = p.add_run(contact)
    r.font.size, r.font.color.rgb = Pt(9.5), GREY
    if HAS_PHOTO:
        pp = right.paragraphs[0]
        pp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        pp.add_run().add_picture(PHOTO, width=Cm(2.6))

    blocks = cv["blocks"]
    for idx, b in enumerate(blocks):
        nxt = blocks[idx + 1][0] if idx + 1 < len(blocks) else None
        if b[0] == "section":
            p = doc.add_paragraph()
            p.paragraph_format.space_before, p.paragraph_format.space_after = Pt(8), Pt(3)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(b[1])
            r.bold, r.font.size, r.font.color.rgb = True, Pt(12), NAVY
            bottom_border(p)
        elif b[0] == "entry":
            et = doc.add_table(rows=1, cols=2)
            et.autofit = False
            lc, rc = et.rows[0].cells
            lc.width, rc.width = Cm(13.4), Cm(4.0)
            p = lc.paragraphs[0]
            p.paragraph_format.space_before = Pt(4)
            p.add_run(b[1]).bold = True
            if b[2]:
                p.add_run(", " + b[2])
            for k, line in enumerate(b[3]):
                q = rc.paragraphs[0] if k == 0 else rc.add_paragraph()
                q.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                if k == 0:
                    q.paragraph_format.space_before = Pt(4)
                q.add_run(line)
            for c in (lc, rc):
                for q in c.paragraphs:
                    q.paragraph_format.keep_with_next = nxt == "bullet"
        elif b[0] == "bullet":
            p = doc.add_paragraph(b[1], style="List Bullet")
            p.paragraph_format.left_indent = Cm(0.55)
            p.paragraph_format.first_line_indent = Cm(-0.35)
            p.paragraph_format.keep_with_next = nxt == "bullet"
        elif b[0] in ("para", "labeled"):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(3)
            if b[0] == "labeled":
                p.add_run(b[1] + " ").bold = True
                p.add_run(b[2])
            else:
                p.add_run(b[1])
    doc.core_properties.title = f'{cv["name"]} - CV'
    doc.core_properties.author = cv["name"]
    path = os.path.join(OUT, cv["file"] + ".docx")
    doc.save(path)
    return path


for cv in (EN, TR):
    print(typst(cv))
    print(docx(cv))
