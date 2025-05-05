##Calculate Factorial Using a Function
from math import factorial

def GetFactVal(n):
    return factorial(n)

a=int(input("Enter a number: "))
result=GetFactVal(5)
print('Task1 \n Factorial of',a,'is:',  result)
print('Task2 \n' )

##Using the Math Module for Calculations
from math import *

def GetCaluclatedValues(a):
    print('Square Root: ', sqrt(a))
    print('logarithm', log(a))
    print('sine', sin(a))


GetCaluclatedValues(10)
