#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 3: Squences/Series",
  assignment: "HW 11",
  instructor: "Keith Clayton",
  author: "Peter Bowman",
  date: "May 11, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

#ps(title: "9.5 Problems")[
  #problem(number: "5")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo (-1)^(n+1) / (n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "7")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo (-1)^n / 3^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "9")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo ((-1)^n (5n-1)) / (4n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "11")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo ((-1)^n n) / ln(n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "13")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo (-1)^n / sqrt(n) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "15")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo ((-1)^(n+1) (n+1)) / ln(n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "17")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo sin((2n-1)pi / 2) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "19")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=0)^oo (-1)^n / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "16")[
    #prob[
      Determine the convergence or divergence of the series.
      $ sum_(n=1)^oo ((-1)^(n+1) ln(n+1)) / (n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "31")[
    #prob[
      Use Theorem 9.15 to determine the number of terms required to approximate the sum of the series
      $ sum_(n=1)^oo (-1)^(n+1) / n^3 $
      with an error of less than 0.001.
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "37")[
    #prob[
      Determine absolute/conditional convergence or divergence.
      $ sum_(n=1)^oo (-1)^n / 2^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "39")[
    #prob[
      Determine absolute/conditional convergence or divergence.
      $ sum_(n=1)^oo (-1)^n / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "41")[
    #prob[
      Determine absolute/conditional convergence or divergence.
      $ sum_(n=1)^oo (-1)^(n+1) / sqrt(n) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "43")[
    #prob[
      Determine absolute/conditional convergence or divergence.
      $ sum_(n=1)^oo ((-1)^(n+1) n^2) / (n+1)^2 $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "53")[
    #prob[
      Determine absolute/conditional convergence or divergence.
      $ sum_(n=1)^oo cos(n pi) / n^2 $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
]

#ps(title: "9.6 Problems")[
  #problem(number: "1")[
    #prob[
      Verify the formula.
      $ (n+1)! / (n-2)! = (n+1)(n)(n-1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "13")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=1)^oo 1 / 5^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "15")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=0)^oo n! / 3^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "17")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=1)^oo n (6/5)^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "19")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=1)^oo n^3 / 3^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "21")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=1)^oo n / 4^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "23")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=0)^oo ((-1)^n 2^n) / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "25")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=1)^oo n! / (n 3^n) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "27")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=0)^oo e^n / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "29")[
    #prob[
      Use the Ratio Test to determine convergence or divergence.
      $ sum_(n=0)^oo 6^n / (n+1)^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "39")[
    #prob[
      Use the Root Test to determine convergence or divergence.
      $ sum_(n=1)^oo ((3n+2)/(n+3))^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "53")[
    #prob[
      Determine convergence or divergence using any appropriate test.
      $ sum_(n=1)^oo 3 / (n sqrt(n)) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "61")[
    #prob[
      Determine convergence or divergence using any appropriate test.
      $ sum_(n=1)^oo cos(n) / 3^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
]

#ps(
  title: "9.8 Problems",
)[
  #problem(number: "5")[
    #prob[
      Find the radius of convergence.
      $ sum_(n=0)^oo (-1)^n x^n / (n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "7")[
    #prob[
      Find the radius of convergence.
      $ sum_(n=1)^oo (4x)^n / n^2 $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "11")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=0)^oo (x/4)^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "13")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=0)^oo (2x)^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "15")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=0)^oo x^(5n) / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "17")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=0)^oo (2n)! (x/3)^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "19")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=1)^oo ((-1)^(n+1) x^n) / 6^n $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "21")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=1)^oo ((-1)^(n+1) (x-4)^n) / (n 9^n) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "23")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=1)^oo ((-1)^(n+1) (x-2)^n) / (n 2^n) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "25")[
    #prob[
      Find the interval of convergence (include endpoint checks).
      $ sum_(n=1)^oo (x-3)^(n-1) / 3^(n-1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(number: "41")[
    #prob[
      Write an equivalent series with the index of summation beginning at $ n=1 $ for
      $ sum_(n=0)^oo x^n / n! $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
  #problem(
    number: "47",
  )[
    #prob[
      Find the intervals of convergence (including endpoint checks) of (a) $ f(x) $, (b) $ f'(x) $, (c) $ f''(x) $, and (d) $ integral f(x) d x $ for:
      $ f(x) = sum_(n=0)^oo ((-1)^(n+1) (x-1)^(n+1)) / (n+1) $
    ]
    #steps[

    ]
    #solution[

    ]
  ]
]