import random

list = []

def create_list():
    num_one = random.randint(1, 50)
    for i in range(10):
     list.append(random.randint(1, 50))

create_list()
print(list)
print('==' * 30)

def sumAllEvenElements(list):
    sum = 0
    for num in range(0, len(list), 2):
        sum += list[num]
    print("Even sum: ", sum)
    print('==' * 30)

def sumOddElements(list):
    sum = 0
    for num in range(1, len(list), 2):
        sum += list[num]
    print("Odd sum: ", sum)
    print('==' * 30)


sumAllEvenElements(list)

sumOddElements(list)

