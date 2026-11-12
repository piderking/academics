#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences",
  assignment: "Daily Notes",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "April 22, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

#notes[
  Following tests are in order of use.
  1. Nth Term Test
  2. Partial Sums 
  3. P-Series
  4. DCT / LCT
  5. Ratio Test
  5. Integral Test
  
  Following tests are ONLY for specific conditions:
  1. Alternating Series Test (AST)
    - $(-1)^n (a_n)$
  2. Geometeric Series
    - $sum_(n=0)^oo a(r^n)$\
  

  Tips:
  - If rule looks like a complex fractions $1/(n(n+2))$ use Partial Fractions to break it up. Going to be Partial Sums from the solution after you break it apart.


]
#ps(title: "Nth Term Test")[
  Look at a Series, and have no clue? Try Nth test
  #formula[
    $sum_(n=1)^oo f(n)$\
    \
    If $lim_(n->oo) f(n) := cases(
  "diverges if" f(n) != 0,
  
  "inconclusive if" f(n) = 0 
)$
  ]
  #notes[
    If the series is inconclusive, you must use a different test
  ]
]
#ps(title: "Partial Sums")[
  #formula[
    
    $sum_(n=1)^oo 1/(2n) - 1/(2(n+2)) $\
    \
    $S_n = 1/(2n) - 1/(2(n+2))$\
      \
      $S_1 = 1/2 - 1/6$\
      \
      $S_2 = (1/2 - 1/6) + (1/4 - 1/8) $\
      \
      $S_3 = (1/2 - 1/6) + (1/4 - 1/8) + (1/6 - 1/10)$\
      \
      $S_4 = (1/2 - 1/6) + (1/4 - 1/8) + (1/6 - 1/10) + (1/8 - 1/12)$\
      \
      Create a rule, which ones are always there and which one would be there at the end (which doen't cancel out). For this problems, it is $1/10$ and $1/12$ and use the value of $n$ and create a rule in terms of $k$ \
      \
      $S_k = 1/2 + 1/4 - 1/(2(k+4)) - 1/(2(k+5)) $\
      \
      $lim_(k->oo) S_k = 1/2 + 1/4 - 0 - 0 $
      \ \
  ]

]
#ps(title: "Geometeric Series")[
  #formula[
      $sum_(n=0)^oo a(r^n) := cases(
    "diverges if" |r| >= 1,
    
    "converges if" |r| < 1,
    
  )$ \
  \
  If convergent, it converges at $a/(1-r)$
  ]
  #notes[
    Power must start with $r^0$ if not, you must adjust the funciton.\
    \
    $sum_(n=1)^oo a(r^n) "is not a geometeric series"$\
    \ 
    Exponent Rules:
    
    $sum_(n=1)^oo a(r^n)*(r^(-1))*(r^1)$\
    \
    $sum_(n=1)^oo a(r)(r^(n-1))$
    
    

  ]
]

#ps(title: "Alternating Series (AST)")[
  #formula[
    $sum_(n=1)^oo ((-1)^n)(a_n) or ((-1)^(n-1))(a_n) $\
    \
    Conditions that must be met:
    1.  $lim_(n->oo) a_n = 0 $
      - If fails, series Diverges
    2. $a_n$ needs to eventually decrease and stay decreasing forever
      - Example: First few terms of derivative could be positive, after it turns negative, the derivative has to STAY stay negative or else the test is inconclusive. 
        - Reasoning: 
          - If $a'_n > 0 "until" n=3$, you can rewrite the summation
          - $a_1 + a_2 + a_3 + sum_(n=4)^oo a_n $ and infinite series will converge, thus you can add the previous
      - If fails, test is Inconclusive
  
    
    If both are true, it converges
  ]
  #notes[
    Almost always it's the first test fails.
  ]

]

#ps(title: "P-Series")[
  #formula[\
    $sum_(n)^oo 1/n^p := cases(
    "diverges if" p <= 1,
    "converges if" p > 1,
    
  )$]
]

#ps(title: "DCT / LCT")[
  \
  #formula(title: "DCT")[
    Evaluate as if limit to infinity\
    $sum_n^oo (n^(a) + ...)/(n^b + ...) underline(~) 1/n^(p)$\
    \
    P-Series Test for the new value:\
    \
    $1/n^p := cases(
    "diverges if" p <= 1,
    "converges if" p > 1,)$\
    \ 
    Create an equation:\
    If new diverges: $"original" > "new"$\
    - if the original is larger than the new, which diverges to infinity, the larger must also diverge
    If new converges $"original" < "new"$
    - if the original is smaller
    \
    If the statement is True, the original has the same end behavior as the new

    Can move the denominators to help understand equation\
     Example:\
    $(n^3 + n^2)/(n^4 - n^2 + n ) >= 1/n "   " = "   "(n^3 + n^2)n >= (n^4 - n^2 + n ) "  " = "   " n^4 + n^3 >= n^4 - n^2 + n$
    - Thus the original also diverges.

    If the inequality is complicated or comes out incorrect, swap to the LCT
  ]
   #formula(title: "LCT")[
    Take limit of the equation\
  
    $ lim_(n->oo) "original"/"new"$, if the limit is NOT $0$ or $oo$, they both do the samething (converge or diverge)
    \
    Example:
    \
    $"original"= (n^3 + n^2)/(n^4 - n^2 + n ))$\
    $"new " = 1/n$\
    New Diverges
    \
    
    $lim_(n->oo)((n^3 + n^2)/(n^4 - n^2 + n ))/(1/n) = (n^4+n^3)/(n^4-n^2+n) = 1$
  ]
  

  $$
]

#ps(title: "Integral Test")[]

#ps(title: "Factorials")[
  #notes[
    How to show factorial is decreasing
    - $a_n = {1/n!} "    " a_(n+1) <= a_n$
    - $a_(n+1) <= 1/n! "  " n!/(n+1)! <= 1$
  ]
]

#ps(title:"Absolute Convergence v. Conditional Convergence")[
  #formula[
    When equation flips from positive to negative, Alternatig Series, usually $sum_(n=1)^oo (-1)^n$ a_n\
    Absolute Convergence (AC):
    - if you take away the alternator, it still converges
    - todo that take away absolute value around series
    Conditional Convergence (CC):
    - weak
    - when theres a negative 
    - if you take away the alternator, it diverges
  ]
]