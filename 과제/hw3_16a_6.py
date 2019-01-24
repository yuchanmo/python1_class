class Person:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address 

    

class Student(Person):
    def __init__(self, name,address,year,fee):
        super().__init__(name, address)
        self.gpa = 0.0
        self.year = year
        self.fee = fee
    
    def setGpa(self,gpa):
        self.gpa = gpa
    
    def getGpa(self):
        return self.gpa

    def hasMinimumGpa(self):
        return self.gpa > 3.5

    def willGraduateNextYear(self):
        return self.year == 4

    


class Staff(Person):
    def __init__(self, name, address,school,pay):        
        super().__init__(name, address)
        self.school = school
        self.annualpay = pay

    def getMonthlyPay(self):
        return self.annualpay/12

    def raiseAnnualPay(self,percent):
        self.annualpay = (percent + 100)*0.01*self.annualpay

    def __gt__(self,other):
        largersalaryperson = self.name if self.annualpay > other.annualpay else other.name
        print('%s has a larger monthly pay'%(largersalaryperson))

    def __str__(self):
        return 'My Name is %s. I earn $%s in a year'%(self.name,self.annualpay)
    
    def getSchool(self):
        return self.school


tom = Staff('Tom','Gangnam','Yonsei',350000)
dane = Staff('Dane','Sindorim','Sogang',20000)

# print('current status')
# print(tom)
# print(dane)

for i in range(1,8):
    #print('after ',i,'year')
    tom.raiseAnnualPay(7)
    dane.raiseAnnualPay(15)
    # print(tom)
    # print(dane)

tom < dane