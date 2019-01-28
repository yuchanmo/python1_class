class Car:

    wheels = 4

    def __init__(self,make,model):
        self.make = make
        self.model = model

mustang = Car('Ford','Mustang')
porsche = Car('Porche','Camaro')
print(mustang.wheels)
print(porsche.wheels)
porsche.wheels = 5
print(mustang.wheels)
print(porsche.wheels)
print(Car.wheels)

class A:
    def foo(self):
        print('executing foo')

    @classmethod
    def class_foo(cls):
        print('excecuting class_foo')

a=  A()
a.foo()
A.class_foo()
A.foo()
a.class_foo()



