# Turtle Practice 3
# author: SSharp

from turtle import *

t = Turtle("turtle")
"""
t.pensize(5)
t.circle(60)
t.penup()
t.left(90)
t.forward(120)
t.right(90)
t.pendown()
t.circle(45)
t.penup()
t.left(90)
t.forward(90)
t.right(90)
t.pendown()
t.circle(30)
"""
def drawCircle (t,r):
    '''Draws circle centered at current position of t with radius r,
    leaves the turtle at the same position facing east'''
    t.penup()
    t.setheading(0)
    t.forward(r)
    t.left(90)
    t.pendown()
    t.circle(r)
    t.penup()
    t.right(90)
    t.backward(r)
    t.pendown()

t.penup()
t.goto(0,-100)

drawCircle(t,100) #Base circle of snowman

baseR = 100
middleR = baseR*.8
topR = middleR*.8

t.penup()
t.left(90)
t.forward(baseR+middleR)

drawCircle(0,middleR)

