import json

data = json.load(open('study_portal/midterm2_lecture_extracted.json', encoding='utf-8'))

for lec_name, lec_info in data.items():
    if 'Outline' in lec_name or 'New Yorker' in lec_name:
        continue
    print(f"\n=======================================================")
    print(f"LECTURE: {lec_name}")
    print(f"=======================================================")
    for s in lec_info['slides']:
        t = s['text'].strip()
        lines = [line.strip() for line in t.split('\n') if len(line.strip()) > 3]
        if lines:
            # show title and first few bullet points
            header = lines[0]
            bullets = " | ".join(lines[1:4])
            print(f"  Slide {s['slide']}: {header} ---> {bullets[:80]}")
