import pypdf
import os
from PIL import Image

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")
out_dir = r"G:\My Drive\Academics\study_portal\images\bot-1121-flowers"

# Figure 9-31 on page 669 (idx 668)
page = reader.pages[668]
for name, img in page.images.items():
    if len(img.data) > 10000:
        fname = "fig_9_31_inflorescence_types.jpg"
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "wb") as f:
            f.write(img.data)
        im = Image.open(fpath)
        print(f"Saved {fname} ({len(img.data)//1024} KB, size {im.size})")

# Figure 9-32 on page 671 or 672
for p in [670, 671, 672]:
    page = reader.pages[p]
    for name, img in page.images.items():
        if len(img.data) > 15000:
            fname = f"fig_9_32_fruit_types_strawberry_aggregate_{p}.jpg"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "wb") as f:
                f.write(img.data)
            im = Image.open(fpath)
            print(f"Saved {fname} ({len(img.data)//1024} KB, size {im.size})")
