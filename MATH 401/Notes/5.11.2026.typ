#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences & Series",
  assignment: "Daily Notes",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "April 22, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

#ps(title:"Power Series")[
  #notes[
    Free variable series

    Example:
    - usually start at 0, don't have to
    $sum_(n=0)^oo a_n (x-c)^n $
    \
    $c$ is the "center point",

    when you plug a value in for x, you get a series we've work with before

    Domain: (Interval of Convergence)\
    All values that can be pluged in for $x$ and the series converges

    - to find Interval of Convergence, always ratio test

    $lim_(n->oo) |a_(n+1)/(a_n)| $ \
    will give you "preliminary" IC, need to check for the end points.

    $sum_(n=0)^oo a_n ("first endpoint"-c)^n $
    $sum_(n=0)^oo a_n ("last endpoint"-c)^n $


    \
    
  ]
  #problem(title: "Example of Power Series")[
    #prob[
      $sum_(n=0)^oo 1x^n $
    ]
    #steps[
      $sum_(n=0)^oo 1x^n $\
      \
      $lim_(n->oo) |(1x^(n+1))/(1x^n)| $ \
      \
      $lim_(n->oo)|x| = |x| $\
      For IC must converge, $|x| < 1$ therefore the preliminary interval of convergence $(-1, 1)$
      now we have to check the endpoints

      $sum_(n=0)^oo 1*1^n $ Diverges\
      \
      $sum_(n=0)^oo 1*(-1)^n $ Diverges \



    ]
    #solution[
      $(-1, 1)$
    ]


  ]
  #problem[
    #prob[
      Find IC for $sum_(n=0)^oo 1/(n+2)^2 (x^n)$
    ]
    #steps[
      Ratio Test:\
      $lim_(n->oo) | (x^(n+1)/(n+3)^2)/(x^n/(n+2)^2) |$\
      \
      $lim_(n->oo) | ((x^(n+1) (n+2)^2) /((n+3)^2 x^n) ) |$
      \
      \
      $lim_(n->oo) | ((x(n+2)^2) /((n+3)^2) ) |$
      \
      \
    ]
    #solution[
            $(-1, 1)$

    ]
  ]

  #problem[
    #prob[
      Find IC:
      $sum_(n=0)^oo ((-1)^n 2^n)/n! (x-2)^n  $

    ]
    #steps[
      Ratio Test:
      - $a_(n+1) = ((-2)^(n+1))/(n+1)! (x-2)^(n+1) $
      \
      - $lim_(n->oo) | ( ((-2)^(n+1))/(n+1)! (x-2)^(n+1) )/(((-1)^n 2^n)/n! (x-2)^n) | $
      \
      - $lim_(n->oo) |(-2  (x-2))/( (n+1)) | = 0 $
    ]
  #solution[
    IC: $(-oo, oo)$
  ]
  ]
  #notes[
    Why is this important?
    - Power Series are like infinite polynomials
      - $sum_(n=0)^oo x^n  = 1 + x + x^2 + x^3 + x^4$
  ]

  #notes[
    Integrals with Power Series
    $integral sum_(n=0)^oo  P(x) d x$
    - don't touch addition
    - don't touch coefficents
    ONLY HAVE TODO STUFF WITH VARIABLE!
    \
    DONT TOUCH COEFFICENT (EVERYTHING WITHOUT X)!
    \
    Example:\
    $integral sum_(n=0)^oo ((-1)^n n^2 (x+1)^n )/3^n d x= sum_(n=0)^oo ((-1)^n n^2)/3^n * (x+1)^(n+1)/(n+1) + C  $
  ]

   #notes[
    Derivatives with Power Series
    $d / (d x) sum P(x) $
    - don't touch addition
    - don't touch coefficents
    ONLY HAVE TODO STUFF WITH VARIABLE!
    \
    DONT TOUCH COEFFICENT (EVERYTHING WITHOUT X)!
    \
    Example:\
    Deriavtive of constant = 0\
    $d / (d x) sum_(n=0)^oo  1/(n+1)^2  x^n = sum_(n=0)^oo n/(x+1)^2 x^(n-1) $
  ]
  
]