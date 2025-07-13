import ten_number

def generate_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

correct_responses = [
    "Very good!",
    "Nice work!",
    "Keep up the good work!"
]

incorrect_responses = [
    "No. Please try again.",
    "Wrong. Try once more.",
    "No. Keep trying."
]

while True:
    x, y = generate_question()
    correct_answer = x * y
    
    while True:
        user_input = int(input(f"How much is {x} times {y}? "))
        
        if user_input == correct_answer:
            print(random.choice(correct_responses) + "\n")
            break 
        else:
            print(random.choice(incorrect_responses))
