initial_population = 8_200_000_000  # 8.2 billion
growth_rate = 0.009  # 0.9%

double_population = initial_population * 2
quadruple_population = initial_population * 4

year_double = None
year_quadruple = None

population = initial_population

print(f"{'Year':>4} {'Population':>20} {'Annual Increase':>20}")

for year in range(1, 101):
    # Calculate annual increase
    increase = population * growth_rate
    # Update population
    population += increase

    # Check for doubling
    if not year_double and population >= double_population:
        year_double = year
    # Check for quadrupling
    if not year_quadruple and population >= quadruple_population:
        year_quadruple = year

    # Display the year, population, and annual increase
    print(f"{year:>4} {int(population):>20,} {int(increase):>20,}")

# Display the years when population doubles and quadruples
if year_double:
    print(f"\nThe population is expected to double in {year_double} years.")
else:
    print("\nThe population is not expected to double within 100 years.")

if year_quadruple:
    print(f"The population is expected to quadruple in {year_quadruple} years.")
else:
    print("The population is not expected to quadruple within 100 years.")