##Calculate Factorial Using a Function

def GetFactVal(n):
    b = 1
    c = 1
    while b < n:
        b = b + 1
        c = b * c
    return c

a=int(input("Enter a number: "))
result=GetFactVal(5)

print('Task1: \n Factorial of',a,'is:',  result,'\n')
print('Task2:' )

##Using the Math Module for Calculations
from math import *

def GetCaluclatedValues(a):
    print('Square Root: ', sqrt(a))
    print('logarithm', log(a))
    print('sine', sin(a))


GetCaluclatedValues(10)
