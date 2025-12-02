
res = 0
ranges = input().split(',')

for i in range(len(ranges)):
    start, end = map(int, ranges[i].split('-'))
    
    for num in range(start, end + 1):
        pfx, cur = "", str(num)
        
        for c in cur[:-1]:
            pfx += c

            if pfx * (len(cur) // len(pfx)) == cur:
                res += num
                break

print(res)

# Done!
