from db import conn,cursor
def insert_emp():
    name=input("enter your name")
    sal=int(input("enter your salary"))
    query="insert into emp (name,sal) values(%s,%s)"
    values=(name,sal)
    cursor.execute(query,values)
    conn.commit()
    print("data inserted")
