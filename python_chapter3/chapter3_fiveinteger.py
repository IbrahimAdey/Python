number = int(input("Enter a five-digit integer: "))

if 10000 <= number <= 99999:
    divisor = 10000  # Start from the leftmost digit
    print("Digits:")
    for _ in range(5):
        digit = number // divisor  
        print(digit, end='  ')     
        number %= divisor          
        divisor //= 10            
else:
    print("Please enter a valid five-digit integer.")