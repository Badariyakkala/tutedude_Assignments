#Sets
#It contain Unique values only,
set1 = {1,2,3,4,5,1}
print("Actual set value : {1,2,3,4,5,1}" )
print("set Output",set1)

#Adding Items to Set
set1.add(77)
print("After adding items to Set",set1)

#Remove Items from Set
set1.remove(77)
print("After removing items from Set",set1)

#To check Items in Set
print("IF 5 Item exists in Set",5 in set1)

set2 = {1,2,3,8,33,55}
#To add Common values from Sets
print("set1 :",set1)
print("set2 :",set2)
print("Set1 & Set2 Values :", set1 & set2)

#To add Common values along with other values from two Sets
print("set1.union(set2) :", set1.union(set2))

#It will common values from two sets
print("set1.intersection(set2) :", set1.intersection(set2))

#To Remove Items from Set.
set1 = {1,2,3,4,5,1}
print(set1)
set1.remove(1)
print("After removing items from Set",set1)