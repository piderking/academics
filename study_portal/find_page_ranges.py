import pypdf
import re

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")
total = len(reader.pages)

# Step through every 20 pages to locate Chapter 8 and 9
for p in range(0, total, 25):
    txt = reader.pages[p].extract_text() or ""
    if "chapter 8" in txt.lower():
        print(f"Ch 8 mention at page {p}")
    if "structure of woody plants" in txt.lower():
        print(f"Woody plants at page {p}")
    if "chapter 9" in txt.lower():
        print(f"Ch 9 mention at page {p}")
    if "flowers and reproduction" in txt.lower():
        print(f"Flowers at page {p}")
