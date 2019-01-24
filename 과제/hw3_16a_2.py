
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

    def equals(self,predicate = False):        
        
        if len(self.tmp)!=0:
            self.tmp = self.tmp + ' = ' + str(self.balance)
            self.history.append(self.tmp)
            self.tmp = ''
        if predicate:            
            print(self.balance)
        self.balance = 0
            
    
    def showHistory(self):
        if self.history == []:
            print('No calculation done yet!')
            print('History:')
        else:
            print('History:')
            list(map(print,self.history))


c = Calculator()
c.equals()
c.showHistory()
c.add(2)
c.substract(1)
c.equals()
c.showHistory()

c.add(2)
c.multiply(4)
c.equals(True)

c.add(10)
c.substract(5)
c.multiply(2)
c.equals()

c.showHistory()