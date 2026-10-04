#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bộ slide 16 trang cho bài báo PFTSA (chịu lỗi chủ động cho Cloud).

Nội dung bám theo kịch bản 15–20 phút (16 slide) do người dùng cung cấp. Script dùng lại
bộ helper vẽ của tools/build_presentation.py để giữ phong cách nhất quán với
các deck sẵn có trong repo.

Chạy:  uv run python tools/build_ft_slides.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_presentation as bp  # noqa: E402
from build_presentation import (  # noqa: E402
    BLUE, BLUEL, GREEN, MUTED, NAVY, NAVY2, PALE, SKY2, WHITE,
    RED, AMB, BORDER, TEXT, GREEN as GRN,
    ML, MR, CW, TOP, BOT, SW, SH,
    callout, card, cards_row, chips, flow_h, flow_v, grid, label, layers,
    new_slide, rect, rich, steps, txbox, head, check,
)
from pptx.dml.color import RGBColor  # noqa: E402
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE  # noqa: E402
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR  # noqa: E402
from pptx.util import Inches, Pt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "FaultTolerance_PFTSA_Presentation.pptx"
TOTAL = 16
SUBJECT = "Chịu lỗi chủ động cho Cloud · Takagi-Sugeno + Simulated Annealing"
PRESENTER = "Nông Văn Tình"

GRNBG = RGBColor.from_string("E9F5F0")
GRNBD = RGBColor.from_string("B3DCCB")
FIG = ROOT / "assets" / "ft"


def fig(slide, name, x, y, w, caption=None):
    """Chèn hình cắt từ bài báo (có viền mảnh), trả về mép dưới."""
    from PIL import Image
    iw, ih = Image.open(FIG / name).size
    h = w * ih / iw
    rect(slide, x - 0.04, y - 0.04, w + 0.08, h + 0.08, fill=WHITE,
         line=BORDER, lw=0.75, shape=MSO_SHAPE.RECTANGLE)
    slide.shapes.add_picture(str(FIG / name), Inches(x), Inches(y),
                             Inches(w), Inches(h))
    if caption:
        tf = txbox(slide, x, y + h + 0.06, w, 0.24)
        rich(tf.paragraphs[0], caption, 9, MUTED, line_spacing=1.0)
        return y + h + 0.32
    return y + h


# --------------------------------------------------------------- khung chung
def footer(slide, idx):
    tf = txbox(slide, ML, 7.13, 9.0, 0.24)
    rich(tf.paragraphs[0], f"{SUBJECT} · {PRESENTER}", 9, MUTED,
         line_spacing=1.0)
    tf = txbox(slide, SW - MR - 1.6, 7.13, 1.6, 0.24)
    rich(tf.paragraphs[0], f"{idx}/{TOTAL}", 9, MUTED, align=PP_ALIGN.RIGHT,
         line_spacing=1.0)


def fr(num, kicker, title, note=""):
    s = new_slide()
    head(s, kicker, title)
    footer(s, num)
    if note:
        s.notes_slide.notes_text_frame.text = note.strip()
    return s


HALF = (CW - 0.4) / 2        # bề rộng một nửa khi chia đôi
RX = ML + HALF + 0.4          # mốc x của cột phải


# ===================================================================== S1
def slide1():
    s = new_slide()
    rect(s, 0, 0, SW, SH, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
    rect(s, SW - 4.3, -1.7, 5.6, 5.6, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    rect(s, SW - 2.6, 4.6, 4.4, 4.4, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    rect(s, 0, 0, 0.16, SH, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)

    tf = txbox(s, 1.15, 1.30, 10.6, 0.4)
    rich(tf.paragraphs[0], "BÁO CÁO BÀI BÁO KHOA HỌC", 15, BLUEL, bold=True,
         line_spacing=1.0)

    tf = txbox(s, 1.15, 1.80, 11.0, 1.5)
    rich(tf.paragraphs[0],
         "A Proactive Fault Tolerance Approach for Cloud Computing",
         31, WHITE, bold=True, hl=WHITE, line_spacing=1.04)
    rich(tf.add_paragraph(),
         "based on Takagi-Sugeno Fuzzy System & Simulated Annealing",
         20, BLUEL, line_spacing=1.08, space_before=4)

    ln = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(1.15),
                                Inches(3.75), Inches(3.4), Inches(3.75))
    ln.line.color.rgb = BLUE
    ln.line.width = Pt(3)

    tf = txbox(s, 1.15, 3.92, 10.6, 0.7)
    rich(tf.paragraphs[0],
         "Cách tiếp cận chịu lỗi chủ động cho điện toán đám mây dựa trên "
         "hệ mờ Takagi-Sugeno và thuật toán Simulated Annealing",
         14, PALE, italic=True, line_spacing=1.2)

    tf = txbox(s, 1.15, 4.86, 10.8, 0.5)
    rich(tf.paragraphs[0], "Nhóm tác giả", 11, BLUEL, bold=True,
         line_spacing=1.0)
    rich(tf.add_paragraph(),
         "Khiet Bui Thanh · Linh Phung Dieu · Sam Dang Thi Hong · "
         "Tran Vu Pham · Hung Tran Cong",
         12.5, WHITE, line_spacing=1.1, space_before=2)

    tf = txbox(s, 1.15, 5.95, 10.8, 0.5)
    rich(tf.paragraphs[0], "Người trình bày:  ", 12.5, PALE,
         line_spacing=1.1)
    rich(tf.paragraphs[0], PRESENTER, 12.5, WHITE, bold=True, hl=WHITE)

    rect(s, 1.15, 6.55, 3.1, 0.42, fill=NAVY2, line=BLUE, lw=1.0, adj=0.3)
    tf = s.shapes[-1].text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_top = tf.margin_bottom = 0
    rich(tf.paragraphs[0], "IJLTET · Vol.13 (3), 2019", 11, PALE,
         align=PP_ALIGN.CENTER, line_spacing=1.0)

    s.notes_slide.notes_text_frame.text = (
        "Xin chào thầy/cô và các bạn. Hôm nay em xin trình bày bài báo về một "
        "phương pháp chủ động xử lý lỗi trong môi trường Cloud Computing.\n\n"
        "Điểm chính của bài báo là kết hợp ba ý tưởng: hệ thống mờ "
        "Takagi-Sugeno để dự đoán lỗi của Physical Machine, Game Theory để mô "
        "hình hóa bài toán migration của các Virtual Machine, và Simulated "
        "Annealing để tìm chiến lược migration phù hợp.\n\n(~30–40 giây)"
    )


# ===================================================================== S2
def slide2():
    note = (
        "Cloud gồm nhiều máy vật lý PM, mỗi PM chạy nhiều máy ảo VM. Ứng dụng "
        "trên đó cần tính sẵn sàng, độ tin cậy và QoS. Khi một PM lỗi, mọi VM "
        "và ứng dụng trên nó đều bị ảnh hưởng.\n\n"
        "Chịu lỗi thụ động đi theo chuỗi: lỗi xảy ra, phát hiện, phục hồi, rồi "
        "hệ thống chạy tiếp. Dịch vụ có thể đã gián đoạn trước khi phục hồi "
        "xong. Chịu lỗi chủ động giám sát liên tục, dự đoán lỗi, di chuyển VM "
        "sang nơi an toàn và tránh để sự cố xảy ra. Bài báo làm việc này trong "
        "môi trường IaaS. (~1 phút 30 giây)"
    )
    s = fr(2, "BỐI CẢNH", "Vì sao cần chịu lỗi chủ động trong Cloud?", note)
    y = callout(s, ML, TOP, CW,
                "Cloud gồm nhiều **PM**, mỗi PM chạy nhiều **VM**. Ứng dụng cần "
                "**availability**, **reliability** và **QoS**. Khi một PM lỗi, "
                "VM và ứng dụng trên nó bị ảnh hưởng.", tone="red")
    label(s, ML, y + 0.26, HALF, "Passive: phản ứng sau lỗi")
    flow_v(s, ML, y + 0.7, HALF,
           ["Fault occurs", "Fault detection", "Recovery",
            "Dịch vụ có thể đã gián đoạn"],
           bh=0.46, gap=0.14, last=(bp.REDBG, bp.REDBD, RED))
    label(s, RX, y + 0.26, HALF, "Proactive: phòng ngừa trước lỗi")
    y2 = flow_v(s, RX, y + 0.7, HALF,
                ["Monitor", "Predict fault", "Preventive action: VM Migration",
                 "Tránh được lỗi tiềm ẩn"],
                bh=0.46, gap=0.14, last=(GRNBG, GRNBD, GREEN))
    y3 = callout(s, ML, y2 + 0.3, CW,
                 "Bài báo đi theo hướng chủ động: **dự đoán lỗi, rồi di chuyển "
                 "VM** để dịch vụ không bị gián đoạn. Bối cảnh là **IaaS**.",
                 tone="green")
    check("S2", y3)


# ===================================================================== S3
def slide3():
    note = (
        "Đây là kiến trúc cốt lõi của bài báo. Hệ thống giám sát PM và VM, đưa "
        "dữ liệu vào khối dự đoán lỗi bằng hệ mờ Takagi-Sugeno. Nếu một PM "
        "được dự đoán sắp lỗi, bài toán chuyển sang mô hình di chuyển VM: mô "
        "hình hóa bằng Game Theory với cân bằng Nash, rồi dùng Simulated "
        "Annealing để tìm lời giải. Toàn bộ gộp lại thành thuật toán PFTSA, "
        "sinh ra chiến lược di chuyển để ngăn lỗi.\n\n"
        "Gọn lại, có hai thành phần: dự đoán lỗi và phòng ngừa lỗi. (~1 phút)"
    )
    s = fr(3, "Ý TƯỞNG TỔNG THỂ", "Kiến trúc đề xuất của bài báo", note)
    flow_v(s, ML, TOP, HALF,
           ["Giám sát PM / VM", "Dự đoán lỗi: Takagi-Sugeno Fuzzy",
            "Mô hình di chuyển VM (Game Theory)", "Cân bằng Nash",
            "Simulated Annealing", "PFTSA → Chiến lược di chuyển",
            "Ngăn lỗi (Prevent failure)"],
           bh=0.5, gap=0.14,
           last=(GRNBG, GRNBD, GREEN))
    label(s, RX, TOP, HALF, "Hai thành phần chính")
    cards_row(s, RX, TOP + 0.44, HALF, 1.4, [
        ("1 · Fault Prediction",
         ["**Takagi-Sugeno Fuzzy System**",
          "Dự đoán PM nào sắp lỗi"], BLUE),
    ], bullet=True)
    cards_row(s, RX, TOP + 2.1, HALF, 1.8, [
        ("2 · Fault Prevention",
         ["**VM migration** (di chuyển VM)",
          "**Game Theory** + cân bằng Nash",
          "**Simulated Annealing**"], GREEN),
    ], bullet=True)
    y = callout(s, RX, TOP + 4.1, HALF,
                "PFTSA = Fault Prediction + Game Theory + Simulated Annealing.",
                tone="navy")
    check("S3", y)


# ===================================================================== S4
def slide4():
    note = (
        "Bài báo tổ chức vòng quản lý theo mô hình MAPE-K, như Hình 1 của bài "
        "báo. Monitor thu thập CPU, bộ nhớ, nhiệt độ. Analyze chạy dự đoán "
        "lỗi. Plan lập kế hoạch di chuyển VM. Execute thực hiện việc di "
        "chuyển.\n\n"
        "Các thành phần hỗ trợ gồm Broker phân phối yêu cầu, Local Agent trên "
        "mỗi VM, các PM và VM, thông tin giám sát và cơ sở tri thức. Cloud "
        "được mô tả như các cụm VM đặt trên các PM không đồng nhất. (~1 phút)"
    )
    s = fr(4, "KIẾN TRÚC HỆ THỐNG", "Vòng lặp quản lý MAPE-K", note)
    label(s, ML, TOP, HALF, "Kiến trúc hệ thống (Figure 1 của bài báo)")
    yb = fig(s, "f1.png", ML + 0.05, TOP + 0.46, HALF - 0.1)
    callout(s, ML, yb + 0.22, HALF,
            "Cloud là các cụm **VM** chạy trên các **PM không đồng nhất**.",
            tone="blue")
    label(s, RX, TOP, HALF, "Vòng lặp MAPE-K")
    y = flow_v(s, RX, TOP + 0.46, HALF,
               ["MONITOR: CPU, Memory, Temperature",
                "ANALYZE: Fault Prediction",
                "PLAN: VM Migration",
                "EXECUTE: Migration"],
               bh=0.52, gap=0.16)
    label(s, RX, y + 0.2, HALF, "Thành phần hỗ trợ")
    y = chips(s, RX, y + 0.62, HALF,
              ["Broker", "Local Agents", "Physical Machines",
               "Virtual Machines", "Monitoring info", "Knowledge base"],
              per_row=3, h=0.4)
    check("S5", y)


# ===================================================================== S5
def slide5():
    note = (
        "Lỗi không có ranh giới rõ ràng, nên bài báo dùng logic mờ. Tải CPU và "
        "nhiệt độ của PM đều được chia thành ba mức Low, Medium, High, với các "
        "hàm thành viên như Hình 3 của bài báo.\n\n"
        "Hai đại lượng này đi vào hệ mờ Takagi-Sugeno theo quy trình: mờ hóa, "
        "áp luật mờ, suy luận xấp xỉ, giải mờ, rồi cho ra dự đoán lỗi. Hệ thống "
        "dùng cơ sở tri thức của chuyên gia để đặt các luật. (~1 phút)"
    )
    s = fr(5, "DỰ ĐOÁN LỖI", "Dự đoán lỗi bằng hệ mờ Takagi-Sugeno", note)
    y = callout(s, ML, TOP, CW,
                "Lỗi không có ranh giới rõ ràng, nên trạng thái PM được mô tả "
                "bằng **logic mờ** theo tải CPU và nhiệt độ.", tone="amber")
    label(s, ML, y + 0.22, CW,
          "Hàm thành viên của tải và nhiệt độ PM (Figure 3 của bài báo)")
    y = fig(s, "f3.png", ML + 1.5, y + 0.64, CW - 3.0)
    label(s, ML, y + 0.28, CW, "Quy trình suy diễn mờ")
    y2 = flow_h(s, ML, y + 0.72, CW, 0.74,
                ["CPU Load + Temperature|đầu vào", "Fuzzification|mờ hóa",
                 "Fuzzy Rules|luật mờ", "Approximate Reasoning|suy luận",
                 "Defuzzification|giải mờ, ra dự đoán lỗi"],
                last=(GRNBG, GRNBD, GREEN))
    check("S6", y2)


# ===================================================================== S6
def slide6():
    note = (
        "Bài báo dùng hai đầu vào Load và Temperature, mỗi đầu vào ba mức, tạo "
        "thành chín luật mờ. Bảng này lấy trực tiếp từ phần thực nghiệm.\n\n"
        "Cách hiểu đơn giản: hệ thống đánh giá PM theo mức tải cộng nhiệt độ, "
        "rồi kết luận PM đó có được dự đoán là lỗi hay không. Bốn tổ hợp cho "
        "kết quả lỗi, năm tổ hợp còn lại là không lỗi. (~1 phút)"
    )
    s = fr(6, "LUẬT MỜ", "Chín luật dự đoán lỗi PM", note)
    rows = [
        ["1", "Low", "Low", "0"], ["2", "Low", "Medium", "0"],
        ["3", "Low", "High", "1 ⚠"], ["4", "Medium", "Low", "0"],
        ["5", "Medium", "Medium", "0"], ["6", "Medium", "High", "1 ⚠"],
        ["7", "High", "Low", "1 ⚠"], ["8", "High", "Medium", "0"],
        ["9", "High", "High", "1 ⚠"],
    ]
    grid(s, ML, TOP, 7.2,
         ["Luật", "Load", "Temperature", "Fault"], rows,
         ratios=[0.9, 1.4, 1.8, 1.2], size=10.6)
    cards_row(s, RX + 1.0, TOP, HALF - 1.0, 2.2, [
        ("Cách hiểu nhanh",
         ["PM được đánh giá theo **mức tải + nhiệt độ**.",
          "**Fault = 1**: PM được dự đoán **có lỗi**.",
          "**Fault = 0**: PM **bình thường**."], GREEN),
    ], bullet=True)
    y = callout(s, RX + 1.0, TOP + 2.5, HALF - 1.0,
                "Nguồn: Bảng 2 của bài báo.", tone="blue")
    check("S6", y)


# ===================================================================== S7
def slide7():
    note = (
        "Sau khi dự đoán một PM sắp lỗi, câu hỏi tiếp theo là VM nào cần di "
        "chuyển và di chuyển ra sao. Tắt PM đó chưa đủ để trả lời.\n\n"
        "Bài toán có nhiều ràng buộc: nhiều PM, nhiều VM thuộc các ứng dụng "
        "khác nhau, tài nguyên PM hữu hạn, việc di chuyển ảnh hưởng cân bằng "
        "tải và có thể gây lãng phí tài nguyên. Tác giả mô hình hóa nó "
        "bằng lý thuyết trò chơi. (~50 giây)"
    )
    s = fr(7, "SAU DỰ ĐOÁN", "Khi một PM được dự đoán sẽ lỗi?", note)
    y = callout(s, ML, TOP, CW,
                "Sau dự đoán, câu hỏi đặt ra là **VM nào cần di chuyển, và di "
                "chuyển như thế nào?** Tắt PM đó chưa đủ để trả lời.",
                tone="green")
    label(s, ML, y + 0.3, CW, "Bài toán có nhiều ràng buộc")
    y = bp.bullets(s, ML, y + 0.68, CW, [
        "Có nhiều **PM** và nhiều **VM**",
        "VM thuộc các **application** khác nhau",
        "Tài nguyên của PM **có giới hạn**",
        "Di chuyển ảnh hưởng đến **cân bằng tải (load balancing)**",
        "Di chuyển có thể gây **lãng phí tài nguyên (resource waste)**",
    ], size=12.5, gap=8) + (y + 0.68)
    y = callout(s, ML, y + 0.3, CW,
                "Tác giả mô hình hóa bài toán di chuyển VM bằng "
                "**Game Theory (lý thuyết trò chơi)**.", tone="navy")
    check("S7", y)


# ===================================================================== S8
def slide8():
    note = (
        "Trong mô hình trò chơi, mỗi ứng dụng đa tầng là một người chơi. Chiến "
        "lược là các cách phân bổ và di chuyển VM. Tài nguyên tranh chấp là "
        "CPU, RAM, Disk.\n\n"
        "Mục tiêu là tìm chiến lược di chuyển giúp hệ thống cân bằng tải, dùng "
        "tài nguyên hiệu quả, giảm lãng phí và tránh PM có nguy cơ lỗi. Chiến "
        "lược của tất cả người chơi hợp lại tạo thành trạng thái bài toán và "
        "quyết định payoff. (~1 phút)"
    )
    s = fr(8, "MÔ HÌNH TRÒ CHƠI", "Di chuyển VM như một trò chơi", note)
    cards_row(s, ML, TOP, CW, 1.3, [
        ("Players", ["Các **multi-tier application**"], BLUE),
        ("Strategies", ["Các chiến lược **phân bổ / di chuyển VM**"], BLUE),
        ("Resources", ["**CPU · RAM · Disk**"], BLUE),
    ], bullet=True)
    label(s, ML, TOP + 1.55, HALF, "Mục tiêu")
    bp.bullets(s, ML, TOP + 1.95, HALF, [
        "Cân bằng tải",
        "Sử dụng tài nguyên hiệu quả",
        "Giảm resource waste",
        "Tránh PM có nguy cơ fault",
    ], size=12, gap=7)
    label(s, RX, TOP + 1.55, HALF, "Từ chiến lược đến payoff")
    flow_v(s, RX, TOP + 1.95, HALF,
           ["App 1 / App 2 / App 3 → Strategy", "Combined Strategy",
            "Payoff"], bh=0.5, gap=0.2,
           last=(GRNBG, GRNBD, GREEN))
    check("S8", BOT)


# ===================================================================== S9
def slide9():
    note = (
        "Các ứng dụng không độc lập với nhau. Khi một ứng dụng đổi chiến lược "
        "di chuyển, nó ảnh hưởng tới tài nguyên còn trống, tới tải của PM và "
        "tới các ứng dụng khác.\n\n"
        "Cân bằng Nash là trạng thái mà không người chơi nào có thể tự đổi "
        "chiến lược để cải thiện payoff khi những người khác giữ nguyên. Bài "
        "báo lấy cân bằng Nash làm cơ sở cho mô hình, rồi dùng metaheuristic "
        "để tìm nghiệm gần tối ưu. (~1 phút)"
    )
    s = fr(9, "CÂN BẰNG NASH", "Vì sao cần Nash Equilibrium?", note)
    y = callout(s, ML, TOP, CW,
                "Các ứng dụng **không độc lập**: một ứng dụng đổi chiến lược "
                "sẽ ảnh hưởng tới tài nguyên còn trống, tải của PM và các ứng "
                "dụng khác.", tone="amber")
    cards_row(s, ML, y + 0.28, CW, 1.1, [
        ("Nash Equilibrium",
         ["Trạng thái mà **không người chơi nào** có thể tự đổi chiến lược để "
          "cải thiện payoff, khi các player khác **giữ nguyên** chiến lược."],
         GREEN),
    ])
    label(s, ML, y + 1.7, CW, "Ý tưởng")
    y2 = flow_h(s, ML, y + 2.08, CW, 0.7,
                ["Player strategies", "Payoff",
                 "Player có thể cải thiện?", "Nash Equilibrium|khi câu trả "
                 "lời là KHÔNG"],
                last=(GRNBG, GRNBD, GREEN))
    check("S9", y2)


# ===================================================================== S10
def slide10():
    note = (
        "Không gian các chiến lược di chuyển rất lớn, duyệt toàn bộ sẽ tốn "
        "nhiều thời gian. Simulated Annealing là phương pháp tìm kiếm "
        "heuristic dựa trên xác suất.\n\n"
        "Điểm quan trọng: SA không chỉ giữ lời giải tốt hơn ngay lập tức, mà "
        "đôi khi chấp nhận một lời giải kém hơn để thoát khỏi cực trị địa "
        "phương. Trong bài báo, không gian trạng thái là tập chiến lược của "
        "các người chơi, và lời giải lân cận được sinh ngẫu nhiên. (~1 phút)"
    )
    s = fr(10, "TỐI ƯU HÓA", "Simulated Annealing", note)
    y = callout(s, ML, TOP, CW,
                "Không gian chiến lược di chuyển **rất lớn**; duyệt toàn bộ "
                "(exhaustive search) tốn nhiều thời gian  →  dùng tìm kiếm "
                "heuristic.", tone="amber")
    flow_v(s, ML, y + 0.26, HALF,
           ["Initial Solution", "Generate Neighbor", "Evaluate Solution",
            "Accept / Reject", "Reduce Temperature → Repeat",
            "Final Solution"],
           bh=0.46, gap=0.14, last=(GRNBG, GRNBD, GREEN))
    cards_row(s, RX, y + 0.26, HALF, 1.6, [
        ("Điểm then chốt",
         ["SA có thể **chấp nhận một lời giải kém hơn** trong một số bước.",
          "Nhờ đó **thoát khỏi local optimum** (cực trị địa phương)."],
         GREEN),
    ], bullet=True)
    yy = callout(s, RX, y + 2.4, HALF,
                 "Trong bài báo: không gian trạng thái là tập **chiến lược của "
                 "các player**; lời giải lân cận được **sinh ngẫu nhiên**.",
                 tone="blue")
    check("S10", max(yy, BOT))


# ===================================================================== S11
def slide11():
    note = (
        "PFTSA là thuật toán gộp các thành phần lại. Từ dự đoán lỗi, xác định "
        "PM bị ảnh hưởng, khởi tạo chiến lược di chuyển, đánh giá hàm mục tiêu "
        "và payoff, sinh lời giải lân cận, chạy Simulated Annealing, cập nhật "
        "chiến lược, cuối cùng ra kế hoạch di chuyển VM.\n\n"
        "Bài báo trình bày hai thuật toán: Algorithm 1 PFTSA điều khiển quá "
        "trình tìm kiếm, Algorithm 2 CreateNeighborSolution sinh lời giải lân "
        "cận để SA tiếp tục khám phá. (~1 phút 20 giây)"
    )
    s = fr(11, "THUẬT TOÁN PFTSA",
           "Proactive Fault Tolerance based on Simulated Annealing", note)
    flow_v(s, ML, TOP, HALF,
           ["Fault Prediction", "Xác định PM bị ảnh hưởng",
            "Khởi tạo chiến lược di chuyển", "Đánh giá objective / payoff",
            "Create Neighbor Solution", "Simulated Annealing",
            "Kế hoạch di chuyển VM"],
           bh=0.48, gap=0.12, last=(GRNBG, GRNBD, GREEN))
    label(s, RX, TOP, HALF, "Hai thuật toán chính")
    cards_row(s, RX, TOP + 0.44, HALF, 1.3, [
        ("Algorithm 1: PFTSA",
         ["Điều khiển quá trình **tìm kiếm chiến lược di chuyển**."], BLUE),
    ], bullet=True)
    cards_row(s, RX, TOP + 2.0, HALF, 1.3, [
        ("Algorithm 2: CreateNeighborSolution",
         ["Sinh **lời giải lân cận** để SA tiếp tục **exploration**."], BLUE),
    ], bullet=True)
    y = callout(s, RX, TOP + 3.7, HALF,
                "PFTSA kết hợp:  **Fault Prediction + Game Theory + Simulated "
                "Annealing**.", tone="navy")
    check("S11", y)


# ===================================================================== S12
def slide12():
    note = (
        "Bài báo mô phỏng một trung tâm dữ liệu gồm 50 máy vật lý không đồng "
        "nhất, triển khai 30 ứng dụng ba tầng, chạy trong khoảng thời gian "
        "t = 1000. Cấu hình CPU, RAM, Disk được sinh ngẫu nhiên theo các giá "
        "trị lớn nhất và nhỏ nhất. Máy chạy thí nghiệm là 8GB RAM, Core i5.\n\n"
        "Hình 4 cho thấy tần suất lỗi của 50 PM: trường hợp 4 PM cùng lỗi tại "
        "một thời điểm phổ biến nhất, hơn 200 lần; 10 PM cùng lỗi ít nhất, "
        "khoảng 15 lần. (~1 phút)"
    )
    s = fr(12, "THỰC NGHIỆM", "Thiết lập thực nghiệm", note)
    w = 6.3
    cards_row(s, ML, TOP, w, 1.75, [
        ("Môi trường Cloud",
         ["**50** PM không đồng nhất", "**30** ứng dụng ba tầng",
          "Thời gian mô phỏng **t = 1000**"], BLUE),
        ("Cấu hình",
         ["CPU, RAM, Disk sinh ngẫu nhiên trong khoảng **max / min**",
          "Máy chạy: **8 GB RAM**, **Core i5**"], BLUE),
    ], bullet=True)
    label(s, ML, TOP + 2.05, w, "Mục tiêu đánh giá")
    chips(s, ML, TOP + 2.45, w,
          ["Fault prediction", "Parameter sensitivity", "Load balancing",
           "Wasted resources", "Execution time", "Objective function"],
          per_row=2, h=0.44)
    rx = ML + w + 0.45
    rw = SW - MR - rx
    label(s, rx, TOP, rw, "Tần suất lỗi của 50 PM tại t = 1000 (Figure 4)")
    y = fig(s, "f4.png", rx + 0.05, TOP + 0.46, rw - 0.1)
    y = callout(s, rx, y + 0.18, rw,
                "Có **4 PM** cùng lỗi tại một thời điểm là phổ biến nhất "
                "(hơn 200 lần); **10 PM** cùng lỗi ít nhất (khoảng 15 lần).",
                tone="blue")
    check("S12", max(y, BOT - 0.5))


# ===================================================================== S13
def slide13():
    note = (
        "Về khảo sát tham số: epsilon thay đổi từ 0.01 đến 0.09 với cooling "
        "rate bằng 0.5 để đo thời gian thực thi, và Hình 5 cho thấy epsilon ổn "
        "định tại 0.03. Cooling rate thay đổi từ 0.1 đến 0.9 để xem tác động "
        "lên cân bằng tải V (Hình 6) và lãng phí tài nguyên W (Hình 7). Trên "
        "các hình này, đường đen là đầu vào, đường màu là kết quả của PFTSA "
        "với cooling rate tương ứng. (~1 phút 20 giây)"
    )
    s = fr(13, "KẾT QUẢ", "Khảo sát tham số ε và cooling rate", note)
    lw = 4.5
    label(s, ML, TOP, lw, "Thời gian thực thi theo ε (Figure 5)")
    y = fig(s, "f5.png", ML + 0.05, TOP + 0.46, lw - 0.1)
    y = cards_row(s, ML, y + 0.2, lw, 1.5, [
        ("Hai tham số",
         ["**ε**: 0.01 → 0.09, ổn định tại **0.03**",
          "**cooling rate**: 0.1 → 0.9, xem tác động lên **V** và **W**"],
         GREEN),
    ], bullet=True)
    rx = ML + lw + 0.4
    rw = SW - MR - rx
    label(s, rx, TOP, rw, "Cân bằng tải V, cooling rate 0.1 và 0.9 (Figure 6)")
    y1 = fig(s, "f6.png", rx + 0.05, TOP + 0.46, rw - 0.5)
    label(s, rx, y1 + 0.12, rw,
          "Tài nguyên lãng phí W, cooling rate 0.1 và 0.9 (Figure 7)")
    y2 = fig(s, "f7.png", rx + 0.05, y1 + 0.58, rw - 0.5)
    check("S13", max(y, y2))


# ===================================================================== S14
def slide14():
    note = (
        "Đây là kết quả quan trọng nhất. Bài báo so sánh PFTSA với PSOVM, với "
        "epsilon bằng 0.03. Cân bằng tải (Hình 8) và lãng phí tài nguyên "
        "(Hình 9) của PFTSA gần bằng PSOVM. Thời gian thực thi của PFTSA nhỏ "
        "hơn (Hình 10). Giá trị hàm mục tiêu của chiến lược tốt nhất theo "
        "PSOVM lớn hơn của PFTSA (Hình 11).\n\n"
        "Tác giả giải thích: PFTSA ngẫu nhiên hóa cách xác định chiến lược di "
        "chuyển, nên tăng khả năng khám phá; PSOVM dựa vào vị trí, vận tốc của "
        "các phần tử và giá trị tối ưu của bầy đàn. (~1 phút 30 giây)"
    )
    s = fr(14, "SO SÁNH", "Benchmark: PFTSA và PSOVM", note)
    lw = 4.55
    y = grid(s, ML, TOP, lw,
             ["Tiêu chí", "Kết quả"], [
                 ["Cân bằng tải", "PFTSA gần bằng PSOVM"],
                 ["Tài nguyên lãng phí", "Tương tự nhau"],
                 ["Thời gian thực thi", "PFTSA thấp hơn"],
                 ["Hàm mục tiêu", "PSOVM lớn hơn PFTSA"],
             ], ratios=[1.2, 1.5], size=10.5)
    y = callout(s, ML, y + 0.3, lw,
                "**PFTSA** ngẫu nhiên hóa chiến lược di chuyển, nên tăng khả "
                "năng khám phá lời giải.", tone="green")
    callout(s, ML, y + 0.2, lw,
            "**PSOVM** dựa vào vị trí, vận tốc của các phần tử và giá trị tối "
            "ưu của bầy đàn.", tone="blue")
    gx = ML + lw + 0.35
    cw = (SW - MR - gx - 0.25) / 2
    caps = [("f8.png", "Figure 8. Cân bằng tải V"),
            ("f9.png", "Figure 9. Tài nguyên lãng phí W"),
            ("f10.png", "Figure 10. Thời gian thực thi (ms)"),
            ("f11.png", "Figure 11. Giá trị hàm mục tiêu F")]
    for i, (name, cap) in enumerate(caps):
        cx = gx + (i % 2) * (cw + 0.25)
        cy = TOP + (i // 2) * 2.85
        fig(s, name, cx + 0.04, cy + 0.04, cw - 0.08, cap)
    check("S14", BOT)


# ===================================================================== S15
def slide15():
    note = (
        "Bài báo làm được bốn việc. Một, dùng hệ mờ Takagi-Sugeno để dự đoán "
        "lỗi PM từ mức sử dụng tài nguyên và nhiệt độ. Hai, mô hình hóa việc "
        "di chuyển VM bằng Game Theory và cân bằng Nash. Ba, dùng Simulated "
        "Annealing để tìm chiến lược di chuyển gần tối ưu. Bốn, gộp lại thành "
        "PFTSA và so sánh với PSOVM.\n\n"
        "Kết quả: PFTSA cho cân bằng tải gần bằng PSOVM, tài nguyên lãng phí "
        "tương tự và thời gian thực thi thấp hơn, trong các thí nghiệm được "
        "báo cáo. Hướng tiếp theo là thử các thuật toán metaheuristic khác. "
        "(~1 phút 30 giây)"
    )
    s = fr(15, "ĐÓNG GÓP & KẾT LUẬN", "Bài báo đã làm được gì?", note)
    label(s, ML, TOP, HALF, "Bốn đóng góp")
    bp.bullets(s, ML, TOP + 0.46, HALF, [
        "**Dự đoán lỗi:** hệ mờ Takagi-Sugeno cho PM, từ tải và nhiệt độ",
        "**Mô hình di chuyển VM:** Game Theory và cân bằng Nash",
        "**Tối ưu:** Simulated Annealing tìm chiến lược gần tối ưu",
        "**PFTSA:** gộp ba thành phần trên, đánh giá tham số và so sánh "
        "với PSOVM",
    ], size=12, gap=10)
    label(s, RX, TOP, HALF, "Kết quả")
    bp.bullets(s, RX, TOP + 0.46, HALF, [
        "Dự đoán được lỗi **trước khi** xảy ra",
        "Cân bằng tải gần bằng PSOVM, tài nguyên lãng phí tương tự",
        "Thời gian thực thi **thấp hơn** PSOVM trong các thí nghiệm được "
        "báo cáo",
    ], size=12, gap=10)
    y = callout(s, RX, TOP + 2.2, HALF,
                "**Hướng phát triển:** thử các thuật toán **metaheuristic "
                "khác** cho bài toán này.", tone="green")
    y = callout(s, ML, TOP + 3.5, CW,
                "Chuỗi xử lý: **Takagi-Sugeno** dự đoán lỗi, **Game Theory và "
                "Nash** mô hình hóa việc di chuyển, **Simulated Annealing** "
                "tìm lời giải, **PFTSA** tạo kế hoạch di chuyển VM.",
                tone="navy")
    check("S15", y)


# ===================================================================== S16
def slide16():
    s = new_slide()
    rect(s, 0, 0, SW, SH, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
    rect(s, -1.8, SH - 4.0, 5.2, 5.2, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    rect(s, SW - 3.3, -1.6, 4.8, 4.8, fill=NAVY2, shape=MSO_SHAPE.OVAL)
    rect(s, 0, 0, 0.16, SH, fill=BLUE, shape=MSO_SHAPE.RECTANGLE)

    tf = txbox(s, 1.3, 2.25, 10.7, 1.0)
    rich(tf.paragraphs[0], "Cảm ơn thầy cô và các bạn", 36, WHITE, bold=True,
         hl=WHITE, line_spacing=1.02)
    tf = txbox(s, 1.3, 3.25, 10.7, 0.5)
    rich(tf.paragraphs[0], "Questions & Discussion", 19, BLUEL, italic=True,
         line_spacing=1.0)

    rect(s, 1.3, 4.25, 10.5, 1.15, fill=NAVY2, line=BLUE, lw=1.25, adj=0.08)
    tf = s.shapes[-1].text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.2)
    rich(tf.paragraphs[0], "Key takeaway", 12, BLUEL, bold=True,
         line_spacing=1.0)
    rich(tf.add_paragraph(),
         "Predict the fault before it happens, then optimize VM migration to "
         "prevent its impact.", 15, WHITE, hl=WHITE, line_spacing=1.12,
         space_before=4)

    footer(s, 16)
    s.notes_slide.notes_text_frame.text = (
        "Cảm ơn thầy cô và các bạn đã lắng nghe. Em xin nhận câu hỏi.\n\n"
        "Thông điệp đọng lại: dự đoán lỗi trước khi nó xảy ra, rồi tối ưu việc "
        "di chuyển VM để ngăn tác động của lỗi. (~20–30 giây)"
    )


# Ghi chú người nói cho từng slide (đã gộp theo cấu trúc 16 slide).
NOTES = [
    # 1
    """Xin chào thầy/cô và các bạn. Hôm nay em xin trình bày một bài báo có tiêu đề "A Proactive Fault Tolerance Approach for Cloud Computing Based on Takagi-Sugeno Fuzzy System and Simulated Annealing Algorithm."

Bài báo tập trung vào bài toán fault tolerance trong môi trường Cloud Computing, cụ thể là làm thế nào để phát hiện nguy cơ xảy ra lỗi trước khi lỗi thực sự xảy ra, rồi thực hiện các hành động phòng ngừa.

Phương pháp kết hợp ba ý tưởng. Thứ nhất là Takagi-Sugeno Fuzzy System để dự đoán lỗi của Physical Machine. Thứ hai là Game Theory, dùng Nash Equilibrium để mô hình hóa bài toán VM migration. Thứ ba là Simulated Annealing, dùng để tìm chiến lược migration phù hợp.

Tác giả gọi phương pháp này là PFTSA. (~40 giây)""",
    # 2
    """Trước hết là vấn đề mà bài báo muốn giải quyết.

Trong Cloud Computing, đặc biệt là mô hình IaaS, hệ thống gồm rất nhiều Physical Machine (PM), và trên mỗi PM chạy nhiều Virtual Machine (VM). Ứng dụng cloud cần độ sẵn sàng và độ tin cậy cao. Nhưng PM có thể lỗi, và khi đó các VM trên nó bị ảnh hưởng, kéo theo ứng dụng và chất lượng dịch vụ.

Với passive fault tolerance, quy trình là: fault xảy ra, hệ thống phát hiện, rồi recovery. Tức là hệ thống phản ứng với một vấn đề đã xảy ra, và lúc đó dịch vụ có thể đã bị ảnh hưởng.

Với proactive fault tolerance, hệ thống bắt đầu từ monitoring, dự đoán xem một PM có khả năng lỗi hay không, và nếu có nguy cơ thì thực hiện hành động phòng ngừa, ví dụ di chuyển các VM ra khỏi PM đó.

Ý tưởng chính: thay vì "fault rồi mới recovery", ta muốn "predict rồi prevent". Bài báo đặt vấn đề trong bối cảnh IaaS và dùng preemptive VM migration làm biện pháp phòng ngừa. (~2 phút)""",
    # 3
    """Đây là ý tưởng tổng thể của phương pháp, gồm hai phần.

Phần một là fault prediction. Hệ thống theo dõi thông tin của Physical Machine, rồi dùng Takagi-Sugeno Fuzzy System để dự đoán khả năng xảy ra fault.

Nếu một PM được dự đoán có nguy cơ, bài toán tiếp theo là quyết định VM nào cần migration và migration như thế nào. Đó là phần hai, fault prevention.

Tác giả mô hình hóa VM migration bằng Game Theory, trong đó các application là các player và mỗi player có những migration strategy khác nhau. Nash Equilibrium được dùng trong mô hình migration, và Simulated Annealing được dùng để tìm một chiến lược tốt.

Toàn bộ quá trình này tạo thành phương pháp PFTSA. (~1 phút)""",
    # 4
    """Để triển khai ý tưởng này, bài báo dùng kiến trúc MAPE-K loop, như Hình 1 của bài báo. MAPE-K gồm bốn bước Monitor, Analyze, Plan, Execute, cùng với Knowledge.

Monitor thu thập thông tin từ các PM và VM, chẳng hạn CPU và memory. Analyze phân tích thông tin đó để xác định trạng thái hệ thống và dự đoán fault. Nếu có PM nguy cơ lỗi, hệ thống chuyển sang Plan để lập kế hoạch migration cho các VM. Execute là bước thực hiện migration.

Đây là một vòng lặp liên tục: monitor, phân tích, lập kế hoạch, hành động. Các thành phần hỗ trợ gồm Broker, Local Agents, các PM và VM, thông tin giám sát và knowledge base. Vòng lặp này là cơ sở để hệ thống chịu lỗi theo hướng chủ động. (~1 phút)""",
    # 5
    """Bây giờ là thành phần đầu tiên của phương pháp, fault prediction. Tác giả dùng Takagi-Sugeno Fuzzy System.

Lý do là trạng thái của một Physical Machine không phải lúc nào cũng chỉ có hai trạng thái rõ ràng là bình thường hoặc lỗi. CPU load có thể thấp, trung bình hoặc cao. Temperature cũng vậy. Hình 3 cho thấy các hàm thành viên của tải và nhiệt độ.

Fuzzy system biểu diễn các trạng thái này bằng các mức Low, Medium, High, rồi dùng fuzzy rule để kết luận. Quy trình gồm fuzzification, dùng các rule trong knowledge base, approximate reasoning, và cuối cùng là defuzzification để đưa ra kết quả.

Hai đầu vào cho fault prediction trong bài báo là load và temperature. (~1 phút)""",
    # 6
    """Đây là các fuzzy rule của bài báo. Có hai input là Load và Temperature, mỗi input có ba mức Low, Medium, High, nên có tổng cộng chín trường hợp.

Ví dụ, Load Low và Temperature Low cho kết quả 0, tức là không dự đoán fault. Load Low mà Temperature High cho kết quả 1, tức là dự đoán có fault. Load Medium với Temperature High cũng là fault. Load High với Temperature Low bài báo cũng đánh dấu là fault. Và cả hai cùng High thì được dự đoán là fault.

Như vậy hệ thống kết hợp mức tải và nhiệt độ để đánh giá trạng thái PM. Kết quả của bước này là danh sách các PM có nguy cơ lỗi, để chuyển sang bước phòng ngừa. (~1 phút)""",
    # 7
    """Sau khi dự đoán một PM có khả năng lỗi, vẫn còn một vấn đề quan trọng: phải migration VM nào, và migration như thế nào.

Đây không phải bài toán đơn giản. Hệ thống có nhiều PM, nhiều VM và nhiều application, và mỗi PM có giới hạn về CPU, RAM, Disk. Nếu migration một cách đơn giản, ta có thể tránh được một PM lỗi nhưng làm một PM khác quá tải. Hoặc ngược lại, tạo ra nhiều tài nguyên bị lãng phí.

Vì vậy tác giả chuyển bài toán VM migration thành một bài toán tối ưu, và dùng Game Theory để mô hình hóa sự tương tác giữa các application. (~50 giây)""",
    # 8
    """Trong mô hình Game Theory của bài báo, các multi-tier application là các player. Mỗi player chọn một migration strategy cho các VM của mình. Các VM dùng tài nguyên CPU, RAM, Disk trên các Physical Machine.

Mục tiêu không chỉ là chuyển VM ra khỏi PM có nguy cơ lỗi, mà còn phải phân bổ tài nguyên hợp lý. Hai vấn đề được quan tâm là load balancing và resource waste. Nếu chuyển quá nhiều VM sang một PM, PM đó có thể quá tải. Nếu phân bổ không hợp lý, một lượng tài nguyên lớn có thể không được dùng hiệu quả.

Strategy của một application ảnh hưởng đến các application khác. Chính sự tương tác này khiến Game Theory phù hợp để mô hình hóa bài toán. (~1 phút)""",
    # 9
    """Sau khi có mô hình Game Theory, bài báo dùng khái niệm Nash Equilibrium.

Mỗi application chọn strategy dựa trên payoff của mình. Nhưng payoff đó không chỉ phụ thuộc vào chính nó, mà còn phụ thuộc vào strategy của các application khác. Một trạng thái là Nash Equilibrium khi không có player nào có thể tự đổi strategy để cải thiện payoff, trong khi các player khác giữ nguyên.

Vì vậy Nash Equilibrium cho ta cách mô tả một trạng thái mà các strategy tương đối ổn định với nhau. Tuy nhiên, không gian strategy của VM migration có thể rất lớn, nên bài báo tiếp tục dùng một phương pháp metaheuristic là Simulated Annealing để tìm solution. (~1 phút)""",
    # 10
    """Simulated Annealing, gọi tắt là SA, là một thuật toán tìm kiếm heuristic dựa trên xác suất.

Ý tưởng là bắt đầu từ một solution ban đầu, tạo ra một solution lân cận (neighbor solution), đánh giá nó và quyết định có chấp nhận hay không. Điểm đặc biệt là trong một số trường hợp SA chấp nhận một solution kém hơn solution hiện tại. Nhìn từng bước thì có vẻ không hợp lý, nhưng nhờ vậy thuật toán thoát được local optimum và tiếp tục khám phá những vùng khác của search space.

Trong quá trình chạy, temperature giảm dần. Khi temperature giảm, khả năng chấp nhận solution kém hơn cũng giảm theo. Vì vậy thuật toán ban đầu có khả năng exploration cao, sau đó dần tập trung vào những solution tốt. Trong bài báo, state space là tập các chiến lược của các player. (~1 phút)""",
    # 11
    """Từ các thành phần trên, tác giả xây dựng thuật toán PFTSA.

Đầu tiên, hệ thống dự đoán lỗi và xác định PM có nguy cơ. Sau đó một migration strategy ban đầu được tạo ra và được đánh giá bằng objective, hay payoff, của bài toán. Tiếp theo thuật toán tạo một neighbor solution, đánh giá nó, và Simulated Annealing quyết định có chấp nhận hay không. Quá trình này lặp lại trong suốt quá trình tìm kiếm.

Mục tiêu cuối là một migration strategy tốt để các VM rời khỏi PM có nguy cơ lỗi, trong khi vẫn dùng tài nguyên ở mức hợp lý.

Bài báo có hai algorithm. Algorithm 1 là PFTSA, điều khiển quá trình tối ưu migration. Algorithm 2 là CreateNeighborSolution, tạo solution lân cận cho quá trình tìm kiếm. PFTSA là nơi fault prediction, game theory và simulated annealing được kết hợp.

Chuỗi cần nhấn từ slide 8 đến 11: Game Theory trả lời migration strategy tương tác với nhau như thế nào. Nash Equilibrium trả lời trạng thái ổn định của các strategy là gì. Simulated Annealing trả lời cách tìm solution tốt trong search space lớn. PFTSA kết hợp cả ba. (~1 phút 20 giây)""",
    # 12
    """Sau phần phương pháp, ta xem tác giả đánh giá nó như thế nào.

Trong simulation, tác giả dùng 50 Physical Machine không đồng nhất và 30 ứng dụng ba tầng, với thời gian t bằng 1000. Các PM có cấu hình CPU, RAM, Disk khác nhau để mô phỏng môi trường cloud không đồng nhất. Thí nghiệm chạy trên một máy 8 GB RAM, Intel Core i5.

Hình 4 cho thấy tần suất lỗi của 50 PM: trường hợp 4 PM cùng lỗi tại một thời điểm phổ biến nhất, hơn 200 lần, còn 10 PM cùng lỗi ít nhất, khoảng 15 lần.

Phần evaluation gồm khảo sát tham số của thuật toán, đánh giá load balancing và wasted resources, rồi benchmark PFTSA với PSOVM theo execution time và objective function. (~1 phút)""",
    # 13
    """Đây là phần khảo sát tham số. Tác giả thay đổi hai tham số để xem chúng ảnh hưởng thế nào đến hành vi của thuật toán.

Tham số thứ nhất, epsilon, đi từ 0.01 đến 0.09 để đánh giá execution time. Hình 5 cho thấy giá trị 0.03 là ổn định. Tham số thứ hai, cooling rate, đi từ 0.1 đến 0.9 để đánh giá load balancing V (Hình 6) và wasted resources W (Hình 7). Trên các hình đó, đường đen là đầu vào, đường màu là kết quả của PFTSA.

Điểm cần chú ý không chỉ là một giá trị tham số cụ thể, mà là tác giả đã làm một sensitivity study để xem lựa chọn tham số ảnh hưởng thế nào đến thuật toán. Số liệu chi tiết nằm trong các figure của bài báo. (~1 phút 15 giây)""",
    # 14
    """Đây là phần quan trọng nhất của kết quả. Tác giả benchmark PFTSA với PSOVM.

Về load balancing (Hình 8), PFTSA gần tương đương PSOVM. Về wasted resources (Hình 9), hai phương pháp tương tự nhau. Về execution time (Hình 10), PFTSA thấp hơn PSOVM. Về objective function (Hình 11), tác giả báo cáo giá trị của các migration strategy tốt nhất theo PSOVM cao hơn PFTSA.

Tác giả giải thích một điểm mạnh của PFTSA là randomization trong migration strategies, giúp tăng khả năng exploration. Còn PSOVM dựa trên particle position, velocity và swarm optimum.

Theo kết quả của bài báo, PFTSA đạt chất lượng gần tương đương về load balancing và wasted resources, và có lợi thế về execution time trong thí nghiệm được thực hiện. (~1 phút 30 giây)""",
    # 15
    """Em tóm tắt bài báo thành bốn đóng góp. Một, dùng Takagi-Sugeno Fuzzy System để dự đoán fault của Physical Machine. Hai, xây dựng mô hình Game Theory cho bài toán VM migration, trong đó các multi-tier application là player. Ba, dùng Simulated Annealing để tìm migration strategy trong search space lớn. Bốn, kết hợp ba thành phần thành PFTSA, rồi đánh giá bằng parameter study và benchmark với PSOVM.

Có thể nhìn chúng như một pipeline: dự đoán lỗi, mô hình hóa migration, tối ưu migration, và ngăn tác động của lỗi.

Kết quả được báo cáo: load balancing gần tương đương, wasted resources tương tự, execution time thấp hơn trong các thí nghiệm của bài báo. Về future work, tác giả đề xuất nghiên cứu các thuật toán metaheuristic khác cho bài toán này.

Ý cốt lõi: không chờ cloud system lỗi rồi mới xử lý, mà dự đoán lỗi và chủ động di chuyển VM để giảm tác động của lỗi. (~2 phút)""",
    # 16
    """Trên đây là phần trình bày của em về phương pháp proactive fault tolerance dựa trên Takagi-Sugeno Fuzzy System và Simulated Annealing. Em xin cảm ơn thầy/cô và các bạn đã lắng nghe. Em sẵn sàng nhận câu hỏi ạ. (~20 giây)

Gợi ý khi trả lời: nếu bị hỏi, đoạn dễ bị hỏi nhất là mối quan hệ Game Theory, Nash Equilibrium, Simulated Annealing và PFTSA ở slide 8 đến 11.""",
]

BUILDERS = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8, slide9, slide10, slide11, slide12, slide13, slide14, slide15, slide16]


def main():
    for b in BUILDERS:
        b()
    assert len(NOTES) == len(bp.prs.slides)
    for sl, text in zip(bp.prs.slides, NOTES):
        sl.notes_slide.notes_text_frame.text = text.strip()
    bp.prs.save(str(OUT))
    print(f"Đã ghi: {OUT}  ({len(BUILDERS)} slide)")
    if bp.warnings:
        print("CẢNH BÁO bố cục:")
        for w in bp.warnings:
            print("  -", w)
    else:
        print("Không có cảnh báo tràn lề.")


if __name__ == "__main__":
    main()

