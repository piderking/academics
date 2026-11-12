import pypdf
import os
from PIL import Image

out_dir = r"G:\My Drive\Academics\study_portal\images\bot-1121-flowers"
os.makedirs(out_dir, exist_ok=True)

reader = pypdf.PdfReader("G:/My Drive/Academics/Textbooks/Botany - James D. Mauseth.pdf")

pages_map = {
    619: "fig_9_3_flower_anatomy_four_whorls",
    625: "fig_9_6_stamens_and_carpels_flower_structure",
    626: "fig_9_7_calyx_sepals_receptacle",
    627: "fig_9_8_stamens_anther_filament",
    629: "fig_9_10_anther_cross_section_pollen_sacs",
    633: "fig_9_12_ovary_cross_section_carpels_ovules",
    650: "fig_9_21_flower_receptacle_fruit_development",
    658: "fig_9_25_monoecious_inflorescences_corn",
    660: "fig_9_26_flower_symmetry_radial_bilateral"
}

for p_idx, base_name in pages_map.items():
    page = reader.pages[p_idx]
    count = 0
    for img_name, img_obj in page.images.items():
        if len(img_obj.data) > 15000: # larger than 15KB
            ext = os.path.splitext(img_name)[1] or '.jpg'
            fname = f"{base_name}_{count}{ext}" if count > 0 else f"{base_name}{ext}"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "wb") as f:
                f.write(img_obj.data)
            im = Image.open(fpath)
            print(f"Page {p_idx+1} -> {fname} ({len(img_obj.data)//1024} KB, size {im.size})")
            count += 1

print("Extraction of flower figures complete!")
