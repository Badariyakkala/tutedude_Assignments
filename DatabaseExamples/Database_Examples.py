import psycopg2

def GetData():
    cnn = psycopg2.connect(dbname="demo",user="postgres",password="69596959",port="5432",host="localhost")
    cursor =cnn.cursor()


    cursor.execute('''SELECT * FROM emp;''')
    data = cursor.fetchall()
    print(data[1][0])
    print("Data Inserted Successfully")

    cnn.commit()
    cnn.close()

# GetData()

def InsertedData():
    cnn = psycopg2.connect(dbname="demo",user="postgres",password="69596959",port="5432",host="localhost")
    cursor =cnn.cursor()

    id = input("Enter EmpID:")
    Name = input("Enter EmpName:")


    cursor.execute('''insert into emp VALUES(%s,%s);''',(id,Name))
    print("Data Inserted Successfully")

    cnn.commit()
    cnn.close()

InsertedData()
