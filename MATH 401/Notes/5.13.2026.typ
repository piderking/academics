#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences & Series",
  assignment: "Daily Notes",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "May 13, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

#ps(title: "Taylor Series")[
  #notes[
    Can we associate a power series with a traditional function?
    \
    $sum_(n=0)^oo 1x^n $ is a geo-meteric series
    Converges if $r=x "  " |x| < 1$ to $a/(1-x)$\
    \
    Traditional Function:
    - $1/(1-x)$
    Power Series Function:
    - $sum_(n=0)^oo 1x^n $
    \
    Start with normal function: $f(x)$ and find a power series version of this function\
    $f(x) = sum_(n=0)^oo  a_n * (x-c)^n $\
    \
    - $a_0 = f(c)/1$
    \
    - $a_1 = f'(c)/1$
    \
    - $a_2 = f''(c)/(2*1)$
    \
    - $a_3 = f'''(c)/(3*2*1)$
    \
    - $a_n = (f^(n)(c))/(n!)$
    \
    Taylor Series center at $c$ for $f(x)$
    - $sum_(n=0)^oo (f^((n))(c))/(n!) * (x-c)^n $
    \
    
     Taylor Series Process:
    - traditional function into a taylor series
  
    \
    center point is center of interval of convergence!
    - usually 0, but have todo what works with functions
    \
    all the work is finding a formula for $f^((n))(c)$
    \
    Only works for interval of convergence for series equivilant. Can't swap it out there
    \
    \
    if
    $f^((0))(c) = 0 $ for example $f(x) = ln(x)$ 
    - if $f(1) = 0$ then the series starts at 1 not 0
    - example: $sum_(n=1)^oo $ not $sum_(n=0)^oo $
  ]
  #problem(title: "Taylor Series Introductory Problem")[
  #prob[
        Find the Taylor Series of $f(x) = e^x$ centered at $c=0$

  ]
  
  #steps[
    1. Layout Template
      - $sum_(n=0)^oo (f^((n))(c))/(n!) (x-c)^n $
      \
    2. Plug in $c = 0$ for all $c$
      - $sum_(n=0)^oo (f^((0))(c))/(n!) (x)^n $
      \
    3. Find the Formula for $f^((n))(c)$
      - List out 3+ derivatives
        - $f'(x) = e^x$
        - $f^((2))(x) = e^x$
        - $f^((3))(x) = e^x$
        - $f^((4))(x) = e^x$
      - Plug in $c$ for derivatives
        - $f'(c) = e^0 = 1$
        - $f^((2))(c) = e^0 = 1$
        - $f^((3))(c) = e^0 = 1$
        - $f^((4))(c) = e^0  = 1$
        - $f^((n))(c) = 1$
     4. Create Taylor Series now that we know formula
      - $sum_(n=0)^oo (f^((n))(c))/(n!) (x)^n $

      - $sum_(n=0)^oo (1)/(n!) (x)^n $
     5. Check the Interval of convergence (IC)
      - Can only beswapped out with the function when the series CONVERGES
      - Do RATIO test
      - $lim_(n->oo)  | a_(n+1) / a_n | = lim_(n->oo) | x/n! |$
    ]
    #solution[
      $sum_(n=0)^oo (1)/(n!) (x)^n $ for $(-oo, oo)$
    ]
   
  ]

  #problem[
    #prob[
      Find the Taylor Series of $f(x) = e^(4x)$ centered at $c=0$

    ]
    #steps[
      1. Layout Template
        - $sum_(n=0)^oo (f^((n))(c))/(n!) (x-c)^n $

        - $sum_(n=0)^oo (f^((n))(0))/(n!) (x)^n $


      2. Find Pattern of for Numerator
        - $n = 0 "   " f(x) = e^(4x)$
        - $f'(x) = 4e^(4x)$
        - $f^((2))(x) = 4 *4 e^(4x)$
        - $f^((3))(x) = 4*4*4 e^(4x)$
      3. Plug in $c = 0$ for all $c$
        - $n = 0 "   " f(c) = e^(c)$
        - $f'(0) = 4$
        - $f^((2))(0) = 4 *4 $
        - $f^((3))(0) = 4*4*4 $
        - $f^((n))(0) = 4^n$

    ]
    #solution[
      $e^(4x) = sum_(n=0)^oo (4^n)/(n!) (x)^n $
      \
      --> In Calc 2, you don't have todo ratio test for these functions

    ]
  ]

  #ps(title: "Trig Taylor Series")[

  ]
]