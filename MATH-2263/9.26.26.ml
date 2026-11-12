Show [ ContourPlot3D[z^2 == x^2 + y^2, {x, -2, 2}, {y, -2, 2}, {z, 0, 2}], Graphics3D[{PointSize[Large], Red, Point[{1, 1, 1}]}] ]


x^2 + y^2 == z^2 /. {x -> r Cos[\[Theta]], y -> r Sin[\[Theta]]} // Simplify
d = Sqrt[x^2 + y^2 + z^2] /. {x -> r Cos[\[Theta]], y -> r Sin[\[Theta]], z^2 -> r^2} // Simplify

RevolutionPlot3D[d, {r, -5, 5}, {\[Theta], 0, 2 \[Pi]} ]
