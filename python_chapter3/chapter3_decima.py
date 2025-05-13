binary = int(input("Enter a binary number (only 0s and 1s): "))

decimal = 0
position = 0

while binary > 0:
    digit = binary % 10
    if digit not in (0, 1):
        print("Invalid input: Not a binary number.")
        break
    decimal += digit * (2 ** position)
    position += 1
    binary //= 10
else:
    print(f"Decimal equivalent: {decimal}")