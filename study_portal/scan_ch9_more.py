import pypdf

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

for p in range(639, 665):
    txt = reader.pages[p].extract_text() or ""
    fig_lines = [l.strip() for l in txt.splitlines() if 'FIGURE 9-' in l or 'FIGURE B9-' in l]
    if fig_lines:
        print(f"Page {p+1} (idx {p}): {len(reader.pages[p].images)} imgs | {fig_lines[0][:85]}")
