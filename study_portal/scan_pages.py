import pypdf

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

for p in range(1300, 1750, 10):
    txt = (reader.pages[p].extract_text() or "")[:150].replace('\n', ' ')
    if any(k in txt.lower() for k in ['chapter 8', 'chapter 9', 'woody', 'flowers']):
        print(f"Page {p}: {txt}")
