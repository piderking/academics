import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("G:/My Drive/Academics/vincent_chin_transcript.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
print(f"Total words: {len(words)}")

print("\n=== OPENING ===")
print(" ".join(words[:250]))

# Search for the strip club argument, Ebens quotes, sentence, and protests
search_phrases = ["because of you", "kaufman", "probation", "3,000", "lily chin", "american citizens for justice", "baseball bat", "plea bargain"]
for phrase in search_phrases:
    print(f"\n=== MENTIONS OF '{phrase.upper()}' ===")
    p_len = len(phrase.split())
    matches = [i for i in range(len(words)-p_len) if " ".join(words[i:i+p_len]).lower() == phrase.lower()]
    for m in matches[:2]:
        start = max(0, m - 25)
        end = min(len(words), m + 35)
        print("..." + " ".join(words[start:end]) + "...")
