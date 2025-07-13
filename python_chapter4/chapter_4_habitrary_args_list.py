product(2, 3)
product(4, 5, 6)
product(1, 2, 3, 4, 5)

def product(*args):
    result = 1 
    for number in args:
        result *= number
    return result
