import pypdf
import os
from PIL import Image

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")
out_dir = r"G:\My Drive\Academics\study_portal\images\bot-1121-flowers"

# Page 665 (idx 664)
page = reader.pages[664]
print("Images on page 665:", len(page.images))
count = 0
for name, img in page.images.items():
    print(f"Image {name}: {len(img.data)} bytes")
    if len(img.data) > 10000:
        ext = os.path.splitext(name)[1] or '.jpg'
        fname = f"fig_9_28_ovary_positions_superior_inferior{ext}"
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "wb") as f:
            f.write(img.data)
        im = Image.open(fpath)
        print(f"Saved {fname} ({len(img.data)//1024} KB, size {im.size})")
