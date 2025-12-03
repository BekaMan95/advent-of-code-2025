import sys

res = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    cur, n = 0, len(line)

    for i in range(n - 1):
        for j in range(i + 1, n):
            cur = max(cur, int(line[i] + line[j]))
    
    res += cur

print(res)

# Done!
