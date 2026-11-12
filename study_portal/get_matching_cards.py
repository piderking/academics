import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    portal_data = json.load(f)

deck = [d for d in portal_data["decks"] if d["id"] == "bot-1121-midterm-2"][0]
cards = deck["flashcards"]

matching = []
for c in cards:
    t = c['front'].lower()
    b = c['back'].lower()
    if any(k in t or k in b for k in [
        'calyx', 'carpel', 'stamen', 'pistil', 'floral whorl', 'flower', 'petal', 'sepal', 'ovary', 'anther', 'stigma', 'style',
        'wood', 'bark', 'cambium', 'periderm', 'cork', 'lenticel', 'heartwood', 'sapwood', 'annual ring', 'growth ring',
        'casparian', 'endodermis', 'pericycle', 'root cap', 'root hair', 'palisade', 'mesophyll', 'stoma', 'stomata', 'syconium', 'ostiole',
        'monocot', 'eudicot', 'radicle', 'mycorrhiz'
    ]):
        matching.append({'id': c['id'], 'front': c['front'], 'back': c['back']})

print(f"Total matching anatomical cards: {len(matching)}")
with open("G:/My Drive/Academics/study_portal/matching_anatomical_cards.json", "w", encoding="utf-8") as out:
    json.dump(matching, out, indent=2)

print("Saved matching_anatomical_cards.json")
