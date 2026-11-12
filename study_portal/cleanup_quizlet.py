import json
import os

decks_path = "G:/My Drive/Academics/study_portal/decks.json"
with open(decks_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Remove the old Quizlet midterm 2 deck
old_count = len(data.get("decks", []))
data["decks"] = [d for d in data.get("decks", []) if d.get("id") != "bot-1121-midterm-2"]
new_count = len(data["decks"])
print(f"Removed old Quizlet deck. Decks count: {old_count} -> {new_count}")

with open(decks_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Remove obsolete scratch files from quizlet scraping
obsolete_files = [
    "G:/My Drive/Academics/study_portal/set1_cards.json",
    "G:/My Drive/Academics/study_portal/set2_cards.json",
    "G:/My Drive/Academics/study_portal/midterm2_deck.json",
    "G:/My Drive/Academics/study_portal/scrape_quizlet.js",
    "G:/My Drive/Academics/study_portal/scrape_set2.js",
    "G:/My Drive/Academics/study_portal/scrape_both_sets.js",
    "G:/My Drive/Academics/study_portal/fetch_quizlet.py",
    "G:/My Drive/Academics/study_portal/quizlet_scraped_data.json"
]

for fp in obsolete_files:
    if os.path.exists(fp):
        try:
            os.remove(fp)
            print(f"Deleted obsolete file: {fp}")
        except Exception as e:
            print(f"Could not delete {fp}: {e}")
