#Task 1: Create a Dictionary of Student Marks
sname = input("Enter Student's Name: ")

dic_Student = {"Sai":90,"Ram":99,"Omkar":100}

if (sname in dic_Student.keys()):
    print("Task1:\n {}'s marks : {} ".format(sname,dic_Student[sname]) )
else:
    print("Task1:\n Student Not Found." )

##Task 2: Demonstrate List Slicing
print("\n Tasks2 : ")
lst = [i for i in range(1,11)]
lst.sort()
lst_5 = lst[:5]
print("Original list : ", lst)
print("First five elements :" ,lst_5)
lst_5.reverse()
print("Reversed extracted elements : ", lst_5)