price = float(input("Enter the purchase price (up to $1.00): "))

if 0 <= price <= 1.00:
    change = round(100 - price * 100)  
    print("Your change is:")

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    if quarters:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")
else:
    print("Invalid input. Please enter a price between $0.00 and $1.00.")