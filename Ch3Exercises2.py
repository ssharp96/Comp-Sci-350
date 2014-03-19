# Ch 3 Exercises 9-15
# author: SSharp

from turtle import *


t = Turtle("turtle")
"""
# Draws star
t.right(72)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
t.right(144)
t.forward(150)
"""
# Draws clock face
t.penup()
t.pensize(5)
for x in range (12):
    t.forward(110)
    t.pendown()
    t.forward(15)
    t.penup()
    t.forward(25)
    t.stamp()
    t.forward(-150)
    t.right(30)
