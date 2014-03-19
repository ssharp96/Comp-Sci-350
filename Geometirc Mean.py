# Geometric Mean
# author:SSharp

import math

def geometricMean(a,b):
    '''Computes and returns geometric mean of a and b'''
    return math.sqrt(a*b)

n1 = float(input("Enter a positive number: "))
n2 = float(input("Enter another positive number: "))
result = geometricMean(n1, n2)

print("The geometric mean of",n1,"and",n2,"is",result)
