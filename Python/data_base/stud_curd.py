import sqlite3
conn=sqlite3.connect("student1.db")
cursor=conn.cursor()

#table creation
cursor.execute('''
            create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null 
               )
''')
print("table created")

#insert
sid = int(input("enter your id"))
sname=input("enter your name")
age=int(input("enter your age"))

cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
conn.commit()
print("data inserted")

#fetch entire rows
cursor.execute("select * from stud")
rows=cursor.fetchall()
print(rows)
for r in rows:
    print(r)
for r in rows:
    print(f"{r[0]}")

#fetch one row
fid=int(input("enter id to fetch"))
cursor.execute("select * from stud where sid=?",(fid,))
row=cursor.fetchone()
print(row)

#update
fid=int(input("enter id to update"))
cursor.execute("select * from stud where sid=?", (fid,))
row=cursor.fetchone()
if fid==row[0]:
    newname=input("enter new name")
    cursor.execute("update stud set name=? where sid=?",(newname,sid))
    conn.commit()
    print("name updated")
else:
    print("no record found")

#fetch record between 
cursor.execute("select * from stud where age between 18 and 25")
row=cursor.fetchall()
print(row)
