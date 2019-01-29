from fileinput import close

import MySQLdb as m

db_host = 'localhost'
db_user = 'asd'
db_pw = '1q2w3e4r5t!'
db_name = 'moyu'

connect_pool = []

def connectdb():
    connect = m.connect(db_host,db_user,db_pw,db_name)
    return connect


def get_connect():
    global connect_pool
    if not connect_pool:
        connect_tmp = connectdb()
        connect_pool.append(connect_tmp)
    return connect_pool.pop()

def return_connect(conn):
    global connect_pool
    connect_pool.append(conn)
    return

def close_db(db):
    db.close()
    return