class BankAccount:
    def __init__(self, int_rate, balance): 
        self.balance = 0
        self.int_rate = .01
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print("You're remaining balance is: "+self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate

alex = BankAccount()