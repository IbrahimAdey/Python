import statistics

data = [9, 11, 22, 34, 17, 22, 34, 22, 40]
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")