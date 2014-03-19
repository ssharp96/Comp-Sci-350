from visual import *

head = sphere(pos = (-1,2,0), radius = .5, color = color.white)
body = cylinder(pos = (-1,2,0), axis = (-2,0,0), radius = .3, color = color.blue)

rarm = cylinder(pos = (-2,2,0), axis = (1.5,1,0), radius = .2, color = color.blue)
larm = cylinder(pos = (-2,2,0), axis = (1.5,-1,0), radius = .2, color = color.blue)

rleg = cylinder(pos = (-3,2.1,0), axis = (-1.5,.7,0),radius = .22, color = color.blue)
lleg = cylinder(pos = (-3,1.9,0), axis = (-1.5,-.7,0),radius = .22, color = color.blue)

a = vector(-1,2,0)
while a.x <= 10:
    rate(10)
    head.pos = a
    a.x = a.x+.1

b = vector(-1,2,0)
while b.x <= 10:
    rate(10)
    body.pos = b
    b.x = b.x+.1


