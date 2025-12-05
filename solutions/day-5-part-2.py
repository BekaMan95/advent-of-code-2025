import sys


res, intervals = 0, list()

for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    s, e = map(int, line.split("-"))
    intervals.append((s, e))

for line in sys.stdin:
    line = line.strip()

    if not line:
        break


intervals.sort()
s, e = intervals[0]

for start, end in intervals:
    if start <= e:
        e = max(e, end)
    else:
        res += e - s + 1
        s, e = start, end

res += e - s + 1

print(res)

# Done!
