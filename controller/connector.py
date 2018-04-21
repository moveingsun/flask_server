
import mysql.connector

def get_conn():
    conn = mysql.connector.connect(user='root', password='000000', host='localhost', database='finalprj')
    return conn
