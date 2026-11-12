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

#ps(title: "Direct Comparision Test (DCT)", numbering-style: "1")[
  #notes[
    Idea: when a series looks a lot like the P-Series Test is a little off. \    
    Examples:
      - $sum_(n=1)^oo 1 / (n^p +1) $ 
      - $sum_(n=1)^oo 1 / (n^p +n) $
    Strip down to highest Powers
    -  when $n$ is very large, highest powers dominate

  ]
  #formula[
    For a series $sum_(n)^oo a_n $  if we can find another series $sum_(n)^oo b_n $ that converges and if $a_n <= b_n$, then $a_n$ converges

    For a series $sum_(n)^oo a_n $  if we can find another series $sum_(n)^oo b_n $ that diverges and if $a_n >= b_n$, then $a_n$ diverges
    
    If inequality is faulty, the DCT is inconclusive
    \
    Tips for $a_n <= b_n$
    - Cancel out a side on a fraction (times both sides by simpler denominator), repeat until no fractions
  ]
  #problem(title: "Example Problem")[
    #prob[
      $a_n =sum_(n=1)^oo (2n^2)/(3n^4+5)$
    ]
    #steps[
      1.    According to DCT looks, the given series looks a lot like   $b_n = sum_(n=1)^oo (2n^2)/(3n^4)$
      2.  Pull out constant, $2/3 sum_(n=1)^oo (n^2)/(n^4)$
      3. Simplify, $2/3 sum_(n=1)^oo 1/n^2$
      4. P-Series test, $p>1$, the series converges
      5. Original converges if $b_n <= a_n$
        - Multiply by opposite side (clear our Fractions) 
        - $(2n^2 )/(3n^4+5) <= 2/(3n^2)$
        - $(2n^2 )/(3n^4+5)*(3n^2) <= 2/(3n^2)*(3n^2)$
        - $(6n^4 )/(3n^4+5) <= 2$
        - $6n^4  <= 2(3n^4+5)$
        - $6n^4  <= 6n^4+10$ which is True
    ]
    #solution[
      Series Converges
    ]


  ]
  #problem(title: "Example 2")[
    #prob[
      Converge or Divergence
      $sum_(n=1)^oo (n^3 + 2n)/(n^6 +2n^5 + 5n^4 +n + 1)$
    ]
    #steps[
      1. DCT, treat like limits to $oo$ and subtract powers from top to bottom $=$ $sum_(n=1)^oo 1/n^3$ and $1/n^3$ converge.
      2. $(n^3 + 2n)/(n^6 +2n^5 + 5n^4 +n + 1) <= 1/n^3$
      3.$ n^3(n^3+2n) <= (n^6 +2n^5 + 5n^4 +n + 1)$
      
      4.$ n^6+2n^4 <= (n^6 +2n^5 + 5n^4 +n + 1)$
      5. Stays True so it converges


      
      ]
      #solution[
        Series Converges
      ]
  ]
  #problem(title: "Example 3")[
    #prob[
      Converge or Divergence
      $sum_(n=0)^oo 6/(4^n + 3)$
    ]
    #steps[
      1. DCT can be done on non P-Series tests, in this case it will be a geometeric series
      2.  $sum_(n=0)^oo 6/(4^n) = 6*(4^(-n)) = 6*(4^(-1)^n) = 6(1/4)^n$ 
      3. Geometeric series converges.
      4. $ 6/(4^n + 3) <= 6/4^n$ cause denominator will always be smaller
    ]
    #solution[
      Series Converges cause original is smaller than comparative that converges
    ]

  ]
  #problem(title: "Example 4 - Divergence")[
    #prob[
      Converge or Divergence
      $sum_(n=2)^oo 1/(3n-1)$
    ]
    #steps[
      1. comparative = $sum_(n=2)^oo 1/(3n)$ and it diverges because of P-Series test

      2. $ 1/(3n-1) >= 1/(3n)$ Denominator smaller so fraction will always be large than the new one
      3. Both diverge


    ]
    #solution[
      Series Diverges
    ]
  ]

#problem(title: "Example 5 - Divergence (inconclusive)")[
    #prob[
      Converge or Divergence
      $sum_(n=2)^oo 1/(3n+1)$
    ]
    #steps[
      1. comparative = $sum_(n=2)^oo 1/(3n)$ and it diverges because of P-Series test

      2. $ 1/(3n+1) >= 1/(3n)$ 
      3. Inequality fails


    ]
    #solution[
      DCT fails, use the LCT (Limit Comparision Test)
    ]
  ]



]

#ps(title: "Limit Comparision Test (LCT)", numbering-style: "1")[
  #formula[
    For a series $sum_(n=1)^oo a_n$ and a comparision series $b_n$, $lim_(n->oo) a_n/b_n = lim_(n->oo) "original"/"comparative"$, if the limit is NOT $0$ or $oo$, they both do the samething (converge or diverge)
  ]
  #problem(title: "Example 5 (redo) - Solution (w/LCT now)")[
    #prob[
      Converge or Divergence
      $sum_(n=2)^oo 1/(3n+1)$
    ]
    #steps[
      1. comparative = $sum_(n=2)^oo 1/(3n)$ and it diverges because of P-Series test

      2. $ 1/(3n+1) >= 1/(3n)$ 
      3. Inequality fails
      4. LCT $ lim_(n->oo) 1/(3n+1) / 1/(3n) = (3n)/(3n+1) = 1$ 


    ]
    #solution[
      LCT is conclusive (not 0 or $oo$), thus because the comparative diverged, the original diverges
    ]
  ]

  #problem(title: "Example 6")[
    #prob[
      $sum_(n=3)^oo (n^2 + 4n)/(n^6 -3n^5 + n^3 + 2n -5)$
    ]
    #steps[
      1. DCT, comparative looks like $sum_(n=3)^oo 1/(n^4)$
      2. comparative converges $p > 1$
      - Would need to solve (possible but looks nasty) $(n^2+ 4n)/(n^6 -3n^5 + n^3 + 2n -5) <= 1/n^4$
      3. You can bail, use LCT $lim_(n->oo) (n^2+ 4n)/(n^6 -3n^5 + n^3 + 2n -5) / (1/n^4)$

      4. $lim_(n->oo) (n^4(n^2+ 4n))/(n^6 -3n^5 + n^3 + 2n -5) $
      5. $lim_(n->oo) (n^6 + ...)/(n^6 -3n^5 + n^3 + 2n -5) = 1 $
      6. Limit is non-zero and finite, both must converge because comparative (comparision series conerges)
    ]
    #solution[
      Series Converges because the comparative series of $1/n^4$ converges and doing the LCT has the limit ($lim_(n->oo) "original"/"comparative"$) evaluates to 1. 
    ]
  ]
]
