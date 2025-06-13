questions = [
     "A. Expand energy, enjoy groups\nB. Conserve energy, enjoy one-on-one",
     "A. Interpret literally\nB. Look for meaning and possibilities",
     "A. Logical, thinking, questioning\nB. Empathetic, feeling, accomodating",
     "A. Organized, orderly\nB. Flexible, adaptable",
     "A. More outgoing\nB. More reserved",
     "A. Focus on the now\nB. Focus on the future",
     "A. Value justice\nB. Value compassion",
     "A. Prefer a plan\nB. Go with the flow",
     "A. Enjoy crowds\nB. Enjoy solitude",
     "A. Trust experience\nB. Trust intuition",
     "A. Firm\nB.  Gentle",
     "A. Regulated, structured\nB. easy-going, live and let live",
     "A. External, communicative\nB. Internal, keep to youself",
     "A. Focus on here-and-now\nB. Look to the future",
     "A. Tough-minded, just\nB. Tender-hearted, merciful",
     "A. Preparation, plan ahead\nB. Go with the flow, adapt as you go",
     "A. Active, initiate\nB.Reflective, delibrate",
     "A. Facts, things\nB. Ideas, dreams, philosophical",
     "A. Matter of fact, issue-oriented\nB. Sensitive, people-oriented",
     "A. Control, govern\nB. Latitude, freedom",
]

scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

for i in range(20):
    while True:
        print(f"\nQuestion {i + 1}")
        print(questions[i])
        answer = input("Choose A or B: ").strip().upper()
        if answer in ["A", "B"]:
            break
        print("Invalid! Please type A or B only.")

    if i % 4 == 0: 
        scores["E" if answer == "A" else "I"] += 1
    elif i % 4 == 1:  
        scores["S" if answer == "A" else "N"] += 1
    elif i % 4 == 2: 
        scores["T" if answer == "A" else "F"] += 1
    else: 
        scores["J" if answer == "A" else "P"] += 1

mbti = ""
mbti += "E" if scores["E"] >= scores["I"] else "I"
mbti += "S" if scores["S"] >= scores["N"] else "N"
mbti += "T" if scores["T"] >= scores["F"] else "F"
mbti += "J" if scores["J"] >= scores["P"] else "P"

print("\nYour MBTI personality type is:", mbti)