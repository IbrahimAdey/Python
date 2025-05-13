# Print the table header
print("   Multiplication Table")
print("    ", end="")
for i in range(1, 10):
    print(f"{i:>3}", end="")
print("\n    " + "-" * 27)

# Print the table rows
for i in range(1, 10):
    print(f"{i:<2} |", end="")
    for j in range(1, 10):
        print(f"{i * j:>3}", end="") 
    print() 