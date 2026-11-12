import pypdf

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

for p in range(664, 680):
    txt = reader.pages[p].extract_text() or ""
    figs = [l.strip() for l in txt.splitlines() if 'FIGURE 9-' in l or 'FIGURE B9-' in l or 'TABLE 9-' in l]
    if figs:
        print(f"Page {p+1} (idx {p}): {len(reader.pages[p].images)} imgs | {figs[0][:80]}")
