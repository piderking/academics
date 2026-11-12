import json

with open('G:/My Drive/Academics/study_portal/decks.json', 'r', encoding='utf-8') as f:
    portal_data = json.load(f)

print('Current deck count:', len(portal_data.get('decks', [])))
for d in portal_data.get('decks', []):
    print(f"  - {d.get('id')} ({d.get('course')}): {d.get('title')} [{len(d.get('flashcards', []))} cards]")

with open('G:/My Drive/Academics/study_portal/midterm2_deck.json', 'r', encoding='utf-8') as f:
    new_deck = json.load(f)

# Replace if exists, or append
existing_idx = None
for i, d in enumerate(portal_data.get('decks', [])):
    if d.get('id') == new_deck['id'] or d.get('title').strip().lower() == 'midterm #2 botany':
        existing_idx = i
        break

if existing_idx is not None:
    print(f"Replacing existing deck at index {existing_idx}")
    portal_data['decks'][existing_idx] = new_deck
else:
    print("Appending new deck to decks.json")
    portal_data['decks'].append(new_deck)

with open('G:/My Drive/Academics/study_portal/decks.json', 'w', encoding='utf-8') as f:
    json.dump(portal_data, f, indent=2)

print("Updated decks.json successfully! Total decks now:", len(portal_data['decks']))
