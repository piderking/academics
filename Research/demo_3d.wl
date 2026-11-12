(* Wolfram 3D Interactive Graphics Demo *)
(* Press <leader>s or <leader>ws on any line below to evaluate *)

(* 1. Torus Surface - Click and drag in the Companion to rotate 360° *)
ParametricPlot3D[{Cos[u] (3 + Cos[v]), Sin[u] (3 + Cos[v]), Sin[v]}, {u, 0, 2 Pi}, {v, 0, 2 Pi}, ColorFunction -> "SolarColors", Boxed -> False, Axes -> False]

(* 2. Ripple Surface with ColorFunction *)
Plot3D[Sin[Sqrt[x^2 + y^2]] / Sqrt[x^2 + y^2 + 0.1], {x, -8, 8}, {y, -8, 8}, ColorFunction -> "Rainbow", Mesh -> 20, PlotPoints -> 35]

(* 3. 3D Geometric Primitive Composition *)
Graphics3D[{
  Opacity[0.85], 
  Red, Sphere[{0, 0, 0}, 1], 
  Blue, Cylinder[{{-1.8, 0, 0}, {1.8, 0, 0}}, 0.35], 
  Green, Cone[{{0, 0, 1}, {0, 0, 2.5}}, 0.75],
  Yellow, Cuboid[{-0.5, -0.5, -2}, {0.5, 0.5, -1}]
}, Boxed -> False]

(* 4. Sinc Saddle Function *)
Plot3D[Sin[x] Cos[y], {x, -Pi, Pi}, {y, -Pi, Pi}, ColorFunction -> "SunsetColors"]

(* 5. Standard 2D Plot (retains crisp vector/raster rendering) *)
Plot[{Sin[x], Cos[x], Sin[2 x]}, {x, 0, 2 Pi}, PlotLegends -> "Expressions"]
