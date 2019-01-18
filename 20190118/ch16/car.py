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


class Employee:
    '''Common base class for all emplotees'''

    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
        self.empCount = 3

    def displayCount(self):
        print('Total Employee %d'%Employee.empCount)

    def displayEmployee(self):
        print('Name : ',self.name,' , Salary : ',self.salary)

    @classmethod
    def countOneEmployee(cls):
        cls.empCount += 1
        print('employee +1')



emp1 = Employee('Zara',2000)
emp1.displayCount()
emp2 = Employee('Manni',5000)
emp2.displayCount()
emp1.displayCount()
emp1.countOneEmployee()
emp2.displayCount()
emp1.displayCount()


