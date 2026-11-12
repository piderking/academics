import urllib.request
import re

url = 'https://archive.org/download/Japanese1943/Japanese1943.asr.srt'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        srt_content = resp.read().decode('utf-8', errors='ignore')
    
    # Strip SRT numbers and timestamps
    lines = srt_content.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\d+$', line):
            continue
        if '-->' in line:
            continue
        clean_lines.append(line)
    
    full_text = " ".join(clean_lines)
    print(f"Downloaded Japanese Relocation transcript! Length: {len(full_text)} characters, {len(full_text.split())} words")
    with open("G:/My Drive/Academics/japanese_relocation_1943_transcript.txt", "w", encoding="utf-8") as f:
        f.write(full_text)
    print("Saved to japanese_relocation_1943_transcript.txt")
except Exception as e:
    print("Error:", e)
