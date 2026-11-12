// template.typ

#let theme-state = state("theme", "light")

#let doc-setup(
  course: none,
  unit: none,
  assignment: none,
  instructor: none,
  author: none,
  date: none,
  doc-type: "notes",
  toc: false,
  theme: "light",
  doc
) = {
  theme-state.update(theme)

  let page-bg = if theme == "dark" { rgb("#1e1e1e") } else { white }
  let text-fg = if theme == "dark" { rgb("#eeeeee") } else { black }

  set page(
    paper: "us-letter",
    fill: page-bg,
    header: context {
      set text(fill: text-fg)
      let display-title = if assignment != none { assignment } else { "Notes" }
      if doc-type == "notes" {
        align(right)[*Notes* - #display-title]
      } else if doc-type == "ps" {
        align(right)[*Problem Set* - #display-title]
      }
    },
    footer: context {
      set text(fill: text-fg)
      let page-num = counter(page).display("1")
      align(center)[
        #if toc or doc-type == "notes" {
          link(<toc>)[#page-num]
        } else {
          page-num
        }
      ]
    }
  )
  
  // Standard formatting
  set text(size: 11pt, fill: text-fg)
  set par(leading: 1em, spacing: 1.5em)
  
  // Make all math use display style to fix squished limits/summations and size
  show math.equation.where(block: false): it => math.display(it)
  
  // Custom styling for Problem headings (Level 2)
  show heading.where(level: 2): it => {
    v(1em)
    text(weight: "bold", size: 12pt)[
      #if it.numbering != none {
        context counter(heading).display(it.numbering)
        if it.body != none and it.body != [] {
          [: #it.body]
        }
      } else {
        it.body
      }
    ]
    v(0.5em)
  }
  
  // Front Page
  if course != none or assignment != none or instructor != none {
    v(1fr) // Push to center
    align(center)[
      #if course != none [
        #text(size: 24pt, weight: "bold")[#course] \
        #v(0.5em)
      ]
      #if unit != none [
        #text(size: 16pt)[#unit] \
        #v(0.5em)
      ]
      #if assignment != none [
        #text(size: 20pt, weight: "bold")[#assignment] \
        #v(1em)
      ]
      #if instructor != none [
        Instructor: #instructor \
      ]
      #if author != none [
        Author: #author \
      ]
      #if date != none [
        Date: #date \
      ]
    ]
    v(1.5fr) // Push to center
    pagebreak(weak: true)
  }
  
  // Table of Contents
  if toc or doc-type == "notes" {
    [#metadata("toc") <toc>]
    outline(title: "Table of Contents", indent: auto)
    pagebreak(weak: true)
  }
  
  doc
}

// Problem Set Page Setup
#let ps(title: none, numbering-style: "1.", body) = {
  pagebreak(weak: true)
  if title != none {
    heading(level: 1, numbering: none)[#title]
    counter(heading).step(level: 1)
  } else {
    counter(heading).step(level: 1)
  }
  set heading(numbering: (..args) => {
    "Problem " + numbering(numbering-style, args.pos().last())
  })
  set enum(numbering: numbering-style)
  body
}

// Single Problem Page Setup
#let single(title: none, body) = {
  pagebreak(weak: true)
  if title != none {
    heading(level: 1, numbering: none)[#title]
    counter(heading).step(level: 1)
  } else {
    counter(heading).step(level: 1)
  }
  set heading(numbering: (..args) => "Problem")
  body
}

// Problem Wrapper
#let problem(number: auto, title: none, desc: none, body) = {
  if number == auto {
    heading(level: 2)[#title]
  } else {
    let head-text = [Problem #number]
    if title != none { head-text = head-text + [: #title] }
    heading(level: 2, numbering: none)[#head-text]
  }
  
  if desc != none {
    v(0.2em)
    context {
      let t = theme-state.get()
      let desc-color = if t == "dark" { rgb("#aaaaaa") } else { rgb("#555555") }
      text(fill: desc-color, style: "italic")[#desc]
    }
  }
  
  v(0.5em)
  block(width: 100%, body)
  v(1em)
}

// Formatting Boxes

#let prob(body) = context {
  let t = theme-state.get()
  let bg = if t == "dark" { rgb("#3b1c1c") } else { rgb("ffe5e5") }
  block(
    fill: bg,
    stroke: red,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [*Problem:* \ #body]
  )
}

#let notes(body) = context {
  let t = theme-state.get()
  let outline-color = if t == "dark" { luma(200) } else { black }
  block(
    stroke: outline-color,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [*Notes:* \ #body]
  )
}
#let steps(body) = context {
  let t = theme-state.get()
  let outline-color = if t == "dark" { luma(200) } else { black }
  block(
    stroke: outline-color,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [*Steps:* \ #body]
  )
}

#let solution(body) = context {
  let t = theme-state.get()
  let bg = if t == "dark" { rgb("#1c3b1c") } else { rgb("e5ffe5") }
  block(
    fill: bg,
    stroke: green,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [
      #show heading: it => text(weight: "bold", size: 11pt)[#it.body:]
      #heading(level: 3, numbering: none)[Solution] \
      #body
    ]
  )
}

#let important(body) = context {
  let t = theme-state.get()
  let bg = if t == "dark" { rgb("#3b2a1c") } else { rgb("ffebd6") }
  block(
    fill: bg,
    stroke: orange,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [
      #show heading: it => text(weight: "bold", size: 11pt)[#it.body:]
      #heading(level: 3, numbering: none)[Important] \
      #body
    ]
  )
}

#let formula(title: none, body) = context {
  let t = theme-state.get()
  let bg = if t == "dark" { rgb("#3b2a1c") } else { rgb("ffebd6") }
  block(
    fill: bg,
    stroke: orange,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    [
      #show heading: it => text(weight: "bold", size: 11pt)[#it.body:]
      #if title != none {
        heading(level: 3, numbering: none)[Formula: #title]
      } else {
        heading(level: 3, numbering: none)[Formula]
      } \
      #body
    ]
  )
}
// Graph Object
#let graph(title: "Graph", img-path: none, url: none) = {
  v(1em)
  heading(level: 3, numbering: none)[Graph: #title]
  v(0.5em)
  align(center)[
    #if img-path != none {
      image(img-path, width: 80%)
    } else {
      block(
        width: 80%, 
        height: 150pt, 
        stroke: (dash: "dashed", paint: gray),
        align(center + horizon)[_Graph Placeholder_ \ #if url != none { link(url)[(Interactive Desmos)] }]
      )
    }
    
    #if url != none and img-path != none {
      v(0.5em)
      link(url)[#text(fill: blue)[#underline[View Interactive Desmos Page]]]
    }
  ]
  v(1em)
}
