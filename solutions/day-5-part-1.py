import sys


res, intervals, nums = 0, list(), list()

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

    nums.append(int(line))


intervals.sort()
order = list()
s, e = intervals[0]

for start, end in intervals:
    if start <= e:
        e = max(e, end)
    else:
        order.append((s, e))
        s, e = start, end

order.append((s, e))

for num in nums:
    for start, end in order:
        if start <= num <= end:
            res += 1
            break

print(res)

# Done!
