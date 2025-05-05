##new functions
# def GetString():
#     print("Getting String")
#
# GetString()
#
# def GetValue(a,b):
#     c= a+b
#     return c
# result=GetValue(10,20)
# print(result)

##Importing Modules
#Method 1
import math
print(math.pi)

#Method 2
from math import pi
print(pi)

#Method 3
from math import *
print(pi)

#Factorials
#4!= 4*3*2*1=24

def GetFactVal(n):
    a=n*factorial(n-1)
    return a

result=GetFactVal(4)
print(result)

#LOCAL AND GLOBAL Variables.
