

import mysql.connector  as d
import sys



def clearscreen():
    for i in range(8):
        print()


def menu():
    try:
            
        l = 'y'
        while l.lower() == 'y':
            print("--------------MENU--------------------")
            print("1.Show Databases. \n2.Show Tables. \n3.Insert Record. \n4.Update Record. \n5.Delete Record. \n6.Search Record. \n7.Display Record. \n8.EXIT")
            print("-----------------------------------")
            clearscreen()
            choice = int(input("Enter the choice (1-8):"))

            if choice == 1:
                show_databases()
            elif choice == 2:
                show_tables()
            elif choice == 3:
                insert_record()
            elif choice == 4:
                update_record()
            elif choice == 5:
                delete_record()
            elif choice == 6:
                search_record()
            elif choice == 7:
                display_record()
            elif choice == 8:
                print("You are now exit the program. ")
                break
            else:
                print("Wrong Choice")
            input("press ENTER KEY to continue.....")
        else:
            sys.exit()
    except Exception as e:
        print("Error : ")

def show_databases():
    try:
        mydb = d.connect(host = "localhost",user = "root",passwd = "123")
        if mydb.is_connected():
            cur = mydb.cursor()
            cur.execute('show databases')
            for i in cur:
                print(i)
            mydb.close()
    except d.Error as err:
        print("Error:",err)


def show_tables():
    try:
        mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
        if mydb.is_connected():
            print("Sucessfully Connected")
            cur = mydb.cursor()
            cur.execute("Show tables")
            for i in cur:
                print(i)
            mydb.close()
    except d.Error as err:
        print("Error : ",err)

def insert_record():
    mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
    if mydb.is_connected():
        cur = mydb.cursor()
        ID = int(input("ENTER EMPLOYEE ID : "))
        NAME = input("ENTER EMPLOYEE NAME : ")
        SALARY = float(input("ENTER EMPLOYEE SALARY : "))
        DEPT = input("ENTER EMPLOYEE DEPARTMENT : ")
        PHONE = int(input("ENTER EMPLOYEE PHONE NUMBER : "))
        ADDRESS = input("ENTER EMPLOYEE ADDRESS : ")
        query1 = "INSERT INTO emp VALUES({},'{}',{},'{}',{},'{}')".format(ID, NAME, SALARY, DEPT, PHONE, ADDRESS)
        cur.execute(query1)
        mydb.commit()
        print("Record Inserted")
        mydb.close()
    else:
        print("Error : Not connected")


def update_record():
    mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
    cur = mydb.cursor()
    de = int(input("Enter Employee ID for update record : "))
    ID = int(input("ENTER NEW EMPLOYEE ID : "))
    name = input("ENTER NEW NAME OF EMPLOYEE : ")
    salary = float(input("ENTER NEW SALARY FOR EMPLOYEE : "))
    dept = input("ENTER NEW DEPARTMENT OF EMPLOYEE : ")
    phone = int(input("ENTER NEW EMPLOYEE PHONE NUMBER : "))
    address = input("ENTER ADDRESS OF NEW EMPLOYEE : ")
    query1 = "update emp set id=%s, employee_name='%s', salary=%s, department='%s', phone=%s, address='%s' where id=%s" %(ID,name,salary,dept,phone,address,de)
    cur.execute(query1)
    mydb.commit()
    print("Record Updated")
    mydb.close()



def delete_record():
    mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
    cur = mydb.cursor()
    de = int(input("Enter Employee ID for deleting record : "))
    query1 = "delete from emp where id={0}".format(de)
    cur.execute(query1)
    mydb.commit()
    print("Record Deleted")
    mydb.close()



def search_record():
    mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
    cur = mydb.cursor()
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO SEARCH RECORD: ")
    print("1.ACCORDING TO ID")
    print("2.ACCORDING TO NAME")
    print("3.ACCORDING TO SALARY")
    print("4.ACCORDING TO DEPARTMENT")
    choice = int(input("Enter your choice(1-4) : "))
    if choice == 1:
        ID = int(input("Enter Employee ID Which you want to search : "))
        query1 = "select * from emp where id=%s" %(ID)
    elif choice == 2:
        name = input("Enter Employee Name Which you want to search : ")
        query1 = "select * from emp where employee_name='%s'" %(name)
    elif choice == 3:
        salary = float(input("Enter Employee Salary Which you want to search : "))
        query1 = "select * from emp where salary=%s" %(salary)
    elif choice == 4:
        department = input("Enter Employee department Which you want to search : ")
        query1 = "select * from emp where department='%s'" %(department)
    else:
        print("Wrong Choice")
    cur.execute(query1)
    rec = cur.fetchall()
    count = cur.rowcount
    print("Total no. of record found : ",count)
    for i in rec:
        print(i)
    print("Record Searched")
    mydb.close()



def display_record():
    try:
        mydb = d.connect(host = "localhost",user = "root",passwd = "123",database = "employee")
        if mydb.is_connected():
            cur = mydb.cursor()
            cur.execute("select * from emp")
            rec = cur.fetchall()
            count = cur.rowcount
            print("+---------|--------------|---------|---------|---------|--------------------------+")
            print("+ Emp ID  | Emp name     |  Salary |   Dept  |  Phone  | Address                  |")
            print("+---------|--------------|---------|---------|---------|--------------------------+")
            for i in rec:
                print('|{0:^8} |{1:10}    | {2:7} | {3:7} | {4:5} | {5:10} |'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            print("+---------|--------------|---------|---------|---------|--------------------------+")
            print("+          Total no. of records are : ",count,"                                         |")
            print("+---------------------------------------------------------------------------------+")
            mydb.close()
    except d.Error as err:
        print("Error : ",err)



menu()
