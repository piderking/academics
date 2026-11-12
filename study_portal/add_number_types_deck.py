import json

numbers_deck = {
    "id": "math-number-systems",
    "course": "MATH 401",
    "title": "Number Systems & Types of Numbers (Hierarchy & Notation)",
    "description": "Comprehensive deck covering all major types of numbers and their formal mathematical notation: Natural (ℕ), Whole (W), Integers (ℤ), Rationals (ℚ), Irrationals (ℝ ∖ ℚ), Reals (ℝ), Complex (ℂ), Algebraic (𝔸), Transcendental (𝕋), Primes (ℙ), Quaternions (ℍ), and Modular Rings (ℤ/nℤ).",
    "source": "Abstract Algebra, Number Theory & Real Analysis Foundations",
    "flashcards": [
        {
            "id": "num-c1",
            "front": "What does **ℕ** represent, and what is the convention regarding the number **0**?",
            "hint": "The counting numbers. Different textbooks have two conventions regarding zero.",
            "back": "**ℕ = Natural Numbers (Counting Numbers)**\n\n• **Standard definition:** `{1, 2, 3, 4, 5, ...}`.\n• **The Zero Debate:**\n  - In number theory and pre-calculus: `ℕ = {1, 2, 3, ...}` (positive integers only).\n  - In set theory and computer science: `0 ∈ ℕ` is often included (`{0, 1, 2, ...}`).\n• **Unambiguous Notation:**\n  - `ℕ*` or `ℕ₁` or `ℤ⁺`: strictly positive `{1, 2, 3, ...}`\n  - `ℕ₀` or `W`: non-negative whole numbers `{0, 1, 2, 3, ...}`.",
            "citation": "Axiomatic Set Theory (Peano Axioms)",
            "tags": ["numbers", "naturals", "notation"]
        },
        {
            "id": "num-c2",
            "front": "What does **ℤ** represent, why is it symbolized by **Z**, and how are even/odd numbers written?",
            "hint": "German word for 'numbers'. Evens are multiples of 2.",
            "back": "**ℤ = Integers (Signed Whole Numbers)**\n\n• **Definition:** `{..., -3, -2, -1, 0, 1, 2, 3, ...}`.\n• **Etymology:** From the German word ***Zahlen*** (meaning \"numbers\"), introduced by David Hilbert and the Bourbaki group.\n• **Subsets & Modifiers:**\n  - `ℤ⁺`: positive integers `{1, 2, 3, ...}` (same as ℕ).\n  - `ℤ⁻`: strictly negative integers `{-1, -2, -3, ...}`.\n  - `ℤ ≥ 0` or `ℤ*`: non-negative integers `{0, 1, 2, ...}`.\n• **Even & Odd Subsets:**\n  - **Even integers:** `2ℤ = {2k | k ∈ ℤ}`\n  - **Odd integers:** `2ℤ + 1 = {2k + 1 | k ∈ ℤ}`.",
            "citation": "Elementary Number Theory",
            "tags": ["numbers", "integers", "parity"]
        },
        {
            "id": "num-c3",
            "front": "What does **ℚ** represent, how is it formally defined in set-builder notation, and what is its decimal behavior?",
            "hint": "Symbol Q stands for 'Quotient'. Think about fractions of integers.",
            "back": "**ℚ = Rational Numbers**\n\n• **Formal Set-Builder Definition:**\n  `ℚ = { p/q | p, q ∈ ℤ, q ≠ 0 }` (where p and q share no common factors in lowest terms).\n• **Etymology:** From the Italian / Latin word ***Quoziente*** (\"Quotient\"), introduced by Giuseppe Peano.\n• **Decimal Characterization:**\n  A real number is in ℚ **if and only if** its decimal representation either:\n  1. **Terminates** (e.g., `3/4 = 0.75`)\n  2. **Repeats indefinitely in a repeating cycle** (e.g., `1/3 = 0.333...` or `1/7 = 0.142857142857...`).",
            "citation": "Real Analysis (Rudin)",
            "tags": ["numbers", "rationals", "fractions"]
        },
        {
            "id": "num-c4",
            "front": "What are **Irrational Numbers**, what is their formal notation, and what are 4 classic examples?",
            "hint": "Defined by what they are NOT. Expressed as the set difference of Reals and Rationals.",
            "back": "**Irrational Numbers (ℝ ∖ ℚ or ℙ / 𝕀)**\n\n• **Definition:** Numbers that **cannot** be written as a ratio of two integers (`p/q`).\n• **Notation:** Most rigorously written as the set difference **`ℝ ∖ ℚ`** (\"Reals minus Rationals\").\n• **Decimal Characterization:** Infinite, **non-repeating**, and **non-terminating** decimals.\n• **Classic Examples:**\n  1. `√2` (Hippasus's classic geometric diagonal of a unit square)\n  2. `π ≈ 3.14159...` (ratio of circle circumference to diameter)\n  3. `e ≈ 2.71828...` (Euler's base of natural logarithms)\n  4. `φ = (1 + √5)/2 ≈ 1.618...` (The Golden Ratio).",
            "citation": "Principles of Mathematical Analysis",
            "tags": ["numbers", "irrationals", "set-difference"]
        },
        {
            "id": "num-c5",
            "front": "What does **ℝ** represent, and how does it relate to the geometrical concept of the number line?",
            "hint": "The continuum. Closes all the 'holes' left by the rationals.",
            "back": "**ℝ = Real Numbers (The Continuum)**\n\n• **Definition:** The union of all rational and irrational numbers (`ℝ = ℚ ∪ (ℝ ∖ ℚ)`).\n• **Geometric Meaning:** Corresponds in a continuous, 1-to-1 bijection with every point along the unbroken geometric **number line**.\n• **The Completeness Axiom:** Unlike ℚ (which has infinite microscopic \"holes\" at every irrational point like √2), ℝ has the property of **completeness**—every bounded non-empty subset of ℝ has a least upper bound (supremum).\n• **Modifiers:**\n  - `ℝ⁺`: strictly positive real numbers `(0, ∞)`\n  - `ℝ⁻`: strictly negative real numbers `(-∞, 0)`\n  - `ℝ*` or `ℝ ∖ {0}`: all non-zero reals.",
            "citation": "Real Analysis & Topology",
            "tags": ["numbers", "reals", "continuum"]
        },
        {
            "id": "num-c6",
            "front": "What does **ℂ** represent, what is the imaginary unit **i**, and what are the two components of any **z ∈ ℂ**?",
            "hint": "Extends the real line into a 2D plane to allow square roots of negative numbers.",
            "back": "**ℂ = Complex Numbers (The Argand Plane)**\n\n• **Formal Definition:** `ℂ = { a + bi | a, b ∈ ℝ, i² = -1 }`.\n• **Imaginary Unit (i):** Defined such that `i = √(-1)`, meaning `i² = -1`.\n• **Two Components of z = a + bi:**\n  - **Real Part:** `Re(z) = a`\n  - **Imaginary Part:** `Im(z) = b` (Note: b is itself a real number!)\n• **Subsets:**\n  - If `b = 0`: z is purely a **Real Number** (`ℝ ⊂ ℂ`).\n  - If `a = 0` and `b ≠ 0`: z is a **Pure Imaginary Number** (`iℝ`).\n• **Fundamental Theorem of Algebra:** Every non-zero polynomial with complex coefficients has at least one root in ℂ.",
            "citation": "Complex Analysis (Ahlfors)",
            "tags": ["numbers", "complex", "imaginary"]
        },
        {
            "id": "num-c7",
            "front": "What is an **Algebraic Number (𝔸 or Q̄)**, and why is **√2** algebraic while **π** is not?",
            "hint": "Roots of polynomials with integer/rational coefficients.",
            "back": "**Algebraic Numbers (𝔸 or Q̄)**\n\n• **Definition:** Any real or complex number that is a root of a non-zero single-variable polynomial with integer (or rational) coefficients:\n  `aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀ = 0` (where each aᵢ ∈ ℤ).\n\n• **Why √2 is Algebraic:** It solves `x² - 2 = 0` (coefficients are 1 and -2, which are integers).\n• **Why i is Algebraic:** It solves `x² + 1 = 0`.\n• **Why all Rationals (ℚ) are Algebraic:** Any fraction `p/q` solves `qx - p = 0`.\n• **Why π is NOT Algebraic:** There is no finite polynomial with integer coefficients that has π as a root!",
            "citation": "Field Theory & Galois Theory",
            "tags": ["numbers", "algebraic", "polynomials"]
        },
        {
            "id": "num-c8",
            "front": "What is a **Transcendental Number (𝕋)**, and what are the two most famous examples?",
            "hint": "They 'transcend' the power of algebraic polynomial equations.",
            "back": "**Transcendental Numbers (𝕋 or ℝ ∖ 𝔸)**\n\n• **Definition:** Any real or complex number that is **NOT algebraic**—meaning it cannot be formed as the root of any polynomial equation with rational coefficients.\n• **Famous Examples:**\n  1. **π ≈ 3.14159...** (Proved transcendental by Ferdinand von Lindemann in 1882, finally proving the ancient impossibility of \"squaring the circle\").\n  2. **e ≈ 2.71828...** (Proved transcendental by Charles Hermite in 1873).\n  3. `2^√2` (Gelfond-Schneider theorem).\n• **Surprising Fact:** Even though they are harder to define individually, **almost all real numbers are transcendental**! (𝔸 is countable, but ℝ is uncountable).",
            "citation": "Transcendental Number Theory",
            "tags": ["numbers", "transcendental", "cardinality"]
        },
        {
            "id": "num-c9",
            "front": "What does **ℙ** represent, why is the number **1** NOT considered prime, and what is the Fundamental Theorem of Arithmetic?",
            "hint": "The atomic building blocks of multiplication. One is excluded to preserve unique factorization.",
            "back": "**ℙ = Prime Numbers**\n\n• **Definition:** An integer `p > 1` whose only positive divisors are 1 and itself (`ℙ = {2, 3, 5, 7, 11, 13, 17, 19, 23, ...}`).\n• **Why 1 is NOT Prime:**\n  If 1 were prime, prime factorization would not be unique (e.g., `6 = 2 · 3 = 1 · 2 · 3 = 1 · 1 · 2 · 3...`).\n• **Fundamental Theorem of Arithmetic:** Every integer greater than 1 can be represented uniquely as a product of prime numbers (up to the order of factors).\n• **Composite Numbers:** Integers greater than 1 that are not prime (`{4, 6, 8, 9, 10, ...}`).",
            "citation": "Number Theory (Euclid's Elements)",
            "tags": ["numbers", "primes", "factorization"]
        },
        {
            "id": "num-c10",
            "front": "What are **ℍ (The Quaternions)**, who invented them, and what algebraic property do they lose compared to **ℂ**?",
            "hint": "A 4-dimensional hypercomplex number system carved on Brougham Bridge by Hamilton.",
            "back": "**ℍ = Quaternions (Hamiltonians)**\n\n• **Definition:** 4-dimensional hypercomplex numbers of the form:\n  `q = a + bi + cj + dk` (where a, b, c, d ∈ ℝ).\n• **Governing Equation:** `i² = j² = k² = ijk = -1` (invented by Sir William Rowan Hamilton in 1843).\n• **What Property They Lose:** **Commutativity of Multiplication!**\n  In quaternions, `i · j = k`, but `j · i = -k` (order matters: `q₁ · q₂ ≠ q₂ · q₁`).\n• **Modern Usage:** Essential in 3D computer graphics, robotics, and aerospace navigation to calculate 3D rotations without \"gimbal lock\".",
            "citation": "Abstract Algebra & Vector Geometry",
            "tags": ["numbers", "quaternions", "hypercomplex"]
        },
        {
            "id": "num-c11",
            "front": "What does **ℤ/nℤ** (or **ℤₙ**) denote, and when does it become a Field?",
            "hint": "Clock arithmetic. Remainders when divided by n.",
            "back": "**ℤ/nℤ (Integers Modulo n)**\n\n• **Definition:** The set of equivalence classes of integers under division by n:\n  `ℤ/nℤ = {0, 1, 2, ..., n - 1}`.\n• **Arithmetic:** Operations are performed normally, then reduced modulo n (e.g., on a 12-hour clock, `9 + 5 ≡ 2 (mod 12)`).\n• **When is it a Field?**\n  - If `n` is composite (like 6), ℤ/6ℤ has zero divisors (`2 · 3 ≡ 0`) and is only a Ring.\n  - If `n` is a **Prime number p**, then **ℤ/pℤ (often written as 𝔽ₚ)** is a **finite field** (every non-zero element has a multiplicative inverse).",
            "citation": "Modern Algebra (Rings and Fields)",
            "tags": ["numbers", "modular-arithmetic", "finite-fields"]
        },
        {
            "id": "num-c12",
            "front": "What is the complete **Nested Inclusion Hierarchy** of standard numbers from smallest to largest?",
            "hint": "Chain of subsets: Primes inside Naturals inside Integers...",
            "back": "**The Universal Number Inclusion Chain:**\n\n```\nℙ ⊂ ℕ ⊂ ℤ ⊂ ℚ ⊂ 𝔸 ⊂ ℝ ⊂ ℂ ⊂ ℍ\n```\n\n• **ℙ (Primes):** `{2, 3, 5, ...}`\n• **ℕ (Naturals):** `{1, 2, 3, ...}`\n• **ℤ (Integers):** adds negative whole numbers and 0\n• **ℚ (Rationals):** adds all fractions `p/q`\n• **𝔸 (Algebraic):** adds radical roots like `√2, ∛5`\n• **ℝ (Reals):** adds transcendental continuous numbers like `π, e`\n• **ℂ (Complex):** adds imaginary dimensions `i = √(-1)`\n• **ℍ (Quaternions):** adds 4D non-commutative dimensions `j, k`.",
            "citation": "Mathematical Structures Summary",
            "tags": ["numbers", "hierarchy", "mastery"]
        }
    ],
    "quizzes": [
        {
            "id": "num-q1",
            "station": "Station 1: Number System Classification",
            "question": "To which of the following number systems does the number -7/3 belong?",
            "options": [
                "ℤ, ℚ, and ℝ",
                "ℚ, ℝ, and ℂ",
                "ℕ, ℤ, and ℚ",
                "ℝ ∖ ℚ (Irrationals)",
                "ℤ and ℂ only"
            ],
            "correctIndex": 1,
            "socraticHint": "-7/3 is a fraction of two integers. Trace where it sits in the inclusion chain.",
            "explanation": "-7/3 is a ratio of integers (-7 and 3), so it is in ℚ. Because ℚ ⊂ ℝ ⊂ ℂ, it is also in ℝ and ℂ. It is NOT an integer (so not in ℤ or ℕ)."
        },
        {
            "id": "num-q2",
            "station": "Station 2: Algebraic vs. Transcendental",
            "question": "The golden ratio φ = (1 + √5)/2 is an irrational number. Is it Algebraic or Transcendental, and why?",
            "options": [
                "Transcendental, because its decimal expansion never terminates or repeats.",
                "Algebraic, because it satisfies the polynomial equation x² - x - 1 = 0.",
                "Transcendental, because it contains the irrational square root √5.",
                "Algebraic, because all real numbers are algebraic.",
                "Neither, because it belongs to the complex numbers."
            ],
            "correctIndex": 1,
            "socraticHint": "Can you construct a polynomial equation with integer coefficients that has φ as its solution?",
            "explanation": "If x = (1 + √5)/2, then 2x - 1 = √5. Squaring both sides yields (2x - 1)² = 5, which simplifies to 4x² - 4x - 4 = 0, or x² - x - 1 = 0. Because it is a root of an integer-coefficient polynomial, φ is Algebraic (𝔸), not Transcendental."
        },
        {
            "id": "num-q3",
            "station": "Station 3: Decimal Expansion Properties",
            "question": "A student claims that 0.121212... (repeating '12' indefinitely) is an irrational number because it has infinite decimals. Is this claim correct?",
            "options": [
                "Yes, because any number with infinitely many decimal places cannot be written as a fraction.",
                "No, because any repeating decimal is a rational number (in this case, 12/99 = 4/33).",
                "Yes, because only terminating decimals belong to ℚ.",
                "No, because 0.121212... is a natural number.",
                "It depends on the base of the number system."
            ],
            "correctIndex": 1,
            "socraticHint": "Recall the decimal test for ℚ: terminating OR repeating.",
            "explanation": "A real number is rational (ℚ) if and only if its decimal terminates or repeats. Let x = 0.1212... Then 100x = 12.1212... Subtracting gives 99x = 12, so x = 12/99 = 4/33 ∈ ℚ."
        },
        {
            "id": "num-q4",
            "station": "Station 4: Non-Commutative Number Fields",
            "question": "In which of the following number systems is multiplication NOT commutative (meaning a · b ≠ b · a in general)?",
            "options": [
                "ℂ (Complex Numbers)",
                "ℝ (Real Numbers)",
                "ℤ/5ℤ (Integers modulo 5)",
                "ℍ (Quaternions)",
                "ℚ (Rational Numbers)"
            ],
            "correctIndex": 3,
            "socraticHint": "Think about Hamilton's 4D hypercomplex numbers with units i, j, k.",
            "explanation": "In the Quaternions ℍ, multiplication is non-commutative: i · j = k, but j · i = -k. In ℚ, ℝ, ℂ, and ℤ/nℤ, multiplication is commutative."
        },
        {
            "id": "num-q5",
            "station": "Station 5: The Cardinality of Transcendentals",
            "question": "Which of the following statements about the set of Algebraic numbers (𝔸) and Transcendental numbers (𝕋) is TRUE?",
            "options": [
                "There are more algebraic numbers than transcendental numbers.",
                "The algebraic numbers 𝔸 are countable, but the real transcendental numbers are uncountable.",
                "Both 𝔸 and 𝕋 are finite sets.",
                "All complex numbers are transcendental.",
                "π and e are the only transcendental numbers known to exist."
            ],
            "correctIndex": 1,
            "socraticHint": "Georg Cantor proved that polynomial roots can be counted, but the real continuum cannot.",
            "explanation": "Cantor proved that the set of all polynomials with integer coefficients is countable, making the algebraic numbers 𝔸 countable. However, the real numbers ℝ are uncountable. Therefore, the transcendental numbers ℝ ∖ 𝔸 must be uncountable—meaning almost all real numbers are transcendental!"
        }
    ]
}

def update_decks():
    deck_file = "G:/My Drive/Academics/study_portal/decks.json"
    with open(deck_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing = [d for d in data.get("decks", []) if d.get("id") != "math-number-systems"]
    botany_decks = [d for d in existing if "bot" in d.get("id", "")]
    other_decks = [d for d in existing if "bot" not in d.get("id", "")]

    data["decks"] = botany_decks + [numbers_deck] + other_decks

    with open(deck_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Updated decks.json successfully with math-number-systems!")

if __name__ == "__main__":
    update_decks()
