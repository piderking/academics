import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("G:/My Drive/Academics/study_portal/decks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

quizzes = data["decks"][0]["quizzes"]
print(f"Total quizzes: {len(quizzes)}")
for i, q in enumerate(quizzes):
    print(f"Q{i+1}: {q['question']}")
    print(f"   Options: {q.get('options')}")
    print(f"   Answer: {q.get('answer')}")
    print(f"   Explanation: {q.get('explanation')[:80]}...\n")
