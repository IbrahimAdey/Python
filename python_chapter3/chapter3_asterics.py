# Pattern A
for i in range(1, 11):
    for j in range(i):
        print('*', end='')
    print()

print() 

# Pattern B
for i in range(10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

print() 

# Pattern C
for i in range(10, 0, -1):
    print(' ' * (10 - i), end='') 
    for j in range(i):
        print('*', end='')
    print()

print() 

# Pattern D
for i in range(1, 11):
    print(' ' * (10 - i), end='') 
    for j in range(i):
        print('*', end='')
    print()