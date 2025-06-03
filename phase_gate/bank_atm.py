class BankATM:
	def __init__(self):
		self.balance = 0
		withdrawal_fee = 100
		max_amount = 20_000 

	def deposit(self, amount):
		deposit = float(input("Amount to deposit: "))
		if amount <= 0:
			raise ValueError("Deposit amount must be positive.")
			self.balance += amount
			print('Your balance is ', self.balance)

	def withdraw(self, amount):
		withdraw = float(input("Amount to withdraw: "))
		amount % 500 == 0
		max_amount <= 20_000
		if amount <= 0:
			raise ValueError("Withdrawal amount must be positive.")
		if max_amount > 20_000 :
			raise ValueError("You cannot withdraw more than 20_000 at once.")
		if amount > self.balance:
			raise ValueError("Insufficient funds.")
		if withdraw > self.balance * 0.9:
			raise ValueError("Insufficient funds.")
		if amount < self.balance:
			self.balance = amount - (withdrawal_fee + withdraw)
			print(float("Transaction succesful!"))
			print(float("Amount withdraw: ", withdraw))
			print(float("Withdrawal fee: N100"))
			print(float("Remaining balance: ", self.balance))

	def balance(self, amount):
		print('Your balance is ', self.balance)
		

class Bank:
	def deposit(self, amount):
		account.deposit(amount)

	def withdraw(self, amount):
		account.withdraw(amount)
           
deposit = float(input("Amount to deposit: "))
print("Deposit successful.")
print("Current balance: N",deposit)
print(self.balance)
          
withdraw = float(input("Amount to withdraw: "))
Bank.withdraw(withdraw)
print("Withdrawal successful.")
       

        
