class Account:
    def __init__(self):
        self.balance = 0

    def withdraw(self):
        print('Account withdraw')

    def deposit(self, amount):
        self.balance += amount


oba = Account()
print(oba.balance)
oba.deposit(1500)
print(oba.balance)
