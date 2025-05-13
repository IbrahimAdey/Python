print("Pythagorean Triples (sides <= 20):")
for side1 in range(1, 21):
    for side2 in range(side1, 21):  # Avoid duplicate pairs like (3,4) and (4,3)
        for hypotenuse in range(side2, 21): 
            if side1*2 + side2*2 == hypotenuse*2:
                print(f"{side1}, {side2}, {hypotenuse}")
