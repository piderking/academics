import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    portal_data = json.load(f)

deck = [d for d in portal_data["decks"] if d["id"] == "bot-1121-midterm-2"][0]
cards = deck["flashcards"]

print(f"Total cards: {len(cards)}")
for c in cards:
    t = c['front'].lower()
    b = c['back'].lower()
    # Check if matches key botanical anatomical structures
    if any(k in t or k in b for k in [
        'calyx', 'carpel', 'stamen', 'pistil', 'floral whorl', 'flower', 'petal', 'sepal', 'ovary', 'anther', 'stigma', 'style',
        'wood', 'bark', 'cambium', 'periderm', 'cork', 'lenticel', 'heartwood', 'sapwood', 'annual ring', 'growth ring',
        'casparian', 'endodermis', 'pericycle', 'root cap', 'root hair', 'palisade', 'mesophyll', 'stoma', 'stomata', 'syconium', 'ostiole'
    ]):
        print(f"[{c['id']}] {c['front']} -> {c['back'][:60]}...")
