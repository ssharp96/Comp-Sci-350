# Turtle Practice
# author: SSharp

from turtle import *

t = Turtle("turtle")
'''
# Draws a blue square
for k in range(4):
    t.fd(100)
    t.lt(90)

# Draws a red hexagon
for k in range(6):
    t.fd(100)
    t.lt(60)

# Draws any shape after user inputs number of sides
n = int(input("Enter a number: "))
print("Watch the turtle draw a",n,"sided figure!")
for k in range(n):
    t.fd(400/n)
    t.lt(360/n)

# Draws shape with random number of sides
from random import randint
n = randint(3,100)
for k in range(n):
    t.fd(400/n)
    t.lt(360/n)
print("The number of sides is",n)    
'''
# Draws a multicolored circles. CIRCLES BITCHES. 
t.pensize(10)
t.pencolor("green")
t.pu()
t.goto(0,50)
t.pd()
t.circle(50)
t.pu()
t.goto(0,0)
t.pd()
t.pencolor("blue")
t.circle(100)
t.pu()
t.goto(0,-50)
t.pencolor("red")
t.pd()
t.circle(150)
t.pu()
t.goto(0,-100)
t.pencolor("darkgreen")
t.pd()
t.circle(200)

    




