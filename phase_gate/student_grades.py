def get_student_grades(prompt):
    while True:
        try:
            score = int(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

subjects = []
for i in range(num_subjects):
    name = input(f"Enter subject {i + 1} name: ")
    subjects.append(name)

students = []
for i in range(num_students):
    student_name = input(f"Enter name of student {i + 1}: ")
    scores = {}
    for subject in subjects:
        score = get_student_grades(f"Enter {student_name}'s score in {subject}: ")
        scores[subject] = score
    students.append({"name": student_name, "scores": scores})

pass_count = {sub: 0 for sub in subjects}
fail_count = {sub: 0 for sub in subjects}
totals = {}

for student in students:
    total = 0
    for sub in subjects:
        score = student["scores"][sub]
        if score >= 50:
            pass_count[sub] += 1
        else:
            fail_count[sub] += 1
        total += score
    totals[student["name"]] = total

best_subject = max(pass_count, key=pass_count.get)
worst_subject = max(fail_count, key=fail_count.get)

best_student = max(totals, key=totals.get)
worst_student = min(totals, key=totals.get)

print("\n=== CLASS SUMMARY ===")
print("Best Subject (Most passed):", best_subject)
print("Worst Subject (Most failed):", worst_subject)
print("Best Student:", best_student, "with total:", totals[best_student])
print("Worst Student:", worst_student, "with total:", totals[worst_student])

print("\n=== All STUDENTS SUMMARY ===")
for student in students:
    print(f"{student['name']} scores: {student['scores']} Total: {totals[student['name']]}")