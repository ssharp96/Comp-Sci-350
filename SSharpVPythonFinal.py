# VPython Final Project
# Simon Sharp

from visual import *

# Creates Green Man
head = sphere(pos = (-3,2,0), radius = 0.5, color = color.green)
body = cylinder(pos = (-3,2,0), axis = (0,-2,0), radius = .2, color = color.green)

rleg = cylinder(pos = (-3,.1,0), axis = (-.5,-1.5,0), radius = .15, color = color.green)
lleg = cylinder(pos = (-3,.1,0), axis = (.5,-1.5,0), radius = .15, color = color.green)
rarm = cylinder(pos = (-3,1.3,0), axis = (-.75,-1.,0), radius = .12, color = color.green)
larm = cylinder(pos = (-3,1.3,0), axis = (1,1,0), radius = .12, color = color.green)

# Creates Ball
ball = sphere(pos = (-2,2.3,0), radius = 0.2, color = color.red)

# Creates Blue Man
head2 = sphere(pos = (3,2,0), radius = 0.5, color = color.blue)
body2 = cylinder(pos = (3,2,0), axis = (0,-2,0), radius = .2, color = color.blue)

rleg2 = cylinder(pos = (3,.1,0), axis = (-.5,-1.5,0), radius = .15, color = color.blue)
lleg2 = cylinder(pos = (3,.1,0), axis = (.5,-1.5,0), radius = .15, color = color.blue)
rarm2 = cylinder(pos = (3,1.3,0), axis = (-1,1.,0), radius = .12, color = color.blue)
larm2 = cylinder(pos = (3,1.3,0), axis = (.75,-1,0), radius = .12, color = color.blue)

# Creates Table
table = box(pos = (0,0,0), length = 4.35, width = 2, height = .1, color = color.orange)
tableleg1 = cylinder(pos = (-1.75,-1.5,0), axis = (0,1.5,0), radius = .2, color = color.orange)
tableleg2 = cylinder(pos = (1.75,-1.5,0), axis = (0,1.5,0), radius = .2, color = color.orange)

print("Tim is going to throw Bob the ball.")

a = vector(-2,2.3,0)

# Makes Green throw Ball to Blue
while a.x < 2:
    rate(10)
    ball.pos = a
    a.x = a.x + .1

b = vector(2,2.3,0)

# Makes Blue drop Ball
while b.y >= .1:
    rate(10)
    ball.pos = b
    b.y = b.y - .1

#Gives Blue a Dunce Hat
hat = cone(pos = (3,2.2,0), axis = (0,1,0), radius = .5, color = color.white)

print("Bob dropped the ball! Bob will never succeed in life.")
