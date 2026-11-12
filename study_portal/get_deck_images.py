import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

deck = data["decks"][0]
for i, c in enumerate(deck["flashcards"]):
    print(f"Card {i+1:02d}: {c.get('image')}")
