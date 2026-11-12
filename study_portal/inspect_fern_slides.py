import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("G:/My Drive/Academics/study_portal/midterm2_lecture_extracted.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lec10 = data["BOT 1121 F2026 Lecture 10 - Herbarium Studies, Ferns.pdf"]["slides"]
for s in lec10:
    if s["slide"] >= 28:
        print(f"=== SLIDE {s['slide']} ===")
        print(s["text"].strip())
