import sqlite3
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import smtplib
import os
from email.message import EmailMessage

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
        create table if not exists Result(
               sid integer primary key,
               sname text not null,
               dcn integer not null,
               java integer not null,
               mic integer not null
               )
""")
# cursor.executemany("""
# INSERT INTO Result (sid, sname, dcn, java, mic)
# VALUES (?, ?, ?, ?, ?)
# """, [
#     (1, 'Kunal', 85, 90, 88),
#     (2, 'Rahul', 78, 82, 80),
#     (3, 'Soham', 92, 89, 95),
#     (4, 'Amit', 70, 75, 72),
#     (5, 'Rohit', 88, 91, 87),
#     (6, 'Priya', 95, 93, 96),
#     (7, 'Sneha', 81, 84, 79),
#     (8, 'Neha', 76, 80, 78),
#     (9, 'Om', 89, 87, 90),
#     (10, 'Akash', 83, 85, 82)
# ])

conn.commit()

def generate_pdf():
    sid = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM Result WHERE sid = ?", (sid,))
    data = cursor.fetchone()

    if not data:
        print("Student ID Not Found")
        return

    total = data[2] + data[3] + data[4]
    percentage = (total / 300) * 100

    filename = f"Result_{data[0]}.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("<b>Student Result Report</b>", styles['Title'])
    elements.append(title)

    table_data = [
        ["Field", "Value"],
        ["Student ID", data[0]],
        ["Student Name", data[1]],
        ["DCN Marks", data[2]],
        ["JAVA Marks", data[3]],
        ["MIC Marks", data[4]],
        ["Total", total],
        ["Percentage", f"{percentage:.2f}%"]
    ]

    table = Table(table_data, colWidths=[150, 200])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),

        ('BACKGROUND', (0,1), (-1,-1), colors.beige),

        ('GRID', (0,0), (-1,-1), 1, colors.black),

        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),

        ('ALIGN', (0,0), (-1,-1), 'CENTER'),

        ('BOTTOMPADDING', (0,0), (-1,0), 12)
    ]))

    elements.append(table)

    doc.build(elements)

    print(f"PDF Generated Successfully: {filename}")
    

    receiver = input("Enter Receiver Gmail: ")
    sender = "hiteshj2900@gmail.com"
    app_password = "Hitesh@29"

    msg = EmailMessage()

    msg["Subject"] = "Student Result PDF"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("Please find the attached Student Result PDF.")

    with open(filename, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(filename)
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, app_password)
            smtp.send_message(msg)

        print("PDF Sent Successfully!")

    except Exception as e:
        print("Error:", e)
ch = 0
while ch!= 9:
    print("1.Add Data\n2.Update Data\n3.Read Data\n4.Search Data\n5.Delete Data\n6.View Result\n7.Generate report\n8.Generate PDF\n9.Exit")
    ch = int(input("Enter you choice: "))
    match ch:
        case 1:
            print("-"*80)
            sid = int(input("Enter Your Id: "))
            name = input("Enetr your name: ")
            dcn = int(input("Enter your DCN marks: "))
            java = int(input("Enter your JAVA marks: "))
            mic = int(input("Enter your MIC marks: "))
            try:
                cursor.execute("insert into Result (sid, sname, dcn, java, mic) VALUES (?,?,?,?,?)",(sid,name,dcn,java,mic))
                conn.commit()
                print("Data Is Inserted Successfully")
                print("-"*80)
            except Exception as e:
                print(e)
                print("-"*80)
        case 2:
            print("-"*80)
            upch = 0
            while upch!= 5:
                print("1.Update Name\n2.Update DCN Marks\n3.Update Java Marks\n4.Update MIC marks:")
                upch = int(input("Enter your update choice: "))
                try:
                    match upch:
                        case 1:
                            upid = int(input("Enetr Your Id: "))
                            newname = input("Enter New Name: ")
                            cursor.execute("Update Result set sname = ? where sid = ?",(newname,upid))
                            if cursor.rowcount > 0:
                                conn.commit()
                                print("Data Updated Successfully")
                                print("-"*80)
                            else:
                                print("Student ID Not Found")
                                print("-"*80)
                        case 2:
                            upid = int(input("Enetr Your Id: "))
                            newdcn = int(input("Enter New DCN Marks: "))
                            cursor.execute("Update Result set dcn = ? where sid = ?",(newdcn,upid))
                            if cursor.rowcount > 0:
                                conn.commit()
                                print("Data Is Updated successfully")
                                print("-"*80)
                            else:
                                print("Data is not Found")
                                print("-"*80)
                        case 3:
                            upid = int(input("Enetr Your Id: "))
                            newjava = int(input("Enter New Java Marks: "))
                            cursor.execute("Update Result set java = ? where sid = ?",(newjava,upid))
                            if cursor.rowcount > 0:
                                conn.commit()
                                print("Data Is Updated successfully")
                                print("-"*80)
                            else:
                                print("Data is not Found")
                                print("-"*80)
                        case 4:
                            upid = int(input("Enetr Your Id: "))
                            newmic = int(input("Enter New Mic Marks: "))
                            cursor.execute("Update Result set mic = ? where sid = ?",(newmic,upid))
                            if cursor.rowcount > 0:
                                conn.commit()
                                print("Data Is Updated successfully")
                                print("-"*80)
                            else:
                                print("Data is not Found")
                                print("-"*80)
                        case 5:
                            print("Returning to main menu...")
                            print("-"*80)
                        case _:
                            print("Invalid Update Choice!")
                            print("-"*80)
                except Exception as e:
                    print(e)
        case 3:
            print("-"*80)
            print("Id\tName\tDCN\tJAVA\tMIC")
            cursor.execute("Select * from Result")
            data = cursor.fetchall()
            for row in data:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
            if not data:
                print("No Record Found")
            print("-"*80)

        case 4:
            print("-"*80)
            sid = int(input("Enter The Id to Search: "))

            cursor.execute("SELECT * FROM Result WHERE sid = ?", (sid,))
            data = cursor.fetchone()

            if data:
                print(f"ID:{data[0]}\tName:{data[1]}\tDCN:{data[2]}\tJAVA:{data[3]}\tMIC:{data[4]}")
            else:
                print("Student ID Not Found")

            print("-" * 80)
        case 5:
            print("-"*80)
            dch = 0
            while dch!= 3:
                print("1.Delete a row\t2.Delete all data\t3.Return to main manu4")
                dch = int(input("Enter a choice: "))
                match dch:
                    case 1 :
                        sid = int(input("Enter the ID: "))
                        cursor.execute("delete from result where sid = ?",(sid,))
                        if cursor.rowcount > 0:
                            conn.commit()
                            print("Row Deleted Successfully")
                            print("-"*80)
                        else:
                            print("Student ID Not Found")
                            print("-"*80)
                    case 2:
                        cursor.execute("delete from Result")
                        conn.commit()
                        print("All DA Deleted Successfully")
                        print("-"*80)
                    case 3:
                        print("Returing to menu")
                        print("-"*80)
                    case _:
                        print("Invalid Choice")
                        print("-"*80)
        case 6:
            print("-"*80)
            print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
            cursor.execute("Select * from Result")
            data = cursor.fetchall()
            for row in data:
                total = row[2] + row[3] + row[4]
                percentage = (total / 300) * 100
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
            if not data:
                print("No Record Found")
            print("-"*80)

        case 7:
            cursor.execute("Select * from Result")
            data = cursor.fetchall()
            print("Pass Student:\n")
            print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
            for row in data:
                total = row[2] + row[3] + row[4]
                percentage = (total / 300) * 100
                if percentage >= 40:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
            print("-"*80)
            print("Fail Student:\n")
            print("ID\tName\tDCN\tJAVA\tMIC\tTotal\tPercentage")
            for row in data:
                total = row[2] + row[3] + row[4]
                percentage = (total / 300) * 100
                if percentage < 40:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{total}\t{percentage:.2f}%")
            print("-"*80)
        case 8:
            generate_pdf()
            
        case 9:
            exit()
        case _:
            print("Inavalid Choice")