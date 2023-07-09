class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        return
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        # your code here
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        # your code here
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        # your code here
        return self
    
    def yield_interest(self):
        yielded_amount = self.balance * self.int_rate
        self.balance = self.balance + yielded_amount
        print(self.balance)
        # your code here
        return self
    


account_123 = BankAccount(.01, 500)
account_456 = BankAccount(.25, 750)

account_123.deposit(100).deposit(150).deposit(250).withdraw(500)
account_456.deposit(50).deposit(700).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()

print(BankAccount.all_accounts)