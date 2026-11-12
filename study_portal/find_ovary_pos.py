import pypdf

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

for p in range(618, 665):
    txt = reader.pages[p].extract_text() or ""
    if any(k in txt.lower() for k in ['superior', 'inferior', 'hypogynous', 'epigynous', 'perigynous']):
        print(f"Page {p+1} (idx {p}): found ovary position terms")
        for line in txt.splitlines():
            if any(k in line.lower() for k in ['superior', 'inferior', 'hypogynous', 'epigynous', 'perigynous', 'ovary']):
                print("   ", line.strip()[:90])
