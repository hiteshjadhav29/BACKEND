from db import get_connection
from student import student
from user_class import user


def add_stud():
    conn=get_connection()
    cursor=conn.cursor()
    name=input("ënter your name: ")
    age=int(input("enter your age: "))
    email=input("enter your mail id: ")
    obj=student(name,age,email)
    query="insert into student(name,age,email) values(%s,%s,%s)"
    value=(obj.name,obj.age,obj.email)
    cursor.execute(query,value)
    conn.commit()
    print("student added")

# add_stud()

def login_user():
    conn=get_connection()
    cursor=conn.cursor()
    username=input("enter username")
    password=input("enter pass")
    role=input("enter role")
    obj=user(username,password,role)
    query="insert into login(username,password,role) values(%s,%s,%s)"
    value=(username,password,role)
    cursor.execute(query,value)
    conn.commit()
    print("added")

#login()

def view_stud():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    print(rows)

print(view_stud())