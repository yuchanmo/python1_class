class Person(object):

    def __init__(self,name):
        self.name = name
        print(self.name)
    def sayHello(self):
        print('Hello,my name is',self.name)
    
    def __del__(self):
        print('%s says bye.' %self.name)


# b = Person('tnangnanga')
# a = b
# b.sayHello()
# a.sayHello()
# del a
# a.sayHello()
# del b
# b.sayHello()


class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destoyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1


def ptpt(p):
    print(id(p))

print(id(pt1))
ptpt(pt1)

print(id(pt1) ==id(pt2),id(pt3))
del pt1
del pt2
del pt3


import sys
sys.getrefcount(3)

a = 3
b = 3
c = 3
sys.getrefcount(3)

