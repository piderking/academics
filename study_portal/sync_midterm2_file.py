import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    portal_data = json.load(f)

deck = [d for d in portal_data["decks"] if d["id"] == "bot-1121-midterm-2"][0]

with open("G:/My Drive/Academics/study_portal/midterm2_deck.json", "w", encoding="utf-8") as f:
    json.dump(deck, f, indent=2)

print("Synchronized study_portal/midterm2_deck.json successfully!")
