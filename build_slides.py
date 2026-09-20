#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh file Chapter11_Vietnamese_Presentation.pptx
Nguồn: chapters/chapter11_cloud_security.tex (main.pdf) + slides/chapter11.tex (chapter11.pdf)
"""
import copy
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR

# ----------------------------------------------------------------- palette
NAVY   = RGBColor.from_string("0E2D4E")
NAVY2  = RGBColor.from_string("173F68")
BLUE   = RGBColor.from_string("1F6FB2")
BLUEL  = RGBColor.from_string("5D9BD3")
SKY    = RGBColor.from_string("EAF2F9")
SKY2   = RGBColor.from_string("F5F9FC")
BORDER = RGBColor.from_string("C3D8EA")
TEXT   = RGBColor.from_string("2B3A47")
MUTED  = RGBColor.from_string("64788A")
WHITE  = RGBColor.from_string("FFFFFF")
RED    = RGBColor.from_string("B8342A")
REDBG  = RGBColor.from_string("FBEDEB")
REDBD  = RGBColor.from_string("EEBDB7")
GREEN  = RGBColor.from_string("1B7A57")
GRNBG  = RGBColor.from_string("E9F5F0")
GRNBD  = RGBColor.from_string("B3DCCB")
AMB    = RGBColor.from_string("A86A00")
AMBBG  = RGBColor.from_string("FDF4E4")
AMBBD  = RGBColor.from_string("EBD2A3")

FONT = "Arial"

SW, SH = 13.333, 7.5           # inch
ML, MR = 0.62, 0.62            # lề trái / phải
CW = SW - ML - MR              # 12.093 in
BODY_TOP = 1.40
BODY_BOT = 7.02

prs = Presentation()
prs.slide_width = Inches(SW)
prs.slide_height = Inches(SH)
BLANK = prs.slide_layouts[6]

warnings = []

# ----------------------------------------------------------------- helpers
def new_slide():
    return prs.slides.add_slide(BLANK)


def noshadow(shape):
    try:
        shape.shadow.inherit = False
    except Exception:
        pass


def rect(slide, x, y, w, h, fill=None, line=None, lw=1.0,
         shape=MSO_SHAPE.ROUNDED_RECTANGLE, adj=None):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    noshadow(s)
    if adj is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            s.adjustments[0] = adj
        except Exception:
            pass
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(lw)
    s.text_frame.word_wrap = True
    s.text_frame.text = ""
    return s


def txbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    return tf


def rich(p, text, size, color, bold=False, italic=False,
         hl=None, hl_bold=True, font=FONT, space_after=0, space_before=0,
         align=PP_ALIGN.LEFT, line_spacing=1.15):
    """`**...**` -> đoạn được làm nổi bật (đậm + màu hl)."""
    p.alignment = align
    p.line_spacing = line_spacing
    p.space_after = Pt(space_after)
    p.space_before = Pt(space_before)
    hl = hl if hl is not None else color
    for i, part in enumerate(text.split("**")):
        if part == "":
            continue
        r = p.add_run()
        r.text = part
        f = r.font
        f.name = font
        f.size = Pt(size)
        strong = (i % 2 == 1)
        f.bold = bold or (strong and hl_bold)
        f.italic = italic
        f.color.rgb = hl if strong else color
    return p


def para(tf, first=False):
    return tf.paragraphs[0] if (first and not tf.paragraphs[0].runs) else tf.add_paragraph()


def textblock(slide, x, y, w, lines, size=12, color=TEXT, hl=NAVY, gap=6,
              line_spacing=1.18, align=PP_ALIGN.LEFT, italic=False, bold=False,
              anchor=MSO_ANCHOR.TOP, h=None):
    """lines: list[str] (đã hỗ trợ **nổi bật**)."""
    est = est_height(lines, w, size, gap, line_spacing)
    tf = txbox(slide, x, y, w, h if h else est, anchor=anchor)
    for i, ln in enumerate(lines):
        p = para(tf, first=(i == 0))
        rich(p, ln, size, color, hl=hl, align=align, italic=italic, bold=bold,
             space_after=gap if i < len(lines) - 1 else 0,
             line_spacing=line_spacing)
    return tf, est


CHAR_W = 0.495   # hệ số bề rộng ký tự trung bình của Arial


def n_lines(text, w_in, size):
    plain = text.replace("**", "")
    cpl = max(8, int(w_in * 72.0 / (size * CHAR_W)))
    # ước lượng theo từ
    words, line, cnt = plain.split(), 0, 1
    for wd in words:
        add = len(wd) + (1 if line else 0)
        if line + add > cpl:
            cnt += 1
            line = len(wd)
        else:
            line += add
    return cnt


def est_height(lines, w_in, size, gap, line_spacing=1.18):
    total = 0.0
    for ln in lines:
        total += n_lines(ln, w_in, size) * size * line_spacing / 72.0
    total += gap * (len(lines) - 1) / 72.0
    return total + 0.04


def bullets(slide, x, y, w, items, size=12, color=TEXT, hl=NAVY, gap=8,
            mark="▪", mark_color=BLUE, indent=0.22, line_spacing=1.16):
    """Mỗi item một dòng bullet; trả về chiều cao thực dùng."""
    cur = y
    for it in items:
        mtf = txbox(slide, x, cur - 0.005, indent, 0.3)
        rich(mtf.paragraphs[0], mark, size, mark_color, bold=True, line_spacing=line_spacing)
        h = est_height([it], w - indent, size, 0, line_spacing)
        tf = txbox(slide, x + indent, cur, w - indent, h)
        rich(tf.paragraphs[0], it, size, color, hl=hl, line_spacing=line_spacing)
        cur += h + gap / 72.0
    return cur - y - gap / 72.0


def numbers(slide, x, y, w, items, size=12, color=TEXT, hl=NAVY, gap=9,
            circ=0.26, chip_fill=BLUE, chip_text=WHITE, line_spacing=1.16,
            start=1):
    cur = y
    for i, it in enumerate(items, start):
        c = rect(slide, x, cur + 0.02, circ, circ, fill=chip_fill, shape=MSO_SHAPE.OVAL)
        tf = c.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        rich(tf.paragraphs[0], str(i), size - 1.5, chip_text, bold=True,
             align=PP_ALIGN.CENTER, line_spacing=1.0)
        ind = circ + 0.16
        h = est_height([it], w - ind, size, 0, line_spacing)
        t = txbox(slide, x + ind, cur, w - ind, h)
        rich(t.paragraphs[0], it, size, color, hl=hl, line_spacing=line_spacing)
        cur += max(h, circ + 0.04) + gap / 72.0
    return cur - y - gap / 72.0


def card(slide, x, y, w, h, heading, lines, fill=SKY, border=BORDER,
         head_color=NAVY, body_color=TEXT, hl=BLUE, head_size=13, body_size=11,
         bullet=False, gap=5, pad=0.18, name=""):
    rect(slide, x, y, w, h, fill=fill, line=border, lw=1.0, adj=0.055)
    cur = y + pad
    if heading:
        ht = est_height([heading], w - 2 * pad, head_size, 0, 1.1)
        tf = txbox(slide, x + pad, cur, w - 2 * pad, ht)
        rich(tf.paragraphs[0], heading, head_size, head_color, bold=True, line_spacing=1.1)
        cur += ht + 0.09
    if lines:
        if bullet:
            used = bullets(slide, x + pad, cur, w - 2 * pad, lines, size=body_size,
                           color=body_color, hl=hl, gap=gap, mark="•",
                           mark_color=head_color, indent=0.15)
        else:
            _, used = textblock(slide, x + pad, cur, w - 2 * pad, lines,
                                size=body_size, color=body_color, hl=hl, gap=gap)
        cur += used
    over = cur + pad - (y + h)
    if over > 0.02:
        warnings.append(f"TRÀN {over:.2f}in trong card '{name or heading[:28]}'")
    return cur + pad


def head(slide, kicker, title, n=None, title_size=25):
    rect(slide, ML, 0.44, 0.085, 0.62, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
    ty = 0.40
    if kicker:
        tf = txbox(slide, ML + 0.22, 0.36, CW - 0.3, 0.24)
        rich(tf.paragraphs[0], kicker.upper(), 11, BLUE, bold=True, line_spacing=1.0)
        ty = 0.61
    tf = txbox(slide, ML + 0.22, ty, CW - 0.3, 0.5)
    rich(tf.paragraphs[0], title, title_size, NAVY, bold=True, line_spacing=1.0)
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(ML), Inches(1.22),
                                    Inches(SW - MR), Inches(1.22))
    ln.line.color.rgb = BORDER
    ln.line.width = Pt(1.0)


def footer(slide, idx):
    tf = txbox(slide, ML, 7.12, 7.0, 0.24)
    rich(tf.paragraphs[0], "Chương 11 · Bảo mật đám mây", 9, MUTED, line_spacing=1.0)
    tf = txbox(slide, SW - MR - 1.2, 7.12, 1.2, 0.24)
    rich(tf.paragraphs[0], str(idx), 9, MUTED, align=PP_ALIGN.RIGHT, line_spacing=1.0)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def arrow(slide, x, y, w=0.26, h=0.16, color=BLUEL):
    a = rect(slide, x, y, w, h, fill=color, shape=MSO_SHAPE.RIGHT_ARROW)
    return a


def flow(slide, x, y, w, h, items, gap=0.34, fill=SKY, border=BLUEL,
         color=NAVY, size=11, last_fill=None, last_border=None, last_color=None,
         arrow_color=BLUEL):
    """Chuỗi hộp nối bằng mũi tên, dàn đều trong bề rộng w."""
    n = len(items)
    bw = (w - gap * (n - 1)) / n
    for i, it in enumerate(items):
        bx = x + i * (bw + gap)
        f, b, c = fill, border, color
        if i == n - 1 and last_fill is not None:
            f, b, c = last_fill, last_border or border, last_color or color
        s = rect(slide, bx, y, bw, h, fill=f, line=b, lw=1.0, adj=0.09)
        tf = s.text_frame
        tf.margin_left = tf.margin_right = Inches(0.06)
        tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for j, ln in enumerate(it.split("|")):
            p = para(tf, first=(j == 0))
            rich(p, ln, size if j == 0 else size - 1.5,
                 c if j == 0 else MUTED, bold=(j == 0),
                 align=PP_ALIGN.CENTER, line_spacing=1.08,
                 space_before=2 if j else 0)
        if i < n - 1:
            arrow(slide, bx + bw + (gap - 0.26) / 2, y + h / 2 - 0.08,
                  color=arrow_color)
    return bw


def divider(slide, num, title, items):
    bg = rect(slide, 0, 0, SW, SH, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
    rect(slide, 0, 0, SW, 0.09, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
    # khối trang trí
    rect(slide, SW - 3.6, -1.3, 4.6, 4.6, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    rect(slide, SW - 2.2, 4.4, 3.6, 3.6, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    tf = txbox(slide, 1.15, 2.35, 7.6, 0.30)
    rich(tf.paragraphs[0], num, 15, BLUEL, bold=True, line_spacing=1.0)
    tf = txbox(slide, 1.15, 2.72, 8.6, 1.1)
    rich(tf.paragraphs[0], title, 36, WHITE, bold=True, line_spacing=1.05)
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.15), Inches(4.12),
                                    Inches(3.0), Inches(4.12))
    ln.line.color.rgb = BLUE
    ln.line.width = Pt(2.5)
    y = 4.45
    for it in items:
        t = txbox(slide, 1.15, y, 8.6, 0.3)
        rich(t.paragraphs[0], "— " + it, 13, RGBColor.from_string("BDD3E6"), line_spacing=1.0)
        y += 0.34


# ================================================================= SLIDE 1
s = new_slide()
rect(s, 0, 0, SW, SH, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
rect(s, SW - 4.3, -1.7, 5.6, 5.6, fill=NAVY2, shape=MSO_SHAPE.OVAL)
rect(s, SW - 2.6, 4.2, 4.4, 4.4, fill=NAVY2, shape=MSO_SHAPE.OVAL)
rect(s, 0, 0, 0.14, SH, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
tf = txbox(s, 1.15, 1.95, 9.0, 0.4)
rich(tf.paragraphs[0], "CHƯƠNG 11", 18, BLUEL, bold=True, line_spacing=1.0)
tf = txbox(s, 1.15, 2.45, 10.0, 0.85)
rich(tf.paragraphs[0], "BẢO MẬT ĐÁM MÂY", 52, WHITE, bold=True, line_spacing=1.0)
tf = txbox(s, 1.15, 3.62, 10.0, 0.45)
rich(tf.paragraphs[0], "Cloud Security", 21, BLUEL, italic=True, line_spacing=1.0)
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.15), Inches(4.35),
                            Inches(3.4), Inches(4.35))
ln.line.color.rgb = BLUE
ln.line.width = Pt(3)
tf = txbox(s, 1.15, 4.70, 9.5, 1.0)
rich(tf.paragraphs[0], "Dữ liệu · Mã hóa · Hạ tầng · PaaS · SaaS · Máy chủ ảo · Kiểm soát bảo mật",
     14, RGBColor.from_string("BDD3E6"), line_spacing=1.2)
p = tf.add_paragraph()
rich(p, "Nguồn: Sunilkumar S. Manvi & Gopal Krishna Shyam, “Cloud Computing: Concepts and Technologies”, CRC Press, 2021 — tr. 205–227",
     11, RGBColor.from_string("8FB2CE"), line_spacing=1.25, space_before=10)
notes(s, """
Xin chào thầy/cô và các bạn. Hôm nay nhóm mình trình bày Chương 11 của giáo trình
"Cloud Computing: Concepts and Technologies" của Manvi và Shyam, chủ đề Bảo mật đám mây.
Đây là chương khép lại phần kiến trúc và dịch vụ, trả lời câu hỏi: khi ta đưa dữ liệu và
ứng dụng lên Đám mây thì rủi ro nằm ở đâu và ta bảo vệ bằng cách nào.
Bài gồm bảy mục, đi từ bảo mật dữ liệu, kỹ thuật mã hóa, hạ tầng, rồi tới từng mô hình
dịch vụ PaaS, SaaS, máy chủ ảo và cuối cùng là các biện pháp kiểm soát.
Mình bắt đầu với mục tiêu bài học.
""")

# ================================================================= SLIDE 2
s = new_slide()
head(s, "Learning Objectives", "Mục tiêu bài học")
cards = [
    ("Đánh giá", "Đánh giá **bảo mật dữ liệu** trong Đám mây: dữ liệu đang truyền, siêu dữ liệu và các mối quan ngại chính."),
    ("Mô tả", "Mô tả **quản lý bảo mật** trong Đám mây: hạ tầng, vùng tin cậy, kiểm soát truy cập và các biện pháp kiểm soát."),
    ("So sánh", "So sánh và đối chiếu bảo mật **IaaS, PaaS, SaaS** trong các triển khai Đám mây."),
]
cw = (CW - 2 * 0.36) / 3
for i, (h_, b) in enumerate(cards):
    x = ML + i * (cw + 0.36)
    rect(s, x, 1.75, cw, 2.35, fill=SKY, line=BORDER, adj=0.05)
    c = rect(s, x + 0.28, 1.52, 0.56, 0.56, fill=BLUE, shape=MSO_SHAPE.OVAL)
    ctf = c.text_frame
    ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
    ctf.margin_left = ctf.margin_right = 0
    rich(ctf.paragraphs[0], str(i + 1), 20, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    tfx = txbox(s, x + 0.28, 2.30, cw - 0.56, 0.4)
    rich(tfx.paragraphs[0], h_, 16, NAVY, bold=True, line_spacing=1.0)
    textblock(s, x + 0.28, 2.78, cw - 0.56, [b], size=12, color=TEXT, hl=BLUE)
card(s, ML, 4.42, CW, 1.55,
     "Bảo mật đám mây (Cloud security) là gì?",
     ["Là tập hợp rộng lớn các **phương pháp tiếp cận, công nghệ và biện pháp kiểm soát** được triển khai nhằm bảo đảm thông tin, ứng dụng và hạ tầng liên quan của điện toán đám mây.",
      "Là **lĩnh vực con** của bảo mật máy tính (computer security), bảo mật mạng (network security) và rộng hơn là bảo mật dữ liệu (data security)."],
     fill=SKY2, border=BORDER, head_size=14, body_size=12, name="def")
footer(s, 2)
notes(s, """
Sau chương này, chúng ta cần làm được ba việc.
Một là đánh giá được bảo mật dữ liệu trong Đám mây — dữ liệu nằm yên và dữ liệu đang di chuyển.
Hai là mô tả được cách quản lý bảo mật, tức là tổ chức phòng thủ ở mức hạ tầng và kiểm soát truy cập.
Ba là so sánh được ba mô hình dịch vụ IaaS, PaaS, SaaS khác nhau ở chỗ nào về trách nhiệm bảo mật.
Định nghĩa ở dưới rất đáng nhớ: bảo mật đám mây không phải một công nghệ đơn lẻ, mà là một tập hợp
phương pháp, công nghệ và biện pháp kiểm soát. Nó là lĩnh vực con của bảo mật máy tính, bảo mật mạng
và bảo mật dữ liệu — nghĩa là mọi kiến thức an toàn thông tin cũ vẫn còn giá trị.
""")

# ================================================================= SLIDE 3
s = new_slide()
head(s, "Outline", "Nội dung trình bày")
secs = [
    ("11.1", "Bảo mật dữ liệu", "Dữ liệu đang truyền, siêu dữ liệu, các mối quan ngại"),
    ("11.2", "Kỹ thuật mã hóa trong Đám mây", "ABE · FHE · SE · WPS"),
    ("11.3", "Bảo mật hạ tầng", "Cấp độ mạng và lược đồ Vùng tin cậy (TZ)"),
    ("11.4", "Bảo mật ứng dụng PaaS", "Kiểm soát truy cập, gia cố OS, SSO"),
    ("11.5", "Bảo mật ứng dụng SaaS", "Lược đồ FHE và kiểm soát truy cập"),
    ("11.6", "Bảo mật máy chủ ảo", "Cấu hình an toàn theo mặc định"),
    ("11.7", "Các biện pháp kiểm soát bảo mật", "Răn đe · Phòng ngừa · Phát hiện · Khắc phục"),
]
colw = (CW - 0.40) / 2
for i, (num, t, sub) in enumerate(secs):
    col, row = i % 2, i // 2
    x = ML + col * (colw + 0.40)
    y = 1.55 + row * 1.10
    rect(s, x, y, colw, 0.92, fill=SKY2, line=BORDER, adj=0.07)
    rect(s, x, y, 0.075, 0.92, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
    tfn = txbox(s, x + 0.24, y + 0.16, 0.9, 0.5)
    rich(tfn.paragraphs[0], num, 17, BLUE, bold=True, line_spacing=1.0)
    tft = txbox(s, x + 1.12, y + 0.14, colw - 1.3, 0.34)
    rich(tft.paragraphs[0], t, 14, NAVY, bold=True, line_spacing=1.0)
    tfs = txbox(s, x + 1.12, y + 0.50, colw - 1.3, 0.3)
    rich(tfs.paragraphs[0], sub, 10.5, MUTED, line_spacing=1.0)
footer(s, 3)
notes(s, """
Đây là bản đồ của bài. Bảy mục chia làm ba khối lớn.
Khối một, mục 11.1 và 11.2, nói về dữ liệu và cách mã hóa dữ liệu.
Khối hai, mục 11.3, nói về hạ tầng và mạng.
Khối ba, từ 11.4 đến 11.7, đi theo từng mô hình dịch vụ: PaaS, SaaS, máy chủ ảo trên IaaS,
rồi tổng kết bằng bốn loại biện pháp kiểm soát.
Các bạn để ý mạch này: dữ liệu — mã hóa — hạ tầng — ứng dụng — kiểm soát. Đi từ trong ra ngoài.
""")

# ================================================================= SLIDE 4
s = new_slide()
head(s, "Tổng quan", "Bảo mật đám mây bao trùm những gì?")
left = 6.6
textblock(s, ML, 1.52, left - 0.35, [
    "Bảo mật đám mây áp dụng cho **mọi mô hình dịch vụ** và **mọi mô hình triển khai**:"],
    size=13, color=TEXT, hl=NAVY)
flow(s, ML, 2.05, left - 0.35, 0.62, ["SaaS", "PaaS", "IaaS"], gap=0.3, size=13)
tfx = txbox(s, ML, 2.88, left - 0.35, 0.3)
rich(tfx.paragraphs[0], "Mô hình triển khai: riêng tư · lai · công cộng · cộng đồng",
     12, MUTED, line_spacing=1.0)
card(s, ML, 3.35, left - 0.35, 3.25,
     "Hai nhóm mối quan ngại bảo mật",
     ["**Nhà cung cấp phải đối mặt:** các tổ chức cung cấp phần mềm, nền tảng hoặc hạ tầng dưới dạng dịch vụ qua Đám mây.",
      "**Khách hàng phải đối mặt:** tổ chức, hiệp hội có ứng dụng hoặc thông tin được lưu trữ trên Đám mây.",
      "→ Trách nhiệm được **chia sẻ giữa hai bên**, không bên nào gánh hết."],
     fill=SKY2, head_size=14, body_size=12, gap=8, name="2 nhóm")
# sơ đồ trách nhiệm chia sẻ
bx = ML + left + 0.05
pw = CW - left - 0.05
rect(s, bx, 1.52, pw, 5.10, fill=SKY2, line=BORDER, adj=0.035)

def _stackbox(x, y, w, h, t1, t2, fill, line, c1, c2):
    b = rect(s, x, y, w, h, fill=fill, line=line, adj=0.12)
    tf = b.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.05)
    rich(tf.paragraphs[0], t1, 13.5, c1, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    rich(tf.add_paragraph(), t2, 10.5, c2, align=PP_ALIGN.CENTER, line_spacing=1.0, space_before=2)
    return b

_stackbox(bx + (pw - 2.9) / 2, 1.88, 2.9, 0.82, "Nhà cung cấp", "(CSP)",
          BLUE, BLUE, WHITE, RGBColor.from_string("CFE2F2"))
textblock(s, bx + 0.32, 2.82, pw - 0.64, [
    "**Nhà cung cấp:** bảo đảm dịch vụ của họ an toàn, dữ liệu và ứng dụng của khách hàng được bảo vệ."],
    size=11, color=TEXT, hl=BLUE, align=PP_ALIGN.CENTER)
rect(s, bx + pw / 2 - 0.10, 3.30, 0.20, 0.26, fill=BLUEL, shape=MSO_SHAPE.DOWN_ARROW)

sh_ = rect(s, bx + (pw - 3.3) / 2, 3.66, 3.3, 0.86, fill=NAVY, line=NAVY, adj=0.12)
tf = sh_.text_frame
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
tf.margin_left = tf.margin_right = Inches(0.05)
rich(tf.paragraphs[0], "TRÁCH NHIỆM CHIA SẺ", 13.5, WHITE, bold=True,
     align=PP_ALIGN.CENTER, line_spacing=1.0)

rect(s, bx + pw / 2 - 0.10, 4.64, 0.20, 0.26, fill=BLUEL, shape=MSO_SHAPE.UP_ARROW)
textblock(s, bx + 0.32, 5.00, pw - 0.64, [
    "**Khách hàng:** thực hiện các biện pháp hỗ trợ, chẳng hạn dùng mật khẩu mạnh."],
    size=11, color=TEXT, hl=BLUE, align=PP_ALIGN.CENTER)
_stackbox(bx + (pw - 2.9) / 2, 5.52, 2.9, 0.82, "Khách hàng", "(Client)",
          WHITE, BLUE, NAVY, MUTED)
footer(s, 4)
notes(s, """
Ý chính của slide này là phạm vi và mô hình trách nhiệm.
Bảo mật đám mây không gắn với riêng một mô hình nào: nó áp dụng cho cả SaaS, PaaS, IaaS,
và cho cả bốn mô hình triển khai riêng tư, lai, công cộng, cộng đồng.
Sách chia mối quan ngại thành đúng hai nhóm: nhóm mà nhà cung cấp phải đối mặt và nhóm mà
khách hàng phải đối mặt. Và điểm cần nhấn mạnh là trách nhiệm được chia sẻ.
Nhà cung cấp bảo đảm dịch vụ của họ an toàn; còn khách hàng phải thực hiện các biện pháp hỗ trợ —
ví dụ đơn giản nhất trong sách là dùng mật khẩu mạnh.
Nếu khách hàng phó mặc hoàn toàn cho nhà cung cấp thì mô hình này gãy — ý đó sẽ quay lại ở phần tổng kết.
Bây giờ ta xem ba tính chất nền tảng của an toàn thông tin.
""")

# ================================================================= SLIDE 5
s = new_slide()
head(s, "Các khái niệm sơ bộ", "Bộ ba CIA: Bí mật – Toàn vẹn – Sẵn sàng")
# tam giác CIA
cx = ML + 0.15
rect(s, cx, 1.50, 4.55, 3.35, fill=SKY2, line=BORDER, adj=0.04)
b1 = rect(s, cx + 1.28, 1.78, 2.0, 0.62, fill=BLUE, line=BLUE, adj=0.14)
b2 = rect(s, cx + 0.30, 3.55, 1.85, 0.62, fill=NAVY, line=NAVY, adj=0.14)
b3 = rect(s, cx + 2.42, 3.55, 1.85, 0.62, fill=NAVY, line=NAVY, adj=0.14)
for b_, t_ in ((b1, "Bí mật"), (b2, "Toàn vẹn"), (b3, "Sẵn sàng")):
    tf = b_.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tf.paragraphs[0], t_, 13.5, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
for (ax, ay, bxx, byy) in ((cx + 1.7, 2.40, cx + 1.0, 3.55),
                           (cx + 2.86, 2.40, cx + 3.5, 3.55),
                           (cx + 2.15, 3.86, cx + 2.42, 3.86)):
    cn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(ax), Inches(ay),
                                Inches(bxx), Inches(byy))
    cn.line.color.rgb = BLUEL
    cn.line.width = Pt(2)
tf = txbox(s, cx + 1.55, 2.92, 1.5, 0.35)
rich(tf.paragraphs[0], "CIA", 15, BLUE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
tf = txbox(s, cx + 0.3, 4.40, 4.0, 0.3)
rich(tf.paragraphs[0], "Confidentiality – Integrity – Availability", 10.5, MUTED,
     italic=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
# giải thích
rx = ML + 4.95
items = [
    "**Tính bí mật (Confidentiality):** ngăn chặn việc tiết lộ nội dung một cách trái phép, dù cố ý hay vô ý.",
    "**Tính toàn vẹn (Integrity):** bảo đảm thông điệp gửi đi chính là thông điệp nhận về, không bị thay đổi trên đường truyền.",
    "**Tính sẵn sàng (Availability):** các thành phần tạo ra độ tin cậy và tính ổn định, để người dùng hợp lệ luôn truy cập được khi cần.",
]
bullets(s, rx, 1.60, CW - 4.95, items, size=13, gap=13)
card(s, ML, 5.10, CW, 1.50,
     "Vì sao bài toán đổi khác khi lên Đám mây?",
     ["Phần lớn **mạng, hệ thống, ứng dụng và thông tin** chuyển sang nằm dưới sự kiểm soát của **bên thứ ba**.",
      "Mô hình này tạo ra những **“hòn đảo” Đám mây** với các **vành đai ảo (virtual perimeter)** và một mô hình bảo mật có nghĩa vụ **chia sẻ giữa khách hàng và CSP**."],
     fill=SKY, head_size=14, body_size=12, gap=7, name="CIA cloud")
footer(s, 5)
notes(s, """
Bộ ba CIA là khung tư duy kinh điển, và sách nhắc lại ngay đầu chương vì mọi thứ phía sau đều quy về đây.
Bí mật là ngăn tiết lộ nội dung trái phép — chú ý sách nói rõ "dù có chủ ý hay không có chủ ý",
tức là rò rỉ do cấu hình sai cũng là mất tính bí mật.
Toàn vẹn là thông điệp gửi đi đúng bằng thông điệp nhận về; nếu kẻ tấn công sửa được luồng thông tin
giữa đường thì toàn vẹn bị phá.
Sẵn sàng là hệ thống phải dùng được khi người dùng hợp lệ cần tới.
Điểm khác biệt khi lên Đám mây nằm ở khối màu xanh phía dưới: phần lớn hạ tầng chuyển sang
tay bên thứ ba, tạo ra các vành đai ảo thay cho vành đai vật lý cũ, và mô hình bảo mật trở thành
nghĩa vụ chia sẻ giữa khách hàng và nhà cung cấp.
Với khung này trong đầu, ta vào mục 11.1 — bảo mật dữ liệu.
""")

# ================================================================= SLIDE 6
s = new_slide()
divider(s, "PHẦN I  ·  MỤC 11.1 – 11.2", "Bảo mật dữ liệu\nvà kỹ thuật mã hóa",
        ["Dữ liệu đang truyền (data-in-transit) và rủi ro chính",
         "Siêu dữ liệu và các mối quan ngại bảo mật trong Đám mây",
         "Ba kỹ thuật mã hóa: ABE, FHE, SE và dịch vụ WPS"])
notes(s, """
Phần đầu tiên: dữ liệu và mã hóa. Đây là phần nền, vì mọi biện pháp phía sau đều nhằm
bảo vệ dữ liệu. Ta sẽ đi qua dữ liệu đang truyền, rủi ro lớn nhất của nó, rồi tới ba
họ kỹ thuật mã hóa đặc trưng cho Đám mây.
""")

# ================================================================= SLIDE 7
s = new_slide()
head(s, "11.1 Bảo mật dữ liệu", "Dữ liệu đang truyền (Data-in-transit)")
textblock(s, ML, 1.52, CW, [
    "Dữ liệu đang truyền nhận diện **dữ liệu đòi hỏi phải mã hóa** khi di chuyển từ thiết bị này sang thiết bị khác."],
    size=14, color=TEXT, hl=NAVY)
cw3 = (CW - 2 * 0.34) / 3
data3 = [
    ("Mạng công cộng", "Public Networks",
     ["Chuyển giao dữ liệu qua các mạng công cộng như **Internet**.",
      "Ví dụ: ứng dụng trên điện thoại di động kết nối tới dịch vụ ngân hàng để yêu cầu một giao dịch.",
      "Thường được mã hóa bằng các giao thức như **HTTP**."]),
    ("Mạng riêng", "Private Networks",
     ["Chuyển giao qua **mạng cục bộ đã được bảo mật**, ví dụ trong một văn phòng.",
      "Nguyên tắc **phòng thủ theo chiều sâu (defense in depth)**: đừng tin rằng mạng đã được bảo mật đúng cách.",
      "→ Áp dụng **cùng mức mã hóa** như với mạng công cộng."]),
    ("Thiết bị cục bộ", "Local Devices",
     ["Chuyển giao giữa **máy tính, thiết bị lưu trữ và thiết bị ngoại vi**.",
      "**Chính phương tiện truyền có thể chặn bắt** dữ liệu.",
      "Ví dụ: một dây cáp USB nối thiết bị với máy tính có thể ghi lại hoặc truyền đi dữ liệu."]),
]
for i, (t, en, lines) in enumerate(data3):
    x = ML + i * (cw3 + 0.34)
    rect(s, x, 2.20, cw3, 4.35, fill=SKY2, line=BORDER, adj=0.045)
    rect(s, x, 2.20, cw3, 0.80, fill=BLUE, line=BLUE, adj=0.12)
    rect(s, x, 2.62, cw3, 0.38, fill=BLUE, line=BLUE, shape=MSO_SHAPE.RECTANGLE)
    tf = txbox(s, x + 0.2, 2.33, cw3 - 0.4, 0.3)
    rich(tf.paragraphs[0], t, 14.5, WHITE, bold=True, line_spacing=1.0)
    tf = txbox(s, x + 0.2, 2.66, cw3 - 0.4, 0.28)
    rich(tf.paragraphs[0], en, 10.5, RGBColor.from_string("CFE2F2"), italic=True, line_spacing=1.0)
    bullets(s, x + 0.2, 3.18, cw3 - 0.4, lines, size=11.5, gap=9, mark="•",
            mark_color=BLUE, indent=0.16, hl=NAVY)
footer(s, 7)
notes(s, """
Mục 11.1 mở đầu bằng khái niệm dữ liệu đang truyền — data-in-transit. Định nghĩa của sách rất gọn:
đó là dữ liệu đòi hỏi phải mã hóa khi di chuyển từ thiết bị này sang thiết bị khác.
Sách cho ba ví dụ phổ biến.
Thứ nhất là mạng công cộng: ví dụ ứng dụng ngân hàng trên điện thoại gọi ra Internet.
Thứ hai là mạng riêng. Ở đây có một ý rất đáng nhớ: nguyên tắc phòng thủ theo chiều sâu nói rằng
đừng giả định mạng nội bộ đã an toàn — vì vậy ta mã hóa trên mạng riêng y như trên mạng công cộng.
Thứ ba là thiết bị cục bộ, và đây là chỗ nhiều người quên: chính phương tiện truyền có thể chặn bắt
dữ liệu. Sách lấy ví dụ sợi cáp USB có khả năng ghi lại hoặc truyền đi dữ liệu.
Slide sau ta xem hai loại dữ liệu đang truyền và rủi ro lớn nhất.
""")

# ================================================================= SLIDE 8
s = new_slide()
head(s, "11.1 Bảo mật dữ liệu", "Hai loại dữ liệu · Rủi ro chính · Siêu dữ liệu")
lw = 6.05
tf = txbox(s, ML, 1.52, lw, 0.3)
rich(tf.paragraphs[0], "HAI LOẠI DỮ LIỆU ĐANG TRUYỀN", 11.5, BLUE, bold=True, line_spacing=1.0)
numbers(s, ML, 1.92, lw, [
    "Thông tin lưu chuyển qua **mạng công cộng hoặc mạng không đáng tin cậy** như Internet.",
    "Dữ liệu lưu chuyển trong phạm vi giới hạn của một **mạng riêng**, như LAN của công ty hay doanh nghiệp.",
], size=12.5, gap=11)
card(s, ML, 3.42, lw, 2.00,
     "⚠  Rủi ro chính (Primary risk)",
     ["Đối với dữ liệu đang truyền, rủi ro chính **không nằm ở việc có mã hóa hay không**, mà là **không sử dụng một thuật toán mã hóa đã được kiểm chứng** (vetted encryption algorithm).",
      "Yêu cầu này hiển nhiên với chuyên gia bảo mật, nhưng **thường không được hiểu** bởi người dùng Đám mây công cộng — bất kể đó là IaaS, PaaS hay SaaS."],
     fill=REDBG, border=REDBD, head_color=RED, hl=RED, head_size=13.5, body_size=11.5,
     gap=7, name="rủi ro chính")
rx = ML + lw + 0.40
card(s, rx, 1.52, CW - lw - 0.40, 3.62,
     "Vượt ra ngoài bản thân dữ liệu: SIÊU DỮ LIỆU",
     ["Khách hàng không chỉ quan tâm **dữ liệu nào được thu thập**, mà còn quan tâm **CSP bảo vệ dữ liệu đó ra sao**.",
      "Ba câu hỏi cần đặt ra với nhà cung cấp:",
      "   • Nhà cung cấp **nắm giữ siêu dữ liệu (metadata) nào** về dữ liệu của tôi?",
      "   • Siêu dữ liệu đó **được bảo mật như thế nào**?",
      "   • Khách hàng **có quyền truy cập gì** đối với siêu dữ liệu đó?",
      "**Khối lượng dữ liệu của tôi ở một nhà cung cấp càng tăng → giá trị siêu dữ liệu đó càng tăng theo.**"],
     fill=SKY, head_size=13.5, body_size=11.5, gap=7, name="metadata")
card(s, ML, 5.52, lw, 1.30,
     "Ghi nhớ",
     ["Cùng một dữ liệu, cùng một mức mã hóa — dù đi qua **Internet hay LAN nội bộ**. Mạng riêng **không phải** lý do để hạ thấp tiêu chuẩn bảo vệ."],
     fill=SKY2, head_size=13, body_size=11.5, name="ghi nhớ")
footer(s, 8)
notes(s, """
Sách chia dữ liệu đang truyền thành đúng hai loại: đi qua mạng công cộng không đáng tin cậy,
và đi trong phạm vi một mạng riêng như LAN doanh nghiệp.
Nhưng ý quan trọng nhất của slide này nằm ở khối đỏ. Rủi ro chính đối với dữ liệu đang truyền
không phải là "quên mã hóa", mà là "mã hóa nhưng không dùng thuật toán đã được kiểm chứng".
Sách nói thẳng: điều này hiển nhiên với chuyên gia bảo mật, nhưng người dùng Đám mây công cộng
thường không hiểu — và điều đó đúng cho cả ba mô hình IaaS, PaaS lẫn SaaS.
Bên phải là một khía cạnh hay bị bỏ quên: siêu dữ liệu. Khách hàng cần hỏi nhà cung cấp ba câu:
nắm giữ siêu dữ liệu nào, bảo mật ra sao, và tôi có quyền truy cập gì.
Và một quy luật: dữ liệu của ta ở nhà cung cấp càng nhiều thì siêu dữ liệu đó càng giá trị —
tức là càng trở thành mục tiêu hấp dẫn.
""")

# ================================================================= SLIDE 9
s = new_slide()
head(s, "11.1 Bảo mật dữ liệu", "Các mối quan ngại bảo mật đáng kể trong Đám mây")
textblock(s, ML, 1.50, CW, [
    "Điện toán đám mây bao hàm **nhiều công nghệ**: mạng, cơ sở dữ liệu, hệ điều hành, ảo hóa, lập lịch tài nguyên, quản lý giao dịch, cân bằng tải, kiểm soát tương tranh và quản lý bộ nhớ."],
    size=12.5, color=TEXT, hl=NAVY)
concerns = [
    ("Truyền dữ liệu", "Data Transmission", "Gửi dữ liệu số hoặc tương tự tới một hoặc nhiều thiết bị; điểm–điểm, điểm–đa điểm, đa điểm–đa điểm."),
    ("Bảo mật ảo hóa", "Virtualization Security", "Các biện pháp, thủ tục, quy trình bảo đảm sự bảo vệ của hạ tầng/môi trường ảo hóa."),
    ("Bảo mật mạng", "Network Security", "Chiến lược bảo đảm an toàn cho tài sản và toàn bộ lưu lượng mạng của tổ chức."),
    ("Toàn vẹn dữ liệu", "Data Integrity", "Xác định dữ liệu nào trong hệ thống **có thể được chia sẻ với bên thứ ba**."),
    ("Quyền riêng tư", "Data Privacy", "Tính toàn vẹn dữ liệu: **độ chính xác và tính nhất quán** của dữ liệu được lưu trữ."),
    ("Vị trí dữ liệu", "Data Location", "Dữ liệu số được lưu trữ trong **các nhóm logic**, trải rộng trên nhiều máy chủ và nhiều địa điểm."),
    ("Sẵn sàng dữ liệu", "Data Availability", "Dữ liệu **tiếp tục sẵn sàng** ở mức hiệu năng yêu cầu, từ tình huống bình thường đến “thảm họa”."),
]
cw4 = (CW - 3 * 0.26) / 4
for i, (t, en, d) in enumerate(concerns):
    col, row = i % 4, i // 4
    x = ML + col * (cw4 + 0.26)
    y = 2.30 + row * 1.92
    rect(s, x, y, cw4, 1.72, fill=SKY2, line=BORDER, adj=0.07)
    rect(s, x, y, cw4, 0.075, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
    tf = txbox(s, x + 0.16, y + 0.20, cw4 - 0.32, 0.28)
    rich(tf.paragraphs[0], t, 13, NAVY, bold=True, line_spacing=1.0)
    tf = txbox(s, x + 0.16, y + 0.50, cw4 - 0.32, 0.26)
    rich(tf.paragraphs[0], en, 9.5, BLUE, italic=True, line_spacing=1.0)
    textblock(s, x + 0.16, y + 0.80, cw4 - 0.32, [d], size=10.5, color=TEXT, hl=NAVY)
tfx = txbox(s, ML + 3 * (cw4 + 0.26), 4.22, cw4, 1.72)
rich(tfx.paragraphs[0],
     "Hai ví dụ về thứ phải bảo vệ: mạng liên kết các hệ thống trong một Đám mây, và ánh xạ máy ảo sang máy vật lý.",
     11, MUTED, italic=True, line_spacing=1.25)
footer(s, 9)
notes(s, """
Slide này là danh mục các mối quan ngại mà sách liệt kê. Ý nền là: Đám mây không phải một công nghệ,
mà là chồng nhiều công nghệ — mạng, cơ sở dữ liệu, hệ điều hành, ảo hóa, lập lịch, giao dịch,
cân bằng tải... nên bề mặt tấn công rất rộng.
Bảy khái niệm ở đây các bạn nên nắm tên tiếng Anh vì đề thi hay hỏi: data transmission,
virtualization security, network security, data integrity, data privacy, data location,
data availability.
Mình nhấn hai cái hay nhầm: toàn vẹn dữ liệu ở đây được sách mô tả gắn với việc xác định
dữ liệu nào có thể chia sẻ với bên thứ ba; còn quyền riêng tư gắn với độ chính xác và
tính nhất quán của dữ liệu lưu trữ.
Và vị trí dữ liệu — data location — rất quan trọng về mặt pháp lý: dữ liệu nằm trong các nhóm logic
trải trên nhiều máy chủ, nhiều địa điểm, thường do công ty lưu trữ sở hữu và quản lý.
Sách khép mục này bằng hai ví dụ cụ thể phải bảo vệ: mạng liên kết các hệ thống, và ánh xạ
máy ảo lên máy vật lý. Đó chính là cầu nối sang phần mã hóa.
""")

# ================================================================= SLIDE 10
s = new_slide()
head(s, "11.2 Kỹ thuật mã hóa trong Đám mây", "Ba họ kỹ thuật mã hóa đặc trưng")
card(s, ML, 1.50, CW, 0.90, "",
     ["**Mã hóa đám mây (Cloud encryption)** là sự biến đổi dữ liệu của khách hàng thành **bản mã (ciphertext)** trước khi được đặt lên một Đám mây lưu trữ."],
     fill=SKY, head_size=13, body_size=13, pad=0.19, name="def enc")
three = [
    ("ABE", "Mã hóa dựa trên thuộc tính", "Attribute-Based Encryption",
     ["Mã hóa **khóa công khai**, trong đó **khóa bí mật của người dùng và bản mã phụ thuộc vào các thuộc tính** (ví dụ: quốc gia sinh sống, loại gói thuê bao).",
      "Giải mã **chỉ khả thi** nếu tập thuộc tính của khóa **khớp** với tập thuộc tính của bản mã."]),
    ("FHE", "Mã hóa đồng cấu toàn phần", "Fully Homomorphic Encryption",
     ["Cho phép **thực hiện phép tính trên dữ liệu đã mã hóa**.",
      "Cho phép tính **tổng và tích** đối với dữ liệu đã mã hóa **mà không cần giải mã**."]),
    ("SE", "Mã hóa có thể tìm kiếm", "Searchable Encryption",
     ["Hệ thống mật mã cung cấp chức năng **tìm kiếm an toàn trên dữ liệu đã mã hóa**.",
      "Hai loại: dựa trên **mật mã khóa bí mật (đối xứng)** và dựa trên **mật mã khóa công khai**."]),
]
cw3 = (CW - 2 * 0.34) / 3
for i, (abbr, vi, en, lines) in enumerate(three):
    x = ML + i * (cw3 + 0.34)
    rect(s, x, 2.60, cw3, 3.30, fill=SKY2, line=BORDER, adj=0.05)
    ch = rect(s, x + 0.22, 2.82, 1.05, 0.55, fill=NAVY, line=NAVY, adj=0.16)
    tf = ch.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tf.paragraphs[0], abbr, 17, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    tf = txbox(s, x + 1.40, 2.84, cw3 - 1.62, 0.55)
    rich(tf.paragraphs[0], vi, 13, NAVY, bold=True, line_spacing=1.05)
    tf = txbox(s, x + 0.22, 3.50, cw3 - 0.44, 0.26)
    rich(tf.paragraphs[0], en, 10, BLUE, italic=True, line_spacing=1.0)
    bullets(s, x + 0.22, 3.86, cw3 - 0.44, lines, size=11.5, gap=9, mark="•",
            mark_color=BLUE, indent=0.16)
card(s, ML, 6.05, CW, 0.62, "",
     ["Để **cải thiện hiệu quả tìm kiếm**, SE khóa đối xứng thường xây dựng các **chỉ mục từ khóa (keyword index)** để trả lời các truy vấn của người dùng."],
     fill=AMBBG, border=AMBBD, body_size=11.5, pad=0.14, name="SE note")
footer(s, 10)
notes(s, """
Sang mục 11.2. Trước hết là định nghĩa: mã hóa đám mây là biến dữ liệu của khách hàng thành bản mã
trước khi đặt lên Đám mây lưu trữ. Nghĩa là việc mã hóa xảy ra trước khi dữ liệu rời khỏi tầm kiểm soát.
Sách trình bày ba kỹ thuật quan trọng, và mỗi kỹ thuật trả lời một nhu cầu khác nhau.
ABE trả lời câu hỏi "ai được giải mã" — khóa và bản mã đều gắn với thuộc tính, ví dụ quốc gia
người đó sinh sống hay loại gói thuê bao; chỉ giải mã được khi hai tập thuộc tính khớp nhau.
FHE trả lời câu hỏi "làm sao tính toán mà không lộ dữ liệu" — cho phép tính tổng và tích ngay
trên bản mã mà không cần giải mã.
SE trả lời câu hỏi "làm sao tìm kiếm mà không lộ nội dung" — và chia làm hai nhánh: khóa đối xứng
và khóa công khai. Với nhánh đối xứng, người ta thường xây chỉ mục từ khóa để tìm nhanh hơn.
Ba slide tiếp theo ta đi sâu lần lượt vào từng kỹ thuật.
""")

# ================================================================= SLIDE 11
s = new_slide()
head(s, "11.2 ABE", "Hai chính sách: CP-ABE và KP-ABE")
half = (CW - 0.45) / 2
card(s, ML, 1.50, half, 2.05,
     "CP-ABE  ·  ABE theo chính sách bản mã",
     ["Ciphertext-Policy ABE",
      "**Bên mã hóa (encryptor) kiểm soát chiến lược truy cập.**",
      "Ý tưởng chính: tập trung vào **thiết kế của cấu trúc truy cập (access structure)**."],
     fill=SKY, head_size=14, body_size=12, gap=7, name="CP-ABE")
card(s, ML + half + 0.45, 1.50, half, 2.05,
     "KP-ABE  ·  ABE theo chính sách khóa",
     ["Key-Policy ABE",
      "**Các tập thuộc tính** được dùng để **mô tả các văn bản đã mã hóa**.",
      "**Các khóa riêng** được liên kết với **chính sách xác định** mà người dùng sẽ có."],
     fill=SKY, head_size=14, body_size=12, gap=7, name="KP-ABE")
rect(s, ML, 3.78, CW, 2.70, fill=SKY2, line=BORDER, adj=0.035)
tf = txbox(s, ML + 0.3, 3.98, CW - 0.6, 0.3)
rich(tf.paragraphs[0], "CƠ CHẾ GIẢI MÃ CỦA ABE", 11.5, BLUE, bold=True, line_spacing=1.0)
flow(s, ML + 0.45, 4.45, CW - 0.9, 1.05,
     ["Thuộc tính người dùng|quốc gia, gói thuê bao",
      "Khóa bí mật|gắn với thuộc tính",
      "Thuộc tính của bản mã|trên Đám mây",
      "Giải mã thành công|chỉ khi KHỚP"],
     gap=0.40, size=12, last_fill=NAVY, last_border=NAVY, last_color=WHITE)
tf = txbox(s, ML + 0.45, 5.72, CW - 0.9, 0.5)
rich(tf.paragraphs[0],
     "Trong một hệ thống như vậy, việc **giải mã một bản mã chỉ khả thi nếu tập thuộc tính của khóa người dùng khớp với các thuộc tính của bản mã**.",
     12, TEXT, hl=NAVY, align=PP_ALIGN.CENTER, line_spacing=1.2)
footer(s, 11)
notes(s, """
ABE có hai biến thể và các bạn cần phân biệt rõ vì tên rất dễ nhầm.
CP-ABE, tức ABE theo chính sách bản mã: bên mã hóa kiểm soát chiến lược truy cập.
Ý tưởng chính của CP-ABE tập trung vào thiết kế cấu trúc truy cập.
Cách nhớ: chính sách nằm trong bản mã — tôi mã hóa và tôi quy định ai mở được.
KP-ABE, tức ABE theo chính sách khóa: các tập thuộc tính dùng để mô tả văn bản đã mã hóa,
còn khóa riêng thì được gắn với chính sách mà người dùng sẽ có.
Cách nhớ: chính sách nằm trong khóa.
Sơ đồ phía dưới mô tả cơ chế chung: thuộc tính người dùng sinh ra khóa bí mật, bản mã cũng
mang thuộc tính, và giải mã chỉ thành công khi hai bên khớp nhau.
""")

# ================================================================= SLIDE 12
s = new_slide()
head(s, "11.2.1 ABE theo chính sách khóa phi tập trung", "Năm mô-đun con của lược đồ phi tập trung")
card(s, ML, 1.48, CW, 0.85, "",
     ["Trong lược đồ **phi tập trung (decentralized)**, **không cần duy trì một số lượng cố định** các cơ quan thuộc tính (attribute authority). Bất kỳ cơ quan nào cũng có thể **gia nhập hoặc rời khỏi hệ thống bất kỳ lúc nào mà không cần khởi động lại hệ thống**."],
     fill=SKY, body_size=12.5, pad=0.18, name="decentralized")
flow(s, ML + 0.30, 2.55, CW - 0.6, 0.78,
     ["Thiết lập\ntoàn cục", "Thiết lập\ncơ quan", "Cấp phát\nkhóa", "Mã hóa", "Giải mã"],
     gap=0.36, size=12.5, last_fill=NAVY, last_border=NAVY, last_color=WHITE)
tf = txbox(s, ML + 0.30, 3.40, CW - 0.6, 0.26)
rich(tf.paragraphs[0], "Global setup  →  Authority setup  →  Key issuing  →  Encryption  →  Decryption",
     10.5, MUTED, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
mods = [
    "**Thiết lập toàn cục (Global setup):** nhận một **tham số bảo mật** làm đầu vào và xuất ra các **tham số hệ thống** mà mọi cơ quan gia nhập đều dùng.",
    "**Thiết lập cơ quan (Authority setup):** mỗi cơ quan thuộc tính dùng tham số hệ thống để sinh ra **khóa công khai và khóa riêng** cho các thuộc tính mà nó duy trì.",
    "**Cấp phát khóa (Key issuing):** người dùng và cơ quan thuộc tính tương tác qua một **giao thức cấp phát khóa ẩn danh**; cơ quan sinh và gửi **chứng thư giải mã** cho người dùng.",
    "**Mã hóa (Encryption):** nhận **tập thuộc tính** do cơ quan duy trì cùng với **dữ liệu**, xuất ra **bản mã**.",
    "**Giải mã (Decryption):** nhận chứng thư giải mã và bản mã; **chỉ thành công khi và chỉ khi** thuộc tính của người dùng **thỏa mãn cấu trúc truy cập**.",
]
bullets(s, ML + 0.15, 3.88, CW - 0.3, mods, size=12, gap=10)
footer(s, 12)
notes(s, """
Đây là một lược đồ KP-ABE phi tập trung. Từ khóa cần nhớ là "phi tập trung":
không cần cố định số lượng cơ quan thuộc tính, và cơ quan nào cũng có thể gia nhập hay rời đi
bất cứ lúc nào mà không phải khởi động lại hệ thống. Đó chính là ưu điểm về khả năng mở rộng.
Lược đồ gồm năm mô-đun con, chạy tuần tự như sơ đồ.
Thiết lập toàn cục nhận tham số bảo mật, trả ra tham số hệ thống dùng chung.
Thiết lập cơ quan: mỗi cơ quan tự sinh cặp khóa công khai và khóa riêng cho các thuộc tính nó quản lý.
Cấp phát khóa là bước thú vị nhất: người dùng và cơ quan tương tác qua một giao thức cấp phát khóa
ẩn danh — tức là cơ quan xác định được người dùng có thuộc tính gì mà không cần biết danh tính,
rồi trả về chứng thư giải mã.
Mã hóa nhận tập thuộc tính cộng với dữ liệu, xuất ra bản mã.
Giải mã thành công khi và chỉ khi thuộc tính của người dùng thỏa mãn cấu trúc truy cập.
Câu hỏi tiếp theo là: làm sao chứng minh lược đồ này an toàn? Đó là nội dung slide sau.
""")

# ================================================================= SLIDE 13
s = new_slide()
head(s, "11.2.2 Trò chơi bảo mật", "Mô hình định danh chọn lọc (Selective ID model)")
textblock(s, ML, 1.50, CW, [
    "Để tránh các lỗ hổng, các lược đồ ABE được **chứng minh là an toàn** trước mô hình **định danh chọn lọc (selective ID)** — biểu diễn dưới dạng một **trò chơi giữa đối thủ (adversary) và người thách đấu (challenger)**."],
    size=12.5, color=TEXT, hl=NAVY)
lw = 7.55
steps = [
    "**Truy vấn khóa bí mật (Secret key queries):** đối thủ được thực hiện **bao nhiêu truy vấn tùy ý**; yêu cầu duy nhất là với mỗi người dùng phải có **ít nhất một cơ quan thuộc tính không bị xâm phạm** — nhờ đó đối thủ chỉ lấy được **số lượng khóa không đủ (insufficient)**.",
    "**Thách đấu (Challenge):** đối thủ gửi hai thông điệp **m₀** và **m₁** ở dạng bản rõ; người thách đấu **chọn ngẫu nhiên một trong hai**, mã hóa và gửi bản mã lại cho đối thủ.",
    "**Thêm truy vấn khóa bí mật:** đối thủ được truy vấn tiếp, **miễn là vẫn thỏa mãn yêu cầu ở bước 1**.",
    "**Đoán (Guess):** đối thủ đoán xem **thông điệp nào** đã được mã hóa.",
]
numbers(s, ML, 2.28, lw, steps, size=12, gap=11)
rx = ML + lw + 0.40
rw = CW - lw - 0.40
card(s, rx, 2.28, rw, 2.15,
     "Điều kiện thành công",
     ["Đối thủ được coi là **thành công** nếu đoán đúng thông điệp với xác suất:"],
     fill=SKY, head_size=13.5, body_size=12, name="success")
fm = rect(s, rx + 0.45, 3.40, rw - 0.90, 0.62, fill=WHITE, line=BLUE, adj=0.12)
tf = fm.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
rich(tf.paragraphs[0], "½  +  ε", 22, NAVY, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
textblock(s, rx + 0.18, 4.55, rw - 0.36, [
    "trong đó **ε** là một **hàm không thể bỏ qua** (non-negligible function)."],
    size=11.5, color=TEXT, hl=BLUE)
card(s, rx, 5.15, rw, 1.42,
     "Kết luận",
     ["Nếu đối thủ **không thể giải mã** thông điệp với **lợi thế không thể bỏ qua**, thì lược đồ được coi là **an toàn** trước mô hình ID chọn lọc."],
     fill=GRNBG, border=GRNBD, head_color=GREEN, hl=GREEN, head_size=13, body_size=11.5, name="ketluan")
footer(s, 13)
notes(s, """
Slide này trả lời câu hỏi "an toàn nghĩa là gì" theo ngôn ngữ mật mã học.
Người ta mô hình hóa nó thành một trò chơi giữa đối thủ và người thách đấu, gồm bốn bước.
Bước một, đối thủ được hỏi bao nhiêu khóa bí mật tùy thích. Nhưng có một ràng buộc:
với mỗi người dùng phải tồn tại ít nhất một cơ quan thuộc tính chưa bị xâm phạm — nhờ vậy
đối thủ chỉ gom được một lượng khóa không đủ để giải mã.
Bước hai là thách đấu: đối thủ đưa ra hai bản rõ m0 và m1, người thách đấu chọn ngẫu nhiên một
cái để mã hóa và trả bản mã về.
Bước ba, đối thủ vẫn được hỏi thêm khóa, miễn là giữ nguyên ràng buộc.
Bước bốn, đối thủ đoán xem thông điệp nào đã được mã hóa.
Công thức bên phải rất quan trọng: đối thủ thành công nếu đoán đúng với xác suất một phần hai
cộng epsilon, với epsilon là hàm không thể bỏ qua. Trực giác là: đoán mò luôn cho 50%,
nên chỉ khi đối thủ vượt 50% một lượng đáng kể thì mới coi là phá được.
Ngược lại, nếu đối thủ không đạt được lợi thế đáng kể thì ta nói lược đồ an toàn trước
mô hình ID chọn lọc.
""")

# ================================================================= SLIDE 14
s = new_slide()
head(s, "11.2.3 FHE", "Mã hóa đồng cấu toàn phần: các bên tham gia")
textblock(s, ML, 1.48, CW, [
    "Trong FHE, hệ thống gồm **nhiều bên đóng ba vai trò then chốt** trong tính toán an toàn."],
    size=13, color=TEXT, hl=NAVY)
# sơ đồ
dy = 1.95
rect(s, ML, dy, CW, 2.55, fill=SKY2, line=BORDER, adj=0.035)
u = rect(s, ML + 0.45, dy + 0.75, 2.85, 1.05, fill=WHITE, line=BLUE, adj=0.10)
tf = u.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
tf.margin_left = tf.margin_right = Inches(0.06)
rich(tf.paragraphs[0], "NGƯỜI DÙNG", 12.5, NAVY, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
rich(tf.add_paragraph(), "thuê ngoài việc tính toán,\ndữ liệu riêng được bảo vệ", 10, MUTED,
     align=PP_ALIGN.CENTER, line_spacing=1.15, space_before=3)
hc = rect(s, ML + 6.3, dy + 0.12, 3.0, 0.95, fill=BLUE, line=BLUE, adj=0.10)
tf = hc.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
tf.margin_left = tf.margin_right = Inches(0.06)
rich(tf.paragraphs[0], "NÚT TÍNH TOÁN ĐỒNG CẤU (HC)", 11.5, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.05)
rich(tf.add_paragraph(), "CPU / GPU / FPGA — KHÔNG được bảo vệ", 9.5,
     RGBColor.from_string("D6E8F7"), align=PP_ALIGN.CENTER, line_spacing=1.05, space_before=3)
bn = rect(s, ML + 6.3, dy + 1.55, 3.0, 0.95, fill=REDBG, line=RED, adj=0.10)
tf = bn.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
tf.margin_left = tf.margin_right = Inches(0.06)
rich(tf.paragraphs[0], "NÚT KHỞI TẠO (Bootstrapping)", 11.5, RED, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.05)
rich(tf.add_paragraph(), "chạy bên trong vùng bao an toàn (secure enclave)", 9.5, RED,
     align=PP_ALIGN.CENTER, line_spacing=1.05, space_before=3)
for (y1, y2, lbl, col) in ((dy + 1.15, dy + 0.60, "dữ liệu đã mã hóa", BLUE),
                           (dy + 1.48, dy + 2.02, "khóa qua kênh bí mật", BLUE)):
    cn = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(ML + 3.30), Inches(y1),
                                Inches(ML + 6.30), Inches(y2))
    cn.line.color.rgb = col
    cn.line.width = Pt(1.5)
    t = txbox(s, ML + 3.55, (y1 + y2) / 2 - 0.30, 2.6, 0.26)
    rich(t.paragraphs[0], lbl, 9.5, BLUE, align=PP_ALIGN.CENTER, line_spacing=1.0)
a1 = rect(s, ML + 7.15, dy + 1.14, 0.16, 0.30, fill=RED, shape=MSO_SHAPE.DOWN_ARROW)
a2 = rect(s, ML + 8.45, dy + 1.14, 0.16, 0.30, fill=GREEN, shape=MSO_SHAPE.UP_ARROW)
t = txbox(s, ML + 6.42, dy + 1.20, 0.65, 0.22)
rich(t.paragraphs[0], "nhiễu", 9, RED, align=PP_ALIGN.RIGHT, line_spacing=1.0)
t = txbox(s, ML + 8.68, dy + 1.20, 0.75, 0.22)
rich(t.paragraphs[0], "làm mới", 9, GREEN, line_spacing=1.0)
textblock(s, ML + 9.55, dy + 0.35, CW - 9.85, [
    "Luồng dữ liệu giữa các bên trong hệ thống FHE là **đơn giản** — ba bước như bên dưới."],
    size=11, color=MUTED, hl=NAVY)
numbers(s, ML, 4.72, CW, [
    "Người dùng **xác minh cấu hình của Đám mây** thông qua **chứng thực từ xa (remote attestation)** và **thiết lập khóa bí mật chia sẻ** với các nút khởi tạo.",
    "Người dùng **cung ứng các tham số mã hóa cùng khóa bí mật và khóa công khai** cho các nút khởi tạo **qua kênh bí mật đã thiết lập**.",
    "Dữ liệu của người dùng, **được mã hóa dưới khóa bí mật đồng cấu**, được gửi tới các **nút HC** để thực hiện các tính toán đồng cấu.",
], size=12, gap=10)
footer(s, 14)
notes(s, """
FHE là kỹ thuật được sách nhấn mạnh nhất, nên ta dành hai slide.
Slide này nói về kiến trúc — ai đóng vai gì.
Người dùng là bên thuê ngoài việc tính toán cho Đám mây, nhưng dữ liệu của họ phải được bảo vệ
khỏi sự dò xét trái phép.
Nút tính toán đồng cấu, viết tắt HC, là nơi thực sự chạy phép tính. Điểm mấu chốt: các nút này
dùng CPU, GPU hoặc FPGA và KHÔNG được bảo vệ — tức là ta không tin chúng.
Nút khởi tạo, bootstrapping node, thì chạy bên trong một vùng bao an toàn — secure enclave — và
đây là nơi duy nhất được tin cậy.
Luồng làm việc gồm ba bước. Đầu tiên người dùng xác minh cấu hình Đám mây bằng chứng thực từ xa,
rồi thiết lập khóa bí mật chia sẻ với nút khởi tạo. Sau đó cung ứng tham số và khóa qua kênh bí mật đó.
Cuối cùng dữ liệu đã mã hóa được gửi tới các nút HC để tính.
Vậy tại sao lại cần nút khởi tạo? Slide sau trả lời.
""")

# ================================================================= SLIDE 15
s = new_slide()
head(s, "11.2.3 FHE", "Bootstrapping: vì sao cần và dùng để làm gì?")
card(s, ML, 1.48, CW, 1.68,
     "Bootstrapping loại bỏ nhiễu (noise)",
     ["Bản mã trung gian được gửi từ **nút HC** tới **nút khởi tạo**. Chạy bên trong **vùng bao an toàn**, nút khởi tạo **giải mã bản mã, rồi mã hóa lại** bằng khóa bí mật và **gửi bản mã đã làm mới** trở lại các nút HC.",
      "Điều này **loại bỏ nhiễu** trong bản mã, **cho phép các nút HC tiếp tục tính toán đồng cấu**. Khi toàn bộ quá trình hoàn tất, bản mã trở về người dùng để **giải mã lấy kết quả**."],
     fill=SKY, head_size=14, body_size=12, gap=7, name="bootstrap")
flow(s, ML + 0.6, 3.34, CW - 1.2, 0.72,
     ["Nút HC tính toán", "Bản mã nhiễu", "Nút khởi tạo:\ngiải mã → mã hóa lại", "Bản mã đã làm mới", "Tiếp tục tính toán"],
     gap=0.30, size=11, last_fill=GRNBG, last_border=GREEN, last_color=GREEN)
half = (CW - 0.45) / 2
card(s, ML, 4.35, half, 2.20,
     "Ứng dụng: lưu trữ & tính toán thuê ngoài",
     ["Mã hóa đồng cấu có thể dùng cho **lưu trữ và tính toán thuê ngoài có bảo toàn quyền riêng tư**.",
      "Dữ liệu được mã hóa và **thuê ngoài tới các môi trường Đám mây thương mại để xử lý**, tất cả **trong khi vẫn ở trạng thái mã hóa**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="uc1")
card(s, ML + half + 0.45, 4.35, half, 2.20,
     "Ngành được quản lý chặt chẽ: y tế",
     ["**Phân tích dự báo (predictive analytics)** trong chăm sóc sức khỏe **khó áp dụng** do các mối quan ngại về **quyền riêng tư của dữ liệu y tế**.",
      "Nếu nhà cung cấp **thao tác trên dữ liệu đã mã hóa thay vì dữ liệu gốc**, thì **những mối quan ngại này sẽ giảm bớt**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="uc2")
footer(s, 15)
notes(s, """
Vấn đề kỹ thuật của FHE là nhiễu: mỗi phép tính trên bản mã làm nhiễu tích lũy thêm, đến một mức
nào đó thì bản mã không còn giải mã đúng được nữa.
Bootstrapping giải quyết chuyện đó. Bản mã trung gian được gửi từ nút HC sang nút khởi tạo.
Nút khởi tạo chạy trong vùng bao an toàn nên nó được phép giải mã, rồi mã hóa lại bằng khóa bí mật,
và gửi bản mã đã làm mới trở lại. Nhiễu bị loại bỏ, các nút HC tính tiếp được.
Khi toàn bộ quá trình xong, bản mã quay về người dùng và chỉ người dùng mới giải mã ra kết quả.
Về ứng dụng, sách nêu hai điểm. Thứ nhất là lưu trữ và tính toán thuê ngoài có bảo toàn quyền riêng tư:
dữ liệu mã hóa vẫn có thể gửi ra Đám mây thương mại để xử lý.
Thứ hai là ví dụ rất thuyết phục trong y tế: phân tích dự báo trong chăm sóc sức khỏe vốn khó triển khai
vì lo ngại quyền riêng tư của dữ liệu bệnh nhân; nếu nhà cung cấp chỉ thao tác trên dữ liệu đã mã hóa
thì lo ngại đó giảm đi đáng kể.
Lát nữa ở mục 11.5 ta sẽ có một ví dụ số rất dễ hiểu về FHE.
""")

# ================================================================= SLIDE 16
s = new_slide()
head(s, "11.2.4", "Mã hóa có thể tìm kiếm (Searchable Encryption)")
textblock(s, ML, 1.48, CW, [
    "SE hoạt động bằng cách **phơi bày một phân đoạn thông tin** của một ngữ cảnh, đủ để **nhận diện ngữ cảnh đó** — tức là nhận diện nội dung đã mã hóa **mà không phơi bày chính nội dung**."],
    size=12.5, color=TEXT, hl=NAVY)
lw = 6.15
bullets(s, ML, 2.15, lw, [
    "Chủ sở hữu nội dung **mã hóa dữ liệu bằng một khóa riêng**.",
    "**Từ khóa** được chia sẻ sau khi mã hóa bằng **khóa công khai của nhà cung cấp dịch vụ tìm kiếm**, hoặc bằng một **khóa bí mật chia sẻ**.",
    "Khi có truy vấn, nhà cung cấp **mở phong bì của tập từ khóa** và **đối sánh với truy vấn**.",
    "Khi khớp, nhà cung cấp **thiết lập kết nối giữa chủ sở hữu và bên yêu cầu**; hai bên **thương lượng điều khoản truy cập mà không có nhà cung cấp dịch vụ tìm kiếm**.",
], size=12, gap=11)
card(s, ML, 4.75, lw, 1.80,
     "Ví dụ 1: tranh luận bầu cử",
     ["Nếu có bài đăng về tranh luận bầu cử trên BBC, **bản gỡ băng** có thể được nhận diện qua các từ khóa như **“electoral debate”, “BBC”** cùng với **ngày tháng** — đủ để tìm ra nó giữa hàng nghìn bản thảo khác."],
     fill=SKY2, head_size=13, body_size=11.5, name="vd1")
rx = ML + lw + 0.40
rw = CW - lw - 0.40
card(s, rx, 2.15, rw, 4.40,
     "Ví dụ 2: định tuyến thư khẩn (Urgent)",
     ["**Bối cảnh:** Alice muốn chuyển tiếp tất cả thư đánh dấu **“Urgent”** cho John trong khi cô ấy đi nghỉ.",
      "**Vấn đề:** Bob gửi email đã **mã hóa bằng khóa công khai của Alice** → **cổng (gateway) không biết** thư nào được đánh dấu “Urgent” để định tuyến.",
      "**Giải pháp:** John **trích xuất từ khóa “urgent”**, thực hiện **mã hóa có thể tìm kiếm** — hay **Mã hóa khóa công khai với tìm kiếm theo từ khóa (PEKS)** — trên từ khóa đã trích xuất và **gửi dữ liệu tới cổng**.",
      "**Kết quả:** cổng **giải mã được danh sách từ khóa** và **định tuyến thông điệp tới John**, mà **vẫn không đọc được nội dung thư**."],
     fill=GRNBG, border=GRNBD, head_color=GREEN, hl=GREEN, head_size=13.5, body_size=11.5,
     gap=9, name="vd2")
footer(s, 16)
notes(s, """
Mã hóa có thể tìm kiếm giải quyết một nghịch lý: dữ liệu đã mã hóa thì làm sao tìm kiếm được?
Ý tưởng là phơi bày một phân đoạn thông tin đủ để nhận diện ngữ cảnh, mà không phơi bày chính nội dung.
Quy trình gồm bốn bước như bên trái: chủ sở hữu mã hóa dữ liệu bằng khóa riêng; từ khóa thì được chia sẻ
dưới dạng mã hóa bằng khóa công khai của nhà cung cấp tìm kiếm hoặc khóa bí mật chia sẻ;
khi có truy vấn, nhà cung cấp mở phong bì từ khóa ra đối sánh; nếu khớp thì nó chỉ làm nhiệm vụ
kết nối hai bên, còn điều khoản truy cập do chủ sở hữu và bên yêu cầu tự thương lượng — không có
mặt nhà cung cấp. Đây là điểm hay: nhà cung cấp tìm kiếm không bao giờ thấy nội dung thật.
Ví dụ bên phải rất dễ hình dung. Alice đi nghỉ, muốn mọi thư khẩn được chuyển cho John.
Nhưng Bob mã hóa thư bằng khóa công khai của Alice, nên cổng thư không biết thư nào là khẩn.
Giải pháp: John trích xuất từ khóa "urgent", áp dụng mã hóa khóa công khai với tìm kiếm theo từ khóa,
rồi gửi dữ liệu này cho cổng. Cổng nhờ đó giải mã được danh sách từ khóa và định tuyến đúng,
mà vẫn không đọc được nội dung thư.
""")

# ================================================================= SLIDE 17
s = new_slide()
head(s, "11.2.5", "Dịch vụ xử lý web (WPS) trên Đám mây")
card(s, ML, 1.48, CW, 0.88, "",
     ["**WPS** của Hiệp hội Không gian Địa lý Mở (**OGC**) định nghĩa một **giao diện được chuẩn hóa** nhằm tạo thuận lợi cho việc **xuất bản các tiến trình không gian địa lý qua Internet** (OGC 2007). Một WPS có thể triển khai trong **bất kỳ mô hình nào trong ba mô hình dịch vụ**."],
     fill=SKY, body_size=12.5, pad=0.18, name="wps def")
half = (CW - 0.45) / 2
card(s, ML, 2.52, half, 2.10,
     "Triển khai trên IaaS",
     ["Người dùng có **toàn quyền kiểm soát tài nguyên**, nhưng **ảo hóa diễn ra ở mức thấp** → người dùng **có trách nhiệm giải quyết nhiều rủi ro bảo mật**.",
      "**Hợp lý khi** tổ chức cần triển khai **nhiều loại WPS khác nhau** và có **đủ nguồn nhân lực quản trị**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="wps iaas")
card(s, ML + half + 0.45, 2.52, half, 2.10,
     "Triển khai trên PaaS",
     ["**Ảo hóa ở mức trừu tượng cao hơn** → nền tảng xử lý giúp một số thách thức về khả năng mở rộng. Dữ liệu đầu vào có thể được **nhúng** hoặc **tham chiếu như một tài nguyên web**.",
      "**Lưu ý:** mã nguồn WPS **không tạo được tệp tạm**; dữ liệu như vậy phải lưu vào **bảng cơ sở dữ liệu của Đám mây**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="wps paas")
bullets(s, ML, 4.80, CW, [
    "WPS có **cường độ tính toán cao** (ví dụ mô hình hóa khí hậu) hưởng lợi từ **khả năng mở rộng tài nguyên**; WPS **đột nhiên trở nên phổ biến** hưởng lợi từ **khả năng mở rộng theo số người dùng**; **WFS** của OGC hưởng lợi từ **khả năng mở rộng về số lượng yêu cầu**.",
    "**Google App Engine (GAE)** cung cấp **xác thực đăng nhập một lần (SSO)** cho lần đăng ký đầu tiên: một **mật khẩu được sinh ra và gửi tới điện thoại của người dùng**, dùng để kích hoạt tài khoản và **sau đó không dùng lại được nữa**.",
    "**Tất cả các Đám mây đều cho phép SSL.** SSL **mã hóa truyền thông mạng**; còn **mã hóa dữ liệu** được cung cấp bởi các **thư viện lập trình và hệ quản trị cơ sở dữ liệu**.",
], size=11.5, gap=10)
footer(s, 17)
notes(s, """
WPS là ví dụ thực tế khép lại mục mã hóa — nó cho ta thấy chọn mô hình dịch vụ nào thì kéo theo
trách nhiệm bảo mật nào.
WPS là chuẩn của OGC, Hiệp hội Không gian Địa lý Mở, định nghĩa giao diện chuẩn hóa để cung cấp
dịch vụ xử lý không gian địa lý qua Internet. Nó triển khai được trên cả ba mô hình dịch vụ.
Trên IaaS: toàn quyền kiểm soát, nhưng ảo hóa ở mức thấp nên người dùng phải tự lo nhiều rủi ro bảo mật.
Sách nói cách này hợp lý khi tổ chức cần nhiều loại WPS khác nhau và có đủ nhân lực quản trị.
Trên PaaS: trừu tượng cao hơn, nền tảng lo giúp phần mở rộng. Nhưng có một ràng buộc kỹ thuật
đáng nhớ: mã nguồn WPS không tạo được tệp tạm, nên dữ liệu tạm phải đẩy vào bảng cơ sở dữ liệu của Đám mây.
Ba gạch đầu dòng cuối là các chi tiết sách nêu: ba kiểu khả năng mở rộng khác nhau;
cơ chế SSO của Google App Engine với mật khẩu dùng một lần gửi qua điện thoại;
và cuối cùng, mọi Đám mây đều cho phép SSL — nhưng nhớ rằng SSL chỉ mã hóa đường truyền,
còn mã hóa dữ liệu thì phải do thư viện lập trình và hệ quản trị cơ sở dữ liệu đảm nhiệm.
""")

# ================================================================= SLIDE 18
s = new_slide()
divider(s, "PHẦN II  ·  MỤC 11.3", "Bảo mật hạ tầng",
        ["Bảo mật thông tin (InfoSec) và quy trình quản lý rủi ro",
         "Cấp độ mạng: Đám mây riêng ≈ extranet an toàn",
         "Ba yếu tố rủi ro của Đám mây công cộng · Lược đồ Vùng tin cậy (TZ)"])
notes(s, """
Phần hai chuyển từ dữ liệu xuống hạ tầng. Câu hỏi ở đây là: khi hạ tầng tính toán nằm ở
nhà cung cấp, mạng và máy chủ bị đe dọa như thế nào, và ta chia vùng tin cậy ra sao.
""")

# ================================================================= SLIDE 19
s = new_slide()
head(s, "11.3 Bảo mật hạ tầng", "Bảo mật thông tin (InfoSec) và quản lý rủi ro")
card(s, ML, 1.48, CW, 1.05, "",
     ["**Bảo mật thông tin (Information security – InfoSec)** là hoạt động thực tiễn nhằm **ngăn chặn việc truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi, kiểm tra, ghi lại hoặc phá hủy thông tin một cách trái phép** — với thông tin ở **bất kỳ dạng nào**, điện tử hay vật lý."],
     fill=SKY, body_size=12.5, pad=0.19, name="infosec")
half = (CW - 0.45) / 2
card(s, ML, 2.70, half, 1.85,
     "Trọng tâm chính",
     ["**Bảo vệ cân bằng bộ ba CIA** — Tính bí mật, Tính toàn vẹn và Tính sẵn sàng của dữ liệu.",
      "Đồng thời **duy trì việc triển khai chính sách một cách hiệu quả**, mà **không cản trở năng suất của tổ chức**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="trongtam")
tf = txbox(s, ML + half + 0.45, 2.72, half, 0.3)
rich(tf.paragraphs[0], "QUY TRÌNH QUẢN LÝ RỦI RO (nhiều bước)", 11.5, BLUE, bold=True, line_spacing=1.0)
steps = ["Nhận diện\ntài sản", "Nguồn\nđe dọa", "Lỗ hổng", "Tác động\ntiềm tàng", "Biện pháp\nkiểm soát", "Đánh giá\nkế hoạch"]
n = len(steps)
bw = (half - 0.16 * (n - 1)) / n
for i, st in enumerate(steps):
    x = ML + half + 0.45 + i * (bw + 0.16)
    b = rect(s, x, 3.12, bw, 0.85, fill=SKY, line=BLUEL, adj=0.10)
    tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.02)
    rich(tf.paragraphs[0], st, 9.5, NAVY, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.1)
    if i < n - 1:
        arrow(s, x + bw + 0.01, 3.47, w=0.14, h=0.12)
tf = txbox(s, ML + half + 0.45, 4.10, half, 0.5)
rich(tf.paragraphs[0],
     "Phần lớn kết quả đạt được **thông qua quy trình quản lý rủi ro nhiều bước** này.",
     11.5, TEXT, hl=NAVY, line_spacing=1.2)
tf = txbox(s, ML, 4.85, CW, 0.3)
rich(tf.paragraphs[0], "ĐỂ HIỂU ĐÚNG CÁC MỐI ĐE DỌA, CẦN HIỂU BẢO MẬT TRUYỀN THÔNG", 11.5, BLUE, bold=True, line_spacing=1.0)
bullets(s, ML, 5.25, CW, [
    "**Bảo mật truyền thông và mạng** khi nó liên quan đến truyền tải **thoại, dữ liệu, đa phương tiện và fax**, xét trên phương diện **mạng cục bộ, mạng diện rộng và mạng truy cập từ xa**.",
    "**Internet / intranet / extranet** xét trên phương diện **tường lửa, bộ định tuyến, cổng nối và các giao thức khác nhau**.",
], size=12, gap=10)
footer(s, 19)
notes(s, """
Mục 11.3 mở đầu bằng định nghĩa InfoSec. Định nghĩa này dài nhưng đáng đọc kỹ vì nó liệt kê
đủ các hành vi trái phép cần ngăn chặn: truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi, kiểm tra,
ghi lại, phá hủy. Và thông tin ở đây là bất kỳ dạng nào — điện tử hay vật lý.
Trọng tâm của InfoSec là bảo vệ cân bằng bộ ba CIA, nhưng có một vế thứ hai rất thực tế mà
sinh viên hay bỏ qua: phải làm mà không cản trở năng suất của tổ chức. Bảo mật quá chặt đến mức
không ai làm việc được thì cũng là thất bại.
Cách đạt được điều đó là quy trình quản lý rủi ro nhiều bước: nhận diện tài sản, nguồn đe dọa,
lỗ hổng, tác động tiềm tàng, các biện pháp kiểm soát khả dĩ, rồi đánh giá hiệu quả của kế hoạch.
Và để hiểu mối đe dọa với hạ tầng Đám mây, sách yêu cầu hiểu bảo mật truyền thông — gồm hai nhóm
nội dung ở cuối slide.
""")

# ================================================================= SLIDE 20
s = new_slide()
head(s, "11.3.1 Cấp độ mạng", "Đám mây riêng ≈ Extranet an toàn")
lw = 4.55
card(s, ML, 1.48, lw, 2.35,
     "Với Đám mây riêng...",
     ["**Không có cuộc tấn công mới, lỗ hổng mới, hay thay đổi nào về rủi ro** đặc thù cho tô-pô này mà nhân sự bảo mật thông tin cần cân nhắc."],
     fill=GRNBG, border=GRNBD, head_color=GREEN, hl=GREEN, head_size=14, body_size=12, name="private")
textblock(s, ML + 0.18, 2.80, lw - 0.36, [
    "Kiến trúc CNTT của tổ chức **có thể thay đổi**, nhưng **tô-pô mạng hiện tại có lẽ sẽ không thay đổi đáng kể**."],
    size=11.5, color=TEXT, hl=GREEN)
bullets(s, ML, 4.00, lw, [
    "Nếu đã có **extranet riêng** thì **tô-pô cho Đám mây riêng gần như đã sẵn có**.",
    "Các **cân nhắc bảo mật hiện nay cũng áp dụng** cho hạ tầng Đám mây riêng.",
    "Các **công cụ bảo mật đang có** (hoặc nên có) **vẫn cần thiết** và **vận hành theo cùng một cách**.",
], size=11.5, gap=9)
# hình 11.1
img_w = CW - lw - 0.45
s.shapes.add_picture("assets/images/fig11_1_extranet_cloud_topology.png",
                     Inches(ML + lw + 0.45), Inches(1.60), width=Inches(img_w))
tf = txbox(s, ML + lw + 0.45, 1.60 + img_w / 1.784 + 0.12, img_w, 0.35)
rich(tf.paragraphs[0], "Hình 11.1 — Những điểm tương đồng giữa một extranet an toàn và một Đám mây riêng",
     10.5, MUTED, italic=True, align=PP_ALIGN.CENTER, line_spacing=1.15)
tf = txbox(s, ML + lw + 0.45, 1.60 + img_w / 1.784 + 0.58, img_w, 0.7)
rich(tf.paragraphs[0],
     "**Internet:** mở cho tất cả mọi người.  ·  **Intranet:** mạng dành cho nhóm nhỏ, chỉ thành viên truy cập được.  ·  **Extranet:** dùng bởi người thuộc một mạng cụ thể, có định danh đăng nhập và mật khẩu.",
     10.5, TEXT, hl=NAVY, line_spacing=1.25)
footer(s, 20)
notes(s, """
Đây là một thông điệp trấn an nhưng rất quan trọng về mặt thực tiễn.
Khi xét cấp độ mạng, sách nói rõ: với Đám mây riêng, không có cuộc tấn công mới, không có lỗ hổng mới,
cũng không có thay đổi nào về rủi ro mà nhân sự bảo mật cần cân nhắc thêm.
Lý do: kiến trúc công nghệ thông tin có thể đổi, nhưng tô-pô mạng thì gần như không đổi.
Nếu tổ chức đã có một extranet riêng — tức là một intranet cho phép truy cập một phần từ bên ngoài
qua Internet một cách an toàn — thì thực tế tô-pô mạng cho Đám mây riêng đã có sẵn rồi.
Hình 11.1 minh họa đúng điều đó: bên trái là Internet mở cho mọi người và mạng khách hàng,
ở giữa là extranet đi qua tường lửa, bên trong là intranet với máy chủ riêng.
Nhắc nhanh ba khái niệm: Internet mở cho tất cả; intranet là mạng của nhóm nhỏ, chỉ thành viên truy cập;
extranet dành cho người thuộc một mạng cụ thể, có định danh đăng nhập và mật khẩu.
Đám mây riêng thì yên tâm như vậy. Còn Đám mây công cộng thì sao? Slide sau.
""")

# ================================================================= SLIDE 21
s = new_slide()
head(s, "11.3.1 Cấp độ mạng", "Đám mây công cộng: ba yếu tố rủi ro đáng kể")
risks = [
    ("Tính bí mật & toàn vẹn của dữ liệu đang truyền",
     "Tài nguyên trước đây **bị giới hạn trong mạng riêng** nay **bị phơi bày ra Internet** — một mạng công cộng chia sẻ thuộc về một **nhà cung cấp Đám mây bên thứ ba**. Dùng **HTTPS thay vì HTTP** đã giảm thiểu được rủi ro về tính toàn vẹn; người dùng **HTTP** phải đối mặt với rủi ro **dữ liệu bị thay đổi mà không hay biết**."),
    ("Kiểm soát truy cập phù hợp",
     "**Xác thực, ủy quyền và kiểm toán** đối với **bất kỳ tài nguyên nào** đang sử dụng ở nhà cung cấp. Khả năng **kiểm toán mạng của nhà cung cấp**, chưa nói đến **giám sát thời gian thực**, gần như **là không tồn tại**."),
    ("Tính sẵn sàng của tài nguyên hướng Internet",
     "Sự phụ thuộc vào bảo mật mạng **đã tăng lên**, bởi **lượng dữ liệu và số lượng nhân sự** phụ thuộc vào các **thiết bị lưu trữ bên ngoài** ngày càng nhiều."),
]
cw3 = (CW - 2 * 0.34) / 3
for i, (t, d) in enumerate(risks):
    x = ML + i * (cw3 + 0.34)
    rect(s, x, 1.75, cw3, 3.05, fill=SKY2, line=BORDER, adj=0.05)
    c = rect(s, x + 0.22, 1.50, 0.52, 0.52, fill=RED, shape=MSO_SHAPE.OVAL)
    tf = c.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tf.paragraphs[0], str(i + 1), 18, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    tf = txbox(s, x + 0.22, 2.22, cw3 - 0.44, 0.7)
    rich(tf.paragraphs[0], t, 13, NAVY, bold=True, line_spacing=1.1)
    textblock(s, x + 0.22, 3.00, cw3 - 0.44, [d], size=11, color=TEXT, hl=BLUE)
card(s, ML, 4.94, CW, 1.68,
     "⚠  Cấu hình sai (misconfiguration) vẫn là rủi ro sống động",
     ["Ba yếu tố rủi ro trên **phải ở mức chấp nhận được** đối với một tổ chức — nhưng **cấu hình sai vẫn có thể ảnh hưởng đến tính sẵn sàng** của các tài nguyên dựa trên Đám mây.",
      "**Nghiên cứu trình bày trước NANOG (tháng 2/2006):** hàng trăm cấu hình sai như vậy mỗi tháng.  ·  **Tháng 2/2008:** Pakistan Telecom công bố một **tuyến giả (dummy route)** cho YouTube tới đối tác PCCW nhằm chặn YouTube trong nước → **YouTube không thể truy cập được trên toàn cầu trong hai giờ.**"],
     fill=REDBG, border=REDBD, head_color=RED, hl=RED, head_size=13.5, body_size=11.5,
     gap=7, name="misconfig")
footer(s, 21)
notes(s, """
Với Đám mây công cộng thì câu chuyện khác hẳn. Sách chỉ ra đúng ba yếu tố rủi ro đáng kể.
Thứ nhất là tính bí mật và toàn vẹn của dữ liệu đang truyền đi tới và đi từ nhà cung cấp.
Tài nguyên trước đây nằm gọn trong mạng riêng nay bị phơi ra Internet. Sách có một nhận xét đắt giá:
ai dùng HTTPS thay cho HTTP thì đã giảm được rủi ro về toàn vẹn; còn ai vẫn dùng HTTP thì
dữ liệu có thể bị thay đổi mà họ không hề hay biết.
Thứ hai là kiểm soát truy cập phù hợp — xác thực, ủy quyền, kiểm toán. Điểm đáng lo: khả năng
kiểm toán mạng của nhà cung cấp, chưa nói tới giám sát thời gian thực, gần như không tồn tại.
Thứ ba là tính sẵn sàng của các tài nguyên hướng Internet, vì ngày càng nhiều dữ liệu và nhân sự
phụ thuộc vào thiết bị lưu trữ bên ngoài.
Khối đỏ cuối là ví dụ lịch sử rất hay. Nghiên cứu trình bày trước NANOG năm 2006 đếm được
hàng trăm cấu hình sai mỗi tháng. Và tháng 2 năm 2008, Pakistan Telecom công bố một tuyến giả
cho YouTube nhằm chặn YouTube trong nước, kết quả là YouTube không truy cập được trên toàn cầu
suốt hai giờ. Một cấu hình sai ở một nhà mạng làm sập dịch vụ toàn thế giới — đó là minh chứng
cho việc tính sẵn sàng phụ thuộc vào bên thứ ba.
""")

# ================================================================= SLIDE 22
s = new_slide()
head(s, "11.3.2", "Lược đồ Vùng tin cậy (Trust Zones – TZ)")
card(s, ML, 1.48, CW, 1.05, "",
     ["**TZ = Phân đoạn mạng (network segmentation)  +  Quản lý danh tính và truy cập (IAM)**. Chúng định nghĩa các **ranh giới vật lý, logic hoặc ảo** quanh tài nguyên mạng; được triển khai bằng **thiết bị vật lý**, bằng **tường lửa ảo / chuyển mạch ảo**, hoặc **cả hai**."],
     fill=SKY, body_size=12.5, pad=0.19, name="tz def")
card(s, ML, 2.70, CW, 1.34,
     "Mô hình đe dọa: kẻ nội gián của CSP (CSP insider)",
     ["Nhân sự của CSP có **quyền truy cập vật lý** vào trung tâm dữ liệu có thể phá vỡ các biện pháp kiểm soát bảo mật **bằng cách truy cập trực tiếp vào máy vật lý**. Tuy nhiên **số lượng máy rất lớn làm phức tạp thêm nhiệm vụ** — kẻ tấn công **trước tiên phải nhận diện được phần cứng đang lưu trữ dữ liệu mục tiêu**."],
     fill=AMBBG, border=AMBBD, head_color=AMB, hl=AMB, head_size=13.5, body_size=11.5, name="tz threat")
flow(s, ML + 0.35, 4.14, CW - 0.7, 0.92,
     ["Liệt kê các VM\nđang hoạt động", "Thu hẹp danh sách\nnhờ dữ liệu cấu hình",
      "Ánh xạ vào sơ đồ\nbố trí trung tâm dữ liệu", "Tiêm mã độc,\nphát tín hiệu (beaconing)"],
     gap=0.42, size=11.5, last_fill=REDBG, last_border=RED, last_color=RED, arrow_color=BLUEL)
half = (CW - 0.45) / 2
card(s, ML, 5.18, half, 1.38,
     "Tín hiệu giúp thu hẹp danh sách",
     ["**Nhóm bảo mật (security group)**, **các cổng đang mở**, **dữ liệu IAM**, **quy ước đặt tên của bên thuê**, **kích cỡ tương đối về bộ nhớ / đĩa / CPU / I/O**."],
     fill=SKY2, head_size=13, body_size=11.5, name="tz signals")
card(s, ML + half + 0.45, 5.18, half, 1.38,
     "Phòng thủ",
     ["**Phân đoạn / ngăn thành các khoang** trong trung tâm dữ liệu và **giữ riêng biệt bản đồ vật lý với bản đồ logic** → làm phức tạp thêm nhiệm vụ của kẻ tấn công."],
     fill=GRNBG, border=GRNBD, head_color=GREEN, hl=GREEN, head_size=13, body_size=11.5, name="tz defense")
footer(s, 22)
notes(s, """
Vùng tin cậy là câu trả lời của sách cho một mối đe dọa rất khó chịu: mối đe dọa dai dẳng nâng cao
và đặc biệt là kẻ nội gián của chính nhà cung cấp.
Định nghĩa: TZ là sự kết hợp giữa phân đoạn mạng và quản lý danh tính, truy cập. Nó định nghĩa
ranh giới vật lý, logic hoặc ảo quanh tài nguyên mạng, triển khai bằng thiết bị vật lý,
bằng tường lửa và chuyển mạch ảo, hoặc cả hai.
Mô hình đe dọa ở khối vàng: nhân sự CSP có quyền truy cập vật lý vào trung tâm dữ liệu, nên về lý thuyết
họ có thể chạm tay vào máy chứa dữ liệu của ta. Nhưng số lượng máy quá lớn nên kẻ tấn công trước hết
phải tìm ra đúng phần cứng đang chứa dữ liệu mục tiêu.
Sơ đồ mô tả đúng bốn bước tấn công: liệt kê các máy ảo của cơ quan, thu hẹp danh sách nhờ dữ liệu cấu hình,
ánh xạ vào sơ đồ bố trí trung tâm dữ liệu, và cuối cùng tiêm mã độc qua truy cập vật lý rồi phát tín hiệu
về các nút điều khiển để mở rộng tấn công.
Những tín hiệu nào giúp thu hẹp? Nhóm bảo mật, cổng đang mở, dữ liệu IAM, quy ước đặt tên của bên thuê,
và cả kích cỡ tương đối về bộ nhớ, đĩa, CPU, I/O — vì máy chủ web lớn hay cơ sở dữ liệu lớn nhìn là nhận ra.
Phòng thủ chính là phân đoạn trung tâm dữ liệu thành các khoang và giữ riêng bản đồ vật lý với bản đồ logic.
""")

# ================================================================= SLIDE 23
s = new_slide()
divider(s, "PHẦN III  ·  MỤC 11.4 – 11.5", "Bảo mật ứng dụng\nPaaS và SaaS",
        ["Ai bảo mật cái gì trong PaaS · Kiểm soát truy cập · Gia cố OS · SSO",
         "Bảo mật ứng dụng SaaS và giới hạn của kiểm soát chi tiết",
         "Lược đồ FHE cho SaaS · Kiểm soát truy cập mạng và người dùng"])
notes(s, """
Phần ba đi vào tầng ứng dụng, và đây chính là nơi trả lời mục tiêu thứ ba của chương:
so sánh trách nhiệm bảo mật giữa các mô hình dịch vụ. Ta xem PaaS trước, rồi tới SaaS.
""")

# ================================================================= SLIDE 24
s = new_slide()
head(s, "11.4 Bảo mật ứng dụng PaaS", "Ai bảo mật cái gì?")
half = (CW - 0.45) / 2
card(s, ML, 1.48, half, 1.52,
     "Hai loại nhà cung cấp PaaS",
     ["**Nhà cung cấp phần mềm:** Bungee, Etelos, GigaSpaces, Eucalyptus.",
      "**CSP:** Google App Engine, Force.com của Salesforce.com, Microsoft Azure, Intuit QuickBase."],
     fill=SKY, head_size=14, body_size=11.5, gap=7, name="paas vendors")
card(s, ML + half + 0.45, 1.48, half, 1.52,
     "Trách nhiệm bảo mật",
     ["**CSP của PaaS** chịu trách nhiệm bảo mật **ngăn xếp phần mềm nền tảng**, bao gồm cả **bộ máy thực thi (runtime engine)** chạy các ứng dụng của khách hàng."],
     fill=SKY, head_size=14, body_size=11.5, gap=7, name="paas resp")
card(s, ML, 3.18, half, 1.98,
     "Phụ thuộc bên thứ ba",
     ["Ứng dụng PaaS **có thể sử dụng ứng dụng, thành phần hoặc dịch vụ web của bên thứ ba** → **nhà cung cấp bên thứ ba** có thể phải chịu trách nhiệm bảo mật các dịch vụ đó.",
      "→ Khách hàng nên **hiểu rõ sự phụ thuộc** của ứng dụng mình vào **tất cả các dịch vụ** và **đánh giá rủi ro** liên quan đến bên thứ ba."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="paas 3rd")
card(s, ML + half + 0.45, 3.18, half, 1.98,
     "Khuyến nghị thực tiễn",
     ["PaaS vẫn **đang ở giai đoạn còn non trẻ**: chưa có Đám mây công cộng lớn nào dùng phần mềm PaaS thương mại có sẵn hoặc mã nguồn mở như Eucalyptus.",
      "→ Tổ chức đánh giá phần mềm PaaS nên **thực hiện đánh giá rủi ro** và **áp dụng tiêu chuẩn bảo mật phần mềm như khi mua sắm bất kỳ phần mềm doanh nghiệp nào**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="paas advice")
card(s, ML, 5.28, CW, 1.62,
     "Vấn đề minh bạch (transparency)",
     ["Cho đến nay, các **CSP vẫn miễn cưỡng** trong việc chia sẻ thông tin liên quan đến **bảo mật nền tảng**, với lập luận rằng thông tin như vậy **có thể mang lại lợi thế cho tin tặc**.",
      "→ Tuy nhiên, **khách hàng doanh nghiệp nên đòi hỏi sự minh bạch** từ các CSP và **tìm kiếm thông tin cần thiết** để thực hiện đánh giá rủi ro và quản lý bảo mật liên tục."],
     fill=AMBBG, border=AMBBD, head_color=AMB, hl=AMB, head_size=13.5, body_size=11.5,
     gap=7, name="paas transparency")
footer(s, 24)
notes(s, """
Mục 11.4 nói về PaaS. Trước hết sách phân loại nhà cung cấp PaaS làm hai nhóm: nhóm nhà cung cấp
phần mềm như Bungee, Etelos, GigaSpaces, Eucalyptus; và nhóm CSP như Google App Engine,
Force.com của Salesforce, Microsoft Azure, Intuit QuickBase.
Về trách nhiệm: CSP của PaaS lo bảo mật ngăn xếp phần mềm nền tảng, bao gồm cả bộ máy thực thi
chạy ứng dụng của khách hàng. Nhưng đây mới là điểm tinh tế: ứng dụng PaaS thường gọi tới ứng dụng,
thành phần hay dịch vụ web của bên thứ ba, và khi đó trách nhiệm bảo mật thuộc về bên thứ ba đó.
Vì vậy khách hàng phải hiểu rõ ứng dụng của mình phụ thuộc vào những dịch vụ nào, và đánh giá rủi ro
cho từng phụ thuộc.
Khuyến nghị thực tiễn của sách: PaaS còn non trẻ, nên hãy đánh giá rủi ro và áp dụng đúng tiêu chuẩn
bảo mật phần mềm như khi mua bất kỳ phần mềm doanh nghiệp nào — đừng vì nó là "cloud" mà nới lỏng.
Cuối cùng là vấn đề minh bạch, rất thời sự: các CSP ngại chia sẻ thông tin bảo mật nền tảng vì sợ
giúp tin tặc. Sách phản biện lại: khách hàng doanh nghiệp nên đòi hỏi minh bạch để còn đánh giá rủi ro
và quản lý bảo mật liên tục.
""")

# ================================================================= SLIDE 25
s = new_slide()
head(s, "11.4 Bảo mật ứng dụng PaaS", "Kiểm soát truy cập · Gia cố hệ điều hành · SSO")
col = (CW - 2 * 0.34) / 3
card(s, ML, 1.48, col, 5.08,
     "① Quản lý kiểm soát truy cập",
     ["Bao trùm **người dùng thường** và cả **quản trị viên hệ thống có đặc quyền**.",
      "Cần giải quyết bốn câu hỏi:",
      "  • **Gán quyền hạn (entitlement)** cho người dùng",
      "  • Gán quyền **dựa trên chức năng công việc**",
      "  • **Phương thức và mức độ mạnh** của xác thực",
      "  • **Kiểm toán và báo cáo** để xác minh"],
     fill=SKY, head_size=13.5, body_size=11, gap=5, name="paas ac")
card(s, ML + col + 0.34, 1.48, col, 5.08,
     "② Gia cố hệ điều hành máy chủ",
     ["Lỗ hổng trong **hệ điều hành máy chủ (host)** có thể **lan ngược lên hệ điều hành của máy ảo**.",
      "Xâm phạm VM → chỉ hỏng **miền khách**. Xâm phạm **host** → kẻ xâm nhập **truy cập được tất cả dịch vụ trên tất cả máy ảo** do máy đó lưu trữ."],
     fill=REDBG, border=REDBD, head_color=RED, hl=RED, head_size=13.5, body_size=11, gap=6, name="paas hard")
bullets(s, ML + col + 0.34 + 0.18, 3.50, col - 0.36, [
    "**Mật khẩu mạnh**, dài, khó đoán, kết hợp chữ – số – ký hiệu, **thay đổi thường xuyên**",
    "**Vô hiệu hóa dịch vụ không cần thiết**, đặc biệt là dịch vụ mạng",
    "**Yêu cầu xác thực đầy đủ** cho việc kiểm soát truy cập",
    "**Đặt tường lửa riêng lẻ** cho máy chủ",
    "**Vá lỗi và cập nhật thường xuyên**, sau khi kiểm thử ngoài môi trường sản xuất",
], size=10.5, gap=8, mark="▸", mark_color=RED, indent=0.18)
card(s, ML + 2 * (col + 0.34), 1.48, col, 5.08,
     "③ Đăng nhập một lần (SSO)",
     ["Người dùng cung cấp **một ID và mật khẩu cho mỗi phiên làm việc**, sau đó **được tự động đăng nhập vào tất cả các ứng dụng cần thiết**.",
      "Để bảo mật SSO, **mật khẩu không được lưu trữ hoặc truyền đi ở dạng rõ**.",
      "**Ưu điểm**",
      "  • Sử dụng **mật khẩu mạnh hơn**",
      "  • **Quản trị dễ dàng hơn**",
      "  • **Ít thời gian hơn** để truy cập tài nguyên",
      "**Nhược điểm lớn**",
      "  • Một khi đã qua **lần đăng nhập ban đầu**, người dùng có thể **tự do đi lại trong các tài nguyên mạng mà không có bất kỳ hạn chế nào**.",
      "**Ví dụ:** đăng nhập Gmail → tự động có quyền truy cập **YouTube, Google Drive, Google Photos** và các sản phẩm khác của Google."],
     fill=SKY2, head_size=13.5, body_size=11, gap=5, name="paas sso")
footer(s, 25)
notes(s, """
Slide này gom ba biện pháp cụ thể cho PaaS.
Thứ nhất, quản lý kiểm soát truy cập. Điểm cần nhớ: nó bao trùm cả người dùng thường lẫn quản trị viên
có đặc quyền. Bốn câu hỏi phải trả lời là: gán quyền hạn thế nào, gán dựa trên chức năng công việc ra sao,
xác thực bằng phương thức nào và mạnh đến đâu, và kiểm toán báo cáo thế nào để xác minh.
Thứ hai, gia cố hệ điều hành máy chủ. Đây là ý quan trọng nhất của slide: lỗ hổng trong hệ điều hành
của máy chủ vật lý lan ngược lên hệ điều hành máy ảo. Nếu chỉ một VM bị xâm phạm thì thiệt hại giới hạn
trong miền khách; nhưng nếu host bị xâm phạm thì kẻ tấn công chạm được vào tất cả dịch vụ trên tất cả
máy ảo mà máy đó lưu trữ. Năm kỹ thuật gia cố ở dưới các bạn nên thuộc: mật khẩu mạnh, vô hiệu hóa
dịch vụ không cần thiết, xác thực đầy đủ, tường lửa riêng cho từng máy chủ, và vá lỗi thường xuyên
sau khi kiểm thử ngoài môi trường sản xuất.
Thứ ba là SSO. Ưu điểm thì rõ: mật khẩu mạnh hơn, quản trị dễ hơn, truy cập nhanh hơn.
Nhưng nhược điểm lớn cũng phải nói thẳng: qua được cửa đầu tiên rồi thì người dùng tự do đi lại
trong mạng mà không bị hạn chế. Ví dụ quen thuộc: đăng nhập Gmail xong là có luôn YouTube,
Google Drive, Google Photos.
""")

# ================================================================= SLIDE 26
s = new_slide()
head(s, "11.5 Bảo mật ứng dụng SaaS", "Nhà cung cấp quản lý toàn bộ — khách hàng còn lại gì?")
half = (CW - 0.45) / 2
card(s, ML, 1.48, half, 2.06,
     "Phân chia trách nhiệm trong SaaS",
     ["Mô hình SaaS quy định nhà cung cấp **quản lý toàn bộ bộ ứng dụng** được chuyển giao tới người dùng → **nhà cung cấp chịu trách nhiệm chính** về bảo mật các ứng dụng và thành phần mà họ cung cấp.",
      "**Khách hàng** thường chịu trách nhiệm về các **chức năng bảo mật vận hành**: **quản lý người dùng** và **quản lý truy cập**, ở mức độ được nhà cung cấp hỗ trợ."],
     fill=SKY, head_size=14, body_size=11.5, gap=7, name="saas resp")
card(s, ML + half + 0.45, 1.48, half, 2.06,
     "Cần yêu cầu thông tin gì từ nhà cung cấp?",
     ["Đây là **thông lệ phổ biến**: khách hàng yêu cầu thông tin liên quan đến **thực hành bảo mật của nhà cung cấp**, bao trùm:",
      "**Thiết kế · Kiến trúc · Phát triển · Kiểm thử bảo mật ứng dụng hộp đen và hộp trắng · Quản lý phát hành.**"],
     fill=SKY2, head_size=14, body_size=11.5, gap=7, name="saas ask")
card(s, ML, 3.70, CW, 1.55,
     "Khi kiểm soát chi tiết (fine-grained) không đủ",
     ["Một số ứng dụng SaaS như **Google Apps** có tính năng tích hợp sẵn để người dùng cuối **gán quyền đọc và ghi** cho người dùng khác.",
      "Tuy nhiên các tính năng **quản lý đặc quyền này không có khả năng cấp phát chi tiết ở mức mịn (fine-grained)** → có thể tạo ra **điểm yếu không phù hợp với tiêu chuẩn kiểm soát truy cập của tổ chức**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="saas fine")
card(s, ML, 5.38, CW, 1.28,
     "Ví dụ: hình ảnh nhúng trong Google Docs",
     ["Các **hình ảnh được nhúng và lưu trữ trong Google Docs không được bảo vệ theo cùng cách** mà tài liệu được bảo vệ bằng các biện pháp kiểm soát chia sẻ. → Nếu bạn từng chia sẻ một tài liệu chứa hình ảnh nhúng, **người kia vẫn xem được những hình ảnh đó ngay cả sau khi bạn đã ngừng chia sẻ tài liệu**."],
     fill=REDBG, border=REDBD, head_color=RED, hl=RED, head_size=13.5, body_size=11.5, name="gdocs")
footer(s, 26)
notes(s, """
Sang SaaS. Ở mô hình này nhà cung cấp quản lý toàn bộ bộ ứng dụng, nên phần lớn trách nhiệm bảo mật
ứng dụng và thành phần thuộc về họ. Khách hàng thì lo phần bảo mật vận hành — chủ yếu là quản lý
người dùng và quản lý truy cập, và chỉ ở mức mà nhà cung cấp hỗ trợ.
Vì khách hàng không kiểm soát được gì nhiều, thông lệ phổ biến là yêu cầu nhà cung cấp cung cấp
thông tin về thực hành bảo mật của họ: thiết kế, kiến trúc, phát triển, kiểm thử bảo mật ứng dụng
cả hộp đen lẫn hộp trắng, và quản lý phát hành.
Hai khối dưới là một cảnh báo thực tế. Google Apps cho phép người dùng cuối gán quyền đọc ghi,
nhưng quản lý đặc quyền không đủ mịn, nên có thể không khớp với tiêu chuẩn kiểm soát truy cập
của tổ chức.
Ví dụ cụ thể mà sách đưa ra rất dễ nhớ: hình ảnh nhúng trong Google Docs không được bảo vệ giống
như bản thân tài liệu. Nếu bạn từng chia sẻ tài liệu có hình nhúng, thì người kia vẫn xem được
những hình ảnh đó ngay cả sau khi bạn đã ngừng chia sẻ. Đây là bài học: quyền kiểm soát chia sẻ
của bạn có thể không bao trùm hết mọi thành phần của dữ liệu.
""")

# ================================================================= SLIDE 27
s = new_slide()
head(s, "11.5.1 Lược đồ FHE cho bảo mật SaaS", "Ví dụ minh họa bằng số")
card(s, ML, 1.48, CW, 1.02, "",
     ["Không giống **mã hóa đồng cấu bộ phận (partially homomorphic)** vốn chỉ cho phép **một số phép toán** trên bản mã (phép cộng, phép nhân, hàm bậc hai...), **FHE hỗ trợ việc tính toán tùy ý trên bản mã**. Chương trình **không bao giờ cần giải mã đầu vào** → có thể **chạy bởi một bên không đáng tin cậy mà không tiết lộ đầu vào và trạng thái nội bộ**."],
     fill=SKY, body_size=12.5, pad=0.18, name="fhe def")
tf = txbox(s, ML, 2.68, CW, 0.3)
rich(tf.paragraphs[0], "VÍ DỤ: DOANH NGHIỆP B VÀ TẬP DỮ LIỆU RẤT QUAN TRỌNG (VIDS)", 11.5, GREEN, bold=True, line_spacing=1.0)
steps = [
    ("Mã hóa", "VIDS gồm các số **5** và **10**.\nDoanh nghiệp B **nhân mỗi phần tử với 2**\n→ tập mới: **10** và **20**.", "5, 10  →  10, 20"),
    ("Lưu trữ", "Gửi tập **đã mã hóa** lên Đám mây để **lưu trữ an toàn**.\nVài tháng sau, **chính phủ yêu cầu tổng** các phần tử VIDS.", "☁  10, 20"),
    ("Tính toán", "Doanh nghiệp B **rất bận** → yêu cầu **nhà cung cấp Đám mây** thực hiện phép toán.\nNhà cung cấp **chỉ có quyền truy cập vào dữ liệu đã mã hóa**.", "10 + 20 = 30"),
    ("Giải mã", "Doanh nghiệp B **giải mã câu trả lời** (chia 2) và **cung cấp cho chính phủ** câu trả lời đã giải mã.", "30  →  15"),
]
cw4 = (CW - 3 * 0.30) / 4
for i, (t, d, f) in enumerate(steps):
    x = ML + i * (cw4 + 0.30)
    fill = GRNBG if i == 3 else SKY2
    bd = GRNBD if i == 3 else BORDER
    rect(s, x, 3.32, cw4, 3.15, fill=fill, line=bd, adj=0.05)
    c = rect(s, x + 0.20, 3.52, 0.44, 0.44, fill=GREEN if i == 3 else BLUE, shape=MSO_SHAPE.OVAL)
    tfc = c.text_frame; tfc.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tfc.paragraphs[0], str(i + 1), 15, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    tf = txbox(s, x + 0.76, 3.58, cw4 - 0.96, 0.34)
    rich(tf.paragraphs[0], t, 14, NAVY, bold=True, line_spacing=1.0)
    fb = rect(s, x + 0.20, 4.12, cw4 - 0.40, 0.55, fill=WHITE, line=GREEN if i == 3 else BLUE, adj=0.14)
    tfb = fb.text_frame; tfb.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tfb.paragraphs[0], f, 14, GREEN if i == 3 else NAVY, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    textblock(s, x + 0.20, 4.85, cw4 - 0.40, d.split("\n"), size=11, color=TEXT, hl=NAVY, gap=4)
    if i < 3:
        arrow(s, x + cw4 + 0.02, 4.32, w=0.24, h=0.16, color=BLUEL)
footer(s, 27)
notes(s, """
Đây là slide mình muốn các bạn nhớ nhất về FHE, vì nó biến một khái niệm trừu tượng thành bốn con số.
Trước hết phân biệt: mã hóa đồng cấu bộ phận chỉ cho phép một số phép toán trên bản mã,
còn mã hóa đồng cấu toàn phần hỗ trợ tính toán tùy ý. Hệ quả rất mạnh: chương trình không bao giờ
phải giải mã đầu vào, nên có thể để một bên không đáng tin cậy chạy nó mà không lộ đầu vào
lẫn trạng thái nội bộ.
Ví dụ của sách: Doanh nghiệp B có tập dữ liệu rất quan trọng gồm hai số 5 và 10.
Bước một, để mã hóa, B nhân mỗi phần tử với 2, được 10 và 20. Đây là một "phép mã hóa" đơn giản
hóa cho dễ hiểu thôi.
Bước hai, B gửi tập đã mã hóa lên Đám mây. Vài tháng sau chính phủ hỏi tổng các phần tử VIDS.
Bước ba, B bận nên nhờ nhà cung cấp Đám mây tính. Nhà cung cấp chỉ nhìn thấy 10 và 20, cộng lại
được 30 và trả về.
Bước bốn, B giải mã 30 — tức là chia 2 — được 15, và đưa cho chính phủ con số 15.
Kết quả đúng bằng 5 cộng 10. Nhà cung cấp đã làm được việc hữu ích cho B mà chưa từng nhìn thấy
dữ liệu thật. Đó chính là tinh thần của FHE.
""")

# ================================================================= SLIDE 28
s = new_slide()
head(s, "11.5.1", "Kiểm soát truy cập trong SaaS")
half = (CW - 0.45) / 2
card(s, ML, 1.48, half, 3.20,
     "Kiểm soát truy cập MẠNG  →  vai trò suy giảm",
     ["Người dùng truy cập dịch vụ Đám mây **từ bất kỳ máy chủ nào có kết nối Internet** → kiểm soát truy cập dựa trên mạng **đóng vai trò ngày càng suy giảm**.",
      "Lý do: kiểm soát truyền thống dựa trên **thuộc tính của máy chủ (host-based)**, mà điều này **hầu hết trường hợp là không thỏa đáng**, **không duy nhất giữa các người dùng**, và có thể gây **hạch toán không chính xác**.",
      "Trong Đám mây, nó thể hiện dưới dạng **chính sách tường lửa Đám mây** tại **điểm vào và điểm ra**, dùng tham số **TCP/IP** tiêu chuẩn: **IP nguồn, cổng nguồn, IP đích, cổng đích**."],
     fill=SKY2, head_size=13.5, body_size=11.5, gap=7, name="saas nac")
card(s, ML + half + 0.45, 1.48, half, 3.20,
     "Kiểm soát truy cập NGƯỜI DÙNG  →  cần nhấn mạnh",
     ["**Ràng buộc chặt chẽ danh tính người dùng với tài nguyên** trong Đám mây → hỗ trợ **kiểm soát truy cập ở mức chi tiết mịn**, **hạch toán người dùng**, **tuân thủ** và **bảo vệ dữ liệu**.",
      "Các biện pháp chủ chốt: **xác thực mạnh**, **đăng nhập một lần (SSO)**, **quản lý đặc quyền**, **ghi nhật ký và giám sát**.",
      "**ISO/IEC 27002** đã định nghĩa **sáu mục tiêu kiểm soát truy cập**, bao trùm kiểm soát truy cập của **người dùng cuối, người dùng đặc quyền, mạng, ứng dụng và thông tin**."],
     fill=SKY, head_size=13.5, body_size=11.5, gap=7, name="saas uac")
card(s, ML, 4.88, CW, 1.15,
     "Giám sát trên IaaS",
     ["Tương tự việc giám sát dịch vụ SaaS, khách hàng đang lưu trữ ứng dụng trên nền tảng **IaaS** nên thực hiện các **bước bổ sung để giám sát tình trạng của ứng dụng** được lưu trữ. Ví dụ: lưu trữ ứng dụng thương mại điện tử trên **Amazon EC2** thì phải giám sát **cả ứng dụng lẫn các thực thể máy chủ ảo**."],
     fill=SKY2, head_size=13.5, body_size=11.5, name="iaas monitor")
tfx = txbox(s, ML, 6.20, CW, 0.4)
rich(tfx.paragraphs[0],
     "Kết luận: trong Đám mây, trọng tâm dịch chuyển từ **“bạn đang ở đâu trong mạng”** sang **“bạn là ai”**.",
     12.5, NAVY, hl=BLUE, align=PP_ALIGN.CENTER, line_spacing=1.2)
footer(s, 28)
notes(s, """
Đây là một trong những ý hay nhất chương, và cũng rất dễ ra đề.
Trong mô hình truyền thống, ta bảo vệ tài nguyên bằng cách kiểm soát máy nào được kết nối —
tức dựa trên thuộc tính của máy chủ như địa chỉ IP. Nhưng trong Đám mây, người dùng truy cập
từ bất kỳ máy nào có Internet, nên kiểu kiểm soát này suy giảm vai trò: nó không thỏa đáng,
không duy nhất giữa các người dùng, và có thể dẫn tới hạch toán sai.
Nó vẫn tồn tại, dưới dạng chính sách tường lửa Đám mây ở điểm vào và điểm ra, dùng bốn tham số
TCP/IP quen thuộc: IP nguồn, cổng nguồn, IP đích, cổng đích.
Ngược lại, kiểm soát truy cập người dùng thì cần được nhấn mạnh mạnh mẽ, vì nó ràng buộc danh tính
người dùng với tài nguyên, cho phép kiểm soát chi tiết mịn, hạch toán, tuân thủ và bảo vệ dữ liệu.
Bốn biện pháp chủ chốt: xác thực mạnh, SSO, quản lý đặc quyền, ghi nhật ký và giám sát.
Sách cũng nhắc ISO/IEC 27002 định nghĩa sáu mục tiêu kiểm soát truy cập.
Và một lưu ý cho IaaS: khách hàng phải giám sát cả ứng dụng lẫn các thực thể máy chủ ảo —
ví dụ chạy thương mại điện tử trên Amazon EC2.
Câu chốt: trong Đám mây, trọng tâm dịch chuyển từ "bạn đang ở đâu trong mạng" sang "bạn là ai".
""")

# ================================================================= SLIDE 29
s = new_slide()
divider(s, "PHẦN IV  ·  MỤC 11.6 – 11.7", "Máy chủ ảo và\nkiểm soát bảo mật",
        ["Sáu khuyến nghị bảo mật máy chủ ảo trên nền tảng IaaS",
         "Bốn loại biện pháp kiểm soát bảo mật đám mây",
         "Tóm tắt chương và các ý cần nhớ"])
notes(s, """
Phần cuối gồm hai mục: bảo mật máy chủ ảo — tức phần việc của khách hàng khi dùng IaaS —
và bốn loại biện pháp kiểm soát, là khung tổng kết cho toàn chương.
""")

# ================================================================= SLIDE 30
s = new_slide()
head(s, "11.6", "Bảo mật máy chủ ảo (Securing Virtual Servers)")
card(s, ML, 1.48, CW, 0.95, "",
     ["Sự đơn giản của việc **tự cấp phát (self-provisioning)** máy chủ ảo mới trên nền tảng IaaS tạo ra rủi ro rằng **những máy chủ ảo không an toàn sẽ được tạo ra**. → **Cấu hình an toàn theo mặc định (secure-by-default)** cần **bằng hoặc vượt qua các đường cơ sở (baseline) sẵn có của ngành**."],
     fill=REDBG, border=REDBD, hl=RED, body_size=12.5, pad=0.18, name="vs intro")
recs = [
    ("Dùng cấu hình an toàn theo mặc định",
     "Xây dựng **ảnh VM tùy chỉnh** chỉ có **những khả năng và dịch vụ cần thiết** để hỗ trợ ngăn xếp ứng dụng → **giới hạn bề mặt tấn công** và **giảm đáng kể số lượng bản vá** cần thiết."),
    ("Theo dõi kiểm kê ảnh VM và phiên bản OS",
     "Ảnh của nhà cung cấp phải trải qua **cùng quy trình xác minh và gia cố** như máy chủ nội bộ. **Phương án tốt nhất: cung cấp ảnh của chính bạn** tuân thủ cùng tiêu chuẩn. Bảo vệ **tính toàn vẹn** của ảnh đã gia cố."),
    ("Bảo vệ các khóa riêng",
     "**Cô lập khóa giải mã khỏi Đám mây** nơi dữ liệu được lưu trữ, **trừ khi chúng cần thiết cho việc xử lý liên tục**. Nếu khóa nằm cùng chỗ với ứng dụng thì **không thể bảo vệ được**."),
    ("Không để chứng thư xác thực trong ảnh ảo hóa",
     "**Ngoại trừ một khóa để giải mã khóa hệ thống tệp.** **Không cho phép truy cập shell dựa trên mật khẩu**; với đặc quyền quản trị (**sudo**) hoặc truy cập dựa trên vai trò (Solaris, SELinux) thì **mật khẩu là bắt buộc**."),
    ("Chạy tường lửa máy chủ",
     "**Chỉ mở tối thiểu các cổng** cần thiết để hỗ trợ dịch vụ trên một thực thể. **Tắt tất cả dịch vụ không sử dụng**: FTP, dịch vụ in, dịch vụ tệp mạng, dịch vụ cơ sở dữ liệu nếu không cần."),
    ("Bật kiểm toán hệ thống và ghi nhật ký",
     "Ghi các **sự kiện bảo mật** vào một **máy chủ nhật ký chuyên dụng**. Máy chủ nhật ký phải có **mức bảo vệ bảo mật cao hơn** và **được cô lập**, bao gồm cả kiểm soát truy cập."),
]
cw3 = (CW - 2 * 0.30) / 3
for i, (t, d) in enumerate(recs):
    col_, row = i % 3, i // 3
    x = ML + col_ * (cw3 + 0.30)
    y = 2.62 + row * 2.00
    rect(s, x, y, cw3, 1.85, fill=SKY2, line=BORDER, adj=0.06)
    rect(s, x, y, 0.07, 1.85, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)
    tfn = txbox(s, x + 0.22, y + 0.16, 0.32, 0.3)
    rich(tfn.paragraphs[0], f"{i+1}.", 13, BLUE, bold=True, line_spacing=1.0)
    tf = txbox(s, x + 0.58, y + 0.14, cw3 - 0.80, 0.62)
    rich(tf.paragraphs[0], t, 12.5, NAVY, bold=True, line_spacing=1.1)
    textblock(s, x + 0.22, y + 0.82, cw3 - 0.44, [d], size=10.5, color=TEXT, hl=BLUE)
footer(s, 30)
notes(s, """
Mục 11.6 là phần rất thực hành: khi thuê IaaS, khách hàng tự tạo máy chủ ảo, và chính sự dễ dàng đó
sinh ra rủi ro — máy chủ ảo không an toàn được tạo ra hàng loạt. Nguyên tắc nền là cấu hình an toàn
theo mặc định phải bằng hoặc vượt các đường cơ sở của ngành.
Sáu khuyến nghị các bạn nên nhớ theo cặp.
Hai cái đầu về ảnh máy ảo: dùng ảnh tùy chỉnh chỉ chứa dịch vụ cần thiết — vừa thu hẹp bề mặt tấn công
vừa giảm số bản vá; và theo dõi kiểm kê ảnh, trong đó ảnh của nhà cung cấp phải được gia cố như máy nội bộ,
tốt nhất là tự cung cấp ảnh của mình.
Hai cái giữa về khóa và chứng thư: cô lập khóa giải mã khỏi chính Đám mây đang chứa dữ liệu — vì để
chung một chỗ thì mã hóa mất ý nghĩa; và không nhúng chứng thư xác thực vào ảnh, ngoại trừ khóa để
giải mã khóa hệ thống tệp. Không cho truy cập shell bằng mật khẩu, nhưng với sudo hoặc truy cập
theo vai trò thì mật khẩu là bắt buộc.
Hai cái cuối về vận hành: chạy tường lửa trên từng máy chủ và chỉ mở cổng tối thiểu, tắt FTP,
dịch vụ in, dịch vụ tệp mạng, dịch vụ cơ sở dữ liệu nếu không dùng; và bật kiểm toán, đẩy nhật ký
sự kiện bảo mật sang một máy chủ nhật ký chuyên dụng được cô lập và bảo vệ ở mức cao hơn.
""")

# ================================================================= SLIDE 31
s = new_slide()
head(s, "11.7", "Các biện pháp kiểm soát bảo mật đám mây")
card(s, ML, 1.48, CW, 0.90, "",
     ["Kiến trúc bảo mật Đám mây **chỉ hiệu quả nếu các triển khai phòng thủ đúng đắn được đặt đúng chỗ**. Các biện pháp kiểm soát bảo mật được đặt ra để **bảo vệ bất kỳ điểm yếu nào trong hệ thống** và **giảm bớt tác động của một cuộc tấn công**."],
     fill=SKY, body_size=12.5, pad=0.18, name="ctrl intro")
# timeline
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(ML + 0.2), Inches(2.90),
                            Inches(SW - MR - 0.2), Inches(2.90))
ln.line.color.rgb = BORDER
ln.line.width = Pt(2)
tf = txbox(s, ML + 0.2, 2.58, 5.0, 0.28)
rich(tf.paragraphs[0], "TRƯỚC SỰ CỐ", 10.5, BLUE, bold=True, line_spacing=1.0)
tf = txbox(s, SW - MR - 5.2, 2.58, 5.0, 0.28)
rich(tf.paragraphs[0], "TRONG / SAU SỰ CỐ", 10.5, RED, bold=True, align=PP_ALIGN.RIGHT, line_spacing=1.0)
ctrls = [
    ("RĂN ĐE", "Deterrent controls", BLUE,
     "Nhằm **làm giảm các cuộc tấn công** vào hệ thống Đám mây. Giống như **biển cảnh báo trên hàng rào**, chúng **giảm mức độ đe dọa bằng cách thông báo cho kẻ tấn công tiềm năng** rằng sẽ có **hậu quả bất lợi** nếu chúng tiếp tục."),
    ("PHÒNG NGỪA", "Preventive controls", BLUE,
     "**Tăng cường hệ thống** chống lại các sự cố, bằng cách **giảm thiểu — nếu không muốn nói là loại bỏ hẳn — các lỗ hổng**. Ví dụ: **xác thực mạnh** khiến người dùng trái phép khó truy cập hơn và **khả năng nhận diện người dùng hợp lệ cao hơn**."),
    ("PHÁT HIỆN", "Detective controls", NAVY,
     "Nhằm **phát hiện và phản ứng phù hợp** với bất kỳ sự cố nào xảy ra. Khi có tấn công, biện pháp phát hiện **báo hiệu cho biện pháp phòng ngừa hoặc khắc phục**. **Giám sát hệ thống và mạng**, bao gồm cơ chế **phát hiện và ngăn chặn xâm nhập**."),
    ("KHẮC PHỤC", "Corrective controls", RED,
     "**Làm giảm hậu quả của một sự cố**, thường bằng cách **giới hạn thiệt hại**. Chúng có hiệu lực **trong hoặc sau một sự cố**. Ví dụ: **khôi phục các bản sao lưu hệ thống** nhằm tái dựng lại một hệ thống đã bị xâm phạm."),
]
cw4 = (CW - 3 * 0.28) / 4
for i, (t, en, col_, d) in enumerate(ctrls):
    x = ML + i * (cw4 + 0.28)
    dot = rect(s, x + cw4 / 2 - 0.11, 2.79, 0.22, 0.22, fill=col_, shape=MSO_SHAPE.OVAL)
    fill = REDBG if i == 3 else SKY2
    bd = REDBD if i == 3 else BORDER
    rect(s, x, 3.22, cw4, 3.25, fill=fill, line=bd, adj=0.05)
    rect(s, x, 3.22, cw4, 0.62, fill=col_, line=col_, adj=0.14)
    rect(s, x, 3.55, cw4, 0.29, fill=col_, line=col_, shape=MSO_SHAPE.RECTANGLE)
    tf = txbox(s, x + 0.16, 3.34, cw4 - 0.32, 0.3)
    rich(tf.paragraphs[0], f"{i+1}. {t}", 14, WHITE, bold=True, line_spacing=1.0)
    tf = txbox(s, x + 0.16, 3.95, cw4 - 0.32, 0.26)
    rich(tf.paragraphs[0], en, 10, col_, italic=True, line_spacing=1.0)
    textblock(s, x + 0.16, 4.28, cw4 - 0.32, [d], size=10.5, color=TEXT, hl=NAVY)
    if i < 3:
        arrow(s, x + cw4 + 0.02, 2.82, w=0.22, h=0.16, color=BLUEL)
footer(s, 31)
notes(s, """
Mục 11.7 là khung tổng kết. Sách nói: kiến trúc bảo mật Đám mây chỉ hiệu quả nếu các triển khai
phòng thủ đúng đắn được đặt đúng chỗ. Và có bốn loại biện pháp kiểm soát, mình sắp theo trục thời gian
của một sự cố cho dễ nhớ.
Răn đe — deterrent — nằm trước sự cố, mục đích làm giảm ý định tấn công. Sách ví như biển cảnh báo
trên hàng rào: nó không chặn được ai, nhưng báo cho kẻ tấn công biết sẽ có hậu quả bất lợi.
Phòng ngừa — preventive — cũng trước sự cố, nhưng tác động thật: giảm thiểu hoặc loại bỏ lỗ hổng.
Ví dụ điển hình là xác thực mạnh, vừa khiến người dùng trái phép khó vào, vừa tăng khả năng nhận diện
đúng người dùng hợp lệ.
Phát hiện — detective — hoạt động khi sự cố đang xảy ra: giám sát hệ thống và mạng, phát hiện và
ngăn chặn xâm nhập, rồi báo hiệu cho nhóm phòng ngừa hoặc khắc phục.
Khắc phục — corrective — hoạt động trong và sau sự cố, làm giảm hậu quả bằng cách giới hạn thiệt hại.
Ví dụ kinh điển là khôi phục bản sao lưu để dựng lại hệ thống đã bị xâm phạm.
Bốn loại này là câu trả lời gọn nhất cho câu hỏi "quản lý bảo mật trong Đám mây là gì".
""")

# ================================================================= SLIDE 32
s = new_slide()
head(s, "Tóm tắt", "Những ý cần nhớ")
takeaways = [
    ("Trách nhiệm chia sẻ", "Nhà cung cấp bảo đảm dịch vụ an toàn; khách hàng thực hiện các biện pháp hỗ trợ."),
    ("Bộ ba CIA", "Vẫn là khung của bài toán, nhưng phần lớn ngăn xếp nay nằm dưới kiểm soát bên thứ ba."),
    ("Dữ liệu đang truyền", "Rủi ro chính là **không dùng thuật toán mã hóa đã được kiểm chứng** — ở mọi mô hình dịch vụ."),
    ("ABE · FHE · SE", "Ba nhu cầu khác nhau: truy cập theo thuộc tính, tính toán trên bản mã, tìm kiếm an toàn."),
    ("Hạ tầng", "Đám mây riêng ≈ extranet an toàn; Đám mây công cộng thêm phơi bày, khó kiểm toán, rủi ro sẵn sàng."),
    ("Bốn biện pháp kiểm soát", "Răn đe → Phòng ngừa → Phát hiện → Khắc phục."),
]
cw3 = (CW - 2 * 0.30) / 3
for i, (t, d) in enumerate(takeaways):
    col_, row = i % 3, i // 3
    x = ML + col_ * (cw3 + 0.30)
    y = 1.52 + row * 1.55
    rect(s, x, y, cw3, 1.40, fill=SKY2, line=BORDER, adj=0.07)
    c = rect(s, x + 0.18, y + 0.18, 0.34, 0.34, fill=BLUE, shape=MSO_SHAPE.OVAL)
    tfc = c.text_frame; tfc.vertical_anchor = MSO_ANCHOR.MIDDLE
    rich(tfc.paragraphs[0], str(i + 1), 12, WHITE, bold=True, align=PP_ALIGN.CENTER, line_spacing=1.0)
    tf = txbox(s, x + 0.62, y + 0.20, cw3 - 0.82, 0.3)
    rich(tf.paragraphs[0], t, 13, NAVY, bold=True, line_spacing=1.0)
    textblock(s, x + 0.18, y + 0.62, cw3 - 0.36, [d], size=11, color=TEXT, hl=BLUE)
card(s, ML, 4.72, CW, 2.02,
     "Từ phần Tóm tắt của chương",
     ["Các tổ chức **chỉ dựa hoàn toàn vào bảo mật tích hợp sẵn của nhà cung cấp** Đám mây có khả năng **phơi bày tổ chức của mình trước những rủi ro không cần thiết**.",
      "Điều này đặc biệt đúng với các **chứng thư (credential)** và **bí mật (secret)** vốn sinh sôi nảy nở trong môi trường Đám mây và các quy trình tự động hóa — chúng được tạo ra hàng trăm nghìn máy và vi dịch vụ, nhưng **nhiều trong số chúng không bao giờ được bảo mật**.",
      "Nếu bị xâm phạm, chúng trao cho kẻ tấn công một **điểm xuất phát then chốt** để đạt **quyền truy cập theo chiều ngang (lateral access)** xuyên các mạng, dữ liệu và ứng dụng — và cuối cùng là **những tài sản quan trọng nhất của tổ chức**."],
     fill=AMBBG, border=AMBBD, head_color=AMB, hl=AMB, head_size=13.5, body_size=11.5,
     gap=6, name="summary")
footer(s, 32)
notes(s, """
Tóm lại sáu ý.
Một, bảo mật đám mây là trách nhiệm chia sẻ — không ai gánh hết.
Hai, bộ ba CIA vẫn là khung tư duy, nhưng phần lớn ngăn xếp giờ nằm dưới kiểm soát bên thứ ba.
Ba, với dữ liệu đang truyền, rủi ro chính là không dùng thuật toán mã hóa đã được kiểm chứng,
và điều này đúng cho cả IaaS, PaaS lẫn SaaS.
Bốn, ba kỹ thuật mã hóa ABE, FHE, SE trả lời ba nhu cầu khác nhau: ai được truy cập,
tính toán mà không giải mã, và tìm kiếm mà không lộ nội dung.
Năm, về hạ tầng: Đám mây riêng gần như tương đương extranet an toàn, còn Đám mây công cộng
cộng thêm ba rủi ro là phơi bày dữ liệu đang truyền, khó kiểm toán, và phụ thuộc tính sẵn sàng bên ngoài.
Sáu, quản lý bảo mật vận hành qua bốn loại kiểm soát: răn đe, phòng ngừa, phát hiện, khắc phục.
Khối vàng cuối là lời cảnh báo của chính tác giả, và mình nghĩ đây là câu đáng nhớ nhất:
tổ chức nào chỉ dựa hoàn toàn vào bảo mật tích hợp sẵn của nhà cung cấp là đang tự phơi mình
trước rủi ro không cần thiết. Đặc biệt là các chứng thư và bí mật sinh ra ồ ạt trong môi trường
tự động hóa mà nhiều cái không bao giờ được bảo mật. Chỉ cần một cái bị lộ, kẻ tấn công có điểm
xuất phát để di chuyển ngang qua mạng, dữ liệu, ứng dụng, và chạm tới tài sản quan trọng nhất.
""")

# ================================================================= SLIDE 33
s = new_slide()
rect(s, 0, 0, SW, SH, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
rect(s, SW - 4.0, -1.6, 5.4, 5.4, fill=NAVY2, shape=MSO_SHAPE.OVAL)
rect(s, -1.5, 4.6, 4.4, 4.4, fill=NAVY2, shape=MSO_SHAPE.OVAL)
tf = txbox(s, 0, 2.72, SW, 0.9)
rich(tf.paragraphs[0], "Cảm ơn thầy cô và các bạn đã lắng nghe!", 34, WHITE, bold=True,
     align=PP_ALIGN.CENTER, line_spacing=1.0)
ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(SW / 2 - 1.1), Inches(3.85),
                            Inches(SW / 2 + 1.1), Inches(3.85))
ln.line.color.rgb = BLUE
ln.line.width = Pt(3)
tf = txbox(s, 0, 4.08, SW, 0.5)
rich(tf.paragraphs[0], "Câu hỏi & Thảo luận", 20, BLUEL, align=PP_ALIGN.CENTER, line_spacing=1.0)
tf = txbox(s, 0, 5.25, SW, 0.8)
rich(tf.paragraphs[0], "Chương 11 · Bảo mật đám mây", 13, RGBColor.from_string("BDD3E6"),
     align=PP_ALIGN.CENTER, line_spacing=1.3)
p = tf.add_paragraph()
rich(p, "Manvi & Shyam, “Cloud Computing: Concepts and Technologies”, CRC Press, 2021, tr. 205–227",
     11, RGBColor.from_string("8FB2CE"), align=PP_ALIGN.CENTER, line_spacing=1.3, space_before=5)
notes(s, """
Phần trình bày của nhóm mình đến đây là hết. Xin cảm ơn thầy cô và các bạn đã lắng nghe.
Nhóm rất mong nhận được câu hỏi và góp ý.
Nếu cần gợi ý thảo luận, mình đề xuất vài hướng: một là so sánh cụ thể trách nhiệm bảo mật
giữa IaaS, PaaS và SaaS; hai là vì sao FHE tuy mạnh nhưng chưa phổ biến trong thực tế;
ba là trong tổ chức của các bạn, bốn loại biện pháp kiểm soát đang được triển khai tới đâu.
""")

# ----------------------------------------------------------------- lưu file
OUT = "Chapter11_Vietnamese_Presentation.pptx"
prs.save(OUT)
print(f"Đã tạo {OUT} — {len(prs.slides.__iter__.__self__._sldIdLst)} slide")
if warnings:
    print("\n".join(warnings))
else:
    print("Không phát hiện tràn text theo ước lượng.")
