#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tách presentation.md thành 18 slide: (số, tiêu đề, markdown nội dung, speaker notes)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "presentation.md"

# "# 📌 SLIDE 3: TIÊU ĐỀ"  /  "### 📌 **SLIDE 1: TIÊU ĐỀ**"
RE_SLIDE = re.compile(r"^#{1,4}\s+.*?SLIDE\s+(\d+)\s*:\s*(.+?)\s*$", re.IGNORECASE)
RE_NOTES = re.compile(r"speaker\s*notes", re.IGNORECASE)
RE_BODY = re.compile(r"NỘI DUNG HIỂN THỊ", re.IGNORECASE)


def clean_heading(text):
    text = text.strip().strip("*").strip()
    text = re.sub(r"^[📌🎙️🖥️🔑🎯💡❓⚠️🔐🌐🔎🔄🛡️📬🏢👤🔗]+\s*", "", text).strip()
    return text.strip("*").strip()


def strip_quote(lines):
    """Bỏ tiền tố '> ' của speaker notes, gộp thành các đoạn văn."""
    out = []
    for ln in lines:
        s = ln.rstrip()
        s = re.sub(r"^\s*>\s?", "", s)
        out.append(s)
    text = "\n".join(out)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)      # bỏ ** trong notes
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse(path=SRC):
    lines = path.read_text(encoding="utf-8").splitlines()

    # 1. xác định điểm bắt đầu mỗi slide
    starts = []
    for i, ln in enumerate(lines):
        m = RE_SLIDE.match(ln)
        if m and not RE_NOTES.search(ln):
            starts.append((i, int(m.group(1)), clean_heading(m.group(2))))
    starts.append((len(lines), None, None))

    slides = []
    for k in range(len(starts) - 1):
        i, num, title = starts[k]
        j = starts[k + 1][0]
        block = lines[i + 1:j]

        # 2. cắt phần notes
        n_at = None
        for t, ln in enumerate(block):
            if RE_NOTES.search(ln):
                n_at = t
                break
        body_lines = block[:n_at] if n_at is not None else block
        note_lines = block[n_at + 1:] if n_at is not None else []

        # 3. bỏ dòng tiêu đề "NỘI DUNG HIỂN THỊ TRÊN SLIDE"
        body_lines = [l for l in body_lines if not RE_BODY.search(l)]
        while body_lines and not body_lines[0].strip():
            body_lines.pop(0)
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()

        slides.append({
            "num": num,
            "title": title,
            "body": "\n".join(body_lines),
            "notes": strip_quote(note_lines),
        })
    return slides


if __name__ == "__main__":
    for s in parse():
        body = s["body"]
        n_tbl = body.count("\n|")
        print(f"Slide {s['num']:>2} | {len(body):>5} ký tự nội dung | "
              f"{len(s['notes']):>5} ký tự notes | bảng:{'có' if n_tbl else '  '} | {s['title'][:52]}")
