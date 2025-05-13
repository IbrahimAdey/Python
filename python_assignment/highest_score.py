num_students = int(input("Enter the number of students: "))
highest_score = -1
top_student = ""

for _ in range(num_students):
    name = input("Enter student's name: ")
    score = float(input("Enter student's score: "))
    
    if score > highest_score:
        highest_score = score
        top_student = name

print(f"The student with the highest score is {top_student} with a score of {highest_score}.")