from useracc import *
from dbconnection import *


def login():
    print('welcome')
    while (user_acc.conn is None):
        print('please sign in')
        id = input('id')
        name = input('name')
        auth(ID,name)

    