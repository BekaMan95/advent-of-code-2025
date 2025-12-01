import sys

res, pos = 0, 50

for line in sys.stdin:
    # Process each input line by line
    line = line.strip()

    if not line:
        break

    direction, value = line[0], int(line[1:]) % 100

    if direction == 'L':
        pos -= value
        if pos < 0:
            pos = 100 + pos
    else:
        pos = (pos + value) % 100
    
    if pos == 0:
        res += 1

print(res)

# Done!
