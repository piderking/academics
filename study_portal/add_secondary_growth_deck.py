import json

secondary_growth_deck = {
    "id": "bot-1121-secondary-growth",
    "course": "BOT-1121",
    "title": "BOT-1121: Secondary Growth — Vascular & Cork Cambium",
    "description": "Atomic, photo-anchored flashcards drilling secondary growth: lateral meristems, vascular cambium (fusiform vs. ray initials, periclinal vs. anticlinal divisions), wood anatomy (secondary xylem, growth rings, sapwood vs. heartwood, tyloses), and bark/periderm (cork cambium, phellem, phelloderm, lenticels).",
    "source": "Botany: Structure of Woody Plants (Mauseth Ch. 8) & BOT 1121 Lab 4",
    "flashcards": [
        {
            "id": "sec-c1",
            "front": "What is the primary difference between **primary growth** and **secondary growth** in plants?",
            "hint": "Think about vertical elongation vs. lateral thickening.",
            "back": "• **Primary growth**: Increases stem and root **length** (produced by apical meristems).\n• **Secondary growth**: Increases stem and root **girth / diameter** (produced by lateral meristems).",
            "citation": "Mauseth Ch. 8, p. 536",
            "tags": ["growth", "meristems", "foundations"],
            "image": "images/bot-1121-secondary-growth/fig_8_11_wood_block_3d_planes.jpg",
            "imageCaption": "🔬 Plant Growth Planes (Click to zoom 🔍)",
            "imageDescription": "3D block diagram illustrating radial expansion and lateral thickness resulting from secondary growth."
        },
        {
            "id": "sec-c2",
            "front": "Which two **lateral meristems** are responsible for secondary growth in woody plants?",
            "hint": "One produces conducting vascular tissues; the other produces protective outer bark.",
            "back": "1. **Vascular Cambium**: Produces secondary xylem (wood) and secondary phloem.\n2. **Cork Cambium (Phellogen)**: Produces the periderm (outer bark).",
            "citation": "Mauseth Ch. 8, p. 541",
            "tags": ["meristems", "cambium", "lateral-growth"],
            "image": "images/bot-1121-secondary-growth/fig_8_20_cambial_zone_xylem_phloem.jpg",
            "imageCaption": "🔬 Lateral Meristem Overview (Click to zoom 🔍)",
            "imageDescription": "Transverse section showing the cylinder of vascular cambium situated between xylem and phloem, beneath the periderm."
        },
        {
            "id": "sec-c3",
            "front": "From which two specific regions does the **vascular cambium** originate to form a continuous ring?",
            "hint": "One part comes from inside the vascular bundles; the other from parenchyma between bundles.",
            "back": "1. **Fascicular cambium**: Residual procambium located *inside* the primary vascular bundles.\n2. **Interfascicular cambium**: Cortex/pith ray parenchyma *between* the bundles that resumes cell division.",
            "citation": "Mauseth Ch. 8, p. 542",
            "tags": ["vascular-cambium", "tissues", "origin"],
            "image": "images/bot-1121-secondary-growth/fig_8_3_fascicular_interfascicular_cambium.jpg",
            "imageCaption": "🔬 Cambium Ring Formation (Click to zoom 🔍)",
            "imageDescription": "Micrograph showing fascicular cambium inside vascular bundles linking with interfascicular cambium in the pith rays to form a continuous cylinder."
        },
        {
            "id": "sec-c4",
            "front": "What are the two distinct cell types found inside the **vascular cambium**?",
            "hint": "One is tall and vertically elongated; the other is small and cuboidal.",
            "back": "1. **Fusiform initials**: Tall, vertically elongated cells.\n2. **Ray initials**: Small, roughly cuboidal / isodiametric cells.",
            "citation": "Mauseth Ch. 8, p. 545",
            "tags": ["vascular-cambium", "cell-types", "histology"],
            "image": "images/bot-1121-secondary-growth/fig_8_4_fusiform_and_ray_initials.jpg",
            "imageCaption": "🔬 Cambium Cell Types in Tangential View (Click to zoom 🔍)",
            "imageDescription": "Tangential section of vascular cambium showing tall fusiform initials and clusters of small, rounded ray initials."
        },
        {
            "id": "sec-c5",
            "front": "What structural system do **fusiform initials** produce in secondary xylem and phloem?",
            "hint": "Think of the vertical up-and-down conduits of the plant stem.",
            "back": "The **Axial System (Vertical System)**:\n• **Secondary xylem**: Tracheids, vessel elements, wood fibers, axial parenchyma.\n• **Secondary phloem**: Sieve-tube elements, companion cells, phloem fibers.",
            "citation": "Mauseth Ch. 8, p. 546",
            "tags": ["axial-system", "fusiform-initials", "xylem-phloem"],
            "image": "images/bot-1121-secondary-growth/fig_8_5_cell_lineages_periclinal_divisions.jpg",
            "imageCaption": "🔬 Cambial Differentiation Lineage (Click to zoom 🔍)",
            "imageDescription": "Diagram demonstrating how fusiform initials divide to generate the vertically oriented axial conduits of wood and inner bark."
        },
        {
            "id": "sec-c6",
            "front": "What structural system do **ray initials** produce, and what is its primary role?",
            "hint": "Think of horizontal, spoke-like transport across the trunk.",
            "back": "The **Radial System (Xylem and Phloem Rays)**:\n• Composed of horizontal ray parenchyma cells.\n• **Role**: Transports water, minerals, and carbohydrates **radially (horizontally)** across the stem, and stores starch/nutrients.",
            "citation": "Mauseth Ch. 8, p. 550",
            "tags": ["ray-initials", "radial-system", "rays"],
            "image": "images/bot-1121-secondary-growth/fig_8_15_wood_xylem_rays.jpg",
            "imageCaption": "🔬 Radial Rays in Wood (Click to zoom 🔍)",
            "imageDescription": "Transverse and radial sections showing prominent multiseriate ray parenchyma traversing secondary xylem horizontally."
        },
        {
            "id": "sec-c7",
            "front": "What is a **periclinal division** in the vascular cambium, and what does it produce?",
            "hint": "The division plane is parallel to the outer surface of the stem.",
            "back": "A division plane **parallel** to the outer stem surface:\n• Produces **Secondary Xylem** toward the **inside** of the stem.\n• Produces **Secondary Phloem** toward the **outside** of the stem.",
            "citation": "Mauseth Ch. 8, p. 547",
            "tags": ["cell-division", "periclinal", "cambium"],
            "image": "images/bot-1121-secondary-growth/fig_8_5_cell_lineages_periclinal_divisions_1.jpg",
            "imageCaption": "🔬 Periclinal Division Orientation (Click to zoom 🔍)",
            "imageDescription": "Lineage diagram showing periclinal divisions generating inward xylem daughter cells and outward phloem daughter cells."
        },
        {
            "id": "sec-c8",
            "front": "What is an **anticlinal division** in the vascular cambium, and why is it necessary?",
            "hint": "The division plane is perpendicular to the stem surface.",
            "back": "A division plane **perpendicular** to the stem surface:\n• **Why necessary**: It adds new cambial initials to the ring so the vascular cambium can **expand its own circumference** as the tree grows thicker.",
            "citation": "Mauseth Ch. 8, p. 547",
            "tags": ["cell-division", "anticlinal", "girth"],
            "image": "images/bot-1121-secondary-growth/fig_8_5_cell_lineages_periclinal_divisions.jpg",
            "imageCaption": "🔬 Circumferential Expansion (Click to zoom 🔍)",
            "imageDescription": "Diagram showing anticlinal cell divisions increasing the total number of cambial initials to accommodate stem girth increase."
        },
        {
            "id": "sec-c9",
            "front": "Which botanical tissue constitutes what we commonly refer to as **\"wood\"**?",
            "hint": "Lignified water-conducting secondary tissue.",
            "back": "**Secondary Xylem**.\n• All wood accumulated inside tree trunks and branches consists of secondary xylem produced to the interior of the vascular cambium.",
            "citation": "Mauseth Ch. 8, p. 550",
            "tags": ["wood", "secondary-xylem", "anatomy"],
            "image": "images/bot-1121-secondary-growth/fig_8_11_wood_block_3d_planes.jpg",
            "imageCaption": "🔬 Wood Structural Architecture (Click to zoom 🔍)",
            "imageDescription": "Scanning electron micrograph of secondary xylem showing tracheary elements, fibers, and ray parenchyma forming wood."
        },
        {
            "id": "sec-c10",
            "front": "Why is there vastly more **secondary xylem** inside a tree trunk than **secondary phloem**?",
            "hint": "Compare what happens to tissues pushed toward the core versus toward the outside.",
            "back": "1. The cambium produces secondary xylem cells at a **much higher rate**.\n2. **Secondary xylem accumulates permanently** year after year.\n3. **Secondary phloem is pushed outward**, stretched, crushed, and sloughed off as bark.",
            "citation": "Mauseth Ch. 8, p. 571",
            "tags": ["secondary-xylem", "secondary-phloem", "accumulation"],
            "image": "images/bot-1121-secondary-growth/fig_8_20_cambial_zone_xylem_phloem.jpg",
            "imageCaption": "🔬 Xylem vs. Phloem Proportion (Click to zoom 🔍)",
            "imageDescription": "Stem cross-section showing huge buildup of internal secondary xylem compared to a thin layer of active secondary phloem."
        },
        {
            "id": "sec-c11",
            "front": "How do you distinguish **early wood (springwood)** from **late wood (summerwood)** under the microscope?",
            "hint": "Compare lumen diameter and cell wall thickness.",
            "back": "• **Early wood (Springwood)**: Wide lumen diameter, thinner walls (optimized for maximum water conduction during rapid spring growth).\n• **Late wood (Summerwood)**: Narrow lumen diameter, thicker walls (optimized for mechanical strength).",
            "citation": "Mauseth Ch. 8, p. 565",
            "tags": ["growth-rings", "early-wood", "late-wood"],
            "image": "images/bot-1121-secondary-growth/fig_8_17_growth_rings_early_late_wood.jpg",
            "imageCaption": "🔬 Growth Ring Micrograph (Click to zoom 🔍)",
            "imageDescription": "Micrograph displaying the abrupt transition from small, thick-walled late wood cells to large, wide-lumened early wood cells."
        },
        {
            "id": "sec-c12",
            "front": "What causes the sharp, visible boundary of an **annual growth ring**?",
            "hint": "It is an abrupt seasonal contrast between two successive cell types.",
            "back": "The **abrupt transition** between the small, dense, thick-walled cells of **late wood** (formed at the end of autumn) and the large, wide-lumened cells of **early wood** (formed the following spring).",
            "citation": "Mauseth Ch. 8, p. 565",
            "tags": ["annual-rings", "dendrochronology", "anatomy"],
            "image": "images/bot-1121-secondary-growth/fig_8_17_growth_rings_early_late_wood.jpg",
            "imageCaption": "🔬 Annual Ring Demarcation (Click to zoom 🔍)",
            "imageDescription": "High-magnification cross-section showing distinct growth rings separated by dense late-wood boundaries."
        },
        {
            "id": "sec-c13",
            "front": "What is the functional difference between **sapwood** and **heartwood**?",
            "hint": "One actively conducts sap/water; the other is dark, dead, and rot-resistant.",
            "back": "• **Sapwood (outer, lighter wood)**: Actively conducts water and dissolved minerals from roots to shoots.\n• **Heartwood (inner, darker wood)**: Older, non-conducting wood plugged with resins, tannins, and tyloses for structural support and decay resistance.",
            "citation": "Mauseth Ch. 8, p. 569",
            "tags": ["sapwood", "heartwood", "xylem"],
            "image": "images/bot-1121-secondary-growth/fig_8_18_heartwood_vs_sapwood.jpg",
            "imageCaption": "🔬 Trunk Cross-Section (Click to zoom 🔍)",
            "imageDescription": "Oak trunk cross-section showing pale, water-conducting sapwood surrounding a dark, aromatic heartwood core."
        },
        {
            "id": "sec-c14",
            "front": "What are **tyloses**, and what is their role in heartwood formation?",
            "hint": "Balloon-like outgrowths that plug vessel lumens.",
            "back": "**Balloon-like outgrowths** from adjacent parenchyma cells that push through pits into vessel element lumens, permanently sealing them off to prevent pathogen spread and water leakage in non-functional heartwood.",
            "citation": "Mauseth Ch. 8, p. 571",
            "tags": ["tyloses", "vessels", "heartwood"],
            "image": "images/bot-1121-secondary-growth/fig_8_12_vessel_elements_secondary_xylem.jpg",
            "imageCaption": "🔬 Vessel Lumen Structure (Click to zoom 🔍)",
            "imageDescription": "Micrograph illustrating vessel lumens invaded by surrounding parenchyma protoplasts forming tyloses."
        },
        {
            "id": "sec-c15",
            "front": "Why must a woody plant form a **cork cambium** once secondary growth begins?",
            "hint": "What happens to the primary epidermis as the stem expands?",
            "back": "As secondary xylem expands the stem girth, the original **epidermis stretches, tears, and dies**. The **cork cambium** arises to produce a new, waterproof protective outer layer (**periderm**).",
            "citation": "Mauseth Ch. 8, p. 575",
            "tags": ["cork-cambium", "periderm", "epidermis"],
            "image": "images/bot-1121-secondary-growth/fig_8_23_cork_cambium_phellogen_origin.jpg",
            "imageCaption": "🔬 Epidermal Rupture & Cambium Origin (Click to zoom 🔍)",
            "imageDescription": "Stem cross-section showing subepidermal cortex parenchyma cells dedifferentiating into the first cork cambium."
        },
        {
            "id": "sec-c16",
            "front": "What is the formal botanical name for the **cork cambium**, and where does it originate?",
            "hint": "Starts with 'phello-'. Originates in outer cortex cells.",
            "back": "**Phellogen**.\n• Originates from subepidermal **cortex parenchyma cells** (or later, from parenchyma in older secondary phloem).",
            "citation": "Mauseth Ch. 8, p. 575",
            "tags": ["phellogen", "cork-cambium", "cortex"],
            "image": "images/bot-1121-secondary-growth/fig_8_23_cork_cambium_phellogen_origin.jpg",
            "imageCaption": "🔬 Phellogen Cell Layer (Click to zoom 🔍)",
            "imageDescription": "Micrograph of the subepidermal layer showing the single-cell-thick band of dividing phellogen cells."
        },
        {
            "id": "sec-c17",
            "front": "What two tissues does the cork cambium (phellogen) produce, and in which directions?",
            "hint": "One layer faces outward (cork); the other faces inward.",
            "back": "• **Outward**: **Phellem (Cork cells)** — dead at maturity, walls impregnated with waterproof suberin.\n• **Inward**: **Phelloderm** — living parenchyma cells.",
            "citation": "Mauseth Ch. 8, p. 576",
            "tags": ["phellem", "phelloderm", "periderm"],
            "image": "images/bot-1121-secondary-growth/fig_8_24_periderm_cork_phelloderm.jpg",
            "imageCaption": "🔬 Periderm Stratification (Click to zoom 🔍)",
            "imageDescription": "Cross-section showing outer phellem (cork), middle phellogen (cork cambium), and inner phelloderm layers."
        },
        {
            "id": "sec-c18",
            "front": "What three tissue layers make up the **periderm**?",
            "hint": "Phellem + Phellogen + Phelloderm.",
            "back": "**Periderm = Phellem (Cork) + Phellogen (Cork Cambium) + Phelloderm**.\n• The periderm is the protective secondary dermal tissue system replacing the epidermis.",
            "citation": "Mauseth Ch. 8, p. 576",
            "tags": ["periderm", "cork", "anatomy"],
            "image": "images/bot-1121-secondary-growth/fig_8_24_periderm_cork_phelloderm.jpg",
            "imageCaption": "🔬 The Three Periderm Layers (Click to zoom 🔍)",
            "imageDescription": "Micrograph showing the periderm boundary consisting of radially arranged cork cells, meristematic phellogen, and phelloderm."
        },
        {
            "id": "sec-c19",
            "front": "What hydrophobic chemical polymer waterproofs **cork (phellem)** cell walls?",
            "hint": "The same waxy substance found in the Casparian strip of roots.",
            "back": "**Suberin**.\n• Suberin is a waxy lipid polymer deposited in cork secondary walls, making them impermeable to water, gases, and pathogens.",
            "citation": "Mauseth Ch. 8, p. 576",
            "tags": ["suberin", "cork", "chemistry"],
            "image": "images/bot-1121-secondary-growth/fig_8_24_periderm_cork_phelloderm.jpg",
            "imageCaption": "🔬 Suberized Cork Cell Walls (Click to zoom 🔍)",
            "imageDescription": "Micrograph detail of dense, compact cork cells exhibiting dark, suberin-impregnated cell walls."
        },
        {
            "id": "sec-c20",
            "front": "What anatomical structure defines the boundary line between **bark** and **wood**?",
            "hint": "The lateral meristem that creates both.",
            "back": "The **Vascular Cambium**.\n• **Wood**: All tissues **interior** to the vascular cambium (secondary xylem).\n• **Bark**: All tissues **exterior** to the vascular cambium (secondary phloem + periderms).",
            "citation": "Mauseth Ch. 8, p. 572",
            "tags": ["bark", "wood", "vascular-cambium"],
            "image": "images/bot-1121-secondary-growth/fig_8_20_cambial_zone_xylem_phloem.jpg",
            "imageCaption": "🔬 Bark vs. Wood Boundary (Click to zoom 🔍)",
            "imageDescription": "Stem cross-section highlighting the precise interface where vascular cambium separates wood (inside) from bark (outside)."
        },
        {
            "id": "sec-c21",
            "front": "What is the difference between **inner bark** and **outer bark (rhytidome)**?",
            "hint": "Think about functional living phloem vs. dead cracked outer layers.",
            "back": "• **Inner Bark**: Living secondary phloem between the vascular cambium and the innermost functional cork cambium.\n• **Outer Bark (Rhytidome)**: All dead tissues outside the innermost cork cambium (old crushed phloem, cortex, and dead cork layers).",
            "citation": "Mauseth Ch. 8, p. 577",
            "tags": ["inner-bark", "outer-bark", "rhytidome"],
            "image": "images/bot-1121-secondary-growth/fig_8_25_bark_and_lenticels.jpg",
            "imageCaption": "🔬 Bark Layers & Rhytidome (Click to zoom 🔍)",
            "imageDescription": "Trunk section demonstrating shedding, cracking outer bark (rhytidome) separated from living inner bark."
        },
        {
            "id": "sec-c22",
            "front": "What are **lenticels**, and why are they necessary in woody stems?",
            "hint": "Pores or raised blisters visible on twigs.",
            "back": "**Lenticels** are raised pores in the periderm packed with loosely arranged, non-suberized cells.\n• **Why necessary**: Because suberized cork is airtight, lenticels allow **gas exchange ($O_2$ and $CO_2$)** between living stem tissues and the outside air.",
            "citation": "Mauseth Ch. 8, p. 578",
            "tags": ["lenticels", "gas-exchange", "periderm"],
            "image": "images/bot-1121-secondary-growth/fig_8_25_bark_and_lenticels.jpg",
            "imageCaption": "🔬 Lenticel Aeration Pore (Click to zoom 🔍)",
            "imageDescription": "Micrograph of a lenticel showing loosely organized, non-suberized complementary cells providing a channel for gas diffusion."
        }
    ],
    "quizzes": [
        {
            "id": "sec-q1",
            "station": "Station 1: Lateral Meristem Derivatives",
            "question": "A periclinal division in a fusiform initial of the vascular cambium produces a daughter cell toward the interior of the stem. What tissue will this cell differentiate into?",
            "options": [
                "Secondary phloem",
                "Secondary xylem (wood)",
                "Phelloderm",
                "Cortex parenchyma",
                "Phellem (cork)"
            ],
            "correctIndex": 1,
            "socraticHint": "Remember the spatial rule: xylem is always internal to the cambium; phloem is always external.",
            "explanation": "The vascular cambium divides periclinally to produce secondary xylem toward the inside of the stem and secondary phloem toward the outside. A daughter cell cut off toward the interior matures into secondary xylem (wood)."
        },
        {
            "id": "sec-q2",
            "station": "Station 2: Cambial Initials",
            "question": "Which component of the secondary vascular system is produced directly by ray initials rather than fusiform initials?",
            "options": [
                "Tracheids",
                "Vessel elements",
                "Xylem and phloem rays",
                "Phloem fibers",
                "Sieve-tube elements"
            ],
            "correctIndex": 2,
            "socraticHint": "Ray initials are cuboidal cells that produce the radial (horizontal) transport system.",
            "explanation": "Ray initials divide to produce the horizontal radial system—specifically xylem rays and phloem rays. Fusiform initials produce the vertical axial system (vessels, tracheids, fibers, sieve tubes)."
        },
        {
            "id": "sec-q3",
            "station": "Station 3: Growth Ring Identification",
            "question": "Examining a cross-section of a pine trunk under 100x magnification, you observe an abrupt boundary where large, thin-walled tracheids abruptly sit adjacent to small, thick-walled, compressed tracheids. What does this boundary represent?",
            "options": [
                "The boundary between sapwood and heartwood.",
                "An annual growth ring boundary between late wood of one year and early wood of the next.",
                "The interface between secondary xylem and vascular cambium.",
                "A false ring caused by a fungal infection.",
                "The transition from primary xylem to secondary xylem."
            ],
            "correctIndex": 1,
            "socraticHint": "Early spring growth produces wide lumens; late summer growth produces dense, thick walls.",
            "explanation": "An annual growth ring boundary is formed by the sharp contrast between the dense, small, thick-walled cells of late wood (summerwood) and the large, wide-lumened cells of early wood (springwood) produced the following spring."
        },
        {
            "id": "sec-q4",
            "station": "Station 4: Periderm Organization",
            "question": "What is the correct sequence of periderm layers from the OUTSIDE of the tree moving INWARD?",
            "options": [
                "Phelloderm → Phellogen → Phellem",
                "Phellem (Cork) → Phellogen (Cork Cambium) → Phelloderm",
                "Phellogen → Phellem → Phelloderm",
                "Phellem → Phelloderm → Phellogen",
                "Vascular Cambium → Phellogen → Cork"
            ],
            "correctIndex": 1,
            "socraticHint": "Cork is on the outside protecting the stem; phellogen is in the middle; phelloderm is on the inside.",
            "explanation": "The periderm consists of: 1) Phellem (cork cells) on the outermost surface, 2) Phellogen (cork cambium) in the middle, and 3) Phelloderm on the innermost side."
        },
        {
            "id": "sec-q5",
            "station": "Station 5: Wood Physiology & Heartwood",
            "question": "Why does a tree continue to survive and conduct water normally even if fungi completely rot away the dark heartwood inside its trunk?",
            "options": [
                "Heartwood only conducts food, not water.",
                "Water conduction occurs exclusively in the outer sapwood; heartwood is non-functional for transport.",
                "The cork cambium takes over water conduction.",
                "Tyloses in the heartwood produce new water channels.",
                "Heartwood turns into secondary phloem."
            ],
            "correctIndex": 1,
            "socraticHint": "Which zone of wood is actively conducting sap, and which zone is plugged and dead?",
            "explanation": "Only the younger, outermost secondary xylem (sapwood) actively conducts water and dissolved minerals. Heartwood is older, non-conducting wood plugged with tyloses, resins, and tannins. Therefore, a hollow tree with rotted heartwood can continue living and transporting water via its sapwood."
        },
        {
            "id": "sec-q6",
            "station": "Station 6: Bark Anatomy & Girdling",
            "question": "If a forestry worker 'girdles' a tree by cutting away a complete strip of bark down to the wood, why does the tree eventually die?",
            "options": [
                "Water cannot reach the leaves because secondary xylem was removed.",
                "Photosynthetic sugars produced in the leaves cannot reach the roots because secondary phloem was severed.",
                "The tree loses all its suberin.",
                "The apical meristems stop dividing.",
                "Lenticels can no longer perform photosynthesis."
            ],
            "correctIndex": 1,
            "socraticHint": "Remember that bark includes all tissues outside the vascular cambium, including inner bark.",
            "explanation": "Bark includes the secondary phloem (inner bark). When a tree is girdled around its entire circumference, the pathway for transporting carbohydrates from leaves down to the roots is completely severed. The roots starve and die, followed by the entire tree."
        }
    ]
}

def update_decks():
    deck_file = "G:/My Drive/Academics/study_portal/decks.json"
    with open(deck_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Filter out existing if any
    existing = [d for d in data.get("decks", []) if d.get("id") != "bot-1121-secondary-growth"]
    
    # Place secondary growth deck right after bot-1121-week-4
    final_decks = []
    inserted = False
    for d in existing:
        final_decks.append(d)
        if d.get("id") == "bot-1121-week-4":
            final_decks.append(secondary_growth_deck)
            inserted = True
    if not inserted:
        final_decks.insert(0, secondary_growth_deck)

    data["decks"] = final_decks

    with open(deck_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Updated decks.json successfully with bot-1121-secondary-growth!")
    print(f"Total decks: {len(final_decks)}")
    for d in final_decks:
        print(f"  - {d['id']}: {d['title']} ({len(d.get('flashcards', []))} cards, {len(d.get('quizzes', []))} quizzes)")

if __name__ == "__main__":
    update_decks()
