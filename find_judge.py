with open("G:/My Drive/Academics/vincent_chin_transcript.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
for i, w in enumerate(words):
    if "judge" in w.lower():
        start = max(0, i - 15)
        end = min(len(words), i + 25)
        print(" ".join(words[start:end]))
        print("---")
