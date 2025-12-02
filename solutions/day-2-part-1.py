
res = 0
ranges = input().split(',')

for i in range(len(ranges)):
    start, end = map(int, ranges[i].split('-'))
    
    for num in range(start, end + 1):
        cur = str(num)
        i = len(cur) // 2
        
        if cur[:i] == cur[i:]:
            res += num

print(res)

# Done!
