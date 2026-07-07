

import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Hitesh@29",
    database="sms_linkcode"
)
print("db connected")

cursor=conn.cursor()
cursor.execute("create table if not exists binar(id int primary key auto_increment,filename varchar(20) not null, filedata LONGBLOB not null)")
print("table created")
ch=0
while ch!=5:
    print("1.upload resume\n2.read data\n3.update name\n4.delete resume\n5.exit")
    ch=int(input("enter choice"))
    match ch:
        case 1:
            res=input("enter resume filename with .pdf extension")
            try:
                with open(res, "rb") as file:
                    data = file.read()
            except FileNotFoundError:
                print("File not found.")
                continue
            #print(data)
            file.close()
            #inserting the data into database
            query="insert into binar(filename,filedata) values(%s,%s)"
            values=(res,data)
            cursor.execute(query,values)
            conn.commit()
            print("data saved")
        
        case 2:
            cid=int(input("enter id to read data"))

            #fetch
            cursor.execute("select * from binar where id=%s",(cid,))
            record=cursor.fetchone()
            if record:
                filename=record[1]
                filedata=record[2]
                #save to sys
                file=open(filename,"wb")
                file.write(filedata)
                file.close()
                print("downloaded")
            else:
                print("record not found")

        case 3:
            print("values updated ")

        case 4:
            
            cid = int(input("Enter ID to delete: "))

            cursor.execute("DELETE FROM binar WHERE id=%s", (cid,))
            conn.commit()

            if cursor.rowcount > 0:
                print("Resume deleted.")
            else:
                print("Record not found.")
        
        case 5:
            exit(0)
        case _:
            print("ïnvalid choice")

cursor.close()
conn.close()
print("Database connection closed.")

    