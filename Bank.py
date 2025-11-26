

class Account:
    def __init__(self,owner,opening_balance,acc_num):
        self.owner = owner
        self.opening_balance = opening_balance
        self.acc_num = acc_num
        self.balance = opening_balance

    def deposit(self,amt):
        self.balance += amt

    def withdraw(self,amt):
        if self.balance >= amt:
            self.balance -= amt
        else:print(f'Not enough balance of {amt}')

    def get_balance(self):
        print(f'Your balance: {self.balance}')

    
    def transfer_balance(self,amt,receiver):
        if self.balance >= amt:
            self.balance -= amt
            receiver.balance += amt
        else:print(f'Not enough balance of {amt}')
        
        
class SavingsAccount(Account):
    def __init__(self, owner, opening_balance, acc_num):
        super().__init__(owner, opening_balance, acc_num)
        self.balance = opening_balance

    def apply_interest(self,interest):
        try :
            self.balance += (self.balance*interest)/100
        except TypeError: print(f'{interest} is not a interest.')
        
class CheckingAccount(Account):
    def __init__(self, owner, opening_balance, acc_num):
        super().__init__(owner, opening_balance, acc_num)

    def withdraw(self, amt):
        if (self.opening_balance - amt) >= (-2000):
            self.balance -= amt
        else:print(f'Overdraft limit reached')

a1 = Account('x',1000,1234)
a2 = Account('y',1000,5678)
a3 = CheckingAccount('z',2000,9803)

a1.get_balance()
a2.get_balance()
a3.get_balance()


    




        