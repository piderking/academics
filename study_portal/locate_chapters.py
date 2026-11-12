import pypdf
import re

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

# Search for pages mentioning flower anatomy, floral whorls, stamen, carpel, sepal, petal, ovary
# and tree anatomy: wood, annual ring, bark, periderm, lenticel, sapwood, heartwood
print("Searching for Chapter 8 and 9 page ranges...")

def search_text_in_range(start, end, keywords):
    matches = []
    for p in range(start, end):
        txt = reader.pages[p].extract_text()
        if any(k in txt.lower() for k in keywords):
            matches.append((p, txt[:200].replace('\n', ' ')))
    return matches

# Let's find Chapter 8 (Woody plants) and Chapter 9 (Flowers) start pages
ch8_start = None
ch9_start = None
ch10_start = None

for p in range(15, 60):
    txt = reader.pages[p].extract_text()
    if 'Chapter 8' in txt and 'Structure of Woody Plants' in txt:
        ch8_start = p
    if 'Chapter 9' in txt and 'Flowers and Reproduction' in txt:
        ch9_start = p
    if 'Chapter 10' in txt and 'Photosynthesis' in txt:
        ch10_start = p

print("TOC references found:", ch8_start, ch9_start, ch10_start)

# Let's search for actual chapter headings in pages 400-1100
for p in range(400, 1100, 50):
    txt = reader.pages[p].extract_text()
    # sample
    m = re.findall(r'CHAPTER\s+\d+', txt, re.IGNORECASE)
    if m:
        print(f"Page {p}: {m}")
