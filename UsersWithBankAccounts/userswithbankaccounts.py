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
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

u1 = User("Alex", "alexyom24@gmail.com")

u1.make_deposit(100)
u1.display_user_balance()


