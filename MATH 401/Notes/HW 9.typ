#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences/Series",
  assignment: "HW 9",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "April 22, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)


#ps(title: "9.1 Problems")[

  #problem(number: "1")[
    #prob[
      First 3 terms of sequence: ${a_n} = 3^n$
    ]
    #solution[
      ${a_3} = {3,9,27}$
    ]
  ]
  #problem(number: "5")[
    #prob[
      ${a_n} = sin((n pi)/2)$

    ]
    #solution[
      ${a_3} = sin(pi/2), sin(pi), sin(3pi/2))$ \
      ${a_3} = 1, 0, -1$

    ]
  ]
  #problem(number: "7")[
    #prob[
      Find first three of recursive rule. \
      $a_1 = 3$,$a_(x+1) = 2(a_k - 1)$
    ]
    #steps[
      $a_2 = 2(3-1) = 4$
      $a_3 = 2(4-1) = 6$
      $a_4 = 2(6-1) = 10$


    ]
    #solution[
      ${a_n} = {3,4,6, 10} $
    ]
  ]
  #problem(number: "9")[
    #prob[
      ${a_n} = {10/(n+1)}$
    ]
    #solution[
      Matches graph $c$ \ ${a_n}={5, 10/3, 2 1/2 }$
    ]

  ]
  #problem(number: "11")[
    #prob[
      ${a_n} = (-1)^n$
    ]
    #solution[
      Matches graph $d$ \ flip flops from $-1$ to $1$
    ]
  ]
  #problem(number: "17")[
    #prob[
      Simplify Factorials
      $(n+1)!/n!$
    ]
    #steps[
      $(n+1) = (n+1)(n+0)(n-1)...1$\
      $n! = n(n-1)(n-2)...1$ \
      $(n+1)!/n! = ((n+1)(n+0)(n-1)...1)/((n+0)(n-1)...1)$
    ]
    #solution[
      $n+1$
    ]
  ]
  #problem(number: "18")[
    #prob[
      $n!/(n+2)!$
    ]
    #solution[
      $1/((n+2)(n+1))$
    ]
  ]
  #problem(number: "21")[
    #prob[
      Find the limit of the sequence\
      ${a_n} = (5n^2)/(n+2)$
    ]
    #steps[
      $lim_(n->oo) (5n^2)/(n+2)$

    ]
    #solution[
      $oo$
    ]
  ]
  #problem(number: "23")[
    #prob[
      Find limit of the sequence\
      ${a_n} = (2n)/sqrt(n^2 + 1)$

    ]
    #steps[
      ${a_n} = (2n)/n$



    ]
    #solution[
      Converges to $2$
    ]
  ]
  #problem(number: "27")[
    #prob[
      Converge or Diverge: \
      ${a_n} = {sin((pi n)/2)}$

    ]
    #steps[
      Limit DNE for: \
      $lim_(n->oo) sin((pi n)/2)$
    ]
    #solution[
      Diverges
    ]
  ]
  #problem(number: "29")[
    #prob[
      Converge or Diverge? \
      ${a_n} = 5/(n+2)$

    ]
    #steps[
      Take limit
      $ lim_(n->oo) 5/(n+2) = 0$
    ]
    #solution[
      Converges at 0
    ]
  ]
  #problem(number: "31")[
    #prob[
      Converge or Diverge? \
      ${a_n} = (-1)^n n/(n+1)$
    ]
    #steps[
      $(-1)^n$ is going to oscilate, thus won't approach a value so the function diverges
    ]
    #solution[
      Diverges (nth term test)
    ]
  ]
  #problem(number: "33")[
    #prob[
      Converge or Diverge? \
      ${a_n} = (10n^2+3n+7)/(2n^2 - 6)$
    ]
    #steps[
      nth term test
      $lim_(n->oo) (10n^2+3n+7)/(2n^2 - 6) = 5$ because of dominating powers
    ]
    #solution[
      Converges at 1

    ]
  ]
  #problem(number: "35")[
    #prob[
      Converge or Diverge? \
      ${a_n} = ln(n^3)/2n$

    ]
    #steps[
      Move exponent \
      ${a_n} = (3ln(n))/(2n)$ \
      Take limit \
      $lim_(n->oo) (3ln(n))/(2n) = oo/oo $ \
      L'Hopitals
      $lim_(n->oo) (3/n)/(2) = 3/(2n) = 0$
    ]
    #solution[
      Converges at 0
    ]
  ]
  #problem(number: "43")[
    #prob[
      Diverges or Converges?
      ${a_n}={sin(n)/n}$
    ]
    #steps[
      nth term test \
      Bounces around on $[-1, 1]$ \
      $lim_(n->oo) sin(n)/n = [-1, 1]/n = 0$
    ]
  ]
  #problem(number: "45")[
    #prob[
      Write Expression for nth term
      ${a_n} = {2,8,14,20}$

    ]
    #solution[
      ${a_n} = {6n + 2}$
    ]
  ]
  #problem(number: "49")[
    #prob[
      ${a_n} = {2/3, 3/4, 5/6}$


    ]
    #solution[
      ${a_n} = { (n+1)/(n+2) }$
    ]
  ]
  #problem(number: "52")[
    #prob[
      ${a_n} = {1/(2*3), 2/(3*4), 3/(4*5), 4/(5*6)}$
    ]
    #steps[
      Two Factorials that cancel each other out \
      ${a_n} = {1/(2*3), 2/(3*4), 3/(4*5), 4/(5*6)}$
    ]
    #solution[
      ${a_n} = {(n(n!))/(n+2)!}$

    ]
  ]

]

#ps(
  title: "9.2 Problems",
)[

  #problem(
    number: "5",
  )[
    #prob[
      Verify that the series diverges. \
      $sum_(n=1)^oo 3/(2^n -1)$
    ]
    #steps[
      nth term test \
      $lim_(n=oo) 3/(2^n -1) = 0$ inconclusive \
      partial sum \
      No, not telescoping sums\
      integral test \

      Pre Requisites\
      Continous, positive and decrease all look good\

      $lim_(k->oo) integral_1^k 3/(2^x -1) d x$ \

      $lim_(k->oo) 3integral_1^k 1/(2^x -1) d x$ \
      Preform U-Sub\
      $u = 2^x "   "d u = 2^x ln(2)d x "   " (d u)/(2^x ln(2)) = d x "    " (d u)/(u ln(2)) = d x$ \
      $lim_(k->oo) 3 integral_1^k 1/(u-1) (d u)/(u ln(2)) $ \
      Partial Fractions\
      $lim_(k->oo) 3/ln(2) integral_1^k 1/((u-1)u) d u $ \
      $lim_(k->oo) 3/ln(2) integral_1^k 1/(u-1) - 1/u d u $ \
      $lim_(k->oo) 3/ln(2) ln(u-1) - ln(u) |_1^k $ \
      $lim_(k->oo) 3/ln(2) ln(2^x-1) - ln(2^x) |_1^k $ \
      $lim_(k->oo) 3/ln(2) (ln(2^k-1) - ln(2^k)) - (ln(1) - ln(2)) |_1^k $ \
      I'm confused on this one could I have some help, because it's indeterminate the limit doesn't exists and thus the series converges?








    ]
    #solution[
      Diverges
    ]
  ]
  #problem(number: "8")[
    #prob[
      $sum_(n=0)^oo 4(-1.05)^n$

    ]
    #solution[
      $r>= 1 $Geometeric Series Diverges
    ]
  ]
  #problem(number: "13")[

    #prob[
      $sum_(n=1)^oo (2^n +1)/(2^(n+1))$


    ]
    #steps[
      $sum_(n=1)^oo (2^n)/(2^(n+1)) + 1 /(2^(n+1))$\
      $sum_(n=1)^oo (2^n)/(2^(n) * 2) + 1 /(2^(n) * 2)$\
      $sum_(n=1)^oo (1)/(2) + 1 /(2^(n) * 2)$\


      nth term test\
      $lim_(n->oo) (1)/(2) + 1 /(2^(n) * 2) = 1/2 + 0 $\
      Series diverges\


    ]
    #solution[
      nth term test shows series diverges
    ]
  ]
  #problem(number: "15")[
    #prob[
      $sum_(n=0)^oo (5/6)^n$

    ]
    #solution[
      $a = 1 "  " 1/(1-5/6) "  =  6"$
    ]

  ]
  #problem(number: "19")[
    #prob[
      $sum_(n=1)^oo 1/(n(n+1))$
    ]
    #steps[
      nth term test \
      fails\

      Partial Fraction Decomposition\
      $sum_(n=1)^oo 1/(n(n+1))$\

      $1 = A/n + B/(n+1)$\
      $1 = A(n+1) + B(n)$\
      $n = 0 "   " A = 1$\
      $n = -1 "    " B = -1$\
      $sum_(n=1)^oo 1/n - 1/(n+1)$\
      Telescoping sum\
      -Partial sums\
      $lim_(k->oo) S_k = 1 - 1/(k+1)$\



    ]
    #solution[
      1
    ]
  ]
  #problem(number: "37")[
    #prob[
      $0.overline(4)$ as a geometeric series
    ]
    #solution[
      $0.overline(4) = sum_(n=0)^oo 0.4(0.1)^n$
    ]
  ]
  #problem(number: "41")[
    #prob[
      $sum_(n=0)^oo (1.075)^n$
    ]
    #solution[
      Diverges $r =1.075 >= 1$
    ]
  ]
  #problem(number: "43")[
    #prob[
      $sum_(n=1)^oo (n+10)/(10n + 1)$
    ]
    #steps[
      Nth term test\
      $lim_(n->oo) (n+10)/(10n + 1) = 1/10$

    ]
    #solution[
      Diverges, Nth test fails
    ]
  ]
  #problem(number: "45")[
    #prob[
      $sum_(n=1)^oo 1/(n) - 1/(n+2)$


    ]
    #steps[
      Telescoping Sum, Use Partial Sums\
      $lim_(k->oo) S_k = 1 - 1/(k+2)$\
    ]
    #solution[
      Converges at $1$
    ]
  ]
  #problem(number: "47")[
    #prob[
      $sum_(n=1)^oo 3^n/n^3$

    ]
    #steps[
      nth term test\
      $lim_(n->oo) 3^n/n^3 = oo/oo $\ we can do L'hopitals rule
      - If we continue doing L'Hopitals, the bottom will disapear
      $oo/1$
    ]
    #solution[
      Diverges
    ]
  ]


]