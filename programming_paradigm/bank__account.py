class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited amount: {amount} to account. New balance is {self.account_balance}."
        else:
            return "Deposit amount must be more than zero."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            return False

    def display_balance(self):
        print(f"Current account balance is: {self.account_balance} ")
