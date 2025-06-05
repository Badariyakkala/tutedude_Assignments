import re
from re import findall, search

'''
#Findall returns string if any characters matches to pattern only from starting
pattern="apple"
str = findall("pp",pattern)
print("findall", str)

#Search:
#Search will return True if characters matched in the string.
pattern="apple"
if re.search(pattern,"bllapple",flags=0):
    print("search Found")
else:
    print("Search not found")


#Match:
#Match will return True only if first 5 characters are matched in the string.
pattern="apple"
if re.match(pattern,"apple",flags=0):
    print("Match Found")
else:
    print("Match not found")
'''

#Replace String Values
str ='it is a dog'
print(re.sub('dog','cat',str,count=1))
