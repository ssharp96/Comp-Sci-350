# The Quadratic Formula
# author: SSharp

import math

def quadForm1 (a,b,c):
    '''Computes and returns the  x-value with quadratic formula using a plus'''
    return ((-1) * b + math.sqrt(b**2 - 4 * a * c)) /(2 * a)
def quadForm2 (a,b,c):
    '''Computes and returns the  x-value with quadratic formula using a minus'''
    return ((-1) * b - math.sqrt(b**2 - 4 * a * c)) /(2 * a)

a = float(input("Pick a number: "))
b = float(input("Pick another number: "))
c = float(input("Pick a third number: "))

response1 = quadForm1(a,b,c)
response2 = quadForm2(a,b,c)

print("The possible x values are",response1,"or",response2)
