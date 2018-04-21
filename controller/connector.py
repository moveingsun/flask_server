
import mysql.connector

def get_conn():
    conn = mysql.connector.connect(user='root', host='localhost', database='finalprj')
    return conn
