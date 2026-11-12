import json
import re

with open('G:/My Drive/Academics/study_portal/set1_cards.json', 'r', encoding='utf-8') as f:
    s1 = json.load(f)
with open('G:/My Drive/Academics/study_portal/set2_cards.json', 'r', encoding='utf-8') as f:
    s2 = json.load(f)

c1 = s1.get('cards', [])
c2 = s2.get('cards', [])

# Deduplicate and merge
merged_cards = {}

def clean_text(t):
    if not t: return ''
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def format_definition(d):
    if not d: return ''
    # Replace numbered items with neat line breaks
    d = re.sub(r'(\d+\.\s*)', r'\n\1', d).strip()
    return d

def generate_hint(term, definition):
    t_low = term.lower()
    d_low = definition.lower()
    if 'casparian' in t_low:
        return 'Waxy hydrophobic strip of suberin in the endodermal radial walls.'
    if 'endodermis' in t_low:
        return 'Innermost layer of the root cortex functioning as a selective apoplastic filter.'
    if 'pericycle' in t_low:
        return 'Meristematic ring inside endodermis giving rise to lateral roots.'
    if 'stoma' in t_low or 'guard' in t_low:
        return 'Turgor-driven epidermal valves regulating CO2 entry and transpirational water loss.'
    if 'palisade' in t_low:
        return 'Columnar upper mesophyll layer packed with chloroplasts for maximum light interception.'
    if 'spongy' in t_low:
        return 'Loosely arranged lower mesophyll with extensive air spaces for gas exchange.'
    if 'mycorrhiz' in t_low:
        return 'Mutualistic fungal association enhancing phosphorus and nutrient uptake.'
    if 'adhesion' in t_low:
        return 'Attraction between water molecules and polar cell wall polymers (cellulose/lignin).'
    if 'cohesion' in t_low:
        return 'Hydrogen bonding holding identical water molecules together under negative tension.'
    if 'root cap' in t_low or 'calyptra' in t_low:
        return 'Thimble-shaped apical protective covering that secretes mucilage and senses gravity.'
    if 'monocot' in t_low:
        return 'Think fibrous root systems, parallel venation, and atactostele (scattered bundles).'
    if 'eudicot' in t_low or 'dicot' in t_low:
        return 'Think taproot systems, reticulate/net venation, and eustele (ring of bundles).'
    if 'monoecious' in t_low:
        return 'Literally "one house": both staminate and carpellate flowers on the SAME individual.'
    if 'dioecious' in t_low:
        return 'Literally "two houses": male and female flowers on SEPARATE distinct plants.'
    if 'syconium' in t_low or 'ostiole' in t_low:
        return 'Inverted hollow fig inflorescence accessed via a tiny apical pore by symbiotic wasps.'
    if 'xylem' in t_low:
        return 'Water-conducting tissue composed of dead lignified tracheary elements (tracheids & vessels).'
    if 'phloem' in t_low:
        return 'Living assimilate-transporting tissue composed of sieve elements and companion cells.'
    return f'Focus on the biological function or anatomical location of {term}.'

def get_tags(term, definition):
    text = (term + ' ' + definition).lower()
    tags = []
    if any(k in text for k in ['root', 'radicle', 'casparian', 'endodermis', 'pericycle', 'mycorrhiz', 'taproot']):
        tags.append('roots')
    if any(k in text for k in ['leaf', 'leaves', 'mesophyll', 'stoma', 'stomata', 'cuticle', 'venation', 'petiole']):
        tags.append('leaves')
    if any(k in text for k in ['stem', 'shoot', 'node', 'internode', 'bud', 'bark', 'lenticel', 'cambium']):
        tags.append('stems')
    if any(k in text for k in ['xylem', 'phloem', 'vascular', 'tracheid', 'vessel', 'cohesion', 'transpiration', 'water']):
        tags.append('vascular-transport')
    if any(k in text for k in ['flower', 'fruit', 'seed', 'ovule', 'pollen', 'monoecious', 'dioecious', 'ostiole', 'syconium']):
        tags.append('reproduction')
    if any(k in text for k in ['secondary', 'cork', 'wood', 'growth']):
        tags.append('secondary-growth')
    if not tags:
        tags.append('plant-anatomy')
    return tags

# Process Set 1
for item in c1:
    term = clean_text(item.get('term', ''))
    definition = item.get('definition', '').strip()
    if not term or not definition: continue
    key = term.lower()
    merged_cards[key] = {
        'term': term,
        'definition': definition,
        'source': 'Quizlet Set 1'
    }

# Process Set 2
for item in c2:
    term = clean_text(item.get('term', ''))
    definition = item.get('definition', '').strip()
    if not term or not definition: continue
    key = term.lower()
    if key in merged_cards:
        # If set 2 has longer or different definition, combine or enrich
        existing = merged_cards[key]['definition']
        if definition not in existing and len(definition) > 5:
            merged_cards[key]['definition'] = f"{existing}\n\n*Additional definition:* {definition}"
    else:
        merged_cards[key] = {
            'term': term,
            'definition': definition,
            'source': 'Quizlet Set 2'
        }

formatted_flashcards = []
for idx, (k, val) in enumerate(sorted(merged_cards.items(), key=lambda x: x[0])):
    term = val['term']
    definition = format_definition(val['definition'])
    
    # Bold the first occurrence of the term or key words in definition
    back_html = definition
    
    formatted_flashcards.append({
        'id': f"m2-{idx+1:03d}",
        'front': term,
        'hint': generate_hint(term, definition),
        'back': back_html,
        'citation': f"Sean Ryan BOT 121 — Midterm 2 ({val['source']})",
        'tags': get_tags(term, definition)
    })

print(f"Total formatted flashcards: {len(formatted_flashcards)}")

# Practical multiple-choice quizzes for Midterm 2
midterm2_quizzes = [
    {
        "id": "m2-q01",
        "station": "Station 1: Root Anatomy & Selective Uptake",
        "question": "Which anatomical structure prevents the uncontrolled apoplastic flow of water and solutes directly into the root vascular cylinder?",
        "options": [
            "Pericycle lateral initials",
            "Casparian strip in endodermal radial walls",
            "Root cap mucilage sheath",
            "Exodermal trichomes"
        ],
        "correctIndex": 1,
        "explanation": "The Casparian strip is a belt of waxy suberin embedded in the transverse and radial walls of endodermal cells. It forces water and dissolved ions out of the apoplast (cell wall pathway) and into the symplast (cytoplasm) for selective plasma membrane filtration.",
        "socraticHint": "Look for the specialized hydrophobic barrier within the innermost layer of the root cortex.",
        "citation": "BOT 121 Lecture: Root Structure & Function"
    },
    {
        "id": "m2-q02",
        "station": "Station 2: Leaf Mesophyll Specialization",
        "question": "In a dorsiventral eudicot leaf, where is the palisade mesophyll located and what is its primary physiological role?",
        "options": [
            "Upper (adaxial) side; maximum sunlight interception and photosynthesis",
            "Lower (abaxial) side; gas exchange and water vapor storage",
            "Surrounding vascular bundles; suberized sheath filtration",
            "Within stomatal crypts; salt secretion"
        ],
        "correctIndex": 0,
        "explanation": "Palisade mesophyll consists of densely packed, columnar parenchyma cells located beneath the upper epidermis where sunlight is strongest, containing the highest concentration of chloroplasts for photosynthesis. In contrast, the lower spongy mesophyll facilitates gas diffusion.",
        "socraticHint": "Consider which side of the leaf directly receives incoming solar irradiance.",
        "citation": "BOT 121 Lecture: Leaf Anatomy"
    },
    {
        "id": "m2-q03",
        "station": "Station 3: Water Transport Mechanics",
        "question": "According to the Cohesion-Tension theory, how does water move from the roots to the uppermost leaves of tall trees without active metabolic pumping?",
        "options": [
            "Positive atmospheric pressure pushing water through phloem sieve tubes",
            "Transpirational pull creates negative tension transmitted via cohesive hydrogen bonds",
            "Active ATP-driven transport in dead vessel elements",
            "Capillary action alone elevating water hundreds of feet"
        ],
        "correctIndex": 1,
        "explanation": "Evaporation of water from stomata (transpiration) generates a negative pressure potential (tension) at the menisci in cell walls. Because water molecules exhibit high cohesion (H-bonding with each other) and adhesion (attraction to xylem walls), a continuous tensile water column is pulled upward.",
        "socraticHint": "Think about what happens to water molecules when transpirational evaporation occurs at the leaf surface.",
        "citation": "BOT 121 Lecture: Water Relations & Transpiration"
    },
    {
        "id": "m2-q04",
        "station": "Station 4: Floral Sexuality & Morphology",
        "question": "A plant species produces staminate (male) flowers on one individual tree and carpellate (female) flowers on a separate individual tree. This sexual condition is termed:",
        "options": [
            "Monoecious",
            "Dioecious",
            "Hermaphroditic (Synoecious)",
            "Parthenocarpic"
        ],
        "correctIndex": 1,
        "explanation": "Dioecious ('two houses') refers to species where staminate and carpellate flowers occur on entirely separate individual plants (e.g., Ginkgo, cannabis, willows). Monoecious ('one house') means separate male and female flowers reside on the same individual (e.g., corn, oaks).",
        "socraticHint": "Distinguish between 'one house' (same plant) versus 'two houses' (separate plants).",
        "citation": "BOT 121 Lecture: Floral Morphology"
    },
    {
        "id": "m2-q05",
        "station": "Station 5: Root Origins & Branching",
        "question": "From which internal cell layer do lateral (branch) roots emerge in seed plants?",
        "options": [
            "Epidermal root hairs",
            "Endodermal Casparian cells",
            "Pericycle",
            "Central pith"
        ],
        "correctIndex": 2,
        "explanation": "Lateral roots initiate endogenously from the pericycle, a layer of meristematic cells directly inside the endodermis. The developing lateral root pushes through the cortex and epidermis into the surrounding soil.",
        "socraticHint": "Identify the outermost cell layer of the stele lying directly beneath the endodermis.",
        "citation": "BOT 121 Lecture: Root Development"
    },
    {
        "id": "m2-q06",
        "station": "Station 6: Specialized Inflorescence & Mutualism",
        "question": "What is a syconium, and how does the ostiole function in its reproductive cycle?",
        "options": [
            "A modified root tuber; the ostiole absorbs dissolved phosphate ions",
            "An inverted fleshy inflorescence containing hundreds of inward-facing flowers; the ostiole is the tiny apical pore for pollinator wasp entry",
            "A winged samara fruit; the ostiole aids aerodynamic dispersal",
            "A specialized stomatal chamber that traps predatory insects"
        ],
        "correctIndex": 1,
        "explanation": "A syconium is the specialized inflorescence of the genus Ficus (figs). The receptacle folds inward to form an internal cavity lined with tiny florets. The ostiole is the narrow apical opening guarded by scales through which female fig wasps enter to achieve pollination and lay eggs.",
        "socraticHint": "Recall the unique structure of figs and their co-evolved mutualism with fig wasps.",
        "citation": "BOT 121 Lecture: Inflorescences & Coevolution"
    }
]

deck_object = {
    "id": "bot-1121-midterm-2",
    "course": "BOT-1121",
    "title": "Midterm #2 Botany",
    "description": "Comprehensive Midterm 2 study deck for Sean Ryan's Botany (BOT 121). Covers root anatomy, leaf morphology, secondary growth, water potential, vascular transport, and floral reproduction synthesized from Quizlet sets 168561570 & 1106261382.",
    "source": "Quizlet (Sean Ryan BOT 121 Midterm 2 Sets #1 & #2)",
    "flashcards": formatted_flashcards,
    "quizzes": midterm2_quizzes
}

with open('G:/My Drive/Academics/study_portal/midterm2_deck.json', 'w', encoding='utf-8') as f:
    json.dump(deck_object, f, indent=2)

print("Saved G:/My Drive/Academics/study_portal/midterm2_deck.json!")
