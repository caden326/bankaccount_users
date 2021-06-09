class Bankaccount:
    def __init__(self,int_rate, balance): #parameters
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        print("\n Deposited:", amount)
    
    def withdraw(self, amount):
        # amount = float(input())
        if self.balance >= amount:
            self.balance -= amount
            print("\n Withdrew:", amount)
        else:
            print("\n You're Broke  ")
    
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
    

    def yield_interest(self):
        self.balance += self.balance * self.int_rate 


class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate=0.03, balance=100)
    def makedeposit(self,amount):
        self.account.balance += amount
        print('accout balance is',self.account.balance)
        return self
    def makewithdraw(self,amount):
        self.account.balance -= amount
        print('accout balance is',self.account.balance)
        return self
    def seeaccountbalance(self):
        print('accout balance is',self.account.balance)
        return self

george = User ('George', 'coolguy@yagoo.com')
george.makedeposit(100)
george.makewithdraw(20)
george.seeaccountbalance()



