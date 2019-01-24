
class Person:

    def __init__(self,name,depart):
        self.name = name
        self.depart = depart

    def getName(self):
        return self.name
    
    def getDepart(self):
        return self.depart


    
    

class Student(Person):

    __classyear = {1:'1st',2:'2nd',3:'3rd'}
    def __init__(self, name, depart,year):
        super().__init__(name, depart)
        self.credit = None
        self.year = year
    
    def getCredit(self):
        return self.credit

    def increaseYear(self):
        self.year += 1

    def getYear(self):
        if self.year in self.__classyear:
            return self.__classyear[self.year]
        else:
            return str(self.year)+'th'

    

class Professor(Person):
    def __init__(self, name, depart,course,salary):
        super().__init__(name, depart)
        self.course = course
        self.salary =salary

    def getCourse(self):
        return self.course
    
    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self,percent):
        self.salary = (100 + percent)/100*self.salary
        return self.salary

def main():
    tim_cook = Professor('Tim Cook','CSE','Soft. Arch',5500)
    total_salary = 0
    for i in range(5):
        total_salary += tim_cook.salary
        #tim_cook.raiseSalary(15)
    print('5 year salary: ',total_salary)

    total_salary_if_salary_is_raised = 0
    for i in range(5):
        tim_cook.raiseSalary(15)
        total_salary_if_salary_is_raised += tim_cook.salary
    print(r'5 year salary 15% raise : ' ,total_salary_if_salary_is_raised)

main()