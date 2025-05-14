#Creating Function
def add(a,b):
    return a+b

res=add(1,2)
print(res)

#Assigning function to variable

#Calling Function inside function.
def call(a,b):
    return add(a,b)

result = add
print("Calling Function Inside function :" , result(1,2))

#Passing function to the function
def pas(i,j,fn):
    return fn(i,j)

result = pas(1,2,call)
print("passing Function as variable :" , result)

#FILTER FUNCTION AND Filter function will return value only if expression is true.
def even(a):
    return a%2==0

lst = [1,2,3,4,5,6,7,8,9,10]
print("list :" , lst)

##ans = list(filter(even,lst))
#ans = list(filter(lambda x:x%2==0,lst))
ans = list(filter(lambda x:x%2==0,range(11)))
print("Filter Function Output with Only even values : ",ans)


##FILTER FUNCTION it returns value based on the expression.
lst = [1,2,3,4,5,6,7,8,9,10]
ans = list(map(lambda x:x*2,lst))
print("list :" , lst)
print("Map Function Output : ",ans)

#Difference between MAP and function is
#   MAP will execute any expression and Filter will return value only if expression is true.

#The difference between YIELD and Return in function is
 # with YIELD it can return multiple values and Return will return only last value.

 #YIELD EXAMPLE
def fn():
    yield 1
    yield 2
    yield 3

ans = fn()
#print("Getting values from function using YIELD ", next(ans))

for i in ans:
    print(i)
