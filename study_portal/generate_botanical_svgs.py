import os

artifact_dir = r"C:\Users\pider\.gemini\antigravity-cli\brain\4fc7ef2c-dc26-4144-a761-288df9e3b360"
portal_diagrams_dir = r"G:\My Drive\Academics\study_portal\images\diagrams"
os.makedirs(portal_diagrams_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. PLANT BODY STRUCTURE SVG
# -------------------------------------------------------------
plant_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 650" width="100%" height="100%" style="background:#0e131f; font-family:'Segoe UI', -apple-system, sans-serif;">
  <defs>
    <linearGradient id="stemGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#15803d"/>
      <stop offset="50%" stop-color="#22c55e"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
    <linearGradient id="rootGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#92400e"/>
    </linearGradient>
    <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#16a34a"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <rect x="25" y="20" width="900" height="60" rx="12" fill="#161f30" stroke="#2d3748" stroke-width="1.5"/>
  <text x="475" y="47" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="700" letter-spacing="0.5">Generalized Plant Body Architecture (Vegetative &amp; Reproductive Systems)</text>
  <text x="475" y="68" text-anchor="middle" fill="#94a3b8" font-size="12">Shoot System (Photosynthesis, Transport, Reproduction) &amp; Root System (Anchorage, Water &amp; Nutrient Uptake)</text>

  <!-- Ground Line & Soil Boundary -->
  <rect x="50" y="380" width="850" height="230" rx="10" fill="#1a1510" opacity="0.6"/>
  <line x1="50" y1="380" x2="900" y2="380" stroke="#78350f" stroke-width="3" stroke-dasharray="6,4"/>
  <text x="70" y="372" fill="#a1a1aa" font-size="12" font-style="italic">Ground Level / Soil Surface</text>

  <!-- Shoot vs Root Bracket Zones -->
  <!-- Shoot System Bracket -->
  <path d="M 60,110 L 45,110 L 45,235 L 35,235 L 45,235 L 45,360 L 60,360" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="30" y="240" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="end" transform="rotate(-90 30,240)">SHOOT SYSTEM</text>

  <!-- Root System Bracket -->
  <path d="M 60,395 L 45,395 L 45,495 L 35,495 L 45,495 L 45,595 L 60,595" fill="none" stroke="#fbbf24" stroke-width="2"/>
  <text x="30" y="500" fill="#fbbf24" font-size="14" font-weight="700" text-anchor="end" transform="rotate(-90 30,500)">ROOT SYSTEM</text>

  <!-- Stem Main Axis -->
  <path d="M 470,120 Q 470,250 470,380" fill="none" stroke="url(#stemGrad)" stroke-width="16" stroke-linecap="round"/>
  
  <!-- Terminal Apical Bud (SAM) -->
  <ellipse cx="470" cy="115" rx="14" ry="18" fill="#86efac" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <path d="M 460,115 Q 470,95 480,115 Z" fill="#22c55e"/>

  <!-- Node 1: Flower on Lateral Pedicel -->
  <path d="M 470,160 Q 430,150 400,140" fill="none" stroke="#22c55e" stroke-width="6"/>
  <!-- Petals -->
  <circle cx="395" cy="138" r="16" fill="#ec4899" opacity="0.9"/>
  <circle cx="380" cy="130" r="12" fill="#f43f5e" opacity="0.8"/>
  <circle cx="410" cy="130" r="12" fill="#f43f5e" opacity="0.8"/>
  <circle cx="395" cy="120" r="12" fill="#fb7185" opacity="0.9"/>
  <circle cx="395" cy="138" r="6" fill="#facc15"/>

  <!-- Node 2: Alternate Leaf Left -->
  <path d="M 470,220 Q 380,210 320,180" fill="none" stroke="#15803d" stroke-width="6"/>
  <path d="M 320,180 C 270,150 250,210 320,240 C 370,250 390,210 320,180 Z" fill="url(#leafGrad)" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <path d="M 320,180 Q 300,210 270,195" fill="none" stroke="#86efac" stroke-width="1.5"/>

  <!-- Axillary Bud at Left Node -->
  <ellipse cx="458" cy="214" rx="5" ry="7" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>

  <!-- Node 3: Alternate Leaf Right -->
  <path d="M 470,280 Q 560,270 620,240" fill="none" stroke="#15803d" stroke-width="6"/>
  <path d="M 620,240 C 670,210 690,270 620,300 C 570,310 550,270 620,240 Z" fill="url(#leafGrad)" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>
  <path d="M 620,240 Q 640,270 670,255" fill="none" stroke="#86efac" stroke-width="1.5"/>

  <!-- Axillary Bud at Right Node -->
  <ellipse cx="482" cy="274" rx="5" ry="7" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>

  <!-- Internode Indicator -->
  <line x1="495" y1="220" x2="495" y2="280" stroke="#cbd5e1" stroke-width="2"/>
  <line x1="490" y1="220" x2="500" y2="220" stroke="#cbd5e1" stroke-width="2"/>
  <line x1="490" y1="280" x2="500" y2="280" stroke="#cbd5e1" stroke-width="2"/>

  <!-- Node 4: Lower Left Leaf -->
  <path d="M 470,340 Q 370,340 310,320" fill="none" stroke="#15803d" stroke-width="6"/>
  <path d="M 310,320 C 250,300 240,360 310,380 C 370,390 380,350 310,320 Z" fill="url(#leafGrad)" stroke="#16a34a" stroke-width="2" filter="url(#shadow)"/>

  <!-- Primary Taproot -->
  <path d="M 470,380 Q 470,480 470,590" fill="none" stroke="url(#rootGrad)" stroke-width="14" stroke-linecap="round"/>
  
  <!-- Lateral / Branch Roots -->
  <path d="M 470,420 Q 410,440 350,460" fill="none" stroke="#d97706" stroke-width="6"/>
  <path d="M 350,460 Q 310,475 270,480" fill="none" stroke="#b45309" stroke-width="3"/>
  
  <path d="M 470,450 Q 530,470 590,490" fill="none" stroke="#d97706" stroke-width="6"/>
  <path d="M 590,490 Q 640,510 680,515" fill="none" stroke="#b45309" stroke-width="3"/>

  <path d="M 470,490 Q 420,520 370,550" fill="none" stroke="#d97706" stroke-width="5"/>
  <path d="M 470,520 Q 520,550 560,575" fill="none" stroke="#d97706" stroke-width="4"/>

  <!-- Root Hairs Detail Cluster -->
  <g stroke="#fef08a" stroke-width="1" opacity="0.8">
    <line x1="330" y1="460" x2="325" y2="450"/><line x1="335" y1="462" x2="332" y2="452"/><line x1="340" y1="463" x2="340" y2="453"/>
    <line x1="345" y1="464" x2="348" y2="454"/><line x1="330" y1="462" x2="325" y2="472"/><line x1="335" y1="464" x2="333" y2="474"/>
    <line x1="340" y1="465" x2="341" y2="476"/><line x1="346" y1="466" x2="349" y2="477"/>
  </g>

  <!-- Root Tip & Cap (RAM) -->
  <ellipse cx="470" cy="595" rx="8" ry="12" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
  <path d="M 462,598 C 462,612 478,612 478,598 Z" fill="#b45309"/>

  <!-- CALLOUT LABELS & ANNOTATIONS (Right Side) -->
  <g fill="#f8fafc" font-size="12">
    <!-- SAM Callout -->
    <line x1="486" y1="115" x2="680" y2="115" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="486" cy="115" r="3" fill="#38bdf8"/>
    <rect x="680" y="100" width="230" height="32" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="690" y="117" font-weight="700" fill="#38bdf8">Shoot Apical Meristem (SAM)</text>
    <text x="690" y="128" font-size="10" fill="#94a3b8">Terminal bud; primary vertical growth</text>

    <!-- Flower Callout -->
    <line x1="375" y1="135" x2="160" y2="135" stroke="#f43f5e" stroke-width="1.5"/>
    <circle cx="375" cy="135" r="3" fill="#f43f5e"/>
    <rect x="160" y="120" width="180" height="30" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1"/>
    <text x="170" y="136" font-weight="700" fill="#fb7185">Flower (Reproductive)</text>
    <text x="170" y="146" font-size="10" fill="#94a3b8">Specialized determinate shoot</text>

    <!-- Leaf Anatomy Callouts -->
    <line x1="260" y1="210" x2="140" y2="210" stroke="#4ade80" stroke-width="1.5"/>
    <circle cx="260" cy="210" r="3" fill="#4ade80"/>
    <rect x="120" y="195" width="170" height="42" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1"/>
    <text x="130" y="212" font-weight="700" fill="#4ade80">Blade (Lamina)</text>
    <text x="130" y="224" font-size="10" fill="#94a3b8">Expanded photosynthetic surface</text>
    <text x="130" y="233" font-size="9" fill="#64748b">Vascular bundle veins (Xylem/Phloem)</text>

    <!-- Petiole Callout -->
    <line x1="390" y1="215" x2="260" y2="270" stroke="#4ade80" stroke-width="1.5"/>
    <circle cx="390" cy="215" r="3" fill="#4ade80"/>
    <rect x="230" y="270" width="150" height="30" rx="6" fill="#1e293b" stroke="#4ade80" stroke-width="1"/>
    <text x="240" y="286" font-weight="700" fill="#4ade80">Petiole (Leaf Stalk)</text>
    <text x="240" y="296" font-size="10" fill="#94a3b8">Connects blade to stem axis</text>

    <!-- Axillary Bud Callout -->
    <line x1="486" y1="272" x2="680" y2="210" stroke="#facc15" stroke-width="1.5"/>
    <circle cx="486" cy="272" r="3" fill="#facc15"/>
    <rect x="680" y="195" width="230" height="32" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
    <text x="690" y="212" font-weight="700" fill="#facc15">Axillary / Lateral Bud</text>
    <text x="690" y="223" font-size="10" fill="#94a3b8">Gives rise to lateral vegetative branches</text>

    <!-- Node & Internode Callout -->
    <line x1="505" y1="250" x2="680" y2="270" stroke="#cbd5e1" stroke-width="1.5"/>
    <circle cx="505" cy="250" r="3" fill="#cbd5e1"/>
    <rect x="680" y="255" width="230" height="32" rx="6" fill="#1e293b" stroke="#cbd5e1" stroke-width="1"/>
    <text x="690" y="272" font-weight="700" fill="#e2e8f0">Node vs Internode</text>
    <text x="690" y="283" font-size="10" fill="#94a3b8">Node: leaf point; Internode: stem segment</text>

    <!-- Taproot Callout -->
    <line x1="480" y1="470" x2="680" y2="440" stroke="#fbbf24" stroke-width="1.5"/>
    <circle cx="480" cy="470" r="3" fill="#fbbf24"/>
    <rect x="680" y="425" width="230" height="32" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="690" y="442" font-weight="700" fill="#fbbf24">Primary Taproot</text>
    <text x="690" y="453" font-size="10" fill="#94a3b8">Main central axis derived from radicle</text>

    <!-- Lateral Roots Callout -->
    <line x1="610" y1="495" x2="680" y2="495" stroke="#fbbf24" stroke-width="1.5"/>
    <circle cx="610" cy="495" r="3" fill="#fbbf24"/>
    <rect x="680" y="480" width="230" height="32" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="690" y="497" font-weight="700" fill="#fbbf24">Lateral (Branch) Roots</text>
    <text x="690" y="508" font-size="10" fill="#94a3b8">Originate endogenously from pericycle</text>

    <!-- Root Hairs Callout -->
    <line x1="320" y1="465" x2="160" y2="465" stroke="#fef08a" stroke-width="1.5"/>
    <circle cx="320" cy="465" r="3" fill="#fef08a"/>
    <rect x="140" y="450" width="190" height="32" rx="6" fill="#1e293b" stroke="#fef08a" stroke-width="1"/>
    <text x="150" y="467" font-weight="700" fill="#fef08a">Root Hairs (Zone of Maturation)</text>
    <text x="150" y="478" font-size="10" fill="#94a3b8">Single-cell epidermal absorptive extensions</text>

    <!-- Root Cap & RAM Callout -->
    <line x1="480" y1="595" x2="680" y2="570" stroke="#fde68a" stroke-width="1.5"/>
    <circle cx="480" cy="595" r="3" fill="#fde68a"/>
    <rect x="680" y="555" width="230" height="42" rx="6" fill="#1e293b" stroke="#fde68a" stroke-width="1"/>
    <text x="690" y="572" font-weight="700" fill="#fde68a">Root Cap &amp; RAM (Apical Meristem)</text>
    <text x="690" y="583" font-size="10" fill="#94a3b8">Mucilage secretion, gravitropism columella</text>
    <text x="690" y="593" font-size="9" fill="#64748b">Zones: Division &#x2192; Elongation &#x2192; Maturation</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 2. FERN STRUCTURE & LIFE CYCLE SVG
# -------------------------------------------------------------
fern_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 650" width="100%" height="100%" style="background:#0b111e; font-family:'Segoe UI', -apple-system, sans-serif;">
  <defs>
    <linearGradient id="frondGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#10b981"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="prothallusGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#34d399"/>
      <stop offset="100%" stop-color="#059669"/>
    </linearGradient>
  </defs>

  <!-- Title Panel -->
  <rect x="25" y="15" width="900" height="60" rx="12" fill="#152033" stroke="#2a3952" stroke-width="1.5"/>
  <text x="475" y="42" text-anchor="middle" fill="#f1f5f9" font-size="19" font-weight="700">Fern Architecture &amp; Reproductive Anatomy (Polypodiopsida)</text>
  <text x="475" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Sporophyte (2n) Frond &amp; Sorus Biomechanics vs. Gametophyte (1n) Prothallus</text>

  <!-- LEFT PANEL: SPOROPHYTE (2n) -->
  <rect x="30" y="90" width="410" height="535" rx="14" fill="#111c2e" stroke="#10b981" stroke-width="1.5"/>
  <text x="235" y="120" text-anchor="middle" fill="#34d399" font-size="16" font-weight="700">A. Diploid Sporophyte (2n)</text>
  <text x="235" y="138" text-anchor="middle" fill="#94a3b8" font-size="11">Conspicuous, vascular leafy plant in nature</text>

  <!-- Rhizome & Roots -->
  <path d="M 80,560 Q 180,550 280,560" fill="none" stroke="#78350f" stroke-width="14" stroke-linecap="round"/>
  <text x="180" y="585" fill="#fde68a" font-size="11" font-weight="600" text-anchor="middle">Horizontal Rhizome (Stem)</text>
  <!-- Adventitious roots -->
  <g stroke="#92400e" stroke-width="2.5">
    <path d="M 110,565 Q 100,595 90,615"/>
    <path d="M 140,565 Q 140,595 130,615"/>
    <path d="M 180,565 Q 190,595 190,615"/>
    <path d="M 220,565 Q 230,595 240,615"/>
  </g>
  <text x="130" y="612" fill="#fbbf24" font-size="10" text-anchor="end">Adventitious Roots</text>

  <!-- Crozier / Fiddlehead -->
  <path d="M 100,555 C 100,480 120,440 125,430 C 130,410 160,410 155,430 C 150,445 135,445 140,435" fill="none" stroke="#22c55e" stroke-width="6" stroke-linecap="round"/>
  <text x="175" y="435" fill="#86efac" font-size="11" font-weight="600">Crozier / Fiddlehead</text>
  <text x="175" y="448" fill="#94a3b8" font-size="9">(Circinate Vernation)</text>

  <!-- Main Stipe & Rachis -->
  <path d="M 230,555 Q 230,370 210,160" fill="none" stroke="#15803d" stroke-width="8" stroke-linecap="round"/>
  <!-- Stipe callout -->
  <line x1="230" y1="490" x2="310" y2="490" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="230" cy="490" r="3" fill="#38bdf8"/>
  <text x="315" y="494" fill="#38bdf8" font-size="11" font-weight="600">Stipe (Petiole of Frond)</text>

  <!-- Rachis callout -->
  <line x1="220" y1="310" x2="310" y2="310" stroke="#38bdf8" stroke-width="1.5"/>
  <circle cx="220" cy="310" r="3" fill="#38bdf8"/>
  <text x="315" y="314" fill="#38bdf8" font-size="11" font-weight="600">Rachis (Central Leaf Axis)</text>

  <!-- Frond Pinnae (Leaflets) -->
  <g fill="url(#frondGrad)" stroke="#065f46" stroke-width="1">
    <!-- Pinna Pair 1 -->
    <path d="M 220,380 Q 150,370 90,390 Q 150,400 220,385 Z"/>
    <path d="M 225,378 Q 295,368 355,388 Q 295,398 225,383 Z"/>
    <!-- Pinna Pair 2 -->
    <path d="M 215,310 Q 140,300 80,315 Q 140,325 215,315 Z"/>
    <path d="M 220,308 Q 295,298 355,313 Q 295,323 220,313 Z"/>
    <!-- Pinna Pair 3 -->
    <path d="M 212,240 Q 140,230 90,240 Q 140,250 212,245 Z"/>
    <path d="M 215,238 Q 285,228 335,238 Q 285,248 215,243 Z"/>
    <!-- Apex -->
    <path d="M 210,180 Q 160,170 120,175 Q 160,185 210,185 Z"/>
    <path d="M 210,178 Q 260,168 300,173 Q 260,183 210,183 Z"/>
    <path d="M 210,160 Q 210,140 210,135 Q 215,140 210,160 Z"/>
  </g>
  <text x="75" y="310" fill="#6ee7b7" font-size="11" font-weight="600" text-anchor="end">Pinna (Leaflet)</text>
  <text x="75" y="323" fill="#94a3b8" font-size="9" text-anchor="end">Subdivided into Pinnules</text>

  <!-- RIGHT TOP PANEL: SORUS & SPORANGIUM BIOMECHANICS -->
  <rect x="460" y="90" width="460" height="260" rx="14" fill="#111c2e" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="690" y="118" text-anchor="middle" fill="#60a5fa" font-size="15" font-weight="700">B. Sorus &amp; Annulus Catapult Biomechanics</text>

  <!-- Indusium & Sporangia Cluster -->
  <g transform="translate(480, 140)">
    <!-- Leaf Blade Slice -->
    <rect x="10" y="0" width="170" height="12" fill="#15803d" rx="3"/>
    <text x="95" y="-5" fill="#86efac" font-size="10" text-anchor="middle">Fertile Frond (Abaxial Surface)</text>
    
    <!-- Umbrella Indusium -->
    <path d="M 95,12 L 95,45 Q 40,55 30,30 Q 95,40 160,30 Q 150,55 95,45" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
    <text x="95" y="62" fill="#cbd5e1" font-size="10" text-anchor="middle">Indusium (Protective Flap)</text>

    <!-- Cluster of Stalked Sporangia -->
    <circle cx="65" cy="28" r="8" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="65" y1="20" x2="75" y2="12" stroke="#d97706" stroke-width="2"/>
    <circle cx="85" cy="25" r="8" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="85" y1="17" x2="90" y2="12" stroke="#d97706" stroke-width="2"/>
    <circle cx="115" cy="26" r="8" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="115" y1="18" x2="105" y2="12" stroke="#d97706" stroke-width="2"/>
    <circle cx="130" cy="30" r="8" fill="#d97706" stroke="#f59e0b" stroke-width="1.5"/>
    <line x1="130" y1="22" x2="115" y2="12" stroke="#d97706" stroke-width="2"/>
    <text x="95" y="80" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Sorus (Cluster of Sporangia)</text>
  </g>

  <!-- Detailed Single Sporangium with Annulus -->
  <g transform="translate(680, 135)">
    <!-- Stalk -->
    <line x1="80" y1="120" x2="80" y2="80" stroke="#d97706" stroke-width="4"/>
    <!-- Capsule -->
    <circle cx="80" cy="50" r="32" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
    
    <!-- Annulus Crest (differential thick walls) -->
    <path d="M 50,50 A 30,30 0 1,1 110,50" fill="none" stroke="#ef4444" stroke-width="8" stroke-dasharray="7,3"/>
    
    <!-- Stomium (Lip cells) -->
    <circle cx="48" cy="56" r="4" fill="#fbbf24"/>
    <circle cx="48" cy="66" r="4" fill="#fbbf24"/>
    
    <!-- Internal Haploid Spores -->
    <circle cx="75" cy="45" r="4" fill="#fef08a"/><circle cx="85" cy="42" r="4" fill="#fef08a"/>
    <circle cx="80" cy="55" r="4" fill="#fef08a"/><circle cx="90" cy="54" r="4" fill="#fef08a"/>
    <circle cx="70" cy="55" r="4" fill="#fef08a"/>

    <!-- Labels -->
    <text x="135" y="30" fill="#f87171" font-size="11" font-weight="700">Annulus (Thickened)</text>
    <text x="135" y="43" fill="#94a3b8" font-size="9">Dries &#x2192; Water Tension &#x2192; Cavitation</text>
    <text x="135" y="55" fill="#94a3b8" font-size="9">Snaps forward to catapult spores</text>

    <text x="40" y="85" fill="#fbbf24" font-size="10" font-weight="600" text-anchor="end">Stomium (Tears Open)</text>
    <text x="80" y="75" fill="#fef08a" font-size="10" font-weight="600" text-anchor="middle">Spores (1n)</text>
  </g>

  <!-- RIGHT BOTTOM PANEL: GAMETOPHYTE / PROTHALLUS (1n) -->
  <rect x="460" y="365" width="460" height="260" rx="14" fill="#111c2e" stroke="#10b981" stroke-width="1.5"/>
  <text x="690" y="392" text-anchor="middle" fill="#34d399" font-size="15" font-weight="700">C. Haploid Gametophyte (1n) — Prothallus</text>
  <text x="690" y="408" text-anchor="middle" fill="#94a3b8" font-size="10">Free-living, photosynthetic heart-shaped thallus (~0.5–1 cm)</text>

  <!-- Heart-shaped Prothallus -->
  <g transform="translate(560, 420)">
    <path d="M 120,40 C 90,-20 10,-10 10,60 C 10,120 120,170 120,170 C 120,170 230,120 230,60 C 230,-10 150,-20 120,40 Z" fill="url(#prothallusGrad)" stroke="#059669" stroke-width="2" filter="url(#shadow)"/>
    
    <!-- Apical Notch -->
    <circle cx="120" cy="35" r="4" fill="#0b111e"/>
    <text x="120" y="15" fill="#a7f3d0" font-size="11" font-weight="600" text-anchor="middle">Apical Notch</text>

    <!-- Archegonia (Female gametangia - near notch) -->
    <g fill="#ec4899" stroke="#be185d" stroke-width="1">
      <circle cx="110" cy="55" r="4"/><circle cx="120" cy="60" r="4"/><circle cx="130" cy="55" r="4"/>
      <circle cx="115" cy="70" r="4"/><circle cx="125" cy="70" r="4"/>
    </g>
    <line x1="135" y1="65" x2="190" y2="65" stroke="#ec4899" stroke-width="1.5"/>
    <text x="195" y="69" fill="#f472b6" font-size="11" font-weight="700">Archegonia (&#x2640;)</text>
    <text x="195" y="80" fill="#94a3b8" font-size="9">Produce single egg</text>

    <!-- Antheridia (Male gametangia - near base & rhizoids) -->
    <g fill="#38bdf8" stroke="#0284c7" stroke-width="1">
      <circle cx="95" cy="115" r="4"/><circle cx="110" cy="125" r="4"/><circle cx="130" cy="125" r="4"/>
      <circle cx="145" cy="115" r="4"/><circle cx="105" cy="140" r="4"/><circle cx="135" cy="140" r="4"/>
    </g>
    <line x1="90" y1="125" x2="30" y2="125" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="25" y="129" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="end">Antheridia (&#x2642;)</text>
    <text x="25" y="140" fill="#94a3b8" font-size="9" text-anchor="end">Produce swimming flagellated sperm</text>
    <text x="25" y="151" fill="#f59e0b" font-size="9" text-anchor="end">(Requires free water film!)</text>

    <!-- Rhizoids -->
    <g stroke="#d97706" stroke-width="1.5" stroke-linecap="round">
      <path d="M 110,155 Q 100,180 90,195"/>
      <path d="M 120,165 Q 120,190 115,205"/>
      <path d="M 130,155 Q 140,180 145,195"/>
      <path d="M 115,160 Q 105,185 100,200"/>
    </g>
    <text x="155" y="195" fill="#fbbf24" font-size="11" font-weight="600">Rhizoids (Anchorage)</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 3. FLOWER STRUCTURE & OVARY INSERTION SVG
# -------------------------------------------------------------
flower_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 650" width="100%" height="100%" style="background:#0c101d; font-family:'Segoe UI', -apple-system, sans-serif;">
  <defs>
    <linearGradient id="petalGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="ovaryGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4ade80"/>
      <stop offset="100%" stop-color="#15803d"/>
    </linearGradient>
  </defs>

  <!-- Title Panel -->
  <rect x="25" y="15" width="900" height="60" rx="12" fill="#161e31" stroke="#2d3b55" stroke-width="1.5"/>
  <text x="475" y="42" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="700">Floral Architecture &amp; The Four Concentric Whorls</text>
  <text x="475" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Angiosperm Reproductive Morphology &amp; Ovary Insertion Typologies</text>

  <!-- MAIN FLOWER DIAGRAM (Center-Left) -->
  <g transform="translate(180, 50)">
    <!-- Pedicel & Receptacle -->
    <path d="M 190,480 L 190,400" stroke="#15803d" stroke-width="16" stroke-linecap="round"/>
    <path d="M 140,400 Q 190,420 240,400 Q 210,380 190,380 Q 170,380 140,400 Z" fill="#166534" stroke="#14532d" stroke-width="2"/>
    <text x="190" y="505" fill="#86efac" font-size="12" font-weight="600" text-anchor="middle">Pedicel (Flower Stalk)</text>
    <text x="245" y="415" fill="#86efac" font-size="12" font-weight="600">Receptacle</text>

    <!-- WHORL 1: CALYX (Sepals) -->
    <path d="M 145,395 C 100,380 70,330 60,290 C 90,330 130,360 155,385 Z" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <path d="M 235,395 C 280,380 310,330 320,290 C 290,330 250,360 225,385 Z" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <text x="40" y="285" fill="#4ade80" font-size="12" font-weight="700">Sepal (Whorl 1: Calyx)</text>

    <!-- WHORL 2: COROLLA (Petals) -->
    <path d="M 155,380 C 70,340 30,220 80,140 C 130,170 150,260 170,360 Z" fill="url(#petalGrad)" opacity="0.9" stroke="#9f1239" stroke-width="2"/>
    <path d="M 225,380 C 310,340 350,220 300,140 C 250,170 230,260 210,360 Z" fill="url(#petalGrad)" opacity="0.9" stroke="#9f1239" stroke-width="2"/>
    <text x="320" y="135" fill="#fb7185" font-size="12" font-weight="700">Petal (Whorl 2: Corolla)</text>

    <!-- WHORL 3: ANDROECIUM (Stamens - Filament & Anther) -->
    <!-- Left Stamen -->
    <path d="M 175,370 Q 130,280 125,180" fill="none" stroke="#fef08a" stroke-width="4"/>
    <!-- Left Anther (4 pollen sacs) -->
    <g transform="translate(125, 175)">
      <rect x="-14" y="-12" width="28" height="24" rx="6" fill="#eab308" stroke="#a16207" stroke-width="1.5"/>
      <circle cx="-6" cy="-4" r="3" fill="#fef08a"/><circle cx="6" cy="-4" r="3" fill="#fef08a"/>
      <circle cx="-6" cy="4" r="3" fill="#fef08a"/><circle cx="6" cy="4" r="3" fill="#fef08a"/>
    </g>

    <!-- Right Stamen -->
    <path d="M 205,370 Q 250,280 255,180" fill="none" stroke="#fef08a" stroke-width="4"/>
    <g transform="translate(255, 175)">
      <rect x="-14" y="-12" width="28" height="24" rx="6" fill="#eab308" stroke="#a16207" stroke-width="1.5"/>
      <circle cx="-6" cy="-4" r="3" fill="#fef08a"/><circle cx="6" cy="-4" r="3" fill="#fef08a"/>
      <circle cx="-6" cy="4" r="3" fill="#fef08a"/><circle cx="6" cy="4" r="3" fill="#fef08a"/>
    </g>

    <!-- WHORL 4: GYNOECIUM (Carpel / Pistil: Stigma, Style, Ovary, Ovule) -->
    <!-- Ovary Base -->
    <ellipse cx="190" cy="355" rx="30" ry="32" fill="url(#ovaryGrad)" stroke="#166534" stroke-width="2"/>
    <!-- Style Neck -->
    <rect x="186" y="200" width="8" height="125" fill="#4ade80" stroke="#16a34a" stroke-width="1"/>
    <!-- Stigma Lobe (Sticky surface) -->
    <ellipse cx="190" cy="195" rx="16" ry="8" fill="#86efac" stroke="#15803d" stroke-width="2"/>
    <circle cx="182" cy="195" r="3" fill="#fbbf24"/><circle cx="198" cy="195" r="3" fill="#fbbf24"/>

    <!-- Internal Ovules inside Ovary Cross-section -->
    <ellipse cx="180" cy="355" rx="8" ry="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <circle cx="180" cy="355" r="3" fill="#f59e0b"/>
    <ellipse cx="200" cy="355" rx="8" ry="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <circle cx="200" cy="355" r="3" fill="#f59e0b"/>

    <!-- BRACKETS & CALLOUTS FOR WHORLS -->
    <!-- Stamen Bracket Callout -->
    <line x1="110" y1="175" x2="30" y2="175" stroke="#facc15" stroke-width="1.5"/>
    <rect x="-140" y="160" width="165" height="42" rx="6" fill="#1e293b" stroke="#facc15" stroke-width="1"/>
    <text x="-130" y="177" font-weight="700" fill="#facc15" font-size="11">Anther + Filament</text>
    <text x="-130" y="193" fill="#e2e8f0" font-size="11">= STAMEN (Androecium)</text>

    <!-- Pistil Bracket Callout -->
    <line x1="206" y1="195" x2="320" y2="195" stroke="#34d399" stroke-width="1.5"/>
    <text x="325" y="199" fill="#34d399" font-size="11" font-weight="700">Stigma (Receptive surface)</text>

    <line x1="194" y1="260" x2="320" y2="260" stroke="#34d399" stroke-width="1.5"/>
    <text x="325" y="264" fill="#34d399" font-size="11" font-weight="700">Style (Pollen tube conduit)</text>

    <line x1="220" y1="355" x2="320" y2="355" stroke="#34d399" stroke-width="1.5"/>
    <text x="325" y="352" fill="#34d399" font-size="11" font-weight="700">Ovary (Houses ovules)</text>
    <text x="325" y="365" fill="#fde68a" font-size="10">&#x2192; Ovule (Becomes seed)</text>
    <text x="325" y="377" fill="#86efac" font-size="10">= CARPEL / PISTIL (Gynoecium)</text>
  </g>

  <!-- RIGHT PANEL: OVARY INSERTION (Superior vs Inferior) -->
  <rect x="580" y="90" width="345" height="535" rx="14" fill="#111827" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="752" y="120" text-anchor="middle" fill="#60a5fa" font-size="16" font-weight="700">Ovary Insertion &amp; Flower Geometry</text>
  <text x="752" y="138" text-anchor="middle" fill="#94a3b8" font-size="11">Taxonomic placement relative to receptacle</text>

  <!-- Diagram 1: Hypogynous (Superior) -->
  <g transform="translate(600, 160)">
    <rect x="10" y="0" width="290" height="135" rx="8" fill="#1f2937" stroke="#374151" stroke-width="1"/>
    <text x="25" y="24" fill="#34d399" font-size="13" font-weight="700">1. Hypogynous (Superior Ovary)</text>
    <!-- Mini diagram -->
    <!-- Ovary sits on top of receptacle -->
    <ellipse cx="70" cy="75" rx="16" ry="18" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <path d="M 40,95 Q 70,105 100,95" fill="none" stroke="#64748b" stroke-width="4"/> <!-- Receptacle -->
    <!-- Petals/stamens emerge BELOW ovary -->
    <path d="M 45,95 Q 25,65 35,45" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <path d="M 95,95 Q 115,65 105,45" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <line x1="50" y1="95" x2="50" y2="55" stroke="#facc15" stroke-width="1.5"/>
    <line x1="90" y1="95" x2="90" y2="55" stroke="#facc15" stroke-width="1.5"/>
    <!-- Text explanation -->
    <text x="130" y="55" fill="#f8fafc" font-size="11" font-weight="600">Sepals, petals &amp; stamens</text>
    <text x="130" y="70" fill="#f8fafc" font-size="11" font-weight="600">insert <tspan fill="#34d399">BELOW</tspan> ovary base.</text>
    <text x="130" y="90" fill="#94a3b8" font-size="10">Ovary free and superior.</text>
    <text x="130" y="105" fill="#a7f3d0" font-size="10">Examples: Tomato, Citrus, Lily</text>
  </g>

  <!-- Diagram 2: Perigynous (Hypanthium) -->
  <g transform="translate(600, 310)">
    <rect x="10" y="0" width="290" height="135" rx="8" fill="#1f2937" stroke="#374151" stroke-width="1"/>
    <text x="25" y="24" fill="#fbbf24" font-size="13" font-weight="700">2. Perigynous (Superior + Hypanthium)</text>
    <!-- Cup-like hypanthium surrounding ovary -->
    <path d="M 35,55 C 35,95 105,95 105,55" fill="none" stroke="#ca8a04" stroke-width="3"/>
    <ellipse cx="70" cy="72" rx="14" ry="16" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <!-- Petals on rim of cup -->
    <path d="M 35,55 Q 20,35 30,20" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <path d="M 105,55 Q 120,35 110,20" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <!-- Text explanation -->
    <text x="130" y="55" fill="#f8fafc" font-size="11" font-weight="600">Cup-shaped <tspan fill="#facc15">Hypanthium</tspan></text>
    <text x="130" y="70" fill="#f8fafc" font-size="11" font-weight="600">surrounds ovary without fusion.</text>
    <text x="130" y="90" fill="#94a3b8" font-size="10">Ovary technically superior.</text>
    <text x="130" y="105" fill="#fde68a" font-size="10">Examples: Cherry, Peach, Rose</text>
  </g>

  <!-- Diagram 3: Epigynous (Inferior) -->
  <g transform="translate(600, 460)">
    <rect x="10" y="0" width="290" height="145" rx="8" fill="#1f2937" stroke="#374151" stroke-width="1"/>
    <text x="25" y="24" fill="#f87171" font-size="13" font-weight="700">3. Epigynous (Inferior Ovary)</text>
    <!-- Receptacle completely fused around ovary -->
    <ellipse cx="70" cy="80" rx="16" ry="18" fill="#22c55e" stroke="#15803d" stroke-width="1.5"/>
    <path d="M 50,65 C 45,95 95,95 90,65" fill="none" stroke="#64748b" stroke-width="4"/>
    <!-- Petals emerge from TOP of ovary -->
    <path d="M 52,65 Q 35,45 45,25" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <path d="M 88,65 Q 105,45 95,25" fill="none" stroke="#f43f5e" stroke-width="2"/>
    <line x1="58" y1="65" x2="58" y2="35" stroke="#facc15" stroke-width="1.5"/>
    <line x1="82" y1="65" x2="82" y2="35" stroke="#facc15" stroke-width="1.5"/>
    <!-- Text explanation -->
    <text x="130" y="55" fill="#f8fafc" font-size="11" font-weight="600">Receptacle fused to ovary wall;</text>
    <text x="130" y="70" fill="#f8fafc" font-size="11" font-weight="600">parts arise <tspan fill="#f87171">ABOVE</tspan> ovary.</text>
    <text x="130" y="90" fill="#94a3b8" font-size="10">Ovary inferior / buried in flesh.</text>
    <text x="130" y="105" fill="#fca5a5" font-size="10">Examples: Apple, Squash, Cucumber</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 4. SEED STRUCTURE (Eudicot vs Monocot vs Gymnosperm) SVG
# -------------------------------------------------------------
seed_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 650" width="100%" height="100%" style="background:#0c111c; font-family:'Segoe UI', -apple-system, sans-serif;">
  <defs>
    <linearGradient id="endoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#fde047"/>
    </linearGradient>
    <linearGradient id="cotGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#86efac"/>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>
  </defs>

  <!-- Title Panel -->
  <rect x="25" y="15" width="900" height="60" rx="12" fill="#141c2b" stroke="#253347" stroke-width="1.5"/>
  <text x="475" y="42" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="700">Comparative Seed Anatomy &amp; Embryology</text>
  <text x="475" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Eudicot (Non-Endospermic) vs. Monocot (Endospermic) vs. Gymnosperm (Naked Conifer Seed)</text>

  <!-- PANEL 1: EUDICOT SEED (Garden Bean) -->
  <rect x="30" y="90" width="280" height="535" rx="14" fill="#111827" stroke="#10b981" stroke-width="1.5"/>
  <text x="170" y="122" text-anchor="middle" fill="#34d399" font-size="15" font-weight="700">A. Eudicot Seed (Bean)</text>
  <text x="170" y="140" text-anchor="middle" fill="#94a3b8" font-size="10">Non-endospermic; food stored in cotyledons</text>

  <!-- Bean Drawing -->
  <g transform="translate(60, 160)">
    <!-- Seed Coat (Testa) Outline -->
    <path d="M 60,10 C 140,10 180,70 180,150 C 180,240 140,300 60,300 C 10,300 -10,240 10,150 C 20,90 20,40 60,10 Z" fill="#1f2937" stroke="#374151" stroke-width="3"/>
    
    <!-- Large Fleshy Cotyledon -->
    <path d="M 60,16 C 130,16 170,72 170,150 C 170,230 130,290 60,290 C 25,290 15,240 28,150 C 35,90 35,40 60,16 Z" fill="url(#cotGrad)" opacity="0.85"/>
    
    <!-- Embryonic Axis -->
    <!-- Radicle (Root) -->
    <path d="M 45,150 Q 30,180 35,210" fill="none" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>
    <!-- Hypocotyl (Stem below cotyledon) -->
    <circle cx="45" cy="150" r="7" fill="#fbbf24"/>
    <!-- Epicotyl / Plumule (First True Leaves) -->
    <path d="M 45,150 Q 55,120 70,110" fill="none" stroke="#15803d" stroke-width="6"/>
    <path d="M 70,110 Q 75,95 85,95 Q 85,110 70,110" fill="#22c55e"/>

    <!-- Seed Coat Cross-Section Edge -->
    <path d="M 60,10 C 140,10 180,70 180,150" fill="none" stroke="#92400e" stroke-width="4"/>

    <!-- Labels -->
    <text x="100" y="45" fill="#fde68a" font-size="11" font-weight="700">Seed Coat (Testa, 2n)</text>
    
    <text x="110" y="200" fill="#a7f3d0" font-size="11" font-weight="700">Two Cotyledons</text>
    <text x="110" y="214" fill="#94a3b8" font-size="9">(Absorbed endosperm)</text>

    <text x="80" y="90" fill="#4ade80" font-size="11" font-weight="700">Epicotyl (Plumule)</text>
    <text x="80" y="102" fill="#94a3b8" font-size="9">Shoot apex + embryonic leaves</text>

    <text x="-15" y="145" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="end">Hypocotyl</text>
    <text x="-15" y="157" fill="#94a3b8" font-size="9" text-anchor="end">Embryonic stem</text>

    <text x="-15" y="210" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="end">Radicle</text>
    <text x="-15" y="222" fill="#94a3b8" font-size="9" text-anchor="end">Embryonic root tip</text>
  </g>

  <!-- PANEL 2: MONOCOT SEED (Corn Caryopsis) -->
  <rect x="335" y="90" width="280" height="535" rx="14" fill="#111827" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="475" y="122" text-anchor="middle" fill="#60a5fa" font-size="15" font-weight="700">B. Monocot Grain (Corn)</text>
  <text x="475" y="140" text-anchor="middle" fill="#94a3b8" font-size="10">Endospermic; single cotyledon (scutellum)</text>

  <!-- Corn Grain Drawing -->
  <g transform="translate(370, 160)">
    <!-- Grain Silhouette -->
    <path d="M 30,10 C 130,10 170,40 180,100 C 190,190 150,280 100,305 C 60,305 20,230 15,160 C 10,80 10,20 30,10 Z" fill="#1f2937" stroke="#374151" stroke-width="3"/>

    <!-- Large Starchy Endosperm (3n) -->
    <path d="M 34,16 C 125,16 165,42 174,100 C 180,160 145,190 100,180 C 65,175 40,140 30,80 Z" fill="url(#endoGrad)" opacity="0.9"/>
    
    <!-- Scutellum (Shield-shaped single cotyledon) -->
    <path d="M 30,80 C 40,140 65,175 100,180 C 145,190 160,250 100,298 C 65,298 25,230 20,160 Z" fill="#6ee7b7" opacity="0.8"/>

    <!-- Embryo inside Scutellum: Coleoptile, Plumule, Radicle, Coleorhiza -->
    <!-- Coleoptile sheath enclosing shoot -->
    <path d="M 50,180 Q 70,160 85,180" fill="none" stroke="#38bdf8" stroke-width="4"/>
    <circle cx="68" cy="182" r="5" fill="#22c55e"/> <!-- Plumule inside -->
    <!-- Coleorhiza sheath enclosing radicle -->
    <path d="M 55,250 Q 75,270 90,250" fill="none" stroke="#f59e0b" stroke-width="4"/>
    <circle cx="72" cy="245" r="5" fill="#eab308"/> <!-- Radicle inside -->

    <!-- Fused Pericarp-Testa (Fruit wall fused to seed coat) -->
    <path d="M 30,10 C 130,10 170,40 180,100" fill="none" stroke="#ea580c" stroke-width="4"/>

    <!-- Labels -->
    <text x="100" y="55" fill="#ea580c" font-size="11" font-weight="700">Fused Pericarp + Testa</text>
    <text x="100" y="68" fill="#94a3b8" font-size="9">(Caryopsis coat)</text>

    <text x="90" y="115" fill="#eab308" font-size="12" font-weight="700">Endosperm (3n)</text>
    <text x="90" y="128" fill="#94a3b8" font-size="9">Massive starch energy reserve</text>

    <text x="95" y="210" fill="#34d399" font-size="11" font-weight="700">Scutellum (Cotyledon)</text>
    <text x="95" y="222" fill="#94a3b8" font-size="9">Absorptive interface organ</text>

    <text x="-10" y="180" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="end">Coleoptile</text>
    <text x="-10" y="192" fill="#94a3b8" font-size="9" text-anchor="end">Protective shoot sheath</text>

    <text x="-10" y="255" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="end">Coleorhiza</text>
    <text x="-10" y="267" fill="#94a3b8" font-size="9" text-anchor="end">Protective root cap sheath</text>
  </g>

  <!-- PANEL 3: GYMNOSPERM SEED (Pine) -->
  <rect x="640" y="90" width="280" height="535" rx="14" fill="#111827" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="780" y="122" text-anchor="middle" fill="#fbbf24" font-size="15" font-weight="700">C. Gymnosperm Seed (Pinus)</text>
  <text x="780" y="140" text-anchor="middle" fill="#94a3b8" font-size="10">Naked seed; haploid gametophyte nutritive tissue</text>

  <!-- Pine Seed Drawing -->
  <g transform="translate(670, 160)">
    <!-- Wing extension -->
    <path d="M 60,30 C 120,-30 190,-40 210,-40 C 200,40 170,100 120,130 Z" fill="#ca8a04" opacity="0.3" stroke="#eab308" stroke-width="1" stroke-dasharray="4,2"/>
    <text x="180" y="-10" fill="#fef08a" font-size="10">Seed Wing (Wind dispersal)</text>

    <!-- Seed Body -->
    <ellipse cx="75" cy="160" rx="60" ry="110" fill="#1f2937" stroke="#374151" stroke-width="3"/>
    
    <!-- Maternal Seed Coat (Integument, 2n) -->
    <ellipse cx="75" cy="160" rx="58" ry="108" fill="none" stroke="#78350f" stroke-width="6"/>

    <!-- Haploid Female Gametophyte Nutritive Tissue (1n) -->
    <ellipse cx="75" cy="160" rx="46" ry="94" fill="#fef3c7" opacity="0.85"/>

    <!-- Central Embryo (2n) with multiple needle cotyledons -->
    <!-- Hypocotyl-radicle axis -->
    <path d="M 75,130 L 75,220" stroke="#f59e0b" stroke-width="8" stroke-linecap="round"/>
    <!-- Multiple Cotyledons (whorled needle rays) -->
    <g stroke="#15803d" stroke-width="4" stroke-linecap="round">
      <line x1="75" y1="130" x2="55" y2="95"/>
      <line x1="75" y1="130" x2="65" y2="85"/>
      <line x1="75" y1="130" x2="75" y2="80"/>
      <line x1="75" y1="130" x2="85" y2="85"/>
      <line x1="75" y1="130" x2="95" y2="95"/>
    </g>

    <!-- Labels -->
    <text x="75" y="55" fill="#fef08a" font-size="11" font-weight="700" text-anchor="middle">Multiple Cotyledons</text>
    <text x="75" y="68" fill="#94a3b8" font-size="9" text-anchor="middle">(Whorled needle leaves)</text>

    <text x="140" y="160" fill="#ca8a04" font-size="11" font-weight="700">Female Gametophyte (1n)</text>
    <text x="140" y="172" fill="#94a3b8" font-size="9">Nutritive tissue formed</text>
    <text x="140" y="184" fill="#fbbf24" font-size="9">BEFORE fertilization!</text>

    <text x="140" y="215" fill="#f59e0b" font-size="11" font-weight="700">Embryo (2n)</text>
    <text x="140" y="227" fill="#94a3b8" font-size="9">New sporophyte generation</text>

    <text x="75" y="295" fill="#d97706" font-size="11" font-weight="700" text-anchor="middle">Seed Coat (Testa, 2n)</text>
    <text x="75" y="307" fill="#94a3b8" font-size="9" text-anchor="middle">Maternal sporophyte integument</text>
  </g>
</svg>"""

# -------------------------------------------------------------
# 5. BONUS: PLANETARY STRUCTURE (Terrestrial Planet / Earth) SVG
# -------------------------------------------------------------
planet_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 650" width="100%" height="100%" style="background:#090d16; font-family:'Segoe UI', -apple-system, sans-serif;">
  <defs>
    <radialGradient id="innerCoreGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="60%" stop-color="#fef08a"/>
      <stop offset="100%" stop-color="#f59e0b"/>
    </radialGradient>
    <radialGradient id="outerCoreGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#ea580c"/>
      <stop offset="100%" stop-color="#dc2626"/>
    </radialGradient>
    <radialGradient id="mantleGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="60%" stop-color="#991b1b"/>
      <stop offset="100%" stop-color="#7c2d12"/>
    </radialGradient>
  </defs>

  <!-- Title Panel -->
  <rect x="25" y="15" width="900" height="60" rx="12" fill="#141c2b" stroke="#253347" stroke-width="1.5"/>
  <text x="475" y="42" text-anchor="middle" fill="#f8fafc" font-size="19" font-weight="700">Internal Geosphere Structure of a Terrestrial Planet (Earth)</text>
  <text x="475" y="62" text-anchor="middle" fill="#94a3b8" font-size="12">Concentric Mechanical &amp; Compositional Layering from Solid Crust to Super-Dense Metallic Core</text>

  <!-- Cutaway Globe Diagram -->
  <g transform="translate(300, 350)">
    <!-- Mantle Base Circle -->
    <circle cx="0" cy="0" r="230" fill="url(#mantleGrad)" stroke="#451a03" stroke-width="3"/>
    
    <!-- Outer Core Circle -->
    <circle cx="0" cy="0" r="140" fill="url(#outerCoreGrad)" stroke="#b91c1c" stroke-width="2"/>
    
    <!-- Inner Core Circle -->
    <circle cx="0" cy="0" r="65" fill="url(#innerCoreGrad)" stroke="#d97706" stroke-width="2"/>

    <!-- Crust Outer Ring -->
    <circle cx="0" cy="0" r="236" fill="none" stroke="#38bdf8" stroke-width="6"/>
    <circle cx="0" cy="0" r="233" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="25,15,40,10"/>

    <!-- 90 Degree Cutaway Wedge Overlay for Perspective -->
    <path d="M 0,0 L 0,-240 A 240,240 0 0,1 240,0 Z" fill="#0f172a" opacity="0.85" stroke="#38bdf8" stroke-width="1.5"/>
    <!-- Wedge Cross-Section Steps -->
    <path d="M 0,0 L 0,-65 A 65,65 0 0,1 65,0 Z" fill="url(#innerCoreGrad)"/>
    <path d="M 0,-65 L 0,-140 A 140,140 0 0,1 140,0 L 65,0 A 65,65 0 0,0 0,-65 Z" fill="url(#outerCoreGrad)"/>
    <path d="M 0,-140 L 0,-233 A 233,233 0 0,1 233,0 L 140,0 A 140,140 0 0,0 0,-140 Z" fill="url(#mantleGrad)"/>
  </g>

  <!-- CALLOUT ANNOTATIONS (Right Side) -->
  <g fill="#f8fafc" font-size="12">
    <!-- Crust Callout -->
    <line x1="535" y1="350" x2="680" y2="170" stroke="#38bdf8" stroke-width="1.5"/>
    <circle cx="535" cy="350" r="4" fill="#38bdf8"/>
    <rect x="680" y="150" width="240" height="46" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="695" y="170" font-weight="700" fill="#38bdf8">1. Crust &amp; Lithosphere</text>
    <text x="695" y="185" font-size="10" fill="#cbd5e1">5–70 km thick; rigid silicate rocks</text>

    <!-- Asthenosphere & Upper Mantle -->
    <line x1="490" y1="260" x2="680" y2="245" stroke="#fb923c" stroke-width="1.5"/>
    <circle cx="490" cy="260" r="4" fill="#fb923c"/>
    <rect x="680" y="225" width="240" height="46" rx="8" fill="#1e293b" stroke="#fb923c" stroke-width="1.5"/>
    <text x="695" y="245" font-weight="700" fill="#fb923c">2. Asthenosphere (Upper Mantle)</text>
    <text x="695" y="260" font-size="10" fill="#cbd5e1">Plastic, ductile, convective silicate rock</text>

    <!-- Mesosphere / Lower Mantle -->
    <line x1="430" y1="300" x2="680" y2="320" stroke="#f87171" stroke-width="1.5"/>
    <circle cx="430" cy="300" r="4" fill="#f87171"/>
    <rect x="680" y="300" width="240" height="46" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
    <text x="695" y="320" font-weight="700" fill="#f87171">3. Lower Mantle (Mesosphere)</text>
    <text x="695" y="335" font-size="10" fill="#cbd5e1">~2,900 km depth; hot solid peridotite</text>

    <!-- Outer Core -->
    <line x1="390" y1="370" x2="680" y2="400" stroke="#facc15" stroke-width="1.5"/>
    <circle cx="390" cy="370" r="4" fill="#facc15"/>
    <rect x="680" y="380" width="240" height="52" rx="8" fill="#1e293b" stroke="#facc15" stroke-width="1.5"/>
    <text x="695" y="400" font-weight="700" fill="#facc15">4. Liquid Outer Core</text>
    <text x="695" y="414" font-size="10" fill="#cbd5e1">Liquid Iron-Nickel (Fe-Ni) alloy (~4000°C)</text>
    <text x="695" y="425" font-size="9" fill="#94a3b8">Convection powers planetary magnetic field</text>

    <!-- Inner Core -->
    <line x1="340" y1="350" x2="680" y2="480" stroke="#fef08a" stroke-width="1.5"/>
    <circle cx="340" cy="350" r="4" fill="#fef08a"/>
    <rect x="680" y="460" width="240" height="52" rx="8" fill="#1e293b" stroke="#fef08a" stroke-width="1.5"/>
    <text x="695" y="480" font-weight="700" fill="#fef08a">5. Solid Inner Core</text>
    <text x="695" y="494" font-size="10" fill="#cbd5e1">Solid crystalline Iron-Nickel under ~3.6 Mbar</text>
    <text x="695" y="505" font-size="9" fill="#94a3b8">Temperature ~5500°C (as hot as solar surface)</text>
  </g>
</svg>"""

files_to_write = [
    ("plant_body_structure.svg", plant_svg),
    ("fern_structure.svg", fern_svg),
    ("flower_structure.svg", flower_svg),
    ("seed_structure.svg", seed_svg),
    ("planetary_structure.svg", planet_svg)
]

for name, content in files_to_write:
    # Save to artifact dir
    artifact_path = os.path.join(artifact_dir, name)
    with open(artifact_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved artifact SVG: {artifact_path}")

    # Save to portal diagrams dir
    portal_path = os.path.join(portal_diagrams_dir, name)
    with open(portal_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved portal SVG: {portal_path}")

print("All 5 botanical & planetary SVGs generated successfully!")
