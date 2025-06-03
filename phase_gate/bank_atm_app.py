from bank_atm import Bank

def main():
    bank = Bank()
    print("Welcome to Semicolon Bank ATM!")

    while True:
        print("\nOptions:")
        print("1 - Account Balance")
        print("2 - Deposit")
        print("3 - Withdraw")
	print("4 - Exit")

        choice = input("Choose option: ")

        if choice == '1':
            amount = input("Enter your account balance: ")
                
        elif choice == '2':
                amount = float(input("Amount to deposit: "))
                bank.deposit(amount)
		if amount <= 0:
			raise ValueError("Deposit amount must be positive.")
			self.balance += amount
			print('Your balance is ', self.balance)
			print("Deposit successful.")

        elif choice == '3':
                amount = float(input("Amount to withdraw: "))
                bank.withdraw(amount)
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
                	print("Withdrawal successful.")
           
                elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Please choose a valid option.")

if __name__ == "__main__":
    main()
