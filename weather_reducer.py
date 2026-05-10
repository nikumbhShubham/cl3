import sys

current_year = None
max_temp = -float('inf')

# Variables to track the overall (Global) winners for the dataset
hottest_year = None
hottest_temp = -float('inf')
coolest_year = None
coolest_temp = float('inf')

# Hadoop/Terminal sends sorted data: e.g., 1880, 1880, 1881, 1881...
for line in sys.stdin:
    line = line.strip()
    try:
        year, temp = line.split('\t', 1)
        temp = float(temp)
    except ValueError:
        continue

    # 1. PER-YEAR LOGIC (The standard MapReduce grouping)
    if current_year == year:
        if temp > max_temp:
            max_temp = temp
    else:
        # Before switching to a new year, print the max for the previous one
        if current_year:
            print(f"Year {current_year} | Max Temp: {max_temp:8.2f}")
        
        # Reset for the new year
        current_year = year
        max_temp = temp

    # 2. GLOBAL LOGIC (To find the absolute hottest/coolest year in the whole file)
    if temp > hottest_temp:
        hottest_temp = temp
        hottest_year = year
    
    if temp < coolest_temp:
        coolest_temp = temp
        coolest_year = year

# Handle the last year in the file
if current_year:
    print(f"Year {current_year} | Max Temp: {max_temp:8.2f}")

# Final Answer according to the Problem Statement
print("\n" + "="*40)
print("   MAPREDUCE CLIMATE ANALYSIS RESULT")
print("="*40)
print(f"ABSOLUTE HOTTEST YEAR: {hottest_year} ({hottest_temp})")
print(f"ABSOLUTE COOLEST YEAR: {coolest_year} ({coolest_temp})")
print("="*40)
