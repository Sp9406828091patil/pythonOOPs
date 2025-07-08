# Write a BankAccount class with a private balance. 
# Provide deposit(), withdraw(), and get_balance() methods. 
# Prevent direct access to the balance.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount deposited. Your current balance is : {self.__balance}")

    def withdrawl(self, amount):
        self.__balance -= amount
        print(f"Amount withdrawl. Your current balance is : {self.__balance}")

    def get_balance(self):
        print(f"Your current balance is : {self.__balance}")

bankAccount = BankAccount(100)
bankAccount.deposit(200)
bankAccount.withdrawl(50)
bankAccount.get_balance()