# Python Project 1
# author: SSharp

from turtle import *
from random import randint

t = Turtle("turtle")

wn = Screen()

def drawStar (t,L):
    """Draws star with side lengths L starting at 0,0"""
    t.right(72)
    t.color("blue")
    t.forward(L)
    t.right(144)
    t.color("green")
    t.forward(L)
    t.right(144)
    t.color("pink")
    t.forward(L)
    t.right(144)
    t.color("purple")
    t.forward(L)
    t.right(144)
    t.forward(L)
  

L = randint(150,250)

t.penup()
t.goto(0,80)
t.pendown()
t.pensize("5")

drawStar(t,L)
