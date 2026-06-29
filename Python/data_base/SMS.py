import sqlite3
conn=sqlite3.connect("sms.db")
cursor=conn.cursor()

cursor.execute('''
            create table if not exists stud(
               sid integer primary key,
               sub text not null,
               marks integer null 
               )
''')
print("table created")

while True:
    print(" 1.add\n 2.update\n 3.view\n 4.delete\n 5.view result\n 6.reports\n 7.exit\n")
    choice=int(input("enter choice"))
    match(choice):
        case 1:
            sid = int(input("enter your id"))
            sub=input("enter subject")
            marks=int(input("enter your marks"))

            cursor.execute("insert into stud (sid,sub,marks) values(?,?,?)",(sid,sub,marks))
            conn.commit()
            print("data inserted")
        case 2:
            print("1.update marks\n 2.update subject")
            choice=int(input("enter choice"))
            match(choice):
                case 1:
                    fid=int(input("enter id to update"))
                    cursor.execute("select * from stud where sid=?", (fid,))
                    row=cursor.fetchone()
                    if row:
                        newmarks=input("enter new marks")
                        cursor.execute("update stud set marks=? where sid=?",(newmarks,fid))
                        conn.commit()
                        print("name updated")
                    else:
                        print("no record found")
                
                case 2:
                    fid=int(input("enter id to update"))
                    cursor.execute("select * from stud where sid=?", (fid,))
                    row=cursor.fetchone()
                    if row:
                        newsub=int(input("enter new sub"))
                        cursor.execute("update stud set sub=? where sid=?",(newsub,fid))
                        conn.commit()
                        print("name updated")
                    else:
                        print("no record found")
        
        case 3:
            print("1.read particular\n 2.read all")
            choice=int(input("enter choice"))
            match(choice):
                case 1:
                    fid=int(input("enter id to fetch"))
                    cursor.execute("select * from stud where sid=?",(fid,))
                    row=cursor.fetchone()
                    print(row)
                
                case 2:
                    cursor.execute("select * from stud")
                    rows=cursor.fetchall()
                    print(rows)

        case 4:
            print("1.delete one\n 2.delete all\n")
            choice=int(input("enter choice"))
            match(choice):
                case 1:
                    fid=int(input("enter id to delete"))
                    cursor.execute("delete from stud where sid=?",(fid,))
                    conn.commit()
                    print("Record deleted")

                case 2:
                    cursor.execute("delete from stud")
                    conn.commit()
                    print("All records deleted")

        case 5:
            print("result")
            fid=int(input("enter id to view result"))

            cursor.execute("select * from stud where sid=?",(fid,))
            row=cursor.fetchone()

            if row:
                print("Roll No :", row[0])
                print("Subject :", row[1])
                print("Marks :", row[2])
                print("Percentage :", row[2],"%")
            else:
                print("No record found")

        case 6:
            print("reports")
            fid=int(input("enter id"))

            cursor.execute("select * from stud where sid=?",(fid,))
            row=cursor.fetchone()

            if row:

                if row[2] >= 35:
                    print("PASS")
                else:
                    print("FAIL")
            else:
                print("No record found")
        
        case 7:
            exit(0)

        case _:
            print("invalid input")
            