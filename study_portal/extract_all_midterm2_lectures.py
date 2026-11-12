import pypdf
import os
import glob
import re
import json

midterm2_dir = r"G:\My Drive\Academics\BOT-1121 (1)\Midterm 2"
pdf_files = sorted(glob.glob(os.path.join(midterm2_dir, "*.pdf")))

out_dir = r"G:\My Drive\Academics\study_portal\images\bot-1121-m2-slides"
os.makedirs(out_dir, exist_ok=True)

lecture_data = {}

for pdf_path in pdf_files:
    fname = os.path.basename(pdf_path)
    reader = pypdf.PdfReader(pdf_path)
    num_pages = len(reader.pages)
    
    slides_text = []
    extracted_imgs = []
    
    # Extract text from all pages
    for p in range(num_pages):
        page = reader.pages[p]
        txt = (page.extract_text() or "").strip()
        slides_text.append({"slide": p + 1, "text": txt})
        
        # Check for prominent images (save top images from each lecture)
        if page.images:
            for idx_img, img_obj in enumerate(page.images):
                if len(img_obj.data) > 35000: # larger than 35KB
                    clean_lec = re.sub(r'[^a-zA-Z0-9]', '_', fname.replace('.pdf',''))[:25]
                    img_name_str = getattr(img_obj, 'name', f'img_{idx_img}')
                    if not isinstance(img_name_str, str):
                        img_name_str = f"img_{idx_img}"
                    ext = '.jpg'
                    if hasattr(img_obj, 'image') and img_obj.image and hasattr(img_obj.image, 'format'):
                        ext = f".{img_obj.image.format.lower()}"
                    img_fname = f"{clean_lec}_p{p+1}_{idx_img}{ext}"
                    img_fpath = os.path.join(out_dir, img_fname)
                    if not os.path.exists(img_fpath):
                        with open(img_fpath, "wb") as f_img:
                            f_img.write(img_obj.data)
                    extracted_imgs.append({"slide": p + 1, "filename": f"images/bot-1121-m2-slides/{img_fname}", "size_kb": len(img_obj.data)//1024})

    lecture_data[fname] = {
        "pages": num_pages,
        "slides": slides_text,
        "images": extracted_imgs
    }
    print(f"Processed {fname}: {num_pages} slides, {len(extracted_imgs)} high-res images extracted.")

with open("G:/My Drive/Academics/study_portal/midterm2_lecture_extracted.json", "w", encoding="utf-8") as f:
    json.dump(lecture_data, f, indent=2)

print("\nSaved all lecture extractions to midterm2_lecture_extracted.json!")
