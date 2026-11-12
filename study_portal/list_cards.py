import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

deck = data["decks"][0]
print(f"Total cards: {len(deck['flashcards'])}")
print(f"Total quizzes: {len(deck['quizzes'])}")

for i, c in enumerate(deck["flashcards"]):
    img = c.get("image", "none")
    cit = c.get("citation", "none")
    print(f"{i+1:02d} [{cit}] {c['front'][:70]}... -> {img}")
