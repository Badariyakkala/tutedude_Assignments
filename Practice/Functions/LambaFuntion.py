#In Lamda function we can pass arguments and expression in single line.

#Passing single argument to Lambda
fun=lambda a : a+2
res = fun(5)
print("lambda with single argument :", res)

#Pass two arguments to Lambda
fun = lambda a,b : a+b+5
res = fun(5,10)
print("lambda with two arguments :", res)