import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("G:/My Drive/Academics/study_portal/midterm2_lecture_extracted.json", "r", encoding="utf-8") as f:
    lectures = json.load(f)

for pdf_name, content in lectures.items():
    if "Lecture" not in pdf_name:
        continue
    slides = content.get("slides", [])
    print(f"\n==========================================")
    print(f"{pdf_name} ({len(slides)} slides)")
    print(f"==========================================")
    for s in slides:
        text = s.get("text", "").strip()
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        slide_num = s.get("slide")
        if lines:
            header = " | ".join(lines[:2])
            print(f"  Slide {slide_num}: {header[:80]}")
