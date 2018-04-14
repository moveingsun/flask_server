import datetime
from controller import connector

cnx = connector.get_conn()
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")


query = "select * from userinfo"
cursor.execute(query)

for (UserName, Password, Role) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
      UserName, Password, Role))

cursor.close()
cnx.close()