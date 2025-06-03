def __init__(self):
	self.balance = 0
	withdrawal_fee = 100 

def deposit(self, amount):
	deposit = float(input("Amount to deposit: "))
	if amount <= 0:
		raise ValueError("Deposit amount must be positive.")
		self.balance += amount
		print('Your balance is ', self.balance)

def withdraw(self, amount):
	withdraw = float(input("Amount to withdraw: "))
	amount % 500 == 0
	if amount <= 0:
		raise ValueError("Withdrawal amount must be positive.")
	if amount > self.balance:
		raise ValueError("Insufficient funds.")
	if amount < self.balance:
		self.balance = amount - (withdrawal_fee + withdraw)
		print(float("Transaction succesful!"))
		print(float("Amount withdraw: ", withdraw))
		print(float("Withdrawal fee: N100"))
		print(float("Remaining balance: ", self.balance))

amount_deposit = float(input("Amount to deposit: "))
deposit(self.deposit)

amount_withdraw = float(input("Amount to withdraw: "))
withdraw(amount_withdraw)

