import os

img_dir = "G:/My Drive/Academics/study_portal"
check_paths = [
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p43_0.png",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p32_2.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p5_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p30_2.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p6_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p5_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p17_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p15_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p26_0.jpeg",
    "images/diagrams/flower_structure.svg",
    "images/diagrams/fern_structure.svg",
    "images/diagrams/seed_structure.svg",
    "images/diagrams/plant_body_structure.svg",
    "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p16_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p12_1.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p2_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p5_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p13_2.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p10_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p18_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p26_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p31_2.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p5_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p22_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p25_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p30_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p8_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p14_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p18_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p13_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p21_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p24_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p35_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p37_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p5_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p7_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p24_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p28_0.jpeg",
    "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p30_0.jpeg",
]

all_found = True
for rel in check_paths:
    full = os.path.join(img_dir, rel)
    if not os.path.exists(full):
        print(f"MISSING: {rel}")
        all_found = False
    else:
        print(f"FOUND: {rel}")

if all_found:
    print("ALL IMAGES VERIFIED!")
