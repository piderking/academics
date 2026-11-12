import json

with open("G:/My Drive/Academics/study_portal/matching_anatomical_cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for c in cards:
    clean_front = c['front'].replace('\n', ' ')
    clean_back = c['back'].replace('\n', ' ').encode('ascii', 'replace').decode('ascii')
    print(f"[{c['id']}] {clean_front} ===> {clean_back[:70]}")
