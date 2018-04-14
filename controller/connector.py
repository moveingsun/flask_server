
import mysql.connector

def get_conn():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='finalprj')
    return conn
