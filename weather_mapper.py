import sys

# The Mapper's job is to extract Year and Temperature from raw data.
for line in sys.stdin:
    # Clean the line
    line = line.strip()
    if not line:
        continue
    
    # Simple Format: Year <space> Temperature
    # In real weather data (NCDC), you often use line[start:end] slicing.
    parts = line.split()
    if len(parts) >= 2:
        year = parts[0]
        temp = parts[1]
        # Emit the Key (Year) and Value (Temp)
        print(f"{year}\t{temp}")
