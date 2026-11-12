import json
import os

cards = [
    # ==========================================
    # LECTURE 10: Herbarium Studies & Ferns (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c01",
        "front": "Observe the cluster of sporangia on the abaxial surface of a fern frond. What is this discrete reproductive cluster termed, what protective flap may cover it, and what is its ploidy level?",
        "hint": "Consider the specialized multicellular aggregation on the sporophyte (2n) leaf and the membranous sterile shield that shelters young sporangia.",
        "back": "This structure is a **sorus** (plural: **sori**).\n\n• **Ploidy**: The frond and sorus belong to the **diploid sporophyte (2n)** generation.\n• **Protective Flap**: Many leptosporangiate ferns possess an **indusium**, an epidermal outgrowth that shields the maturing sporangia from desiccation and premature exposure.\n• **False Indusium**: In ferns lacking a true indusium (e.g., *Adiantum* maidenhair ferns), the curled leaf margin serves as a protective flap.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "Transverse section of a fern sorus showing stalked sporangia clustered beneath an overarching indusium.",
        "citation": "BOT 1121 Lec 10, Slide 31",
        "tags": ["ferns", "sorus", "indusium", "sporangia"]
    },
    {
        "id": "bot-1121-m2-c02",
        "front": "In leptosporangiate ferns, what anatomical structure functions as a catapult to violently disperse spores, and what physical mechanism powers this release?",
        "hint": "Look for the ring of differentially thickened cell walls encircling the sporangium that responds dynamically to water evaporation.",
        "back": "The structure is the **annulus**.\n\n• **Mechanism**: The annulus consists of a single row of cells with differentially thickened, lignified inner and radial walls, but thin outer walls.\n• **Cavitation / Cohesion**: As water evaporates from these cells, surface tension pulls the thin outer walls inward, creating massive negative hydrostatic tension. When water tension breaks (cavitation), the stored elastic energy snaps the annulus forward, catapulting haploid **meiospores (n)** into air currents away from the parent frond.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "Single fern sporangium showing the prominent crest of thickened annulus cells and lip cells (stomium) that tear during spore release.",
        "citation": "BOT 1121 Lec 10, Slide 31",
        "tags": ["ferns", "annulus", "sporangium", "biomechanics"]
    },
    {
        "id": "bot-1121-m2-c03",
        "front": "Describe the fern gametophyte (prothallus): What is its ploidy, morphology, trophic status, and how are gametes produced and fertilized?",
        "hint": "Recall that in homosporous ferns, spores germinate into a tiny heart-shaped, free-living, photosynthetic thallus bearing both archegonia and antheridia.",
        "back": "The fern gametophyte is the **prothallus**.\n\n• **Ploidy**: **Haploid (n)**, germinated directly from a single haploid meiospore via mitosis.\n• **Morphology & Trophic Status**: A tiny (~0.5–1 cm), heart-shaped, photosynthetic, independent thallus anchored by single-celled rhizoids (lacks true roots and vascular tissue).\n• **Gametangia**: Produces flagellated sperm inside **antheridia** (near rhizoids) and non-motile egg cells inside **archegonia** (near apical notch).\n• **Fertilization**: Requires external film of **liquid water** for multi-flagellated sperm to swim chemotactically into the archegonial neck to fertilize the egg.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p32_2.jpeg",
        "imageDescription": "Whole mount of a heart-shaped fern gametophyte (prothallus) with archegonia located near the apical notch and antheridia near the basal rhizoids.",
        "citation": "BOT 1121 Lec 10, Slide 32",
        "tags": ["ferns", "gametophyte", "prothallus", "archegonia", "antheridia"]
    },
    {
        "id": "bot-1121-m2-c04",
        "front": "What are the essential data elements required on an archival herbarium voucher label, and why are voucher specimens indispensable for botanical research?",
        "hint": "Review the standards of the Robert F. Hoover Herbarium at Cal Poly for documentation, taxonomic authorship, and spatial metadata.",
        "back": "Key components of an archival **Herbarium Voucher Label**:\n\n1. **Scientific Name & Authorship**: Binomial nomenclature with authority (e.g., *Eschscholzia rhombipetala* Greene).\n2. **Location & Coordinates**: Precise geographic locality, GPS latitude/longitude, elevation, and county/state.\n3. **Habitat & Ecology**: Soil type, slope, aspect, associated plant community.\n4. **Phenology & Frequency**: Flowering/fruiting condition, abundance in population.\n5. **Collector & Number**: Primary collector name, collection date, and unique collection number.\n\n• **Scientific Value**: Provides an immutable physical baseline for DNA extraction, phenological shift tracking across climate eras, morphological verification, and conservation status assessments.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p5_0.jpeg",
        "imageDescription": "Archival herbarium specimen sheet from Cal Poly Robert F. Hoover Herbarium displaying mounted voucher specimen and standard metadata label.",
        "citation": "BOT 1121 Lec 10, Slide 5",
        "tags": ["herbarium", "voucher", "taxonomy", "conservation"]
    },
    {
        "id": "bot-1121-m2-c05",
        "front": "How do Lycophytes and Horsetails (Equisetum) differ morphologically and anatomically from true ferns (Polypodiopsida)?",
        "hint": "Consider microphylls vs megaphylls, silica accumulation, jointed stems, and spore-bearing strobili.",
        "back": "Comparative distinction among seedless vascular plants:\n\n• **Lycophytes (*Lycopodium*, *Selaginella*)**:\n  - Possess **microphylls** (leaves with a single, unbranched vascular trace).\n  - Sporangia are born on **sporophylls** often aggregated into terminal **strobili** (cones).\n\n• **Horsetails (*Equisetum*)**:\n  - Possess jointed, ribbed, photosynthetic stems impregnated with abrasive **silica dioxide (SiO2)**.\n  - Microphylls/megaphylls are reduced to whorled subterranean or nodal non-photosynthetic scales.\n  - Spores bear 4 hygroscopic ribbon-like **elaters** that unfurl in dry air to facilitate wind dispersal.\n\n• **True Ferns (Polypodiopsida)**:\n  - Possess **megaphylls** (fronds with complex branched vascular networks) and leptosporangia in sori.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p27_0.jpeg",
        "imageDescription": "Equisetum stem morphology showing ribbed silica-impregnated node, reduced leaf whorls, and terminal sporangiophore strobilus.",
        "citation": "BOT 1121 Lec 10, Slide 27",
        "tags": ["lycophytes", "equisetum", "horsetails", "microphylls"]
    },

    # ==========================================
    # LECTURE 11: Gymnosperms (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c06",
        "front": "What defines a 'gymnosperm' from an evolutionary and anatomical perspective, and what are the four extant divisions (phyla)?",
        "hint": "Translate 'gymno-' and '-sperma'. Are the ovules enclosed within an ovary wall?",
        "back": "The term **Gymnosperm** means **'naked seed'** (from Greek *gymnos* = naked, *sperma* = seed).\n\n• **Key Distinction**: Ovules and seeds are born exposed on the surface of sporophylls or modified scale bracts (e.g., ovuliferous scales of female cones), **not enclosed inside a carpel or ovary wall**.\n\n• **The 4 Extant Phyla**:\n  1. **Pinophyta (Conifers)**: Pines, redwoods, firs, cypresses (largest group; needle/scale leaves, resin canals).\n  2. **Cycadophyta (Cycads)**: Palm-like leaves, massive dioecious cones, flagellated swimming sperm within pollen tubes.\n  3. **Ginkgophyta (*Ginkgo biloba*)**: Monotypic living fossil, fan-shaped dichotomous leaves, dioecious, fleshy smelly seeds.\n  4. **Gnetophyta (*Ephedra*, *Gnetum*, *Welwitschia*)**: Possess vessel elements in xylem, double-fertilization-like phenomena.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p3_0.jpeg",
        "imageDescription": "Morphological comparison of the 4 extant gymnosperm phyla: Conifers, Cycads, Ginkgo, and Gnetophytes.",
        "citation": "BOT 1121 Lec 11, Slide 3",
        "tags": ["gymnosperms", "pinophyta", "cycads", "ginkgo", "gnetophyta"]
    },
    {
        "id": "bot-1121-m2-c07",
        "front": "Identify the primary anatomical components of an immature pine ovule and trace the pathway of the pollen grain during pollination.",
        "hint": "Consider the integument, micropyle, nucellus (megasporangium), and pollination drop.",
        "back": "Anatomical components of a pine ovule:\n\n1. **Integument**: Outer protective diploid (2n) maternal layer that later hardens into the seed coat.\n2. **Micropyle**: Small opening at the apex of the integument through which pollen enters.\n3. **Nucellus (Megasporangium, 2n)**: Nutritive tissue enclosing the megasporocyte.\n4. **Pollination Drop**: Fluid droplet secreted through the micropyle that catches airborne pollen grains (winged/saccate). As the drop evaporates, it draws pollen grains directly into the pollen chamber adjacent to the nucellus.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p4_0.jpeg",
        "imageDescription": "Cross-sectional diagram of a gymnosperm ovule showing integument, micropyle canal, nucellus, and female gametophyte.",
        "citation": "BOT 1121 Lec 11, Slide 4",
        "tags": ["gymnosperms", "ovule", "integument", "micropyle", "pollination"]
    },
    {
        "id": "bot-1121-m2-c08",
        "front": "What is the origin and ploidy of the nutritive reserve tissue in a gymnosperm seed, and how does this contrast fundamentally with angiosperms?",
        "hint": "Is the endosperm formed before or after fertilization? Does double fertilization produce 3n tissue here?",
        "back": "In gymnosperms, the nutritive tissue is the **haploid (n) female gametophyte**.\n\n• **Gymnosperm Nutritive Reserve**: Developed *prior* to fertilization by mitotic division of the functional megaspore. Ploidy is **haploid (1n)**.\n• **Angiosperm Contrast**: In flowering plants, nutritive **endosperm** is **triploid (3n)**, synthesized only *after* double fertilization when a second sperm nucleus fuses with the two polar nuclei of the central cell.\n• **Evolutionary Advantage**: Gymnosperms risk maternal metabolic investment if fertilization fails; angiosperms synthesize nutritive endosperm only upon confirmed fertilization.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p4_0.jpeg",
        "imageDescription": "Gymnosperm seed longitudinal section highlighting the maternal seed coat (2n), nutritive female gametophyte (n), and embryonic sporophyte (2n).",
        "citation": "BOT 1121 Lec 11, Slide 4",
        "tags": ["gymnosperms", "seed", "gametophyte", "ploidy", "endosperm"]
    },
    {
        "id": "bot-1121-m2-c09",
        "front": "Describe the unique sexual and reproductive traits of Ginkgo biloba and Cycads that reflect primitive seed plant ancestry.",
        "hint": "Consider plant sexuality (monoecious vs dioecious) and the method by which sperm reaches the archegonium.",
        "back": "Primitive ancestral traits shared by Cycads and *Ginkgo biloba*:\n\n1. **Strict Dioecy**: Separate male trees (producing pollen cones/strobili) and female trees (producing paired ovules).\n2. **Haustorial Pollen Tube & Motile Swimming Sperm**: Unlike conifers and angiosperms (where non-motile sperm nuclei are conveyed directly by a siphoning pollen tube), cycad and ginkgo pollen tubes act as branched, haustorial nutritive anchors. They eventually rupture in the pollen chamber to release **massive, multi-flagellated motile sperm** that actively swim through archegonial fluid to fertilize the egg.\n3. **Butyric Acid in Ginkgo Seeds**: Female ginkgo seed fleshy outer integument layers produce pungent, vomit-smelling **butyric acid**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p28_0.jpeg",
        "imageDescription": "Ginkgo biloba foliage showing dichotomous fan leaves and mature dioecious seeds with fleshy sarcotesta.",
        "citation": "BOT 1121 Lec 11, Slide 28",
        "tags": ["ginkgo", "cycads", "motile-sperm", "dioecious"]
    },
    {
        "id": "bot-1121-m2-c10",
        "front": "What anatomical adaptations allow Conifers (Pinophyta) to dominate cold, arid, high-latitude, and high-altitude boreal biomes?",
        "hint": "Analyze leaf cross-sectional anatomy: epidermis, hypodermis, stomata, mesophyll, and resin canals.",
        "back": "Xeromorphic and cold adaptations of Conifer needles:\n\n• **Thick Cuticle & Heavy Epidermis**: Minimizes non-stomatal cuticular transpiration.\n• **Sunken Stomata**: Stomatal pores are sunken into crypts filled with wax plugs to increase boundary layer resistance.\n• **Pectinate / Plicate Mesophyll**: Cells with deeply folded walls maximize internal surface area for CO2 absorption within a compact leaf volume.\n• **Resin Canals**: Antiseptic, terpene-rich resin deters herbivores and seals winter freeze-thaw injuries.\n• **Tracheids with Torus-Margo Pits**: Narrow tracheids resist cavitation and prevent air embolisms from spreading under severe freeze-thaw cycles.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p35_0.jpeg",
        "imageDescription": "Pinus needle transverse section showing sunken stomata, plicate mesophyll, resin ducts, endodermis, and transfusion tissue.",
        "citation": "BOT 1121 Lec 11, Slide 35",
        "tags": ["conifers", "pinus", "xeromorphic", "tracheids", "resin"]
    },

    # ==========================================
    # LECTURE 12: Angiosperms I — Flowers (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c11",
        "front": "Name the four concentric floral whorls of a complete flower from outermost to innermost, and state the collective term and function of each.",
        "hint": "Start with the protective green layer, move to the attractive colorful petals, the male organ, and the central female organ.",
        "back": "The 4 Concentric Floral Whorls:\n\n1. **Whorl 1: Calyx (Sepals)** — Outermost sterile whorl; protects floral bud before opening.\n2. **Whorl 2: Corolla (Petals)** — Inner sterile whorl; visually attracts specific pollinators.\n   *(Calyx + Corolla collectively = **Perianth**; when indistinguishable = **Tepals**)*.\n3. **Whorl 3: Androecium (Stamens)** — Male fertile whorl; each stamen consists of a filament and an anther with 4 pollen sacs (microsporangia).\n4. **Whorl 4: Gynoecium (Carpels/Pistil)** — Innermost female fertile whorl; consists of stigma, style, and ovary enclosing ovules.",
        "image": "images/bot-1121-flowers/fig_9_3_flower_anatomy_four_whorls.jpg",
        "imageDescription": "Schematic diagram of complete flower exhibiting four concentric whorls: calyx, corolla, androecium, and gynoecium.",
        "citation": "BOT 1121 Lec 12, Slide 5",
        "tags": ["flowers", "whorls", "calyx", "corolla", "androecium", "gynoecium"]
    },
    {
        "id": "bot-1121-m2-c12",
        "front": "Distinguish between connation and adnation in floral organ fusion, and provide an anatomical example of each.",
        "hint": "One describes fusion of like organs within the same whorl; the other describes fusion between different whorls.",
        "back": "Fusion terms in floral morphology:\n\n• **Connation**: Fusion of members of the **same whorl** (like parts fused).\n  - *Example*: Petals fused into a floral tube (sympetaly), or carpels fused into a compound syncarpous pistil (e.g., tomato or bell pepper with fused carpel walls).\n\n• **Adnation**: Fusion of members of **different whorls** (unlike parts fused).\n  - *Example*: Stamens fused to petals (epipetalous stamens in mints/Lamiaceae and snapdragons), or calyx/corolla/stamen bases fused with ovary wall in epigynous flowers.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p12_1.jpeg",
        "imageDescription": "Diagram showing fusion patterns: connate sympetalous corolla vs adnate epipetalous stamens.",
        "citation": "BOT 1121 Lec 12, Slide 12",
        "tags": ["flowers", "connation", "adnation", "floral-fusion"]
    },
    {
        "id": "bot-1121-m2-c13",
        "front": "Compare hypogynous, perigynous, and epigynous floral architectures with respect to ovary insertion and receptacle geometry.",
        "hint": "Identify where the perianth and stamens insert relative to the ovary: below, around on a hypanthium, or above.",
        "back": "Ovary Insertion & Floral Architecture:\n\n1. **Hypogynous (Superior Ovary)**:\n   - Sepals, petals, and stamens insert on the receptacle **below** the ovary base. The ovary sits free and above.\n2. **Perigynous (Superior Ovary with Hypanthium)**:\n   - A cup-like floral tube (**hypanthium**) formed by fused bases of calyx, corolla, and stamens surrounds the ovary, but the ovary is **not fused** to the hypanthium wall (e.g., cherry, rose, peach).\n3. **Epigynous (Inferior Ovary)**:\n   - Receptacle or hypanthium is completely fused to the ovary wall; sepals, petals, and stamens appear to arise from the **top** of the ovary (e.g., apple, squash, cucumber).",
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Comparative diagram illustrating hypogynous (superior), perigynous (superior with hypanthium), and epigynous (inferior) ovary positions.",
        "citation": "BOT 1121 Lec 12, Slide 28",
        "tags": ["flowers", "superior-ovary", "inferior-ovary", "hypogynous", "epigynous", "hypanthium"]
    },
    {
        "id": "bot-1121-m2-c14",
        "front": "Clarify the precise taxonomic differences between: Complete vs Incomplete, and Perfect vs Imperfect flowers.",
        "hint": "One classification depends on all 4 whorls being present; the other depends strictly on reproductive functionality (male + female).",
        "back": "Precise floral completeness & sexuality definitions:\n\n• **Complete**: Possesses **all 4 floral whorls** (calyx, corolla, stamens, and carpels).\n• **Incomplete**: Lacks **one or more whorls** (e.g., wind-pollinated oak flowers lacking petals and sepals).\n\n• **Perfect (Bisexual / Hermaphroditic)**:\n  - Possesses **both fertile whorls** (stamens AND carpels present and functional).\n• **Imperfect (Unisexual)**:\n  - Lacks one fertile whorl:\n    - **Staminate**: Possesses stamens but lacks carpels (male flower).\n    - **Pistillate / Carpellate**: Possesses carpels but lacks stamens (female flower).\n\n*Note*: All complete flowers are necessarily perfect, but not all perfect flowers are complete (e.g., a flower with stamens and carpels that lacks petals).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p16_0.jpeg",
        "imageDescription": "Morphological chart differentiating complete vs incomplete, and staminate vs pistillate imperfect flowers.",
        "citation": "BOT 1121 Lec 12, Slide 16",
        "tags": ["flowers", "complete", "incomplete", "perfect", "imperfect"]
    },
    {
        "id": "bot-1121-m2-c15",
        "front": "Contrast the pollination syndromes of Bee-pollinated (Melittophily) vs Bird-pollinated (Ornithophily) vs Wind-pollinated (Anemophily) flowers.",
        "hint": "Analyze floral colors, nectar volume, scent, landing platform, and pollen physical properties.",
        "back": "Pollination Syndromes Comparative Breakdown:\n\n• **Bee-Pollinated (Melittophily)**:\n  - Color: Yellow, blue, purple, or UV nectar guides (bees cannot see pure red).\n  - Scent: Sweet, fresh floral fragrance.\n  - Architecture: Zygomorphic (bilateral symmetry) with landing platform; pollen sticky and sculptured.\n\n• **Bird-Pollinated (Ornithophily — Hummingbirds)**:\n  - Color: Bright scarlet red, tubular or pendant.\n  - Scent: Absent (birds have minimal olfactory sense).\n  - Reward: Abundant, dilute, high-volume nectar deeply sequestered in floral spurs.\n\n• **Wind-Pollinated (Anemophily — Grasses, Oaks)**:\n  - Flowers: Highly reduced, green or brown, no petals, no nectar, no scent.\n  - Organs: Enormous feathery stigmas to catch pollen; pendulous anthers on long filaments producing copious, lightweight, smooth pollen grains.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p38_0.jpeg",
        "imageDescription": "Pollination syndromes showing floral color, petal shape, and structural adaptations for insects, birds, and wind.",
        "citation": "BOT 1121 Lec 12, Slide 38",
        "tags": ["pollination", "syndromes", "melittophily", "ornithophily", "anemophily"]
    },

    # ==========================================
    # LECTURE 13: Angiosperms II — Fruits & Seeds (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c16",
        "front": "What botanical structure gives rise to a true fruit, and what are the three distinct histological layers of the pericarp?",
        "hint": "Consider the post-fertilization fate of the ovary wall, from outer skin to middle flesh to inner pit/lining.",
        "back": "A botanical fruit develops from the **mature, ripened ovary wall** (plus associated floral tissues in accessory fruits).\n\n• **The 3 Layers of the Pericarp**:\n  1. **Exocarp**: Outermost skin or rind of the fruit.\n  2. **Mesocarp**: Middle layer; often thick, fleshy, and succulent (e.g., peach flesh) or fibrous (e.g., coconut husk).\n  3. **Endocarp**: Innermost layer surrounding the seeds; can be stony and lignified (e.g., peach/cherry pit), membranous (e.g., apple core), or succulent with juice sacs (e.g., citrus pulp).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p2_0.jpeg",
        "imageDescription": "Peach fruit longitudinal section demonstrating the three distinct layers of the pericarp: exocarp, fleshy mesocarp, and stony endocarp.",
        "citation": "BOT 1121 Lec 13, Slide 2",
        "tags": ["fruits", "pericarp", "exocarp", "mesocarp", "endocarp"]
    },
    {
        "id": "bot-1121-m2-c17",
        "front": "Distinguish between a Drupe, a true Berry, and a Pome using precise pericarp anatomy and floral origin.",
        "hint": "Analyze the consistency of the endocarp and whether the ovary was superior or inferior with hypanthium.",
        "back": "Comparative Fleshy Fruit Types:\n\n• **Drupe (Stone Fruit — Peach, Cherry, Olive)**:\n  - Derived from a single carpel; fleshy mesocarp, but **stony, lignified endocarp (pit)** enclosing a single seed.\n\n• **True Berry (Tomato, Grape, Blueberry)**:\n  - Derived from a compound ovary; **entire pericarp (mesocarp and endocarp) is soft, fleshy, and succulent**, enclosing one or many seeds without a stony pit.\n\n• **Pome (Apple, Pear)**:\n  - Derived from an **inferior ovary surrounded by a fleshy hypanthium** (accessory fruit). The edible flesh is derived from fused hypanthium/receptacle tissue; the true pericarp forms the leathery or cartilaginous core.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p5_0.jpeg",
        "imageDescription": "Anatomical comparison of drupe (peach pit), berry (tomato succulent wall), and pome (apple core vs hypanthium).",
        "citation": "BOT 1121 Lec 13, Slide 5",
        "tags": ["fruits", "drupe", "berry", "pome", "accessory-fruit"]
    },
    {
        "id": "bot-1121-m2-c18",
        "front": "Differentiate between an Aggregate fruit and a Multiple fruit based on floral morphology, providing a classic botanical example of each.",
        "hint": "Count the number of flowers involved: one flower with many separate carpels vs an entire inflorescence of many flowers.",
        "back": "Aggregate vs Multiple Fruits:\n\n• **Aggregate Fruit**:\n  - Develops from a **single flower** that contains **multiple separate (apocarpous) carpels** on a common receptacle.\n  - *Example*: Raspberry/Blackberry (aggregate of drupelets), Strawberry (aggregate of achenes on an enlarged red accessory receptacle).\n\n• **Multiple Fruit**:\n  - Develops from an **entire inflorescence of many separate flowers** whose individual ovaries fuse together into a single cohesive structure during maturation.\n  - *Example*: Pineapple (*Ananas comosus*), Fig (*Ficus* syconium), Mulberry, Jackfruit.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p13_2.jpeg",
        "imageDescription": "Diagram contrasting aggregate fruit development (single flower with multiple carpels) vs multiple fruit development (dense inflorescence of multiple flowers).",
        "citation": "BOT 1121 Lec 13, Slide 13",
        "tags": ["fruits", "aggregate", "multiple", "inflorescence", "apocarpous"]
    },
    {
        "id": "bot-1121-m2-c19",
        "front": "Why is a strawberry botanically classified as an 'accessory aggregate of achenes' rather than a true berry?",
        "hint": "What is the red sweet edible part derived from, and what are the tiny specks on its surface?",
        "back": "Strawberry Botanical Breakdown (*Fragaria*):\n\n1. **Achenes**: The tiny yellow/brown 'specks' on the surface are individual dry, indehiscent fruits called **achenes**, each containing a single seed derived from a separate carpel.\n2. **Accessory Receptacle**: The red, sweet, succulent flesh is **not pericarp**; it is the **swollen receptacle** of the single flower that expanded under the stimulation of auxin produced by the developing achenes.\n3. **Conclusion**: Because the edible part is non-ovarian tissue and the fruits are numerous separate carpels from one flower, it is an **accessory aggregate of achenes**, completely distinct from a true botanical berry.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p15_0.jpeg",
        "imageDescription": "Macro photograph and anatomical diagram of strawberry illustrating individual surface achenes and enlarged central receptacle.",
        "citation": "BOT 1121 Lec 13, Slide 15",
        "tags": ["fruits", "strawberry", "achenes", "accessory-fruit", "receptacle"]
    },
    {
        "id": "bot-1121-m2-c20",
        "front": "What are the major anatomical parts of an angiosperm seed, and how does the ploidy of each tissue reflect its genetic origin?",
        "hint": "Analyze the maternal seed coat, the nutritive reserve, and the embryo.",
        "back": "Angiosperm Seed Components & Ploidy Levels:\n\n1. **Seed Coat (Testa)** — **Diploid (2n)** maternal tissue derived from the integuments of the parent sporophyte.\n2. **Endosperm** — **Triploid (3n)** nutritive tissue formed by double fertilization (1 sperm nucleus [n] + 2 maternal polar nuclei [n+n]). Absorbed into cotyledons in non-endospermic seeds (e.g., beans) or retained (e.g., corn, castor bean).\n3. **Embryo** — **Diploid (2n)** new sporophyte generation (1 egg [n] + 1 sperm [n]); consists of epicotyl (plumule), hypocotyl, radicle (embryonic root), and 1 or 2 cotyledons.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p25_1.jpeg",
        "imageDescription": "Longitudinal section of monocot and eudicot seeds detailing seed coat, endosperm, cotyledon, epicotyl, and radicle.",
        "citation": "BOT 1121 Lec 13, Slide 25",
        "tags": ["seeds", "endosperm", "cotyledon", "radicle", "ploidy"]
    },

    # ==========================================
    # LECTURE 14: Fig Biology & Ficus Mutualisms (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c21",
        "front": "What is a syconium, what is the function of the ostiole, and how does this inflorescence architecture dictate fig pollination?",
        "hint": "Visualize an inverted fleshy stem housing hundreds of tiny flowers inside with a single bract-lined opening at the apex.",
        "back": "Fig Inflorescence Architecture (*Ficus*):\n\n• **Syconium**: An urn-shaped, fleshy, inverted receptacle/stem that encloses hundreds to thousands of microscopic, unisexual flowers inside an internal cavity.\n• **Ostiole**: A tiny apical pore tightly closed by overlapping scales/bracts that serves as the **only entrance** into the syconium.\n• **Pollination Consequence**: Flowers are inaccessible to generalist wind or insect pollinators. Only microscopic, highly co-evolved **fig wasps (Agaonidae)** can squeeze past the ostiolar scales to enter the cavity and achieve pollination.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p10_0.jpeg",
        "imageDescription": "Longitudinal bisection of a Ficus syconium showing ostiole at the apex, internal cavity, and hundreds of lining florets.",
        "citation": "BOT 1121 Lec 14, Slide 10",
        "tags": ["figs", "ficus", "syconium", "ostiole", "agaonidae"]
    },
    {
        "id": "bot-1121-m2-c22",
        "front": "Outline the obligate mutualistic life cycle of the female fig wasp (Blastophaga psenes) upon entering a receptive syconium.",
        "hint": "Consider wings and antennae detachment, oviposition attempts, pollen deposition, and wasp death.",
        "back": "Life Cycle of Female Foundress Wasp (*Blastophaga psenes*):\n\n1. **Entry**: Attracted by volatile terpenes, the female foundress squeezes through ostiolar scales, usually snapping off her wings and antennae.\n2. **Pollination & Oviposition**: She walks over flowers, depositing pollen carried in thoracic pockets onto stigmas. She probes flower styles with her ovipositor:\n   - **Short-styled flowers**: Ovipositor reaches ovary -> lays egg -> flower develops into a gall nursery for wasp larvae.\n   - **Long-styled flowers**: Ovipositor cannot reach ovary -> cannot lay egg -> flower is cross-pollinated and produces a viable seed.\n3. **Death**: Spent foundress dies inside syconium and is broken down by the plant protease enzyme **ficin**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p18_0.jpeg",
        "imageDescription": "Diagram of Blastophaga psenes foundress wasp penetrating ostiole, ovipositing in short-styled florets, and pollinating long-styled florets.",
        "citation": "BOT 1121 Lec 14, Slide 18",
        "tags": ["figs", "blastophaga", "mutualism", "ovipositor", "ficin"]
    },
    {
        "id": "bot-1121-m2-c23",
        "front": "In functionally dioecious figs like Ficus carica, distinguish between a 'Caprifig' (male) and an 'Edible Fig' (female).",
        "hint": "Which tree produces pollen and wasp offspring, and which produces only seeds and sweet edible fruit?",
        "back": "Caprifigs vs Edible Figs (*Ficus carica*):\n\n• **Caprifig (Functionally Male Tree)**:\n  - Contains **short-styled female flowers** and **staminate (male) flowers** producing pollen.\n  - Acts as a **wasp nursery**: wasps successfully oviposit in all flowers. Emerging wasps pick up pollen from mature anthers near the ostiole.\n  - Syconia are woody, non-palatable, and dry.\n\n• **Edible Fig (Functionally Female Tree)**:\n  - Contains **only long-styled female flowers** and **no staminate flowers**.\n  - Wasps enter, cross-pollinate the flowers, but cannot oviposit because styles exceed ovipositor length.\n  - Flowers develop into true seeds surrounded by fleshy, sugar-rich syconium tissues consumed by humans and wildlife.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p26_0.jpeg",
        "imageDescription": "Comparison of Caprifig floret architecture (short styles allowing galling) vs Edible Fig floret architecture (long styles preventing wasp reproduction).",
        "citation": "BOT 1121 Lec 14, Slide 25",
        "tags": ["figs", "ficus-carica", "caprifig", "dioecy", "gall-flowers"]
    },
    {
        "id": "bot-1121-m2-c24",
        "front": "What role do wingless male fig wasps play inside the maturing syconium prior to female emergence?",
        "hint": "Analyze male morphology: why lack wings and eyes? What do they do to galls, each other, and the syconium wall?",
        "back": "Role of Wingless Male Fig Wasps:\n\n1. **Early Emergence**: Male wasps hatch first from gall flowers. They are wingless, blind, and possess powerful jaws.\n2. **Mating**: They locate galls containing unhatched females, chew a small hole through the gall wall, and insert their elongate abdomen to mate with females.\n3. **Tunneling Escape Route**: After fertilizing females, males chew escape tunnels through the thick ostiolar wall or syconium tissue to allow mated females (laden with pollen) to exit.\n4. **Death**: Males never leave the fig; having spent all metabolic energy mating and chewing escape channels, they die inside the syconium.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p20_0.jpeg",
        "imageDescription": "Micrograph of wingless male fig wasp chewing through syconium gall wall to mate with enclosed female.",
        "citation": "BOT 1121 Lec 14, Slide 20",
        "tags": ["figs", "wasps", "male-wasps", "chewing", "escape-tunnel"]
    },
    {
        "id": "bot-1121-m2-c25",
        "front": "What is parthenocarpy, and how does the commercial 'Black Mission' fig produce ripe fruit without wasp pollination?",
        "hint": "Does fruit ripening strictly require seed fertilization in all cultivated varieties?",
        "back": "**Parthenocarpy** is the development and ripening of fruit **without fertilization or seed formation**.\n\n• **Black Mission Fig**: Many commercial varieties of *Ficus carica* are selected genetic mutants that exhibit vegetative parthenocarpy.\n• **Mechanism**: Hormonal surges (auxin and gibberellins) in the syconium receptacle trigger fleshy swelling, sugar accumulation, and softening of the syconium wall **in the complete absence of wasp visitation or fertilization**.\n• **Commercial Value**: Allows cultivation of figs in regions lacking the *Blastophaga psenes* wasp and produces seedless, insect-free fruit for commercial markets.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p31_2.jpeg",
        "imageDescription": "Ripe Black Mission parthenocarpic fig split open showing sweet fleshy interior without insect remnants or fertilized seeds.",
        "citation": "BOT 1121 Lec 14, Slide 31",
        "tags": ["figs", "parthenocarpy", "black-mission", "hormones"]
    },

    # ==========================================
    # LECTURE 15: Water Transport (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c26",
        "front": "State the water potential equation (Ψ = Ψs + Ψp) and explain the biological meaning and typical sign (+ or -) of each component.",
        "hint": "Water always moves spontaneously from higher (less negative) to lower (more negative) water potential.",
        "back": "Water Potential Equation: **Ψ = Ψs + Ψp** (measured in Megapascals, MPa)\n\n• **Ψ (Total Water Potential)**: Determines direction of water movement (flows spontaneously from higher Ψ -> lower Ψ).\n• **Ψs (Solute / Osmotic Potential)**:\n  - Proportional to the number of dissolved solute molecules. Pure water at standard pressure = 0 MPa. Adding solutes **always lowers Ψs (strictly ≤ 0)**.\n• **Ψp (Pressure Potential)**:\n  - Hydrostatic pressure exerted on cell contents.\n  - In living cells, turgor pressure pressing outward against cell walls is **positive (+)**.\n  - In xylem conduits undergoing transpiration, tension is **negative (-)**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p6_0.jpeg",
        "imageDescription": "Diagram of plant cell water potential showing osmotic solute potential (Ψs) balanced by turgor pressure potential (Ψp).",
        "citation": "BOT 1121 Lec 15, Slide 5",
        "tags": ["water-transport", "water-potential", "solute-potential", "turgor"]
    },
    {
        "id": "bot-1121-m2-c27",
        "front": "Summarize the Cohesion-Tension Theory of sap ascent: How does solar energy pull water hundreds of feet up a redwood tree without metabolic pumping in the xylem?",
        "hint": "Trace the tension generated by leaf transpiration down the continuous water columns held together by hydrogen bonding.",
        "back": "The **Cohesion-Tension Theory**:\n\n1. **Transpiration**: Solar evaporation of water through open stomata into dry air generates a powerful meniscus curvature and massive negative hydrostatic tension (e.g., -1.5 to -3.0 MPa) in mesophyll cell wall capillary pores.\n2. **Tension Transmission**: This negative pressure pulls water out of leaf xylem tracheary elements.\n3. **Cohesion & Adhesion**:\n   - **Cohesion**: High hydrogen bonding between water molecules gives water immense tensile strength, maintaining unbroken, continuous water columns up the stem.\n   - **Adhesion**: Hydrogen bonding between water molecules and hydrophilic xylem cell walls (cellulose, lignin) prevents gravitational collapse.\n4. **Passive Driving Force**: The entire process is driven by **solar energy (evaporation)**; the plant expends zero metabolic ATP to hoist xylem sap.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p12_0.jpeg",
        "imageDescription": "Cohesion-Tension diagram illustrating water potential gradient from moist soil (-0.1 MPa) through trunk xylem (-0.8 MPa) to dry air (-100 MPa).",
        "citation": "BOT 1121 Lec 15, Slide 12",
        "tags": ["water-transport", "cohesion-tension", "transpiration", "xylem"]
    },
    {
        "id": "bot-1121-m2-c28",
        "front": "Trace the three radial pathways water takes from root epidermis to the stele, and explain why the Casparian strip forces all water into the symplast.",
        "hint": "Distinguish between apoplast (cell walls), symplast (cytoplasm via plasmodesmata), and transmembrane pathways.",
        "back": "Radial Water Movement in Roots:\n\n1. **Apoplastic Pathway**: Water diffuses through continuous, non-living cell walls and intercellular spaces without crossing plasma membranes.\n2. **Symplastic Pathway**: Water crosses a plasma membrane once and moves from cell to cell through living cytoplasm interconnected by **plasmodesmata**.\n3. **Transmembrane Pathway**: Water crosses multiple plasma membranes and tonoplasts directly via **aquaporin** protein channels.\n\n• **The Casparian Strip**:\n  - A suberized and lignified impermeable band embedded in radial and transverse walls of **endodermal cells**.\n  - Blocks the apoplastic route completely, forcing all water and dissolved mineral ions to pass through a selectively permeable endodermal plasma membrane, preventing toxic ion entry and preventing backflow.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p18_0.jpeg",
        "imageDescription": "Cross section of root cortex and endodermis illustrating apoplastic vs symplastic flow and the Casparian strip checkpoint.",
        "citation": "BOT 1121 Lec 15, Slide 18",
        "tags": ["water-transport", "roots", "casparian-strip", "endodermis", "apoplast", "symplast"]
    },
    {
        "id": "bot-1121-m2-c29",
        "front": "Explain the biochemical and osmotic mechanism governing the opening and closing of stomatal guard cells.",
        "hint": "Focus on blue-light activation of H+-ATPase proton pumps, potassium (K+) influx, water uptake, and asymmetric cell wall thickening.",
        "back": "Mechanism of Stomatal Guard Cell Regulation:\n\n• **Stomatal Opening (Daylight / Blue Light)**:\n  1. Active transport: Light activates plasma membrane **H+-ATPase proton pumps**, driving H+ out of guard cells (hyperpolarizing membrane).\n  2. Influx: Voltage-gated channels open, driving massive influx of **Potassium ions (K+)** and anions (Cl-, malate2-).\n  3. Osmosis: High solute concentration drops guard cell **Ψs**, drawing water in by osmosis.\n  4. Turgor deformation: Guard cells swell. Because inner cell walls adjacent to pore are thick and radially banded by cellulose microfibrils, they bow outward, opening the stomatal aperture.\n\n• **Stomatal Closing (Drought / Darkness / ABA)**:\n  - Abscisic acid (ABA) triggers K+ and anion efflux -> Ψs rises -> water exits by osmosis -> guard cells lose turgor and become flaccid, sealing the pore.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p22_0.jpeg",
        "imageDescription": "Stomatal guard cell opening mechanism: H+ pumping, K+ accumulation, osmotic swelling, and pore expansion.",
        "citation": "BOT 1121 Lec 15, Slide 22",
        "tags": ["stomata", "guard-cells", "potassium", "turgor", "abscisic-acid"]
    },
    {
        "id": "bot-1121-m2-c30",
        "front": "What is xylem cavitation, what triggers it, and how does air-seeding create a non-functional embolism in tracheary elements?",
        "hint": "What happens when xylem water tension becomes so extreme that dissolved gases break water column cohesion?",
        "back": "Xylem Cavitation & Embolism:\n\n• **Cavitation**: The sudden rupture of a water column under extreme negative hydrostatic tension, creating an expanding vapor- or air-filled bubble.\n• **Air-Seeding Mechanism**:\n  - Under severe drought stress or freezing/thawing, the pressure difference across pit membranes exceeds surface tension, sucking an air bubble through a pit pore from an adjacent empty tracheary element into a functional one.\n• **Embolism & Functional Loss**:\n  - The expanding air bubble breaks water continuity (embolism). Water can no longer be pulled through that conduit.\n• **Mitigation**: Plants bypass embolized vessels through pit membranes to adjacent intact vessels, and can repair embolisms overnight via positive **root pressure**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p26_0.jpeg",
        "imageDescription": "Diagram of cavitation: negative pressure ruptures water column, forming an air bubble that blocks sap transport.",
        "citation": "BOT 1121 Lec 15, Slide 26",
        "tags": ["water-transport", "cavitation", "embolism", "xylem", "pit-membrane"]
    },

    # ==========================================
    # LECTURE 16: Sugar Transport (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c31",
        "front": "State the Münch Pressure-Flow (Bulk Flow) Hypothesis: What physical force drives phloem sap from sugar source to sugar sink?",
        "hint": "Analyze how osmotic sugar loading and unloading generate a hydrostatic turgor pressure gradient (ΔΨp) between source and sink.",
        "back": "The **Münch Pressure-Flow Hypothesis**:\n\n1. **Phloem Loading at Source (Leaves)**:\n   - Photosynthetically active mesophyll cells load high concentrations of sucrose into sieve tube elements (STEs).\n   - High solute concentration drastically lowers sieve tube **Ψs**, causing water to enter from adjacent xylem by osmosis.\n   - Water entry generates high **positive turgor pressure (Ψp)** at the source.\n2. **Bulk Flow Through Sieve Tubes**:\n   - Sap flows en masse through open sieve plate pores along a hydrostatic pressure gradient toward regions of lower pressure.\n3. **Phloem Unloading at Sink (Roots, Tubers, Developing Fruits)**:\n   - Sucrose is unloaded from STEs into sink cells and metabolized or converted to insoluble starch.\n   - Sieve tube **Ψs** rises, causing water to exit by osmosis back into the xylem, resulting in low **turgor pressure (Ψp)** at the sink.\n4. **Driving Force**: Sap moves by **bulk hydrostatic pressure gradient (ΔΨp)**, NOT simple diffusion.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p14_0.jpeg",
        "imageDescription": "Münch pressure-flow schematic: active phloem loading at leaf source generating high turgor, driving bulk sap flow to low-pressure root sink.",
        "citation": "BOT 1121 Lec 16, Slide 14",
        "tags": ["sugar-transport", "phloem", "pressure-flow", "bulk-flow", "source-sink"]
    },
    {
        "id": "bot-1121-m2-c32",
        "front": "Contrast the cytology of mature Sieve Tube Elements with Vessel Elements: Which is living, which is dead, and what organelles do they retain?",
        "hint": "One conducts sugar sap and must maintain a living plasma membrane; the other conducts water under tension as a dead hollow tube.",
        "back": "Cytological Comparison of Transport Conduits:\n\n• **Sieve Tube Elements (STEs — Phloem)**:\n  - **Living at maturity**, bounded by an intact, selectively permeable plasma membrane essential for maintaining osmotic turgor.\n  - To minimize drag during bulk flow, STEs undergo selective autolysis: they **lack nuclei, vacuoles, ribosomes, and Golgi**, retaining only a thin peripheral cytoplasm with modified plastids, smooth ER, and mitochondria.\n\n• **Vessel Elements (Xylem)**:\n  - **Dead at functional maturity**, undergoing complete programmed cell death (PCD).\n  - Completely hollow, rigid, lignified tubes with perforated end walls, specialized for high-volume passive water conduction under negative tension.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p6_0.jpeg",
        "imageDescription": "Cellular anatomy comparing living sieve tube element with its companion cell vs dead, lignified vessel element.",
        "citation": "BOT 1121 Lec 16, Slide 6",
        "tags": ["phloem", "sieve-tube", "vessel-element", "cytology"]
    },
    {
        "id": "bot-1121-m2-c33",
        "front": "Explain the obligate relationship between a Sieve Tube Element and its Companion Cell, and describe how P-protein prevents sap bleeding upon wounding.",
        "hint": "Why does the companion cell possess a dense nucleus and abundant mitochondria? What plugs damaged sieve plates?",
        "back": "Sieve Tube Element — Companion Cell Complex & Wounding Defense:\n\n• **Metabolic Life Support**:\n  - Derived from the same mother procambial cell, the companion cell retains a large nucleus, dense ribosomes, and abundant mitochondria.\n  - It provides all transcriptional, translational, and ATP energy support to the enucleated STE via numerous branched **plasmodesmata**.\n\n• **P-Protein (Phloem Protein) & Callose Defense**:\n  - When a stem is bruised or severed by herbivores, pressurized sieve tubes risk catastrophic sap loss ('bleeding').\n  - High pressure surge sweeps **P-protein filaments** into sieve plate pores, instantly forming a physical plug. Over subsequent hours, the plant synthesizes **callose** (a β-1,3-glucan polymer) around pores to permanently seal the wounded conduit.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p8_0.jpeg",
        "imageDescription": "High-magnification transmission electron micrograph of sieve plate with P-protein slime plug preventing sap loss.",
        "citation": "BOT 1121 Lec 16, Slide 8",
        "tags": ["phloem", "companion-cell", "p-protein", "callose", "wounding"]
    },
    {
        "id": "bot-1121-m2-c34",
        "front": "Detail the active apoplastic phloem loading mechanism: What proteins are required, and why is ATP necessary to load sucrose against its concentration gradient?",
        "hint": "Consider the plasma membrane H+-ATPase proton pump and the secondary active sucrose-H+ symporter.",
        "back": "Active Apoplastic Phloem Loading Mechanism:\n\n1. **Primary Active Transport (Proton Pumping)**:\n   - Companion cell plasma membrane **H+-ATPase pumps** hydrolyze ATP to pump protons (H+) into the apoplastic cell wall space, creating a steep electrical and pH gradient.\n2. **Secondary Active Transport (Sucrose-H+ Symport)**:\n   - Sucrose from mesophyll cell walls enters companion cells and STEs via a **Sucrose/H+ symporter protein** (SUC/SUT).\n   - The downhill movement of H+ back into the cytoplasm drives the uphill transport of sucrose against its steep concentration gradient.\n3. **Result**: Phloem sap accumulates sucrose concentrations 2–3 times higher than surrounding mesophyll cells, driving osmotic water influx and creating high turgor pressure.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p24_0.jpeg",
        "imageDescription": "Molecular diagram of phloem loading showing H+-ATPase pump hydrolyzing ATP and sucrose/H+ symporter loading sucrose into companion cell.",
        "citation": "BOT 1121 Lec 16, Slide 24",
        "tags": ["phloem-loading", "apoplast", "atp-ase", "symport", "sucrose"]
    },
    {
        "id": "bot-1121-m2-c35",
        "front": "Define a 'source' versus a 'sink' in plant physiology, and explain how a single organ (such as a potato tuber or sugar beet) can switch roles seasonally.",
        "hint": "Analyze whether the organ produces or exports sugars versus consumes or stores sugars in spring versus autumn.",
        "back": "Source vs Sink Dynamics:\n\n• **Source**: Any organ that produces more photoassimilates than it requires for its own metabolism and **exports excess sugar** (e.g., mature photosynthetic leaves, germinating cotyledons).\n• **Sink**: Any non-photosynthetic or actively growing organ that **consumes or stores sugar** (e.g., developing roots, shoot apical meristems, flowers, ripening fruits, storage tubers).\n\n• **Seasonal Role Reversal (e.g., Potato Tuber / Carrot)**:\n  - **Late Summer / Autumn (Sink)**: Mature leaves act as sources; the tuber acts as a sink, importing sucrose and synthesizing storage starch.\n  - **Early Spring (Source)**: Before new leaves expand, the overwintered tuber mobilizes stored starch back into sucrose and exports it upward to fuel sprouting shoots and expanding spring leaves.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p36_0.jpeg",
        "imageDescription": "Seasonal shift diagram showing sugar beet/tuber functioning as sugar storage sink in autumn, then converting to primary sugar source in spring.",
        "citation": "BOT 1121 Lec 16, Slide 36",
        "tags": ["source-sink", "phloem", "tuber", "storage", "seasonality"]
    },

    # ==========================================
    # LECTURE 17: Photosynthesis Part 1 (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c36",
        "front": "Where specifically do the light-dependent reactions of photosynthesis occur inside the chloroplast, and what are the essential input reactants and final output products?",
        "hint": "Focus on the thylakoid membrane, water, light energy, oxygen, ATP, and NADPH.",
        "back": "Light-Dependent Reactions Overview:\n\n• **Subcellular Site**: The **thylakoid membranes** (organized into stacked granal lamellae and unstacked stromal lamellae) and **thylakoid lumen** inside the chloroplast.\n• **Inputs**:\n  1. **Photons of light energy** (absorbed primarily by chlorophylls *a*, *b*, and carotenoids).\n  2. **Water (H2O)** (source of electrons).\n  3. **ADP + Pi** (adenosine diphosphate and inorganic phosphate).\n  4. **NADP+** (oxidized electron carrier).\n• **Outputs**:\n  1. **Oxygen gas (O2)** (byproduct released from photolysis of water).\n  2. **ATP** (chemical energy generated via photophosphorylation).\n  3. **NADPH** (high-energy reducing power required for the Calvin Cycle).",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p4_0.jpeg2000",
        "imageDescription": "Chloroplast thylakoid membrane architecture showing granum stacks, lumen, and stroma where light reactions occur.",
        "citation": "BOT 1121 Lec 17, Slide 4",
        "tags": ["photosynthesis", "light-reactions", "thylakoid", "atp", "nadph"]
    },
    {
        "id": "bot-1121-m2-c37",
        "front": "Describe the Z-scheme of noncyclic electron flow: Trace an electron from the photolysis of water at Photosystem II to the reduction of NADP+ at Photosystem I.",
        "hint": "Follow the sequence: H2O -> P680 -> Plastoquinone -> Cytochrome b6f -> Plastocyanin -> P700 -> Ferredoxin -> NADP+ reductase.",
        "back": "The **Z-Scheme** (Noncyclic Electron Flow):\n\n1. **Photolysis at PSII (P680)**: Absorbed photons excite P680 reaction center chlorophyll. An electron is ejected to the primary electron acceptor (pheophytin). The oxidized P680+ extracts an electron from H2O via the Oxygen-Evolving Complex (Mn4CaO5 cluster):\n   `2 H2O -> 4 H+ + 4 e- + O2`.\n2. **Electron Transport Chain (ETC)**: Electrons pass through **Plastoquinone (PQ)** -> **Cytochrome b6f complex** (pumps protons into thylakoid lumen) -> **Plastocyanin (PC)** (copper-containing mobile carrier).\n3. **Photosystem I (P700)**: Light absorption re-excites electrons at P700, ejecting them to ferredoxin.\n4. **NADP+ Reductase**: Enzyme **Ferredoxin-NADP+ Reductase (FNR)** transfers electrons to NADP+ in the stroma:\n   `NADP+ + 2 e- + H+ -> NADPH`.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p28_0.jpeg",
        "imageDescription": "Z-scheme energy diagram plotting redox potential from water oxidation through PSII (P680), cytochrome b6f, PSI (P700), to NADPH.",
        "citation": "BOT 1121 Lec 17, Slide 28",
        "tags": ["photosynthesis", "z-scheme", "psii", "psi", "electron-transport"]
    },
    {
        "id": "bot-1121-m2-c38",
        "front": "How is the proton motive force established across the thylakoid membrane, and how does ATP Synthase exploit it to produce ATP?",
        "hint": "Identify the two sources of H+ accumulation in the lumen and the consumption of H+ in the stroma.",
        "back": "Proton Gradient & Photophosphorylation:\n\n• **Proton (H+) Accumulation in Thylakoid Lumen**:\n  1. **Photolysis of H2O**: Splitting water by the Oxygen-Evolving Complex releases 4 H+ directly into the thylakoid lumen per O2 formed.\n  2. **Q-Cycle via Cytochrome b6f**: Plastoquinone picks up protons from the stroma upon reduction and translocates them across into the lumen upon oxidation.\n  3. **Stroma H+ Depletion**: Reduction of NADP+ to NADPH consumes stromal protons.\n• **Result**: Steep electrochemical gradient (lumen pH ~4.5 vs stroma pH ~8.0, ΔpH ≈ 3.5 units).\n• **ATP Synthase (CF0-CF1 complex)**:\n  - Protons flow down their concentration gradient through CF0 channel, rotating the c-ring rotor and driving conformational changes in CF1 catalytic heads to synthesize **ATP from ADP + Pi**.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p34_0.jpeg2000",
        "imageDescription": "Thylakoid membrane cross section showing PSII, Cytochrome b6f, PSI, and ATP Synthase powered by lumenal proton accumulation.",
        "citation": "BOT 1121 Lec 17, Slide 34",
        "tags": ["photosynthesis", "proton-gradient", "atp-synthase", "photophosphorylation"]
    },
    {
        "id": "bot-1121-m2-c39",
        "front": "Why is the reaction center of Photosystem II termed P680 and Photosystem I termed P700, and what are their primary functional roles?",
        "hint": "What do the numbers 680 and 700 represent in nanometers?",
        "back": "Photochemical Reaction Centers:\n\n• **P680 (Photosystem II)**:\n  - Specialized pair of chlorophyll *a* molecules with peak light absorption wavelength at **680 nm** (red light).\n  - **Function**: Powerful biological oxidizing agent (redox potential ~+1.25 V), strong enough to split water and strip away electrons to initiate noncyclic electron flow.\n\n• **P700 (Photosystem I)**:\n  - Specialized chlorophyll *a* dimer with peak light absorption wavelength at **700 nm** (far-red light).\n  - **Function**: Traps lower-energy photons to re-energize electrons to an exceptionally low redox potential (~-0.45 V), sufficient to reduce NADP+ to NADPH via ferredoxin.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p20_0.jpeg",
        "imageDescription": "Absorption spectra comparing chlorophyll a and b peak wavelengths with reaction centers P680 and P700.",
        "citation": "BOT 1121 Lec 17, Slide 20",
        "tags": ["photosynthesis", "p680", "p700", "chlorophyll", "reaction-center"]
    },
    {
        "id": "bot-1121-m2-c40",
        "front": "What is Cyclic Photophosphorylation, which photosystem does it involve, and why must a plant switch to cyclic electron flow?",
        "hint": "Does cyclic flow generate NADPH or split water? What does the Calvin Cycle require in a higher ATP:NADPH ratio?",
        "back": "Cyclic Photophosphorylation:\n\n• **Mechanism**:\n  - Involves **only Photosystem I (P700)**.\n  - Electrons ejected from P700 are transferred to ferredoxin, but instead of moving to NADP+ reductase, they are routed back to the **Cytochrome b6f complex** -> plastocyanin -> back to P700.\n• **Energy Yield**:\n  - Generates a proton gradient across the thylakoid lumen, driving **ATP synthesis**, but produces **NO NADPH** and **NO O2** (water is not split).\n• **Physiological Purpose**:\n  - The Calvin-Benson Cycle requires an ATP:NADPH stoichiometric ratio of **3:2** (or higher under stress), whereas linear electron flow produces roughly 1:1.\n  - Cyclic electron flow provides the supplemental ATP needed without over-accumulating reducing power, and protects photosynthetic machinery under high light stress.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p29_0.jpeg",
        "imageDescription": "Diagram of cyclic electron flow: ferredoxin cycling electrons back to cytochrome b6f and PSI, pumping H+ for ATP synthesis without NADPH formation.",
        "citation": "BOT 1121 Lec 17, Slide 29",
        "tags": ["photosynthesis", "cyclic-electron-flow", "psi", "atp", "photoprotection"]
    },

    # ==========================================
    # LECTURE 18: Photosynthesis Part 2 (5 cards)
    # ==========================================
    {
        "id": "bot-1121-m2-c41",
        "front": "Outline the three distinct phases of the Calvin-Benson Cycle, specifying the key substrate, enzyme, and energetic investment of each.",
        "hint": "1. Carbon fixation by RuBisCO; 2. Reduction of 3-PGA to G3P; 3. Regeneration of RuBP.",
        "back": "The Three Phases of the **Calvin-Benson Cycle** (in stroma):\n\n1. **Phase 1: Carbon Fixation**:\n   - Enzyme **RuBisCO** catalyzes carboxylation of 5-carbon **Ribulose-1,5-bisphosphate (RuBP)** with CO2, producing an unstable 6-carbon intermediate that immediately cleaves into two molecules of **3-Phosphoglycerate (3-PGA)**.\n2. **Phase 2: Reduction**:\n   - 3-PGA is phosphorylated by ATP to 1,3-bisphosphoglycerate, then reduced by **NADPH** to **Glyceraldehyde-3-phosphate (G3P)**. For every 3 CO2 fixed, 6 G3P are formed; **1 net G3P exits** to synthesize glucose/sucrose.\n3. **Phase 3: Regeneration of RuBP**:\n   - The remaining 5 G3P molecules undergo a series of complex rearrangements powered by additional **ATP** to regenerate 3 molecules of RuBP, enabling cycle continuation.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p7_0.png",
        "imageDescription": "Calvin Cycle diagram detailing 3 phases: carbon fixation (RuBisCO), reduction (ATP & NADPH consumption), and RuBP regeneration.",
        "citation": "BOT 1121 Lec 18, Slide 7",
        "tags": ["photosynthesis", "calvin-cycle", "rubisco", "rubp", "g3p"]
    },
    {
        "id": "bot-1121-m2-c42",
        "front": "Explain why RuBisCO is considered an evolutionarily 'inefficient' enzyme, and describe the costly process of Photorespiration.",
        "hint": "What happens when RuBisCO binds O2 instead of CO2, and what toxic 2-carbon byproduct is produced?",
        "back": "RuBisCO & Photorespiration (C2 Cycle):\n\n• **Dual Catalytic Activity**:\n  - RuBisCO evolved ~3.5 billion years ago in an anoxic ancient atmosphere.\n  - Its active site cannot perfectly discriminate between CO2 and O2, exhibiting both **carboxylase** and **oxygenase** activity.\n• **The Oxygenase Reaction**:\n  - `RuBP (5C) + O2 -> 1 molecule of 3-PGA (3C) + 1 molecule of 2-Phosphoglycolate (2C)`.\n• **Metabolic Cost of Photorespiration**:\n  - Phosphoglycolate is a toxic metabolic dead-end. Salvaging it requires an energy-draining salvage pathway spanning **chloroplasts, peroxisomes, and mitochondria**.\n  - Costs significant ATP and NADPH while releasing previously fixed carbon as CO2, reducing photosynthetic efficiency by 25–40% in hot, dry environments.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p24_0.png",
        "imageDescription": "Comparison of Calvin Cycle carbon fixation vs Photorespiration oxygenation pathway yielding 2-phosphoglycolate.",
        "citation": "BOT 1121 Lec 18, Slide 24",
        "tags": ["photosynthesis", "rubisco", "photorespiration", "phosphoglycolate", "oxygenase"]
    },
    {
        "id": "bot-1121-m2-c43",
        "front": "How do C4 plants eliminate photorespiration? Describe their unique 'Kranz anatomy' and spatial separation of enzymes.",
        "hint": "Contrast what happens in the mesophyll cells (PEP carboxylase) versus the bundle sheath cells (RuBisCO).",
        "back": "C4 Photosynthesis & **Kranz Anatomy** (Spatial Separation):\n\n• **Kranz Anatomy**: Ring of prominent, photosynthetic **bundle sheath cells** tightly encircling leaf vascular bundles, surrounded radially by **mesophyll cells**.\n• **Two-Compartment Spatial Separation**:\n  1. **Mesophyll Cells**:\n     - Initial CO2 fixation is catalyzed by **PEP Carboxylase**, which has a massive affinity for bicarbonate (HCO3-) and **zero affinity for O2**.\n     - Forms a 4-carbon acid (**oxaloacetate** -> **malate**).\n  2. **Bundle Sheath Cells**:\n     - Malate is shuttled into bundle sheath cells and decarboxylated, releasing a dense burst of CO2 in direct vicinity of **RuBisCO**.\n  3. **Result**: The local CO2 concentration around RuBisCO is maintained at 10–20 times atmospheric levels, virtually eliminating photorespiration even under hot, arid conditions with closed stomata.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p28_0.jpeg",
        "imageDescription": "Kranz anatomy cross-section in C4 leaf showing radial arrangement of mesophyll cells around enlarged, chloroplast-rich bundle sheath cells.",
        "citation": "BOT 1121 Lec 18, Slide 28",
        "tags": ["c4-photosynthesis", "kranz-anatomy", "pep-carboxylase", "bundle-sheath", "spatial-separation"]
    },
    {
        "id": "bot-1121-m2-c44",
        "front": "How does Crassulacean Acid Metabolism (CAM) temporally separate carbon capture and sugar production in succulent desert plants?",
        "hint": "Analyze stomatal behavior at Night vs Day, and where malic acid is sequestered overnight.",
        "back": "CAM Photosynthesis (Temporal Separation):\n\n• **Night (Stomata Open)**:\n  - Temperatures drop and relative humidity rises, minimizing transpirational water loss.\n  - Stomata open; CO2 enters and is fixed by **PEP Carboxylase** into 4-carbon **oxaloacetate -> malic acid**.\n  - Malic acid is pumped into large central **vacuoles**, causing vacuolar sap to become highly acidic overnight.\n\n• **Day (Stomata Closed)**:\n  - Stomata remain tightly sealed to conserve water in extreme heat.\n  - Malate is transported out of vacuoles into chloroplasts and decarboxylated, flooding stroma with CO2.\n  - Sunlight activates light reactions; **RuBisCO and the Calvin Cycle** fix this concentrated CO2 into sugars with zero evaporative water loss.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p32_0.png",
        "imageDescription": "Day vs Night diagram of CAM photosynthesis showing nocturnal malic acid accumulation in vacuoles and daytime Calvin cycle fixation.",
        "citation": "BOT 1121 Lec 18, Slide 32",
        "tags": ["cam-photosynthesis", "temporal-separation", "desert-plants", "malate", "vacuole"]
    },
    {
        "id": "bot-1121-m2-c45",
        "front": "Synthesize the ecological trade-offs between C3, C4, and CAM photosynthetic pathways in cool/moist vs hot/sunny vs hyper-arid environments.",
        "hint": "Consider energy cost per CO2 fixed vs water-use efficiency (WUE).",
        "back": "Comparative Ecological Trade-Offs (C3 vs C4 vs CAM):\n\n• **C3 Plants (Wheat, Rice, Oak, Rose)**:\n  - Energy Cost: Low (3 ATP per CO2 fixed under cool conditions).\n  - Water-Use Efficiency (WUE): Lowest (400–500 g H2O lost per g CO2 fixed).\n  - Optimal Habitat: Cool, temperate, humid climates; loses efficiency when temperature >28°C due to photorespiration.\n\n• **C4 Plants (Corn, Sugarcane, Crabgrass)**:\n  - Energy Cost: Moderate (5 ATP per CO2 fixed; extra 2 ATP to regenerate PEP).\n  - WUE: Intermediate (250–350 g H2O lost per g CO2 fixed).\n  - Optimal Habitat: High light, high temperature, tropical grasslands; outcompetes C3 at >30°C.\n\n• **CAM Plants (Cacti, Agaves, Pineapple, Orchids)**:\n  - Energy Cost: Highest (up to 5.5–6.5 ATP per CO2 fixed).\n  - WUE: Highest (only 50–100 g H2O lost per g CO2 fixed).\n  - Optimal Habitat: Arid deserts and epiphytic canopies; exhibits slow growth rates due to limited overnight vacuolar malate storage capacity.",
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p30_0.jpeg",
        "imageDescription": "Comparative chart contrasting C3, C4, and CAM water use efficiency, optimal temperature range, and energetic costs.",
        "citation": "BOT 1121 Lec 18, Slide 30",
        "tags": ["photosynthesis", "c3-vs-c4-vs-cam", "water-use-efficiency", "ecology"]
    }
]

# 15 Comprehensive Practical / Exam Quizzes
quizzes = [
    {
        "station": "Station 1: Fern Sporangium Biomechanics",
        "question": "A student examines a fern sporangium under the compound microscope and observes a single curved ridge of cells with heavily lignified, reddish inner walls and thin, flexible outer walls. When heat from the illuminator warms the slide, this ring suddenly snaps open, ejecting the internal spores. What is this specialized cell layer?",
        "options": [
            "Indusium",
            "Annulus",
            "Tapetum",
            "Prothallus"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p31_0.jpeg",
        "imageDescription": "High magnification of a fern sporangium showcasing the thickened annulus cells that create the catapult mechanism.",
        "socraticHint": "Think about the specialized band of cells responsible for the mechanical catapult action triggered by water evaporation and cavitation.",
        "explanation": "The correct answer is the **Annulus**. The annulus consists of cells with unevenly thickened walls that store elastic energy as water evaporates, eventually cavitating and snapping forward to catapult haploid spores into the air. The *indusium* is the protective epidermal flap covering the entire sorus, not the sporangium wall itself. The *tapetum* is nutritive tissue inside anthers/sporangia, and the *prothallus* is the gametophyte thallus.",
        "citation": "BOT 1121 Lec 10, Slide 31"
    },
    {
        "station": "Station 2: Fern Alternation of Generations",
        "question": "Which of the following statements regarding the fern life cycle is biologically ACCURATE?",
        "options": [
            "The leafy fern frond represents the haploid gametophyte generation.",
            "Spores are produced via mitosis inside the prothallus archegonia.",
            "Fern sperm are multi-flagellated and require an external film of free water to swim to the archegonium.",
            "The fern sporophyte remains nutritionally dependent on the gametophyte throughout its entire lifespan."
        ],
        "correctIndex": 2,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_10_p34_0.jpeg",
        "imageDescription": "Fern life cycle diagram highlighting alternation between independent sporophyte (2n) and independent gametophyte (n).",
        "socraticHint": "Recall the primitive reproductive requirement ferns share with bryophytes regarding fertilization and flagellated sperm.",
        "explanation": "The correct answer is that **fern sperm are multi-flagellated and require an external film of water to swim to the archegonium**. The conspicuous leafy frond is the diploid sporophyte (not gametophyte). Spores are produced by *meiosis* in sporangia on sporophyte fronds (not mitosis in archegonia). Once the young sporophyte produces green leaves and roots, it becomes completely independent of the gametophyte prothallus, which soon senesces.",
        "citation": "BOT 1121 Lec 10, Slide 34"
    },
    {
        "station": "Station 3: Gymnosperm Seed Anatomy",
        "question": "In a dissected pine seed (*Pinus*), a student identifies the food storage tissue surrounding the central embryo. What is the ploidy level and developmental origin of this nutritive reserve?",
        "options": [
            "Triploid (3n), formed by double fertilization of the central cell polar nuclei.",
            "Haploid (1n), derived from the vegetative body of the female gametophyte.",
            "Diploid (2n), derived from the maternal nucellus tissue.",
            "Diploid (2n), formed by mitotic expansion of the zygote suspensor."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p4_0.jpeg",
        "imageDescription": "Dissected gymnosperm seed showing the haploid female gametophyte nutritive tissue enclosing the embryo.",
        "socraticHint": "Does gymnosperm reproduction feature triploid endosperm from double fertilization, or is the nutritive tissue generated prior to fertilization?",
        "explanation": "The correct answer is **Haploid (1n), derived from the female gametophyte**. Unlike angiosperms (which synthesize triploid 3n endosperm via double fertilization only after successful pollination and egg fertilization), gymnosperms allocate nutritive reserves to the female gametophyte *before* fertilization takes place.",
        "citation": "BOT 1121 Lec 11, Slide 4"
    },
    {
        "station": "Station 4: Gymnosperm Phyla Identification",
        "question": "A botanical garden specimen displays broad, fan-shaped leaves with dichotomous venation. The tree is dioecious, and the fallen seeds on the ground produce a nauseating odor resembling rancid butter (caused by butyric acid). Which gymnosperm division does this plant belong to?",
        "options": [
            "Pinophyta (Conifers)",
            "Cycadophyta (Cycads)",
            "Ginkgophyta (*Ginkgo biloba*)",
            "Gnetophyta (*Welwitschia*)"
        ],
        "correctIndex": 2,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_11_p28_0.jpeg",
        "imageDescription": "Ginkgo biloba foliage showing distinctive dichotomous fan leaves and mature dioecious seeds.",
        "socraticHint": "Think of the monotypic 'living fossil' renowned for fan-shaped leaves and foul-smelling sarcotesta in female trees.",
        "explanation": "The correct answer is **Ginkgophyta (*Ginkgo biloba*)**. *Ginkgo biloba* is a monotypic gymnosperm with unique fan-shaped leaves with dichotomously branching veins. Female trees bear paired ovules that ripen into fleshy seeds whose outer sarcotesta layer produces rancid butyric acid.",
        "citation": "BOT 1121 Lec 11, Slide 28"
    },
    {
        "station": "Station 5: Floral Architecture & Whorl Fusion",
        "question": "In a dissected flower, a botanist observes that the five petals are fused along their margins to form a tubular bell-shaped corolla, while the filaments of the stamens are fused directly to the inner surface of the petal tube. What technical botanical terms describe these two fusion patterns?",
        "options": [
            "Connation of petals; Adnation of stamens to petals",
            "Adnation of petals; Connation of stamens to petals",
            "Epigyny of petals; Perigyny of stamens",
            "Apocarpy of petals; Syncarpy of stamens"
        ],
        "correctIndex": 0,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_12_p12_1.jpeg",
        "imageDescription": "Diagram of floral fusion illustrating connation (fusion of like members) vs adnation (fusion of unlike whorls).",
        "socraticHint": "Remember: 'Connation' = fusion of like parts in the same whorl; 'Adnation' = fusion between unlike parts from different whorls.",
        "explanation": "The correct answer is **Connation of petals; Adnation of stamens to petals**. When members of the same whorl fuse together (petals fusing with petals), the condition is *connation* (sympetaly). When members of different whorls fuse together (stamens fusing to petals, known as epipetalous stamens), the condition is *adnation*.",
        "citation": "BOT 1121 Lec 12, Slide 12"
    },
    {
        "station": "Station 6: Ovary Position & Epigyny",
        "question": "In an apple or cucumber blossom, the sepals, petals, and stamens insert at the very top of the ovary because the surrounding floral tube/receptacle is completely fused with the ovary wall. How is this floral insertion and ovary position classified?",
        "options": [
            "Hypogynous flower with a Superior ovary",
            "Perigynous flower with a Superior ovary",
            "Epigynous flower with an Inferior ovary",
            "Apocarpous flower with a Hypanthium"
        ],
        "correctIndex": 2,
        "image": "images/bot-1121-flowers/fig_9_28_ovary_positions_superior_inferior.jpg",
        "imageDescription": "Comparative diagram illustrating hypogynous, perigynous, and epigynous floral architectures.",
        "socraticHint": "When the ovary is sunken underneath the insertion point of the other whorls, the prefix 'epi-' (above) refers to parts being above the 'gyn' (ovary).",
        "explanation": "The correct answer is **Epigynous flower with an Inferior ovary**. In epigynous flowers, the receptacle or hypanthium is adnate to the ovary wall, so the sepals, petals, and stamens appear to emerge from the top of the ovary, rendering the ovary inferior.",
        "citation": "BOT 1121 Lec 12, Slide 28"
    },
    {
        "station": "Station 7: Pericarp Layering in Drupes",
        "question": "When enjoying a fresh peach (*Prunus persica*), what specific botanical layer does the hard, stony 'pit' (which you discard to access the enclosed seed) represent?",
        "options": [
            "Lignified seed coat (testa)",
            "Endocarp of the pericarp",
            "Mesocarp of the pericarp",
            "Sclerified hypanthium"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p2_0.jpeg",
        "imageDescription": "Peach fruit cross-section detailing thin exocarp, fleshy mesocarp, and stony endocarp pit.",
        "socraticHint": "Recall the three layers of the pericarp: exo-, meso-, and endo-. Which layer directly lines the interior cavity enclosing the seed?",
        "explanation": "The correct answer is the **Endocarp of the pericarp**. In a drupe, the pericarp differentiates into three distinct zones: a thin outer skin (exocarp), a fleshy edible middle (mesocarp), and a stony, heavily lignified inner wall (endocarp, pit). The actual seed sits safely inside the hollow of this stony endocarp.",
        "citation": "BOT 1121 Lec 13, Slide 2"
    },
    {
        "station": "Station 8: Aggregate vs Multiple Fruits",
        "question": "A raspberry develops from a single flower that contains numerous separate carpels, producing a cluster of small drupelets. In contrast, a pineapple develops from the fused ovaries of dozens of flowers on a dense inflorescence spike. How are these two fruits classified?",
        "options": [
            "Raspberry is a Multiple fruit; Pineapple is an Aggregate fruit",
            "Raspberry is an Aggregate fruit; Pineapple is a Multiple fruit",
            "Both are classified as Compound Drupes",
            "Raspberry is a Pome; Pineapple is an Accessory Berry"
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_13_p13_2.jpeg",
        "imageDescription": "Diagram comparing aggregate fruit (apocarpous single flower) with multiple fruit (fused inflorescence flowers).",
        "socraticHint": "Key distinction: One flower with multiple free carpels = Aggregate. Multiple distinct flowers fused together = Multiple.",
        "explanation": "The correct answer is **Raspberry is an Aggregate fruit; Pineapple is a Multiple fruit**. Aggregate fruits arise from a single apocarpous flower with multiple distinct pistils/carpels (e.g., raspberry, blackberry). Multiple fruits arise from the fusion of ovaries from multiple separate flowers along an inflorescence (e.g., pineapple, fig, mulberry).",
        "citation": "BOT 1121 Lec 13, Slide 13"
    },
    {
        "station": "Station 9: Fig Syconium & Mutualism",
        "question": "Why are female fig wasps (*Blastophaga psenes*) capable of successfully reproducing inside the syconia of male Caprifigs, but unable to lay eggs in the syconia of female Edible Figs?",
        "options": [
            "Caprifigs lack ostioles, allowing wasps to enter through natural fissures in the skin.",
            "Caprifigs possess short-styled florets that match the wasp's ovipositor length, whereas female edible figs have long-styled florets that prevent the ovipositor from reaching the ovary.",
            "Female edible figs secrete lethal insecticidal latex that kills larvae within 24 hours.",
            "Wasps only mate with winged male wasps found exclusively in caprifigs."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_14_p26_0.jpeg",
        "imageDescription": "Stylar dimorphism in Ficus carica: short styles in caprifigs allow oviposition; long styles in edible figs exclude oviposition while ensuring seed set.",
        "socraticHint": "Consider style length vs ovipositor length in the flowers of each tree type.",
        "explanation": "The correct answer is that **Caprifigs possess short-styled florets matching ovipositor length, whereas female edible figs possess long-styled florets exceeding ovipositor length**. In female edible figs, the wasp visits and pollinates the stigmas, but cannot reach the ovary to oviposit, so the flower develops into a viable seed instead of a wasp gall.",
        "citation": "BOT 1121 Lec 14, Slide 25"
    },
    {
        "station": "Station 10: Water Potential Directionality",
        "question": "A plant cell with a solute potential (Ψs) of -0.8 MPa and a pressure potential (Ψp) of +0.3 MPa is placed into an open beaker containing pure distilled water (Ψ = 0 MPa). What will happen to the cell?",
        "options": [
            "Water will flow out of the cell because the cell's total water potential is positive.",
            "Water will enter the cell by osmosis until the cell's turgor pressure (Ψp) rises to +0.8 MPa and total cell Ψ reaches 0 MPa.",
            "Solutes will actively pump out of the cell until Ψs equals 0 MPa.",
            "The cell will undergo immediate plasmolysis due to hypotonic collapse."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p6_0.jpeg",
        "imageDescription": "Water potential equilibrium diagram showing water uptake into a plant cell until internal Ψ equals surrounding solution Ψ.",
        "socraticHint": "Calculate initial total cell water potential: Ψ = Ψs + Ψp = (-0.8) + (+0.3) = -0.5 MPa. Distilled water is 0 MPa. Does water flow from 0 to -0.5 MPa?",
        "explanation": "The correct answer is that **water will enter the cell until cell turgor pressure rises to +0.8 MPa and cell Ψ reaches 0 MPa**. Initial cell Ψ = -0.8 + 0.3 = -0.5 MPa. Distilled water in the beaker has Ψ = 0 MPa. Because water flows spontaneously from higher (-0.0 MPa) to lower (-0.5 MPa) water potential, water enters the cell, increasing turgor pressure (Ψp) until Ψ_cell reaches 0 MPa, establishing dynamic equilibrium.",
        "citation": "BOT 1121 Lec 15, Slide 5"
    },
    {
        "station": "Station 11: Cohesion-Tension Dynamics",
        "question": "What is the ultimate physical energy source that drives the continuous upward movement of water columns through xylem tracheary elements to the top of tall forest canopies?",
        "options": [
            "ATP hydrolysis by H+-ATPase pumps located in the endodermis.",
            "Solar radiation driving the evaporation and transpiration of water from leaf mesophyll surfaces.",
            "Active contractile pumping of lignified tracheid secondary cell walls.",
            "Metabolic respiratory heating by the stem vascular cambium."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_15_p12_0.jpeg",
        "imageDescription": "Cohesion-Tension diagram highlighting solar evaporation from leaf mesophyll as the passive driving engine of sap ascent.",
        "socraticHint": "Does the xylem spend metabolic cellular ATP to pull water, or is it powered by an environmental energy source acting at the leaf surface?",
        "explanation": "The correct answer is **Solar radiation driving evaporation and transpiration of water**. According to the Cohesion-Tension theory, transpiration driven by solar heating lowers water potential at the evaporative menisci of leaf cell walls, generating massive negative hydrostatic tension that pulls water columns upward via water's cohesive hydrogen bonds.",
        "citation": "BOT 1121 Lec 15, Slide 12"
    },
    {
        "station": "Station 12: Münch Pressure-Flow Mechanism",
        "question": "According to the Münch Pressure-Flow hypothesis, what primary event causes the high positive hydrostatic turgor pressure at a sugar source (e.g., mature leaf)?",
        "options": [
            "Direct active pumping of water molecules across sieve plates by ATP synthase.",
            "Active loading of sucrose into sieve tube elements, which drastically lowers Ψs and causes osmotic water influx from adjacent xylem.",
            "Rapid enzymatic conversion of insoluble starch into gaseous CO2 within sieve tube elements.",
            "Negative tension generated by leaf transpiration pulling phloem sap toward the petiole."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_16_p14_0.jpeg",
        "imageDescription": "Pressure-flow diagram showing high sucrose concentration lowering Ψs, drawing in water from xylem to generate source turgor.",
        "socraticHint": "Follow the sequence: Sugar loading -> solute potential drops -> water enters from nearby xylem -> internal hydrostatic turgor rises.",
        "explanation": "The correct answer is that **active loading of sucrose lowers Ψs, drawing in water from xylem via osmosis, generating high positive turgor pressure**. This high turgor at the source drives bulk sap flow through sieve tube pores toward regions of lower turgor at sugar sinks.",
        "citation": "BOT 1121 Lec 16, Slide 14"
    },
    {
        "station": "Station 13: Thylakoid Photophosphorylation",
        "question": "During the light reactions of photosynthesis, how does the proton (H+) concentration gradient across the thylakoid membrane generate ATP?",
        "options": [
            "Protons are actively pumped from the stroma into the lumen by ATP Synthase using NADPH.",
            "Protons accumulated in the thylakoid lumen diffuse down their electrochemical gradient into the stroma through the CF0-CF1 ATP Synthase complex, driving catalytic rotation.",
            "Electrons pass directly through the ATP Synthase rotor, reducing ADP to ATP.",
            "Protons split water molecules on the stromal surface of Photosystem I."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_17_p34_0.jpeg2000",
        "imageDescription": "Thylakoid ATP Synthase diagram illustrating chemiosmotic proton translocation from lumen to stroma.",
        "socraticHint": "Remember chemiosmosis: high H+ in the lumen flows down its gradient into the stroma through ATP Synthase.",
        "explanation": "The correct answer is that **protons accumulated in the thylakoid lumen diffuse into the stroma through ATP Synthase, driving catalytic synthesis of ATP**. Photolysis of water and plastoquinone Q-cycle proton pumping acidify the lumen (pH ~4.5-5.0). The flow of protons through CF0 causes CF1 to rotate and synthesize ATP from ADP and Pi.",
        "citation": "BOT 1121 Lec 17, Slide 34"
    },
    {
        "station": "Station 14: Calvin-Benson Cycle & RuBisCO",
        "question": "What is the primary enzymatic reaction catalyzed by RuBisCO in the stroma during Phase 1 (Carbon Fixation) of the Calvin-Benson Cycle?",
        "options": [
            "Combining CO2 with 5-carbon RuBP to produce an unstable 6-carbon intermediate that immediately yields two molecules of 3-PGA.",
            "Combining CO2 with 3-carbon PEP to produce 4-carbon oxaloacetate.",
            "Reducing 3-PGA to G3P using electrons donated by NADPH.",
            "Regenerating RuBP from G3P by consuming ATP."
        ],
        "correctIndex": 0,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p7_0.png",
        "imageDescription": "Phase 1 of Calvin Cycle: RuBisCO carboxylation of RuBP yielding two 3-PGA molecules.",
        "socraticHint": "Recall the full name of RuBisCO: Ribulose-1,5-bisphosphate carboxylase/oxygenase. What molecule does it carboxylate?",
        "explanation": "The correct answer is **combining CO2 with 5-carbon RuBP to yield two molecules of 3-PGA**. RuBisCO carboxylates ribulose-1,5-bisphosphate (RuBP). The resulting 6-carbon intermediate hydrolyzes into two molecules of 3-phosphoglycerate (3-PGA). Combining CO2 with PEP is performed by PEP Carboxylase in C4/CAM plants, not RuBisCO.",
        "citation": "BOT 1121 Lec 18, Slide 7"
    },
    {
        "station": "Station 15: C4 vs CAM Adaptation",
        "question": "How do C4 plants and CAM plants differ fundamentally in their mechanism of eliminating photorespiration?",
        "options": [
            "C4 plants use RuBisCO exclusively, whereas CAM plants completely lack RuBisCO.",
            "C4 plants achieve spatial separation of carbon capture (mesophyll) and the Calvin cycle (bundle sheath), whereas CAM plants achieve temporal separation (night vs day) within the same photosynthetic cells.",
            "C4 plants open stomata at night, whereas CAM plants open stomata only during mid-afternoon.",
            "C4 plants store malate in xylem vessels, whereas CAM plants store malate in phloem companion cells."
        ],
        "correctIndex": 1,
        "image": "images/bot-1121-m2-slides/BOT_1121_F2026_Lecture_18_p32_0.png",
        "imageDescription": "Comparative diagram illustrating spatial separation in C4 Kranz anatomy vs temporal separation in CAM succulents.",
        "socraticHint": "Think: C4 separates by LOCATION (different cells); CAM separates by TIME (night vs day).",
        "explanation": "The correct answer is that **C4 plants achieve spatial separation (mesophyll vs bundle sheath cells), whereas CAM plants achieve temporal separation (nighttime CO2 capture vs daytime Calvin cycle) within the same cell**. Both pathways utilize PEP carboxylase to avoid RuBisCO oxygenation, but C4 relies on Kranz anatomy while CAM relies on nocturnal vacuolar malate storage.",
        "citation": "BOT 1121 Lec 18, Slide 32"
    }
]

deck = {
    "id": "bot-1121-midterm-2",
    "course": "BOT-1121",
    "title": "BOT-1121: Midterm #2 Master Deck (Lectures 10–18)",
    "description": "Comprehensive, authoritative study set for Cal Poly BOT-1121 Midterm 2 covering Ferns & Herbaria, Gymnosperms, Flower Anatomy, Fruits & Seeds, Fig Biology (Ficus mutualism), Water Transport, Sugar Transport, and Photosynthesis Parts 1 & 2. Features 45 high-yield flashcards with extracted lecture diagrams and 15 practical lab/exam quizzes.",
    "source": "Sean Ryan Lecture Slides (Lectures 10–18) & Cal Poly Herbarium / Lab Practicals",
    "flashcards": cards,
    "quizzes": quizzes
}

# Update study_portal/decks.json
decks_path = 'study_portal/decks.json'
with open(decks_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Replace existing or insert at index 0 for top prominence
existing_idx = next((i for i, d in enumerate(data['decks']) if d['id'] == deck['id']), None)
if existing_idx is not None:
    data['decks'][existing_idx] = deck
else:
    data['decks'].insert(0, deck)

with open(decks_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(cards)} flashcards and {len(quizzes)} quizzes to deck '{deck['id']}' in {decks_path}!")
