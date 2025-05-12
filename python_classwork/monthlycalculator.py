"""
    Mortgage calculation using the formula:
     M = P[r(1+r)**n]/[(1+r)**n – 1]
     M is monthly payment value to be calculated
      P is the principal amount
      r is the rate
      n is the duration of the loan
     Convert annual interest rate to a monthly percentage rate
     monthly_interest_rate = (annual_interest_rate / 100) / 12
     Calculate total number of monthly payments
    number_of_payments = number * 12
"""

principal = float(input("enter the principal loan amount: "))
loanrate = float(input("enter annual interest rate: "))
loanduration = float(input("enter duration in years: "))

pmr = loanrate / 100 / 12
nm = loanduration * 12
pmr1 = pmr * (1 + pmr)**loanduration
pmr2 = (1 + pmr)**loanduration
pmr3 = pmr2 - 1
mp = principal * pmr1 /pmr3
print("Your monthly payment is: $ %.2f" %mp)