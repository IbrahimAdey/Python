import random

def generate_question():
	num1 = random.randint(1, 9)
	num2 = random.randint(1, 9)
	return num1, num2

correct_responses = [
    "Very good!"
]

incorrect_responses = [
    "Wrong. Try once more."
]

while True:
	x, y = generate_question()
	x > y
	correct_answer = x - y
for correct_answer in range(1, 11):
    
	while True:
		user_input = int(input(f"What is {x} minus {y}? "))
        
		if user_input == correct_answer:
			print(random.choice(correct_responses) + "\n")
			break 
		else:
			print(random.choice(incorrect_responses))
	
for incorrect_answer in range(1, 3):
	user_input = int(input(f"What is {x} minus {y}? "))
 

sum = correct_answers

print(sum)