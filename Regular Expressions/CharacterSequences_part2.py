
import re
'''
# *It shows repeated characters  with the possible  matching pattern.
str = 'it is a dog'
pattern="a*" # ^ Matches the beginning of a line.
print("check for repeating character",re.findall(pattern,str,flags=0))

# * It shows repeated characters  with the exact matching pattern.
str = 'it is a dog'
pattern="i+" # ^ Matches the beginning of a line.
print("it will show repeated characters",re.findall(pattern,str,flags=0))
'''
# [] Return character if it is matches to string.
str = 'it is a dog'
pattern="[i]"
print("[] example.",re.findall(pattern,str,flags=0))

# [^XYZ] if any characters present in the string then it will give other characters which are not exists in pattern.
str = 'it is a dog'
pattern="[^it is]"
print(re.findall(pattern,str,flags=0))

#[a-z 0-9] This will return all small characters from a to z and 0 to 9 numbers
#[A-Z 0-9] This will return all capital characters from A to Z.
