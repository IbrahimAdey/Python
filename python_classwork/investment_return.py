investment_amount = int(input('Enter investment amount: '))
number_of_years = int(input('Enter the number of years: '))
interest_rate = int(input('Enter interest rate: '))

rate = interest_rate / 100

for number_of_years in range(0,number_of_years,1):
	investment_interest = investment_amount * rate
	investment_return = investment_amount + investment_interest
	print(f"The investment return for year {number_of_years + 1} is {investment_return:,.2f}")
	investment_amount = investment_return