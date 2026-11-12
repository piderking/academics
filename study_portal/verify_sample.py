import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    d = json.load(f)["decks"][0]

print(f"Deck: {d['title']}")
print(f"Total flashcards: {len(d['flashcards'])}")
print(f"Total quizzes: {len(d['quizzes'])}\n")

sample_indices = [0, 1, 2, 3, 5, 10, 15, 20, 25, 30, 35, 40]
for idx in sample_indices:
    c = d["flashcards"][idx]
    print(f"Card {idx+1:02d}: {c['front']}")
    print(f"   Back preview: {c['back'].splitlines()[0]}")
    print(f"   Image: {c.get('image')}\n")
