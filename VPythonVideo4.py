from visual import *

b1 = sphere(pos = vector(0,0,0), radius = 0.5, color = color.cyan)
b2 = sphere(pos = vector(-3,2,0), radius = 0.5, color = color.red)
a1 = arrow(pos = b1.pos, axis = b2.pos-b1.pos, color = color.green)

r = vector(-3,2,0)

while r.x <= 10:
    rate(5)
    print(r.x)
    b2.pos = r
    a1.axis = r #b2.pos-b1.pos
    r.x = r.x+1

while r.x > 10:
    rate(5)
    b2.pos = r
    a1.axis = r
    r.x = r.x - 1



    
