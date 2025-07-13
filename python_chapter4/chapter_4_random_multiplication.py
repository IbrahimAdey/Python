import ten_number

def generate_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

while True:
    x, y = generate_question()
    correct_answer = x * y
    
    while True:
        user_input = int(input(f"How much is {x} times {y}? "))
        
        if user_input == correct_answer:
            print("Very good!")
            break  
        else:
            print("No. Please try again.")
