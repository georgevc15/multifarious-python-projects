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
