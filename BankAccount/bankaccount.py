class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
        return self

ba1 = BankAccount(balance=500, int_rate=.01)
ba2 = BankAccount(balance=2000, int_rate=.02)

ba1.deposit(200).deposit(100).deposit(75).withdraw(250).yield_interest().display_account_info()

ba2.deposit(150).deposit(500).withdraw(75).withdraw(200).withdraw(310).withdraw(10).yield_interest().display_account_info()

