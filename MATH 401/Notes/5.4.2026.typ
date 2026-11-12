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

#ps(title: "AST Practice")[
  #problem[
    #prob[
      Determine if it Converges or Diverges?
      If it converges, is it AC or CC?\
      $sum_(n=1)^oo (-1)^n n^3/(n^5 + 2)$
    ]
    #steps[
      AST:
      1. $lim_(n->oo) a_n = 0 "   " lim_(n->oo) n^3/(n^5+2)$
      - passed
      2. $d/(d x)(n^3/(n^5 + 2)) = -$ (can start positive, but then must go negative and stay negative)
        - $ f'(x) = (3n^2(n^5 + 2) -  4n^7 )/(n^5 + 2)^2$
        - Once it goes negative it will stay negative ( because of large power $4n^7$)
      - passed\

      Thus, the series converges by the AST. Now check if it is AC or CC.\
      $sum_(n=1)^oo |((-1)^n n^3)/(n^5 + 2)| "-> " 1/n^2$\
      \
      $(n^3)/(n^5 + 2) <= 1/n^2$\
      This converges, because of DCT and thus says this series is AC



    ]
    #solution[
      AC
    ]
  ]
]

#ps(title: "Ratio Test")[
  #formula[
      $sum_(n)^oo a_n $ (entire series)\
      \
      Work well with exponentials $e^n$ and/or always with factorials $n!$

      $lim_(n->oo) |a_(n+1)/(a_(n))| := cases(
        < 1 : "series absolute converges",
        = 1 : "inconclusive",
        > 1 : "series diverges",

      ) $

  ]
  #problem[
    #prob[
      $sum_(n)^oo e^n/n! $
    ]
    #steps[
      Ratio Test:
      - Will always always simplify

      $lim_(n->oo) (e^(n+1)/(n+1!))/(e^n/n!) $\
      \
      $lim_(n->oo) (e^(n+1)/(n+1)!)  * n!/e^n$\
      \
      Be careful when simplifying factorials...
    
     \
      $lim_(n->oo) e/(n+1) = 0$

    ]
    #solution[
      Limit evaluates to less than one, series is Absolute Convergence
    ]
  ]
]