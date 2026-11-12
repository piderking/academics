#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences/Series",
  assignment: "HW 10",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "April 28, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

#ps(
  title: "9.3 Problems",
)[
  I did 9.2 Problems til 27 on accidenct, I'll finish the rest of the exercises
  #problem(number: "1")[
    #prob[
      Find Partial Sums
      $1 + 1/4 + 1/9 + 1/16 + 1/25 + ...$\
    ]
    #solution[
      $S_n = 1/(2^(n-1))$\
      \
      $S_1 = 1/1$\
      \
      $S_2 = 1/1 + 1/4$\
      \
      $S_3 = 1/1 + 1/4 + 1/9$\
      \
      $S_4 = 1/1 + 1/4 + 1/9 + 1/16$\
      \
      $S_5 = 1/1 + 1/4 + 1/9 + 1/16 + 1/25$\
      \
    ]

  ]
  #problem(number: "5")[
    #prob[
      \
      Find $sum_(n=1)^oo 3/2^(n-1)$\
      \
      $S_1, S_2, S_3, S_4, S_5$
    ]
    #solution[
      $S_1 = 3/1 $\
      \
      $S_2 = 3/1 + 3/2 $\
      \
      $S_3 = 3/1 + 3/2 + 3/4 $\
      \
      $S_4 = 3/1 + 3/2 + 3/4 + 3/8 $\
      \
      $S_5 = 3/1 + 3/2 + 3/4 + 3/8 + 3/16$\
      \
    ]
  ]
  #problem(number: "9")[
    #prob[
      Verify that the infinity series diverges
      $sum_(n=1)^oo n/(n+1)$

    ]
    #steps[
      DCT \
      \
      $sum_(n=1)^oo n/(n+1)$\
      \
      Verify inequality for divergence
      $n/(n+1) >= 1/n $\
      \ $sum_(n=1)^oo 1/n = oo$ diverges because of P-Series test \
      \
      Evaluate Inequality \
      $n/(n+1) >= 1/n$\
      \
      $n^2/n >= 1 "    "n >= 1$\
      \
      $sum_(n=1)^ oo$



    ]
    #solution[
      DCT inequality holds, orginal is large than function that diverges, thus the original function diverges

    ]
  ]
  #problem(number: "13")[
    #prob[
      Verify Convergence
      $sum_(n=1)^ oo (2^n + 1)/(2^(n+1))$

    ]
    #steps[
      Exponent Rules\
      $sum_(n=1)^ oo (2^n + 1)/(2^(n) * 2)$\
      \
      $1/2 sum_(n=1)^ oo (2^n + 1)/(2^(n))$\
      New equation diverges because is equal to 1, added up infinitely time is infinity
      \
      DCT:
      $(2^n + 1)/(2^(n)) >= (2^n)/(2^n)$ \
      \




    ]
    #solution[
      Diverges, DCT, original will always be larger because the top has a $+1$ in it, thus both will diverge

    ]
  ]
  #problem(number: "15")[
    #prob[
      $sum_(n=0)^oo (5/6)^n$

    ]
    #steps[
      Geometeric Series
      $|r| < 1$
      $1/(1-5/6) = 1(1/6) = 6$

    ]
    #solution[
      Converges at $6$

    ]
  ]
  #problem(number: "20")[
    #prob[
      $sum_(n=1)^oo 1/(n(n+2))$
    ]
    #steps[
      \
      $sum_(n=1)^oo 1/(n(n+2))$\
      \
      Partial Fraction Decomposition\
      \
      $1 = A/n + B/(n+2)$\
      \
      $1 = A(n+2) + B(n)$\
      \ $n = 0 "  " 1 = 2A "   " A = 1/2$\
      \
      $n = -2 "  " 1 = -2B "   " B= -1/2$\
      \
      $sum_(n=1)^oo 1/(2n) - 1/(2(n+2))$\
      \
      Telescoping Sum\
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
      $S_k = 1/2 + 1/4 - 1/(2(k+4)) - 1/(2(k+5)) $\
      \
      $lim_(k->oo) S_k = 1/2 + 1/4 - 1/(2(k+4)) - 1/(2(k+5)) $\
      \
      $lim_(k->oo) S_k = 1/2 + 1/4 - 0 - 0 = 3/4 $\
    ]
    #solution[
      Converges at $3/4$
    ]
  ]
  #problem(
    number: "27",
  )[
    #prob[
      USe Integral Test for Convergence or Divergence
      $sum_(n=1)^oo (2+sin(n))/(n) $

    ]
    #steps[
      Check three steps:
      1. Always positive? Yes, $2 > [-1, 1]$ (range of $sin(x)$)
      2. Continous? Yes, only discontunity is at $x=0$, not in domain $[1, oo)$
      3. Always decreasing? No. $sin(x)$ is a wave function so it will not always be decreasing. Example, derivative.
      $f(x) = 2 + sin(x) "  " g(x) = x$
      $d/(d x)( (f'(x)g(x) - g'(x)f(x))/g(x)^2)$\
      \
      $f'(x) = (cos(x)x - (2+sin(x)) )/(x^2) "     "$ gives both positive and negative number, therefore not always decreasing

    ]
    #solution[
      Integral test doesn't apply.
    ]
  ]
  #problem(number: "35")[
    #prob[
      $ S_n = {1, 1/(2sqrt(2)), 1/(3sqrt(3)), 1/(4sqrt(4)), 1/(5sqrt(5))} $

    ]
    #steps[
      $S_n = {1/n^(3/2)}$

    ]
    #solution[
      Converges: P-Series Test, $p > 1$
    ]
  ]
  #problem(number: "38")[
    #prob[
      $sum_(n=1)^oo 1/n^(pi) $
    ]
    #steps[
      $pi > 1$

    ]
    #solution[
      Converges, P-Series Test
    ]
  ]
  #problem(number: "47")[
    #prob[
      $sum_(n=2)^oo 1/(n (ln(n))^p) $

    ]
    #steps[
      $p = 0$
      Integral Test:
      $lim_(b->oo) integral_(2)^(b) 1/(n (ln(n))^p) d x $\
      \
      $u = ln(x) "    " d u = 1/x d x$ \
      \
      $lim_(b->oo) integral_(2)^(b) u^(-p) d u $\
      \
      $lim_(b->oo) u^(-p+1)/(-p+1) |_2^b $\
      \
      $lim_(b->oo) (1/x)^(-p+1)/(-p+1) |_2^b $\
      \
      $lim_(b->oo) (1/b)^(-p+1)/(-p+1) - (1/2)^(-p+1)/(-p+1) $\
      \

      Integral Test: \

      - Discontinuous when $(1/b)$ is to negative exponent\
      - $p > 1$ for the limit to be valid.




    ]
    #solution[
      $[1, oo)$
    ]
  ]

]

#ps(title: "9.4 Problems")[

  #problem(number: "3")[
    #prob[
      $sum_(n=1)^oo 1/(2n-1) $
    ]
    #steps[
      DCT\
      \
      1. $1/(2n - 1) >= n$ \
      \
      2. $n/(2n - 1) >= 1$\
      \
      3. DCT Fails
      \
      LCT\

      $lim_(n->oo) n / (2n - 1) = 1/2$

    ]
    #solution[
      Converges

    ]
  ]
  #problem(number: "5")[
    #prob[
      $sum_(n=2)^oo 1/(sqrt(n) - 1) $
    ]
    #steps[
      $ 1/(sqrt(n) - 1) >= 1/(sqrt(n)) $
    ]
    #solution[
      Diverges, original larger than function that diverges, denominator is bigger



    ]
  ]
  #problem(number: "7")[
    #prob[
      $sum_(n=2)^oo ln(n)/(n+1) $
    ]
    #steps[
      \
      Converge or Diverge? $sum_(n=2)^oo ln(n)/n$\
      \
      Nth term test\
      $lim_(n->oo) ln(n)/n = oo/oo "   " 1/n / n = 1/n^2$\
      \
      Diverges, It's not going down fast enough cause of numerator (I could do Integral test)\
      $ln(n)/(n+1) <= ln(n)/u$\
      \
      $ln(n)u <= ln(n)(u+1)$\



    ]
    #solution[
      Diverges, DCT is true

    ]
  ]
  #problem(number: "8")[
    #prob[
      $sum_(n=1)^oo 1/sqrt(n^3+1) $
    ]
    #steps[
      $1/sqrt(n^3+1) <= 1/n^(3/2)$\
      \
      $1/n^(3/2)$ converges
    ]
    #solution[
      Converges, DCT

    ]
  ]
  #problem(number: "15")[
    #prob[
      $sum_(n=1)^oo 1/sqrt(n^2 + 1) $
    ]
    #steps[
      $1/sqrt(n^2 + 1) = 1/sqrt(n^2)$\
      \
      $1/sqrt(n^2 + 1) >= 1/n$ because $1/n$ diverges: Inconclusive\
      \
      LCT\
      \
      $lim_(n->oo) n/sqrt(n^2 + 1) = 1$
      - they, lim exists, both diverge




    ]
    #solution[
      Diverges
    ]
  ]
  #problem(number: "17")[
    #prob[
      $sum_(n=1)^oo (2n^2 - 1)/(3n^5 + 2n + 1) $
    ]
    #steps[
      Converges \
      $ (2n^2 - 1)/(3n^5 + 2n + 1) <= 1/(n^3)$ Converges \
      \
      $(2n^2 - 1) (n^3) <= (3n^5 + 2n + 1)$
    ]
    #solution[
      Converges. DCT, Statement True
    ]
  ]
  #problem(number: "18")[
    #prob[
      $sum_(n=1)^oo 1/(n^2(n+3)) $
    ]
    #steps[
      Converges:\
      $sum_(n=1)^oo 1/(n^3+3n^2) <= 1/n^3$\
      \
      $n^3 <= n^3 + 3n^2$

    ]
    #solution[
      Both Converges
    ]
  ]
  #problem(number: "19")[
    #prob[
      $sum_(n=1)^oo 1/sqrt(n^4 + n^2) $
    ]
    #steps[
      Convergence:\
      $1/(n sqrt(n^2 + 1)) <= 1/n^2 $\
      \
      $1 <= (n sqrt(n^2 + 1))/n^2$\
      \
      $1 <= sqrt(n^2 + 1)/n$\
      \
      $n <= sqrt(n^2 + 1)$

    ]
    #solution[
      Converge, DCT
    ]
  ]
  #problem(number: "23")[
    #prob[
      $sum_(n=1)^oo n^(1/3)/n , 1/n^(2/3)$
    ]
    #steps[

    ]
    #solution[
      Divergence, P-Series test
    ]
  ]
  #problem(number: "24")[
    #prob[
      $sum_(n=0)^oo 5(-4/3)^n$
    ]
    #solution[
      Divergence, Geometeric Series: $|r| >= 4/3 $
    ]
  ]
  #problem(number: "26")[
    #prob[
      $sum_(n=2)^oo 1/(n^3 -8) $\

    ]
    #steps[
      Convergence: \

      $1/(n^3 -8) <= 1/(n^3) $
    ]
    #solution[
      Converges, True
    ]
  ]
  #problem(number: "28")[
    #prob[
      $sum_(n=1)^oo (1/(n+1) - 1/(n+2)) $\
      \
      $S_1 = 1/2 - 1/3$\
      \
      $S_2 = 1/2 - 1/3 + 1/3 - 1/4$\
      \
      $S_k = 1/2 - 1/(k+2)$\
      \
      $lim_(k->oo) 1/2 - 0 = 1/2$
    ]

    #solution[
      Converges
    ]
  ]


]
