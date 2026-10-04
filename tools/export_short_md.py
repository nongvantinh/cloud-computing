#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh presentation-short.md từ speaker notes của bản 12 slide.

Giữ cho file markdown và notes trong file pptx luôn khớp nhau.
Chạy:  .venv/bin/python tools/export_short_md.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from short_notes import NOTES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "presentation-short.md"
WPM = 130                       # nhịp nói tham chiếu

TITLES = {
    1: "TIÊU ĐỀ",
    2: "MỤC LỤC",
    3: "NỀN TẢNG: TRÁCH NHIỆM & MỤC TIÊU BẢO MẬT",
    4: "BẢO VỆ DỮ LIỆU TRÊN CLOUD",
    5: "BA BÀI TOÁN — BA KỸ THUẬT",
    6: "ABE — MÃ HÓA DỰA TRÊN THUỘC TÍNH",
    7: "FHE — TÍNH TOÁN TRÊN DỮ LIỆU MÃ HÓA",
    8: "SE — TÌM KIẾM TRÊN DỮ LIỆU MÃ HÓA",
    9: "BẢO VỆ HẠ TẦNG & VÙNG TIN CẬY",
    10: "IaaS / PaaS / SaaS & QUẢN LÝ TRUY CẬP",
    11: "MÁY CHỦ ẢO & CÁC LỚP KIỂM SOÁT",
    12: "TỔNG KẾT",
}

ON_SLIDE = {
    1: "Chương 11 · BẢO MẬT ĐÁM MÂY · Cloud Security — Trách nhiệm · Dữ liệu · "
       "Mật mã · Hạ tầng · Ứng dụng · Kiểm soát.",
    2: "6 phần trong 2 hàng thẻ, mỗi phần 2 dòng ý.",
    3: "Shared Responsibility (CSP / Khách hàng / Dịch chuyển IaaS→PaaS→SaaS) "
       "+ bộ ba CIA.",
    4: "Vòng đời dữ liệu (Người dùng → Đường truyền → Lưu trữ → Xử lý → Trả kết quả) "
       "+ 3 trạng thái + 4 vấn đề cần kiểm soát.",
    5: "Luồng “Mã hóa → Tải lên → Giải mã để xử lý → Cloud thấy dữ liệu gốc” "
       "+ bảng ánh xạ câu hỏi ↔ kỹ thuật.",
    6: "3 bước (Thuộc tính người dùng → Chính sách trên dữ liệu → Khớp thì giải mã) "
       "+ CP-ABE / KP-ABE.",
    7: "Luồng Mã hóa → Gửi lên Cloud → Tính trên bản mã → Kết quả mã hóa → Giải mã "
       "+ Điểm đặc biệt / Đánh đổi.",
    8: "Hai luồng song song — Khi tải lên (từ khóa → chỉ mục mã hóa) và "
       "Khi tìm kiếm (trapdoor → đối chiếu → trả tài liệu).",
    9: "4 lớp (Dữ liệu → Mạng → Danh tính → Máy chủ/VM) + Private vs Public Cloud "
       "+ nguy cơ điển hình.",
    10: "Bảng 3 mô hình (CSP quản lý / Khách hàng lo / Rủi ro tiêu biểu) + 4 thẻ IAM.",
    11: "5 việc tối thiểu cho máy ảo + 4 nhóm kiểm soát.",
    12: "Chuỗi Trách nhiệm → Dữ liệu → Mật mã → Mạng & Trust zone → IAM & Ứng dụng "
        "→ Giám sát & Khôi phục + 3 thông điệp.",
}

DROPPED = [
    ("KP-ABE phi tập trung, 5 thành phần lược đồ, Security Game / Selective-ID",
     "`presentation.md` — Slide 7"),
    ("FHE: kiến trúc 3 thành phần, chi tiết noise & bootstrapping",
     "`presentation.md` — Slide 8"),
    ("FHE: ví dụ 5+10, ứng dụng phân tích dữ liệu y tế",
     "`presentation.md` — Slide 9"),
    ("SE: hai hướng triển khai, ví dụ email “Urgent”",
     "`presentation.md` — Slide 10"),
    ("Bảo mật ứng dụng PaaS chi tiết (WPS)", "`presentation.md` — Slide 13"),
    ("SaaS & fine-grained access control chi tiết", "`presentation.md` — Slide 15"),
    ("Vòng đời secrets đầy đủ", "`presentation.md` — Slide 18"),
]


def mmss(words):
    sec = round(words / WPM * 60)
    return f"{sec // 60}:{sec % 60:02d}"


def main():
    counts = {n: len(NOTES[n].split()) for n in NOTES}
    total = sum(counts.values())
    L = []
    L.append("# BẢO MẬT ĐÁM MÂY — BẢN RÚT GỌN 12 SLIDE (20–30 phút)\n")
    L.append("> Kịch bản nói giữ mạch dẫn dắt như `presentation.md` nhưng đã lược "
             "phần đi sâu và ví dụ dài.\n"
             "> Bản đầy đủ 18 slide vẫn ở `presentation.md` + "
             "`Chapter11_Vietnamese_Presentation.pptx`.\n"
             "> File trình chiếu: `Chapter11_Vietnamese_Presentation_Short.pptx` "
             "(build: `tools/build_short.py`, notes: `tools/short_notes.py`).\n"
             "> File này được sinh tự động: `tools/export_short_md.py`.\n")
    L.append("| # | Slide | Số từ | Thời lượng |")
    L.append("|---|-------|-------|-----------|")
    for n in sorted(NOTES):
        L.append(f"| {n} | {TITLES[n]} | {counts[n]} | ~{mmss(counts[n])} |")
    L.append(f"\n**Tổng: {total} từ ≈ {total / WPM:.0f} phút nói** (nhịp {WPM} từ/phút) "
             "— cộng thời gian chuyển slide khoảng 25–27 phút.\n")
    for n in sorted(NOTES):
        L.append("---\n")
        L.append(f"## SLIDE {n} — {TITLES[n]}\n")
        L.append(f"**Trên slide:** {ON_SLIDE[n]}\n")
        L.append(f"**Nói** (~{mmss(counts[n])}):\n")
        L.append(NOTES[n] + "\n")
    L.append("---\n")
    L.append("## NỘI DUNG ĐÃ LƯỢC BỎ (giữ lại để phòng khi bị hỏi)\n")
    L.append("| Nội dung | Ở đâu trong bản đầy đủ |")
    L.append("|---|---|")
    for what, where in DROPPED:
        L.append(f"| {what} | {where} |")
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Đã ghi: {OUT.relative_to(ROOT)} — {total} từ ≈ {total / WPM:.1f} phút")


if __name__ == "__main__":
    main()
