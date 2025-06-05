
import re
# ^ Matches the beginning of a line.
str = 'it is a dog'
pattern="^i" # ^ Matches the beginning of a line.
print("check for first character",re.findall(pattern,str,flags=0))

# $ Matches to last character of line.
str = 'it is a dog'
pattern="g$"
print("check for last character",re.findall(pattern,str,flags=0))

# . Matches to any character
str = 'it is a dog'
pattern=".g"
print("check for any character",re.findall(pattern,str,flags=0))

#\d returns any digit value from string
str = 'it is a dog 9a9b'
pattern= "\\d"
print("check for all digits",re.findall(pattern,str,flags=0))

#\D returns any non-digit value from string
str = 'it is a dog 9a9b'
pattern= "\\D"
print("check for non-Digit digits",re.findall(pattern,str,flags=0))

#\s returns white space.
str = 'it is a dog 9a 9b'
pattern= "\\s"
print("check for white space",re.findall(pattern,str,flags=0))

#\S returns non white space.
str = 'it is a dog 9a 9b'
pattern= "\\S"
print("check for white space",re.findall(pattern,str,flags=0))