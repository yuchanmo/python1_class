
class Person:
    pass

class Employee(Person):
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

    def __add__(self,other):
        print(self.name, 'loves',other.name)

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

emp1 + emp2

print("__doc__",Employee.__doc__)
print('__name__',Employee.__name__)
print('__module__',Employee.__module__)
print('__bases__',Employee.__base__)
print('__dict__',Employee.__dict__)

for i,v in Employee.__dict__.items():
    print(i)
    print(type(v))
    if type(v) == 'function':
        v()

