import moyumodule

class A:
    yy= 'ssss'
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('A class initialize')

    def printx(self):
        print(self.x)

    @classmethod
    def aclassmethod(cls):
        print(cls.yy)

    def __hash__(self):
        return hash((self.x,self.y))

class B(A):
    def __init__(self,x,y,z):
        # A.__init__(self)  
        super().__init__(x,y)  
        #super().__init__(self,x,y)
        print('B is initialized')

A.aclassmethod()

a = A(2,3)
getattr(a,'x')
# A.printx(a)
# a.printx()

b = B(2,3,4)

s = set()
s.add(a)

ss = {'a','b',{1,2,3}}

aaa = [i for i in range(5)]
aaa.index(4)
aaa