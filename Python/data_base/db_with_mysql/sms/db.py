import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Hitesh@29",
        database="sms_linkcode"
    )
    print("connected")
    return conn

get_connection()