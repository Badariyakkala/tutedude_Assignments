#Exception Handling
# try:
#     file1=open("SampleFile.txt","r")
#     data=file1.read()
#     print(data)
#     file1.close()
# except FileNotFoundError:
#     print("File not found")

try:
    with open("SampleFile.txt","r") as file:
        fname=file.name
        data=file.readlines()
        for i, line in enumerate(data):
            print(data[i])
        print(fname)
except FileNotFoundError:
    print("File not found")