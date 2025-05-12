print("Welcome to the Mortgage Calculator\n")

   
        principal = float(input("Enter the loan principal amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the duration of the mortgage (in years): "))

        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)

        print(f"\nMonthly Mortgage Payment: ${monthly_payment:,.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for all fields.")
