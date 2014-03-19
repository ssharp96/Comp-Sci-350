# Turtle Practice
# author: SSharp

from turtle import *

t = Turtle("turtle")

'''
# Draws a blue square

t.color(blue)

for k in range(4):
    t.fd(100)
    t.lt(90)

# Draws a red hexagon

t.color(red)

for k in range(6):
    t.fd(100)
    t.lt(60)
'''

# Draws any shape after user inputs number of sides
n = int(input("Enter a number: "))
print("Watch the turtle draw a",n,"sided figure!")
for k in range(n):
    t.fd(400/n)
    t.lt(360/n)
    
    




