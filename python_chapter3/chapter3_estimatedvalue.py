def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

e_estimate = 0

for n in range(11): 
    e_estimate += 1 / factorial(n)

print(f"Estimated value of e after 10 terms: {e_estimate:.10f}")