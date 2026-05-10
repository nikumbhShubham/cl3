import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        # Emit word and count 1
        print(f"{word.lower()}\t1")
