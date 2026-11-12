import pypdf

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

for p in range(580, 640):
    txt = reader.pages[p].extract_text() or ""
    fig_lines = [l.strip() for l in txt.splitlines() if 'FIGURE 9-' in l or 'FIGURE B9-' in l or 'CHAPTER 9' in l]
    if fig_lines or 'Flower' in txt[:100]:
        first_line = fig_lines[0] if fig_lines else txt[:80].replace('\n', ' ')
        print(f"Page {p+1} (idx {p}): {len(reader.pages[p].images)} imgs | {first_line[:85]}")
