a="python"
print(a)
#Using this it will capitalize only first letter and make other letters are small.
print("To Capitalize String: ",a.capitalize())
print("To Capitalize whole String: ",a.upper())
print("To make small characters whole String: ",a.lower())
print("string is Numeric: " , a.isnumeric())
print("string is Alpha: " , a.isalpha())
print("string is Startwith I: " , a.startswith("I"))
print("string is Startwith p: " , a.startswith("p")) #It is case sensitive.
print("string is EndsWith n: " , a.endswith("n")) #It is case sensitive.

str = "India is my country"
print("Original String :", str)
print("Replaced Value : ", str.replace("India", "US"))
str = "india is my country"
#find character in string
print("Original Value: ", str)
print("find Charater Index of Letter i",str.find("i"))

str = "    india is my country    "

print("Original Value: ", str)
print("Removing Left space :" ,str.lstrip())
print("Removing both Left and right space :" ,str.strip())

str = "Welcome to Python"
print("Original Value: ", str)
print("Splitting the string Value using Splitlines function:" ,str.splitlines())
print("Splitting the string Value using Split function:" ,str.split())

##To Print Multiple Values using format method.
Name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello {} you are {} years old ".format(Name,age))

#Format method is using Index numbers.
first ="apple"
second ="Banana"
third ="orange"
print("{2} {1} {0} ".format(first,second,third))

#FORMATTING STRING WITH DECIMAL POINTS ,2f menas it will print that many decimal points
price= 100
Tax_percent = 50
print("price is {:.2f} with tax value is {:.2f}".format(price,Tax_percent))