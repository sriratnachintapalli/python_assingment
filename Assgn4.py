class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def check_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
            return f"Transferred ${amount} to {other_account.owner}. New balance: ${self.balance}"
        else:
            return "Invalid transfer amount or insufficient funds."

# Create two BankAccount objects
account1 = BankAccount("Sri", 1000)
account2 = BankAccount("Jhanu", 500)

# Deposit, withdraw, and check balances for account1
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.check_balance())

# Deposit, withdraw, and check balances for account2
print(account2.deposit(300))
print(account2.withdraw(700))
print(account2.check_balance())

# Transfer money from account1 to account2
print(account1.transfer(account2, 300))

# Check balances after the transfer
print(account1.check_balance())
print(account2.check_balance())

