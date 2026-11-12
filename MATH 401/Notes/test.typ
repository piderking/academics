#import "template.typ": *

// Apply the show rule directly. You can toggle the theme here!
#show: doc => doc-setup(
  course: "MATH 401",
  unit: "Unit 2: Derivatives",
  assignment: "Homework 2",
  instructor: "Prof. Smith",
  author: "Your Name",
  date: "October 24, 2026",
  toc: true, // Set to false to hide Table of Contents
  theme: "dark", // Try changing this to "dark"!
  doc,
)

// 3. Start using the template!
// By giving the problem set a title, it will show up as the top level in the TOC!
#ps(title: "Part 1: Basic Derivatives", numbering-style: "a)")[

  // We can add a custom title and a description with links!
  #problem(title: "The Power Rule", desc: [Reference: #link("https://example.com")[Textbook Section 2.1]])[
    #prob[
      Find the derivative of $f(x) = x^2$ using the power rule.
    ]
    #steps[
      1. Identify the exponent.
      2. Bring the exponent down to multiply.
      3. Subtract $1$ from the exponent.
    ]
    #important[
      Don't forget the power rule: $d / d x (x^n) = n x^(n-1)$
    ]

    // Here is how you can use a graph!
    // Just pass the path to your image if you have one, e.g., img-path: "my_graph.png"
    #graph(title: "Graph of f(x)", url: "https://www.desmos.com/calculator/ea329ee047324c21861ea29b652fe109")

    #solution[
      $f'(x) = 2x$
    ]

  ]
  #problem(title: "The Power Rule", desc: [Reference: #link("https://example.com")[Textbook Section 2.1]])[
    #prob[
      Find the derivative of $f(x) = x^2$ using the power rule.
    ]
    #steps[
      1. Identify the exponent.
      2. Bring the exponent down to multiply.
      3. Subtract $1$ from the exponent.
    ]
    #important[
      Don't forget the power rule: $d / d x (x^n) = n x^(n-1)$
    ]

    // Here is how you can use a graph!
    // Just pass the path to your image if you have one, e.g., img-path: "my_graph.png"
    #graph(title: "Graph of f(x)", url: "https://www.desmos.com/calculator/ea329ee047324c21861ea29b652fe109")

    #solution[
      $f'(x) = 2x$
    ]

  ]

  #problem(number: "Bonus")[
    #prob[
      Can you prove the power rule?
    ]
    #solution[
      Yes, using limits!
    ]
  ]
]

// The #single block will automatically jump to a new page!
#single(title: "Part 2: Advanced Problems")[
  #problem(title: "Chain Rule Application")[
    #prob[
      This is a massive problem that deserves its own page.
    ]
  ]
]
