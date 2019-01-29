import MySQLdb

db = MySQLdb.connect('localhost','asd','1q2w3e4r5t!','moyu')
c = db.cursor()

try:
    sql = 'select * from student where name=%s'
    c.execute(sql,('Manber'))
    data = c.fetchall()
    for d in data:
        print(d)
        
except Exception as e:
    db.rollback()


print('Welecome')


