class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

alex = User("Alex", "alexyom24@gmail.com")
jeff = User("Jeff", "jeff@gmail.com")
mike = User("Mike", "mike@gmail.com")

alex.make_deposit(100)
alex.make_deposit(350)
alex.make_deposit(220)
alex.make_withdrawal(75)
print("Alex's account balance is:") 
alex.display_user_balance()

jeff.make_deposit(250)
jeff.make_deposit(40)
jeff.make_withdrawal(22)
jeff.make_withdrawal(15)
print("Jeff's account balance is:") 
jeff.display_user_balance()

mike.make_deposit(500)
mike.make_withdrawal(75)
mike.make_withdrawal(15)
mike.make_withdrawal(200)
# mike.display_user_balance()

alex.transfer_money(jeff,75)
alex.display_user_balance()
jeff.display_user_balance()
