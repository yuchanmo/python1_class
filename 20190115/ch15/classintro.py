class Ph:
    def __init__(self):
        self.y = 5
        self.z = 5
    def printHam(self):
        print('ham')


class Hero:
    def __init__(self,name):
        self.name = name
        self.health = 100
    
    def eat(self,food):
        if food == 'apple':
            self.health -=100
        elif food =='ham':
            self.health+=20

bob = Hero('bob')
print(bob.name)
print(bob.health)
bob.eat('ham')
print(bob.health)

p = Ph()
p.printHam()
print(p.y)
print(p.z)


class Service:
    def sum(self,a,b):
        result = a+b
        print('%s + %s = %s 입니다'%(a,b,result))
        print("{0} +{1} = {2}".format(a,b,result))

pey = Service()
pey.sum(1,1)


# class Foo(object):
#     def __init__(self):
#         self.health = 100


# class SubFoo(Foo):
#     pass


# testobj = SubFoo()
# testobj.health


class Foo(object):
    def __init__(self):
        self.health = 100
    
class SubFoo(Foo):
    def __init__(self):      
        super().__init__()  
        self.muscle = 200


testobj = SubFoo()
testobj.health
testobj.muscle


class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
a.f()
b.f()
a.g()
b.g()