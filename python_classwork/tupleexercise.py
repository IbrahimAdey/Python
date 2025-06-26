def unpack_collection(collection):
    result = [0, 0, 0, 0]
    for index in range(4):
        result[index] += collection[index]
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(unpack_collection(my_list))
print('=' * 30)

def unpacking_collection(numbers):
    first_number, second_number, third_number, *rest = numbers
    return first_number, second_number, third_number, rest

print(unpacking_collection(my_list))
print('=' * 30)

def slice_collection(numbers):
    return numbers[0: 8 : 2]
print(slice_collection(my_list))
print('=' * 30)

def sort_collection(numbers):
    numbers.sort(reverse=True)
    return numbers
print(sort_collection(my_list))
print('=' * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def isodd(number):
    return number % 2 == 1
print(isodd(1))
print('=' * 30)

filter_value = list(filter(isodd, numbers))
print(filter_value)
print('=' * 30)

def filter_collection(collection):
    return list(filter(isodd, collection))

print(filter_collection(my_list))
print('=' * 30)

def filter_with_lamda(collection):
    return list(filter(lambda number: number % 2 == 1, collection))
print(filter_with_lamda(my_list))
print('=' * 30)

def sum_collection(collection):
    sum_all_numbers = sum(map(lambda number: number + number, collection))
    return sum_all_numbers

print(sum_collection([2, 3, 4]))





