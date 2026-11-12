import pypdf
import os

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

# Let's inspect images on pages 620-662
for p in range(618, 665):
    page = reader.pages[p]
    if page.images:
        for name, img in page.images.items():
            if len(img.data) > 20000: # larger than 20KB
                print(f"Page {p+1} (idx {p}): {name} ({len(img.data)//1024} KB)")
