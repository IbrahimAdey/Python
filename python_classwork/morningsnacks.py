num = [10, 20, 30, 40, 50]
print(num[2])
print("_" * 30)

colors = ['red', 'green', 'blue']
del colors[2]
colors.append ('yellow')
print(colors)
print("_" * 30)

colors.append('purple')
print(colors)
print("_" * 30)

digit = [1, 2, 3, 4, 5]
digit.remove(3)
print(digit)
print("_" * 30)

name = ['Alice', 'Bob', 'Charlie']
print(len(name[0]))
print(len(name[1]))
print(len(name[2]))
print("_" * 30)

nums = [4, 1, 3, 9, 2]
sorted(nums)
print(sorted(nums))
print("_" * 30)

def get_even(numbers):
    number = []
    for num in numbers:
        if num % 2 == 0:
            number.append(num)
    return number
a = get_even([1, 2, 3, 4, 5,6, 7, 8, 9, 10])
print(a)
print("_" * 30)

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print("_" * 30)

a = ["lamb", "kit", "yam", "kings", "dogs", "man"]
b = []
for word in a:
    if len(word) > 3:
        b.append(word)
print(b)
