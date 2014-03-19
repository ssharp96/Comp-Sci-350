# Turtle quiz  Jan 24
#
# Draws a horizontal tiled walk made of square tiles.  Every adjacent pair of tiles has a common vertical side.
# The number of tiles is random, between 4 and 10, inclusive.
# The side length of all squares is the same -- a random integer between 30 and 50, inclusive.
# After all tiles are drawn, the turtle is placed in the center of the leftmost square and its color is changed to blue.
# Submit via PAnet.
#
# Author: SSharp

from random import randint
from turtle import *

t = Turtle("turtle")

def drawSquare(t, sideLength):
    ''' Draws a square with turtle t, with the upper-left corner of the square in the current position of t,
        with the side of the square equal sideLength.
        t ends up in the upper-right corner of the square, facing east.
        This implementation includes a loop'''
    # Code for the function goes below:
    for x in range(4):
        t.forward(sideLength)
        t.right(90)
    

# Sets the number of squares to an integer between 4 and 10, inclusive
numSquares =  randint(4,10)

# Sets the side length to an integer between 30 and 50, inclusive
sideLength = randint(30,50)

# Places turtle t into position (-250,0)   
t.penup()
t.goto(-250,0)
t.pendown()

# Draws numSquares squares horizontally, with the neighboring squares sharing a vertical side:
for y in range(numSquares):
    drawSquare(t,sideLength)
    t.forward(sideLength)

# Turtle t is placed in the center of the leftmost square, and turns blue 
a = sideLength/2
t.penup()
t.goto(-250+a,0-a)
t.color("blue")
