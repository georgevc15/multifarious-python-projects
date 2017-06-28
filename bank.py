class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self,amount):
        self.balance += amount

    def widraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -=amount
        else:
            print("Sorry not enough funds!")

    def statement(self):
        print("Accoount Balance: £{}".format(self.balance))


class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance =- 1000)

    def __str__(self):
        return "{} Current Account: Balance £{}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = 0)

    def __str__(self):
        return "{} Savings Account: Balance £{}".format(self.name, self.balance)



    
    
