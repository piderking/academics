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

// 3. Start using the template!
// By giving the problem set a title, it will show up as the top level in the TOC!
#ps(title: "Warm Up", numbering-style: "1.")[

  // We can add a custom title and a description with links!
  #problem( )[
    #prob[
      Determine Convergence or Divergence & Which test
      
      $ sum_(n=0)^oo 2(-1/2)^(n+2)$
    ]

    #steps[
      Get in correct form.\
            $ sum_(n=0)^oo 2(-1/2)^(n+2)*(-1/2)^1$

            $ sum_(n=0)^oo 1/4 (-1/2)^(n+2)$
           
      Geo-Meteric Series \
      $|r| < 1$

      $(1/4)/(1-(-1/2))$\ \
      $(1/4)/(3/2)$\


    ]

    #solution[
      Converge to $1/3$
    ]

  ]

  #problem()[
   #prob()[ Determine Convergence or Divergence & Which test

    $ sum_(n=1)^oo (1/n^2 - 1/(n+4)) $
    
    ]
    #solution[
    Since they're telescope sum, we use 
  ]

  ]
  
]

#ps(title: "Integral Test")[
  #notes[
    $sum_n^oo f(x)$\
    Before using, must meet 3 questions.
      1. Is $f(x)$ continous on $[0, oo)$
      2. $f(x)>= 0$ on $[0, oo)$?
      3. Decreasing acrost $[0, oo)$?
        - Take derivative and check if < 0
    If all pass, then the integral test can be use?
    $lim_(t->oo) integral_n^(t)f(x)d x$ 
    Lower Bound is starting for summation
    - If Limit Converges, Series Converges
    - If Limit DIverges, Series Diverges
  ]
  #problem()[
    #prob[
      Does $sum_(n=1)^oo 1/(n^2+1)$ converge or diverge
    ]
    #steps[
      1. Try nth term test
      $lim_(n=oo) 1/(n^2+1) = 0$ ; therefore test is inconclusive
      2. Telescoping Sum? No
      3. Geometeric Series? No
      4. Integral test

      Pre-Requisites for the Integral test
      1. Is $f(x)$ continous on $[0, oo)$
        Yes, f(x) never undefinied
      2. $f(x)>= 0$ on $[0, oo)$?
        Yes, Always positive
      3. Decreasing acrost $[0, oo)$?
        Use derivative of $f(x)$ and check if is always negative\
        $d/(d x)(f(x)) = (-2x)/(x^2+1)^2$
        Yes, $f'(x)$ is always negative... therefore always Decreasing

      Integral Test\
      - $lim_(t->oo) integral_0^oo 1/(x^2+1) d x$ \
      - $lim_(t->oo) arctan(x) |_0^t$
      - $lim_(t->oo) arctan(t) - 0$
      - $ pi/2- 0$
    ]
    #solution[
      Limit Converges, thus Series Converges

    ]
  ]
  #problem()[
    #prob[
      Does $sum_(n=2)^oo 1/(x  (ln(x) )^2)$ converge or diverge
    ]
    #steps[
      Pre-Requisites for the Integral test
      1. Is $f(x)$ continous on $[2, oo)$
        Yes, only 0 is at x=0, not in interval
      2. $f(x)>= 0$ on $[0, oo)$?
        Yes, Always positive
      3. Decreasing acrost $[0, oo)$?
        Use derivative of $f(x)$ and check if is always negative\
        $f'(x) < 0 $
        

      Integral Test\
      - $lim_(t->oo) integral_2^oo 1/(x (ln(x))^2) d x$ \
      - $u = ln(x)$  $d u = 1/x$ \
      - $lim_(t->oo) integral_2^oo 1/u^2 d u $
      - $lim_(t->oo) - u^(-1) |_2^t$
      - $lim_(t->oo)  - 1/(ln(x)) |_2^t$
      - $lim_(t->oo) -1( ln(t) - ln(2)) $
    ]
    #solution[
      Integral Test converges to $ln(2)$\
      Limit Converges, thus Series Converges

    ]
  ]
  #notes[
    Integral Test is super strong however, it's long and tedious
  ]
  
]

#ps(title: "P-Series Test",)[
  #notes[
    How to avoid the integral.

  ]
  #problem()[
    When does $sum_(n=1)^oo 1 / n^p $ converge?

  ]
  #notes[
    nth Term Test\
    $sum_(n=1)^oo 1 / n^p $ \ \
    $lim(n->oo) 1 / n^p $ 
    - If $p<0$ $lim = oo $ would diverge
    - If $p=0$ $lim =1$ would diverge 
    - If $p>0$ $lim= 0$ inconclusive

    For $p>0$ do intgral test
    $lim_(b->oo) (b^(-p+1)/(p+1) - ...)$ \ 

    Therefore
    - If $-p+1<0$ then it converges
    - If $-p+1>0$ then it converges
  ]

  #formula()[
    P-Series Test\
    For all P-Series ($sum_(n)^oo 1/n^p$)
    - If $p>1$ series converges
    - If $p<=1$ series diverges
  ]
]
