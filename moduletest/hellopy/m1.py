import classtest

class BaseClass(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printYourSelf(self):
        print('%s + %s'%(self.name,self.age))


class Inher(BaseClass):
    pass

