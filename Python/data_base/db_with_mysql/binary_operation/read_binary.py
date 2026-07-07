# file=open("Aesthetic wallpaper.png","rb")
# data=file.read()
# print(data)
# file.close()

# with open("copy_img.png","wb") as file:
#     file.write(data)

import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="Hitesh@29",
    database="sms_linkcode"
)
print("db connected")

cursor=conn.cursor()
#cursor.execute("create table files(id int primary key auto_increment,filename varchar(20) not null, filedata LONGBLOB not null)")
print("table created")
file=open("image.PNG","rb")
data=file.read()
print(data)
file.close()

query="insert into files(filename,filedata) values(%s,%s)"
values=("image.PNG",data)
cursor.execute(query,values)
conn.commit()
print("data saved")

#fetch
cursor.execute("select * from files where id=%s",(1,))
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

cursor.close()
conn.close()