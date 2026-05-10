import sys

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()
    # For every character in the line
    for char in line:
        # Emit: character <tab> 1
        print(f"{char}\t1")
