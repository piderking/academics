import json

with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

deck = None
for d in data.get("decks", []):
    if d.get("id") == "bot-1121-midterm-2":
        deck = d
        break

print("Found deck:", deck.get("title"))
print("Total cards:", len(deck.get("flashcards", [])))
print("Total quizzes:", len(deck.get("quizzes", [])))

# Check which cards have images
with_img = [c for c in deck.get("flashcards", []) if c.get("image")]
print(f"Cards with images: {len(with_img)}")

# List some cards related to flowers, tree/wood, bark, root, leaves
flower_cards = [c for c in deck.get("flashcards", []) if any(k in (c['front'] + ' ' + c['back']).lower() for k in ['flower', 'carpel', 'stamen', 'pistil', 'petal', 'sepal', 'ovary', 'anther', 'stigma', 'style', 'inflorescence', 'syconium', 'monoecious', 'dioecious'])]
tree_cards = [c for c in deck.get("flashcards", []) if any(k in (c['front'] + ' ' + c['back']).lower() for k in ['wood', 'tree', 'bark', 'cambium', 'periderm', 'cork', 'xylem', 'phloem', 'lenticel', 'annual ring', 'growth ring', 'sapwood', 'heartwood', 'tracheid', 'vessel'])]

print(f"Flower-related cards: {len(flower_cards)}")
print("Sample flower cards:")
for c in flower_cards[:8]:
    print(f"  - [{c['id']}] {c['front']}: {c['back'][:80]}...")

print(f"\nTree/Wood/Bark-related cards: {len(tree_cards)}")
for c in tree_cards[:8]:
    print(f"  - [{c['id']}] {c['front']}: {c['back'][:80]}...")
