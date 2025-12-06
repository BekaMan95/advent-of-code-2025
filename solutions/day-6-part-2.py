
def helper(arr: list, op: str):
    if op == "*":
        while len(arr) > 1:
            arr.append(arr.pop() * arr.pop())
    else:
        while len(arr) > 1:
            arr.append(arr.pop() + arr.pop())
    
    return arr.pop()


res, grid, cols = 0, list(), 0

while True:
    line = input()
    cols = max(cols, len(line))

    if not line.strip():
        break

    grid.append(line)
    

rows,  nums = len(grid), list()

for c in range(cols - 1, -1, -1):
    s = ""
    for r in range(rows):
        if grid[r][c] in ("*", "+"):
            if s:
                nums.append(int(s))
                s = ""
            
            res += helper(nums, grid[r][c])
        elif grid[r][c] != " ":
            s += grid[r][c]
    
    if s:
        nums.append(int(s))


print(res)

# Done!
