class Person():
    def speak(self):
        print('I can speak')

class Man(Person):
    def wear(self):
        print('I wear shirt')

class Woman(Person):
    def wear(self):
        print('I wear skirt')

man = Man()
man.wear()
man.speak()


class Parent:
    def myMethod(self):
        print('Calling parent method')

class Child(Parent):
    def myMethod(self):
        print('Calling child method')

    def myMethod(self,a):
        super().myMethod()
        print(self.myMethod(),a)

c = Child()
c.myMethod('aa','aa')

class A(object):
    def __init__(self,x):
        self.x = x

    def f(self):
        return 10*self.x

class B(A):
    def g(self):
        return 1000*self.x

print(A(5).f())
print(B(7).g())
print(B(7).f())
print(A(5).g())

class Test:
    def a(self):
        print('Test class')

    def a(self,agg):
        print('Test class 2',agg)


t = Test()
t.a()


class A(object):
    def __init__(self,x):
        self.x = x

    def f(self):
        return 10*self.x

    def g(self):
        return 100*self.x

    def h(self,a,b):
        print(a,b,c)

import sys

print(sys.path)

class B(A):
    
    def __init__(self,x=42,y=99):
        super().__init__(x)
        self.y = y
    
    def f(self):
        return 100*self.x

    def g(self):
        return (super().g(),self.y)

    def h(self,a,b,c):
        super().h(a,b)
        print('additional print',c)

a = A(33)
b = B(2323,3434)
b.h(5656,7878)


print(type(a)==A)
print(type(b)==A)
print(isinstance(b,A))
print(isinstance(a,B))
print(isinstance(a,A))

class A:
    def A(self):
        print('I am A')

class B:
    def A(Self):
        print('I am a')

    def B(self):
        print('I am B')

class C(A,B):
    def C(self):
        print('i am c')

class D(C):




c = C()
c.A()
c.B()
c.C()