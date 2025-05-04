#IF Statement
# a=input('Enter A Value:')
# if (a=='5'):
#     print('Passed')
# else:
#     print('Failed')

#IF,ELIF and ELSE Statements
Value_1=int(input('Enter first value: '))
Value_2=int(input('Enter second value: '))
Operand= input('Enter Operand operator: ')

if Operand == '+':
    print(Value_1 + Value_2)
elif Operand == '*':
    print(Value_1 * Value_2)
elif Operand == '/':
    print(Value_1 / Value_2)
elif Operand == '-':
    print(Value_1 - Value_2)
else:
    print('Invalid input')



