import json

math_deck = {
    "id": "math-symbols-logic",
    "course": "MATH 401",
    "title": "Mathematical Logic, Set Theory & Advanced Notation",
    "description": "Mastery deck for advanced mathematical symbols: quantifiers (∀, ∃, ∃!), set membership & operations (∈, ∉, ⊆, ⊂, ∖, ∪, ∩), logical connectives (⟹, ⟺), standard number systems (ℕ, ℤ, ℚ, ℝ, ℂ), and calculus/analysis operators (∇, ∂, ∘, :=).",
    "source": "Advanced Mathematics, Set Theory & Real Analysis Foundations",
    "flashcards": [
        {
            "id": "sym-c1",
            "front": "What does the symbol **∈** mean, and how is the statement **x ∈ A** read?",
            "hint": "Derived from the Greek letter epsilon (ϵ) standing for 'element'.",
            "back": "**∈ means \"Element of\" (or \"in / belongs to\").**\n\n• **Reading:** \"x is an element of A\" or \"x belongs to set A\".\n• **Formal meaning:** Object x is a member of the collection of objects defined as set A.\n• **Example:** `3 ∈ ℤ` (\"3 is an element of the integers\").\n• **Counterpart:** **∉** means \"is not an element of\" (`3.5 ∉ ℤ`).",
            "citation": "Naive Set Theory (Halmos)",
            "tags": ["set-theory", "membership", "fundamentals"]
        },
        {
            "id": "sym-c2",
            "front": "What is the crucial difference between **x ∈ A** and **{x} ⊆ A**?",
            "hint": "Think about an individual object vs. a collection holding that object.",
            "back": "**Element vs. Subset Distinction:**\n\n• **x ∈ A:** x is an *individual element* contained directly inside set A.\n• **{x} ⊆ A:** {x} is a *set (a singleton)* whose elements are all contained in A.\n\n• **Example:** If `A = {1, 2, 3}`:\n  - `1 ∈ A` is **TRUE**\n  - `{1} ∈ A` is **FALSE** (A contains the number 1, not a set containing 1)\n  - `{1} ⊆ A` is **TRUE** (every element of {1} is in A).",
            "citation": "Foundations of Higher Mathematics",
            "tags": ["set-theory", "subsets", "logic-trap"]
        },
        {
            "id": "sym-c3",
            "front": "What do the symbols **⊆** and **⊂** denote, and how do they differ?",
            "hint": "Compare them to ≤ (less than or equal to) versus < (strictly less than).",
            "back": "**Subset vs. Proper (Strict) Subset:**\n\n• **A ⊆ B (Subset):** Every element of A is also in B. A *can* be equal to B (`A ⊆ A` is always true).\n• **A ⊂ B (or A ⊊ B, Proper Subset):** Every element of A is in B, AND there is at least one element in B not in A (`A ≠ B`).\n\n• **Analogy:** `⊆` is like `≤`, while `⊂` is like `<`.",
            "citation": "Set Theory Foundations",
            "tags": ["set-theory", "subsets"]
        },
        {
            "id": "sym-c4",
            "front": "What does the symbol **∀** represent, and how do you translate **∀x ∈ S, P(x)** into English?",
            "hint": "An inverted letter 'A' standing for 'ALL'.",
            "back": "**∀ is the Universal Quantifier (\"For all\" / \"For every\").**\n\n• **Translation:** \"For every x in set S, the property P(x) is true.\"\n• **Truth Condition:** The statement is TRUE only if P(x) holds for *every single* element in S. A single counterexample makes the entire statement FALSE.\n• **Negation Rule:** `¬(∀x, P(x)) ⟺ ∃x, ¬P(x)` (\"The negation of 'all are' is 'there exists at least one that is not'\").",
            "citation": "Predicate Logic",
            "tags": ["logic", "quantifiers"]
        },
        {
            "id": "sym-c5",
            "front": "What do **∃** and **∃!** represent in mathematical proofs?",
            "hint": "A backwards letter 'E' standing for 'EXISTS'. The exclamation mark adds uniqueness.",
            "back": "**Existential Quantifiers:**\n\n• **∃ (\"There exists\"):** At least one element satisfies the condition.\n  - Example: `∃x ∈ ℝ, x² = 2` (\"There exists a real number whose square is 2\").\n• **∃! (\"There exists a UNIQUE\"):** Exactly one element satisfies the condition (one and only one).\n  - Example: `∃!x ∈ ℝ, 2x + 4 = 0` (only `x = -2` works).\n\n• **Negation Rule:** `¬(∃x, P(x)) ⟺ ∀x, ¬P(x)`.",
            "citation": "Predicate Logic & Proof Writing",
            "tags": ["logic", "quantifiers", "uniqueness"]
        },
        {
            "id": "sym-c6",
            "front": "What does the logical connective **P ⟹ Q** mean, and when is it FALSE?",
            "hint": "Material implication. Think about a broken contract.",
            "back": "**P ⟹ Q means \"P implies Q\" (or \"If P, then Q\").**\n\n• **P** is the hypothesis (antecedent); **Q** is the conclusion (consequent).\n• **The ONLY way P ⟹ Q is FALSE:** When P is **TRUE** but Q is **FALSE**.\n\n• **Vacuous Truth:** If P is FALSE, `P ⟹ Q` is automatically **TRUE**, regardless of whether Q is true or false! (e.g., \"If 5 is even, then 2 + 2 = 7\" is logically true).",
            "citation": "Propositional Calculus",
            "tags": ["logic", "implication", "truth-tables"]
        },
        {
            "id": "sym-c7",
            "front": "What does **P ⟺ Q** mean, and what is its relationship to **P ⟹ Q**?",
            "hint": "A two-way double arrow. Often abbreviated as 'iff'.",
            "back": "**P ⟺ Q means \"P is equivalent to Q\" (\"P if and only if Q\", or \"iff\").**\n\n• **Formal Definition:** `(P ⟹ Q) ∧ (Q ⟹ P)`.\n• **Meaning:** P and Q always share the exact same truth value (both true or both false).\n• **In Proofs:** To prove `P ⟺ Q`, you must prove TWO directions: forward (`P ⟹ Q`) and backward (`Q ⟹ P`).",
            "citation": "Proof Techniques (Direct & Biconditional)",
            "tags": ["logic", "biconditional", "proofs"]
        },
        {
            "id": "sym-c8",
            "front": "Identify the standard Blackboard Bold number systems: **ℕ**, **ℤ**, **ℚ**, **ℝ**, **ℂ**.",
            "hint": "German 'Zahlen' = numbers; Latin 'Quotient' = ratio.",
            "back": "**The Standard Number Hierarchy:**\n\n• **ℕ (Natural Numbers):** `{1, 2, 3, ...}` (positive integers, sometimes including 0).\n• **ℤ (Integers):** `{..., -2, -1, 0, 1, 2, ...}` (from German *Zahlen*).\n• **ℚ (Rational Numbers):** Fractions `{p/q | p, q ∈ ℤ, q ≠ 0}` (from *Quotient*).\n• **ℝ (Real Numbers):** All points on the continuous number line (rationals + irrationals like π, √2).\n• **ℂ (Complex Numbers):** Numbers of the form `{a + bi | a, b ∈ ℝ, i² = -1}`.\n\n• **Hierarchy:** `ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ`.",
            "citation": "Number Theory & Analysis",
            "tags": ["number-systems", "notation"]
        },
        {
            "id": "sym-c9",
            "front": "What does the set difference symbol **∖** (or minus sign **-**) mean in **A ∖ B**?",
            "hint": "Read as 'without' or 'set-theoretic difference'.",
            "back": "**A ∖ B (read \"A minus B\" or \"A without B\") is the Set Difference:**\n\n• **Definition:** `{x | x ∈ A and x ∉ B}`.\n• **Meaning:** Take all elements in A and remove any that are also in B.\n• **Common Math Usages:**\n  - `ℝ ∖ {0}`: All real numbers *except zero* (domain of 1/x).\n  - `ℝ ∖ ℚ`: The set of all *irrational numbers*.",
            "citation": "Set Theory Operations",
            "tags": ["set-theory", "operations"]
        },
        {
            "id": "sym-c10",
            "front": "What is the meaning of the vertical bar **|** (or colon **:**) in set-builder notation `{x ∈ S | P(x)}`?",
            "hint": "Specifies the filter or condition for membership.",
            "back": "**| (or :) means \"Such that\" (French: 'tel que').**\n\n• **Full Expression:** `{x ∈ S | P(x)}`\n• **Reading:** \"The set of all x in S *such that* x satisfies condition P(x).\"\n• **Example:** `{x ∈ ℝ | x² - 4 = 0}` denotes the set `{-2, 2}`.\n• **Alternative:** A colon `{x ∈ S : P(x)}` means the exact same thing.",
            "citation": "Set-Builder Notation",
            "tags": ["set-theory", "notation"]
        },
        {
            "id": "sym-c11",
            "front": "What does **∅** represent, and why is the statement **∅ ⊆ A** true for EVERY set A?",
            "hint": "The Norwegian letter Ø introduced by André Weil. What elements are inside it?",
            "back": "**∅ (or {}) is the Empty Set (Null Set).**\n\n• **Definition:** The unique set that contains **no elements** at all (`|∅| = 0`).\n• **Why ∅ ⊆ A is always true:**\n  - By definition, `S ⊆ A` means: \"If `x ∈ S`, then `x ∈ A`\".\n  - Since `x ∈ ∅` is always FALSE (there are no elements in ∅), the implication is **vacuously true** for every possible set A!\n• **Common Trap:** `{∅} ≠ ∅`. `{∅}` is a non-empty set containing one element (the empty set).",
            "citation": "Axiomatic Set Theory (ZFC)",
            "tags": ["set-theory", "vacuous-truth"]
        },
        {
            "id": "sym-c12",
            "front": "What does the circle symbol **∘** denote in **(f ∘ g)(x)**, and what is its evaluation order?",
            "hint": "Function composition. Which function gets evaluated first?",
            "back": "**∘ denotes Function Composition (\"f composed with g\" or \"f circle g\").**\n\n• **Definition:** `(f ∘ g)(x) = f(g(x))`.\n• **Evaluation Order:** **Right-to-left!** First evaluate `g(x)` on input x, then pass the resulting output into `f`.\n• **Calculus Link:** The derivative of `(f ∘ g)(x)` requires the **Chain Rule**: `(f ∘ g)'(x) = f'(g(x)) · g'(x)`.",
            "citation": "Calculus & Abstract Algebra",
            "tags": ["functions", "calculus", "composition"]
        },
        {
            "id": "sym-c13",
            "front": "What does the symbol **:=** (or **≡**) mean in an equation like **f(x) := x³ - x**?",
            "hint": "Look at the colon preceding the equal sign. It is not asserting equality; it is declaring it.",
            "back": "**:= means \"Is Defined As\" (Definitional Equality).**\n\n• **Purpose:** It establishes an assigned definition rather than asserting a factual equation to be solved.\n• **Difference:**\n  - `2x + 1 = 5` is an equation to be solved for x.\n  - `L := lim_{x→a} f(x)` defines the symbol L as shorthand for the limit.\n• **Alternative (≡):** `≡` can mean \"identically equal to\" (`sin²(x) + cos²(x) ≡ 1` for all x) or modular congruence (`a ≡ b (mod n)`).",
            "citation": "Mathematical Conventions & Notation",
            "tags": ["notation", "definitions"]
        },
        {
            "id": "sym-c14",
            "front": "What does the symbol **∂** (del / curly d) denote in **∂f / ∂x**, and how does it differ from **df / dx**?",
            "hint": "Introduced by Legendre and Jacobi for multivariable rates of change.",
            "back": "**∂ denotes a Partial Derivative.**\n\n• **df / dx (Ordinary Derivative):** Used when f is a function of a *single* variable x.\n• **∂f / ∂x (Partial Derivative):** Used when f is a function of *multiple* variables (e.g., `f(x, y, z)`). It measures the rate of change of f with respect to x **while treating all other variables (y and z) as constants**.\n• **Example:** If `f(x, y) = x²y`, then `∂f/∂x = 2xy`, and `∂f/∂y = x²`.",
            "citation": "Multivariable Calculus (MATH 2263 / MATH 401)",
            "tags": ["calculus", "multivariable", "derivatives"]
        },
        {
            "id": "sym-c15",
            "front": "What does the inverted triangle **∇** (nabla / del) represent when applied to a multivariable scalar function **f**?",
            "hint": "Named after a Phoenician harp (nabla). Produces a vector of partials.",
            "back": "**∇f denotes the Gradient of f.**\n\n• **Formula:** `∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)`.\n• **Two Fundamental Properties:**\n  1. **Direction:** Points in the direction of **greatest rate of increase** of the function f at that point.\n  2. **Magnitude:** `‖∇f‖` equals the maximum directional derivative (the steepness of that increase).\n• **Orthogonality:** `∇f` is always **perpendicular (normal)** to the level curves/surfaces `f(x, y) = c`.",
            "citation": "Vector Calculus",
            "tags": ["calculus", "vector-calculus", "gradient"]
        },
        {
            "id": "sym-c16",
            "front": "How do you decipher Cauchy's famous rigorous limit definition: **∀ε > 0, ∃δ > 0, ∀x ∈ D (0 < |x - c| < δ ⟹ |f(x) - L| < ε)**?",
            "hint": "Break down each symbol: For every epsilon, there exists a delta, such that...",
            "back": "**The Epsilon-Delta Limit Definition (lim_{x→c} f(x) = L):**\n\n• **∀ε > 0:** \"For every positive tolerance ε (no matter how tiny),\"\n• **∃δ > 0:** \"there exists a corresponding positive distance δ,\"\n• **such that if:** `0 < |x - c| < δ` (x is within δ distance of c, but not equal to c),\n• **⟹ (then):** `|f(x) - L| < ε` (the function value f(x) is guaranteed to stay within ε of the limit L).\n\n• **Core Concept:** You name the error bound (ε), and I can always find an input radius (δ) tight enough to satisfy it.",
            "citation": "Real Analysis & Rigorous Calculus",
            "tags": ["analysis", "limits", "epsilon-delta"]
        }
    ],
    "quizzes": [
        {
            "id": "sym-q1",
            "station": "Station 1: Set Membership vs. Inclusion",
            "question": "Let set S = { 2, {2}, 4 }. Which of the following statements is mathematically FALSE?",
            "options": [
                "2 ∈ S",
                "{2} ∈ S",
                "{2} ⊆ S",
                "{{2}} ⊆ S",
                "{4} ∈ S"
            ],
            "correctIndex": 4,
            "socraticHint": "Carefully distinguish between an element being directly inside S versus a set constructed from elements in S.",
            "explanation": "{4} is a set containing the number 4. While 4 ∈ S is true, the set {4} is NOT an element of S, so {4} ∈ S is FALSE (it should be {4} ⊆ S). Meanwhile, 2 ∈ S is true, {2} ∈ S is true (it is explicitly listed), {2} ⊆ S is true (since 2 ∈ S), and {{2}} ⊆ S is true (since {2} ∈ S)."
        },
        {
            "id": "sym-q2",
            "station": "Station 2: Truth Values of Implication",
            "question": "Consider the mathematical statement: \"If 5 is an even number, then 2 + 2 = 7.\" What is the truth value of this statement in formal logic?",
            "options": [
                "FALSE, because 2 + 2 does not equal 7.",
                "FALSE, because both the premise and conclusion are false.",
                "TRUE, because an implication with a false premise is vacuously true.",
                "UNDEFINED, because 5 is not an even number.",
                "PARADOXICAL, because mathematical falsehoods cannot imply anything."
            ],
            "correctIndex": 2,
            "socraticHint": "Recall the truth table for P ⟹ Q. When is an implication false?",
            "explanation": "In propositional logic, P ⟹ Q is false ONLY when P is true and Q is false. When the hypothesis P is false, the implication is automatically TRUE (known as vacuous truth)."
        },
        {
            "id": "sym-q3",
            "station": "Station 3: Number System Operations",
            "question": "What set of numbers is described by the expression ℤ ∖ ℕ (where ℕ = {1, 2, 3, ...})?",
            "options": [
                "The set of all rational fractions {p/q}.",
                "{0, -1, -2, -3, -4, ...} (zero and all negative integers)",
                "The empty set ∅.",
                "{-1, -2, -3, -4, ...} (strictly negative integers only)",
                "The set of all irrational numbers."
            ],
            "correctIndex": 1,
            "socraticHint": "The backslash denotes set difference: take all integers and remove the positive natural numbers.",
            "explanation": "ℤ contains all positive integers, negative integers, and zero. Subtracting ℕ = {1, 2, 3, ...} leaves zero and all negative integers: {0, -1, -2, -3, ...}."
        },
        {
            "id": "sym-q4",
            "station": "Station 4: Quantifier Negation",
            "question": "What is the logical negation of the proposition: \"∀x ∈ ℝ, x² ≥ 0\"?",
            "options": [
                "∀x ∈ ℝ, x² < 0",
                "∃x ∈ ℝ, x² ≤ 0",
                "∃x ∈ ℝ, x² < 0",
                "∀x ∉ ℝ, x² < 0",
                "¬∃x ∈ ℝ, x² ≥ 0"
            ],
            "correctIndex": 2,
            "socraticHint": "Negating ∀ turns it into ∃, and the interior statement must be negated.",
            "explanation": "To disprove that \"all x have property P\", you only need to show that \"there exists at least one x that does NOT have property P\". The strict opposite of x² ≥ 0 is x² < 0, so the negation is ∃x ∈ ℝ, x² < 0."
        },
        {
            "id": "sym-q5",
            "station": "Station 5: Vector Calculus Gradient",
            "question": "For a scalar potential function f(x, y), what does the geometric vector ∇f(x₀, y₀) signify?",
            "options": [
                "The direction tangent to the level curve f(x, y) = c.",
                "The direction of steepest descent (rate of fastest decrease).",
                "A scalar quantity representing the curvature of the graph.",
                "The direction of greatest rate of increase, perpendicular to the level curve.",
                "The second derivative test matrix."
            ],
            "correctIndex": 3,
            "socraticHint": "Nabla creates the gradient vector (∂f/∂x, ∂f/∂y). Consider how it points relative to elevation contour lines.",
            "explanation": "The gradient ∇f points directly in the direction of greatest instantaneous rate of increase (steepest ascent) and is orthogonal (normal/perpendicular) to the level curve at that point."
        },
        {
            "id": "sym-q6",
            "station": "Station 6: Definitional Uniqueness",
            "question": "Which of the following statements accurately uses the uniqueness quantifier ∃! ?",
            "options": [
                "∃!x ∈ ℝ, x² = 9",
                "∃!x ∈ ℝ, x³ = 8",
                "∃!x ∈ ℝ, sin(x) = 0",
                "∃!x ∈ ℝ, |x| = 5",
                "∃!x ∈ ℝ, x² = -1"
            ],
            "correctIndex": 1,
            "socraticHint": "∃! requires that there is ONE AND ONLY ONE real solution.",
            "explanation": "For x³ = 8 in the real numbers, x = 2 is the single, unique real solution. For x² = 9, there are two solutions (3 and -3). For |x| = 5, there are two solutions (5 and -5). For sin(x) = 0, there are infinitely many solutions. For x² = -1, there are no real solutions."
        }
    ]
}

def update_decks():
    deck_file = "G:/My Drive/Academics/study_portal/decks.json"
    with open(deck_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing = [d for d in data.get("decks", []) if d.get("id") != "math-symbols-logic"]
    botany_decks = [d for d in existing if "bot" in d.get("id", "")]
    other_decks = [d for d in existing if "bot" not in d.get("id", "")]

    data["decks"] = botany_decks + [math_deck] + other_decks

    with open(deck_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("Updated decks.json successfully with math-symbols-logic!")

if __name__ == "__main__":
    update_decks()
