age = int(input("Enter your age in years: "))
max_heart_rate = 220 - age

target_min = max_heart_rate * 0.50
target_max = max_heart_rate * 0.85

print(f"\nYour maximum heart rate is: {max_heart_rate} beats per minute.")
print(f"Your target heart rate range is: {target_min:.1f} to {target_max:.1f} beats per minute.")

print("\n[Note: These estimates are based on AHA guidelines. "
      "Consult a healthcare professional before starting an exercise program.]")