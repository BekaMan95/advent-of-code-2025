from collections import defaultdict



res, cols = 0, defaultdict(list)

while True:
    line = [s for s in input().strip().split(" ") if s]

    if not line:
        break

    for i, val in enumerate(line):
        cols[i].append(val)
    
for c in cols:
    sign = cols[c].pop()
    if sign == "*":
        cur = int(cols[c].pop())

        while cols[c]:
            cur *= int(cols[c].pop())
    elif sign == "+":
        cur = sum([int(s) for s in cols[c]])
    else:
        raise ValueError("Unknown sign:", sign)
        
    res += cur


print(res)

# Done!
