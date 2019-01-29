class UserAcc:
    id = 0
    name = ''
    role = 0
    conn = None

    def __init__(self,id = 0,name = '',role=0,conn=None):
        self.id = id
        self.name = name
        self.role = role
        self.conn = conn

    def set_attrs(self,id,name,role,conn):
        self.id = id
        self.name = name
        self.role = role
        self.conn= conn

user_acc = UserAcc()