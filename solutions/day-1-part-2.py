import sys

res, pos = 0, 50

for line in sys.stdin:
    # Process each input line by line
    line = line.strip()

    if not line:
        break

    direction, value = line[0], int(line[1:])

    passed = value // 100

    value %= 100

    if direction == 'L':
        if pos and pos - value < 0:
            passed += 1
        
        pos -= value
        
        if pos < 0:
            pos = 100 + pos
    else:
        if pos and pos + value > 100:
            passed += 1
        
        pos = (pos + value) % 100
    
    if pos == 0:
        res += 1
    
    res += passed

print(res)

# Done!
