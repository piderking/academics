import pypdf
import re

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")
print("Total pages in Mauseth:", len(reader.pages))

# Search for Chapter titles in the first 25 pages (TOC)
toc_text = ""
for i in range(min(25, len(reader.pages))):
    toc_text += f"\n--- Page {i+1} ---\n" + reader.pages[i].extract_text()

matches = re.findall(r'(Chapter\s+\d+[:\s]+[^\n]+)', toc_text, re.IGNORECASE)
for m in matches:
    print(m)

# Specifically look for Flower or Reproduction in TOC
for line in toc_text.split('\n'):
    if any(k in line.lower() for k in ['flower', 'reproduction', 'angiosperm', 'inflorescence', 'fruit', 'woody', 'secondary']):
        print("  TOC line:", line.strip())
