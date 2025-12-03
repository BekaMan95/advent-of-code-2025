import sys

def helper(start: int, end: int) -> tuple:
    s, pos = line[start], start
    
    for k in range(start, end + 1):
        if line[k] > s:
            s, pos = line[k], k

    return (s, pos)

res = 0
x, y = 0, 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    x, y = max(x, len(line)),y + 1

    cur, n, idx, digit = "", len(line), 0, 12

    for _ in range(digit):
        c, idx = helper(idx, n - digit)
        cur += c
        idx += 1
        digit -= 1
    
    res += int(cur)

print(res, x, y)

# Done!
