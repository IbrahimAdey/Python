
number = int(input("Enter an integer between 1 and 10,000: "))

if 1 <= number <= 10000:

    digits = str(number)
    
    digit_sum = sum(int(digit) for digit in digits)
   
    print("The sum of the digits is:", digit_sum)
else:
    print("Invalid input. Please enter a number between 1 and 10,000.")

def sum_of_digit(number):
	if 1 <= number <= 10000:

    		digits = str(number)
    
    		digit_sum = sum(int(digit) for digit in digits)
   
    		return f"The sum of the digits is: {digit_sum}"
	else:
    		return "Invalid input. Please enter a number between 1 and 10,000."



print(sum_of_digit(12))
print(sum_of_digit(333))
print(sum_of_digit(4567))
print(sum_of_digit(66666))



	