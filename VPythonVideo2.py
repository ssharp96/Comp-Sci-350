from visual import *

S1 = sphere(pos = vector(3,2,0), radius = 0.5, color = color.green)
S2 = sphere(pos = vector(-3,2,0), radius = 0.5, color = color.green)
S3 = sphere(pos = vector(0,-2,0), radius = 0.5, color = color.green)


A1 = arrow(pos = S1.pos, axis = S2.pos - S1.pos, color = color.red)
A2 = arrow(pos = S2.pos, axis = S3.pos - S2.pos, color = color.red)
A3 = arrow(pos = S3.pos, axis = S1.pos - S3.pos, color = color.red)
