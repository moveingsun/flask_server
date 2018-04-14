from controller import connector


def get_user_info(username, password):
    cnx = connector.get_conn()
    cursor = cnx.cursor()

    query = "select * from userinfo where UserName = '{}' and Password = '{}'".format(username, password)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result

if __name__=='__main__':
    get_user_info('kurt')