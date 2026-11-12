import json
import os

# Define the 45 simplified flashcards grounded directly in Sean Ryan's lecture slides
simplified_cards = [
    # ==========================================
    # LECTURE 10: Ferns & Herbarium Studies (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c01",
        "front": "What are the main parts of a fern plant (sporophyte)?",
        "hint": "Think of the leaf, the leaflets, the stalk, the central axis, and the underground stem.",
        "back": "The main parts of a fern plant:\n\n• **Frond**: The entire fern leaf.\n• **Blade**: The leafy, expanded part of the frond.\n• **Pinna**: An individual leaflet of the blade (plural: *pinnae*).\n• **Rachis**: The central axis / stem running through the leafy blade.\n• **Stipe**: The stem-like stalk below the blade connecting it to the rhizome.\n• **Rhizome**: The horizontal underground stem that produces roots and new fronds.\n• **Fiddlehead (Crozier)**: A young coiled frond that unrolls as it grows (*circinate vernation*).",
        "image": "images/diagrams/fern_structure.svg",
        "imageDescription": "Diagram of fern anatomy showing the frond, blade, pinna, rachis, stipe, rhizome, and developing fiddlehead.",
        "citation": "BOT 1121 Lec 10, Slide 43-44",
        "tags": ["ferns", "anatomy", "frond", "rhizome", "fiddlehead"]
    },
    {
        "id": "bot-1121-m2-c02",
        "front": "On a fern gametophyte, what are an antheridium and an archegonium?",
        "hint": "One makes male gametes (sperm) and the other makes the female gamete (egg).",
        "back": "On the tiny, heart-shaped fern gametophyte (prothallus):\n\n• **Antheridium**: The male reproductive organ that produces many swimming **sperm**.\n• **Archegonium**: The female reproductive organ that produces a single **egg**.\n• **Fertilization**: Fern sperm have flagella and require an external film of **liquid water** to swim to the archegonium and fertilize the egg!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p32_2.jpeg",
        "imageDescription": "Fern gametophyte (prothallus) slide showing archegonia near the notch and antheridia near the rhizoids.",
        "citation": "BOT 1121 Lec 10, Slide 32 & 39",
        "tags": ["ferns", "gametophyte", "antheridium", "archegonium", "reproduction"]
    },
    {
        "id": "bot-1121-m2-c03",
        "front": "What is a sorus and what is a sporangium on a fern?",
        "hint": "Look at the brown clusters on the underside of a fern frond.",
        "back": "• **Sporangium**: A tiny capsule or sac that produces spores via meiosis.\n• **Sorus** (plural: **sori**): A cluster of many sporangia on the underside of a fern frond.\n• **Indusium**: A small protective flap of tissue covering the sorus in many fern species.\n• **Ploidy**: The frond and sorus belong to the **diploid sporophyte (2n)** generation.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "Cross section of a fern sorus showing stalked sporangia clustered under a protective indusium.",
        "citation": "BOT 1121 Lec 10, Slide 31 & 36",
        "tags": ["ferns", "sorus", "sporangium", "indusium", "spores"]
    },
    {
        "id": "bot-1121-m2-c04",
        "front": "What is the annulus on a fern sporangium, and what does it do?",
        "hint": "A ring of thickened cells that acts like a tiny catapult.",
        "back": "• **What it is**: The **annulus** is a curved ridge or ring of thickened cells running along the outer rim of the sporangium.\n• **What it does**: It acts like a **catapult**! As water evaporates from these cells, surface tension pulls them back; when the tension suddenly snaps, the sporangium flings haploid spores into the air to be dispersed by the wind.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "Close-up of a fern sporangium showing the prominent crest of thickened annulus cells.",
        "citation": "BOT 1121 Lec 10, Slide 31",
        "tags": ["ferns", "annulus", "sporangium", "spore dispersal"]
    },
    {
        "id": "bot-1121-m2-c05",
        "front": "What is an herbarium, and what essential info must be on an herbarium label?",
        "hint": "Think of a botanical library of dried, pressed plants (like Cal Poly's Hoover Herbarium).",
        "back": "• **Herbarium**: A scientific library or museum collection of dried, pressed, and mounted plant specimens used for research.\n• **Required on an Herbarium Label**:\n  1. **Plant Scientific Name** & Author (e.g., *Eschscholzia rhombipetala*)\n  2. **Location**: Precise geographic locality, county, state, GPS coordinates, elevation\n  3. **Habitat**: Surrounding plant community, soil, slope, aspect\n  4. **Date**: When the specimen was collected\n  5. **Collector**: Name of the collector and their unique collection number",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p5_0.jpeg",
        "imageDescription": "Herbarium sheet from Cal Poly Hoover Herbarium showing pressed plant and standard metadata label.",
        "citation": "BOT 1121 Lec 10, Slide 4-6",
        "tags": ["herbarium", "voucher label", "taxonomy", "collecting"]
    },

    # ==========================================
    # LECTURE 11: Gymnosperms (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c06",
        "front": "What does 'gymnosperm' mean, and how do their seeds differ from angiosperms?",
        "hint": "Gymno = naked, sperm = seed.",
        "back": "• **Meaning**: Gymnosperm literally means **\"naked seed\"**.\n• **Key Difference**:\n  - **Gymnosperms**: Seeds are \"naked\"—they sit exposed on cone scales (not inside an ovary or fruit).\n  - **Angiosperms**: Seeds develop enclosed inside an ovary that ripens into a fruit.\n• **Nutrition**: In gymnosperms, food stored for the embryo comes from the haploid (1n) female gametophyte (unlike the 3n endosperm of angiosperms).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p6_0.jpeg",
        "imageDescription": "Diagram comparing gymnosperm naked seeds on cone scales vs angiosperm seeds inside fruit.",
        "citation": "BOT 1121 Lec 11, Slide 5-7",
        "tags": ["gymnosperms", "naked seed", "cones", "ovary"]
    },
    {
        "id": "bot-1121-m2-c07",
        "front": "What are the four living groups of gymnosperms?",
        "hint": "Conifers are the biggest group; name the other three living divisions.",
        "back": "The four living groups of gymnosperms:\n\n1. **Conifers (Pinophyta)**: Pines, redwoods, firs, spruces, cedars (most abundant group).\n2. **Cycads**: Palm-like plants with large cones; mostly tropical and subtropical.\n3. **Ginkgo**: Only one living species (*Ginkgo biloba*).\n4. **Gnetophytes**: Bizarre plants with vessel elements, including *Ephedra* (Mormon tea) and *Welwitschia*.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p3_0.jpeg",
        "imageDescription": "Phylogeny showing the four gymnosperm lineages: Conifers, Cycads, Ginkgo, and Gnetophytes.",
        "citation": "BOT 1121 Lec 11, Slide 3 & 5",
        "tags": ["gymnosperms", "conifers", "cycads", "ginkgo", "gnetophytes"]
    },
    {
        "id": "bot-1121-m2-c08",
        "front": "What does dioecious mean, and which gymnosperms are dioecious?",
        "hint": "Dioecious means 'two houses' — separate male and female trees.",
        "back": "• **Dioecious**: Male and female reproductive structures are on **separate individual plants** (you have male trees and female trees).\n• **Examples**:\n  - ***Ginkgo biloba***: Male trees produce pollen cones; female trees produce smelly seeds.\n  - **Cycads**: Separate male cone-bearing and female cone-bearing plants.\n• *(In contrast, **monoecious** plants like pines have male cones and female cones on the same tree).* ",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p4_0.jpeg",
        "imageDescription": "Diagram showing separate male pollen cones and female seed cones.",
        "citation": "BOT 1121 Lec 11, Slide 17 & 27",
        "tags": ["gymnosperms", "dioecious", "monoecious", "reproduction"]
    },
    {
        "id": "bot-1121-m2-c09",
        "front": "What are the unique traits of Ginkgo biloba (Maidenhair tree)?",
        "hint": "Living fossil, fan-shaped leaves, smelly female seeds.",
        "back": "Key characteristics of ***Ginkgo biloba***:\n\n• **Living Fossil**: Only surviving species in its entire phylum (native to Asia).\n• **Leaves**: Unique fan-shaped, two-lobed leaves with dichotomously branching veins.\n• **Dioecious**: Separate male and female trees.\n• **Smelly Seeds**: The outer fleshy seed coat produces **butyric acid** when ripe, giving off an odor of rancid butter or vomit!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p15_0.jpeg",
        "imageDescription": "Fan-shaped leaves of Ginkgo biloba displaying dichotomous parallel venation.",
        "citation": "BOT 1121 Lec 11, Slide 14-17",
        "tags": ["ginkgo", "living fossil", "fan leaves", "butyric acid"]
    },
    {
        "id": "bot-1121-m2-c10",
        "front": "What adaptations do conifer needles have for cold winters and drought?",
        "hint": "Think about needle shape, waxy coat, stomata position, and sap/resin.",
        "back": "Conifer needle adaptations to conserve water and survive extreme cold:\n\n• **Needle Shape**: Small surface area reduces water loss and easily sheds heavy snow.\n• **Thick Waxy Cuticle**: Waterproof outer coating prevents drying out.\n• **Sunken Stomata**: Stomatal pores are tucked into recessed pits to protect against drying winds.\n• **Resin Ducts**: Produce sticky resin that deters insects, seals wounds, and resists freezing.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p35_0.jpeg",
        "imageDescription": "Cross section of a pine needle showing thick cuticle, sunken stomata, and resin canals.",
        "citation": "BOT 1121 Lec 11, Slide 26 & 35",
        "tags": ["conifers", "needles", "adaptations", "cuticle", "resin ducts"]
    },

    # ==========================================
    # LECTURE 12: Angiosperms I - Flowers (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c11",
        "front": "What are the four whorls of a flower from outermost to innermost?",
        "hint": "Sepals, petals, male organs, female organs.",
        "back": "The 4 concentric whorls of a flower:\n\n1. **Calyx (Sepals)**: Outermost whorl; green and leaf-like; protects flower bud before opening.\n2. **Corolla (Petals)**: Second whorl; often brightly colored to attract pollinators.\n3. **Stamens (Androecium)**: Third whorl; male reproductive organs that produce pollen.\n4. **Carpels / Pistil (Gynoecium)**: Innermost whorl; female organ containing ovules that develop into seeds.",
        "image": "images/diagrams/flower_structure.svg",
        "imageDescription": "Diagram of a complete flower detailing the four concentric whorls: calyx, corolla, androecium, and gynoecium.",
        "citation": "BOT 1121 Lec 12, Slide 10",
        "tags": ["flowers", "whorls", "calyx", "corolla", "stamen", "carpel"]
    },
    {
        "id": "bot-1121-m2-c12",
        "front": "What are the parts of a stamen (male) and a carpel (female)?",
        "hint": "Stamen = pollen sac + stalk. Carpel = sticky top + neck + swollen base.",
        "back": "• **Stamen (Male Organ)**:\n  - **Anther**: Top sac where pollen grains are produced.\n  - **Filament**: Slender stalk holding up the anther.\n\n• **Carpel / Pistil (Female Organ)**:\n  - **Stigma**: Sticky top surface that captures pollen.\n  - **Style**: Long neck or tube connecting stigma to ovary.\n  - **Ovary**: Swollen base containing **ovules** (ovules become seeds; the ovary becomes fruit).",
        "image": "images/diagrams/flower_structure.svg",
        "imageDescription": "Anatomy of the stamen (anther, filament) and carpel (stigma, style, ovary with ovules).",
        "citation": "BOT 1121 Lec 12, Slide 10 & 20-22",
        "tags": ["stamen", "anther", "filament", "carpel", "stigma", "style", "ovary"]
    },
    {
        "id": "bot-1121-m2-c13",
        "front": "What is the difference between Complete vs Incomplete, and Perfect vs Imperfect flowers?",
        "hint": "Complete is about whorls; Perfect is about sex organs (stamens & carpels).",
        "back": "• **Complete Flower**: Has all **4 whorls** (sepals, petals, stamens, and carpels).\n• **Incomplete Flower**: Missing **one or more** of the 4 whorls (e.g., lacks petals).\n\n• **Perfect Flower**: Has **both** male (stamens) and female (carpels) parts (bisexual).\n• **Imperfect Flower**: Has only **one sex**:\n  - *Staminate*: Has stamens only (male flower).\n  - *Pistillate*: Has carpels/pistil only (female flower).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p16_0.jpeg",
        "imageDescription": "Comparison chart illustrating complete vs incomplete and perfect vs imperfect flowers.",
        "citation": "BOT 1121 Lec 12, Slide 16",
        "tags": ["flowers", "complete", "incomplete", "perfect", "imperfect"]
    },
    {
        "id": "bot-1121-m2-c14",
        "front": "In flowers, what is the difference between connation and adnation?",
        "hint": "Fusing like parts together vs fusing unlike parts together.",
        "back": "• **Connation**: The fusion of **like parts** together.\n  - *Example*: Petals fused together to form a tube, or sepals fused together.\n\n• **Adnation**: The fusion of **unlike parts** together.\n  - *Example*: Stamens fused directly onto the inside of the petal tube.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p12_1.jpeg",
        "imageDescription": "Diagram contrasting connation (like organs fused) and adnation (unlike organs fused).",
        "citation": "BOT 1121 Lec 12, Slide 12",
        "tags": ["flowers", "connation", "adnation", "fusion"]
    },
    {
        "id": "bot-1121-m2-c15",
        "front": "What is the difference between a superior ovary and an inferior ovary?",
        "hint": "Look at where the petals, sepals, and stamens attach relative to the ovary.",
        "back": "• **Superior Ovary (Hypogynous flower)**:\n  - The ovary sits **above** the attachment point of the sepals, petals, and stamens.\n  - The ovary is free and visible above the floral parts.\n\n• **Inferior Ovary (Epigynous flower)**:\n  - The ovary sits **below** the attachment point of the sepals, petals, and stamens.\n  - The ovary is embedded down inside the receptacle/floral cup (like in apples and squash).",
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Botanical comparison showing hypogynous flower with superior ovary vs epigynous flower with inferior ovary.",
        "citation": "BOT 1121 Lec 12, Slide 28",
        "tags": ["flowers", "superior ovary", "inferior ovary", "hypogynous", "epigynous"]
    },

    # ==========================================
    # LECTURE 13: Angiosperms II - Fruits and Seeds (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c16",
        "front": "What is a fruit, and what are the three layers of the pericarp (fruit wall)?",
        "hint": "A fruit is a mature ripened ovary. Think skin, flesh, and inner pit layer.",
        "back": "• **Fruit**: A mature, ripened **ovary** that protects the seeds and helps with seed dispersal.\n• **Pericarp** (the fruit wall) is divided into 3 layers:\n  1. **Exocarp**: The outer skin or rind.\n  2. **Mesocarp**: The fleshy middle tissue (the part we usually eat).\n  3. **Endocarp**: The innermost layer surrounding the seed (can be thin, fleshy, or a hard stony pit).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p2_0.jpeg",
        "imageDescription": "Diagram of fruit pericarp layers showing exocarp, mesocarp, and endocarp around the seed.",
        "citation": "BOT 1121 Lec 13, Slide 2-3",
        "tags": ["fruit", "pericarp", "exocarp", "mesocarp", "endocarp"]
    },
    {
        "id": "bot-1121-m2-c17",
        "front": "What is a drupe, a berry, and a pome? (Give examples of each)",
        "hint": "Stone pit vs all soft flesh vs apple core.",
        "back": "• **Drupe (\"Stone Fruit\")**:\n  - Fleshy fruit with a hard, stony **endocarp (pit)** enclosing a single seed.\n  - *Examples*: Peach, cherry, plum, olive, avocado.\n• **Berry**:\n  - Entire pericarp is soft and fleshy throughout, usually with multiple seeds; no stony pit.\n  - *Examples*: Tomato, grape, blueberry, pepper, banana.\n• **Pome**:\n  - Fruit where the fleshy edible part comes from the swollen receptacle/hypanthium around an inferior ovary; papery endocarp \"core\".\n  - *Examples*: Apple, pear.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p5_0.jpeg",
        "imageDescription": "Comparison of fleshy fruit types: drupe (peach), berry (tomato), and pome (apple).",
        "citation": "BOT 1121 Lec 13, Slide 4-8",
        "tags": ["fruit", "drupe", "berry", "pome", "classification"]
    },
    {
        "id": "bot-1121-m2-c18",
        "front": "What is the difference between an aggregate fruit and a multiple fruit?",
        "hint": "One flower with many ovaries vs many separate flowers fused together.",
        "back": "• **Aggregate Fruit**:\n  - Develops from a **single flower** that has **many separate carpels (ovaries)**.\n  - Each carpel develops into a tiny fruitlet on one receptacle.\n  - *Examples*: Blackberry, raspberry, strawberry.\n\n• **Multiple Fruit**:\n  - Develops from an **entire inflorescence (cluster of many separate flowers)** that fuse together as they mature.\n  - *Examples*: Pineapple, fig, mulberry.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p13_2.jpeg",
        "imageDescription": "Morphology of aggregate fruits (single flower, many carpels) vs multiple fruits (many flowers fused).",
        "citation": "BOT 1121 Lec 13, Slide 13",
        "tags": ["fruit", "aggregate", "multiple", "inflorescence", "receptacle"]
    },
    {
        "id": "bot-1121-m2-c19",
        "front": "Why is a strawberry classified as an 'accessory aggregate fruit'?",
        "hint": "What is the red part you eat, and what are the tiny 'seeds' on the surface?",
        "back": "In a strawberry:\n\n• **Red Fleshy Part**: Is NOT the ovary! It is the enlarged, swollen **receptacle** (an *accessory* organ).\n• **Tiny \"Seeds\" on Surface**: Are actually the true botanical fruits! They are tiny individual dry fruits called **achenes**, each containing a single seed.\n• Because it comes from one flower with many carpels and edible non-ovary tissue, it is called an **accessory aggregate fruit**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p15_0.jpeg",
        "imageDescription": "Close-up of strawberry anatomy highlighting swollen receptacle and surface achenes.",
        "citation": "BOT 1121 Lec 13, Slide 15",
        "tags": ["fruit", "strawberry", "accessory fruit", "achene", "receptacle"]
    },
    {
        "id": "bot-1121-m2-c20",
        "front": "What are the three main parts of an angiosperm seed?",
        "hint": "The protective coat, the baby plant, and the food storage tissue.",
        "back": "An angiosperm seed consists of:\n\n1. **Seed Coat (Testa)**: Tough protective outer layer developed from the integuments of the ovule.\n2. **Embryo**: The young baby plant consisting of cotyledon(s) (seed leaves), epicotyl (future shoot), and radicle (embryonic root).\n3. **Endosperm**: Nutritive tissue formed by double fertilization (triploid, 3n) that feeds the embryo during germination.",
        "image": "images/diagrams/seed_structure.svg",
        "imageDescription": "Diagram of an angiosperm seed showing seed coat, embryo (cotyledon, radicle), and endosperm.",
        "citation": "BOT 1121 Lec 13, Slide 25",
        "tags": ["seeds", "seed coat", "embryo", "endosperm", "cotyledon"]
    },

    # ==========================================
    # LECTURE 14: Fig Biology (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c21",
        "front": "In fig biology, what is a syconium and what is the ostiole?",
        "hint": "A fig is an inside-out flower cluster with a small entrance hole.",
        "back": "• **Syconium**: The hollow, fleshy, flask-shaped structure of a fig. It is an **inverted inflorescence** with hundreds of tiny individual flowers lining the inside wall!\n• **Ostiole**: The small opening or pore at the tip of the syconium, covered by tight scales, through which the fig wasp enters.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p10_0.jpeg",
        "imageDescription": "Longitudinal section of a fig syconium showing internal flowers and the apical ostiole pore.",
        "citation": "BOT 1121 Lec 14, Slide 10-12",
        "tags": ["fig", "syconium", "ostiole", "inflorescence"]
    },
    {
        "id": "bot-1121-m2-c22",
        "front": "How do fig wasps and figs help each other (obligate mutualism)?",
        "hint": "The wasp gets a nursery for its young; the fig gets pollinated.",
        "back": "Fig wasps and figs share an **obligate mutualism** (neither can reproduce without the other):\n\n• **For the Fig**: The female wasp carries pollen on her body from her birth fig and pollinates the flowers inside the new syconium, enabling seed production.\n• **For the Wasp**: The fig provides a safe nursery. The wasp lays eggs in some flower ovaries, which form galls that nourish the wasp larvae until adulthood.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p18_0.jpeg",
        "imageDescription": "Diagram illustrating the mutualistic life cycle of the fig wasp (Blastophaga psenes) and fig tree.",
        "citation": "BOT 1121 Lec 14, Slide 18-19",
        "tags": ["fig", "fig wasp", "mutualism", "pollination", "symbiosis"]
    },
    {
        "id": "bot-1121-m2-c23",
        "front": "What is the difference between a caprifig and an edible fig?",
        "hint": "Male tree where wasps breed vs female tree that makes seeds/fruit.",
        "back": "• **Caprifig (Male tree)**:\n  - Produces male flowers with pollen and **short-styled** female flowers.\n  - The wasp's ovipositor easily reaches the ovary to lay eggs (wasp nursery; inedible to humans).\n\n• **Edible Fig (Female tree)**:\n  - Produces only **long-styled** female flowers.\n  - The style is longer than the wasp's ovipositor, so she cannot lay eggs! Instead, she only deposits pollen, fertilizing the flowers to produce seeds and delicious edible figs.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p26_0.jpeg",
        "imageDescription": "Comparison of short-styled flowers in male caprifigs vs long-styled flowers in female edible figs.",
        "citation": "BOT 1121 Lec 14, Slide 24-26",
        "tags": ["fig", "caprifig", "edible fig", "short style", "long style"]
    },
    {
        "id": "bot-1121-m2-c24",
        "front": "What are the roles of male and female fig wasps inside the syconium?",
        "hint": "Males never leave the fig; females collect pollen and fly away.",
        "back": "Inside the syconium:\n\n• **Male Wasps**: Wingless and blind. They hatch first, find galls containing females, mate with them, chew escape holes through the fig wall, and die without ever leaving the fig.\n• **Female Wasps**: Winged. After mating, they gather pollen from male flowers inside the fig, crawl out through the escape hole, and fly to search for a new syconium to lay eggs and pollinate.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p20_0.jpeg",
        "imageDescription": "Photomicrograph of wingless male fig wasps chewing exit holes and winged female fig wasps.",
        "citation": "BOT 1121 Lec 14, Slide 20-21",
        "tags": ["fig wasp", "male wasp", "female wasp", "gall", "mating"]
    },
    {
        "id": "bot-1121-m2-c25",
        "front": "What is parthenocarpy, and why is it important for commercial figs?",
        "hint": "Fruit ripening without pollination or seeds (virgin fruit).",
        "back": "• **Parthenocarpy**: The development and ripening of fruit **without pollination or fertilization**, resulting in seedless fruit.\n• **Why it matters**: Commercial fig cultivars like **'Black Mission'** are parthenocarpic—they produce delicious, sweet, mature figs without needing caprifig trees or fig wasps to pollinate them!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p31_2.jpeg",
        "imageDescription": "Ripe Black Mission figs developing parthenocarpically without requiring wasp pollination.",
        "citation": "BOT 1121 Lec 14, Slide 31",
        "tags": ["fig", "parthenocarpy", "black mission", "commercial agriculture"]
    },

    # ==========================================
    # LECTURE 15: Water Transport (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c26",
        "front": "What is transpiration, and where does most of it occur?",
        "hint": "Water evaporating from leaves through microscopic pores.",
        "back": "• **Transpiration**: The evaporation of water vapor from a plant's tissues into the atmosphere.\n• **Location**: Over **90%** of transpiration occurs through the **stomata** (pores on the surface of leaves).\n• **Function**: Transpiration generates the negative tension that \"pulls\" water and dissolved mineral nutrients all the way up from roots to the leaves.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p6_0.jpeg",
        "imageDescription": "Diagram of leaf transpiration showing water vapor diffusing out through open stomata.",
        "citation": "BOT 1121 Lec 15, Slide 5-6",
        "tags": ["water transport", "transpiration", "stomata", "evaporation"]
    },
    {
        "id": "bot-1121-m2-c27",
        "front": "How do guard cells open and close stomata?",
        "hint": "Potassium ions (K+) are pumped in, and water follows by osmosis.",
        "back": "• **To OPEN Stomata**:\n  1. Guard cells actively pump in potassium ions (**K+**).\n  2. Water enters the guard cells by **osmosis**.\n  3. Guard cells become **turgid (swollen)** and bow outwards, opening the pore.\n\n• **To CLOSE Stomata**:\n  1. Potassium ions (**K+**) exit the guard cells.\n  2. Water leaves by osmosis.\n  3. Guard cells become **flaccid (limp)** and collapse together, closing the pore.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p22_0.jpeg",
        "imageDescription": "Mechanism of stomata opening: K+ ion influx causes osmotic swelling of guard cells.",
        "citation": "BOT 1121 Lec 15, Slide 22",
        "tags": ["stomata", "guard cells", "potassium", "osmosis", "turgor"]
    },
    {
        "id": "bot-1121-m2-c28",
        "front": "What is the Cohesion-Tension Theory of water transport?",
        "hint": "Water is pulled from the top; water sticks to water, and water sticks to xylem walls.",
        "back": "The **Cohesion-Tension Theory** explains how water climbs tall trees without pumps:\n\n• **Tension (Pull)**: Evaporation of water from leaves (transpiration) creates a strong **negative pressure (suction/tension)** that pulls water up from below.\n• **Cohesion**: Water molecules stick tightly to each other via hydrogen bonds, forming an unbroken water chain.\n• **Adhesion**: Water molecules stick to the hydrophilic cell walls of xylem, supporting the weight of the water column against gravity.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p25_0.jpeg",
        "imageDescription": "The cohesion-tension model showing water pulled upward through xylem by leaf transpiration.",
        "citation": "BOT 1121 Lec 15, Slide 25",
        "tags": ["cohesion-tension", "transpiration", "xylem", "water pull"]
    },
    {
        "id": "bot-1121-m2-c29",
        "front": "What is xylem cavitation (or embolism), and what causes it?",
        "hint": "An air bubble forms inside the water pipeline, breaking the chain.",
        "back": "• **Cavitation**: The breaking of the continuous water column inside a xylem vessel or tracheid, forming an **air bubble (embolism)**.\n• **Causes**:\n  - Severe drought (extreme negative tension pulls air through pit membranes).\n  - Freezing and thawing (dissolved air comes out of solution as ice forms).\n• **Consequence**: The air bubble blocks water flow through that xylem conduit, like an air bubble in a drinking straw.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p26_0.jpeg",
        "imageDescription": "Diagram of cavitation forming an air bubble embolism that blocks xylem water transport.",
        "citation": "BOT 1121 Lec 15, Slide 26 & 30",
        "tags": ["xylem", "cavitation", "embolism", "drought", "water tension"]
    },
    {
        "id": "bot-1121-m2-c30",
        "front": "What are tracheids and vessel elements in xylem?",
        "hint": "Dead tube cells: one is long and tapered with pits; the other is wider with open perforated ends.",
        "back": "Both are **dead at maturity** with thick lignified cell walls that conduct water under tension:\n\n• **Tracheids**:\n  - Long, slender, tapered cells with closed ends.\n  - Water passes through **pits** in lateral walls.\n  - Found in all vascular plants (only water conduit in gymnosperms/ferns).\n• **Vessel Elements**:\n  - Shorter, much wider cylindrical cells aligned end-to-end.\n  - Have open **perforation plates** at the ends, forming open pipe-like vessels.\n  - Highly efficient water flow; found almost exclusively in **angiosperms**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p12_0.jpeg",
        "imageDescription": "Comparison of xylem tracheids with bordered pits vs wide vessel elements with perforation plates.",
        "citation": "BOT 1121 Lec 15, Slide 12",
        "tags": ["xylem", "tracheids", "vessel elements", "perforation plate"]
    },

    # ==========================================
    # LECTURE 16: Sugar Transport (Phloem) (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c31",
        "front": "What are sieve tube elements and companion cells in phloem?",
        "hint": "One is the living tube without a nucleus; the other is the metabolic helper cell with a nucleus.",
        "back": "Phloem conducting cells are **alive at maturity**:\n\n• **Sieve Tube Elements**:\n  - Elongated conducting cells joined end-to-end through perforated **sieve plates**.\n  - Lack a nucleus, vacuole, and ribosomes at maturity to allow sap to flow freely.\n• **Companion Cells**:\n  - Connected to sieve tube elements by numerous plasmodesmata.\n  - Retain their nucleus and have many mitochondria; they handle metabolism and load/unload sugars into the sieve tubes.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p8_0.jpeg",
        "imageDescription": "Longitudinal section of phloem showing sieve tube elements, sieve plates, and companion cells.",
        "citation": "BOT 1121 Lec 16, Slide 8",
        "tags": ["phloem", "sieve tube", "companion cell", "sieve plate"]
    },
    {
        "id": "bot-1121-m2-c32",
        "front": "In phloem transport, what is a sugar source vs. a sugar sink?",
        "hint": "Where sugar is produced/exported vs where sugar is consumed or stored.",
        "back": "• **Source**: A plant organ that **produces or exports** more sugar than it uses.\n  - *Examples*: Mature photosynthesizing leaves, or storage roots in early spring releasing stored starch.\n\n• **Sink**: A plant organ that **consumes or stores** sugar.\n  - *Examples*: Growing root tips, developing fruits, flowers, seeds, apical buds, and young expanding leaves.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p14_0.jpeg",
        "imageDescription": "Diagram of source-to-sink sugar translocation from mature leaves to roots and shoot tips.",
        "citation": "BOT 1121 Lec 16, Slide 14",
        "tags": ["phloem", "source", "sink", "sugar translocation"]
    },
    {
        "id": "bot-1121-m2-c33",
        "front": "How does the Pressure-Flow Hypothesis explain sugar transport?",
        "hint": "Sugar is pumped in, water follows by osmosis creating high pressure, pushing sap to the sink.",
        "back": "The **Pressure-Flow Hypothesis** (Münch model):\n\n1. **Loading at Source**: Sugars are actively pumped into sieve tube elements at the source.\n2. **Water Influx**: Water moves from adjacent xylem into the phloem by **osmosis**, creating **high positive turgor pressure**.\n3. **Bulk Flow**: The high pressure pushes the sugary sap through sieve tubes toward the sink.\n4. **Unloading at Sink**: Sugars are unloaded at the sink; water moves back to the xylem by osmosis, lowering pressure.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p18_0.jpeg",
        "imageDescription": "The pressure-flow mechanism: high turgor pressure at source drives sap to low pressure at sink.",
        "citation": "BOT 1121 Lec 16, Slide 18",
        "tags": ["pressure-flow", "phloem", "bulk flow", "osmosis", "turgor"]
    },
    {
        "id": "bot-1121-m2-c34",
        "front": "What form of sugar is transported in phloem sap, and why?",
        "hint": "Table sugar (disaccharide made of glucose + fructose).",
        "back": "• **Sugar Transported**: Plants transport sugar primarily as **sucrose** (a disaccharide made of glucose + fructose).\n• **Why Sucrose?**:\n  - Sucrose is a **non-reducing sugar**, making it chemically stable and unreactive during transit.\n  - It packs twice the energy of glucose per molecule, making transport highly efficient.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p24_0.jpeg",
        "imageDescription": "Molecular structure of sucrose (glucose + fructose) transported through phloem sieve tubes.",
        "citation": "BOT 1121 Lec 16, Slide 24",
        "tags": ["phloem", "sucrose", "carbohydrate transport", "non-reducing sugar"]
    },
    {
        "id": "bot-1121-m2-c35",
        "front": "What is girdling (ringing) a tree, and why does it cause the tree to die?",
        "hint": "Removing a strip of bark all the way around the trunk removes the phloem.",
        "back": "• **What it is**: Girdling is removing a complete strip of outer bark (which contains the **phloem**) all the way around a tree trunk.\n• **Why it kills the tree**:\n  - The xylem (deeper inside the wood) is unharmed, so water still flows up to leaves.\n  - However, **sugars cannot travel down** through the severed phloem to the roots.\n  - Eventually, the **roots starve to death** from lack of sugar, causing the entire tree to die.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p36_0.jpeg",
        "imageDescription": "Photo of a girdled tree trunk showing severed phloem and root starvation mechanism.",
        "citation": "BOT 1121 Lec 16, Slide 36",
        "tags": ["girdling", "phloem", "bark", "tree death", "root starvation"]
    },

    # ==========================================
    # LECTURE 17: Photosynthesis Part 1 - Light Reactions (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c36",
        "front": "What is the chemical equation for photosynthesis, and where does a plant's mass come from?",
        "hint": "CO2 + H2O + light -> glucose + O2. Mass comes from the air, not the soil!",
        "back": "• **Photosynthesis Equation**:\n  $$6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{light energy} \\rightarrow \\text{C}_6\\text{H}_{12}\\text{O}_6 \\text{ (glucose)} + 6\\text{O}_2$$\n\n• **Where Plant Mass Comes From**:\n  - Jan Baptist van Helmont's classic willow tree experiment proved that plant mass does **NOT** come from soil.\n  - The massive dry weight of trees and plants comes from **carbon dioxide (CO2) absorbed from the air** (fixed into carbon polymers like cellulose)!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p4_0.jpeg2000",
        "imageDescription": "Van Helmont's willow tree experiment showing plant mass comes from air and water, not soil.",
        "citation": "BOT 1121 Lec 17, Slide 8 & 13",
        "tags": ["photosynthesis", "equation", "van helmont", "carbon dioxide", "biomass"]
    },
    {
        "id": "bot-1121-m2-c37",
        "front": "What are the main parts of a chloroplast, and where does each stage of photosynthesis take place?",
        "hint": "Thylakoid discs, grana stacks, and stroma fluid.",
        "back": "Chloroplast structure:\n\n• **Thylakoids**: Flattened disc-like membrane sacs containing chlorophyll.\n  - **Light-Dependent Reactions** take place here across the thylakoid membrane.\n• **Granum** (plural: *grana*): Stacks of thylakoid discs.\n• **Stroma**: The dense fluid-filled space surrounding the thylakoids.\n  - The **Calvin Cycle (Light-Independent Reactions)** takes place here in the stroma.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p21_0.jpeg",
        "imageDescription": "Chloroplast anatomy detailing outer/inner membranes, stroma, thylakoids, and grana stacks.",
        "citation": "BOT 1121 Lec 17, Slide 21",
        "tags": ["chloroplast", "thylakoid", "granum", "stroma", "light reactions"]
    },
    {
        "id": "bot-1121-m2-c38",
        "front": "What are the inputs and outputs of the Light-Dependent Reactions of photosynthesis?",
        "hint": "Water and light go in; oxygen, ATP, and NADPH come out.",
        "back": "In the thylakoid membrane:\n\n• **Inputs**:\n  - **Sunlight (photons)**: Absorbed by chlorophyll pigments.\n  - **Water (H2O)**: Split to provide replacement electrons.\n  - **ADP + Pi** and **NADP+**.\n\n• **Outputs**:\n  - **Oxygen (O2)**: Released as a byproduct into the atmosphere when water is split.\n  - **ATP**: Chemical energy to fuel the Calvin Cycle.\n  - **NADPH**: High-energy electron carrier to fuel the Calvin Cycle.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p28_0.jpeg",
        "imageDescription": "Overview of the light-dependent reactions generating ATP and NADPH while releasing O2.",
        "citation": "BOT 1121 Lec 17, Slide 30-37",
        "tags": ["light reactions", "inputs", "outputs", "water splitting", "atp", "nadph"]
    },
    {
        "id": "bot-1121-m2-c39",
        "front": "What does chlorophyll do, and which colors of light does it absorb and reflect?",
        "hint": "Why do leaves appear green to our eyes?",
        "back": "• **Role**: Chlorophyll is the primary photosynthetic pigment; it absorbs photons to excite electrons to higher energy levels.\n• **Absorbs**: Strongly absorbs **Blue** (~430-450 nm) and **Red** (~650-680 nm) light.\n• **Reflects**: Reflects **Green** light (~500-550 nm).\n  - Because green light is reflected and not absorbed, plants look green to us!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p24_0.jpeg",
        "imageDescription": "Absorption spectrum of chlorophyll a and b showing peak absorption in red/blue and reflection in green.",
        "citation": "BOT 1121 Lec 17, Slide 23-25",
        "tags": ["chlorophyll", "pigments", "absorption spectrum", "green light"]
    },
    {
        "id": "bot-1121-m2-c40",
        "front": "What is ATP Synthase and how does it make ATP in the thylakoid membrane?",
        "hint": "A microscopic rotary turbine powered by hydrogen protons (H+).",
        "back": "• **ATP Synthase**: An enzyme complex embedded in the thylakoid membrane.\n• **How it works**:\n  1. The electron transport chain pumps hydrogen protons (**H+**) into the thylakoid lumen, creating a steep concentration gradient.\n  2. Protons rush back out into the stroma through ATP Synthase.\n  3. This proton flow spins the enzyme like a turbine, attaching a phosphate to ADP to create **ATP** (*photophosphorylation*).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p29_0.jpeg",
        "imageDescription": "ATP Synthase rotary turbine driven by proton (H+) electrochemical gradient across thylakoid.",
        "citation": "BOT 1121 Lec 17, Slide 34-36",
        "tags": ["atp synthase", "chemiosmosis", "proton gradient", "photophosphorylation"]
    },

    # ==========================================
    # LECTURE 18: Photosynthesis Part 2 - Calvin Cycle & C4/CAM (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c41",
        "front": "What is the Calvin Cycle, where does it occur, and what are its inputs and outputs?",
        "hint": "Occurs in the stroma; turns CO2 into sugar using ATP and NADPH.",
        "back": "• **Location**: In the **stroma** (fluid) of the chloroplast.\n• **Inputs**:\n  - **CO2** (absorbed from air)\n  - **ATP** & **NADPH** (energy from the light reactions)\n• **Outputs**:\n  - **G3P** (Glyceraldehyde-3-phosphate, a 3-carbon sugar used to build glucose, starch, and cellulose)\n  - **ADP + Pi** & **NADP+** (recycled back to light reactions)",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p7_0.png",
        "imageDescription": "Calvin-Benson cycle in the stroma converting CO2 into 3-carbon sugars (G3P) using ATP and NADPH.",
        "citation": "BOT 1121 Lec 18, Slide 7-10",
        "tags": ["calvin cycle", "stroma", "carbon fixation", "g3p", "glucose"]
    },
    {
        "id": "bot-1121-m2-c42",
        "front": "What is RuBisCO, why is it so important, and what is its main flaw?",
        "hint": "Most abundant enzyme on Earth! Fixes CO2, but sometimes grabs oxygen by mistake.",
        "back": "• **What it is**: *Ribulose-1,5-bisphosphate carboxylase-oxygenase*.\n• **Importance**: The most abundant enzyme on Earth (makes up 10-25% of all leaf protein). It performs **carbon fixation**—attaching CO2 from the air to RuBP to kick off the Calvin Cycle.\n• **Main Flaw**: It evolved when atmospheric O2 was low, so its active site can accidentally bind **O2 instead of CO2**, triggering wasteful **photorespiration**!",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p5_0.jpeg",
        "imageDescription": "RuBisCO enzyme structure and role in catalyzing the addition of CO2 to RuBP.",
        "citation": "BOT 1121 Lec 18, Slide 4-6 & 23",
        "tags": ["rubisco", "enzyme", "carbon fixation", "photorespiration"]
    },
    {
        "id": "bot-1121-m2-c43",
        "front": "What is photorespiration, and why is it bad for plants?",
        "hint": "RuBisCO binds O2 instead of CO2, wasting ATP and releasing CO2 without making sugar.",
        "back": "• **What it is**: A wasteful metabolic process that occurs when RuBisCO binds to **O2** instead of CO2.\n• **Why it is bad**:\n  - It consumes ATP and NADPH without producing any sugar or ATP.\n  - It actually *releases* previously fixed CO2 back into the air.\n• **When it happens**: In hot, dry weather when plants close stomata to save water. CO2 drops inside the leaf while O2 builds up from light reactions, accelerating photorespiration.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p24_0.png",
        "imageDescription": "Comparison of Calvin Cycle (CO2 binding) vs wasteful photorespiration (O2 binding by RuBisCO).",
        "citation": "BOT 1121 Lec 18, Slide 24-25",
        "tags": ["photorespiration", "rubisco", "stomata closure", "wasteful"]
    },
    {
        "id": "bot-1121-m2-c44",
        "front": "How do C4 plants (like corn and sugarcane) prevent photorespiration?",
        "hint": "Spatial separation — carbon capture happens in one cell, Calvin cycle in another.",
        "back": "C4 plants use **Spatial Separation** (Kranz anatomy) to beat photorespiration:\n\n1. **Mesophyll Cells**: CO2 is captured by **PEP carboxylase** (an enzyme that never binds O2) and turned into a 4-carbon acid.\n2. **Bundle Sheath Cells**: The 4-carbon acid is pumped into bundle sheath cells around leaf veins, where it releases high concentrations of CO2 right around RuBisCO.\n• Because CO2 is concentrated around RuBisCO, it never binds O2!\n• *Examples*: Corn, sugarcane, crabgrass, sorghum.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p28_0.jpeg",
        "imageDescription": "C4 Kranz anatomy showing spatial separation of CO2 capture in mesophyll and Calvin cycle in bundle sheath.",
        "citation": "BOT 1121 Lec 18, Slide 28-29",
        "tags": ["c4 photosynthesis", "spatial separation", "pep carboxylase", "bundle sheath", "corn"]
    },
    {
        "id": "bot-1121-m2-c45",
        "front": "How do CAM plants (cacti, agaves, succulents) survive in hot, dry deserts?",
        "hint": "Temporal separation — open stomata at night, close them during the hot day!",
        "back": "CAM plants (*Crassulacean Acid Metabolism*) use **Temporal Separation (Night vs. Day)**:\n\n• **At Night (Stomata Open)**: It is cool and humid, so plants open stomata with minimal water loss. CO2 is captured by PEP carboxylase and stored as malic acid in large cell vacuoles.\n• **During the Day (Stomata Closed)**: Stomata remain tightly shut to conserve water under the blazing sun. Stored acid breaks down to release CO2 inside the cells, running the Calvin cycle using sunlight!\n• *Examples*: Cacti, pineapple, agaves, jade plant, aloe.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p30_0.jpeg",
        "imageDescription": "CAM photosynthesis mechanism: night CO2 fixation into vacuoles and daytime Calvin cycle with closed stomata.",
        "citation": "BOT 1121 Lec 18, Slide 30-33",
        "tags": ["cam photosynthesis", "temporal separation", "desert succulents", "night stomata", "cacti"]
    }
]

# Define 15 clean, direct practical quiz questions testing Midterm 2 concepts
simplified_quizzes = [
    {
        "station": "Question 1: Fern Biomechanics",
        "question": "What is the specialized ring of thickened cells on a fern sporangium that snaps open to catapult spores into the air?",
        "options": ["Indusium", "Annulus", "Rhizoid", "Prothallus"],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "High magnification of a fern sporangium showcasing the thickened annulus crest.",
        "socraticHint": "Think of the ring that acts like an elastic catapult when water evaporates.",
        "explanation": "The correct answer is the **Annulus**. The annulus is a crest of cells with thickened inner walls. As water evaporates, negative tension builds until the ring snaps forward, flinging spores out.",
        "citation": "BOT 1121 Lec 10, Slide 31"
    },
    {
        "station": "Question 2: Fern Life Cycle",
        "question": "What do fern sperm require in order to swim to the archegonium and fertilize the egg?",
        "options": [
            "Insect pollinators like bees",
            "A film of liquid water",
            "High wind currents",
            "Direct sunlight"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p32_2.jpeg",
        "imageDescription": "Gametophyte slide showing antheridia producing swimming flagellated sperm.",
        "socraticHint": "Fern sperm have flagella and must swim across the surface of the gametophyte.",
        "explanation": "The correct answer is **A film of liquid water**. Fern sperm have flagella and must physically swim from the antheridium to the archegonium to fertilize the egg.",
        "citation": "BOT 1121 Lec 10, Slide 32 & 39"
    },
    {
        "station": "Question 3: Gymnosperm Seeds",
        "question": "In a gymnosperm seed (like a pine seed), where does the stored food reserve for the embryo come from?",
        "options": [
            "Triploid (3n) endosperm formed by double fertilization",
            "Haploid (1n) female gametophyte tissue",
            "Diploid (2n) fruit wall tissue",
            "The pollen grain"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p6_0.jpeg",
        "imageDescription": "Gymnosperm seed diagram showing the haploid female gametophyte feeding the embryo.",
        "socraticHint": "Gymnosperms lack double fertilization; their nutritive tissue is the haploid gametophyte.",
        "explanation": "The correct answer is the **Haploid (1n) female gametophyte tissue**. Unlike flowering plants (which form 3n endosperm via double fertilization), gymnosperms feed the embryo using the existing female gametophyte.",
        "citation": "BOT 1121 Lec 11, Slide 6-7"
    },
    {
        "station": "Question 4: Living Fossils",
        "question": "Which gymnosperm is a 'living fossil' with fan-shaped leaves and smelly female seeds containing butyric acid?",
        "options": [
            "Coast Redwood (*Sequoia sempervirens*)",
            "Cycad (*Cycas revoluta*)",
            "Maidenhair tree (*Ginkgo biloba*)",
            "Mormon tea (*Ephedra*)"
        ],
        "correctIndex": 2,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p15_0.jpeg",
        "imageDescription": "Distinctive fan-shaped leaves of Ginkgo biloba.",
        "socraticHint": "Think of the only surviving species in Ginkgophyta.",
        "explanation": "The correct answer is ***Ginkgo biloba***. It is the sole surviving member of its division, has fan-shaped leaves, is dioecious, and female seeds emit a butyric acid smell (like rancid butter).",
        "citation": "BOT 1121 Lec 11, Slide 14-17"
    },
    {
        "station": "Question 5: Floral Fusion",
        "question": "What is the botanical term for the fusion of LIKE floral organs (such as petals fused into a tube)?",
        "options": ["Adnation", "Connation", "Epigyny", "Parthenocarpy"],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p12_1.jpeg",
        "imageDescription": "Illustration showing petals fused together into a single corolla tube.",
        "socraticHint": "Like parts fused is connation; unlike parts fused (like stamens to petals) is adnation.",
        "explanation": "The correct answer is **Connation**. Connation is the fusion of like organs (petals to petals, sepals to sepals). Adnation is the fusion of unlike organs (stamens attached to petals).",
        "citation": "BOT 1121 Lec 12, Slide 12"
    },
    {
        "station": "Question 6: Ovary Position",
        "question": "In an apple or cucumber flower, the sepals and petals attach ABOVE the ovary. What type of ovary is this?",
        "options": [
            "Superior ovary (Hypogynous)",
            "Inferior ovary (Epigynous)",
            "Superficial ovary",
            "Apocarpous ovary"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Diagram comparing superior ovary (hypogynous) vs inferior ovary (epigynous).",
        "socraticHint": "When the floral parts attach above the ovary, the ovary sits below (inferior).",
        "explanation": "The correct answer is an **Inferior ovary (Epigynous flower)**. The ovary is embedded in the receptacle and sits below the attachment points of the sepals, petals, and stamens.",
        "citation": "BOT 1121 Lec 12, Slide 28"
    },
    {
        "station": "Question 7: Fruit Anatomy",
        "question": "When eating a peach or cherry (a drupe), what fruit layer does the hard, stony 'pit' represent?",
        "options": [
            "The seed coat (testa)",
            "The endocarp layer of the pericarp",
            "The mesocarp layer of the pericarp",
            "The exocarp peel"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p5_0.jpeg",
        "imageDescription": "Cross section of a drupe showing exocarp skin, fleshy mesocarp, and stony endocarp pit.",
        "socraticHint": "The pericarp has 3 layers: exocarp (skin), mesocarp (flesh), and endocarp (pit).",
        "explanation": "The correct answer is the **Endocarp layer of the pericarp**. In a drupe, the inner ovary wall lignifies into a hard, protective pit that encloses the true seed.",
        "citation": "BOT 1121 Lec 13, Slide 5"
    },
    {
        "station": "Question 8: Fruit Types",
        "question": "A blackberry develops from a single flower with many separate carpels. What type of fruit is this?",
        "options": [
            "Multiple fruit",
            "Aggregate fruit",
            "Pome",
            "Simple berry"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p13_2.jpeg",
        "imageDescription": "Aggregate fruit developing from multiple carpels on a single flower.",
        "socraticHint": "One flower with many ovaries makes an aggregate; multiple flowers fused make a multiple fruit.",
        "explanation": "The correct answer is an **Aggregate fruit**. Aggregate fruits (like blackberries and raspberries) arise from a single flower that possesses multiple separate pistils/carpels.",
        "citation": "BOT 1121 Lec 13, Slide 13"
    },
    {
        "station": "Question 9: Fig Biology",
        "question": "Why can female fig wasps lay eggs in caprifigs, but CANNOT lay eggs in female edible figs?",
        "options": [
            "Edible figs lack an ostiole entrance hole",
            "Caprifigs have short-styled flowers matching the wasp's ovipositor length, while edible figs have long-styled flowers",
            "Edible figs produce poison that kills wasp eggs",
            "Wasps only mate inside dark caves"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p26_0.jpeg",
        "imageDescription": "Comparison of short style in caprifig vs long style in edible fig.",
        "socraticHint": "Look at the length of the flower style compared to the wasp's egg-laying tube (ovipositor).",
        "explanation": "The correct answer is that **Caprifigs have short-styled flowers matching the wasp ovipositor, while edible figs have long styles**. The wasp's ovipositor cannot reach the ovary in edible figs, so she only pollinates them.",
        "citation": "BOT 1121 Lec 14, Slide 24-26"
    },
    {
        "station": "Question 10: Stomata Physiology",
        "question": "What causes guard cells to swell and OPEN the stomatal pore?",
        "options": [
            "Pumping out potassium ions (K+) so water leaves",
            "Pumping in potassium ions (K+), causing water to enter by osmosis",
            "Loss of water vapor during the night",
            "Accumulation of oxygen gas inside the leaf"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p22_0.jpeg",
        "imageDescription": "Diagram of guard cell turgor mechanism driven by K+ ion uptake and osmosis.",
        "socraticHint": "Active uptake of K+ lowers solute potential, drawing water inward so guard cells swell.",
        "explanation": "The correct answer is that **guard cells pump in K+ ions, and water follows by osmosis**. As turgor pressure rises, the guard cells swell and bow outwards, opening the pore.",
        "citation": "BOT 1121 Lec 15, Slide 22"
    },
    {
        "station": "Question 11: Water Transport",
        "question": "According to the Cohesion-Tension Theory, what provides the main 'pull' that moves water up tall trees?",
        "options": [
            "Positive root pressure pushing from below",
            "Transpiration (evaporation of water from leaves)",
            "Active muscle-like contraction of xylem walls",
            "Sugar transport in the phloem"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p25_0.jpeg",
        "imageDescription": "Transpiration pull at the top of the plant driving the continuous xylem water column.",
        "socraticHint": "Water evaporating from leaf stomata creates strong negative suction.",
        "explanation": "The correct answer is **Transpiration (evaporation of water from leaves)**. Transpiration creates negative hydrostatic tension that pulls the unbroken, cohesive water chain all the way up.",
        "citation": "BOT 1121 Lec 15, Slide 25"
    },
    {
        "station": "Question 12: Sugar Transport",
        "question": "In the Pressure-Flow Hypothesis, why does sap flow from source to sink in the phloem?",
        "options": [
            "High turgor pressure at the source pushes sap toward lower pressure at the sink",
            "Gravity pulls sugar downwards toward the roots",
            "Transpiration pull sucks phloem sap upward",
            "Air pressure blows sap through empty vessels"
        ],
        "correctIndex": 0,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p18_0.jpeg",
        "imageDescription": "High turgor pressure generated by sugar loading at the source pushes bulk phloem sap to sink.",
        "socraticHint": "Active sugar loading draws in water by osmosis, generating high positive pressure.",
        "explanation": "The correct answer is that **high turgor pressure at the source pushes sap toward the lower pressure sink**. Water enters phloem by osmosis at the source, creating positive hydrostatic pressure.",
        "citation": "BOT 1121 Lec 16, Slide 18"
    },
    {
        "station": "Question 13: Light Reactions",
        "question": "What gas is released as a byproduct when water molecules are split during the Light Reactions of photosynthesis?",
        "options": [
            "Carbon dioxide (CO2)",
            "Oxygen (O2)",
            "Methane (CH4)",
            "Nitrogen (N2)"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p28_0.jpeg",
        "imageDescription": "Photolysis of water yielding H+ ions, electrons, and O2 gas.",
        "socraticHint": "Plants split H2O to take its electrons; what happens to the remaining oxygen?",
        "explanation": "The correct answer is **Oxygen (O2)**. In the light reactions, water molecules (H2O) are split by the oxygen-evolving complex to supply replacement electrons, releasing O2 gas.",
        "citation": "BOT 1121 Lec 17, Slide 31-33"
    },
    {
        "station": "Question 14: Calvin Cycle",
        "question": "What is the primary job of the enzyme RuBisCO in the Calvin Cycle?",
        "options": [
            "To split water molecules and make oxygen",
            "To fix carbon dioxide by attaching CO2 to RuBP",
            "To absorb green light photons",
            "To pump potassium ions into guard cells"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p5_0.jpeg",
        "imageDescription": "RuBisCO catalyzing the fixation of atmospheric CO2 onto 5-carbon RuBP.",
        "socraticHint": "RuBisCO stands for Ribulose-1,5-bisphosphate carboxylase/oxygenase.",
        "explanation": "The correct answer is **To fix carbon dioxide by attaching CO2 to RuBP**. RuBisCO catalyzes the very first step of the Calvin Cycle, turning gaseous CO2 into organic carbon molecules.",
        "citation": "BOT 1121 Lec 18, Slide 4-6"
    },
    {
        "station": "Question 15: C4 & CAM Photosynthesis",
        "question": "How do CAM plants (like desert cacti and agaves) avoid water loss and photorespiration?",
        "options": [
            "They only open stomata at night to capture CO2, and keep them closed during the hot day",
            "They absorb water directly through their spines without using stomata",
            "They run the Calvin Cycle only underground in roots",
            "They stop photosynthesis completely during sunny days"
        ],
        "correctIndex": 0,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p30_0.jpeg",
        "imageDescription": "CAM plants opening stomata at night to store CO2 as malic acid and closing stomata during day.",
        "socraticHint": "Temporal separation: cool night for CO2 intake, sunny day for light reactions with closed pores.",
        "explanation": "The correct answer is that **they open stomata at night to capture CO2, and close them during the hot day**. This temporal separation allows them to conserve scarce water while avoiding photorespiration.",
        "citation": "BOT 1121 Lec 18, Slide 30-32"
    }
]

# Load existing decks.json
decks_path = "G:/My Drive/Academics/study_portal/decks.json"
with open(decks_path, "r", encoding="utf-8") as f:
    portal_data = json.load(f)

# Replace deck 0 (bot-1121-midterm-2) with simplified, slide-grounded cards and quizzes
deck_found = False
for deck in portal_data.get("decks", []):
    if deck.get("id") == "bot-1121-midterm-2":
        deck["title"] = "BOT-1121: Midterm #2 Master Deck (Lectures 10–18)"
        deck["description"] = "Comprehensive, student-friendly study deck for BOT 1121 Midterm #2 directly grounded in Sean Ryan's lecture slides (Lectures 10 to 18). Covers Ferns, Gymnosperms, Flowers, Fruits & Seeds, Fig Biology, Water & Sugar Transport, and Photosynthesis Parts 1 & 2."
        deck["flashcards"] = simplified_cards
        deck["quizzes"] = simplified_quizzes
        deck_found = True
        break

if not deck_found:
    print("ERROR: Deck bot-1121-midterm-2 not found!")
else:
    with open(decks_path, "w", encoding="utf-8") as f:
        json.dump(portal_data, f, indent=2, ensure_ascii=False)
    print(f"SUCCESS: Successfully updated bot-1121-midterm-2 with {len(simplified_cards)} simplified flashcards and {len(simplified_quizzes)} practical quiz questions!")
