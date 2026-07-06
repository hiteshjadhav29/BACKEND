from curd import *
from db import *
def login():
    conn=get_connection()
    cursor=conn.cursor()
    username=input("enter your username")
    password=input("enter your password")
    cursor.execute("select * from login where username=%s",(username,))
    row=cursor.fetchone()
    print(row)
    if row[3]=='admin':
        choice = 0
        while choice!=4:
            print("1.add user\n2.add student\n3.view student\n4.exit")
            choice=int(input("enter choice"))
            match choice:
                case 1:
                    login_user()
                case 2:
                    add_stud()
                case 3:
                    view_stud()
                case 4:
                    exit(0)
                case _:
                    print("ïnvalid input")
    elif row[3]=='user':
        print("1.view student")
        view_stud()
    

login()