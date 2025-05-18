def product(number1 , number2):
	result = 0

	for i in range (number2):
		
		result = result + number1

	return result

digit1 = int(input("Enter a number: "))
digit2 = int(input("Enter a number: "))


print(product(digit1 , digit2))