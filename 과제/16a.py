from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Pythagoras:
    '''Implement the Pythagoras Class'''
    def __init__(self):
        pass

    def setPointOne(self,p1):
        self.point1 = p1
    
    def setPointTwo(self,p2):
        self.point2 = p2

    def getSlope(self):
        
        
        assert self.point1 != None and self.point2 != None
        try:
            return (self.point2.y - self.point1.y) / (self.point2.x - self.point1.x)
        except ZeroDivisionError as ze:
            print('x values of both point1 and point2 are same')
        

    def getDistance(self):
        xskewpow = (self.point2.x - self.point1.x)**2
        yskewpow = (self.point2.y - self.point1.y)**2
        return sqrt(xskewpow + yskewpow)

    
p1 = Point(0,0)
p2 = Point(1,3)

ps = Pythagoras()
ps.setPointOne(p1)
ps.setPointTwo(p2)

ps.getDistance()
ps.getSlope()


class Calculator:    

    def __init__(self):
        self.balance = 0
        self.history = []
        self.tmp = ''
           

    def add(self,val):
        self.tmp = str(val) if len(self.tmp) == 0 else self.tmp + ' + ' + str(val)
        self.balance = self.balance + val

    def substract(self,val):        
        self.tmp = str(val) if len(self.tmp) == 0 else self.tmp + ' - ' + str(val)
        self.balance = self.balance - val

    def multiply(self,val):        
        self.tmp = str(val) if len(self.tmp) == 0 else self.tmp + ' * ' + str(val)
        self.balance = self.balance * val

    def equal(self,predicate = False):        
        self.tmp = self.tmp + ' = ' + str(self.balance)
        self.history.append(self.tmp)
        self.tmp = ''
        if predicate:            
            print(self.balance)
        self.balance = 0
            
    
    def show_history(self):
        if self.history == []:
            print('No calculation done yet!')
            print('History:')
        else:
            list(map(print,self.history))


c = Calculator()
c.add(2)
c.substract(1)
c.equal()
c.show_history()

c.add(2)
c.multiply(4)
c.equal(True)

c.add(10)
c.substract(5)
c.multiply(2)
c.equal()

c.show_history()
        
        
class Account:

    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
        self.tranactions = []

    def __saveHistory(self,action,amount):
        self.tranactions.append((action,amount))

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.__saveHistory('deposit',amount)

    def withdraws(self,amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance = self.balance - amount
            self.__saveHistory('withdraws',amount)

    def status(self):
        print(self.holder + ' : ',end ='')
        print(self.tranactions)

bob = Account('Bob')
bob.deposit(1000000)
bob.withdraws(100)
bob.deposit(440)
bob.status()

tom = Account('Tom')
tom.deposit(5000000)
tom.withdraws(250)
tom.withdraws(875)
tom.status()


class Atom(object):
    __Atno_to_Symbol = {1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O'}
    def __init__(self,atno,x,y,z):
        self.atno = atno
        self.position = (x,y,z)

    def symbol(self):
        return self.__Atno_to_Symbol[self.atno]

    def __repr__(self):
        return '%d %10.4f %10.4f %10.4f' %(self.atno,self.position[0],
                self.position[1],self.position[2])


class Molecule:

    def __init__(self,name = 'Generic'):
        self.name = name
        self.atomlist = []

    def addAtom(self,atom):
        self.atomlist.append(atom)

    def __repr__(self):
        s = 'This is a molecule names %s\n' %(self.name)
        s = s + 'It has %d atoms \n'%(len(self.atomlist))
        for atom in self.atomlist:
            s = s + '%s\n '%atom
        return s

at = Atom(6,0.0,1.0,2.0)
print(at)
at.symbol()

#Atom : 원자 (원자 번호, x,y,z) 정보 출력
#해당 원자의 기호(dictionary key 값 참조) 출력

mol = Molecule('Water')
at = Atom(8,0.,0.,0.)
mol.addAtom(at)
mol.addAtom(Atom(1,0.,0.,1.))
mol.addAtom(Atom(1,0.,0.,0.))
print(mol)

#분자정보 입력(물), 어떤 원자로 이루어져있는지 정보 입력후 출력


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
        self.salary = (100 + percent)*0.01*self.salary
        return self.salary


tim_cook = Professor('Tim Cook','CSE','Soft. Arch',5500)
total_salary = 0
for i in range(5):
    total_salary += tim_cook.salary
    #tim_cook.raiseSalary(15)
print(total_salary)

total_salary_if_salary_is_raised = 0
for i in range(5):
    tim_cook.raiseSalary(15)
    total_salary_if_salary_is_raised += tim_cook.salary
print(total_salary_if_salary_is_raised)


class SPerson:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address 

    

class Student(SPerson):
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

    


class Staff(SPerson):
    def __init__(self, name, address,school,pay):        
        super().__init__(name, address)
        self.school = school
        self.annualpay = pay

    def getMonthlyPay(self):
        return self.annualpay

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

print('current status')
print(tom)
print(dane)

for i in range(1,8):
    print('after ',i,'year')
    tom.raiseAnnualPay(7)
    dane.raiseAnnualPay(15)
    print(tom)
    print(dane)




