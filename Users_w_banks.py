class BankAccount:
    def __init__(self, acc, int_rate=0.02, balance=0):
        self.ID = acc
        self.interest = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.ID} balance: {self.account_balance} interest yield: {self.yield_interest()}")
    def yield_interest(self):
        if self.account_balance > 0:
            interest_yield = self.account_balance * self.interest
            self.account_balance += interest_yield
        return interest_yield

class User:
    def __init__(self, username, email_address):
        self.ID = username			
        self.email = email_address
    def inst_deposit(self, amount):
        self.account_balance.deposit(100)
        return self
    def inst_withdrawal(self, amount):
        self.account_balance.withdraw(40)
        return self
    def display_user_info(self):
        print .display_user_balance()


George = BankAccount(1, 0.02, 723)
Devon = BankAccount(2, 0.02, 324)

George=User("g.cec99", "george@nomail.com")

George.display_user_info()

