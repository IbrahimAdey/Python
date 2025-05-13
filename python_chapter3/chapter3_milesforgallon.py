total_miles = 0
total_gallons = 0

while True:
    miles = input("Enter miles driven (-1 to quit): ")
    if miles == "-1":
        break

    gallons = input("Enter gallons used: ")
    
    try:
        miles = float(miles)
        gallons = float(gallons)
        
        if gallons == 0:
            print("Gallons used cannot be zero. Try again.")
            continue

        mpg = miles / gallons
        print(f"Miles per gallon for this tankful: {mpg:.2f}")
        
        total_miles += miles
        total_gallons += gallons

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if total_gallons > 0:
    combined_mpg = total_miles / total_gallons
    print(f"\nCombined miles per gallon for all tankfuls: {combined_mpg:.2f}")
else:
    print("\nNo valid data entered.")