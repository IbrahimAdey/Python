number1 = int(input('Enter first integer:'))
number2 = int(input('Enter second integer:'))
number3 = int(input('Enter third integer:')) 

sum = number1 + number2 + number3
print('The sum of the integers is', sum)

average = sum / 3
print('The average of the integers is', average)

product = number1 * number2 * number3
print('The product of the integers is', product)

smallest = min(number1,number2,number3)
print('The smallest integer is', smallest)

largest = max(number1,number2,number3)
print('The largest integer is', largest)