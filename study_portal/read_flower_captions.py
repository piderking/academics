import pypdf
import os

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

pages_to_check = [619, 620, 621, 625, 626, 627, 628, 629, 633, 634, 650, 658, 660, 663]

for p in pages_to_check:
    txt = reader.pages[p].extract_text() or ""
    figs = [l.strip() for l in txt.splitlines() if 'FIGURE 9-' in l or 'FIGURE B9-' in l or 'TABLE 9-' in l]
    print(f"=== Page {p+1} (idx {p}) ===")
    for f in figs:
        print("  ", f[:100])
