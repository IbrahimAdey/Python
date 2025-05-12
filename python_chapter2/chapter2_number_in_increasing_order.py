a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

print("\nNumbers in increasing order:")

if a <= b and b <= c:
    print(a, b, c)
elif a <= c and c <= b:
    print(a, c, b)
elif b <= a and a <= c:
    print(b, a, c)
elif b <= c and c <= a:
    print(b, c, a)
elif c <= a and a <= b:
    print(c, a, b)
elif c <= b and b <= a:
    print(c, b, a)