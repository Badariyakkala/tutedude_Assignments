#Declaring Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

##***Adding lists
print("1st List",list1)
print("2nd List",list2)
print("Adding Multiple lists :" ,list1 + list2)

##Replacing List item values
l =             ['Test','Test2','3']
print("Before Adding Items to list",l)
#INDEX POSITION    0       1      2
#To replace the list Item value need to use List INDEX
#   This Means Mutable means list item value we can change it.
l[2]='Test3'
print("After Adding New Item with Specific Index at Index 2:" ,l)

#list multiplication(means the number which gives that many times it will repeat the list
print("Multiplication of lists:" ,l*2)
'''
Output:
['Test', 'Test2', '3']
print(l*2) --> ['Test', 'Test2', 'Test3', 'Test', 'Test2', 'Test3']
'''

##To check Items in list, It will return "True" if exists else false.
print("Item [Test21] Exists in List : ", 'Test21' in l)

#To Remove Items from List we need to use List Index
print("Before remving Items from list",l)
l.pop(2)
print("After removing the specific Item from List: ",l)

#Adding Items to list with specific Index
l.insert(2,'Test5')
print("Adding new items to list",l)

#To add Items to list, append will add the values to the end of list.
l = ['Test','Test2','3']
l.append('Test8')
print("After adding new Items to list using Apped Method", l)

#To sort the index use sort method
l=[5,8,6,3,2,7]
l.sort()
print("Before Sorting", l)
print("Sorted List: ", l)

#To Reverse the list
l.reverse()
print("Reverse the list", l)
# print(printl)

#TO Get specific Index value
print("full list value:" , l)
print("To Get Index Value of 8",l.index(8))

#To get len of list
print("To Get len of list",len(l))

#To Print the only specific interval of list
print("full list value:" , l)
print("To print only specific Interval of list" ,l[0:3] )
print("To print only specific Interval of list means only 1st 4 times" ,l[1:4] )
print("This will print next alternate items as we have put 2" ,l[0:5:2] )

#Adding Items to Empty List
x=[]
print("Empty List",x)
for i in range(11):
    z=i*2
    x.append(z)
print("Adding Items to Empty List", x)

#Adding Items to Empty List using For loop.
x=[]
x=[i*2 for i in range(11)]
print("Adding Items to Empty List", x)