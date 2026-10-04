"""Build ban-dich-tieng-viet.docx from the LaTeX translation (pandoc) and prepend a cover page."""
import copy, re, subprocess, tempfile, pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, Cm

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "ban-dich-tieng-viet.tex", ROOT / "ban-dich-tieng-viet.docx"
FONT = "Times New Roman"

def pandoc_body():
    s = SRC.read_text(encoding="utf-8")
    s = s.replace("\\input{cover.tex}", "")
    s = re.sub(r"\\title\{.*?\}\n\\author", "\\\\author", s, flags=re.S)
    s = re.sub(r"\\tag\{(\d+)\}", r"\\quad (\1)", s)  # pandoc cannot parse \tag
    tmp = pathlib.Path(tempfile.mkdtemp()) / "src.tex"
    tmp.write_text(s, encoding="utf-8")
    subprocess.run(["pandoc", str(tmp), "-f", "latex", "-o", str(OUT)], check=True)

def rule(p):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement("w:pBdr"); e = OxmlElement("w:bottom")
    for k, v in (("val", "single"), ("sz", "8"), ("space", "1"), ("color", "000000")): e.set(qn("w:" + k), v)
    b.append(e); pPr.append(b)

TEMPLATE = ROOT / "image/cover-template.docx"
TITLE = "CÁCH TIẾP CẬN CHỊU LỖI CHỦ ĐỘNG CHO ĐIỆN TOÁN ĐÁM MÂY DỰA TRÊN HỆ MỜ TAKAGI-SUGENO VÀ THUẬT TOÁN SIMULATED ANNEALING"
FILL = {"SINH VIÊN:": "SINH VIÊN: NÔNG VĂN TÌNH", "MSSV:": "MSSV: 8480101250028"}

def set_text(p, text):
    runs = [r for r in p.findall(qn("w:r")) if r.find(qn("w:t")) is not None]
    for r in runs[1:]: p.remove(r)
    t = runs[0].find(qn("w:t")); t.text = text
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")

def cover():
    """Splice the lecturer's cover template (image/cover-template.docx) in front of the body."""
    doc, tpl = Document(OUT), Document(TEMPLATE)
    body = doc.element.body
    first = body[0]
    tbody = tpl.element.body
    sect = tbody.find(qn("w:sectPr"))
    elems = [copy.deepcopy(e) for e in tbody if e.tag != qn("w:sectPr")]
    rid = doc.part.get_or_add_image(str(ROOT / "image/siu-logo.png"))[0]
    last = None
    for e in elems:
        for blip in e.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}blip"):
            blip.set(qn("r:embed"), rid)
        if e.tag != qn("w:p"): continue
        txt = "".join(t.text or "" for t in e.iter(qn("w:t")))
        s = txt.strip()
        if s.startswith("…"):
            set_text(e, TITLE)
            for c in e.iter(qn("w:color")): c.getparent().remove(c)  # template shows a red placeholder
            for sz in e.iter(qn("w:sz")): sz.set(qn("w:val"), "30")
            for sz in e.iter(qn("w:szCs")): sz.set(qn("w:val"), "30")
        elif s.startswith("SINH VIÊN:"): set_text(e, FILL["SINH VIÊN:"])
        elif s == "MSSV:": set_text(e, FILL["MSSV:"])
        elif s.startswith("LỚP:"): set_text(e, "LỚP: 25MCS2")
        last = e
    # the template's page border applies to the cover section only
    pPr = last.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr"); last.insert(0, pPr)
    pPr.append(copy.deepcopy(sect))
    ps = [e for e in elems if e.tag == qn("w:p")]
    gap = [e for e in ps[ps.index([x for x in ps if "HK2" in "".join(t.text or "" for t in x.iter(qn("w:t")))][0]) - 5:] [:5]]
    for e in gap[1:4]:
        if not "".join(t.text or "" for t in e.iter(qn("w:t"))).strip(): elems.remove(e)
    for e in elems: first.addprevious(e)
    doc.save(OUT)

if __name__ == "__main__":
    pandoc_body(); cover()
