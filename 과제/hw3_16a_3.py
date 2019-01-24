        
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
            self.__saveHistory('withdrawl',amount)

    def status(self):
        print(self.holder + ' : ',end ='')
        print(self.tranactions)

def main():        
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

main()