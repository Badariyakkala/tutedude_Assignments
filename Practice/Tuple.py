#Adding Tuples.
tup1 =(1,2,3,4)
tup2 = ('Test','Test2','Test3','Test4')
print(tup1+tup2)
print("tup1 :",tup1)
print("length of Tup1 :",len(tup1))

#Tuple is Immutable means we cannot replace item values
#tup1[0] ='99' #This will not work in case of tuple

#Sorting Tuple.
tup1=(2,5,7,8,3)
sort_tup1=sorted(tup1)
print("Before Sorting Tup1:",tup1)
print("After Sorting Tup1:",sort_tup1)
print("Get Item Index Number of Item 8:: ",tup1.index(8))