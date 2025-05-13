num_students = int(input("Enter the number of students: "))
highest_score = -1
second_highest_score = -1
top_student = ""
second_top_student = ""

for _ in range(num_students):
    name = input("Enter student's name: ")
    score = float(input("Enter student's score: "))
    
    if score > highest_score:
        second_highest_score = highest_score
        second_top_student = top_student
        highest_score = score
        top_student = name
    elif score > second_highest_score:
        second_highest_score = score
        second_top_student = name

print(f"The student with the highest score is {top_student} with a score of {highest_score}.")
print(f"The student with the second-highest score is {second_top_student} with a score of {second_highest_score}.")