#Get mail.com from string
import re
str = "From badari@gmail.com"
pattern= "@([^ ]*)"
print(re.findall(pattern,str,flags=0))