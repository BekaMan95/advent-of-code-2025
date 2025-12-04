import sys

def inbound(a: int, b: int) -> bool:
    return 0 <= a < rows and 0 <= b < cols

def count(r: int, c: int) -> int:
    ans = 0
    
    for nr, nc in directions:
        nr += r
        nc += c

        if inbound(nr, nc) and grid[nr][nc] == "@":
            ans += 1 

    return ans

res, grid = 0, list()
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    grid.append(line)

rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@" and count(r, c) < 4:
            res += 1

print(res)

# Done!
