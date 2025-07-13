def fahrenheit(celsius):
    return (9 / 5) * celsius + 32

print(f"{'Celsius':>7} | {'Fahrenheit':>10}")
print('-' * 21)

for c in range(0, 101):
    f = fahrenheit(c)
    print(f"{c:7.1f} | {f:10.1f}")
