import json
import re

decks_path = "G:/My Drive/Academics/study_portal/decks.json"
with open(decks_path, "r", encoding="utf-8") as f:
    portal_data = json.load(f)

deck = None
deck_idx = None
for i, d in enumerate(portal_data["decks"]):
    if d["id"] == "bot-1121-midterm-2":
        deck = d
        deck_idx = i
        break

if not deck:
    print("Error: bot-1121-midterm-2 deck not found!")
    exit(1)

print(f"Current flashcards: {len(deck['flashcards'])}, quizzes: {len(deck['quizzes'])}")

# 1. Update existing cards with relevant images and pedagogical descriptions
card_img_map = {
    # Flower cards
    "m2-011": {
        "image": "images/bot-1121-flowers/fig_9_7_calyx_sepals_receptacle.jpg",
        "imageDescription": "Flower bud enclosed by sepals forming the calyx, attached to the expanded receptacle stem tip."
    },
    "m2-012": {
        "image": "images/bot-1121-flowers/fig_9_12_ovary_cross_section_carpels_ovules.jpg",
        "imageDescription": "Cross-section of an ovary composed of multiple fused carpels, showing separate chambers (locules) bearing ovules attached at the central placenta."
    },
    "m2-036": {
        "image": "images/bot-1121-flowers/fig_9_3_flower_anatomy_four_whorls.jpg",
        "imageDescription": "Schematic diagram of the four concentric floral whorls: calyx (sepals), corolla (petals), androecium (stamens), and gynoecium (carpels/pistil)."
    },
    "m2-037": {
        "image": "images/bot-1121-flowers/fig_9_26_flower_symmetry_radial_bilateral.jpg",
        "imageDescription": "Flower symmetry comparison: Actinomorphic (radial symmetry with multiple planes of division) vs. Zygomorphic (bilateral symmetry with only one plane of division)."
    },
    "m2-048": {
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Inferior ovary (epigynous flower): the ovary is embedded within the receptacle/hypanthium tissue below the point where sepals, petals, and stamens insert."
    },
    "m2-064": {
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Ovary positions: Superior (hypogynous - ovary sits entirely above perianth attachment) vs. Inferior (epigynous - ovary sits below perianth insertion)."
    },
    "m2-088": {
        "image": "images/bot-1121-flowers/fig_9_8_stamens_anther_filament.jpg",
        "imageDescription": "Stamen structure consisting of a slender stalk (filament) supporting a four-lobed terminal anther containing pollen sacs."
    },
    "m2-092": {
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Superior ovary (hypogynous flower): carpel/ovary originates above the attachment points of sepals, petals, and stamens on the receptacle."
    },
    "m2-060": {
        "image": "images/bot-1121-flowers/fig_9_25_monoecious_inflorescences_corn.jpg",
        "imageDescription": "Monoecious plant (Zea mays / corn) showing separate staminate flowers (tassels at apex) and carpellate flowers (ears with silks/styles along stem) on the same individual."
    },
    "m2-003": {
        "image": "images/bot-1121-flowers/fig_9_32_fruit_types_strawberry_aggregate_671.jpg",
        "imageDescription": "Aggregate fruit (e.g., strawberry): develops from a single flower containing numerous separate carpels/pistils on an enlarged fleshy receptacle."
    },
    "m2-049": {
        "image": "images/bot-1121-flowers/fig_9_31_inflorescence_types.jpg",
        "imageDescription": "Comparative inflorescence branching architectures: simple indeterminate raceme, spike, umbel, head/capitulum, and catkin."
    },
    "m2-077": {
        "image": "images/bot-1121-flowers/fig_9_3_flower_anatomy_four_whorls.jpg",
        "imageDescription": "Hierarchy of flower anatomy from outer sterile perianth whorls (calyx & corolla) to inner fertile reproductive whorls (androecium & gynoecium)."
    }
}

for c in deck["flashcards"]:
    cid = c["id"]
    if cid in card_img_map:
        c["image"] = card_img_map[cid]["image"]
        c["imageDescription"] = card_img_map[cid]["imageDescription"]

# 2. Add high-impact dedicated visual identification cards for flowers and trees
new_identifying_cards = [
    # --- FLOWER IDENTIFICATION CARDS ---
    {
        "id": "m2-id-flw-01",
        "front": "🔬 **Flower Identification**: Examine the four concentric whorls of a complete flower. Identify the four whorls from outermost to innermost and state the sterile vs. fertile components.",
        "hint": "Start from the protective green outer leaf-like structures and move inward toward the seed-producing core.",
        "back": "The four concentric floral whorls (from outermost to innermost) are:\n\n1. **Calyx (Sepals)**: Outermost sterile whorl; protects the developing floral bud before anthesis.\n2. **Corolla (Petals)**: Second sterile whorl; often pigmented or scented to attract specific animal pollinators.\n*(Calyx + Corolla together form the **Perianth**)*.\n3. **Androecium (Stamens)**: Third whorl (fertile male); each consists of a slender **filament** and a terminal **anther** housing four pollen sacs (microsporangia).\n4. **Gynoecium (Carpels / Pistil)**: Innermost whorl (fertile female); consists of the receptive **stigma**, guiding **style**, and basal **ovary** enclosing one or more ovules.",
        "image": "images/bot-1121-flowers/fig_9_3_flower_anatomy_four_whorls.jpg",
        "imageDescription": "Schematic diagram of an angiosperm flower displaying receptacle, sepals (calyx), petals (corolla), stamens (filament + anther), and carpels (stigma + style + ovary + ovules).",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-3)",
        "tags": ["reproduction", "flower-anatomy", "whorls"]
    },
    {
        "id": "m2-id-flw-02",
        "front": "🔬 **Flower Identification**: Examine this male reproductive unit. Identify the two primary structural parts of the **stamen** and explain their physiological functions.",
        "hint": "One part is a structural stalk for spatial presentation; the other is the four-lobed pollen factory.",
        "back": "A **Stamen** consists of two distinct regions:\n\n1. **Filament**: The slender stalk that elevates and positions the anther for optimal contact with pollinators or wind currents.\n2. **Anther**: The terminal fertile organ, typically composed of **two thecae** containing **four microsporangia (pollen sacs)** where microsporocytes undergo meiosis to generate haploid pollen grains (microgametophytes).",
        "image": "images/bot-1121-flowers/fig_9_8_stamens_anther_filament.jpg",
        "imageDescription": "High-magnification view of stamens showing the elongated filaments topped by pollen-bearing anthers shedding mature yellow pollen grains.",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-8)",
        "tags": ["reproduction", "stamen", "anther"]
    },
    {
        "id": "m2-id-flw-03",
        "front": "🔬 **Flower Identification**: Examine this cross-section of a mature lily anther. Identify the internal chambers and the cell types produced inside.",
        "hint": "Look for the four symmetrical lobes containing countless developing haploid grains.",
        "back": "This micrograph reveals the cross-section of an **Anther**:\n\n* **Pollen Sacs (Microsporangia)**: Four circular chambers lined internally by a nutritive layer called the **tapetum**.\n* **Microsporocytes (Pollen Mother Cells)**: Diploid cells within the locules that undergo **meiosis** to produce tetrads of haploid **microspores**.\n* **Pollen Grains**: Mature into two-celled male gametophytes containing a **tube cell** (for pollen tube growth) and a **generative cell** (which divides into two sperm cells).",
        "image": "images/bot-1121-flowers/fig_9_10_anther_cross_section_pollen_sacs.jpg",
        "imageDescription": "Transverse section of a Lilium anther displaying four distinct microsporangia chambers packed with microsporocytes and pollen grains.",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-10)",
        "tags": ["reproduction", "anther", "microscopy"]
    },
    {
        "id": "m2-id-flw-04",
        "front": "🔬 **Flower Identification**: Examine the female reproductive unit (**carpel / pistil**). What are its three vertical regions, and what does the basal region contain?",
        "hint": "Think of the receptive sticky top, the transmission neck, and the swollen chamber at the base.",
        "back": "A **Carpel / Pistil** comprises three distinct zones:\n\n1. **Stigma**: The uppermost receptive surface, often covered with papillate cells and sticky exudate to capture and hydrate compatible pollen grains.\n2. **Style**: The neck-like column of tissue through which the pollen tube germinates and elongates toward the ovary.\n3. **Ovary**: The swollen basal chamber enclosing one or more **ovules** (megasporangia). Following double fertilization, the ovary wall matures into the **pericarp (fruit)** while the fertilized ovules become **seeds**.",
        "image": "images/bot-1121-flowers/fig_9_6_stamens_and_carpels_flower_structure.jpg",
        "imageDescription": "Longitudinal dissection of a flower illustrating central carpels with prominent stigmatic surface, elongated style, and basal ovary surrounded by stamens.",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-6)",
        "tags": ["reproduction", "carpel", "pistil"]
    },
    {
        "id": "m2-id-flw-05",
        "front": "🔬 **Flower Identification**: Examine this ovary transverse section. Identify the **locules**, the **ovules**, and the central **placenta**.",
        "hint": "Notice how multiple fused carpels create internal compartments (like segments in an orange or bell pepper).",
        "back": "This ovary cross-section demonstrates a **compound pistil** formed by three fused carpels:\n\n* **Locules**: The three distinct cavities or internal chambers inside the ovary.\n* **Septa**: The dividing internal walls formed by the fused margins of adjacent carpels.\n* **Ovules**: The developing megasporangia attached to the central column via short stalks called **funiculi**.\n* **Placentation**: **Axile placentation**, where ovules originate from the central axis of a multilocular ovary.",
        "image": "images/bot-1121-flowers/fig_9_12_ovary_cross_section_carpels_ovules.jpg",
        "imageDescription": "Transverse section of a compound syncarpous ovary showing three distinct locules, thick outer pericarp wall, central axile placentation, and developing ovules.",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-12)",
        "tags": ["reproduction", "ovary", "microscopy"]
    },
    {
        "id": "m2-id-flw-06",
        "front": "🔬 **Flower Identification**: Compare the two flower cross-sections shown. How do you distinguish a **Superior Ovary** from an **Inferior Ovary**?",
        "hint": "Look at the level of insertion of the sepals, petals, and stamens relative to the base of the ovary.",
        "back": "The distinction depends on the relative insertion point of perianth whorls:\n\n* **Superior Ovary (Hypogynous Flower)**: The ovary is positioned **above** the receptacle attachment point. Sepals, petals, and stamens insert beneath the ovary (e.g., tomatoes, lilies, peaches).\n* **Inferior Ovary (Epigynous Flower)**: The ovary is embedded **below** the floral whorls, enclosed within the receptacle or fused floral cup (hypanthium). Sepals, petals, and stamens appear to emerge from the top of the fruit (e.g., apples, cucumbers, squash).",
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Diagram comparing (A) superior ovary with hypogynous insertion versus (B) inferior ovary with epigynous insertion embedded in the receptacle/hypanthium.",
        "citation": "Mauseth Botany (Ch. 9, Fig. 9-28)",
        "tags": ["reproduction", "ovary-position", "morphology"]
    },

    # --- TREE & WOODY STEM IDENTIFICATION CARDS ---
    {
        "id": "m2-id-tree-01",
        "front": "🔬 **Tree Anatomy Identification**: Examine this transverse cross-section of a mature tree trunk. Identify the dark central core, the pale outer wood, the cambium line, and the bark.",
        "hint": "The dark core is non-functional for transport; the lighter outer zone actively moves water.",
        "back": "A mature woody tree trunk exhibits concentric structural zones:\n\n1. **Heartwood (Duramen)**: The dark, central cylinder of secondary xylem. Vessels and tracheids are permanently plugged by **tyloses** and saturated with decay-resistant tannins, resins, and polyphenols. Functions exclusively for **mechanical support**.\n2. **Sapwood (Alburnum)**: The lighter, active outer secondary xylem that maintains living parenchyma and **conducts water and minerals** upward.\n3. **Vascular Cambium**: Microscopic single-cell layer between sapwood and bark that produces new wood inward and new phloem outward.\n4. **Inner Bark**: Living **secondary phloem** transporting photosynthetic sugars.\n5. **Outer Bark (Periderm)**: Layers of suberized dead **cork cells (phellem)** that prevent desiccation and pathogen invasion.",
        "image": "images/bot-1121-secondary-growth/fig_8_18_heartwood_vs_sapwood.jpg",
        "imageDescription": "Cross-section of a Quercus nigra (water oak) trunk showing dark heartwood, pale active sapwood, annual rings, vascular cambium boundary, and outer bark.",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-18)",
        "tags": ["secondary-growth", "tree-anatomy", "wood"]
    },
    {
        "id": "m2-id-tree-02",
        "front": "🔬 **Tree Anatomy Identification**: Examine these concentric growth rings in secondary xylem. What anatomical difference creates the visible boundary between **Early Wood** and **Late Wood**?",
        "hint": "Compare vessel lumen diameter and cell wall thickness between spring and late summer.",
        "back": "An **Annual Growth Ring** represents one seasonal growth flush of secondary xylem:\n\n* **Early Wood (Springwood)**: Produced at the start of the season when soil moisture is high; characterized by **large vessel lumens and thin secondary walls** to maximize volumetric water conduction.\n* **Late Wood (Summerwood)**: Formed as moisture becomes limited; characterized by **narrow, small vessel elements and dense, thick-walled fibers** for structural rigidity.\n* **The Ring Boundary**: The abrupt transition from the narrow, dense latewood of one year to the wide, expansive vessel lumens of the subsequent spring forms the visible tree ring.",
        "image": "images/bot-1121-secondary-growth/fig_8_17_growth_rings_early_late_wood.jpg",
        "imageDescription": "High-magnification transverse micrograph of wood showing distinct boundaries between five annual growth rings with large earlywood vessels transitioning to dense latewood fibers.",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-17)",
        "tags": ["secondary-growth", "growth-rings", "tree-anatomy"]
    },
    {
        "id": "m2-id-tree-03",
        "front": "🔬 **Tree Anatomy Identification**: Examine this cross-section through the outer bark of a woody stem. Identify the three layers of the **Periderm**.",
        "hint": "Identify the dead waxy outer cells, the single meristematic initial layer, and the inner parenchyma layer.",
        "back": "The **Periderm** (secondary protective dermal tissue) replaces the epidermis in woody stems and roots and consists of three layers:\n\n1. **Cork (Phellem)**: Outermost dead layer; cells are densely packed and coated internally with impermeable waxy **suberin** to resist water loss, fire, and pathogens.\n2. **Cork Cambium (Phellogen)**: The lateral meristem that originates from cortical parenchyma; divides periclinally to produce cork outward and phelloderm inward.\n3. **Phelloderm**: Innermost living layer composed of parenchyma cells that function in storage and photosynthesis.",
        "image": "images/bot-1121-secondary-growth/fig_8_24_periderm_cork_phelloderm.jpg",
        "imageDescription": "Micrograph of periderm showing outer stacked radial rows of suberized cork cells (phellem), thin cork cambium (phellogen), and inner phelloderm cells.",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-24)",
        "tags": ["secondary-growth", "periderm", "tree-bark"]
    },
    {
        "id": "m2-id-tree-04",
        "front": "🔬 **Tree Anatomy Identification**: What is this raised porous fissure on the bark of a tree branch, and what vital physiological function does it perform?",
        "hint": "Because cork is waterproof and airtight, living cells beneath need a breathing chimney.",
        "back": "This structure is a **Lenticel**:\n\n* **Structure**: A raised, lens-shaped rupture in the periderm where the cork cambium produces rounded, **unsuberized complementary cells** with extensive intercellular air spaces.\n* **Function**: Permits **gas exchange (aeration)**—allowing oxygen to diffuse into the metabolically active inner bark, vascular cambium, and ray parenchyma while releasing carbon dioxide, circumventing the impervious barrier of suberized cork.",
        "image": "images/bot-1121-secondary-growth/fig_8_25_bark_and_lenticels.jpg",
        "imageDescription": "Transverse section of a woody twig showing a lenticel: an opening in the suberized cork layer packed with loosely arranged complementary cells facilitating gas diffusion.",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-25)",
        "tags": ["secondary-growth", "lenticel", "gas-exchange"]
    },
    {
        "id": "m2-id-tree-05",
        "front": "🔬 **Tree Anatomy Identification**: Examine the active meristematic boundary between wood and bark. How does the **Vascular Cambium** divide to increase tree girth?",
        "hint": "One division plane produces xylem and phloem; the other plane expands the cambium's circumference.",
        "back": "The **Vascular Cambium** increases stem circumference via two types of cell divisions:\n\n1. **Periclinal Divisions (Additive Divisions)**: Form cell division planes parallel to the stem surface. Cells cut off toward the **inside** differentiate into **secondary xylem (wood)**; cells cut off toward the **outside** differentiate into **secondary phloem (inner bark)**.\n2. **Anticlinal Divisions (Multiplicative Divisions)**: Form cell division planes perpendicular to the surface. These divisions increase the number of cambial cells, allowing the cambium ring to **expand in circumference** as the woody core widens.",
        "image": "images/bot-1121-secondary-growth/fig_8_20_cambial_zone_xylem_phloem_1.jpg",
        "imageDescription": "Transverse section through the vascular cambial zone showing thin-walled meristematic initials dividing between dense secondary xylem (bottom) and secondary phloem (top).",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-20)",
        "tags": ["secondary-growth", "vascular-cambium", "meristem"]
    },
    {
        "id": "m2-id-tree-06",
        "front": "🔬 **Tree Anatomy Identification**: Wood anatomy is studied along three geometric planes. Name the three cuts shown in this 3D cube of wood.",
        "hint": "One is across the trunk; one is parallel to rays; one is perpendicular to rays.",
        "back": "The three anatomical planes of wood are:\n\n1. **Transverse (Cross-Section)**: Cut perpendicular to the long axis of the stem; reveals annual growth rings, vessel diameters, and radial ray ribbons.\n2. **Radial Section**: Longitudinal cut that passes directly through the center of the stem (pith); runs **parallel to wood rays**, showing rays as horizontal brick-like sheets of parenchyma.\n3. **Tangential Section**: Longitudinal cut made perpendicular to rays; shows rays in end-on profile (as lens-shaped heights of cells) and reveals whether the cambium was storied or nonstoried.",
        "image": "images/bot-1121-secondary-growth/fig_8_11_wood_block_3d_planes.jpg",
        "imageDescription": "Scanning electron micrograph and 3D diagram of a block of secondary xylem displaying transverse, radial, and tangential viewing faces.",
        "citation": "Mauseth Botany (Ch. 8, Fig. 8-11)",
        "tags": ["secondary-growth", "wood-anatomy", "3d-planes"]
    }
]

# Append new cards (avoiding duplicate IDs)
existing_ids = {c["id"] for c in deck["flashcards"]}
added_cards_count = 0
for nc in new_identifying_cards:
    if nc["id"] not in existing_ids:
        deck["flashcards"].append(nc)
        added_cards_count += 1

print(f"Added {added_cards_count} dedicated visual identification cards.")
print(f"Total flashcards now: {len(deck['flashcards'])}")

# 3. Add practical visual exam questions to Quizzes
new_visual_quizzes = [
    {
        "id": "m2-q07",
        "station": "Station 7: Floral Whorl Architecture",
        "question": "Examine the provided complete flower diagram. Which labeled whorl represents the fertile female gynoecium, and what are its three essential anatomical parts?",
        "options": [
            "Innermost whorl; Stigma, Style, and Ovary",
            "Outermost whorl; Sepals, Petals, and Receptacle",
            "Third whorl; Filament and Anther",
            "Second whorl; Corolla, Hypanthium, and Nectar Guide"
        ],
        "correctIndex": 0,
        "explanation": "The gynoecium is the innermost fourth whorl composed of one or more carpels. Each typical carpel consists of a receptive apical stigma, an elongate style for pollen tube guidance, and a basal ovary containing ovules.",
        "socraticHint": "Follow the concentric whorls from the outer protective sepals to the center of the floral axis.",
        "image": "images/bot-1121-flowers/fig_9_3_flower_anatomy_four_whorls.jpg",
        "citation": "BOT 121 Lecture: Flower Morphology (Fig. 9-3)"
    },
    {
        "id": "m2-q08",
        "station": "Station 8: Tree Trunk Zonation",
        "question": "In this transverse section of a mature oak trunk, what accounts for the dark coloration and physiological function of the central heartwood compared to the outer sapwood?",
        "options": [
            "It conducts all upward water transport under high tensile pressure",
            "Its vessels are permanently occluded by tyloses and infused with antimicrobial tannins and resins for decay resistance and structural support",
            "It is composed exclusively of living secondary phloem storing starch",
            "It is produced by primary apical meristems rather than the vascular cambium"
        ],
        "correctIndex": 1,
        "explanation": "Heartwood (duramen) consists of older, non-functional secondary xylem. Surrounding parenchyma cells push bladder-like outgrowths (tyloses) into vessel lumens and saturate the wood with aromatic compounds, tannins, and resins, creating rot-resistant structural support.",
        "socraticHint": "Determine whether the dark central core continues to conduct water or is chemically plugged for mechanical support.",
        "image": "images/bot-1121-secondary-growth/fig_8_18_heartwood_vs_sapwood.jpg",
        "citation": "BOT 121 Lecture: Woody Plants & Secondary Xylem (Fig. 8-18)"
    },
    {
        "id": "m2-q09",
        "station": "Station 9: Tree Bark & Gas Exchange",
        "question": "Examine the micrograph of this tree bark fissure. What is this specialized aeration opening called, and what cell type facilitates gas diffusion through the impervious suberin barrier?",
        "options": [
            "Stoma; Guard cells swollen with potassium ions",
            "Lenticel; Loosely packed, unsuberized complementary parenchyma cells",
            "Resin canal; Secretory epithelial cells",
            "Hydathode; Epithem tracheary cells"
        ],
        "correctIndex": 1,
        "explanation": "Lenticels are macroscopic ruptures in the cork layer of periderm. The cork cambium produces loosely arranged, round, unsuberized complementary cells with abundant intercellular spaces, enabling oxygen diffusion to living tissues beneath.",
        "socraticHint": "Distinguish between microscopic leaf epidermis valves (stomata) versus macroscopic bark aeration pores in woody periderm.",
        "image": "images/bot-1121-secondary-growth/fig_8_25_bark_and_lenticels.jpg",
        "citation": "BOT 121 Lecture: Bark & Periderm Anatomy (Fig. 8-25)"
    },
    {
        "id": "m2-q10",
        "station": "Station 10: Ovary Position Diagnosis",
        "question": "Examine diagram (B) showing an Inferior Ovary (epigynous flower). Where do the perianth parts (sepals and petals) and stamens attach relative to the ovary?",
        "options": [
            "Beneath the ovary on the receptacle axis",
            "At the top of the ovary, appearing to emerge above the fruit",
            "Inside the locule directly attached to ovules",
            "Exclusively to the terminal stigma"
        ],
        "correctIndex": 1,
        "explanation": "In an epigynous flower with an inferior ovary, the ovary is deeply sunken into and fused with the receptacle or hypanthium. Consequently, the sepals, petals, and stamens insert above the summit of the ovary (seen in apples, squash, and blueberries).",
        "socraticHint": "Look at where the sepals and petals branch off relative to the swollen ovule-bearing chamber.",
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "citation": "BOT 121 Lecture: Floral Evolution (Fig. 9-28)"
    },
    {
        "id": "m2-q11",
        "station": "Station 11: Tree Annual Growth Rings",
        "question": "Examine this high-magnification micrograph of secondary xylem. What structural feature marks the boundary between two successive annual rings?",
        "options": [
            "A ring of living cork cambium separating xylem from phloem",
            "The abrupt transition between small, dense, thick-walled latewood cells and the expansive, large-diameter vessel lumens of earlywood",
            "A layer of dead epidermal cuticle",
            "Horizontal phloem sieve plates"
        ],
        "correctIndex": 1,
        "explanation": "The visible growth ring boundary is created when narrow, thick-walled latewood (summerwood) cells of the previous season abut the suddenly wide, thin-walled vessel elements of earlywood (springwood) produced when the cambium reactivates.",
        "socraticHint": "Compare the lumen diameter and wall thickness across the sharp line of transition.",
        "image": "images/bot-1121-secondary-growth/fig_8_17_growth_rings_early_late_wood.jpg",
        "citation": "BOT 121 Lecture: Dendrochronology & Wood (Fig. 8-17)"
    },
    {
        "id": "m2-q12",
        "station": "Station 12: Anther Microanatomy",
        "question": "In this transverse section of a mature lily anther, how many microsporangia (pollen sacs) are present, and what is the ploidy level of microsporocytes prior to meiosis?",
        "options": [
            "Four microsporangia; diploid (2n)",
            "Two microsporangia; haploid (1n)",
            "Six microsporangia; triploid (3n)",
            "Eight microsporangia; polyploid"
        ],
        "correctIndex": 0,
        "explanation": "A typical anther has two thecae containing four microsporangia (pollen sacs). The microsporocytes inside are diploid (2n) mother cells that undergo meiosis to produce four haploid (1n) microspores each.",
        "socraticHint": "Count the total lobes of the anther cross-section and recall the chromosome count before reductive division.",
        "image": "images/bot-1121-flowers/fig_9_10_anther_cross_section_pollen_sacs.jpg",
        "citation": "BOT 121 Lecture: Angiosperm Reproduction (Fig. 9-10)"
    }
]

# Append new quiz questions
existing_q_ids = {q["id"] for q in deck["quizzes"]}
added_quizzes_count = 0
for nq in new_visual_quizzes:
    if nq["id"] not in existing_q_ids:
        deck["quizzes"].append(nq)
        added_quizzes_count += 1

print(f"Added {added_quizzes_count} visual quiz stations.")
print(f"Total quizzes now: {len(deck['quizzes'])}")

# Save updated decks.json
portal_data["decks"][deck_idx] = deck
with open(decks_path, "w", encoding="utf-8") as f:
    json.dump(portal_data, f, indent=2)

print("Saved updated decks.json successfully!")
