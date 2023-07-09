class BankAccount:

    all_accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        return
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        yielded_amount = self.balance * self.int_rate
        self.balance = self.balance + yielded_amount
        print(self.balance)
        return self
    


account_123 = BankAccount(.01, 500)
account_456 = BankAccount(.25, 750)

account_123.deposit(100).deposit(150).deposit(250).withdraw(500)
account_456.deposit(50).deposit(700).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()

print(BankAccount.all_accounts)