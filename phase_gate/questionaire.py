import random
import time

score = 0
total_questions = 10
total_answers = 10
total_correct = 10


for i in range(1, total_questions + 1):
	a = true
	b = false

	quetion1 = What is 1 + 1 = 2 ? 
	answer1 = (a)True (b)false 
	correct1 = (a)True

	quetion2 = What is 1 + 4 = 5 ? 
	answer2 = (a)True (b)false 
	correct2 = (a)True

	quetion3 = What is 11 + 11 = 1111 ? 
	answer3 = (a)True (b)false 
	correct3 = (b)false

	quetion4 = What is 1 * 1 = 2 ? ;
	answer4 = (a)True (b)false 
	correct4 = (b)false

	quetion5 = What is 1 * 0 = 10 ? 
	answer5 = (a)True (b)false 
	correct5 = (b)false

	quetion6 = What is 11 * 1 = 11 ? 
	answer6 = (a)True (b)false 
	correct6 = (a)True

	quetion7 = What is 1 / 1 = 0 ? 
	answer7 = (a)True (b)false 
	correct7 = (b)false

	quetion8 = What is 10 + 12 = 22? 
	answer8 = (a)True (b)false 
	correct8 = (a)True

	quetion9 = What is 10 + 3 = 13 ? 
	answer9 = (a)True (b)false 
	correct9 = (a)True

	quetion10 = What is 1 - 1 = 0 ? 
	answer10 = (a)True (b)false 
	correct10 = (a)True

	question = random.randint(1, 10)
	print(f"Question {i}: What is {question1}?")
	print(f"Answer {i}: Choose {answer1}?")

	for attempt in range(1, 3):
		try:
			answer = int(input(f"Attempt {attempt}: "))
		except ValueError:
			print("Please enter a valid number.")
		continue

	if answer == correct_answer:
		print("Correct!\n")
		answer += 1
		break
	else:
		print("Incorrect.")

	else:
		print(f"The correct answer was: {correct_answer}\n")

print("Quiz Completed!")
print(f"Your final score: {score}/{total_questions}")
