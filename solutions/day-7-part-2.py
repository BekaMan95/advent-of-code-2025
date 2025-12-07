

def dfs(r: int, c: int):
    if r == rows:
        return 1
    
    if (r, c) not in cache:
        if c in tree[r]:
            cache[(r, c)] = dfs(r + 1, c)
        else:
            cache[(r, c)] = dfs(r + 1, c - 1) + dfs(r + 1, c + 1)

    return cache[(r, c)]


grid = list()

while True:
    line = input()

    if not line.strip():
        break

    grid.append(line)
    

rows, cols = len(grid), len(grid[0])
col, tree, beams = 0, list(), set()

for i in range(cols):
    if grid[0][i] == "S":
        beams.add(i)
        tree.append({i})
        col = i


for r in range(1, rows):
    prev_row = beams.copy()
    for c in range(cols):
        if grid[r][c] == "^" and c in beams:
            prev_row.remove(c)

            if 0 <= c - 1 < cols:
                prev_row.add(c - 1)
            
            if 0 <= c + 1 < cols:
                prev_row.add(c + 1)
    
    beams = prev_row
    tree.append(beams.copy())

cache = dict()
res = dfs(0, col)

print(res) if res else print(1)

# Done!
