class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

alex = User("Alex", "alexyom24@gmail.com")
jeff = User("Jeff", "jeff@gmail.com")
mike = User("Mike", "mike@gmail.com")

alex.make_deposit(100).make_deposit(350).make_deposit(220).make_withdrawal(75).display_user_balance()

jeff.make_deposit(250).make_deposit(40).make_withdrawal(22).make_withdrawal(15).display_user_balance()

mike.make_deposit(500).make_withdrawal(75).make_withdrawal(15).make_withdrawal(200).display_user_balance()

alex.transfer_money(jeff,75)
alex.display_user_balance()
jeff.display_user_balance()
