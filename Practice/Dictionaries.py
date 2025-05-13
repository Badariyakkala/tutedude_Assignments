#Declaring Dictionary
#Dictonary is KEY VALUE Pair
#Inside Dictionary we can add list also but inside list we cannot add Dictionary
    #dict = {kay:value,key1:value1....etc}

dict ={'key1':1,'key2':'Test','key3':{1,2,3}}
print(dict)
#TO print specific Key Value
print(dict['key3'])

#Adding ITEMS to Dictionary
dict['b']='Test123'
print(dict)

#DELETE ITEMS FROM Dictionary
del(dict['b'])
print(dict)

#TO Check Key present In DICTIONARY
print('key3' in dict)

#To Print all Keys and Values in Dictioary
print(dict.keys())
print(dict.values())

#TO Get particular Key value.
print(dict.get('Test')) ##-- If value not exists it will return as "None".
print(dict.get('key4',"'key4' not found" ))