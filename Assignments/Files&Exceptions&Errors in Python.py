##Files, Exceptions, and Errors in Python
###Get Data if File Exists
def GetFileData(Fname):
    try:
        with open(Fname,'r') as file:
            data=file.readlines()
            print('Reading File Content')
            for i, line in enumerate(data):
                print('Line:',i+1,data[i].rstrip('\n'))
    except FileNotFoundError as error:
        print('\n','Error: The file,', "'"+ error.filename+"'", 'was not found')

GetFileData('SampleFile.txt') ##With Exact FileName
GetFileData('SampleFile1.txt') ##With Wrong FileName

##Write and Append Data to a File
def WriteDatatoFile(filename,data):
    try:
        with open(filename,"r+") as file:
            file.write(data)
        with open("output.txt","r+") as file1:
            readData=file1.read()
            print(readData)

    except FileNotFoundError as error:
        print('\n','Error: The file,', "'"+ error.filename+"'", 'was not found')


WriteDatatoFile("output.txt",'Write Data to File')
WriteDatatoFile("output.txt",'Append Data to the File')
WriteDatatoFile("output.txt",'Append Data Third line to the File')
WriteDatatoFile("output1.txt",'Append Data Third line to the File')
